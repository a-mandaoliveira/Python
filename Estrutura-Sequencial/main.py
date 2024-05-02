# Primeiros programas feitos para fixação da linguagem
import os

while True:
    os.system('cls')
    menu= input('''
Bem vindo(a) ao seu calculador de coisas específicas,
Escolha uma das opções abaixo:
[1] Cálculo de Salário
[2] Calcular número ²(ao quadrado) e √(raiz quadrada)
[3] Cálculo de Ração
[4] Calcular média ponderada
[5] Cáculo de convites que devem ser vendidos
[6] Cálculo de desconto de salário
[7] Cálculo para iluminação
[8] Sair         
''')

    if menu not in ["1","2","3","4","5","6""7","8"]:
        print("OPÇÃO INVÁLIDA")
        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    elif menu == "1":
        horas_trabalhadas=int(input("Horas Trabalhadas: "))
        salario_minimo=float(input("Salário Mínimo: "))
        valor_hr=salario_minimo/2
        salario_bruto=horas_trabalhadas*valor_hr
        imposto=salario_bruto*0.03
        salario_receber=salario_bruto-imposto
        print("Você receberá: R$",salario_receber)
        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    elif menu == "2":
        while True:
            numero=float(input("Digite um número positivo e maior que 0: "))
            if numero<=0:
                print("DIGITE UM NÚMERO >POSITIVO E MAIOR QUE ZERO<")
            else:
                numero_quadrado=numero**2
                numero_raiz=numero**0.5
                print(f"{numero}²= {numero_quadrado}\n√{numero}= {numero_raiz}")
                break

        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    elif menu == "3":
        

        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    elif menu == "4":
        

        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    elif menu == "5":
        
        
        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    elif menu == "6":
        

        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    elif menu == "7":
        
        
        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    else:
        print("Tchau, Até a próxima!")
        break