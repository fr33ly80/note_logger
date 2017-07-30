#Audio Record Program
#June 10 2016
#Brendan Freely

import os
import speech_recognition as sr
#import pyttsx
import pyaudio
import wave
import datetime


# Default Audio Settings
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
#RATE = 48000
CHUNK = 1024
#CHUNK = 512
RECORD_SECONDS = 3
AssertionErrortime=5
std_wd = '/home/pi/note_logger/recorded_logs/'

# Getting CWD
dflt_wd = os.getcwd() + '/recorded_logs/' # Windows

controller = pyaudio.PyAudio()

# Fundamental Functions    
def open_mic():
    # Start Recording
    mic = controller.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print "recording..."
    frames = []
    return mic, frames

def record_pd(mic, time=20, frames = []):
    time+=1 # This offset accounts for delay in the beginning of the recording
    for i in range(0, int(RATE / CHUNK * time)):
        data = mic.read(CHUNK)
        frames.append(data)
    close_mic(mic, controller)
    print "finished recording"
    return frames


def close_mic(mic, controller):
    mic.stop_stream()
    mic.close()
    controller.terminate()
    print "mic and controller closed"


def save_audio(frames, name=''):
    footer = datetime.datetime.now().strftime("%m%d%Y-%H:%M") + '.wav'
    if name != '':
        footer = '_' + footer
    if name == 'test':
        footer = ''
    filename = dflt_wd + name + footer
    wavefile = wave.open(filename, 'wb')
    wavefile.setnchannels(CHANNELS)
    wavefile.setsampwidth(controller.get_sample_size(FORMAT))
    wavefile.setframerate(RATE)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()
    print('Audio file saved as ' + filename + ' in  ' + dflt_wd)

# Testing and Debugging Functions
def test_file(time=3):
    mic, frames = open_mic()
    log = record_pd(mic, time=time, frames=frames)
    #close_mic(mic, controller)
    save_audio(log, name='test')

# Executed Statements
test_file(5)
    
    

# Speech Recognition
###r = sr.Recognizer()
###WIT_AI_KEY = "6EWVDDDK5KGH3YXFJFOFVE7FF2VSVAAA"
###try:
###    print("What I heard was: " + sr.recognize_wit(input.wav, key=WIT_AI_KEY))
###except sr.UnknownValueError:
###    print("I could not understand what you said.")
###except sr.RequestError as e:
###    print("I could not reach the server at this time.; {0}".format(e))

###try:
###    print("What I heard was: " + r.recognize_wit(input.wav, key=WIT_AI_KEY))
###except sr.UnknownValueError:
###    print("I could not understand what you said.")
###except sr.RequestError as e:
###    print("I could not reach the server at this time.; {0}".format(e))

