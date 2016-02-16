#BlackJack game programmed by Ellissa Barclay de Tolly

#Class

class Card:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite
        self.numValue = self.cardvalue(jazzmine)
        
    def cardvalue(self):
        if self.value== 'Ace':
            return 1
        elif self.value== 'Jack' or self.value== 'Queen' or self.value == 'King':
            return 10
        else:
            return (int(self.value))

    def __str__(self):
        return ("The card value is "+ self.value +" and the card suite is "+ self.suite)

#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
#Main
    
def main ():
    import random
    turncount = 0
    instructions()
    time.sleep( 1 )
    while turncount < 2: 
        if turncount % 2 == 0:
            print("Player 1, it's your turn!")
        elif turncount % 2 == 1:
            print("Player 2, it's your turn!")
#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
#Where hands are dealt and game is played
            
        hand = []
        deck = createDeck()
        random.shuffle(deck)
        #Below is where the Primary hand is dealt 
        hand,deck = dealCard (hand,deck)
        hand,deck = dealCard (hand,deck)
        value = displayHand (hand)
        time.sleep( 1 )
        (value)= playGame(value, hand, deck, turncount)
        if turncount % 2 == 0:
            value1 =  int(value)
        elif turncount % 2 == 1:
            value2 = int(value)
        turncount += 1
    determineWinner(value1, value2)
    time.sleep( 1 )
    print("Thanks for playing Black Jack!")

#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
#Functions
    
def instructions():   
    print("You are playing Black Jack!")
    time.sleep( 2 )
    print("The ultimate goal of this game is to have the highest value of cards")
    time.sleep( 3 )
    print("The only catch is that the value must be under 21")
    time.sleep( 2 )
    print("All number cards are equal to their value")
    time.sleep( 2 )
    print("All face cards are equal to 10")
    time.sleep( 2 )
    print("Aces are equal to 1")
    time.sleep( 2 )
    print("Good Luck!")

def createDeck():
    suitetypes = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    cardvalues =  ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = []
    for suite in suitetypes:
        for value in cardvalues:
            deck.append(Card(value, suite))
    return deck

def dealCard (hand,deck):
    hand.append(deck.pop())
    return hand, deck

def displayHand(hand):  
    value = 0
    print("Here is your hand")
    time.sleep( 1 )
    for card in hand :
        print (card)
        time.sleep( 1 )
    for card in hand:
        value += card.numValue
        time.sleep( 1 )
    print("The value of your hand is " + str(value))
    return value

def playGame (value, hand, deck, turncount):
    hitme = input("Do you want another card? If so, type 'hit me.' If not, type 'pass.' ")
    while (hitme == "hit me"):
        hand,deck = dealCard (hand,deck)
        value = displayHand (hand)
        time.sleep( 1 )
        if (value <= 21):
            hitme = input("Do you want another card? If so, type 'hit me.' If not, type 'pass.' ")
        else:
            print("Sorry, you passed 21!")
            hitme = "pass"  
    print("Your game is over!")
    time.sleep( 1 )
    return value
  
def determineWinner(value1, value2):
    #Determines if both are losers
    if value1 and value2  > 21:
        print("Sorry, you both lost!")
    #Both are Winners
    elif value1 == value2:
        print("interesting, looks like a tie!")
    #If Player1 is a winner (higher value than 2 or less than 21 if 2 is over 21
    if value1 <= 21:
        if value2 > 21:
            print("Congratulations Player One, you win!!!")
        elif value1 > value2:
            print("Congratulations Player One, you win!!!")
    #If Player2 is a winner (higher value than ! or less than 21 if 1 is over 21
    if value2 <=21:
        if value1 > 21:
            print("Congratulations Player Two, you win!!!")                 
        elif value2 > value1:
            print("Congratulations Player Two, you win!!!")

#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
import time
main()


    
