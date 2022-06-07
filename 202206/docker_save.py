import os
import string
import random

import docker

client = docker.from_env()


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for _ in range(y))


for image in client.images.list():
    if len(image.tags):
        name = image.tags[0]
        if "/" in name:
            name = name.split('/')[-1]
        if ":" in name:
            name = name.replace(":", "_")
    else:
        print(image.tags)
        name = random_char(10)
    file_path = f'images/{name}.tar'
    if os.path.exists(file_path):
        continue
    with open(file_path, 'wb') as f:
        print(file_path)
        for chunk in image.save(named=True):
            f.write(chunk)
