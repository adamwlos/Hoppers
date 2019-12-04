# <a name="top"></a> Hoppers

A recreation of the board game Checkers, made using Python and the Pygame library.

## Navigation
<a name="navigation"></a>
1. [Game Description](#description)
2. [How to Play](#howtoplay)
3. [Installation](#installation)
    - [Pre-Installation](@preinstallation)
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

Screenshots and breif descriptions of what they show happening
(Use imgur to host images)

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
Sudo apt-get install pip3
pip3 install python-pygame
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
brew install python
pip3 install python-pygame
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

Maybe you'd like to try extending our project? Here are a few ideas that we had for extra features which we never got around to implementing.

- More difficulties for the computer player
- Creating image assets and using them to show the game elements rather than using Pygame's built in drawing functionality

Here is an example of how you can add a new computer player difficulty to our game.  Assuming you've come up with an algorithm for finding 
the moves for the difficulty, first create a new private method in our PlayerComputer and PlayerKing classes which returns a list of Move 
objects. eg:_get_new_difficulty_move(self).  Take a look at the Move class in our Models folder to learn how to create Move objects. Then 
navigate to our get_move() method in the PlayerComputer and PlayerKing classes. Decide on any integer to represent your new difficulty, 
(Our difficulty uses 0, so make sure not to use that) and add a block to the if statement which checks if the difficulty variable 
corresponds to yours. Then simply return the value of your new private method in this block.

Or maybe you want to improve the look of our game with your own pictures? Go ahead and open up our visualizer class. This class is the only 
one concerned with rendering the game, so no need to worry about switching between multiple classes! Our create_board() method updates the 
screen with a new board by drawing the grid tiles and the pieces on top. To change the look of the pieces, simply replace each call of 
pygame.draw.ellipse() with logic to draw your own picture in the corresponding space.

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
