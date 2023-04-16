import os
import whisper
import openai
from pytube import YouTube

API_KEY = os.environ['API_KEY']
WHISPER_MODEL_NAME = 'base'

openai.api_key = API_KEY

link = 'https://www.youtube.com/watch?v=H1HdZFgR-aA'

yt = YouTube(link)

stream = yt.streams.get_audio_only()

file_path = stream.download(filename='video.mp4')

model = whisper.load_model(WHISPER_MODEL_NAME)

result = model.transcribe(file_path)

text = result['text']

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
