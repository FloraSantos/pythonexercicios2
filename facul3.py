print('''Quadro 1: Dimensões versus Valor          Quadro 2: Peso versus multiplicador
    dimensões (cm³)        valor R$          peso kg         multiplicador
 volume < 1000               10            peso < 0.1          1
 1000 <= volume < 10000      20            0.1 <= peso < 1     1.5
 10000 <= volume < 30000     30            1 <= peso < 10      2
 30000 <= volume < 100000    50            10 <= peso < 30     3
 valume >= 100000        Não é aceito      peso > 30       Não é aceito

Quadro 3: Rota versus multiplicador
rota                                    multiplicador
RS - De Rio de Janeiro até São Paulo        1 
SR - De São Paulo até Rio de Janeiro        1   
BS - De Brasília até São Paulo              1.2
SB - De São Paulo até Brasília              1.2 
BR - De Brasília até Rio de Janeiro         1.5
RB - Rio de Janeiro até Brasília            1.5''')

# ----Começo da função dimensoesObjeto-----
from ast import Try


def dimensoesObjeto():  # EXIGÊNCIA 1 DE 3
    while True:
        try:  # feito try/except para caso não digitar valor numérico
            altura = float(input("Informe a altura do Objeto (em cm): "))  # pergunta a altura do objeto
            largura = float(input("Informe a largura do Objeto (em cm): "))  # pergunta a largura do objeto
            comprimento = float(input("Informe o comprimento do Objeto (em cm): "))  # pergunta o comprimento do objeto
            volume = altura * largura * comprimento  # calcula o volume do objeto
            print('O volume do objeto é (em cm³): {}'.format(volume))  # informa o valor o volume
            if volume < 1000:
                return 10.00  # Retordados os valores para cada volume
            elif 1000 <= volume < 10000:
                return 20.00
            elif 10000 <= volume < 30000:3
                return 30.00
            elif 30000 <= volume < 100000:
                return 50.00
            elif volume >= 100000:  # tratamento de valor inválido
                print('Estas dimensões não são aceitas. Tente novamente.')
                continue
            else:
                print('Algo está errado. Tente de novamente')
                continue
        except ValueError:  # tratamento de valor não numérico
            print('Você digitou um valor não numérico. Tente novamente.')
            continue

#  Fim da Função dimensoesObjeto

# ------- Começo da função pesoObjeto-----


def pesoObjeto():  # EXIGÊNCIA 2 DE 3
    while True:
        try:  # feito try/except para caso não digitar valor numérico
            pesoObj = float(input('Entre com o peso do Objeto (em kg): '))  #Pergunta o peso do Objeto em kg
            if pesoObj < 0.1:
                return 1.0      #retorna o multiplicador correspondente ao peso
            elif 0.1 <= pesoObj < 1:
                return 1.5
            elif 1 <= pesoObj < 10:
                return 2.0
            elif 10 <= pesoObj < 30:
                return 3.0
            elif pesoObj > 30:  # tratamento de valor inválido
                print('Este peso não é aceito. Tente novamente.')
                continue
            else:
                print('Algo deu errado. Tente de novamente.')
                continue
        except ValueError:  # tratamento de valor não numérico
            print('Você digitou um valor não numérico. Tente novamente.')
            continue

# Fim da Função pesoObjeto

# ------- Começo da função pesoObjeto-----


def pesoObjeto():  # EXIGÊNCIA 2 DE 3
    while True:
        try:  # feito try/except para caso não digitar valor numérico
            pesoObj = float(input('Entre com o peso do Objeto (em kg): '))  #Pergunta o peso do Objeto em kg
            if pesoObj < 0.1:
                return 1.0      #retorna o multiplicador correspondente ao peso
            elif 0.1 <= pesoObj < 1:
                return 1.5
            elif 1 <= pesoObj < 10:
                return 2.0
            elif 10 <= pesoObj < 30:
                return 3.0
            elif pesoObj > 30:  # tratamento de valor inválido
                print('Este peso não é aceito. Tente novamente.')
                continue
            else:
                print('Algo deu errado. Tente de novamente.')
                continue
        except ValueError:  # tratamento de valor não numérico
            print('Você digitou um valor não numérico. Tente novamente.')
            continue

# Fim da Função pesoObjeto


# Começo da função rotaObjeto

def rotaObjeto():   #EXIGÊNCIA 3 DE 3
    while True:
        print('Escolha o tipo de Rota:') #pergunta a rota do Objeto desejada
        print(' RS - Rio de Janeiro x São Paulo')
        print(' SR - São Paulo x Rio de Janeiro')
        print(' BS - Brasília x São Paulo')
        print(' BR - Brasilia x Rio de Janeiro')
        print(' RB - Rio de Janeito x Brasilia')
        rotaObj = input('--')
        if rotaObj == 'RS':
            return 1            #retorna um multiplicador conforme a rota escolhida
        elif rotaObj == 'SR':
            return 1
        elif rotaObj == 'BS':
            return 1.2
        elif rotaObj == 'SB':
            return 1.2
        elif rotaObj == 'BR':
            return 1.5
        elif rotaObj == 'RB':
            return 1.5
        else:
            print('Rota inexistente. Tente de novamente.') #tratamento de valor inválido
            continue


# Fim da Função rotaObjeto

# ----Começo do Programa Principal-------
print('Bem vindo a Transportadora da RU:3922190') #indentificador pessoal
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes*peso*rota

#valor total a pagar
print('Valor total foi de: R$ {:.2f} \nDimensões: {} * peso: {} * rota: {}'.format(total,dimensoes,peso,rota))
# -----------Fim da Programa Principal-----


