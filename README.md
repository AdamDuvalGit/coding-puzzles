# coding-puzzles
Coding interesting puzzles

# How to Solve the Hiding Cat Puzzle
Simulations to find the cat hiding in a box. 

Rules of the game: 
There are five box and a cat is hiding in one of them. In each move we can open one box to try and find the cat. If we find the cat, we win. If not, the cat moves exactly one box to the left or right, unbeknown to us.

Goal:
What strategy will you use to find the cat as soon as possible? And, in how many moves maximum will your strategy find the cat?

Description:
Please watch this YouTube video for a detailed explanation of the game rules and educated selection of the optimal strategy: https://youtu.be/yZyx9gHhRXM?si=nFpKEKeHUZJAnNQ1

This simulation plays the Hiding Cat Puzzle game with five boxes and one cat. The cat hides in one box. Each morning we can open one box to find the cat. If the cat is the opened box, we win. If not, the cat moves exactly one box to the left or right. We, of course, do not know where it moved. Randomly opening the boxes or opening them from left to right (or right to left) is not effective in terms of finding the cat reliably. It can take infinite number of moves to find it unless you get lucky.

The traditional approach (the one described in the above mentioned video) is to assume the cat starts in an even-numbered box. Therefore, with each move it alternates between the odd and even numbered boxes. The most effective way has proven to be the "2-3-4-4-3-2" sequence, which guarantees finding the cat in six or fewer moves. With this approach you will certainly find the cat in six or fewer moves.

I argue and demoonstrate theoretically and empirically that this approach is effective but not efficient. It does not take into account probabilities. More specifically, it does not utilize Bayesian inference. By opening a box and not finding the cat, we gain additional information. Therefore, we can update the probability of the cat hiding in each box before opening another box. In other words, we can use a sequence that uses Bayesian inference instead of the traditional method.

For a game with five boxes, the effective sequence then becomes "2-2-4-4-3-2-2". This sequence also guarantees finding the cat in six or fewer moves. However, it is not only effective but more efficient compared to traditional approach. This approach guarantess finding the cat in seven or fewer moves (which is one move in addition to the traditional method). However, the cumulative probability of finding the cat prior to seven is greater for each move (except the first) comppared to the traditional method.

The simulation using Python empirically shows that the Bayesian approach is more efficient by building and comparing the cumulative distribution functions of the two approaches. With the Bayesian approach, the cumulative probability of finding the cat in earlier moves is significantly greater.

This is important in cases with limited resources (which is like always!). If each move costs us something, for example, money or timem, then the Bayesian approach is more profitable for the player. And, getting to the seventh move is highly unlikely. The chance of finding the cat under this approach in six or fewer moves is more than 96%!
