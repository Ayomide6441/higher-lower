# Project: Higher or Lower

The higher or lower game in this case is a game to compare between two instagram accounts who has the highest number of followers. This game will help you practice dictionaries, loops and other parts of python.

## Your Task

- Generate a random account from the game data.
- Format account data into printable format.
- Ask user for a guess.
- Check if user is correct.
- Get follower count.
- Give the user a good feedback.
- Score Keeping.
- Make game repeatable.
- Make B become the next A. Check the project notion site for example
- Add art.

## FAQ

Why does choice B always become choice A in every round, even when A had more followers?

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k).
Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and
someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the
comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A
each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense
