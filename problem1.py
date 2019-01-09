import random

print ("Hello! Let's play Rock-Paper-Scissors!");

options = {1:'rock', 2:'paper', 3:'scissors'};
player_result = ["tie!", "win!", "lose!"];

def collection(user_choice = 42):
  
    while (user_choice not in ['1','2','3']):
       
        print ("Pick a Number: \n 1) \t Rock \n 2) \t Scissors \n 3) \t Paper \n");
        user_choice = raw_input();
       
        if (user_choice in ['1','2','3']):
            break;
    
        else:
            print("\nPlease pick either 1, 2, or 3!\n");


    user_choice = int(user_choice);

  
    comp_choice = random.randint(1,3);
    return (user_choice, comp_choice);


def translate_choices(user,comp):
    print ("\nYou chose " + options[user] +"!");
    print ("Computer chose " + options[comp] +"!");


def compare(x,y):
    result = player_result[ (x-y)%3 ];
    return result;

(user_choice,comp_choice) = collection();
translate_choices(user_choice,comp_choice);
result = compare (user_choice, comp_choice);
print ("You " + result);
