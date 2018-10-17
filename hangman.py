

def hangman(word):
    wrong = 0
    stages = ["",
             " _____________      ",
             "|         |         ",
             "|         0         ",
             "|        /|\        ",
             "|         /\        ",
             ]
    rletters = list(word)
    print("rletters:{}".format(rletters))
    board = ["_"] * len(word)
    print("board:{}".format(board))
    win = False
    print("Welcome to Hangman!")    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Predict One letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            print("cind ok:{}".format(cind))
            board[cind] = char
            print("board ok:{}".format(board))
            rletters[cind] = '$'
            print("rletters ok:{}".format(rletters))
        else:
            wrong += 1
        print(" ".join(board))
        print("board if else after:{}".format(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You are winner!")
            print(" ".join(board))
            win = True
            break
    if not win:
            print("\n".join(stages[0:wrong+1]))
            print("You are loser! The correct answer is {}".format(word))

hangman("cat")