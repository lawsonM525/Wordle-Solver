# Wrodle-Solver
eeeeAAA
Context: Wordle Solver, unconventional approach. User opens an instance of NYTimes wordle and this program and makes initial guess in wordle. They then insert guess into this program that has a  box for each letter and mark it as green/yellow/black with gui element.
Program has an included txt file with all current possible wordle answers arranged in ranked order of possibility.
Program checks the position of the green/yellow/black letters and filters the file into a new list, iterating the list smaller with each guess. 
Aim is to give the user the most probable word according to the rank in the txt file every time they submit a word.

Main problems right now: Code is slightly spaghetti due to AI aid and i'm still fixing it.
main is fine I think?
display has logical calculations which belong in engine
engine logic may or may not work lol. has some duplicate functions or undefined variables
fileIO has some logic which also belongs in engine

GUI past the instruction screen is kinda fucked but can be ignored I can fix it if the rest of the elements work.
