import random
import time

play = True 

while play:
    player = input("[T]aş, [K]ağıt, [M]akas arasından seçim yapınız ==> ")
    player = player.capitalize()
    
    while player != "T" and player != "K" and player != "M":
        player = input("Lütfen T,K veya M giriniz ==> ")
        player = player.capitalize()
    
    computer = random.randint(1,3)
    if computer == 1:
        computer = "T"
    elif computer == 2:
        computer = "K"
    elif computer == 3:
        computer = "M" 
    
    time.sleep(0.5)    
    print("TAŞ...")
    time.sleep(0.5)
    print("KAĞIT...")
    time.sleep(0.5)
    print("MAKAS...")
    time.sleep(0.5)

    
    if player == "T" and computer == "T":
        print("Sen Taş seçtin, Bilgisayarda Taş seçti. Kısaca berabere XD")
    elif player == "T" and computer == "K":
        print("Sen Taş seçtin, bilgisayarda Kağıt seçti. Yani kaybettin :)")
    elif player == "T" and computer == "M":
        print("Sen Taş seçtin, bilgisayarda Makas seçti. Yani sen kazandınnnn!!!")
    
    if player == "K" and computer == "K":
        print("Sen Kağıt seçtin, bilgisayarda Kağıt seçti. Kısaca berabere XD")
    elif player == "K" and computer == "M":
        print("Sen Kağıt seçtin, bilgisayarda Makas seçti. Yani kaybettin :)")
    elif player == "K" and computer == "T":
        print("Sen Kağıt seçtin, bilgisayarda Taş seçti. Yani sen kazandınnnn!!!")
        
    if player == "M" and computer == "M":
        print("Sen Makas seçtin, bilgisayarda Makas seçti. Kısaca berabere XD")
    elif player == "M" and computer == "T":
        print("Sen Makas seçtin, bilgisayarda Taş seçti. Yani kaybettin :)")
    elif player == "M" and computer == "K":
        print("Sen Makas seçtin, bilgisayarda Kağıt seçti. Yani sen kazandınnnn!!!")
        
    play = input("Tekrar oynamak için e, çıkmak için q ya basın ==> ")
    
    player = player.lower()
    
    if play == "e":
        play = True
    elif play == "q":
        play = False
        