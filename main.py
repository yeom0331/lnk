import os.path
import csv
import glob
from datetime import datetime, timedelta
import struct

desktop_path = os.getenv('USERPROFILE') + "/Desktop"
recent_path = os.getenv('USERPROFILE') + "/AppData/Roaming/Microsoft/Windows/Recent"
start_menu_path = os.getenv('USERPROFILE') + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs"
quick_path = os.getenv('USERPROFILE') + "/AppData/Roaming/Microsoft/Internet Explorer/Quick Launch"
desktop_lnk_data = []
recent_lnk_data = []
start_menu_data = []
quick_data = []
dlnk_file_list = glob.glob(desktop_path + '/*.lnk')
dlnk_filename_List = os.listdir(desktop_path)
rlnk_file_list = glob.glob(recent_path + '/*.lnk')
rlnk_filename_List = os.listdir(recent_path)
slnk_file_list = glob.glob(start_menu_path + '/*.lnk')
slnk_filename_List = os.listdir(start_menu_path)
qlnk_file_list = glob.glob(quick_path + '/*.lnk')
qlnk_filename_List = os.listdir(quick_path)

def raw_data(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    return bytearray(content)

def Win_ts(timestamp):
    WIN32_EPOCH = datetime(1601, 1, 1)
    return WIN32_EPOCH + timedelta(microseconds=timestamp // 10, hours=9)

f = open('lnk.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(["Path", "File Name", "Creation Time", "Access Time", "Write Time", "File Size"])

def desktop_parse():
    cnt = 0
    for lnk_file in dlnk_file_list:
        data = raw_data(lnk_file)
        path = desktop_path
        filename = dlnk_filename_List[cnt]
        creation_time = (Win_ts(struct.unpack_from("<Q", data[0x1C:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
        access_time = (Win_ts(struct.unpack_from("<Q", data[0x24:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
        write_time = (Win_ts(struct.unpack_from("<Q", data[0x2C:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
        file_size = (struct.unpack_from("<i", (data[0x34:]))[0])

        desktop_lnk_data.append((path, filename, creation_time, access_time, write_time, file_size))
        cnt += 1

    for i, (path, name, ctime, atime, wtime, size) in enumerate(desktop_lnk_data):
        wr.writerow([path, name, ctime, atime, wtime, size])

def recent_parse():
    cnt = 0
    for lnk_file in rlnk_file_list:
        data = raw_data(lnk_file)
        path = recent_path
        filename = rlnk_filename_List[cnt]
        creation_time = (Win_ts(struct.unpack_from("<Q", data[0x1C:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
        access_time = (Win_ts(struct.unpack_from("<Q", data[0x24:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
        write_time = (Win_ts(struct.unpack_from("<Q", data[0x2C:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
        file_size = (struct.unpack_from("<i", (data[0x34:]))[0])

        recent_lnk_data.append((path, filename, creation_time, access_time, write_time, file_size))
        cnt += 1

    for i, (path, name, ctime, atime, wtime, size) in enumerate(recent_lnk_data):
        wr.writerow([path, name, ctime, atime, wtime, size])

def start_menu_parse():
    cnt = 0
    for lnk_file in slnk_file_list:
        data = raw_data(lnk_file)
        path = start_menu_path
        filename = slnk_filename_List[cnt]
        creation_time = (Win_ts(struct.unpack_from("<Q", data[0x1C:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
        access_time = (Win_ts(struct.unpack_from("<Q", data[0x24:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
        write_time = (Win_ts(struct.unpack_from("<Q", data[0x2C:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
        file_size = (struct.unpack_from("<i", (data[0x34:]))[0])

        start_menu_data.append((path, filename, creation_time, access_time, write_time, file_size))
        cnt += 1

    for i, (path, name, ctime, atime, wtime, size) in enumerate(start_menu_data):
        wr.writerow([path, name, ctime, atime, wtime, size])

def quick_parse():
    cnt = 0
    for lnk_file in qlnk_file_list:
        data = raw_data(lnk_file)
        path = quick_path
        filename = qlnk_filename_List[cnt]
        creation_time = (Win_ts(struct.unpack_from("<Q", data[0x1C:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
        access_time = (Win_ts(struct.unpack_from("<Q", data[0x24:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
        write_time = (Win_ts(struct.unpack_from("<Q", data[0x2C:])[0]).strftime('%Y:%m:%d %H:%M:%S.%f'))
        file_size = (struct.unpack_from("<i", (data[0x34:]))[0])

        quick_data.append((path, filename, creation_time, access_time, write_time, file_size))
        cnt += 1

    for i, (path, name, ctime, atime, wtime, size) in enumerate(quick_data):
        wr.writerow([path, name, ctime, atime, wtime, size])

desktop_parse()
recent_parse()
start_menu_parse()
quick_parse()