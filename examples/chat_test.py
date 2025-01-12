from ploppie import Chat
from ploppie.messages import System
from ploppie.messages.files import Image

import os
import re
from datetime import datetime

if __name__ == "__main__":
    chat = Chat(model="gpt-4o-mini")

    # Add a dynamic message that updates the current time, 
    # called every time we send a message
    @chat.dynamic()
    def dynamic_message():
        return System("The current time is " + datetime.now().strftime("%H:%M:%S"))
    
    @chat.tool("Perform mathematical calculations")
    def calculate(expression: "str: The expression to calculate"):
        print(f"Calculating {expression}")

        try:
            return eval(expression)
        except Exception as e:
            return f"I'm sorry, I can't calculate that. ({e})"
    
    while True:
        input_ = input("<You> ")

        # Parse the input for a file path

        inputs = [input_]

        file_path_match = re.search(r'(?:^|\s)([\'"]?)([a-zA-Z0-9_\-./\\]+\.(png|jpg|jpeg|gif|webp))\1(?:\s|$)', input_)
        if file_path_match:
            file_path = file_path_match.group(2)

            if os.path.exists(file_path):
                print(f"* Found image: {file_path}")
                image = Image(open(file_path, 'rb'))
                inputs.append(image)
            else:
                chat.system(f"File not found: {file_path} - please inform the user")
                print(f"* File not found: {file_path}")

        responses = chat.send(inputs)

        for response in responses:
            print(f"<Ploppie> {response}")