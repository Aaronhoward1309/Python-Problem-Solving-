def guess_the_num():
    num=6
    int(print("please guess a number beteen 1 and 10 "))
    while True:
        try:
            guess= int(input("gues the number"))

            if guess==num:
                  print("correct number guessed")
            break
            elif guess!= num:
                    print("guess again")
guess_the_num

            
                      
