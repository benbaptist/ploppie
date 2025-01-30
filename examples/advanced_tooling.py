from ploppie import Chat
import random

if __name__ == "__main__":
    chat = Chat(model="gpt-4o-mini", verbose=True)
    
    @chat.hook("list_tools")
    def list_tools():
        return [
            {
                "type": "function",
                "function": {
                    "name": "calculate",
                    "description": "Perform mathematical calculations", 
                    "parameters": {
                    "type": "object",
                    "properties": {
                            "expression": {"type": "string"}
                        }
                    }
                }
            }
        ]
    
    @chat.hook("call_tool")
    def call_tool(tool_call):
        if tool_call.name == "calculate":
            return eval(tool_call.arguments["expression"])
        else:
            return "Unknown tool"
    
    response = chat.user("What is 2502 * 2502, and 2858 - 28592? And then combine them together for a third result.") \
        .ready()

    print(response)