import os
import whisper
import openai
from pytube import YouTube

API_KEY = os.environ['API_KEY']
WHISPER_MODEL_NAME = 'base'

openai.api_key = API_KEY

link = 'https://www.youtube.com/watch?v=H1HdZFgR-aA'

video_id = link.split('watch?v=')[1]

file_name = f'{video_id}.mp4'

yt = YouTube(link)

stream = yt.streams.get_audio_only()

file_path = stream.download(filename=file_name)

model = whisper.load_model(WHISPER_MODEL_NAME)

result = model.transcribe(file_path)

text = result['text']

os.remove(file_name)

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
