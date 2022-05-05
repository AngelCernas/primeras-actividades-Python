#tupla 
import pickle

tupla=("a tupla", "including another tupla", ("inner", "tupla"))
with open('tupla.bin','wb') as fh:
        pickle.dump(tupla,fh)

print('done...')
 
print (tupla)
