import os


def getImagesFromFolder(folder: str) -> list[str]:
    replaceBackslashes = lambda x: os.path.join(folder, x.replace("\\", "/"))
    jpegFiles = filter(lambda x: x.endswith(".jpeg"), os.listdir(folder))

    return list(map(replaceBackslashes, jpegFiles))


someData = 5


def get_name_and_age():
    return getImagesFromFolder, someData