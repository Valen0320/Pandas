matrizNumeros=[[23,43,3424,21],[12,48,121,32],[432,22,54,45]]

# 2. Imprimir la matriz
print(matrizNumeros)

# 3. Imprimir una posicion fija
print("Posicion especifica: ",matrizNumeros[0][2])

# 4. Solicitar la posicion al usuario
fil=int(input("Fila: "))
col=int(input("Columna: "))
print("Posicion leida por teclado: ",matrizNumeros[fil-1][col-1])

# 5. Imprimir fila determinada
print("Fila 0: ",matrizNumeros[0])
print("Fila 1: ",matrizNumeros[1])

# 6. Imprimir columna
for f in range(3):
    print(matrizNumeros[f][1])

# 7. Imprimir la columna que el usuario elija
col=int(input("Columna que desea imprimir: "))
for f in range(3):
    print(matrizNumeros[f][col])

# 8. Sumar todos los elementos de la matriz
sumEleMat=0
for f in range(3):
    for c in range(4):
        sumEleMat=sumEleMat+matrizNumeros[f][c]
print("La suma de los elementos es: ")

# 9. Sumar e imprimir los elementos de cada fila
print("Sumar e imprimir la suma de los elementos de una fila")
sumEleMat=0
for f in range(3):
    for c in range(4):
        sumEleMat=sumEleMat+matrizNumeros[f][c]
    print("La suma de los elementos es: ",sumEleMat)
    sumEleMat=0