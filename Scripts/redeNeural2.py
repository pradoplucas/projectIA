import random
import numpy as np

# Classe da rede neural em si
class Neural(object):
    '''
    e -> Camada de Entrada
    o -> Camda Oculta
    s -> Camada de Saida
    '''
    def __init__(self, nos_e, nos_o, nos_s, data_pesos=None):
        self.nos_e = nos_e
        self.nos_o = nos_o
        self.nos_s = nos_s
        
        if data_pesos:
            self.bias_eo = data_pesos[0]
            self.bias_os = data_pesos[1]
            self.pesos_eo = data_pesos[2]
            self.pesos_os = data_pesos[3]
        else:
            # Matriz correspondente ao número de neurônios
            self.bias_eo = np.random.randn(self.nos_o, 1)
            self.bias_os = np.random.randn(self.nos_s, 1)

            # Para o projeto, vai ser considerado pesos com valores aleatorios mesmo
            # Mas existe estudo para uma melhor escolha dos pesos
            self.pesos_eo = np.random.randn(self.nos_o, self.nos_e)
            self.pesos_os = np.random.randn(self.nos_s, self.nos_o)

        self.taxa_aprendizagem = 0.1

    # Etapa de FEEDFORWARD, vou chamar de predict()
    def predict(self, vet):
        # Entrada -> oculta
        vet = np.array(vet)                                     # Transformando List em Numpy Array
        entrada = vet.reshape(vet.size, 1)                      # Transformando Vetor em Matriz de 1 coluna
        oculta = np.dot(self.pesos_eo, entrada) + self.bias_eo  # Fazendo o calculo dos valores de entrada para a camada oculta
        oculta = funcaoAtivacao(oculta)
        
        # Oculta -> Saída
        saida = np.dot(self.pesos_os, oculta) + self.bias_os    # Fazendo o calculo dos valores de saida
        saida = funcaoAtivacao(saida)

        return saida, oculta
    
    # Etapa de BACKPROPAGATION, vou chamar de train
    def train(self, entrada, resultado_esperado):
        saida, oculta = self.predict(entrada)
        entrada = np.array(entrada)
        entrada = entrada.reshape(entrada.size, 1)

        ### SAIDA -> OCULTA
        resultado_esperado = np.array(resultado_esperado)                                     # Transformando List em Numpy Array
        resultado_esperado = resultado_esperado.reshape(resultado_esperado.size, 1)           # Transformando Vetor em Matriz de 1 coluna
        erro_saida =  resultado_esperado - saida
        d_saida = funcaoAtivacaoDerivada(saida)     # Derivada do valor de saida obtido

        # np.multiply => Produto Hadamard
        gradiente = np.multiply(d_saida, erro_saida) * self.taxa_aprendizagem
        
        # Atualizando valor das bias da oculta
        self.bias_os += gradiente 
        

        # Atualizando pesos da camada oculta
        self.pesos_os += np.dot(gradiente, oculta.transpose())

        ### Oculta -> Entrada
        erro_oculta =  np.dot(self.pesos_os.transpose(), erro_saida)
        d_oculta = funcaoAtivacaoDerivada(oculta)

        gradiente_oculta = np.multiply(d_oculta, erro_oculta) * self.taxa_aprendizagem

        # Atualizando bias e pesos da ligação da entrada para a saida
        self.bias_eo += gradiente_oculta
        self.pesos_eo += np.dot(gradiente_oculta, entrada.transpose())

    ## Mutação
    def mutacao(self):
        '''
        0 -> bias_eo
        1 -> bias_os
        2 -> pesos_eo
        3 -> pesos_os
        '''
        pesos_selecionados = np.random.randint(0,3)
        tipo_mutacao = np.random.randint(0, 2)

        if pesos_selecionados == 0:
            i = np.random.randint(0, self.nos_o)
            self.bias_eo[i] = mutacaoMatriz(tipo_mutacao, self.bias_eo[i])
        elif pesos_selecionados == 1:
            i = np.random.randint(0, self.nos_s)
            self.bias_os[i] = mutacaoMatriz(tipo_mutacao, self.bias_os[i])
        elif pesos_selecionados == 2:
            i = np.random.randint(0, self.nos_o)
            j = np.random.randint(0, self.nos_e)
            self.pesos_eo[i,j] = mutacaoMatriz(tipo_mutacao, self.pesos_eo[i,j])
        elif pesos_selecionados == 3:
            i = np.random.randint(0, self.nos_s)
            j = np.random.randint(0, self.nos_o)
            self.pesos_os[i,j] = mutacaoMatriz(tipo_mutacao, self.pesos_os[i,j])


################################## Funcões de Ativacao #########################################
# Função genérica de ativação
def funcaoAtivacao(x):
    return relu(x)

# Derivada da Função genérica de ativação
def funcaoAtivacaoDerivada(x):
    return drelu(x)

# Função de Ativação Sigmóide
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Função para retornar as derivadas da função Sigmóide
def dsigmoid(x):
    return x * (1-x)

def relu(x):
    for i in range(len(x)):
        if(x[i] < 0):
            x[i] = 0
    return x

def drelu(x):
    for i in range(len(x)):
        if(x[i] < 0):
            x[i] = 0
        else:
            x[i] = 1
    return x

#Função para auxiliar a copiar valores
def copy(var1, var2):
    var1.nos_e = var2.nos_e
    var1.nos_o = var2.nos_o
    var1.nos_s = var2.nos_s
    var1.bias_eo = var2.bias_eo.copy()
    var1.bias_os = var2.bias_os.copy()
    var1.pesos_eo = var2.pesos_eo.copy()
    var1.pesos_os = var2.pesos_os.copy()

## Função para auxiliar na mutação
def mutacaoMatriz(tipo_mutacao, valor):
    if (tipo_mutacao == 0):         #Recebe valor aleatorio
        valor = np.random.randn()  
    elif (tipo_mutacao == 2):       #Multiplicacao Aleatoria
        multiplicador = (np.random.randint(0,10001)/10000) + 0.5
        valor *= multiplicador
    elif (tipo_mutacao == 3):       #Soma aleatoria
        somador = np.random.randint(0,100)
        valor += somador
    return valor
