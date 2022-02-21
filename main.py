liczby_podzielne = []

for i in range (0,100):
    if i % 5 == 0:
        liczby_podzielne.append(i)
print(liczby_podzielne)

cubes = [number ** 3 for number in liczby_podzielne]

print(cubes)
print("Zmiana,zmaina,zmiana")
