from ploppie import Utility
import random

if __name__ == "__main__":
    utility = Utility(model="gpt-4o-mini")

    # Generate a random pretend error message
    error_messages = [
        "The database connection failed. Please check your credentials and try again.",
        "The authentication credentials are invalid. Please check your credentials and try again.",
        "The network connection timed out. Please check your network connection and try again.",
        "You do not have permission to access this resource. Please check your permissions and try again.",
        "The server is experiencing high traffic. Please try again later.",
        "Aliens have invaded the earth. Please evacuate the area immediately."
    ]

    error_message = random.choice(error_messages)

    error_message = error_messages[-1]

    print(f"Error message: {error_message}")
    
    # Diagnose the root cause of the pretend error
    result = utility.selector(
        f"Based on the error message, what is the most likely root cause? Error message: {error_message}",
        options=[
            "DATABASE_CONNECTION_ERROR",
            "INVALID_AUTHENTICATION_CREDENTIALS", 
            "NETWORK_TIMEOUT",
            "INSUFFICIENT_PERMISSIONS",
            "UNKNOWN_ERROR"
        ]
    )

    # Print the diagnosed root cause
    print(f"Diagnosed root cause: {result}")
