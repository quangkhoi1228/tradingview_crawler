import os
import shutil


def writeFile(fileName, data):
    f = open(fileName, "w")
    f.write(data)
    f.close()


def clearFolder(path):
    shutil.rmtree(path)
    os.mkdir(path)


def getFileInPath(path):
    return os.listdir(path)
