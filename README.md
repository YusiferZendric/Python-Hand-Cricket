# Python-Hand-Cricket
Play hand cricket as an individual or as a team of 11 against a team of 11 bots for free on the Python Command Line Interface! More information about the gameplay is available in the [documentation](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/docs/Hand%20Cricket%20Python%20App%20Documentation.pdf).

## About this game

This is a hybrid of cricket and the legacy hand cricket game – implemented in Python and played using the command line interface.

This game was built entirely on Python 3.7.4. It is compatible with all releases of Python 3.5 and later.

The game can be played even without an internet connection.

Tournament mode is not yet included in this game. Customized tournaments can be created using individual team files. For such tournaments, at least 20 MB of disk space is recommended.

Test cricket is fully supported.

This game supports almost all of the laws of cricket which can be implemented in a computer program.

### Pure hand cricket settings
NOTE: To play only the traditional hand cricket game, play a limited overs game, and set a large number of overs (For example, 1000 overs) and 1 wicket as the game settings when prompted.

### Modules:
The source code is located in the [src](https://github.com/BurraAbhishek/Python-Hand-Cricket/tree/main/src) directory. The source code comprises of the following modules:
- [Team setup](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/setupateam.py): Setup your team and it's members. Team members need not be unique, since only one person may actually be an entire team, i.e., the person wants to play as an individual. In that case, the person's name can be the name of each team member.
- [Match registration](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/registerformatch.py): Register a match between your team and another team. To play against the computer, simply skip the play human option.
- [Limited-overs game](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/handcricketgame.py): The limited-overs cricket module. 
- [Test cricket](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/handcricketgametestcricket.py): The test cricket module. 
#### Submodules:
- [src/innings/scoring.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/innings/scoring.py): The innings in which teams try to score big. In limited-overs cricket, this is always the first innings. In test cricket, this is the non-chasing innings.
- [src/innings/chasing.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/innings/chasing.py): The innings in which teams chase the opposition's total.
- [src/modules/batterchoice.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/modules/batterchoice.py): From a given list of players, select the player who will bat now.
- [src/modules/batting.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/modules/batting.py): Module which contains the code for batting.
- [src/modules/bowlerchoice.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/modules/bowlerchoice.py): From a given list of players, select the bowler.
- [src/modules/bowling.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/modules/bowling.py): Module which contains the code for bowling.
- [src/modules/scoreinput.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/modules/scoreinput.py): This module contains the code to play each ball by using the batting and bowling modules.
- [src/modules/commentary.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/modules/commentary.py): Generate the commentary for each ball bowled, based on the result of that ball.
- [src/modules/scorecard.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/modules/scorecard.py): Generate the innings scorecard at the end of each innings.
- [src/modules/superover.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/modules/superover.py): The super over tiebreaker. 
- [src/modules/hashfunc.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/modules/hashfunc.py): Contains the hashing and verification algorithms used, by importing the required modules. Therefore, if a stronger algorithm is found, it is easier to simply update the algorithm from this file than to update the algorithms everywhere.
- [src/modules/toss.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/modules/toss.py): Toss to decide which team bats / fields first. This code is not compatible with super over games, since this decision is the reverse of their decision in the latest tied game
- [src/modules/followon.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/modules/followon.py): Only works for test cricket. Determine whether the team which batted first can enforce the follow-on or not. This code runs only if the team batting first leads by a certain threshold.
- [src/modules/savegamedata.py](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/src/modules/savegamedata.py): Saves the completed game into a JSON file.

Some folders (directories) have a README.md file. Please read them carefully as they describe the contents of that directory

## Getting Started:
### Rules of the game:
This game is a hybrid of cricket and hand cricket and runs on the Python Command-line interface. 
- To know more about hand cricket, visit https://www.instructables.com/id/How-to-Play-Hand-Cricket/
- To know more about the laws of cricket, visit https://en.wikipedia.org/wiki/Laws_of_Cricket

#### NOTE: The scoring and dismissal mechanisms are determined by the rules of Hand Cricket. The rest of the game follows the Laws of Cricket

The ultimate goal is simple: Score more than your opponent to win.
### Pre-requisites:
To play this game, you need to have Python software installed. The software was built on Python 3.7.4, while the newest release as of 28 June 2021 is Python 3.9.6. Go to https://www.python.org/downloads to install the latest version.

Supported platforms:
-	Microsoft Windows 7 or later
-	Android API 24 or later (Apps are available on the Play Store)
-	Mac OS X 10.6 or later
-	Linux 

Either download this entire repository to play this game, or clone this repository using:

```
$ git clone https://github.com/BurraAbhishek/Python-Hand-Cricket.git
```

Disk space: 32 MB (minimum), 256 MB or more (recommended).

## Features of cricket which are not implemented in this game
- [Run out](https://en.wikipedia.org/wiki/Run_out): The batter fails to reach the crease before the wickets fall.
- [Extras](https://en.wikipedia.org/wiki/Extra_%28cricket%29): Wides, no balls, byes, leg-byes. 
- This game implements a 6-run penalty for wrong bowling input. In actual cricket, various infractions by the fielding side can lead to 5 penalty runs.
- Rain delay and [DLS](https://en.wikipedia.org/wiki/Duckworth%E2%80%93Lewis%E2%80%93Stern_method) par score

### Known bugs

Rain delay and abandoned matches are not yet implemented in this game. However, deliberately closing the application in order to avoid losing a match is considered as an abandoned match. This issue can't be fixed, since there are other ways to get around it, for example, by manually editing the JSON team files.

# License

The source code is licensed under the terms of the [MIT License](https://github.com/BurraAbhishek/Python-Hand-Cricket/blob/main/LICENSE), unless specified otherwise.

The sample games and documentation are licensed under the Creative Commons CC0 license.
