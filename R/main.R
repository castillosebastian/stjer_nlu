library(reticulate)
#use_virtualenv('/home/scastillo/stjer_nlu/pythonenv')

# check config
reticulate::py_config()

# Instalar librerias
#py_install("requests")
#py_install("scipy")
#py_install("matplotlib")
#py_install("google.colab")
#py_install("sklearn")
#py_install("psycopg2")
#py_install("dash")
#py_install("Jinja2")

reticulate::source_python('~/stjer_nlu/Py/config.py')
reticulate::source_python('~/stjer_nlu/Py/connect.py')
reticulate::source_python('~/stjer_nlu/Py/main.py')