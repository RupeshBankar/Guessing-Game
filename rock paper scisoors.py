player_1 = input("What's your name player 1? ")
player_2 = input("What's your name player 2? ")

game_on = True
while game_on:
    
    print(player_1 + ", choose rock(a), paper(b), or scissors(c)")
    player_1_choice = input()
    print("\n\n\n\n\n\n\n\n\n\n\n\n")

    print(player_2 + ", choose rock(a), paper(b), or scissors(c)")
    player_2_choice = input()
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    
    
    if player_1_choice == "a" and player_2_choice == "a":
        print("It's a draw")
        continue
    elif player_1_choice == "a" and player_2_choice == "b":
        print(player_2 + " wins!")
    elif player_1_choice == "a" and player_2_choice == "c":
        print(player_1 + " wins!")
    
    elif player_1_choice == "b" and player_2_choice == "a":
        print(player_1 + " wins!")
    elif player_1_choice == "b" and player_2_choice == "b":
        print("It's a draw!")
        continue
    elif player_1_choice == "b" and player_2_choice == "c":
        print(player_2 + " wins!")

    elif player_1_choice == "c" and player_2_choice == "a":
        print(player_2 + " wins!")
    elif player_1_choice == "c" and player_2_choice == "b":
        print(player_1 + " wins!")
    elif player_1_choice == "c" and player_2_choice == "c":
        print("It's a draw")
        continue
    else:
        print("Invalid input dumbum")
        continue
    
    ans = input("Wanna play again? (y/n) ")
    if ans == "y":
        continue
    if ans == "n":
        print("cool")
        break