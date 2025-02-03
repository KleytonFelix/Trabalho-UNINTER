#Menu da Pizzaria
print("=" * 5, "Bem vindos a Pizzaria de Kleyton Félix", "=" * 5)
print("=" * 20, "Cardápio", "=" * 20)
print("=" * 50)
print("=|", "Tamanho", "|", "Pizza Salgada(PS)", "|", "Pizza Doce(PD)", "|=")
print("=|", "   P   ", "|", "   R$ 30,00      ", "|", "   R$34,00    ", "|=")
print("=|", "   M   ", "|", "   R$ 45,00      ", "|", "   R$48,00    ", "|=")
print("=|", "   G   ", "|", "   R$ 60,00      ", "|", "   R$66,00    ", "|=")
print("=" * 50)

valor_total = 0 #variável acumuladora

while True: #primeiro laço while que engloba toda a execução do pedido

    while True: #laço while aninhado, para verificar se o sabor da pizza digitado está correto
        sabor = input("Qual sabor da pizza? (PS/PD)")
        if sabor.upper() == "PD" or sabor.upper() == "PS": #caso seja uma opção válida (PS/PD), o loop encerra
            break  
        else: #caso digite algum sabor inválido, o programa apresenta uma mensagem de erro e retorna ao inicio
            print("Entrada inválida. Tente novamente")
        continue #continua o laço, solicitando novamente uma entrada válida

    while True: #laço while aninhado, para verificar se o tamanho da pizza é válido
        tam = input("Qual o tamanho da pizza? ")
        if tam.upper() == "P" or tam.upper() == "M" or tam.upper() == "G": #Se for digitado um tamanho válido, o laço encerra e o programa continua
            break
        else: #caso for digitado um tamanho inválido. O laço retorna ao início
            print("Tamanho inválido. Tente novamente")
        continue #solicita uma nova entrada válida

    if sabor.upper() == "PS": #Início da estrutura condicional; Pizzas Salgadas(PS)
        if tam.upper() == "P": #Pizza salgada tamanho P
            print("Você pediu uma Pizza Salgada no Tamanho P: R$ 30.00") #mostra na tela a opção escolhida seguida do valor unitário
            valor_total += 30 #acumula o valor da (pizza Salgada P) na variável de soma do total do pedido
        elif tam.upper() == "M": #Pizza salgada tamanho M
            print("Você pediu uma Pizza Salgada no Tamanho M: R$ 45.00") #mostra na tela a opção escolhida seguida do valor unitário
            valor_total += 45 #acumula o valor da (pizza Salgada M) na variável de soma do total do pedido
        elif tam.upper() == "G": #Pizza salgada tamanho G
            print("Você pediu uma Pizza Salgada no Tamanho G: R$ 60.00") #mostra na tela a opção escolhida seguida do valor unitário
            valor_total += 60 #acumula o valor da (pizza Salgada G) na variável de soma do total do pedido
    elif sabor.upper() == "PD": # Condicional de Múltipla Escolha. Pizzas doces (PD)
        if tam.upper() == "P": #Pizza Doce Tamanho P
            print("Você pediu uma Pizza Doce no Tamanho P: R$ 34.00")
            valor_total += 34
        elif tam.upper() == "M": #Pizza Doce Tamanho M
            print("Você pediu uma Pizza Doce no Tamanho M: R$ 48.00")
            valor_total += 48
        elif tam.upper() == "G": #Pizza Doce Tamanho G
            print("Você pediu uma Pizza Doce no Tamanho G: R$ 66.00")
            valor_total += 66
    resposta = input("Deseja pedir mais alguma coisa? (S/N)") #Atribui a resposta do input mostrado na tela se deseja continuar ou fechar o pedido
    if resposta == "N": #Se for digitado N, laço primeiro laço while (linha 13) encerra e o programa continua
        break
    elif resposta == "S": #Se for digitado S, laço while do pedido continua
        continue

print(f"O valor total a ser pago: R$ {valor_total:.2f}")
