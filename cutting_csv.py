from tkinter import filedialog
from datetime import datetime
import tkinter
import csv
import os

print('\n\nstart : ', datetime.now(), '\n')

root = tkinter.Tk()         # select folder
root.withdraw()
dir_path = filedialog.askdirectory(parent=root, initialdir="C:\\Users\\user\\Desktop\\", title='Please select a directory')

rt = os.walk(dir_path)

print('directory : ', dir_path, '\n')

gps_list = []

for root, dirs, files in rt:
    for f in files:
        if((str(f)[-4:] == '.csv') and (str(f)[:3] == 'GPS') and (len(str(f)) == 23)):
            if os.path.exists(str(root)+'/sep_gps'):
                pass
            else:
                os.mkdir(str(root)+'/sep_gps')
            
            file_name = str(f)[:-4]
            print('\t', file_name)

            cf = open(str(root)+'/'+str(f), 'r')
            cfr = csv.reader(cf)
            
            cnt = 1

            for line in cfr:
                gps_list = line
                ncf = open(str(root)+'/sep_gps/'+ file_name + '_%04d'%cnt + '.csv', 'w', newline='')
                ncfw = csv.writer(ncf)
                ncfw.writerow(gps_list)
                ncf.close()
                cnt += 1

            cf.close()


print('\nend   : ', datetime.now(), '\n\n')