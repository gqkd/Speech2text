# s2t.py

This code is a Python script that transcribes the audio from a video file.

## Dependencies

* speech_recognition: This library is used to transcribe audio files.
* pydub: This library is used to split audio files into chunks.
* moviepy.editor: This library is used to extract the audio from a video file.

## Instructions

1. Install the dependencies by running the following command:

pip install speech_recognition pydub moviepy


2. Run the script by providing the name of the video file as an argument:

python s2t.py <video_file_name>

For example, to transcribe the audio from the video file video.mp4, you would run the following command:

python s2t.py video.mp4

The script will first extract the audio from the video file and save it as a WAV file. It will then split the WAV file into chunks and transcribe each chunk using the speech_recognition library. The transcripts for each chunk will be printed to the console. The final transcript will be saved to a file named <video_file_name>_text.txt.
