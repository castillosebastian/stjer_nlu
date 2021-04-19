# Instalar python y ambiente de trabajo:
# https://support.rstudio.com/hc/en-us/articles/360023654474-Installing-and-Configuring-Python-with-RStudio
# https://rstudio.github.io/reticulate/articles/python_packages.html

# Activar ambiente
# use_virtualenv("pythonenv")

# # Libraries, tools and thanks 
import bs4 
import nltk
import pandas as pd
import io
import requests
#from google.colab import drive
import numpy as np 
import json
import stanza
import scipy
import matplotlib
import os
from os import listdir

# prueba_stanza_OK: 
# To see Stanza’s neural pipeline in action, you can launch the Python interactive interpreter, 
# and try the following commands
#stanza.download('en') # download English model
#nlp = stanza.Pipeline('en') # initialize English neural pipeline
#doc = nlp("Barack Obama was born in Hawaii.") # run annotation over a sentence
# You should be able to see all the annotations in the example by running the following commands
#print(doc)
#print(doc.entities)

# Lectura de datos primarios
with open('tbfallos.json', 'r') as myfile:
  data1=myfile.read()
# parse file
tbfallos = json.loads(data1)
tbfallos = pd.DataFrame.from_dict(tbfallos)
tbfallos['textos_fallo'][1]
tbfallos.head()

