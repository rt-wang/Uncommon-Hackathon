# Uncommon-Hackathon: The Red Planet
Developed by Yichen, Able, Mimi, Yili, Ruotian

In order to run this game, you need to install pyxel, a 2D retro game engine for python games.
```python
pip install pyxel
```
If you want to view the art for this game, run this:
```python
pyxel edit astronaut
```
Then you can run this game through the following command
```python
pyxel run program.py
```
Enjoy.

## Game Description
### Inspiration
Our team drew a lot of inspiration from recent sci-fi films like Dune 2 as well as older ones like the Martian for our story line and setting. We modeled many game design features after retro games we had played ourselves in the past like soul knight or Pokémon (Nintendo DS versions). We also took inspiration from escape rooms, mystery books, and common riddles to design our clue system.

### What it does
Our project is a simple rogue-like retro game where the main character is an astronaut who wakes up without knowing where they are. They can interact with objects and explore the map to find out more clues about themselves and the place they are at. There are also enemies (worms) that can be attacked and can attack you as well as safe houses for oxygen refills and hiding out from worms. There is a good mixture of adventure, story, fighting, and mystery.

### How we built it
We used the Pyxel game engine to build the Red Planet.

### Challenges we ran into
For all of us, this was our first try at using Pyxel to create a project. Most of our team attended a simple workshop the night before, but while that was a good foundation, it left us with many challenges. We started our project with the code from the workshop and worked off it. Our first challenge was reckoning with the fact that the base code tile map used tiles for coordinates whereas much of Pyxel's built-in functions used pixels as coordinates. We also faced challenges with displaying text constantly (instead of resetting each time the game processed) and changing the text based on user input. The worms were perhaps our greatest challenge. We spent a lot of time to make the worms move after the player so that there would a be a higher level of difficulty in fighting. The worms also had to be killed and needed to not enter the safe houses.

### Accomplishments that we're proud of
Our biggest accomplishment is that the game works! While there are still many items and storylines that we did not have time to completely implement, the framework we have set up allows for us to add features very easily. We spent a lot of time working on all the game mechanics, and they all work now!

We are also very proud of our graphics.

### What we learned
We learned how to use Github, Pyxel, and about building a game.

### What's next for Red Planet
We plan to improve the story line and add more details. We also plan to work on the game mechanics some more and add in a proper ending screne.

### Built With
Pyxel