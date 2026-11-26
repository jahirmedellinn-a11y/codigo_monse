from collections import deque

def preorden(nodo):
    if nodo is not None:
        print(nodo.valor)
        preorden(nodo.izquierdo)
        preorden(nodo.derecho)

def inorden(nodo):
    if nodo is not None:
        inorden(nodo.izquierdo)
        print(nodo.valor)
        inorden(nodo.derecho)

def postorden(nodo):
    if nodo is not None:
        postorden(nodo.izquierdo)
        postorden(nodo.derecho)
        print(nodo.valor)

def por_niveles(raiz):
    if raiz is None:
        return
    
    cola = deque([raiz])
    
    while cola:
        nodo = cola.popleft()
        print(nodo.valor)
        
        if nodo.izquierdo is not None:
            cola.append(nodo.izquierdo)
            
        if nodo.derecho is not None:
            cola.append(nodo.derecho)