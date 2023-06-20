import os


def env(key: str):
    return os.environ.get(key)
