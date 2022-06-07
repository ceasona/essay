import glob
import docker

client = docker.from_env()

for i in glob.glob("images/*.tar"):
    with open(i, 'rb') as fr:
        data = fr.read()
        print(i)
        client.images.load(data)