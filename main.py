import time
import random
import re

money = 100

def play():
  time.sleep(0.5)
  global money
  global bet
  bet = input("=" * 40 + f"\nHow much would you like to bet? (1 - {money})? ")
  if bet == '' or re.search("[^0-9+]", bet) or int(bet) < 1 or int(bet) > money:
    print("You can't bet that amount!")
    play()
  else:
    
    tempdeck = ['A', 'A', 'A', 'A', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']

    computernum1 = tempdeck[random.randint(0, 51)]
    tempdeck.remove(computernum1)
    computernum2 = tempdeck[random.randint(0, len(tempdeck)-1)]
    tempdeck.remove(computernum2)


    usernum1 = tempdeck[random.randint(0, len(tempdeck)-1)]
    tempdeck.remove(usernum1)
    usernum2 = tempdeck[random.randint(0, len(tempdeck)-1)]
    tempdeck.remove(usernum2)

    global currentcards
    currentcards = f"Dealer's cards: [ ] [{computernum2}] \nYour cards: [{usernum1}] [{usernum2}]"

    global usercardarr
    usercardarr = [usernum1, usernum2]
    global dealercardarr
    dealercardarr = [computernum1, computernum2]

    print(f"You've bet {bet}\n" + ("=" * 40) + "\n"  + currentcards)


    #check for blackjack/double As

    usersum = 0
    for i in usercardarr:
      if i == "A":
        usersum += 11
      elif i == "J" or i == "K" or i == "Q":
        usersum += 10
      else:
        usersum += i

    computersum = 0
    for i in dealercardarr:
      if i == "A":
        computersum += 11
      elif i == "J" or i == "K" or i == "Q":
        computersum += 10
      else:
        computersum += i

    if usersum == 21:
      print("You got a blackjack! You win double your bet")
      money = money + (int(bet) * 2)
      print(f"Current balance: {money}")
      play_again()
      quit()
    elif usersum == 22:
      print("You got double As! You win triple your bet")
      money = money + (int(bet) * 3)
      print(f"Current balance: {money}")
      play_again()
      quit()
    elif computersum == 21:
      print("Dealer got blackjack! You lose double your bet")
      dealercards = ""
      for i in dealercardarr:
        dealercards += "[" + str(i) + "] "
      print(f"Dealer's cards: {dealercards} ==> {computersum}")
      print(currentcards[25:])

      money = money - (int(bet) * 2)
      print(f"Current balance: {money}")
      if money <= 0:
        print("You've gone bankrupt! Game over...")
      else:
        play_again()

      quit()
    elif computersum == 22:
      print("Dealer got double As! You lose triple your bet")
      dealercards = ""
      for i in dealercardarr:
        dealercards += "[" + str(i) + "] "
      print(f"Dealer's cards: {dealercards} ==> {computersum}")
      print(currentcards[25:])
      money = money - (int(bet) * 3)
      print(f"Current balance: {money}")
      if money <= 0:
        print("You've gone bankrupt! Game over...")
      else:
        play_again()
      quit()


    def hitorstand():
      
      global currentcards
      global usercardarr
      global money
      

      if len(usercardarr) == 5:
        usersum = 0
        print("=" * 40)

        for i in usercardarr:
          if i == "A":
            usersum += 1
          elif i == "J" or i == "K" or i == "Q":
            usersum += 10
          else:
            usersum += i

        
              
        if usersum > 21:
          print(f"You burst! Your total is {usersum}. You lost twice your bet")
          dealercards = ""
          for i in dealercardarr:
            dealercards += "[" + str(i) + "] "
          print(f"Dealer's cards: {dealercards}")
          print(currentcards[25:])
          
          money = money - (int(bet) * 2)
          print(f"Current balance: {money}")

          if money <= 0:
            print("You've gone bankrupt! Game over...")
          else:
            play_again()
        
        else:
          print(f"You took 5 cards and didn't burst! Your total is {usersum}. You won twice your bet!")
          money = money + (int(bet) * 2)
          print(f"Current balance: {money}")
          
          play_again()


      else:
        actionchoice = input("Would you like to hit or stand? (h / s) \n").lower()

        if actionchoice == "h":
          newcard = tempdeck[random.randint(0, len(tempdeck)-1)]
          tempdeck.remove(newcard)
          currentcards = currentcards + f" [{newcard}]"
          usercardarr.append(newcard)
          time.sleep(1)
          print("=" * 40)
          print(currentcards)
          hitorstand()


        elif actionchoice == "s":
          
          def countingsum():
            global dealercardarr
            global currentcards
            global money
            global bet
            computersum = 0
            for i in dealercardarr:
              if i == "A":
                if len(dealercardarr) == 2:
                  computersum += 11
                else:
                  computersum += 1
              elif i == "J" or i == "K" or i == "Q":
                computersum += 10
              else:
                computersum += i

            if len(dealercardarr) == 5:
              if computersum > 21:
                print("=" * 40 + "\nDealer took 5 cards and burst! You won twice your bet" )
                dealercards = ""
                for i in dealercardarr:
                  dealercards += "[" + str(i) + "] "
                print(f"Dealer's cards: {dealercards} ==> {computersum}")
                print(currentcards[25:])
                money += int(bet) * 2
                print(f"Current balance: {money}")
                play_again()
              else:
                print("=" * 40 + "\nDealer took 5 cards and didn't burst! You lost twice your bet")
                dealercards = ""
                for i in dealercardarr:
                  dealercards += "[" + str(i) + "] "
                print(f"Dealer's cards: {dealercards} ==> {computersum}")
                print(currentcards[25:])
                money -= int(bet) * 2
                print(f"Current balance: {money}")
                if money <= 0:
                  print("You've gone bankrupt! Game over...")
                else:
                  play_again()


            elif computersum < 17:
              newcard = tempdeck[random.randint(0, len(tempdeck)-1)]
              tempdeck.remove(newcard)
              dealercardarr.append(newcard)
              time.sleep(0.5)
              print("Dealer took another card.")
              time.sleep(1)

              countingsum()

            else:
              usersum = 0
              for i in usercardarr:
                if i == "A":
                  if len(usercardarr) == 2:
                    usersum += 11
                  else:
                    usersum += 1
                elif i == "J" or i == "K" or i == "Q":
                  usersum += 10
                else:
                  usersum += i

              if usersum > 21 and computersum <= 21:
                print("=" * 40 + "\nYou burst! You lost your bet!")
                dealercards = ""
                for i in dealercardarr:
                  dealercards += "[" + str(i) + "] "
                print(f"Dealer's cards: {dealercards} ==> {computersum}")
                print(currentcards[25:]  + " ==> " +str(usersum))
                money = money - (int(bet))
                print(f"Current balance: {money}")

                if money <= 0:
                  print("You've gone bankrupt! Game over...")
                else:
                  play_again()

              elif computersum > 21 and usersum <= 21:
                print("=" * 40 + "\nDealer burst! You won your bet!")
                dealercards = ""
                for i in dealercardarr:
                  dealercards += "[" + str(i) + "] "
                print(f"Dealer's cards: {dealercards} ==> {computersum}")
                print(currentcards[25:]  + " ==> " +str(usersum))
                money = money + (int(bet))
                print(f"Current balance: {money}")

                play_again()


              elif usersum > computersum and usersum <= 21:
                print("=" * 40 + "\nYour cards' total is higher! You won your bet!")
                dealercards = ""
                for i in dealercardarr:
                  dealercards += "[" + str(i) + "] "
                print(f"Dealer's cards: {dealercards} ==> {computersum}")
                print(currentcards[25:]  + " ==> " +str(usersum))
                money += int(bet)
                print(f"Current balance: {money}")
                play_again()

              elif computersum > usersum and computersum <= 21:
                print("=" * 40 + "\nYour cards' total is lower! You lost your bet!")
                dealercards = ""
                for i in dealercardarr:
                  dealercards += "[" + str(i) + "] "
                print(f"Dealer's cards: {dealercards} ==> {computersum}")
                print(currentcards[25:]  + " ==> " +str(usersum))
                money = money - (int(bet))
                print(f"Current balance: {money}")

                if money <= 0:
                  print("You've gone bankrupt! Game over...")
                else:
                  play_again()

              elif computersum == usersum or (computersum > 21 and usersum > 21):
                print("=" * 40 + "\nYou and the dealer tied!")
                dealercards = ""
                for i in dealercardarr:
                  dealercards += "[" + str(i) + "] "
                print(f"Dealer's cards: {dealercards} ==> {computersum}")
                print(currentcards[22:]  + " ==> " +str(usersum))
                print(f"Current balance: {money}")

                play_again()

          countingsum()
        else:
          print("That's not a valid option!")
          hitorstand()

    hitorstand()



def play_again():
 
  playagain = input("=" * 40 + "\nPlay again? (yes / no) ").lower()
  if playagain == "yes":
    play()
  elif playagain == "no":
    print("Ok. Good game!")
    exit()
    
  else:
    print("That's not a valid option.")
    play_again()

play()
