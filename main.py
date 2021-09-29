import os
import csv
import glob
from datetime import datetime, timedelta
import struct

def raw_data(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    return bytearray(content)

def Win_ts(timestamp):
    WIN32_EPOCH = datetime(1601, 1, 1)
    return WIN32_EPOCH + timedelta(microseconds=timestamp // 10, hours=9)

path = "C:/Users/lg/Desktop"
lnk_data = []
cnt = 0
lnk_file_list = glob.glob(path + '/*.lnk')
lnk_filename_List = os.listdir(path)

f = open('lnk.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(["File Name", "Creation Time", "Access Time", "Write Time", "File Size"])

for lnk_file in lnk_file_list:
    data = raw_data(lnk_file)
    filename = lnk_filename_List[cnt]
    creation_time = (Win_ts(struct.unpack_from("<Q", data[0x1C:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
    access_time = (Win_ts(struct.unpack_from("<Q", data[0x24:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
    write_time = (Win_ts(struct.unpack_from("<Q", data[0x2C:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
    file_size = (struct.unpack_from("<i", (data[0x34:]))[0])

    lnk_data.append((filename, creation_time, access_time, write_time, file_size))
    cnt += 1

for i, (name, ctime, atime, wtime, size) in enumerate(lnk_data):
    wr.writerow([name, ctime, atime, wtime, size])
