# Primeros pasos
# Crear base doc2vec 
# https://towardsdatascience.com/detecting-document-similarity-with-doc2vec-f8289a9a7db7
# https://radimrehurek.com/gensim/auto_examples/tutorials/run_doc2vec_lee.html#sphx-glr-auto-examples-tutorials-run-doc2vec-lee-py
# https://rdu.unc.edu.ar/bitstream/handle/11086/11342/Tesis_de_Agust_n_Capello.pdf?sequence=1&isAllowed=y

# Estructura de tabla de fallos
# public.jur_fallos
#  |-idfallo (integer)
#  |-descripcion (character varying)
#  |-sentencia (bytea)
#  |-caratula (character varying)
#  |-expediente (character varying)
#  |-fecha_fallo (date)
#  |-fecha_carga (date)
#  |-idorganismo (integer)
#  |-pdf2 (bytea)
#  |-pdf3 (bytea)
#  |-pdf4 (bytea)
#  |-pdf5 (bytea)
#  |-idestado (smallint)
#  |-usuario (character varying)
#  |-usuario_control (character varying)
#  |-observacion_carga (text)
#  |-observacion_ctrl (text)
#  |-fecha_control (date)
#  |-pdf_tsv (tsvector)
#  |-pdf_txt (text)
#  |-tema_sugerido (character varying)


##############################################################################
# Elementos identificacion
# idfallo


###############################################################################

# Exploracion
cursor = connection.cursor()
postgreSQL_select_Query = "select * from public.jur_fallos"
cursor.execute(postgreSQL_select_Query)
fallos = cursor.fetchall()


# Exploracion de tablas
len(fallos)
fallo3 = fallos[3]
fallo3.__class__
fallo3[2:5]
print(fallo3[-2])
# Cada tupla tiene 21 elementos
# El texto fallo está anidado en cada elemento de la tupla -2:
print(fallos[11196][-2])
print(len(fallos[3]))

# Creando array fallos
np.array(fallos[3])

# Pasar a lista para procesar

#------------------------------
# Extraer jur.sumarios y jur.sumarios.voces

# public.jur_sumarios
#  |-idsumario (integer)
#  |-idfallo (integer)
#  |-idmateria (integer)
#  |-fecha_sumario (date)
#  |-titulo_sumario (character varying)
#  |-memo (text)
#  |-voces_sugeridas (character varying)
#  |-idestado (smallint)
#  |-usuario (character varying)
#  |-usuario_control (character varying)
#  |-observacion_carga (text)
#  |-observacion_ctrl (text)
#  |-fecha_carga (date)
#  |-fecha_control (date)
#  |-tsv (tsvector)


cursor = connection.cursor()
postgreSQL_select_Query = "select * from public.jur_sumarios"
cursor.execute(postgreSQL_select_Query)
sumarios = cursor.fetchall()

# Exploracion Sumarios
len(sumarios)
sumarios[1]
np.array(sumarios[1])


