print("Sistema desenvolvido por Kleyton Félix")
valorBase = float(input("Qual o valor base do plano de saúde do cliente? R$ "))
idade = int(input("Qual a idade do cliente? "))

if (idade >= 0 and idade < 19): #100% do valor base
    valorMensal = valorBase # Multiplicar por 100 e depois dividir por 100 é fazer e desfazer. Para economizar processamento, valorMensal recebe valorBase
elif (idade >= 19 and idade < 29): #150% do valor base
    valorMensal = valorBase * (150/100)
elif (idade >= 29 and idade < 39): #225% do valor base
    valorMensal = valorBase * (225/100)
elif(idade >= 39 and idade < 49): #240% do valor base
    valorMensal = valorBase * (240/100)
elif (idade >= 49 and idade < 59): #350% do valor base
    valorMensal = valorBase * (350/100)
else: #Idade maior ou igual a 59, 600% do valor base
    valorMensal = valorBase * (600/100)

print(f"Valor mensal do plano de saúde do cliente: R$ {valorMensal:.2f}") #f-string para exibir a mensagem e o valor mensal. Mostrando apenas 2 casas decimais
