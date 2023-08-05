from setuptools import setup, find_packages

setup(
    name='beewant',
    version='0.0.1',
    url='https://github.com/Beewant/beewant',
    author='Beewant',
    author_email='contact@beewant.fr',
    description='Beesearch enables you to search through unstructured data using customized foundation models',
    packages=find_packages(),    
    install_requires=['uvicorn', 'fastapi', 'torch', 'torchvision', 'matplotlib', 'transformers', 'pillow', 'typing', 'loguru', 'tqdm', 'googletrans >= 3.1.0a0', 'python-multipart', 'weaviate-client'],
)
