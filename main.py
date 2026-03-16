import os
import time

def write_stats():
    with open("stats", "r") as f:
        stats = f.read()
        print(f"Your best score is: {get_stats()[0]} points. \nYour last score is: {get_stats()[1]} points.")

def get_stats():
    with open("stats", "r") as f:
        return f.read().splitlines()

def end_game(score):
    with open("stats", "r+") as f:
        lines = f.read().splitlines()
        best = int(lines[0])

        if score > best:
            best = score

        f.seek(0)
        f.write(str(best))
        f.write(f"\n{score}")

print(f"Welcome to the PI Remember!")

with (open("pi.txt", "r", encoding="UTF-8") as f):
    pi = f.read()

    for i in range(10000):
        n = i + 1

        write_stats()

        print(f"PI is: {pi[:n]}")
        time.sleep(1)

        os.system('cls' if os.name == 'nt' else 'clear')

        write_stats()
        put = input("PI is? ")

        if put != pi[:n]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Incorrect. GAME OVER!")
            end_game(n)
            time.sleep(5)
            break

        os.system('cls' if os.name == 'nt' else 'clear')