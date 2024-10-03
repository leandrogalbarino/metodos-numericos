import matplotlib.pyplot as plt
import numpy as np


def f_string():
    return "x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827"
    


def f(x):
    return x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827
    

def e():
    return 0.000001

def tolerancia(x, x_anterior):
    return abs((x - x_anterior) / x)


def pedir_numero_float(str):
    while True:
        try:
            x = float(input(str))
            return x
        except ValueError:
            print("Entrada invalida, tente novamente!")


def metodo_falsa_posicao():
    a = pedir_numero_float("Digite a1:")
    b = pedir_numero_float("Digite b1:")
    print()

    if f(a)*f(b) > 0:
        print("Nao existe raiz nesse intervalo ou o intervalo possui mais de uma raiz. Tente outro.")
        return None, []
    
    x_anterior = None
    interacoes = []  # Lista para armazenar as interações

    for _ in range(100):
        x = a - (b - a)/(f(b) - f(a))*f(a)

        interacoes.append((a, x, b, f(x), tolerancia(x, x_anterior) if x_anterior is not None else "--------"))

        if x_anterior is not None and tolerancia(x, x_anterior) <= e():
            return x, interacoes

        if f(a)*f(x) < 0:
            b = x
        else:
            a = x
        x_anterior = x

    print("O método não convergiu dentro do número máximo de iterações.")
    return None, []


raiz, interacoes = metodo_falsa_posicao()
# Preparar dados para o gráfico
x_vals = np.linspace(-3, 7, 1000)  # Intervalo ajustado para incluir a raiz
y_vals = f(x_vals)

# Plotar a função
plt.plot(x_vals, y_vals, label=f_string())
plt.axhline(0, color='black', linewidth=0.5)  # Linha do eixo x

# Se a raiz foi encontrada, marcá-la no gráfico
if raiz is not None:
    plt.plot(raiz, f(raiz), 'ro', label=f"Raiz = {raiz:.10f}")

# Configurações do gráfico
plt.title('Método da Falsa Posicao')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
print()
# Exibir tabela de interações
print("\tMÉTODO DA FALSA POSIÇÃO | DETERMINAÇÃO DA RAIZ z4")
# Cabeçalho da tabela
print(f"{'     '}{'k':<6}{'ak':>16}{'xk':>16}{'bk':>16}{'f(xk)':>16}{'ERk':>16}")
for i, (a, x, b, fx, er) in enumerate(interacoes):
    if isinstance(er, str):
        print(f"{'     '}{i:<6}{a:>16.10f}{x:>16.10f}{b:>16.10f}{fx:>16.10f}{er:>16}")
    else:
        print(f"{'     '}{i:<6}{a:>16.10f}{x:>16.10f}{b:>16.10f}{fx:>16.10f}{er:>16.10f}")
if raiz is not None:
    print(f"{'     '}Raiz z4 = {raiz:>16.10f}")
input()