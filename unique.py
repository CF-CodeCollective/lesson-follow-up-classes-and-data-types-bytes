import random

def run():
    num = set()
    while len(num) < 50:
        num.add(random.randint(1, 1000))

    return num

if __name__ == "__main__":
    print(run())