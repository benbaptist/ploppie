# Ploppie Library Documentation

## Overview
Ploppie is a library designed for managing an interactive chat interface that can utilize tools and assist with dynamic responses. It consists of various message types and functionalities that help construct conversational agents leveraging large language models.

## Installation
To install the Ploppie library, run:
```bash
pip install ploppie
```

## Directory Structure
The main directory structure of the Ploppie library is organized as follows:
```
ploppie/
    ├── __init__.py          # Initialization file for the package
    ├── chat.py              # The main chat management functionality
    ├── utility.py           # Utility functions for chat processing
    └── messages/            # Module for message definitions
        ├── __init__.py      # Initialization file for messages
        ├── assistant.py      # Assistant messages and tool calls
        ├── dynamic.py        # Dynamic message handling
        ├── message.py        # Base class for all messages
        ├── system.py         # System messages
        ├── toolcall.py       # Tool call management
        ├── toolresult.py      # Tool result management
        └── user.py           # User messages
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
chat_session = Chat(verbose=True)  # Enables verbose logging
```
You can also pass any litellm completion()-supported parameter to Chat().


### Sending Messages
You can send messages as either a user or assistant:
```python
chat_session.system("You are a helpful assistant.")
chat_session.assistant("I can assist you with your queries.")
chat_session.user("What can you do?")
```

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
def fetch_dynamic_content():
    return "This content is dynamic!"
```

## Conclusion
The Ploppie library facilitates the creation of sophisticated chat interfaces with modular design for handling both user and system interactions. Refer to the API documentation for further information on individual classes and methods.