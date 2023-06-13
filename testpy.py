numeros = [int(input(f"Informe o {i+1}º número: ")) for i in range(5)]
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
media = sum(numeros) / len(numeros)

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"Média geral: {media}")