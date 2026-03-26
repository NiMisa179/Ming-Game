# 1. Description
## Mind-Game
The so-called Mind Game with Cards developed in Python by me. 

# 2. Features
* The application uses 2 lists. The first one displays the hidden cards and the second one has the exact position of each card
* Edits Python Lists
* The current state of the game is displayed
* Instructions provided during running
* Guess count
* Saves highscores

# 3. Technologies
* Python3
* Lists
* Parallel Lists
* Loops
* 2-dimension Lists

# 4. Execute the program
1. Save the script as:
   MnimisGame.py
2. Run the program:
   python MnimisGame.py

# 5. Structure
``` text
Ming-Game/    

├── MnimisGame.py         # Main program
└── README.md           # Project Documentation
``` 

# 6. Example Output

``` plaintext

Welcome in mnimis Game!
Will you start? If so, write yes: yes
Type the number of cards you would like to play: 6
    1 2 3 
1:  x x x 
2:  x x x 
Choose your row: 1
Choose your column: 1
    1 2 3 
1:  1 x x 
2:  x x x 
Choose your row: 1
Choose your column: 2
    1 2 3 
1:  1 3 x 
2:  x x x 
--------------------------
    1 2 3 
1:  x x x 
2:  x x x 
Choose your row: 1
Choose your column: 3
    1 2 3 
1:  x x 3 
2:  x x x 
Choose your row: 1
Choose your column: 3
You already have chose that combo! Choose your row between 1 and 2: 1
You already have chose that combo! Choose your column between 1 and 3: 2
--------------------------
    1 2 3 
1:  x 3 3 
2:  x x x 
Choose your row: 3
Choose your row between 1 and 2: 2
Choose your column: 1
    1 2 3 
1:  x 3 3 
2:  1 x x 
Choose your row: 1
Choose your column: 1
--------------------------
    1 2 3 
1:  1 3 3 
2:  1 x x 
Choose your row: 2
Choose your column: 2
    1 2 3 
1:  1 3 3 
2:  1 2 x 
Choose your row: 2
Choose your column: 3
--------------------------
You won!
4
Continue? type yes. Stop? type anything: yes
Type the number of cards you would like to play: 6
    1 2 3 
1:  x x x 
2:  x x x 
Choose your row: 1
Choose your column: 1
    1 2 3 
1:  2 x x 
2:  x x x 
Choose your row: 1
Choose your column: 2
    1 2 3 
1:  2 1 x 
2:  x x x 
--------------------------
    1 2 3 
1:  x x x 
2:  x x x 
Choose your row: 1
Choose your column: 3
    1 2 3 
1:  x x 3 
2:  x x x 
Choose your row: 2
Choose your column: 1
    1 2 3 
1:  x x 3 
2:  1 x x 
--------------------------
    1 2 3 
1:  x x x 
2:  x x x 
Choose your row: 1
Choose your column: 2
    1 2 3 
1:  x 1 x 
2:  x x x 
Choose your row: 2
Choose your column: 1
--------------------------
    1 2 3 
1:  x 1 x 
2:  1 x x 
Choose your row: 2
Choose your column: 2
    1 2 3 
1:  x 1 x 
2:  1 2 x 
Choose your row: 1
Choose your column: 2
You already have chose that combo! Choose your row between 1 and 2: 1
You already have chose that combo! Choose your column between 1 and 3: 1
--------------------------
    1 2 3 
1:  2 1 x 
2:  1 2 x 
Choose your row: 1
Choose your column: 3
    1 2 3 
1:  2 1 3 
2:  1 2 x 
Choose your row: 2
Choose your column: 3
--------------------------
You won!
5
Continue? type yes. Stop? type anything: no
Your highscore was 4

Process finished with exit code 0


```

# 7. Future Improvements

* Keep track of every highscore using a database
* GUI
* Fixed number of cards for each game
* Hide the previous states of the game
  
# 8. Author
Nikos Misailidis 
GitHub: https://github.com/NiMisa179
