#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Again, your lists should be random numbers
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = 5,7,2,9,1,1,3,8,6,9
#Player Two = 3,8,5,5,8,1,4,7,4,7
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

#List 1
print("Are you ready to Duel, Player 1 and Player 2?")

import random

player1List = []

for i in range(10):
    player1List.append(random.randint(1, 50))
    
print(f"Player 1's Numbers are: " + str(player1List))

#List 2
import random

player2List = []

for i in range(10):
    player2List.append(random.randint(1, 50))
    
print(f"Player 2's Numbers are: " + str(player2List))

#Compare Lists and display wins
player1Wins = 0
player2Wins = 0

for i in range(len(player1List)):
    if player1List[i] == player2List[i]:
        player2Wins += 0

for i in range(len(player1List)):
    if player1List[i] > player2List[i]:
        player1Wins += 1

for i in range(len(player1List)):
    if player1List[i] < player2List[i]:
        player2Wins += 1

print(f"Player 1 won " + str(player1Wins) + " times")
print(f"Player 2 won " + str(player2Wins) + " times")

#Highest numbers and index for players
player1Highest_num = max(player1List)
player1Highest_index = player1List.index(player1Highest_num)

player2Highest_num = max(player2List)
player2Highest_index = player2List.index(player2Highest_num)

#Lowest numbers and index for players
player1Lowest_num = min(player1List)
player1Lowest_index = player1List.index(player1Lowest_num)

player2Lowest_num = min(player2List)
player2Lowest_index = player2List.index(player2Lowest_num)

#Print High Results
print(f"Player 1's Highest number is " + str(player1Highest_num) + " at index " + str(player1Highest_index) + ".")
print(f"Player 2's Highest number is " + str(player2Highest_num) + " at index " + str(player2Highest_index) + ".")

#Print Low Results
print(f"Player 1's Lowest number is " + str(player1Lowest_num) + " at index " + str(player1Lowest_index) + ".")
print(f"Player 2's Lowest number is " + str(player2Lowest_num) + " at index " + str(player2Lowest_index) + ".")






