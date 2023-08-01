import math
import speedtest
import math

wifi = speedtest.Speedtest()

print("Getting download speed...")
downoad_speed = wifi.download()

print("Getting upload speed...")
upload_speed = wifi.upload()


print("Download : ",round(downoad_speed*(pow(10, -6)), 2), "Mbps")
print("Upload : ",round(upload_speed*(pow(10, -6)), 2), "Mbps")