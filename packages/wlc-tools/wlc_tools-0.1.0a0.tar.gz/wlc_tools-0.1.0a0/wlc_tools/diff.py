import os
import shutil

def diff(path_fold_1, path_fold_2, name_1, name_2, path_result, delimiter='_'):

    image_names_1 = os.listdir(path_fold_1)
    image_names_2 = os.listdir(path_fold_2)

    image_names_1_map = {}

    for name in image_names_1:
        if isinstance(delimiter, str):
            pos = name.rfind(delimiter)
        elif isinstance(delimiter, int):
            pos = delimiter
        image_names_1_map[name[pos:]] = name


    image_names_2_map = {}

    for name in image_names_2:
        
        if isinstance(delimiter, str):
            pos = name.rfind(delimiter)
        elif isinstance(delimiter, int):
            pos = delimiter

        image_names_2_map[name[pos:]] = name


    result_base_path = os.path.join(path_result,name_1 + '_'+ name_2 + '_diff')

    if not os.path.exists(  result_base_path ):
        os.makedirs(  result_base_path )

    result_base_path_1 = os.path.join(result_base_path, name_1+'_not_'+ name_2)
    result_base_path_2 = os.path.join(result_base_path, name_2+'_not_'+ name_1)

    if not os.path.exists( result_base_path_1 ):
        os.mkdir( result_base_path_1 )

    if not os.path.exists( result_base_path_2 ):
        os.mkdir( result_base_path_2 )


    i = 0
    count = 0
    for key in image_names_1_map.keys():
        if not key in image_names_2_map:
            src_path = os.path.join(path_fold_1, image_names_1_map[key] )
            dst_path = os.path.join(result_base_path_1, image_names_1_map[key] )
            shutil.copyfile(src_path,dst_path)
            count += 1
        i += 1

    print('{} in {} not in {}'.format(count, name_1, name_2))

    i = 0
    count = 0
    for key in image_names_2_map.keys():
        if not key in image_names_1_map:
            src_path = os.path.join(path_fold_2, image_names_2_map[key])
            dst_path = os.path.join(result_base_path_2, image_names_2_map[key])
            shutil.copyfile(src_path,dst_path)
            count += 1
        i += 1

    print('{} in {} not in {}'.format(count, name_2, name_1))




if __name__ == '__main__':

    path_fold_1 = '/mnt/data3/wanglichun/download-online-data/wrapper/first_stage/0620_ran/data_9002/bath_towel/'

    path_fold_2 = '/mnt/data3/wanglichun/download-online-data/wrapper/first_stage/0620_ran/data_9003/bath_towel/'


    fold_tag = 'diff_middle_finger_kafka0706-newdocker'

    name_1 = 'new'
    name_2 = 'old'

    path_result = '/mnt/data3/wanglichun/data/diff_data/' + fold_tag

    delimiter = '-'

    diff(path_fold_1, path_fold_2, name_1, name_2, path_result, delimiter)