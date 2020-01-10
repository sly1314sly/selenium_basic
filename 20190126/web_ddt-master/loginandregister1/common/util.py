
import time
import os
import logging

def getRootPath():
    rootpath = os.path.dirname(os.path.abspath(__file__))
    while rootpath:
        if os.path.exists(os.path.join(rootpath, 'README.md')):
            break
        rootpath = rootpath[0:rootpath.rfind(os.path.sep)]

    return rootpath

def getScreenShotsPath():
    rootPath = getRootPath()
    screenshotpath = os.path.join(rootPath, 'report', "screenshots")
    if not os.path.exists(screenshotpath):
        os.makedirs(screenshotpath)
    return screenshotpath


    
def getPngfileName():
    screenshotsDir = getScreenShotDir()
    current_time = time.time()

    # TODO filename 2018_05_27_15_48_30.png
    # http://www.runoob.com/python/python-date-time.html
    filename = os.path.join(screenshotsDir,str(current_time)+'.png')
    return filename
    
def getLogger(name):
    loggerFile = os.path.join(getRootPath(),'log','example.log')
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

    file_handler = logging.FileHandler(loggerFile)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    
    return logger
