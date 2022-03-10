def game():
    win_num = 3
    while True:
        try:
            user_num = int(input("Enter Your Number Under (1-10): "))
            if user_num == win_num:
                print("Congratulation !! Your are winner .")
                break
            else:
                print("Try Again !")
        except ValueError:
            print("Wrong Data")

game()
