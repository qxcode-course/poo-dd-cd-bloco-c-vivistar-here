
class Foo:
    def __init__(self, quantidade: int):
        self.quantidade = 0

    def __str__(self):
        return f'Foo({self.quantidade})'

lista_vazia: list[int] = []
lista_preenchida: list[int] = [1, 2, 3, 4, 5]
lista_preenchida_objetos: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]

lista_vazia.append(1)
lista_preenchida.append(Foo(6))

lista_numeros: list[int] = [1, 2, 3, 4, 5]
lista_dobrados: list[int] = [x * 10 for x in lista_numeros]
lista_numerosmaiores: list[int] = [10, 20, 30, 40, 50]

lista_numeros.append(6)
lista_numeros.remove(1)
lista_numerosmaiores[2] = 99



print(lista_numeros)
print(lista_dobrados)
print(lista_numerosmaiores)
