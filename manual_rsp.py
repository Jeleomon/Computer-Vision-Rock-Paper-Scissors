'''
create a rock paper scissors game 
'''
import random
 
def get_computer_choice():
    lst_choice = ["rock","paper","scissors"]
    return random.choice(lst_choice)
    

def get_user_choice():
    return input("Please choose rock, paper, or scissors: ")
  
def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It's a tie!")
    elif (computer_choice == 'rock' and user_choice == 'scissors') or (computer_choice == 'scissors' and user_choice == 'paper') or \
        (computer_choice == 'paper' and user_choice == 'rock'):
        print("Computer Wins!") 
    else:
        print("User Won!")
    #elif(computer_choice== 'scissors' and user_choice == 'rock') or (computer_choice == 'paper' and user_choice == 'scissors') or \
       # (computer_choice == 'rock' and user_choice== 'paper'):
        
             
def play(): 
    comp = get_computer_choice()  
    user =  get_user_choice()
    #if  user == comp:
        #return "It's a tie!"
    print(f"Computer picks: {comp}")
    print(f"User picks: {user}")

    get_winner(comp, user)     
    
play()     
      