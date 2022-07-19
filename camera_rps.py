import time
import numpy as np
import random 
import cv2
from keras.models import load_model


class RPS:
    def __init__(self):
        self.num_rounqds = 0
        self.user_score =0
        self.computer_score= 0
        self.comp_msg = " "
        self.user_msg = " "
        
    
    
        #self.computer_score = 0 
        #self.user_score =0
    def get_computer_choice(self):
        lst_choice=  ["rock", "paper", "scissors", "nothing"]
        self.comp_choice = random.choice(lst_choice)
        return self.comp_choice

    def get_user_choice(self):
        prediction = self.get_prediction()
        #print(prediction)  
        if prediction == 0:
        
            self.user_choice = "rock"
    #print(f"{user_choice}")
        elif prediction == 1:
            
            self.user_choice = "paper"
        elif prediction== 2:
             
            self.user_choice="scissors"
            
        else: 
              
            self.user_choice ="nothing"
      
        return self.user_choice

    def get_prediction(self):
        model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        end_time = time.time() +3
    
        while  True:
            
            ret, self.frame = self.cap.read()
            resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            self.prediction = model.predict(data)
            cv2.putText(self.frame, self.comp_msg, (430, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
            cv2.putText(self.frame, self.user_msg, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

            cv2.imshow('frame', self.frame)
            # Press q to close the window
            print(self.prediction)
            self.max_index = np.argmax(self.prediction[0])
            print(self.max_index)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            return self.max_index
        
            
# After the loop release the cap object
   
   

    
    def get_winner(self):
        self.comp_choice = self.get_computer_choice()
        self.user_choice = self.get_user_choice()
        print(self.comp_choice)
        print(self.user_choice)
        if self.comp_choice == self.user_choice:  
            print("It's a tie!")
            #self.num_rounds +=1
            
        elif (self.comp_choice == 'rock' and self.user_choice == 'scissors') or (self.comp_choice == 'scissors' and self.user_choice == 'paper') or \
            (self.comp_choice == 'paper' and self.user_choice == 'rock'):
            
            self.comp_msg =  f"computer choice is {self.comp_choice}"
            print(f"Computer Wins! round {self.num_rounds}")
            
        

            self.computer_score +=1
            #self.num_rounds +=1
        else:
            self.user_msg = f"user choice is {self.user_choice}"
          
            print ("User Wins!")
            self.user_score +=1
            #self.num_rounds +=1
         

def play_game():
    game = RPS()
    while game.num_rounds<4:
        #print(f"Start round {game.num_rounds}")
        
    #return 
       # game.get_computer_choice()
        #game.get_user_choice()
        #game.get_prediction()
        game.get_winner()
        if game.user_score == 3:
            print("User Won!")
            exit()
        
        if game.computer_score ==3:
            print ("Computer Won!")
            exit()
        game.num_rounds +=1
    game.cap.release() 
   
# Destroy all the windows
    cv2.destroyAllWindows()

if __name__ =='__main__':
    lst_choice = ["rock", "paper","scissors"]
    play_game()


    

     #num_rounds =1
   # while num_rounds<3:
        #print(f"Start round {num_rounds}")
        
        #num_rounds +=1
    #return 
   # game.num_rounds +=1
    
#create a class
# iniitialise attribute 
# user score, computer score, number runs, list of choice(rock paper scissors or nothing)

#  create get_computer choice method and return the variable
# get prediction method(code that was downloaded  from the portal and twike to find max index, np.add *argmax
# max index)
# get winner ( manual rps)
# play( while number of rounds less than )

#np.argmax
#  returns index of the max number in the list 
# change the true in the while loop  to a timely condition( start time )





