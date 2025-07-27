from os import system
from time import sleep

def limpar_tela(): 
    system("Cls")

def esperar():
    sleep(2)

tarefas = []

def adicionar_tarefa():
    global tarefas

    adc_tarefa = str(input(
        "Digite a tarefa que voce quer adicionar: "
    ))

    tarefa = {
        "Tarefa": adc_tarefa,
        "Concluida": False
    }

    tarefas.append(tarefa)

def listar_tarefas():
    for numero, valor in enumerate(tarefas):
        status_conclusao = "Sim" if valor["Concluida"] else "Não"
        print(
            f"{numero + 1}) {valor['Tarefa']} - Concluída: {status_conclusao}"
            )
        
def marcar_tarefas(): 
    global tarefas, esperar, limpar_tela

    listar_tarefas()

    print (
        "-=-"*10
    )

    marcar_concluida = int(input(
        "Digite o indice do numero que deseja marcar como concluido: "
    ))

    if tarefas[marcar_concluida - 1]["Concluida"] == True:
        limpar_tela() 
        print ("Você já marcou essa tarefa como concluída. Tente Novamente com uma tarefa pendente.")
        esperar()
        limpar_tela()
    
    else: 
        tarefas[marcar_concluida - 1]["Concluida"] = True
        limpar_tela()

while True: 
    try:
        escolha = int(input(
            "[1] - Adicionar Tarefa\n" \
            "[2] - Listar Tarefas\n" \
            "[3] - Marcar Tarefa como 'Concluída'\n"
            "[0] - Exit\n" \
            ">>> "
        ))
        limpar_tela()
    except (ValueError, NameError):
        limpar_tela()
        print (
            "Neste momento, aceitamos apenas número como resposta válida."
        )
        esperar()
        limpar_tela()
        continue

    if escolha == 1: 
        adicionar_tarefa()
        limpar_tela()

    elif escolha == 2: 
        listar_tarefas()
        esperar()
        limpar_tela()

    elif escolha == 3: 
        marcar_tarefas()
    
    else: 
        limpar_tela()
        break