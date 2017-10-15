from subprocess import Popen, PIPE
import sys
import time

LEFT_PORT = sys.argv[1]
RIGHT_PORT = sys.argv[2]
print("Hold the drumsticks parallel to each other, pointing away from you")
time.sleep(5)
p1 = Popen(['python', './left.py', LEFT_PORT, '115200'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
p2 = Popen(['python', './right.py', RIGHT_PORT, '115200'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
leftCal = False;
rightCal = False;

while 1:
    hitR = bytes.decode(p2.stdout.readline())
    hitL = bytes.decode(p1.stdout.readline())
    if not leftCal:
        if "Waiting" in hitL:
            print('Left side calibrating...')
        if "calibrated" in hitL:
            leftCal = True
            print('Left side calibrated')
    if not rightCal:
        if "Waiting" in hitR:
            print('Right side calibrating...')
        if "calibrated" in hitR:
            rightCal = True
            print('Right side calibrated')