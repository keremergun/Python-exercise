import random

play = True 

while play:
    player = input("[T]aş, [K]ağıt, [M]akas arasından seçim yapınız ==> ")
    player = player.capitalize()
    
    while player != "T" and player != "K" and player != "M":
        player = input("Lütfen T,K veya M giriniz")
    
    computer = random.randint(1,3)
    if computer == 1:
        computer = "T"
    elif computer == 2:
        computer = "K"
    elif computer == 3:
        computer = "M" 
    
                         