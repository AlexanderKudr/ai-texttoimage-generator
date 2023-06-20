import cloudinary
import cloudinary.uploader
import cloudinary.api

cdn = cloudinary.uploader


def uploadToCDN(images):
    for image in images:
        uploadResult = cdn.upload(
            image.get("imagePath"),
            public_id=image.get("caption"),
            folder="wallpapers",
            overwrite=True,
            resource_type="image",
        )

    return
