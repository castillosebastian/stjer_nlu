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
import plotly

params = config()
# connect to the PostgreSQL server
connection = psycopg2.connect(**params)
# create a cursor
#cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)



