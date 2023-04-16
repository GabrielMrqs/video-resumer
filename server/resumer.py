import os
import whisper
import openai
from pytube import YouTube

# API_KEY = os.environ['API_KEY']
API_KEY = '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'
WHISPER_MODEL_NAME = 'base'


class Resumer:
    def __init__(self) -> None:
        openai.api_key = API_KEY
        self.model = whisper.load_model(WHISPER_MODEL_NAME)

    def resume_video(self, id_video):

        link = f'https://www.youtube.com/{id_video}'

        yt = YouTube(link)

        stream = yt.streams.get_audio_only()

        file_path = stream.download(filename='video.mp4')

        result = self.model.transcribe(file_path)

        text = result['text']

        print(text)

        os.remove(file_path)

        response_chat_gpt = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você resume textos em português"},
                {"role": "user", "content": text},
            ]
        )

        response = ''
        for choice in response_chat_gpt.choices:
            response += choice.message.content
        
        print(response)

        return response
