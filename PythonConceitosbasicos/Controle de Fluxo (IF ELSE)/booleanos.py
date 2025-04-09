#booleanos
tem_conta = input("Você tem conta? (s/n): ").lower() == "s"
tem_senha = input("Você sabe a senha? (s/n): ").lower() == "s"

if tem_conta and tem_senha:  # Só entra se tiver conta E senha
    print(" Acesso permitido!")
elif tem_conta or tem_senha:  # Se tiver apenas um dos dois
    print(" Falta senha ou conta.")
else:  # Se não tiver nenhum
    print(" Acesso negado. ")

"""
OPERADORES BOOLEANOS - TABELA COMPLETA

Operador    Função               Exemplo               Resultado
---------   -------------------  --------------------  ---------
and         E lógico             True and True         True
                                     True and False        False
                                     False and True        False
                                     False and False       False

or          OU lógico            True or True          True
                                     True or False         True
                                     False or True         True
                                     False or False        False

not         NEGAÇÃO lógica       not True              False
                                     not False             True
"""