#1 import the random module 

import random

#2 creted subjects

subjects =[
 "Salaman Khan",
 "Virat Kholi",
 "Nirmala Sitharaman",
 "A Group Of Monkeys",
 "Prime Minister Modi",
 "Auto Rickshow Driver from Delhi",
]

actions =[
 "Launches",
 "Cancels",
 "dances with",
 "eats",
 "declares war on",
 "orders",
 "celerabrates",
]

palces_or_things =[
 "at Red Fort",
 "in Mubmbai Local Train",
 "a plote of samosa",
 "inside parliament",
 "at Ganga Ghats",
 "during IPL Match",
 "at india Gate",   
]

#3 start the headline generation loop
while True :  
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(palces_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\n Do you want another headline? (yes/no)").strip().lower
    if user_input == "no":
        break

    #print goodbye message
    print("\nThanks for using the Fake News Headilng Generator. Have a fun day ")  
