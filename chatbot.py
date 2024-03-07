import speech

def main():
    # Example usage
    text = "Hello, how are you?"
    bucket_name = "taxi-chatbot-bucket"
    audio_file_name = "hello_audio.mp3"
    text_to_audio(text, bucket_name, audio_file_name)

if __name__ == "__main__":
    main()
