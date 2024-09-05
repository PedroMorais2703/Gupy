def sequencia_fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        proximo_valor = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_valor)
    return sequencia

def is_in_fibonacci(n):
    sequencia = sequencia_fibonacci(n)
    if n in sequencia:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."


numero = int(input("Informe um número: "))
resultado = is_in_fibonacci(numero)
print(resultado)
