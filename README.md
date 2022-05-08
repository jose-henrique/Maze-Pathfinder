![Maze pathfinder logo](https://i.imgur.com/d0JN8qJ.jpg')

  
  

![StatusBadge](https://badgen.net/badge/Status/Finished/green)  ![Tech](https://badgen.net/badge/Tech/Python/blue)

  

This project has the objective to practice my programming logic, solving a simple computer science problem, using different ways.

  

##  Project features

  

This project in the moment have 3 different files, each of them have some diferrent features

- Subtitle:
![Subtitle](https://i.imgur.com/4ijJBTZ.jpg)
  

- `finder.py`: This is the most basic demonstration of the code, he have a maze hardcoded as a matrix, and solve the problem using something like a brute force algorithm. This version of the code have two big problems:

    ***First:***  How the moves are based on a for loop, the alorithm become biased, he ever follow the same way, so he acctually don't solve anything, for all choice that his made is ever the same for all trys.

    ***Second:*** This is not efficient, for bigger and bigger mazes he became more slow and with more chance of not solve the maze, as saied on the first point.
	
Exemple of finder solving the maze:
	
![Finder Solving](https://i.imgur.com/uMfnHGC.jpg)

  

- `finderImageMaze.py`: This algorithm, use a image as a maze, following the subtitle bellow. He convert the image into a matrix for process the maze, and show the solution steps as matrix too. But the solving algorithm is the same of above.

Exemple Solving Maze1:
![Solve Maze 1](https://i.imgur.com/0HotLkc.jpg)

This algorithm take more than 2 minutes and not sove the Maze4.

  

- `finderImageRandomMaze.py`:

This method theoretically solve all mazes, but have many problems of efficiency, but two of them are:

  

***First:*** The algorithm pick a direction to "walk" randomly, so he can chose a lot of times the same wrong direction, this make the algorithm depend on lucky, every time you run the code, the way can be different and the time to solve too.

First time solving the Maze4
![First Time maze4](https://i.imgur.com/3AUr0Xo.jpg)
Second time solving the Maze4
![Second Time maze4](https://i.imgur.com/GrZFLiE.jpg)
the diferrence between times is very large.

  

***Second:*** Every time that he arrive in a dead end, he restart from zero, i didn't code a way to back on last good point.

  

- `finderImageBFSMaze.py`: This is the best method that i coded for the project until now, they use BFS algorithm to move through the maze. Basically from a start node the algorithm spread  throug all the maze, and find the shortest way, after find the end node the algorithm backtrack the parents node and show the way. This algorithm have one problem, how much the maze increase more slow he solve, because he move throug all allowed spaces.

Exemple solving the Maze 4, first time:
![BFS Maze 4](https://i.imgur.com/uwzFm5c.jpg)
Exemple solving the Maze 4, second time:
![BFS Maze 4 second](https://i.imgur.com/JG5szoX.jpg)
the diferrence between the two times is almost zero, and the path is shortest than the above algorithm.
  

## Running the project

  

To run this project you need python 3 on your device, type on terminal `python3 [featureYouWant].py`, then the program gonna ask you, what of the mazes tou want to solve, now just let the magic happen.

  

## Creating your own mazes

  

I'm not really good drawing mazes as you can see, so in case you want make it by yourself here the instructions. Just follow the scheme of colors bellow and try make ways have one pixel of width.
![Tble of Color](https://i.imgur.com/Ht3m2pr.jpg)

## Conclusion
This project was very interesting, i learn more about graphs and optmizations of code and i could try to aplly clean code principles. About the algoritms:
- My algortihm, that pick the path randomically, can solve small mazes with low complexity, and he don't chose necessarily the shortest way.
- BFS algorithm solve small mazes more slow than my algorithm, but when the complexity increase he show his power, and ever find the shortest way.

## Next steps
For me this project is already finished, because i don't have a lot of time and i just learn what i wanted, but I'll let here some ideas for you that want to improve the project:
- [ ] Create algorithm using DFS.
- [ ] Print Solution as an animation.
- [ ] Show the solution generating a new image.
- [ ] Thinking other algorithm to solve a maze.

