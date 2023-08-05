from typing import List
from PIL import Image
from io import BytesIO
from tqdm.auto import tqdm 

import requests

from bee_search.model_embedder import ModelEmbedder
from bee_search.file_loader import ImageLoader

class Search:
    def __init__(self,
                 image_dir_path : str = None,
                 model_dir : str = "clip"
                ):

        self.imageloader = ImageLoader(image_dir_path, traverse=True)
        self.embedder = ModelEmbedder(model_dir)
        
        self.image_dir_path =self.imageloader.search_tree()

    def embed_images(self):
        vectors = []
        new_files = self.update_file()
        
        for file_path in tqdm(new_files):
            image = Image.open(file_path) 
            vector = self.embedder.embed_images(image)
            vectors.append(vector)
            
        return vectors
    
    
    def embed_image(self, image_path ,url : bool= False) :
        
        if url : 
            response = requests.get(image_path)
            image = Image.open(BytesIO(response.content))
            
        else :
            image = Image.open(image_path)
           
        vector = self.embedder.embed_images(image)
            
        return vector, image_path   