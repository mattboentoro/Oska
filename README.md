# Oska
Consider the game of Oska, whose rulesare as follows:Oska is played on a board like that shown below.  The two players face each other across the board.  Each player begins with four pieces, placed one to a square in each of the four squares nearest that player.
```
 ---------------
| W | W | W | W |
 ---------------
  |   |   |   |
   -----------
    |   |   |
   -----------
  |   |   |   |
 ---------------
| B | B | B | B |
 ---------------
```
The player with the white pieces makes the first move, andthe players alternate moves after that. A player may choose to move one of his or her pieces in one of these ways:  
1. A piece may be moved forward on the diagonal, one space at a time,to an empty space, as in checkers or draughts.
2. A piece may jump forward on the diagonal over an opponent's piece to an empty space, thereby capturing the opponent's piece and removing it from the board. This capturing move is again like that seen in checkers or draughts.  Unlike checkers, however, only a single capture is permitted on one turn; multiple jumps are not allowed.  Also, even if a capture is possible, it does not have to be made if other moves are possible.

The players alternate moving pieces until one of the players wins. If a player can't make a legal move ona given turn, the player loses that turn and the opponent makes another move. A player wins when:  
1. All the opponent's pieces have been removed from the board, or
2. All the player's REMAINING pieces have been moved to the opponent's starting (or back) row. 

Note that this rule makes the strategy for this game most interesting. A player may want to sacrifice pieces in order to have fewer pieces to move to the opponent's startingrow.  But this approach carries some risk in that every sacrificed piece brings the player closer to having all of his orher pieces removed from the board, thereby losing the game.  

As envisioned by its inventor, Bryn Jones (with refinements by Michael Woodward, who made this charming game available commercially), the game of Oska was intended to be played with only four pieces on each side. Now, however, we are extending the definition of Oska to include any similar game involving n white pieces, n black pieces, and a correspondingly larger board of 2n-3 rows (where n is greater than or equal to 4).  

Thus, an Oska game with 5 pieces on each side would look like this:  

```
 -------------------
| W | W | W | W | W |
 -------------------
  |   |   |   |   |
   ---------------
    |   |   |   |
     -----------
      |   |   |
     -----------
    |   |   |   |
   ---------------
  |   |   |   |   |
 -------------------
| B | B | B | B | B |
 -------------------
```
