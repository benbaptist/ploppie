from ploppie import Chat

from ploppie.messages.files import Audio

if __name__ == "__main__":
    chat = Chat(
        model="gpt-4o-mini-audio-preview-2024-12-17",
        modalities=["text"],
        verbose=True
    )

    a = chat.system("Identify what is being said.") \
        .user(Audio(file_handle=open("examples/test.wav", "rb"))) \
        .ready()
    
    for i in a:
        print(i)