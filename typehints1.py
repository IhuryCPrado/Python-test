from typing import List, Union, Tuple, Dict, Any, NewType, Callable, Sequence, Iterable

# Primitivos
numero: int = 10
flutuante: float = 1.0
booleano: bool = False
string: str = "Ihury Prado"

# Sequências
lista1: list = [1, 2, 3]
lista2: List[int] = [1, 2, 3]
lista3: List[Union[int, str]] = [1, 2, 3, "Ihury"]
tupla1: tuple = (1, 2, 3, "Ihury")
tupla2: Tuple[int, int, int, str] = (1, 2, 3, "Ihury")

# Dicionários e Conjuntos
pessoa1: Dict[str, Union[str, int]] = {'nome': 'Ihury', 'sobrenome': 'Prado', 'idade': 10}
pessoa2: Dict[str, Any] = {'nome': 'Ihury', 'sobrenome': 'Prado', 'idade': 10}
pessoa3: Dict[str, Union[str, int, List[int]]] = {'nome': 'Ihury', 'sobrenome': 'Prado', 'idade': 10, 'lista': [1, 2]}

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]]
pessoa4: MeuDict = {'nome': 'Ihury', 'sobrenome': 'Prado', 'idade': 10, 'lista': [1, 2]}

# Meu novo tipo
UserId = NewType('UserId', int)
user_id = UserId(12312312)


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao

def soma(x: int, y: int) -> int:
    return x + y

retorna_funcao(soma)(10, 20)

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')


def iterar1(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]

def iterar2(sequencia: Iterable[int]):
    return [x * 2 for x in sequencia]

print(iterar1([1, 2, 3, 4, 5, 6]))
print(iterar1((1, 2, 3, 4, 5, 6)))
print(iterar2([1, 2, 3, 4, 5, 6]))
print(iterar2((1, 2, 3, 4, 5, 6)))