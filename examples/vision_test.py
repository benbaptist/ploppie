from ploppie import Chat

from ploppie.messages.files import Image

if __name__ == "__main__":
    chat = Chat(model="gpt-4o-mini")

    a = chat.system("Identify the objects in the image.") \
        .user(Image(file_handle=open("examples/test.png", "rb"))) \
        .ready()
    
    for msg in a:
        print(msg)