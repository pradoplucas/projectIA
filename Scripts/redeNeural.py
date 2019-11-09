import random
import numpy as np

# Função de Ativação Sigmóide
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Função para retornar as derivadas da função Sigmóide
def derivada_sigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))

# Classe da rede neural em si
class Neural(object):
    def __init__(self, sizes):
        self.num_camadas = len(sizes)
        self.sizes = sizes
        self.bias = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
    
    '''
    A função feedforward aplica a equação : a' = sigmoid(wa + b)
    Onde a é o vetor de ativações da segunda camada de neurônios
    Retorna a saída da rede se `a` for input.
    '''
    def feedforward(self, a):
        for b, w in zip(self.bias, self.weights):
            # Dot -> faz a multiplicação matricial
            a = sigmoid(np.dot(w, a) + b)
        return a

    def train(self, training_data , epocas, mini_lotes_size, learning_rate, test_data = None):
        training_data = list(training_data)
        n = len(training_data)

        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)
        
        for j in range(epocas):
            random.shuffle(training_data)
            mini_lotes = [training_data[k:k+mini_lotes_size] for k in range(0, n, mini_lotes_size)]

            for mini_lote in mini_lotes:
                self.update_mini_lote(mini_lote, learning_rate)
            
            if test_data:
                print("Epoca {} : {} / {}".format(j,self.evaluate(test_data),n_test))
            else:
                print("Epoca {} finalizada".format(j))

    # Função que funciona calculando os gradientes para cada exemplo de treinamento, atualizando valores dos bias e weights
    def update_mini_lote(self, mini_lote, learning_rate):
        nabla_b = [np.zeros(b.shape) for b in self.bias]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        for x, y in mini_lote:
            delta_nabla_b, delta_nabla_w = self.backpropagation(x, y)
            nabla_b = [np.zeros(b.shape) for b in self.bias]
            nabla_w = [np.zeros(w.shape) for w in self.weights]
        
        self.weights = [w-(learning_rate/len(mini_lote))*nw for w, nw in zip(self.weights, nabla_w)]
        self.bias = [b-(learning_rate/len(mini_lote))*nb for b, nb in zip(self.bias, nabla_b)]

    
    def backpropagation(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.bias]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        #Feedforward
        activation = x

        # Lista para armazenar todas as ativações, camada por camada
        activation_list = [x]

        # Lista para armazenar todos os vetores z, camada por camada
        z_list = []

        for b, w in zip(self.bias, self.weights):
            z = np.dot(w, activation) + b
            z_list.append(z)
            activation = sigmoid(z)
            activation_list.append(activation)
        
        # Backward Pass
        delta = self.cost_derivative(activation_list[-1], y) * derivada_sigmoid(z_list[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activation_list[-2].transpose())

        for l in range(2, self.num_camadas):
            z = z_list[-l]
            sp = derivada_sigmoid(z)
            delta = np.dot(self.weights[-l + 1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, self.weights[-l+1].transpose())
        
        return (nabla_b, nabla_w)
    
    def evaluate(self, test_data):
        """Retorna o número de entradas de teste para as quais a rede neural 
         produz o resultado correto. Note que a saída da rede neural
         é considerada o índice de qualquer que seja
         neurônio na camada final que tenha a maior ativação."""

        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        # Retorna o vetor das derivadas parciais.
        return (output_activations-y)
