# <a name="top"></a> Hoppers

A recreation of the board game Checkers, made using Python and the Pygame library.

## Navigation
<a name="navigation"></a>
1. [Game Description](#description)
2. [How to Play](#howtoplay)
3. [Installation](#installation)
    - [Pre-Installation](#preinstallation)
        - [For Windows](#windows)
        - [For Linux](#linux)
        - [For Mac OS X](#macos)
    - [Running the game](#running)
4. [Documentation](#documentation)
    - [Project Directory Structure](#projdir)
    - [Overview of Code](#overview)
5. [Extending the Game](#extending)
6. [License](#license)
7. [Members](#members)
8. [Member Contributions](#contributions)

## <a name="description"></a>Game Description


Hoppers is a **2-player game** and players are on opposite side of the gameboard.

In this game, only the dark squares of the checkers board is used.
All pieces are classified into two categories:
1. **Uncrowned pieces called pawn**
2. **Crowned pieces called kings**

**Pawn** can only move one step diagonally forwards. \
**Kings** can move diagonally forwards and backwards. \
When a man reaches the king row (the farthest row forward), it becomes a king.

**Rules:** \
**1.** If an opponent piece is in a place where you could normally move, and there is an empty space directly across from it, you can “jump over” it and remove the opponent’s piece.

**2.** If this leaves you in a position to jump another piece, you must continue to do so.

**3.** The player without pieces remaining, or the player who has no move due to being blocked, loses the game.





[Back to top](#top)

## <a name="howtoplay"></a>How to Play

Once you open our game, you'll be greeted with our menu screen.
<img src="https://i.imgur.com/gTeMWQs.png" width="400" height="400">

Select your desired mode of play.

<img src="https://i.imgur.com/qXsirb7.png" width="400" height="400">

Now you'll see the game board. 
Simply click on a piece to select it.
<img src="https://i.imgur.com/FcUPXKv.png" width="400" height="400">

Then click on a space to choose where you want to move it to.
<img src="https://i.imgur.com/qnfqsor.png" width="400" height="400">

[Back to top](#top)

## <a name="installation"></a>Installation

For an easy installation you can download the executable [here](https://github.com/shadowshadow725/blank/releases/latest)

If you would rather get the source code and run it manually then follow the steps below:

#### <a name="preinstallation"></a>Pre-Installation

It is recommended that you have the following installed before downloading our game:

- Python 3+
- Pygame
- Git

[Back to top](#top)

#### <a name="windows"></a>For `Windows`
Install Git for windows [here](https://git-scm.com/download/win)\
Install Python3 for windows [here](https://www.python.org/downloads/windows/)

Install Pygame:
```bash
pip3 install python-pygame
```

[Back to top](#top)

#### <a name="linux"></a>For `Linux`

Use the following commands to install the required software:
```bash
Sudo apt-get install git
Sudo apt-get install python3
Sudo apt-get install python3-pip3
pip3 install python3-pygame
```

[Back to top](#top)

#### <a name="macos"></a>For `Mac OS X`

Optional: Install the homebrew package manager [here](https://brew.sh/).

Install Git for Mac OS X [here](https://git-scm.com/download/mac)\
Install Python3 for Mac OS X [here](https://www.python.org/downloads/mac-osx/)
`Pip3` comes with Python3

Use the following commands to install the required software:
```bash
brew install git
brew install python3
pip3 install python3-pygame
```

[Back to top](#top)

#### <a name="running"></a>Running the game
To run the game you must run the following commands after installing the above software.

```bash
cd Documents/Project/
git clone https://github.com/shadowshadow725/blank.git
cd blank/
python3 visualizer.py
```

The game may also be made into an executable or app file using your choice of third party software.

[Back to top](#top)

## <a name="documentation"></a>Documentation

Some detail about what we used (mvc, pygame, python, etc)

#### <a name="projdir"></a> Project Directory Structure

How are repository is structured into folders/classes

[Back to top](#top)

#### <a name="overview"></a> Overview of Code

How the components of the project work together and anything else about our design. Where someone would look if they wanted to make changes

[Back to top](#top)

## <a name="extending"></a>Extending the Game

<!-- Some out of scope ideas we had that could be implemented later. -->
Some ideas we had that could be implemented in the future:

| Feature | Description |
| :----------------- | :------------------------------------------------------------------------------------------------ |
| Jump count tracker | When a piece is jumped over the opponent gains a piece jumped |
| Improved sprites | Improved sprites of pieces |
| Turn timer | A time limit for the player that decreases on their turn. Once a player's timer ends, the opponent wins |
| Harder computer modes | Harder HumanVSComputer modes with more advanced algorithms for finding paths of possible jumps |
| Account creation | Lets the user create an account |
| Games played history | A history linked to each account that keeps track of the games a user played |
<!-- Example of a feature that can be implemented and how someone would go about implementing it. -->

#### Example of an Extension

As an example, we will go through the process of adding in a new HumanVSComputer difficulty level.\
This will require us to make changes to the following files:
- MainMenu
- CheckersHumanVSComputer
- PlayerComputer
- PlayerComputerKing

###### PlayerComputer and PlayerComputerKing
1. Implement a new method into the two player classes using the naming convention `_get_<difficulty>_move`. This method should return a list of moves.
2. Update the `get_move` method to allow the user to set a players difficulty to the newly added difficulty. This simply requires you to add a new `elif` statement.

###### CheckersHumanVSComputer
1. Store the difficulty as a variable
2. Set the opponents pieces to computer players with the difficulty.

###### MainMenu
1. Inside the `create_buttons` method, draw a new button (small than the mode buttons) with a label for the difficulty you are adding.
2. Add a method similar to `get_game_mode` that instead gets the difficulty.

###### Visualizer
1. Add in some code that checks if both the computer mode and a difficulty are selected. Difficulty can be ignored when the opponent is human.
2. Pass the difficulty to the controller

[Back to top](#top)

## <a name="license"></a>License

Hoppers is distributed under the [MIT License](https://choosealicense.com/licenses/mit/).

Copyright © 2019 Team_blank_290

The conditions of the license are located at the root directory of the repository within the [LICENSE](https://github.com/shadowshadow725/blank/blob/master/LICENSE) file.

[Back to top](#top)

## <a name="members"></a>Members

Team Blank is a group of University of Toronto, Mississauga students taking the course CSC290 (Communication Skills for Computer Scientists).

The following members contributed to this project:

-	Adam Wloszczak
-	Zuhair Syed
-	Yu-Chieh Wu (Sunny)
-	Xinhao Hou (Andy)
-	Ronald Chen

[Back to top](#top)

## <a name="contributions"></a>Member Contributions

Below are paragraphs for each members to describe their contributions to the project:

##### Adam Wloszczak

...

##### Zuhair Syed

...

##### Yu-Chieh Wu (Sunny)

...

##### Xinhao Hou (Andy)

...

##### Ronald Chen

...

[Back to top](#top)
