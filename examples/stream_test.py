from ploppie import Chat
import logging

# from litellm import completion
# import sys

# response = completion(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You're a helpful assistant."},
#         {"role": "user", "content": "What is the capital of France?"}
#     ],
#     stream=True
# )

# chunks = []

# for chunk in response:
#     chunks.append(chunk)
#     print(chunk.json())

# # help(chunks[0])

# sys.exit()

if __name__ == "__main__":
    # Create a Chat instance with streaming enabled
    chat = Chat(model="gpt-4o-mini", stream=True, verbose=True)

    # Set up logging to see what's happening
    logging.basicConfig(level=logging.DEBUG)

    @chat.tool("Perform mathematical calculations")
    def calculate(expression: str):
        """Evaluate a mathematical expression.
        
        Args:
            expression (str): The mathematical expression to evaluate
        """
        try:
            result = float(eval(expression))
            print(f"Calculated {expression} = {result}")
            return result
        except Exception as e:
            print(f"Error calculating {expression}: {e}")
            return str(e)
    
    # Example 1: Simple streaming response
    print("\nExample 1: Simple streaming response")
    print("Response: ", end="", flush=True)
    
    chat.system("You're a helpful assistant.")
    for chunk in chat.user("Write a haiku about coding.").ready():
        print(chunk, end="", flush=True)
    print("\n")

    # Example 2: Streaming with tool calls
    print("\nExample 2: Streaming with tool calls")
    print("Response: ", end="", flush=True)
    
    for chunk in chat.user("Calculate 25 * 4 and tell me the result.").ready():
        print(chunk, end="", flush=True)
    print("\n")

    # Example 3: Multiple tool calls in streaming
    print("\nExample 3: Multiple calculations in streaming")
    print("Response: ", end="", flush=True)
    
    for chunk in chat.user("Calculate 25 * 4, then 100 / 5, and write a sentence using both results.") \
            .ready():
        print(chunk, end="", flush=True)
    print("\n")