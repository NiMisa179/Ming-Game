import random

highScore = []
print("Welcome in mnimis Game!")
answer = input("Will you start? If so, write yes: ")

while answer == "yes":

    N = int(input("Type the number of cards you would like to play: "))
    while N % 2 != 0:
        N = int(input("The number must be equally divided by 2: "))

    diairetes = [i for i in range(1, N) if N % i == 0]

    if len(diairetes) == 2:
        rows = diairetes[-1]
        columns = diairetes[-1]
    elif len(diairetes) == 1:
        rows = 1
        columns = 2
    elif len(diairetes) == 3:
        rows = diairetes[-2]
        columns = diairetes[-1]
    else:
        for x in diairetes:
            for j in diairetes:
                if x != 1 and j != 1 and x * j == N and j < N / 2 and x < N / 2:
                    rows = j
                    columns = x
                    break

    cards = [[0 for i in range(columns)] for j in range(rows)]

    hidden = [["x" for i in range(columns)] for j in range(rows)]

    row_h = len(hidden)
    cols_h = len(hidden[0])

    num = 1

    N = N // 2

    for i in range(0, N):

        r1 = random.randint(1, row_h) - 1
        r2 = random.randint(1, row_h) - 1

        c1 = random.randint(1, cols_h) - 1
        c2 = random.randint(1, cols_h) - 1

        while (r1 == r2 and c1 == c2) or (cards[r1][c1] != cards[r2][c2]) or (
                cards[r1][c1] != 0 and cards[r2][c2] != 0):
            if cards[r1][c1] != 0:
                c1 = random.randint(1, cols_h) - 1
                r1 = random.randint(1, row_h) - 1

            elif cards[r2][c2] != 0:
                c2 = random.randint(1, cols_h) - 1
                r2 = random.randint(1, row_h) - 1

            elif r1 == r2 and c1 == c2:
                c1 = random.randint(1, cols_h) - 1
                r1 = random.randint(1, row_h) - 1

        if cards[r1][c1] == 0 and cards[r2][c2] == 0:
            cards[r1][c1] = num
            cards[r2][c2] = num
        # print(cards)

        num += 1
    # print(cards)

    guesses = 0

    while True:

        cols = len(cards[0])
        rows = len(cards)

        row = 1

        cols_tuple = tuple(range(1, cols + 1))

        print("   ", end=" ")
        for i in cols_tuple:
            print(str(i), end=" ")
        print("")
        for i in hidden:

            print(str(row) + ": ", end=" ")

            col = 1
            for j in i:
                print(j, end=" ")
                col += 1
            print("")
            row += 1

        rowC = int(input("Choose your row: ")) - 1
        while rowC < 0 or rowC > rows - 1:
            rowC = int(input("Choose your row between 1 and " + str(rows) + ": ")) - 1

        colC = int(input("Choose your column: ")) - 1
        while colC < 0 or colC > cols - 1:
            colC = int(input("Choose your column between 1 and " + str(cols) + ": ")) - 1

        while hidden[rowC][colC] != "x":
            rowC = int(input("You already have chose that combo! Choose another row between 1 and " + str(rows) + ": ")) - 1
            while rowC < 0 or rowC > rows - 1:
                rowC = int(
                    input("Choose your row between 1 and " + str(rows) + ": ")) - 1

            colC = int(input("You already have chose that combo! Choose your column between 1 and " + str(cols) + ": ")) - 1
            while colC < 0 or colC > cols - 1:
                colC = int(
                    input("Choose your column between 1 and " + str(cols) + ": ")) - 1

        picked1 = cards[rowC][colC]
        hidden[rowC][colC] = picked1

        row = 1

        print("   ", end=" ")
        for i in cols_tuple:
            print(str(i), end=" ")
        print("")
        for i in hidden:

            print(str(row) + ": ", end=" ")

            col = 1
            for j in i:
                print(j, end=" ")
                col += 1
            print("")
            row += 1

        rowC2 = int(input("Choose your row: ")) - 1
        while rowC2 < 0 or rowC2 > rows - 1:
            rowC2 = int(input("Choose your row between 1 and " + str(rows) + ": ")) - 1

        colC2 = int(input("Choose your column: ")) - 1
        while colC2 < 0 or colC2 > cols - 1:
            colC2 = int(input("Choose your column between 1 and " + str(cols) + ": ")) - 1

        while hidden[rowC2][colC2] != "x":
            rowC2 = int(input("You already have chose that combo! Choose your row between 1 and " + str(rows) + ": ")) - 1
            while rowC2 < 0 or rowC2 > rows - 1:
                rowC2 = int(input("Choose your row between 1 and " + str(rows) + ": ")) - 1

            colC2 = int(input("You already have chose that combo! Choose your column between 1 and " + str(cols) + ": ")) - 1
            while colC2 < 0 or colC2 > cols - 1:
                colC2 = int(input("Choose your column between 1 and " + str(cols) + ": ")) - 1

        picked2 = cards[rowC2][colC2]
        hidden[rowC2][colC2] = picked2

        guesses += 1

        row = 1
        if picked1 != picked2:

            print("   ", end=" ")
            for i in cols_tuple:
                print(str(i), end=" ")
            print("")
            for i in hidden:

                print(str(row) + ": ", end=" ")

                col = 1
                for j in i:
                    print(j, end=" ")
                    col += 1
                print("")
                row += 1

            hidden[rowC][colC] = "x"
            hidden[rowC2][colC2] = "x"

        print("--------------------------")

        if hidden == cards:
            break
    print("You won!")
    print(guesses)
    highScore.append(guesses)
    answer = input("Continue? type yes. Stop? type anything: ")

if len(highScore) != 0:
    print("Your highscore was " + str(min(highScore)))
else:
    print("You haven' t played yet")
