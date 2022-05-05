from logging.config import dictConfig
import pickle

diccionario = ("a diccionario", "including another diccionario", {"inner", "diccionario"})

with open('diccionario.bin','wb') as fh:
        pickle.dump(diccionario,fh)

print('done...')
