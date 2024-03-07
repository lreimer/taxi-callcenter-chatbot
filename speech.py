import os
from google.cloud import texttospeech
from google.cloud import storage

def text_to_audio(text, bucket_name, audio_file_name):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request
    voice = texttospeech.VoiceSelectionParams(
        language_code="de-DE", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Store the audio file in a GCS bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(audio_file_name)
    blob.upload_from_string(response.audio_content, content_type="audio/mpeg")

    print(f"Audio file '{audio_file_name}' created and stored in bucket '{bucket_name}'.")
