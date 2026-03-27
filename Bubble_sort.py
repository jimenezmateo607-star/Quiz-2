Lista =  []
num = int(input("Cuantos núumeros deea ingresar? :  "))
for i, x in enumerate((range(num))):
    Lista.append(int(input(f"Ingrese número {i+1}: ")))

print(f"Lista original {Lista}")

for x in range(num):
    for j in range (num - 1):
        if Lista[j] > Lista[j+1]:
            Lista[j], Lista[j+1] = Lista [j+1], Lista[j]

print(f"Lista modificada {Lista}")

 