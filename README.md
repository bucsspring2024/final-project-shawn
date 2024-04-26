# Battleship
## CS110 Final Project Spring, 2024

## Team Members

Shawn Healy

## Project Description

This project will allow the user to play a game of the classic board game, Battleship, against an AI. You will be prompted to choose between an easy and hard difficulty: in the easy mode, the AI will fire completely randomly with no strategy and in the hard mode it will fire randomly at first, but once it has hit its target it will use an algorithm to sink the ship in the most efficient manner possible. Before the game begins, the user will be prompted to place their ships by clicking on the cell they want and hitting enter and then the Ai will do the same. The player and Ai will alternate attacks until one player's entire fleet is sunk and a player has been declared the winner which will create an ending screen for the game.

### Additional Modules Used

pygame-menu: https://pygame-menu.readthedocs.io/en/latest/


## GUI Design

### Initial Design
 
![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start Menu
2. 2 Difficulty Levels
3. Game Over Screen
4. Data Permanence Feature: Saves High Score (Lowest amount of moves it took to win)
5. Ship Placing

### Classes

- Board:
- Cell:
- Ship:
- Ai:
- Player:
- Controller:

## ATP

### Test #1: Test Start and Difficulty Buttons

- Step 1: Start Game
  - Open terminal, go to project folder, type: python main..py
  - Click on start button
  - Click on either easy or hard
- **Expected Outcome**
  - Two grids should appear with an ocean background and you should be prompted to place your carrier


### Test #2: Test Data Permanence Feature: High Score

- Step 1: Start Game
  - Open terminal, go to project folder, type: python main..py
  - Click on high score button
- **Expected Outcome**
  - A new menu will appear which displays the current high score, which is the least amount of turns a user has won in (minimum score possible is 17)
  - If the user breaks the high score while playing, this should update and they can view it after


### Test #3: Test Placing Ships

- Step 1: Start Game
  - Open terminal, go to project folder, type: python main..py
  - Click on start button
  - click on either easy or hard
- Step 2: Place ship
  - Click on 5 consecutive squares and hit enter
- **Expected Outcome**
  - The squares you selected will first turn green and then when five have been selected and you hit enter, a ship should appear in those cells
  - This process should work for all 5 ships which vary in length


### Test #4: Test Game Over Screen

- Step 1: Start Game
  - Open terminal, go to project folder, type: python main..py
  - Click on start button
  - Click on either easy or hard
- Step 2: Place ships
  - Use the steps from test 3 to place all five ships as prompted
- Step 3: When prompted alternate attacking with the Ai until the game is over by clicking on the cell you want to attack
- **Expected Outcome**
  - If you have sunk all the Ai's ships then you have won the game and a new screen will appear telling you that you have won
  - If the Ai has sunk all of your ships, then the game will end a screen will appear telling you that you have lost.


  ### Test #5: Testing Medium Difficulty

- Step 1: Start Game
  - Open terminal, go to project folder, type: python main..py
  - Click on start button
  - Click on medium
- Step 2: Place ships
  - Use the steps from test 3 to place all five ships as prompted
- Step 3: When prompted alternate attacking with the Ai by clicking the cell you want to attack
- **Expected Outcome**
  - Based on the algorithm, once the Ai has randomly hit one of your ships they should begin by shooting at the cell next to it. Once the first hit is recorded is should take at maximum number of tries to sink the ship as its length + 2