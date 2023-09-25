#################################factorial#################################
# numFactorial = int(input("Ingrese el número para sacar factorial: "))
# fact = 0
# contador = 0
# while contador <= numFactorial:
#     if fact == 0:
#         fact = contador
#     else:
#         fact = fact * contador
#     contador += 1
# print(f"el factorial de {numFactorial} es {fact}")

#################################numerosImpares#################################
# numInicio = int(input("Ingrese e numero inicial del rango: "))
# numFinal = int(input("Ingrese e numero final del rango: "))

# for n in range(numInicio, numFinal):
#     if n % 2 == 2:
#         continue
#     else:
#         print(n)

#################################saltoCada7#################################
# a = "8 15 22 29"
# for n in range(1, 31):
#     if n == 8 or n == 15 or n == 22 or n ==29:
#         print("\n")
#     else:
#         print(n)

#################################interesDeInversion#################################
# capital = int(input("Ingrese el capital invertido: "))
# interesAnual = int(input("Ingrese el interes anual: "))/100
# cantAños = int(input("Ingrese la cantiddad de años de inversión: "))

# capObtenido = (capital*interesAnual*cantAños)/cantAños
# for n in range(1, cantAños):
#     valor = capObtenido * n
#     print(f"El valor obtenido en el año {n} es de {valor}")

# print(f"\n El valor obtenido durante los {cantAños} años es de: {capital + (capObtenido*cantAños)}")

#################################interesDeInversion#################################
# cantNotas = int(input("Ingrese la cantidad de notas: "))
# acumuladoNotas = 0
# i = 1
# while i <= cantNotas:
#     nota = float(input(f"Ingrese su nota {i} en un rango de 1 a 5: "))
#     if nota >=6:
#         print("Esta nota no está dentro del rango requerido, \nIngrese nuevamente su nota")
#         continue
#     else:
#         acumuladoNotas += nota
#         i+=1
# prom = acumuladoNotas/cantNotas

# if prom >= 4.5:
#     print(f"Su nota es: {prom}. Si aprobó la asignatura")
# else:
#     print(f"Su nota es: {prom}. No aprobó la asignatura")
#################################interesDeInversion#################################
