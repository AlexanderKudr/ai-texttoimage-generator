from services.cloudinary import uploadToCDN

data = [
    {
        "imagePath": "img/photo-1686664219282-a1787f057706.jpeg",
        "caption": "a field of green grass with a blue sky",
    },
    {
        "imagePath": "img/photo-1686670179902-10fd23ce71a3.jpeg",
        "caption": "a mountain range with a sky background",
    },
    {
        "imagePath": "img/photo-1686824579901-9c90fd95b086.jpeg",
        "caption": "a large white boat floating on top of a sandy beach",
    },
]
print(uploadToCDN(data))
