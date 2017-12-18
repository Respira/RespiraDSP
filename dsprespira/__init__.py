import statistics
import pyaudio 
import struct
import numpy
from dsprespira.SampleBuffer import SampleBuffer 
from dsprespira.Sample import Sample
from pyaudio import PyAudio
from asyncio.tasks import wait
import time
from builtins import str
CHANNELS = 1
RATE = 48000  
FRAMES_PER_BLOCK = 768

#INITIALIZE
p= pyaudio.PyAudio()
dbsplBuffer = SampleBuffer()


def callback(in_data, frame_count, time_info, flag):
    if in_data:
        sample =Sample(numpy.fromstring(in_data, 'Float32'))
        dbsplBuffer.__append__(sample.getdbSPL())

    return (None, pyaudio.paContinue)
  
# open stream (2)
stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=RATE,
                output=False,input=True,
                frames_per_buffer=FRAMES_PER_BLOCK,
                stream_callback=callback)
stream.start_stream()

try:
    time.sleep (2);
    stream.stop_stream()
    stream.close()
    p.terminate()  
    print(dbsplBuffer.getSyllables())
# block =stream.read(INPUT_FRAMES_PER_BLOCK)
# x=SampleBuffer(block)
#   print(x.getSyllables())
except IOError as e:
    print("error recording "+ str(e))