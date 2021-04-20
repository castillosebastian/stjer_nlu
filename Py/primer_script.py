# primer script
# source:
## https://colab.research.google.com/drive/1n_X-r1mXG5Z0VBkOHC9AtjO1lyY-kSpl#scrollTo=sVVbXUmIUhpB
## https://colab.research.google.com/drive/1pdLNJPU7PEhhRUI8fPLx5iNaL4MTEH-T
## https://colab.research.google.com/drive/1bthcNIKqaFRpb-TpbXTMNsKOVdyqnlh7

# Prueba lectura datos primarios scba bd de prueba y exploracion
with open('/home/scastillo/stjer_nlu/data/tbfallos.json', 'r') as myfile:
  data1=myfile.read()
# parse file
tbfallos = json.loads(data1)
tbfallos = pd.DataFrame.from_dict(tbfallos)
tbfallos['textos_fallo'][1]
tbfallos.head()

# Trabajar con Stanza
# Prueba_stanza_OK: 
# To see Stanza’s neural pipeline in action, you can launch the Python interactive interpreter, 
# and try the following commands
#stanza.download('en') # download English model
#nlp = stanza.Pipeline('en') # initialize English neural pipeline
#doc = nlp("Barack Obama was born in Hawaii.") # run annotation over a sentence
# You should be able to see all the annotations in the example by running the following commands
#print(doc)
#print(doc.entities)

# Segunda Prueba Stanza_OK:
# Prueba tokenizacion de un sumario
stanza.download('es') # download spanish model
fallos = tbfallos['textos_fallo'][1]
fallos = fallos.replace("#","\n\n")
# creacion objeto stanza
nlp = stanza.Pipeline(lang='es', processors='tokenize,ner,mwt,pos,lemma,depparse', tokenize_no_ssplit=True)
doc = nlp(fallos)
# exploracion de resultados
doc.sentences[0].text

for sent in doc.sentences:
    print(sent.text)

for i, sentence in enumerate(doc.sentences):
    print(f'====== Sentence {i+1} tokens =======')
    print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')
    
dicts = doc.to_dict() # create a dictionary

# Prueba de manipulacion objeto doc sobre un sumario_OK:
def print_doc_info(doc):
    print(f"Num sentences:\t{len(doc.sentences)}")
    print(f"Num tokens:\t{doc.num_tokens}")
    print(f"Num words:\t{doc.num_words}")
    print(f"Num entities:\t{len(doc.entities)}")
print_doc_info(doc)

def word_info_df(doc):
    """
    - Parameters: doc (a Stanza Document object)
    - Returns: A Pandas DataFrame object with one row for each token in
      doc, and columns for text, lemma, upos, and xpos.
    """
    rows = []
    for sentence in doc.sentences:
        for word in sentence.words:
            row = {
                "text": word.text,
                "lemma": word.lemma,
                "upos": word.upos,
                "xpos": word.xpos,
            }
            rows.append(row)
    return pd.DataFrame(rows)

word_info_df(doc)
doc.num_words

# Prueba sobre entidades de un sumario_OK:
print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n')[1]

# select person entities
def select_person_entities(doc):
    return [ent for ent in doc.entities if ent.type == "PER"]
    
def person_df(doc):
    """
    - Parameters: doc (a Stanza Document object)
    - Returns: A Pandas DataFrame with one row for each entity in doc
      that has a "PERSON" type, and and columns text, type, start_char.
    """
    rows = []
    persons = select_person_entities(doc)
    for person in persons:
        row = {
            "text": person.text,
            "type": person.type,
            "start_char": person.start_char,
            "end_char": person.end_char
        }
        rows.append(row)
    return pd.DataFrame(rows)
    
person_df(doc)

# Pruebas de manipulacion de objeto
for i, sent in enumerate(doc.sentences):
  sent.print_tokens()

# Iterate over all tokens in all sentences
for i, sent in enumerate(doc.sentences):    
    for t in sent.tokens:
        print(t.text)
        
# Iterate over all words in all sentences
for i, sent in enumerate(doc.sentences):    
    for w in sent.words:
        print(w.text)
        
# Iterate over all entities in all sentences
for i, sent in enumerate(doc.sentences):    
    for e in sent.entities:
        print(e.text)
        
# Iterate over all llemmas in all sentences
for i, sent in enumerate(doc.sentences):    
    for w in sent.words:
        print(w.lemma)
        
# NEXT STEP: Continuar con armado de matriz docxword con STANZA:

# Word count Matrix of documents with SKLEARN_OK:
from sklearn.feature_extraction.text import CountVectorizer
df = tbfallos['textos_fallo']

cv = CountVectorizer()
cv.fit(df)
results = cv.transform(df)

print(results.shape) # Sparse matrix

features = cv.get_feature_names()
df_res = pd.DataFrame(results.toarray(), columns=features)

df_res.head()
