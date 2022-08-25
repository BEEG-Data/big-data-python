""" _EJ1_
phrase = input("Input phrase: ")
number = input("Input number:  ")
print(phrase[::-1])
print(phrase.replace("a", number.upper()))
"""

"""
email = input("Introduce tu correo electrónico: ")
newemail=input("Introduce nuevo correo: ")
print(newemail+email[email.find('@'):])
"""

""" _EJ3_
monto = float(input("¿Qué cantidad desea invertir? "))
interes = float(input("¿Cual es el interés porcentual anual? "))
anios = int(input("¿Cuántos años?"))
for i in range(anios):
    # "*=" es lo mimso que "monto = monto * x"
    monto *= 1 + interes / 100 
    #round es redondeo (el parametro, desde cuantos decimales)
    print("Capital después de " + str(i+1) + " años: " + str(round(monto, 2)))
"""

""" _EJ4_
materias = ["Seguridad informática", "Big Data", "Inteligencia Artificial", "Redes", "Machine Learning"]
aprobadas = []
for materia in materias:
    calificacion = float(input("¿Qué calificación ha obtenido en: " + materia + "? "))
    if calificacion >= 51:
        aprobadas.append(materia)
for materia in aprobadas:
    materias.remove(materia)
print("Usted debe repetir las materias: " + str(materias))
#len() nos permite saber el tamaño de la lista
print(len(materias))
"""

"""
producto = 0
size = int(input("introduzca el tamaño de sus listas: "))
listaA=[]
listaB=[]
for x in range(size):
    valor=int(input("Ingrese un valor entero LISTA A:"))
    listaA.append(valor)

for x in range(size):
    valor=int(input("Ingrese un valor entero LISTA B:"))
    listaB.append(valor)
    
for i in range(len(listaA)):
    producto += listaA[i]*listaB[i]
print(f"El producto escalar de los vectores {listaA} y {listaB} es {producto}")
"""


nf = int(input("filas: "))
nc = int(input("columnas: "))
matrizA = []
for i in range(nf):
    matrizA.append([])
    for j in range(nc):
        matrizA[i].append(int(input("LISTA A: ")))

matrizB = []
for i in range(nf):
    matrizB.append([])
    for j in range(nc):
        matrizB[i].append(int(input("LISTA B: ")))

matrizC = []
transpose = []
for i in range(nf):
    matrizC.append([])
    transpose.append([])
    for j in range(nc):
        matrizC[i].append(int(0))
        transpose[i].append(int(0))

for i in range(nf):
    for j in range(nc):
        matrizC[i][j]=matrizA[i][j]+matrizB[i][j]
               
for i in range(len(matrizC)):
    for j in range(len(matrizC[0])):
        transpose[j][i] = matrizC[i][j]

ml = len(matrizA)   
print("A")
for i in range(ml):
    print(matrizA[i])
print("+")
ml = len(matrizB)   
print("B")
for i in range(ml):
    print(matrizB[i])

ml = len(matrizC)   
print("Suma:")
for i in range(ml):
    print(matrizC[i])
    
ml = len(transpose) 
print("Transpuesta:")  
for i in range(ml):
    print(transpose[i])