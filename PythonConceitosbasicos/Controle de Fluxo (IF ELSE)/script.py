idade = int(input("Qual a sua idade? "))  # Pergunta a idade e converte para número

if idade < 18:  # Se idade menor que 18
    print("Você tem menos de 18 anos")  # Mostra isso

elif idade == 18:  # Senão, se idade IGUAL a 18
    print("Você tem 18 anos")  # Mostra isso

else:  # Senão (se nenhum dos casos acima)
    print("Você é maior de idade")  # Mostra isso


# OPERADORES DE COMPARAÇÃO

resposta1 = input("Tá com fome? (s para sim) ")  # Pergunta se está com fome

if resposta1 == "s":
    resposta2 = input("Tem comida em casa? (s para sim) ")  # Pergunta se tem comida
    
    if resposta2 != "s": 
        print("Ir ao mercado")
        print("Voltar para casa")
    
    print("Fazer comida")
    print("Comer")  
