import random
import numpy as np
import dinoRedeNeural as rn

RangeRandom = 30 # O ideal é ser a quantidade de pesos da rede Neural
TamanhoPopulacao = 0
NumGeracaoEpoca = 0


#Vai retornar os dois filhos..
def defCrossover(var1, var2):
    Var1EO = rn.Neural(5,5,1)
    Var2EO = rn.Neural(5,5,1)

    for j in range(0, 3):
        for k in range(0,5):
            Var1EO.pesos_eo[j][k] = var1.pesos_eo[j][k]
            Var2EO.pesos_eo[j][k] = var2.pesos_eo[j][k]

    for j in range(3, 5):
        for k in range(0, 5):
            Var1EO.pesos_eo[j][k] = var2.pesos_eo[j][k]
            Var2EO.pesos_eo[j][k] = var1.pesos_eo[j][k] 

    return Var1EO, Var2EO

def defCopy(dino):
    for j in range(135):
        dino[j + 15].cerebro = dino[j].cerebro

def geneticCrossover(dino):
    #global dino

    #Colocando os indivíduos selecionados nas primeiras posições
    rn.copy(dino[2].cerebro, dino[3].cerebro)
    rn.copy(dino[3].cerebro, dino[7].cerebro)
    rn.copy(dino[4].cerebro, dino[15].cerebro)
    rn.copy(dino[5].cerebro, dino[31].cerebro)

    dino[6].cerebro, dino[7].cerebro = defCrossover(dino[0].cerebro, dino[1].cerebro)
    dino[8].cerebro, dino[9].cerebro = defCrossover(dino[0].cerebro, dino[2].cerebro)
    dino[10].cerebro, dino[11].cerebro = defCrossover(dino[1].cerebro, dino[2].cerebro)
    dino[12].cerebro, dino[13].cerebro = defCrossover(dino[1].cerebro, dino[3].cerebro)
    dino[14].cerebro, dino[15].cerebro = defCrossover(dino[4].cerebro, dino[5].cerebro)

    defCopy(dino)

def GeneticChanges(dino):
    global RangeRandom, NumGeracaoEpoca
    #Ordenação de dino por score
    aux_trocar=dino[0].cerebro
    for i in range(TamanhoPopulacao):
        for j in range(TamanhoPopulacao-1):
            if(dino[j].score < dino[j+1].score):
                # Trocando "Cerebro"
                rn.copy(aux_trocar, dino[j].cerebro)
                rn.copy(dino[j].cerebro, dino[j+1].cerebro)
                rn.copy(dino[j+1].cerebro, aux_trocar)

    geneticCrossover(dino)

    #Aplicando random mutations
    for i in range(15, TamanhoPopulacao):
        mutations = np.random.randint(0, int(RangeRandom)) + 1

        for j in range(mutations):
            dino[i].cerebro.mutacao()

    testTest = 'Geração: ' + str(NumGeracaoEpoca + 1)
    testTest += '\n\n--Bias_EO-- \n' + str(dino[0].cerebro.bias_eo)
    testTest += '\n\n--Bias_OS--\n' + str(dino[0].cerebro.bias_os)
    testTest += '\n\n--Pesos_EO--\n' + str(dino[0].cerebro.pesos_eo)
    testTest += '\n\n--Pesos_OS--\n' + str(dino[0].cerebro.pesos_os)
    testTest += '\n\n\n==============================================================='

    writeFile(testTest)

    RangeRandom *= 0.97
    if RangeRandom < 10:
        RangeRandom = 10

def writeFile(text):
    with open('bests.txt', 'a') as file:
        file.write(text + '\n\n')
