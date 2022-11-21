from gtts import gTTS
import os
text="Python is Amazing, You should also try it!"
audio=gTTS(text=text,lang='en',slow=False)
audio.save("python.mp3")
os.system("start python.mp3") 