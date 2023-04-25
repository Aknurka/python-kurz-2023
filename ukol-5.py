teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#Vytvořte seznam průměrných teplot pro každý den.
prumer = [sum(n) / len(n) for n in teploty]
print(prumer)

#Vytvořte seznam ranních teplot.
morning = [n[0] for n in teploty]
print(morning)

#Vytvořte seznam nočních teplot.
evening = [n[3] for n in teploty]
print(evening)

#Vytvořte seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu
afternoon = [[n[1], n[3]] for n in teploty]
print(afternoon)