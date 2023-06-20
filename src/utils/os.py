import os


def getImagesFromFolder(folder: str) -> list[str]:
    jpegFiles = filter(lambda x: x.endswith(".jpeg"), os.listdir(folder))

    return list(map(lambda x: os.path.join(folder, x), jpegFiles))
