import requests
from urllib.parse import quote

def textToSpeech(text):
    apiUrl = "https://fanyi.sogou.com/reventondc/synthesis"
    audio_url = f"{apiUrl}?text={quote(text)}&speed=1&lang=zh-CHS&from=translateweb&speaker=5"
    response = requests.get(audio_url)
    with open('audio.mp3', 'wb') as f:
        f.write(response.content)
    audio = AudioSegment.from_file('audio.mp3', format='mp3')
    play(audio)
