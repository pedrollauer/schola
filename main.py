#Atividade Somativa 1
#Nome: Pedro Guilherme Lauer Lemos da Silva
#Disciplina: Raciocínio Computacional 
#Código da disciplina: 11100010563_20231_02
#Número do Envio: e598f27f-01c6-4bce-8575-ab4852ce2962. 

#Função para ler o input do usuário 
#com segurança e retornar um número caso o usuário 
#entre com um número, ou -1 caso o usuário entre
#com alguma opção inválida
def pegar_opcao():
    try:
         return int(input("Informe a ação desejada: "))
    except: 
        return -1

#Função para printar uma msg de que a 
#função ainda não foi implementada
def menu_desenvolvimento():
    print("")
    print("EM DESENVOLVIMENTO")
    print("")
    return 0

#Função com o menu dos estudantes
#e funcões correspondentes
def menu_estudante():
    #Printamos o menu
    print("")
    print("==== ESTUDANTE ====")
    print("")
    print("[1] Incluir")
    print("[2] Listar")
    print("[3] Atualizar")
    print("[4] Excluir")
    print("")
    print("[5] Voltar ao menu principal")
    print("")
    print("")
    #Pegamos a opção com segurança
    opcao = pegar_opcao()
    #referimos à variavel global
    #que mantem os registros de 
    #estudantes
    global estudantes

    #Tratamos a opção selecionada
    if opcao < 1 or opcao >5:
        print("")
        print("Opção inválida")
        return 1
    elif opcao == 5:
        return 0
    elif opcao == 1:
        #Pegamos o novo estudante e colocamos na lista
        novo_estudante = input("Informe o nome do estudante: ")
        estudantes.append(novo_estudante)
        return 1;
    elif opcao == 2:
        #Vemos se já tem algum estudante cadastrado
        #se não, dizemos que não há
        #se sim, printamos os nomes
        if len(estudantes) == 0:
            print("")
            print("Não há estudantes cadastrados!")
            return 1
        for estudante in estudantes:
            print("")
            print(" - ",estudante)
        return 1
    #Caso alguma opção não implementada seja selecionada
    #damos a mensagem de que está em desenvolvimento
    elif opcao < 5:
        menu_desenvolvimento()
        return 1

def menu_principal():
    #Desenhamos o menu
    print("")
    print("==== MENU PRINCIPAL ====")
    print("")
    print("[1] Estudante")
    print("[2] Disciplina")
    print("[3] Professor")
    print("[4] Turma")
    print("[5] Matricula")
    print("[6] Sair")
    print("")

    #Usamos a função pegar opção
    #para pegar input do teclado
    #com segurança
    opcao = pegar_opcao()
    
    
    #Tratamos as diferentes opções
    if opcao == 1 or opcao == 6:
        return opcao
    elif opcao > 1 and opcao<=5:
        return 2
    else:
        print("")
        print("Opção inválida")
        return 0

#Ponto de início do programa
def principal():

    menu_atual = 0
    # A variável menu_atual marca a tela atual do usuário
    # menu atual = 0 => Menu Principal
    # menu atual = 1 => Menu Estudante
    # menu atual = 2 => Escreve em desenvolvimento na tela
    # Loop de execução
    while True:
        #Selecao dos Menus
        if menu_atual == 0:
            menu_atual = menu_principal()
            if menu_atual== 6:
                break
        elif menu_atual == 1:
            menu_atual = menu_estudante()
        elif menu_atual == 2:
            menu_atual = menu_desenvolvimento()
        

#Início da execucão do programa
estudantes = [] # Esta lista será usada globalmente para guardar os estudantes
principal()



