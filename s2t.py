import speech_recognition as sr
import os, shutil
from pydub import AudioSegment
from pydub.silence import split_on_silence
import moviepy.editor as mp

#inserire nome video
nomevideo = input("inserisci il nome del video preciso:\n")

video = mp.VideoFileClip(nomevideo)
audio = video.audio
# audio.write_audiofile()
audio.write_audiofile(nomevideo.split(".")[0]+".wav",codec='pcm_s16le')

filename = nomevideo.split(".")[0]+".wav"

r = sr.Recognizer()
# print(os.path.abspath(os.getcwd())+"\\"+filename)
filenamemp3 = os.path.abspath(os.getcwd())+"\\"+filename
path = filenamemp3
# def get_large_audio_transcription(path):
"""
Splitting the large audio file into chunks
and apply speech recognition on each of these chunks
"""
# open the audio file using pydub
# sound = AudioSegment.from_mp3(path)
sound = AudioSegment.from_wav(path)
# split audio sound where silence is 700 miliseconds or more and get chunks
chunks = split_on_silence(sound,
    # experiment with this value for your target audio file
    min_silence_len = 300,
    # adjust this per requirement
    silence_thresh = sound.dBFS-14,
    # keep the silence for 1 second, adjustable as well
    keep_silence=500,
)
#TODO control over the length of audio files
#TODO load automatic bunch of files, delete wav
folder_name = "audio-chunks"
# create a directory to store the audio chunks
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
whole_text = ""
# process each chunk 
for i, audio_chunk in enumerate(chunks, start=1):
    # export audio chunk and save it in
    # the `folder_name` directory.
    chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
    audio_chunk.export(chunk_filename, format="wav")
    # recognize the chunk
    with sr.AudioFile(chunk_filename) as source:
        audio_listened = r.record(source)
        # try converting it to text
        try:
            text = r.recognize_google(audio_listened, language="it-IT")
        except sr.UnknownValueError as e:
            print("Error:", str(e))
        else:
            text = f"{text.capitalize()}. "
            print(chunk_filename, ":", text)
            whole_text += text
    # return the text for all chunks detected
    # return whole_text

# text = get_large_audio_transcription(filenamemp3)
#delete the audio chunks directory

textfilename = os.path.abspath(os.getcwd())+"\\"+filename.split(".")[0]+"_text.txt"
with open(f"{textfilename}","w") as fp:
    fp.write(whole_text)
    
shutil.rmtree(os.getcwd()+"\\"+folder_name)
os.remove(os.getcwd()+"\\"+filename)