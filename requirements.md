## **Vision**
# 
#### What is the vision for you project?
Our vision is to create a termial version of Black Jack as well as a cheater function that calculated yours scoring odds on a given hand.
#### What pain point is this project to solve?
This is a low risk enviorment to play Black Jack and see what type of scores you can reach. The Jupyter lab will be a way to see what sort out the matmatical probablity of being able to win on a given hand.
#### Why should we care about the project?
You shouldn't. Gambling is bad
# 
## **Scope**
#### In
* **Terminal:**
    * In the terminal there whould be a fully functioning game of black jack that allows for the player to be able to challenge a dealer and be able to see how many points they can amass
    * Scoreing. Can take in a list of cards and be able to see what the persons best possible hand would be or if they instead bust. 
* **Jupyter:**
    * Provide the player with the ability to see what their odds are if they preform certain avctions based on the card that they have seen
#### Out
* Online functionality. This app will be entirely offline
* Desktop Only no application outs
# 
## **MVP**
#### What is the functionality?
The MVP functinality will be to create a version of BlackJack that can be played in the terminal. There will be a partner program that will be able to calculate your odds of scoring on a given hand.

#### **Gaols**
* Create a commandline playable version of Black Jack that allows the user to play against the dealer
* Keep track of the users points to see if they can cross a certain threshold before going bust (Start: 100, Gaol: 250)
* Using Jupyter create a program that can calculate the odds you hav on your current hand for beating the dealer.
#### **Stretch**
* Be able to hot reload you stats in the Jupyter notebook
* Allows multiple players to play at the same time
* Create Bots to play along side you that will try to also beat the dealer
* Allow your odds to take in the probability based on what other cards have bee played on the field
* Imporve the user expierence by creating a better user interface that is more enjoyable to look at
* Allow for more complicated rules to the game like `Double Downs` and `Hand Splits`
* Provide a way with in the program for the user to see the rules of how to play.

# 
## **Functional Requirements**


## **Testing**
This will probably more closely mirror the pattern that we used in the game of greed where we test the input and output with a varity of inputs by over riding the actual game functions for the I/O stream. 