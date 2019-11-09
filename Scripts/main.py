import redeNeural2 as rn
import numpy as np
import time

'''
#nn = rn.Neural(2, 3, 1)
#print(nn.predict([2, 1]))



####### Testes matrizes
array1 = np.array([[2, 2], [1, 1]])
array2 = np.array([[2, 1], [3, 4]])
bias = np.array([[1], [3], [5]])

array3 = np.multiply(array2, array1)

print(np.dot(array2, array1))
print(array3.transpose())
'''


nn = rn.Neural(2, 3, 2)

# XOR
dataset = {
    'inputs': [[1, 1], [1, 0], [0, 1], [0, 0]],
    'outputs': [[0], [1], [1], [0]]
}

# testando rede neural
train = True
tempo_inicio = time.time()
cont = 0
while train:
    for i in range(0, 1000):
        i = np.random.randint(0,4)
        nn.train(dataset['inputs'][i], dataset['outputs'][i])
        cont += 1

    saida1, oculta1 = nn.predict([0, 0])
    saida2, oculta2 = nn.predict([1, 0])
    if  (saida1[0] < 0.1 and saida2[0] > 0.9) or time.time() - tempo_inicio > 60:
        train = False
        print("Treino terminado!!!")

print('Tempo:  %.3f' %(time.time() - tempo_inicio))
print('Previsão: %.3f' %nn.predict([1, 1])[0][0])
print('Qtd treinos: %d' %cont)
