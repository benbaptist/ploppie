# Ploppie Library Documentation

## Overview
Ploppie is a library designed for managing an interactive chat interface that can utilize tools and assist with dynamic responses. It consists of various message types and functionalities that help construct conversational agents leveraging large language models.

## Installation
To install the Ploppie library, run:
```bash
pip install ploppie
```

## Usage
### Import the Library
To begin using Ploppie, you can import the necessary classes as follows:
```python
from ploppie import Chat, Utility
```

### Creating a Chat Session
You can create a chat session with the following code:
```python
chat_session = Chat(model="gpt-4o-mini", verbose=True)
```
You can also pass any litellm completion()-supported parameter to Chat().


### Sending Messages
You can add messages to the chat session as System, Assistant, or User messages:
```python
chat_session.system("You are a helpful assistant.")
chat_session.assistant("I can assist you with your queries.")
chat_session.user("What can you do?")
```

### Executing the Chat Session
You can execute the chat session by calling `ready()`:
```python
responses = chat_session.ready()
```

`ready()` returns a list of responses, which you can then process as needed. In most cases, it'll only return one response.

### Using Tools
You can define tools that the assistant can interact with via decorators:
```python
@chat_session.tool("This tool does something.")
def my_tool(param):
    return f"The result of the tool call is {param}"
```

### Dynamic Messages
You can add dynamic messages that are computed at runtime:
```python
@chat_session.dynamic()
def current_time():
    return "The current time is " + datetime.now().strftime("%I:%M %p")
```

These dynamic messages are processed in the order they are added, and processed upon every call to `ready()`.

### Using Utility
You can use the Utility class to select from a list of options:
```python
time_of_day = datetime.now().strftime("%I:%M %p")

response = Utility.selector(
    "Pick a color that best matches the sky for this time of day: {time_of_day}",
    options=["red", "yellow", "blue", "green", "purple", "orange", "pink"]
)

print(f"The color of the sky is {response} at {time_of_day}.")
```

## Conclusion
The Ploppie library facilitates the creation of sophisticated chat interfaces with modular design for handling both user and system interactions. Refer to the API documentation for further information on individual classes and methods.