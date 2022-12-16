from turtle import color
import speedtest
import numpy as np
import matplotlib.pyplot as plt

speed_test = speedtest.Speedtest()

download_speed = round(speed_test.download()/1e6)
print("Your Download speed is", download_speed,'Mb') 

upload_speed = round(speed_test.upload()/1e6)
print("Your Upload speed is", upload_speed,'Mb')

x = 0
y = 0
fig = plt.figure()

plt.subplot(1,2,1)
plt.pie([download_speed, 300-download_speed])
plt.title('Download speed', color = 'white')
circle = plt.Circle( (x,y), 0.7, color='none')
ax=plt.gcf().gca()
ax.add_artist(circle)
ax.set_facecolor('none')
label = ax.annotate((str(download_speed) + 'Mb'), xy=(x, y), 
                    fontsize=20, ha="center", va='center', color='white')
plt.show(block=False)

plt.subplot(1,2,2)
plt.pie([upload_speed, 100-upload_speed])
plt.title('Upload speed', color = 'drak gray')
circle = plt.Circle( (x,y), 0.7, color='none')
ax=plt.gcf().gca()
ax.add_artist(circle)
label = ax.annotate((str(upload_speed) + 'Mb'), xy=(x, y), 
                    fontsize=20, ha="center", va='center', color='white')
# plt.show()

plt.savefig('test.png', transparent=True)

from PIL import Image
img = Image.open('test.png')
img.show() 