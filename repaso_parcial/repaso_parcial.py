import funciones_repaso
#BINGO

bingo_table = [[0]*5 for _ in range(5)]

table_complete = [[0]*5 for _ in range(5)]

bingo_table = funciones_repaso.complete_table_bingo(bingo_table)

print("Tu carton es el siguiente:")
for i in range(5):
    print("\n")
    for j in range(5):
        print(f"[{bingo_table[i][j]}]", end="")
print("\n Inicia el juego:")

import random
numbers_bingo = []
while True: 
    number = random.randint(1,75)
    if number in numbers_bingo:
        continue
    else:
        numbers_bingo.append(number)
        