import json
import os
from ploppie import Chat

if __name__ == "__main__":
    chat = Chat(model="gpt-4o-mini")
    
    @chat.tool("Perform mathematical calculations")
    def calculate(expression: "str: The expression to calculate"):
        return eval(expression)
        
    if os.path.exists("chat.json"):
        with open("chat.json", "r") as f:
            chat.from_dict(json.load(f))
    
    while True:
        input_ = input("<You> ")
        responses = chat.send(input_)
        
        for response in responses:
            print(f"<Ploppie> {response}")

        with open("chat.json", "w") as f:
            json.dump(chat.to_dict(), f)