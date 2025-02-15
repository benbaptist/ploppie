from .chat import Chat
import logging

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
    
    def selector(self, message: str, options: list, attempts: int = 3, multi_select: bool = False):
        """
        Prompts the LLM to select one option from a list of choices.
        
        :param message: The prompt or question to ask the LLM
        :type message: str
        :param options: List of valid options the LLM can choose from
        :type options: list
        :param attempts: Number of attempts before raising error, defaults to 3
        :type attempts: int, optional
        :param multi_select: Whether to allow the LLM to select multiple options, defaults to False
        :type multi_select: bool, optional
        
        :returns: The selected option that matches one from the options list
        :rtype: str
        
        :raises ValueError: If no valid selection is made within the allowed attempts
        """
        chat = self.chat
        attempt = 0

        # Calculate max tokens needed for largest option, to help 
        # increase the chance of a match
        max_tokens = max(
            chat.token_counter([{"role": "assistant", "content": option}])
            for option in options
        )

        self.chat.kwargs["max_tokens"] = max_tokens
        self.logger.debug(f"Max tokens needed: {max_tokens}")

        while attempt < attempts:
            if attempt == 0:
                # Add system message explaining the constraints
                chat.system(message)

                z = "\n\n".join(options)

                if multi_select:
                    options_msg = f"You must respond with one or more of these options, with no additional text, separated by commas: \n\n{z}"
                else:
                    options_msg = f"You must respond with exactly one of these options, with no additional text: \n\n{z}"
                chat.system(options_msg)
                
                self.logger.debug(f"System message: {options_msg}\n\n{message}")
            
            # Get response from LLM
            responses = chat.ready()
            response = responses[0] if isinstance(responses, list) else responses
            
            if multi_select:
                # Split response by commas and clean up whitespace
                selected_items = [item.strip() for item in response.lower().split(',')]
                matched_options = []
                
                # Check each selected item against options
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
                
                if matched_options:
                    self.logger.debug(f"Found matches: {matched_options}")
                    return matched_options
            else:
                # Single selection logic (existing code)
                for option in options:
                    if option.lower() == response.lower().strip():
                        self.logger.debug(f"Found exact match: {option}")
                        return option
                
                for option in options:
                    if option.lower() in response.lower():
                        self.logger.debug(f"Found option in response: {option}")
                        return option
            
            attempt += 1
            self.logger.debug(f"Attempt {attempt} failed: {response}")
            
            # Add error message for invalid response
            chat.system(f"INVALID SELECTION! {options_msg}")
        
        raise ValueError(f"Failed to get valid selection after {attempts} attempts")
