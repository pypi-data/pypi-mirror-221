import os
import cv2
import shutil
import hashlib


def get_md5(data):
    return str(hashlib.md5(data).hexdigest())


def rename_md5(base_path, count=0):

    subfiles = os.listdir(base_path)

    for file in subfiles:
        subfile_path = os.path.join(base_path, file)

        if os.path.isdir(subfile_path):
            rename_md5(subfile_path,count)         ## recursion
        else:
            try:
                img = cv2.imread(subfile_path)
                if img is None:
                    os.remove(subfile_path)
                    continue
                md5 = get_md5(img)
                try:
                    os.rename(subfile_path,os.path.join(base_path, str(md5)+'.jpg'))
                except:
                    print('error')
                    os.remove(subfile_path)
                    continue
            except:
                print('error')
                os.remove(subfile_path)
                continue

            count += 1

            if count % 100 == 0:
                print('has finished:{}'.format(count))



if __name__ == '__main__':

    path = '/mnt/large2/wanglichun/data/diff_data/diff_middle_finger_kafka0706-newdocker/new_old_diff/new_not_old' 

    rename_md5(path)