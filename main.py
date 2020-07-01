import numpy as np

array=np.array([2,4,56,8,98])

def MaxOfArray(array):
  return np.max(array)
  print(MaxOfArray)


a=np.array([2,4,5])
b=["asf","asfh","hkjhsdf"]
c="casa"
d={"name":5}
l=(3,5)
print()

#Differenza tra array e lista è che la lista è un contenitore di oggetti

listval=[a,b,c,d,l]

#L'array è numerico e si possono fare delle operazioni negli oggetti contenuti all'interno

#La lista ha una dimensione, l'array ha una shape, cioè può avere più dimensioni, come una matrice, mentre una lista è vettoriale

a2=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a2.shape)

#Come vediamo qua ci da la shape di a2 che ha 3 righe e 3 colonne