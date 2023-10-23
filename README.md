# luminova-ai-model
Part of the luminova project [link](https://github.com/AlexanderKudr/luminova)


## Generate text caption from images
>  Also you can upload images payload to CDN

---
## To start using project, run:
1. "pip install pipenv --user" (or create requirements.txt file to run pip install -r requirements.txt, packages in Pipfile)
2. "pipenv install" (here venv should be created or run "pipenv shell" if it wasn't)
3. "pipenv run ai" or "pipenv run cdn"
4. run "pipenv run ai" with images in "img" folder
5. then add generated array to data in uploadToCDN.py file or use it as you wish

> Optional
- "exit" in terminal to deactivate venv
- skip first step and install things manually through pip and activate venv by yourself



## Here goes info and credits about model

tags:
- image-to-text
- image-captioning
license: apache-2.0
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/savanna.jpg
  example_title: Savanna
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/football-match.jpg
  example_title: Football Match
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/airport.jpg
  example_title: Airport

### nlpconnect/vit-gpt2-image-captioning

This is an image captioning model trained by @ydshieh in [flax ](https://github.com/huggingface/transformers/tree/main/examples/flax/image-captioning) this is pytorch version of [this](https://huggingface.co/ydshieh/vit-gpt2-coco-en-ckpts).


### The Illustrated Image Captioning using transformers

![](https://ankur3107.github.io/assets/images/vision-encoder-decoder.png)

* https://ankur3107.github.io/blogs/the-illustrated-image-captioning-using-transformers/
