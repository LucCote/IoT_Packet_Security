from scapy.all import rdpcap
import matplotlib.pyplot as plt

starttime = 20190402094103
timeinterval = 1
filenum = 101

traffic_rates = []


def change_start():
    global starttime
    starttime += timeinterval
    if starttime % 100 >= 60:
        starttime += 40
    if starttime % 10000 >= 6000:
        starttime += 4000
    if starttime % 1000000 >= 240000:
        starttime += 760000


def format_num(n):
    toreturn = ""
    if n < 10:
        toreturn = "0000"
    elif n < 100:
        toreturn = "000"
    elif n < 1000:
        toreturn = "00"
    elif n < 10000:
        toreturn = "0"
    else:
        toreturn = ""
    change_start()
    return toreturn + str(n) + "_" + str(starttime)


for i in range(1, filenum):
    data = "../../desktop/STEM-Fellowship/pcaps-switch-shape128-1-20-60-20/output_" + format_num(i) + ""
    print(data)
    file_rate = 0
    a = rdpcap(data)
    sessions = a.sessions()
    for session in sessions:
        for packet in sessions[session]:
            file_rate += len(packet)
    traffic_rates.append(file_rate)


# print(traffic_rates)
plt.plot(traffic_rates)
plt.ylabel('traffic rate (bytes)')
plt.xlabel('time (seconds)')
plt.grid(True)
plt.ylim(ymin=0)
plt.xlim(xmin=0)
# plt.xticks([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600])
plt.show()
