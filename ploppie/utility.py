from .chat import Chat
import logging
import json
from typing import Union

class Utility:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

        # Set up logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Create console handler if no handlers exist
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO if not self.kwargs.get("verbose", False) else logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
        
        # Set verbose logging if requested
        if self.kwargs.get("verbose", False):
            self.logger.setLevel(logging.DEBUG)
        
    @property
    def chat(self):
        return Chat(**self.kwargs)
    
    def selector(self, message: str, options: list, attempts: int = 3, multi_select: bool = False, min_matches: int = 1):
        """
        Prompts the LLM to select one or more options from a list of choices, returning JSON formatted response.
        
        :param message: The prompt or question to ask the LLM
        :type message: str
        :param options: List of valid options the LLM can choose from
        :type options: list
        :param attempts: Number of attempts before raising error, defaults to 3
        :type attempts: int, optional
        :param multi_select: Whether to allow the LLM to select multiple options, defaults to False
        :type multi_select: bool, optional
        :param min_matches: Minimum number of matches required to return a result, defaults to 1
        :returns: The selected option(s) that match from the options list
        :rtype: Union[str, list]
        
        :raises ValueError: If no valid selection is made within the allowed attempts
        """
        chat = self.chat
        attempt = 0

        # Calculate max tokens needed for largest option plus JSON formatting
        max_tokens = max(
            chat.token_counter([{"role": "assistant", "content": f'["{option}"]'}])
            for option in options
        )

        self.chat.kwargs["max_tokens"] = max_tokens
        self.logger.debug(f"Max tokens needed: {max_tokens}")

        while attempt < attempts:
            if attempt == 0:
                chat.system(message)

                z = "\n\n".join(options)

                if multi_select:
                    options_msg = (
                        f"You must respond with a JSON array containing at least {min_matches} of these options:\n\n{z}\n\n"
                        "Format your response as a valid JSON array of strings, for example: [\"option1\", \"option2\"]. "
                        "No additional text outside the JSON array."
                    )
                    if min_matches == 0:
                        options_msg += "\nRespond with an empty array [] if you don't find any matches."
                else:
                    options_msg = (
                        f"You must respond with a JSON array containing exactly one of these options:\n\n{z}\n\n"
                        "Format your response as a valid JSON array with a single string, for example: [\"selected_option\"]. "
                        "No additional text outside the JSON array."
                    )
                chat.system(options_msg)
                
                self.logger.debug(f"System message: {options_msg}\n\n{message}")
            
            # Get response from LLM
            responses = chat.ready()
            
            try:
                if len(responses) == 0:
                    selected_items = []
                else:
                    response = responses[0] if isinstance(responses, list) else responses
                    selected_items = json.loads(response.strip())
                    
                    if not isinstance(selected_items, list):
                        raise ValueError("Response is not a JSON array")
                    
                    selected_items = [str(item).strip().lower() for item in selected_items]
                
                matched_options = []
                for selected in selected_items:
                    # Try exact match first
                    exact_matches = [opt for opt in options if opt.lower() == selected]
                    if exact_matches:
                        matched_options.extend(exact_matches)
                        continue
                    
                    # Try partial match if no exact match found
                    partial_matches = [opt for opt in options if selected in opt.lower()]
                    if partial_matches:
                        matched_options.extend(partial_matches)
                
                if multi_select:
                    if len(matched_options) >= min_matches:
                        self.logger.debug(f"Found matches: {matched_options}")
                        return matched_options
                else:
                    if len(matched_options) == 1:
                        self.logger.debug(f"Found match: {matched_options[0]}")
                        return matched_options[0]
            
            except (json.JSONDecodeError, ValueError) as e:
                self.logger.debug(f"Failed to parse JSON response: {e}")
            
            attempt += 1
            self.logger.debug(f"Attempt {attempt} failed: {response}")
            
            # Add error message for invalid response
            chat.system(f"INVALID SELECTION! Response must be a valid JSON array. {options_msg}")
        
        raise ValueError(f"Failed to get valid selection after {attempts} attempts")
