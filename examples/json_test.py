from ploppie import Chat
import random

if __name__ == "__main__":
    # You can pass any standard LiteLLM parameters to the Chat object
    chat = Chat(model="gpt-4o-mini", response_format={"type": "json_object"})
    
    response = chat.system("Take any input and convert it to a sensible JSON object.") \
        .user("Make a JSON object that represents a cat.") \
        .ready()
    
    print(response)