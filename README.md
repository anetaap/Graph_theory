# _INSTRUCTION HOW TO USE THE BELLMAN FORD's ALGORITHM_ 💻

- First of all, this algorithm was written in Python, for this reason it is necessary that you have an IDE on your device, an integrated development environment for the Python language (I personally recommend PyCharm). Then all you have to do is clone this repository. 

-------------------------------------------------------------------------------

### _Now you are ready to find the shortest paths in your graph._

#### Some crucial informations about the algorithm:
> Bellman Ford algorithm helps us find the shortest path from a vertex to all other vertices of a weighted graph.
>It is similar to Dijkstra's algorithm but it can work with graphs in which edges can have negative weights.
#### The instruction on how to use this code is as follows: 
1. You must put the list of adjacency  your graph in the ___"graph.txt"___ file, which is in the __"tests"__ folder.
      Or you can just put your own .txt file in the __tests__ folder and change the word ___graph___ on line __44__ to your file name. 

      ![instruction](https://github.com/anetaap/Graph_theory/blob/main/Instructions/Instruction.png)
      
2. Your list of adjacency must look like this: the line number is the vertex where the edge starts, then you enter the end vertex and the weight of the edge one by one in the line. Just like in the picture below. If at a given vertex __no__ edge begins, put "#" in its line.  

      ![instruction1](https://github.com/anetaap/Graph_theory/blob/main/Instructions/Instruction2.jpg)
      
      >_Don't use any commas or periods to separate the data in the list, a single space is enough!_
      
3. When the data of your graph is properly prepared, you just need to run the code in the file ___"main.py"___. By default, the shortest paths are searched from the vertex number 0, if you want to change it, just replace the digit 0 in the line __62__ with another number of the vertex that you are intrested. The vertices are numbered from "___0___" which means each vertex number is 1 less, don't forget about this!   

4. This is what the result will look like: 

      ![instruction2](https://github.com/anetaap/Graph_theory/blob/main/Instructions/instruction3.png)
      
_________________________________
### ___I hope you will find the manual instruction helpful and understandable. Have a nice use!___ ✨
