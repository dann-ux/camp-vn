#!/bin/bash
pkill Xvfb pkill x11vnc pkill websockify Xvfb :1 -screen 0 1280x720x24 -ac & sleep 2 export DISPLAY=:1 x11vnc 
-display :1 -nopw -forever -shared -rfbport 5900 -bg
websockify --web=/usr/share/novnc 6080 localhost:5900 &
