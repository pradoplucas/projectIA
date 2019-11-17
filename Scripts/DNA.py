import numpy as np

# Bestfitness por geração e Ever 
def BestFitness(self):
    Maior = 0
    for indiviudo in range(len(self)):
        if indiviudo.Fitness > Maior:
            Maior = indiviudo.Fitness
    return Maior

def MediaFitnessGeracao(self):
    Media = 0
    for indiviudo in range(len(self)):
        Media += indiviudo.Fitness
    Media = Media/float(len(self))
    return Media

# TamanhoDNA = Soma
def incializarDNA(self, DNAdaVez, SomaPesosTotal):
    for i in range(len(self)):
        for j in range(SomaPesosTotal): 
            DNAdaVez.append(np.random.randn())
