import nltk

try:
    nltk,download('puntk')
    pint(" NLTK punkt descargado correctamente")
except Exception as e:
    print("Error durante la descarga:",e)
    