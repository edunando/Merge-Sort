import random

class No:
    def __init__(self, carga: object = None, prox: 'No' = None):
        self.carga = carga
        self.prox = prox

    def __str__(self):
        return str(self.carga)


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.total = 0

    def adicionar_todos(self, lista: 'ListaEncadeada'):
        if self.cauda is not None:
            self.cauda.prox = lista.cabeca
        else:
            self.cauda = self.cabeca = lista
        self.total += lista.__len__()

    def __len__(self):
        return self.total

    def __iter__(self):
        atual: 'No' = self.cabeca
        while atual is not None:
            yield atual.carga
            atual = atual.prox

    def __setitem__(self, indice, valor):
        atual: 'No' = self.cabeca
        for i in range(0, indice):
            atual = atual.prox
        atual.carga = valor

    def __getitem__(self, indice):
        if isinstance(indice, slice):
            fatia = ListaEncadeada()
            atual: 'No' = self.cabeca
            
            inicio = indice.start if indice.start else 0
            final = indice.stop if indice.stop else self.total

            for i in range(final):
                if i >= inicio:
                    fatia.inserir_valor_no_final(atual.carga)
                atual = atual.prox
            return fatia
        else:
            atual: 'No' = self.cabeca
            for i in range(indice): 
                atual = atual.prox
            return atual.carga

    def inserir_valor_no_inicio(self, valor: object):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo 
        else:
            novo.prox = self.cabeca
            self.cabeca = novo
        self.total += 1

    def imprimir_lista(self):
        if self.cabeca is None:
            print("Lista Vazia")
            return
        atual: 'No' = self.cabeca
        while atual is not None:
            print(str(atual.carga) + " ", end='')
            atual = atual.prox
        print()

    def inserir_valor_no_final(self, valor):
        novo = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo 
        else:
            self.cauda.prox = novo
            self.cauda = novo
        self.total += 1

    def inserir_todos(self, vetor):
      for item in vetor:
        self.inserir_valor_no_final(item)

    def remover_do_inicio(self):
        if self.cabeca is None:
            print("Lista vazia")
            return
        
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox
        self.total -= 1    

    def remover_do_final(self):
        if self.cabeca is None:
            print("Lista vazia")
            return
        
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            atual: 'No' = self.cabeca
            while atual.prox is not self.cauda:
                atual = atual.prox

            self.cauda = atual
            atual.prox = None
        self.total -= 1

def lista_numeros_aleatorios(qtd=100):
    vetor = random.sample(range(0,999), qtd)
    lista = ListaEncadeada()
    for item in vetor:
        lista.inserir_valor_no_final(item)
    return lista



#Algoritmo de Ordena????o Merge Sort
def merge(esquerda, direita, vetor):
    i,j,k = 0,0,0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            vetor[k] = esquerda[i]
            i, k = i+1, k+1
        else:
            vetor[k] = direita[j]
            j,k = j+1,k+1
                    
    while i < len(esquerda):
        vetor[k] = esquerda[i]
        i, k = i+1, k+1

    while j < len(direita):
        vetor[k] = direita[j]
        j,k = j+1,k+1

def mergesort(vetor):
    if len(vetor) < 2: return vetor
    meio = len(vetor) // 2
    esquerda = vetor[:meio]
    direita = vetor[meio:]
    mergesort(esquerda)
    mergesort(direita)
    merge(esquerda, direita, vetor)

def main():
    lista = lista_numeros_aleatorios(100)
    lista.imprimir_lista()
    mergesort(lista)
    lista.imprimir_lista()
    print(type(lista))
    
if __name__ == '__main__':
    import timeit
    main()
    ## TODO - ajustar trecho abaixo para medir corretamente o tempo de execu????o do algoritmo
    print(timeit.timeit("lista=lista_numeros_aleatorios(100); mergesort(lista)", setup="from __main__ import mergesort; from __main__ import lista_numeros_aleatorios", number=1000))
