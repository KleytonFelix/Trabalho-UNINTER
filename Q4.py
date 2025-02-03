#funções do programa

def cadastrar_contato(id): #Função de cadastrar um novo contato na lista, opção 1 do menu principal
    print("============================================")
    print("========== Menu Cadastrar Contato ==========\n")
    print(f"Id do contato: {id}")
    nome = input("Qual o nome do contato? ") #recebe um nome, string
    atividade = input("Qual ramo de atividade do contato? ") #recebe uma atividade, string
    telefone = int(input("Qual o número de telefone do contato? ")) #recebe um numero, inteiro
    contato = {"id":id, "nome":nome, "atividade": atividade,"telefone":telefone} #armazena id, nome, atividade e telefone num dicionário local "contato"
    lista_contatos.append(contato.copy()) #uma cópia do dicionário é adicionado a um índice na lista_contatos do programa principal 

def consultar_contatos(): #função de consultar contatos, opção 2 do menu principal
    print("============================================")
    print("========== Menu Consultar Contatos ==========\n")
    while True: #aqui inicia o loop do menu
        print("\n----- Menu de Opções -----") 
        print("1 - Consultar Todos")
        print("2 - Consultar Por Id")
        print("3 - Consultar Por Setor")
        print("4 - Retornar ao Menu")
        escolha = int(input("Digite uma opção: ")) #recebe um inteiro  
        while (escolha > 4) or (escolha < 1): #Se o número digitado estiver fora do intervalo do menu é:
            print("Opção inválida. Digite uma opção válida\n") #apresentado uma mensagem que diz o que está acontecendo
            escolha = int(input("Digite uma opção: ")) # e pergunta novamente e recebe um novo inteiro, caso estiver dentro do intervalo, sai do loop
                                                       # Se ainda estiver fora do intervalo, executa até receber um número válido passado na expressão lógica do loop while                 
        if escolha == 4: #Se for digitado a opção 4, encerra o laço e retorna ao menu principal
            return #retorna ao programa principal sem nenhum valor associado a instrução return
        elif escolha == 1: #Opção 1, consulta todos os contatos
            for contato in lista_contatos: #para cada contato (índice) na lista de contatos, neste caso, cada dicionário dentro da lista
                print("===================")
                for chave, valor in contato.items(): #para cada par (chave:valor) dentro do dicionário; método items() para retornar a chave e o valor associado
                    
                    print(f"|{chave} = {valor}\n", end="") #exibe na tela todos os contatos com seus(uas) respectivos(as) id's, nomes, atividades, e número de telefone
                    
                    
        elif escolha == 2: #Opção 2, consulta por Id
            escolha_id = int(input("Digite o Id do contato: ")) #recebe um inteiro
            for id in lista_contatos: #para cada índice na lista de contatos
                print("===================")
                if id.get("id") == escolha_id: #se no índice da lista de contatos (em cada dicionário), em cada chave:"id" se encontrar o mesmo valor do que foi digitado:
                    for chave, valor in id.items():
                        print(f"|{chave} = {valor}\n", end="") #exibe na tela o índice completo dal ista (todas as chaves e valores do dicionário encontrado)
                print("===================")   
        elif escolha == 3: #Opção 3, busca por atividade.   
            escolha_atividade = input("Digite a atividade profissional: ") #recebe uma string
            for atividade in lista_contatos: #para cada índice na lista de contatos
                print("===================")
                if atividade.get("atividade") == escolha_atividade: #se no índice(dicionario) da lista na chave "atividade" tiver um valor associado igual ao que foi digitado:
                    for chave, valor in atividade.items():
                        print(f"|{chave} = {valor}\n", end="") #exibe na tela todos os índices (dicionários) da lista encontrado pela atividade digitada
                    
        
def remover_contato(): #Função de remover contatos da lista. Opção 3 do menu principal
    print("============================================")
    print("========== Menu Remover Contatos ==========\n")
    id = int(input("Digite o id do contato que quer remover da lista: ")) #recebe um inteiro
    while True: #loop infinito
        for contato in lista_contatos: #para cada índice na lista
            if contato.get("id") == id: #se for encontrado na lista um dicionário que tiver como índice igual ao digitado:
                lista_contatos.remove(contato) # remove este dicionário da lista. Método .remove()
                print("Contato removido com sucesso!")
                return #retorna para o menu principal
            
        print("Id Inválido. Tente novamente") #caso não for encontrado um id igual ao digitado na lista, é exibido uma mensagem
        id = int(input("Digite o id do contato que quer remover da lista: ")) #pergunta novamente um id até ser um válido

#programa principal

lista_contatos = [] #é criada uma lista vazia que vai ser incrementada ao longo do programa
id_global = 5085601 #id global recebe um número de registro inicial, que vai ser incrementado em +1 a cada cadastro na lista

while True: #loop do programa principal
    #Menu principal com as opções válidas
    print("=====Lista de contatos de Kleyton Félix=====\n")
    print("      |    1) Cadastrar Contato    |")
    print("      |    2) Consultar Contato    |")
    print("      |    3) Remover Contato      |")
    print("      |    4) Encerrar Programa    |\n")
    print("============================================\n")
    
    op = int(input("Qual opção deseja escolher? ")) #variável de controle para testar expressões lógicas nos laços e condicionais. Recebe um inteiro
    while (op < 1) or (op > 4): #testa se o número digitado está no intervalo das opções do menu
        print("Opção inválida. Tente novamente") #caso a expressão acima for verdadeira (estiver fora do intervalo), é iniciado um loop infinito    
        op = int(input("Qual opção deseja escolher? ")) #até ser digitado um número válido e a expressão retornar false

    if op == 1: #Opção 1 digitada
        id_global += 1 #Id global é incrementada
        cadastrar_contato(id_global) #chamada de função com o parâmetro id_global
    elif op == 2: #Opção 2 digitada
        consultar_contatos() #chamada de função
    elif op == 3: #Opção 3 digitada 
        remover_contato() #chamada de função 
    elif op == 4: #Opção 4 digitada
        print("Encerrando programa...") #Encerra o programa
        break


