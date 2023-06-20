import cloudinary

from utils import env


config = cloudinary.config(
    cloud_name=env("CLOUDINARY_NAME"),
    api_key=env("CLOUDINARY_API_KEY"),
    api_secret=env("CLOUDINARY_API_SECRET"),
)
print(config)