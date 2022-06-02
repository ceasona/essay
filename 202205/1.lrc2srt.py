#!/usr/bin/python3
from datetime import datetime
import sys
import os.path

'''
Author:danielchc
Version: 16092018
'''


def convertTime(time):
    t = datetime.strptime(time, '%M:%S.%f')
    return "{}:{}:{},{}".format(str(t.hour).zfill(2), str(t.minute).zfill(2), str(t.second).zfill(2),
                                str(t.microsecond)[:3].zfill(3))


# return datetime.strftime("%H:%M:%S,%f",t)
def loadLRC(file):
    lyrics = []
    with open(file, encoding="utf-8") as f:
        for l in f.readlines():
            xi = l.split(":")
            if (len(xi) == 2) and xi[0][1:].isdigit():
                sp = l.split("]")
                if len(sp) == 2:
                    time = sp[0][1:]
                    lyric = sp[1].strip()
                    cur = {"time": time, "lyric": lyric}
                    lyrics.append(cur)
    return lyrics


def convertSRT(lyricsArray):
    '''
    2
    0:00:11,28 --> 0:00:14,28
    You got to keep you head held high
    '''
    output = ""
    for i in range(1, len(lyricsArray) + 1):
        timeEnd = lyricsArray[i - 1]["time"] if i >= len(lyricsArray) else lyricsArray[i]["time"]
        lyric = "{}\n{} --> {}\n{}\n\n".format(i, convertTime(lyricsArray[i - 1]["time"]), convertTime(timeEnd),
                                               lyricsArray[i - 1]["lyric"])
        output += lyric
    return output


if len(sys.argv) == 3:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[2], "w", encoding="utf-8") as w:
            w.write(convertSRT(loadLRC(sys.argv[1])))
    else:
        print("Error! File {} not exist".format(sys.argv[1]))
else:
    print(
        "lrctosrt.py 0.1\nAuthor: danielchc\nWebsite: danielchc.github.io\n\tSyntax: lrctosrt.py <file.lrc> <output.srt>")
