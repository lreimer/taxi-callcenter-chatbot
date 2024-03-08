from speech import text_to_audio 

def main():
    text = "Hallo, ich bin ihr intelligenter Call-Center Agent. Wie kann ich helfen?"
    bucket_name = "taxi-callcenter-bucket"
    audio_file_name = "hello_callcenter.mp3"
    text_to_audio(text, audio_file_name, bucket_name)

if __name__ == "__main__":
    main()
