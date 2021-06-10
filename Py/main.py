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
import sklearn
import psycopg2

params = config()
# connect to the PostgreSQL server
connection = psycopg2.connect(**params)
# create a cursor
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)



