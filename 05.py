def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string = input("Informe uma string: ")

string_invertida = inverter_string(string)
print("String invertida:", string_invertida)
