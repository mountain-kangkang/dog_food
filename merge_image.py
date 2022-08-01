import tkinter
from tkinter import filedialog
from datetime import datetime
from PIL import Image
import os

print('\nstart : ', datetime.now(), '\n')

root = tkinter.Tk()         # select folder
root.withdraw()
dir_path = filedialog.askdirectory(parent=root, initialdir="C:\\Users\\user\\Desktop\\", title='Please select a directory')

rt = os.walk(dir_path)

for root, dirs, files in rt:
    for file in files:
        err = root.replace('/', '\\')
        #errRoot = err.replace('\', '\\')
        if str(root)[-7:]=='image_L' and str(file)[-6:]=='_L.png':
            if os.path.exists(str(root)[:-8]+'/pano'):
                pass
            else:
                os.mkdir(str(root)[:-8]+'/pano')
            file_name = str(file)[:-6]
            print(err, file_name)
            files_list = []
            files_list.append(str(err) +'\\' + file)
            files_list.append(str(err)[:-1] +'F\\' + file_name + '_F.png')
            files_list.append(str(err)[:-1] +'R\\' + file_name + '_R.png')
            files_list.append(str(err)[:-1] +'B\\' + file_name + '_B.png')

            new_image = Image.new("RGB", (1920*4, 1200), (256,256,256))
            for index in range(len(files_list)):
                area = ((index*1920), 0, (1920*(index+1)), 1200)
                new_image.paste(Image.open(files_list[index]), area)
            # new_image.show()
            new_image.save(str(err)[:-7] + 'pano\\' + file_name + '.png')

        else:
            pass

print('\nend   : ', datetime.now(), '\n')