# =============================================
# LISTAS EM PYTHON - TUDO EM UM SÓ CÓDIGO
# =============================================

# 1. Criando listas
print("\n1. CRIAÇÃO DE LISTAS:")
lista_vazia = []
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
misturada = [10, "texto", True, 3.14]

print("Lista vazia:", lista_vazia)
print("Lista de frutas:", frutas)
print("Lista numérica:", numeros)
print("Lista mista:", misturada)

# 2. Acessando elementos
print("\n2. ACESSO A ELEMENTOS:")
linguagens = ["Python", "Java", "C++", "JavaScript"]

print("Primeiro elemento:", linguagens[0])     # Python
print("Último elemento:", linguagens[-1])      # JavaScript
print("Terceiro elemento:", linguagens[2])     # C++

# 3. Operações básicas
print("\n3. OPERAÇÕES BÁSICAS:")
lista = [1, 2, 3]

# Adicionando itens
lista.append(4)           # [1, 2, 3, 4]
lista.insert(1, 1.5)      # [1, 1.5, 2, 3, 4]

# Removendo itens
lista.remove(2)           # Remove o primeiro 2 → [1, 1.5, 3, 4]
ultimo = lista.pop()       # Remove e retorna 4 → lista fica [1, 1.5, 3]

print("Lista após operações:", lista)
print("Último item removido:", ultimo)

# 4. Fatiamento (slicing)
print("\n4. FATIAMENTO DE LISTAS:")
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Do índice 2 ao 5:", numeros[2:6])       # [2, 3, 4, 5]
print("Pulando de 2 em 2:", numeros[::2])      # [0, 2, 4, 6, 8]
print("Lista invertida:", numeros[::-1])       # [9, 8, 7, ..., 0]

# 5. Métodos úteis
print("\n5. MÉTODOS ÚTEIS:")
cores = ["vermelho", "azul", "verde", "amarelo", "azul"]

print("Número de elementos:", len(cores))           # 5
print("Contagem de 'azul':", cores.count("azul"))  # 2
print("Índice de 'verde':", cores.index("verde"))  # 2

cores.sort()                                        # Ordem alfabética
print("Lista ordenada:", cores)

# 6. List Comprehension
print("\n6. LIST COMPREHENSION:")
quadrados = [x**2 for x in range(1, 6)]            # [1, 4, 9, 16, 25]
pares = [x for x in range(10) if x % 2 == 0]       # [0, 2, 4, 6, 8]

print("Quadrados de 1 a 5:", quadrados)
print("Números pares até 10:", pares)

# 7. Exemplo prático completo
print("\n7. EXEMPLO PRÁTICO - SISTEMA DE ESTOQUE:")
estoque = ["maçã", "banana", "laranja"]

print("Estoque inicial:", estoque)

# Adicionando itens
estoque.append("uva")
estoque.insert(1, "abacaxi")

print("Estoque após adições:", estoque)

# Verificando e removendo
if "banana" in estoque:
    estoque.remove("banana")
    print("Banana removida do estoque")

# Ordenando
estoque.sort()
print("Estoque organizado:", estoque)

# =============================================
# FIM DO PROGRAMA
# =============================================
print("\nFim da demonstração sobre listas! 🐍")