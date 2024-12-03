from ploppie import Chat

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

    # You can pass any standard LiteLLM parameters to the Chat object
    chat = Chat(model="gpt-4o-mini", stream=False)

    @chat.tool("Perform mathematical calculations")
    def calculate(expression: "str: The expression to calculate"):
        return eval(expression)
    
    response = chat.system("You're a helpful assistant.") \
        .user("What is the capital of France? Afterrwards, calculate 50 * 50.") \
        .ready()
    
    print("Response: ", end="", flush=True)
    for chunk in response:
        print(chunk, end="", flush=True)

    print("")