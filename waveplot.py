import serial, sys
import matplotlib.pyplot as plt

x=range(0, 100, 1)
data=[0.0]*100

ser=serial.Serial(sys.argv[1],sys.argv[2])
print("connected to: " + ser.portstr)
while True:
  line = ser.readline()
  line1=line.strip().decode('utf-8')
  if line1=='':
    line1="0.0"
  d=float(line1)
  #print(d)
  data.pop(-1)
  data.insert(0,d)
  plt.clf()
  plt.ylim([-1.0,20000.0])
  plt.plot(x,data)
  plt.pause(0.1)
