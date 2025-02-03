def escolha_tipo(): #Função que retorna o valor referente ao tipo de madeira escolhido
    tipoMadeira = input("Qual tipo de madeira deseja comprar? ")
    while tipoMadeira != "PIN" and tipoMadeira != "PER" and tipoMadeira != "MOG" and tipoMadeira != "IPE" and tipoMadeira != "IMB":
        print("Escolha inválida. Digite uma opção disponível")
        tipoMadeira = input("Qual tipo de madeira deseja comprar? ")
    if tipoMadeira == "PIN": #R$ Pinho = 150,40
        valor = 150.40
    elif tipoMadeira == "PER": #Peroba = R$ 170,20
        valor = 170.20
    elif tipoMadeira == "MOG": #Mogno = R$ 190,90
        valor = 190.90
    elif tipoMadeira == "IPE": #Ipê = R$ 210,10
        valor = 210.10
    elif tipoMadeira == "IMB": # Imbuia = R$ 220.70
        valor = 220.70 

    return valor #retorna o valor de acordo com a escolha do usuário. Cada madeira tem um valor relacionado
def qtd_toras(): #Função que retorna o valor da quantidade da madeira e a porcentagem do desconto
    while True: #loop que testa se um valor digitado é inteiro com o (try) e gera uma exceção se for digitado outro tipo de dado
        try:
            qtd = int(input("Quantas toras deseja comprar? (m³)"))
            break #encerra o loop se for um inteiro
        except ValueError: #gera uma exceção e retorna pro início do loop caso for um dado diferente de int
            print("Oops! Digite um número! Tente novamente.\n")
    while qtd > 2000: #se a quantidade for maior que 2000 é apresentado uma mensagem que informa o limite até 2000
        print("Limite de madeira é de 2000m³\n")
        while True: #repete o primeiro loop, para sempre verificar se é um número inteiro.
            try:
                qtd = int(input("Quantas toras deseja comprar? (m³)"))
                break
            except ValueError:
                print("Oops! Digite um número! Tente novamente.")
    if qtd < 100: #início da condicional de múltipla escolha para testar e armazenar o valor referente ao tipo de madeira escolhido
        desconto = 0/100
    elif qtd >= 100 and qtd < 500:
        desconto = 4/100
    elif qtd >= 500 and qtd < 1000:
        desconto = 9/100
    elif qtd >= 1000 and qtd <= 2000:
        desconto = 16/100

    return qtd, desconto #retorna dois valores, a quantidade e a porcentagem do desconto
def transporte(): #Função que apresenta um menu referente ao tipo de transporte a ser utilizado na compra e retorna o valor relacionado a cada um
    print("\n== Serviço adicional de transporte ==")
    print("1 - Transporte Rodoviário - Valor R$ 1000,00")
    print("2 - Transporte Ferroviário - Valor R$ 2000,00")
    print("3 - Transporte Hidroviário - Valor R$ 2500,00\n")
    escolha = int(input("Que tipo de transporte irá escolher? Digite o número da opção: "))
    while (escolha < 1) or (escolha > 3): #Testa se a opção digitada está fora do intervalo de 1 até 3 (únicas opções disponíveis)      
        escolha = int(input("Que tipo de transporte irá escolher? Digite o número da opção")) #enquanto não for digitado um valor válido, o input será mostrado
    
    if escolha == 1: #início da estrutura condicional de múltipla escolha que ira testar e armazenar o valor dos transportes
        x = 1000
    elif escolha == 2:
        x = 2000
    elif escolha == 3:
        x = 2500
    return x #retorna o valor do transporte escolhido


#Programa principal

print("Madeireira do Lenhador Kleyton Félix")
print("=" * 5, "Tipos de Madeiras Disponíveis", "=" * 5)
print("|", "Pinho (PIN)", "|")
print("|", "Peroba (PER)", "|")
print("|", "Mogno (MOG)", "|")
print("|", "Ipê (IPE)", "|")
print("|", "Imbuia (IMB)", "|\n")

tipoMadeira = escolha_tipo() #variável global que recebe o retorno da função atribuída
qtdToras, desconto = qtd_toras() #variáveis globais que armazenará os retornos da função atribuída (qtd_horas)
valor_Trasporte = transporte() #variável global que será atribuído o retorno da função transporte()
total = ((tipoMadeira * qtdToras) * (1 - desconto)) + valor_Trasporte #Expressão do cálculo total da compra, atribuída a variável total
 
print(f"\nTotal: R$ {total:.2f}") #Apresenta o valor total da compra
