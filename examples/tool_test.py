from ploppie import Chat
import random

if __name__ == "__main__":
    chat = Chat(model="gpt-4o-mini")
    
    @chat.tool("Perform mathematical calculations")
    def calculate(expression: "str: The expression to calculate"):
        return eval(expression)
    
    @chat.tool("Random number generator")
    def random_number(min: "int: The minimum value", max: "int: The maximum value"):
        return random.randint(min, max)
    
    print(chat.send("What is 2502 * 2502, and 2858 - 28592? Please tell me the result. And then throw me a random number for giggles."))