import os
import time

def write_stats():
    with open("stats", "r") as f:
        stats = f.read()
        print(f"Your best score is: {stats} points.")

print(f"Welcome to the PI Remember!")

with (open("pi.txt", "r", encoding="UTF-8") as f):
    pi = f.read()

    write_stats()
    for i in range(10000):
        write_stats()

        print(f"PI is: {pi[:i]}")
        time.sleep(1)

        os.system('cls' if os.name == 'nt' else 'clear')

        write_stats()
        put = input("PI is? ")

        if put != pi[:i]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Incorrect. GAME OVER!")
            break

        os.system('cls' if os.name == 'nt' else 'clear')