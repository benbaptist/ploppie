Ploppie is a high-level, stupid-simple Pythonic LiteLLM abstraction layer for implementing simple chat workflows, with tools. No more messing around with dictionaries and JSON, no more OpenAI-specific APIs. Just plain Python.

Supports vision, audio, and any other LiteLLM features.

# Vanilla LiteLLM Example

```python
from litellm import completion

# Define a system prompt
system_prompt = "You are a helpful assistant that can perform calculations."

# Define a tool for basic math
def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"

# Example conversation
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What is 25 * 4?"}
]

# Get completion from LiteLLM
response = completion(
    model="gpt-4o-mini",
    messages=messages,
    functions=[{
        "name": "calculate",
        "description": "Perform basic mathematical calculations",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to evaluate"
                }
            },
            "required": ["expression"]
        }
    }]
)

# Print the response
print(response.choices[0].message)
```

# Ploppie Example
```python
from ploppie import Chat, Tool, System

chat = Chat(model="gpt-4o-mini")

@chat.tool(description="Perform basic mathematical calculations.")
def calculate(
    expression: "str: The result of the calculation as a string, or 'Invalid expression' if evaluation fails") -> str:
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"

chat.system("You are a helpful assistant that can perform calculations.")\
    .user("What is 25 * 4?")\
    .ready()

print(_)
```

# Vision Example

```python
from ploppie import Chat, System, User, Assistant

chat = Chat(model="gpt-4o-mini")

a = chat.system("Identify the objects in the image.") \
    .user(Image(content=open("path/to/image.jpg", "rb"))) \
    .ready()  # Signals chat is ready for execution

print(a)
```
