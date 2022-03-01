import os
import zipfile

path = "/home"
compress_li = ["run.sh"]
zip_full_path = path + os.sep + f"model_result.zip"
z = zipfile.ZipFile(zip_full_path, 'w')
for d in compress_li:
    file_path = os.path.join(path, d)
    z.write(file_path, d)
z.close()


def un_zip(file_name):
    """unzip zip file"""
    temp = os.path.split(file_name)
    newfolder = temp[0] + '\\' + os.path.splitext(temp[1])[0]
    zip_file = zipfile.ZipFile(file_name)
    print(newfolder)
    for names in zip_file.namelist():
        zip_file.extract(names, path=newfolder)
    zip_file.close()
