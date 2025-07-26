import random

print("!!WELCOME TO ROCK, PAPER AND SCISSORS GAME!!\n")
print('Type "rock","paper" or "scissors" as per your choice.')
print('---------OR---------\nType "exit" to end the game\n')


def game():
    round_no=1
    user_score=0
    comp_score=0
    while True:
        comp=random.choice(["rock","paper","scissors"])
        print(f"-----ROUND {round_no}-----")
        user=input("Enter your choice: ").lower()
        if (user not in ["rock","paper","scissors","exit"]):
            print("!!Invalid input!!\nPlease enter a valid input")
            continue
        if (user=="exit"):
            print("Thank you for playing the game!!")
            print(f"FINAL SCORES->\nYOUR SCORE:{user_score} | COMPUTER SCORE:{comp_score}")
            break
        print(f"\nYou chose: {user}")
        print(f"Computer chose: {comp}\n")
        
        if (comp==user):
                print("Match Tie")
        elif (comp=="rock" and user=="paper") or \
             (comp=="paper" and user=="scissors") or \
             (comp=="scissors" and user=="rock"):
                print("You win :)") 
                user_score+=1
        else:
            print("You lose :(\nTry next time")
            comp_score+=1
        print(f"SCORE->\nYOUR SCORE:{user_score} | COMPUTER SCORE:{comp_score}")
         
        
        play_more=input('\nDo you want to play another round?\nType "yes" or "no":')
        if (play_more not in ["yes","YES"]):
            print("\nThank you for playing the game!!")
            print(f"FINAL SCORES->\nYOUR SCORE:{user_score} | COMPUTER SCORE:{comp_score}")
            break
        round_no+=1
game()
                
                
                
    