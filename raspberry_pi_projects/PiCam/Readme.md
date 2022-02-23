# PiCam stream to PC
## Configure PiCam in raspberry pi
Follow this tutorial [Getting started with PiCam](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera).

## Stream video from RaspberryPi (pi-cam) to your computer using mplayer
- On raspberry pi side <br/>
`/opt/vc/bin/raspivid -t 0 -w 300 -h 300 -hf -fps 20 -o - | nc 192.168.2.4 2222` <br/>
Replace **192.168.2.4** with your PC's IP address and you can change the -w and -h values and -fps values. Here 2222 is socket connect port can give another value. <br/>
- On your pc side <br/>
`sudo apt install mplayer`<br/>
`nc -l 2222 | mplayer -fps 200 -demuxer h264es -`<br/>

### Stream video from RaspberryPi (pi-cam) to your computer using opencv and ffmpeg
- On raspberry pi side <br/>
  `ssh pi@x.x.x.x`<br/>
   `raspivid -t 0 -w 640 -h 480 -hf -ih -fps 20 --rotation 180 -o - | nc -k -l 2222`<br/>

- On you PC <br/>
  `python3 streamFromPiCam.py`<br/>
  Requirement - opencv, numpy, ffmpeg.<br/>

