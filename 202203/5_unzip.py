import gzip
import os
import tarfile
import zipfile
import rarfile


def un_zip(file_name):
    """unzip zip file"""
    temp = os.path.split(file_name)
    newfolder = temp[0] + '\\' + os.path.splitext(temp[1])[0]
    zip_file = zipfile.ZipFile(file_name)
    print(newfolder)
    for names in zip_file.namelist():
        zip_file.extract(names, path=newfolder)
    zip_file.close()


def un_rar(file_name):
    """unrar zip file"""
    temp = os.path.split(file_name)
    newfolder = temp[0] + '\\' + os.path.splitext(temp[1])[0]
    rar = rarfile.RarFile(file_name)
    for names in rar.namelist():
        rar.extract(names, path=newfolder, pwd="ewmJWTfrKM0QvBy7")
        rar.close()


def un_gz(file_name):
    """ungz zip file"""
    f_name = file_name.replace(".gz", "")
    # 获取文件的名称，去掉
    g_file = gzip.GzipFile(file_name)
    # 创建gzip对象
    open(f_name, "w+").write(g_file.read())
    # gzip对象用read()打开后，写入open()建立的文件里。
    g_file.close()


# tar
# XXX.tar.gz解压后得到XXX.tar，还要进一步解压出来。
# 注：tgz与tar.gz是同样的格式，老版本号DOS扩展名最多三个字符，故用tgz表示。
# 因为这里有多个文件，我们先读取全部文件名称。然后解压。例如以下：
# 注：tgz文件与tar文件同样的解压方法。
def un_tar(file_name):
    tar = tarfile.open(file_name)
    names = tar.getnames()
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    # 因为解压后是很多文件，预先建立同名目录
    for name in names:
        tar.extract(name, file_name + "_files/")
    tar.close()


path = r'D:\BaiduNetdiskDownload'

files = os.listdir(path)
files_rar = []
files_zip = []
for i in files:
    i = path + '\\' + i
    if os.path.isdir(i):
        continue
    elif os.path.isfile(i):
        if '.rar' == os.path.splitext(i)[1]:
            files_rar.append(i)
        if '.zip' == os.path.splitext(i)[1]:
            files_zip.append(i)
for r in files_rar:
    print(r, "unrar>>>>>>>>")
    un_rar(r)
    os.remove(r)
for z in files_zip:
    print(z, "unzip>>>>>>>>")
    try:
        un_zip(z)
        os.remove(z)
    except:
        print("faild")
