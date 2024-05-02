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
        os.system('cls')

        horas_trabalhadas=int(input("Horas Trabalhadas: "))
        salario_minimo=float(input("Salário Mínimo: "))
        valor_hr=salario_minimo/2
        salario_bruto=horas_trabalhadas*valor_hr
        imposto=salario_bruto*0.03
        salario_receber=salario_bruto-imposto
        print("Você receberá: R$",salario_receber)
        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    elif menu == "2":
        os.system('cls')
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
        os.system('cls')

        racao_total_kg=float(input("Quantidade de ração(kg): "))
        qntd_gato1=float(input("Quantidade de ração para o primeiro animal(g): "))
        qntd_gato2=float(input("Quantidade de ração para o segundo animal(g): "))
        
        racao_total_g=racao_total_kg*1000
        racao_gastada=qntd_gato1+qntd_gato2
        racao_gastada_5dias=racao_gastada*5
        racao_restante_g=racao_total_g - racao_gastada_5dias
        racao_restante_kg=racao_restante_g/1000

        print(f"Após 5 dias, restará: {racao_restante_kg}kg")
        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    elif menu == "4":
        os.system('cls')

        nota1=float(input("Primeira nota: "))
        nota2=float(input("Segunda nota: "))
        nota3=float(input("Terceira nota: "))

        media_ponderada=(nota1*2+nota2*3+nota3*5)/10

        print(f"A média ponderada das suas notas é: {media_ponderada}")

        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    elif menu == "5":
        os.system('cls')

        custo_espetaculo=float(input("Custo total do espetáculo: "))
        preco_convite=float(input("Preço do convite: "))

        quantidade_convite=custo_espetaculo/preco_convite
        convite_arredondado=round(quantidade_convite)

        print(f"Será necessário vender: {convite_arredondado} convites")
        
        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    elif menu == "6":
        

        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    elif menu == "7":
        
        
        input("PRESSIONE ENTER PARA VOLTAR AO MENU")
    else:
        print("Tchau, Até a próxima!")
        break