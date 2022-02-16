import os, cv2
from PIL import Image

def FileTypeCheck(file):
    name, ext = os.path.splitext(file)

    type = None

    if ext == ".mp4":
        type = "VOD"

    elif ext == ".jpg" or ".png" or "jpeg":
        type = "IMG"

    return name, type

def GetFileInfo(file, type):

    if type == "IMG":

        imgInfo = Image.open(file)
        name = imgInfo.filename
        format = imgInfo.format
        size = imgInfo.size
        mode = imgInfo.mode
        width = imgInfo.width
        height = imgInfo.height
        HVType = None

        if int(width) > int(height):
            HVType = "landscape"

        elif int(width) < int(height):
            HVType = "portrait"

        elif int(width) == int(height):
            HVType = "square"

        imgDict = {'name': name, 'format': format,
                   'size': size, 'mode': mode,
                   'width': width, 'height': height,
                   'HVType': HVType}

        return imgDict

    else:
        vodInfo = cv2.VideoCapture(file)
        width = vodInfo.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = vodInfo.get(cv2.CAP_PROP_FRAME_HEIGHT)
        HVType = None

        if int(width) > int(height):
            HVType = "landscape"

        elif int(width) < int(height):
            HVType = "portrait"

        elif int(width) == int(height):
            HVType = "square"

        vodDict = {'width': width, 'height': height, 'HVType': HVType}

        return vodDict

def createDirectory(directory):

    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

            return directory
    except OSError:
        print('Error: Creating directory. ' + directory)

def CutFilePath(path, string):

    split_path = path.split(string)
    cut_path = split_path[1] + "thumbnail.jpg"
    print(cut_path)

    return cut_path






