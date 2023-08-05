
  

<img  src="https://i.ibb.co/6tzcbWS/beewant-logo.png"/>

  

## What is Beewant Image Embedding?

  

<!-- <a href="https://i.ibb.co/6tzcbWS/beewant-logo.png" align="right" /></a> -->

  

Beewant Image Embedding is a powerful tool that utilizes a specific model to generate embeddings from image URLs. These embeddings represent high-dimensional numerical representations of the visual content, capturing the essence of the images in a condensed form. With Beewant, users can easily extract meaningful features from images, enabling various applications such as image similarity search and content-based recommendation systems.

  

- [Try out Beewant Image Embedding](#beewant-image-embedding)

- [Code explanations](#code-explanations)

- [API explanations](#api-explanations)

  

## Beewant Image Embedding

  

### Install

Run Beewant Image Embedding in a Docker container and access it at `http://localhost:5001`.

NB : Download the weights from the provided <a  href="https://ufile.io/e729vycs">link</a> . Copy the downloaded weights file into the clip folder.

  

```bash

docker  build  -t  image_embedding  -f  ./Dockerfile.Embedding  .

```
```bash


docker  run  -d  -p  5001:5001  image_embedding

```

### Inference

#### Server status

To check if the server is running, run the following command:

```bash

curl  -X  GET  http://localhost:5001/ping

```

#### Model status

To check if the model is loaded, run the following command:

```bash

curl  -X  GET  http://localhost:5001/health

```

#### Image embeddings

To get the images embeddings, run the following command:

```bash

curl -X POST http://localhost:5001/embed -H 'Content-Type: application/json' -d '{"image_urls": ["image_url_1", "image_url_2", ... , "image_url_n"]}'

```
image_urls : list of image urls
image_url : is the public image url

### Code explanations

-  `file_loader.py`: Implements the ImageLoader class for loading image files.

-  `model_embedder.py`: Defines the ModelEmbedder class for embedding images and text using the CLIP model.

-  `image_search.py`: Contains the Search class for performing image search based on text queries.

### API explanations

  
  
  

## Contributing

Contributions to the Beewant Image Embedding project are welcome! If you'd like to contribute, please follow these guidelines:


- Fork the repository.

- Create a new branch for your feature or bug fix.

- Make your changes and commit them with descriptive commit messages.

- Push your changes to your forked repository.

- Submit a pull request to the main repository.


## License

[Specify the license under which your project is distributed.]
