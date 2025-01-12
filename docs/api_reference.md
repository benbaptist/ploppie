# API Reference for Ploppie Library

## Overview
This section summarizes the essential modules and classes provided by the Ploppie library.

### Chat Class
`Chat` serves as the primary interface for creating chat sessions.
- **Methods**:
    - `__init__(**kwargs)`: Initializes a chat session with possible configurations.
    - `send(message: str)`: Sends a user message to the chat.
    - `user(message: str)`: Appends a user message to the chat.
    - `assistant(message: str)`: Appends an assistant message to the chat.
    - `ready()`: Prepares the chat to send messages for processing.

### Message Classes
#### Message
The base class for all types of messages. 
- **Constructor**: `__init__(role: str, content: str)`

#### User
Represents a message sent by a user.
- **Constructor**: `__init__(content: str)`

#### Assistant
Represents messages sent by the assistant. Includes functionality for tool calls and results.
- **Constructor**: `__init__(content: str, tool_calls=[], tool_result=None)`

#### ToolCall
Used to represent a tool call in the assistant's messages.
- **Constructor**: `__init__(name: str, arguments: dict, id: str)`

#### ToolResult
Represents the result of a tool call.
- **Constructor**: `__init__(content: str, name: str, tool_call_id: str)`

#### System
Represents system messages that provide context or notifications within the chat.
- **Constructor**: `__init__(content: str)`

### Utility Class
A utility class that provides additional helpful functions, such as method for responding to prompts and managing choices.
- **Methods**:
    - `selector(message: str, options: list, attempts: int = 3)`: Requests the LLM to make a selection based on provided options.

## Conclusion
This API reference details the components of the Ploppie library. Each class is designed for specific use within chat functionalities, allowing for flexible interaction with large language models.