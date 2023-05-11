class nodo: 

    #Constructor Nodo

    def __init__(self, valor): 
        self. valor = valor
        self.siguiente = None

    #Método Ver el valor

    def devolver_valor(self): 
        print(self.valor)

    #Método asginar

    def asignar_siguiente(self, Nodo):
        self.siguiente = Nodo
    
    #Método cambiar el valor

    def cambiar_valor(self, nuevo_valor):
        self.valor = nuevo_valor

Nodo1 = nodo("A")
Nodo2 = nodo("C")

# Obtener valor
print (Nodo1.valor)

# Obtener valor siguiente
print (Nodo1.siguiente)

# Primera forma
Nodo1.devolver_valor()

#Segunda forma
nodo.devolver_valor(Nodo1)

# Cambiar valor del Nodo
Nodo1.cambiar_valor("B")

Nodo1.devolver_valor()

# Asignar siguiente valor

Nodo1.asignar_siguiente(Nodo2)

print(Nodo1.siguiente)
