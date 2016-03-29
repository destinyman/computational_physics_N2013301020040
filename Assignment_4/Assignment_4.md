# simulation of population growth model

## ***Abstract***
 In this part, I have wrote a program to simulate the initial value problem of the population growth model and curved  the result with the help of Matplotlib. The main method I have used is the Euler method. From the curve, we can see that with different initial values of the model: mainly the initial population, the parameter ' **a** ' and " **b** ", the shapes of the curves differ much from each other.

## ***Background Introduction***
   The population growth model was first presented by [Thomas Robert Malthus](http://www.baidu.com/link?url=vVos2-we_tXKQp6m6Z90Lwsym8wepCHdk_a1BnGMLmZliAX5MyIySH4zxRvQa5edAcnpIJSN8DZou6WWVGgNCK&wd=&eqid=f93bf0730008e74a0000000556f94365) , who is an English cleric and scholar, influential in the fields of political economy and demography. Inspired by ancient concepts about mankind, he thought that the dangers of population growth precluded progress towards an Utopian society: *"The power of population is indefinitely greater than the power in the earth to produce subsistence for man."* and later gave out his own theory of the population growth model. By which, he meant that *the increase of population is necessarily limited by the means of subsistence, that population does invariably increase when the means of subsistence increase, and, that the superior power of population is repressed, and the actual population kept equal to the means of subsistence, by misery and vice.* On the basis of his theory, scientists have developed various of  modern population growth model to track the population problem. In the following, I have first presented the model we met and use Euler method to solve the problem numerically. Later, I plotted the tendency in terms of N-t. Lastly and discussed the influence of the parameters in the formula on the shape of the curve.
 
##  ***Body***

- ***problem***
  Firstly, I showed the problem in chapter.
1.5 Population growth problems often give rise to rate equations that are first-order. For example, the equation
 
  ![](http://latex.codecogs.com/gif.latex?dN/dt=aN-bN^2)

might describe how the number of individuals in a population , N , varies with time. Here the first term aN corresponds to the birth of new members, while the second term -bN^2 corresponds to deaths. The death term is proportional to https://github.com/wuweipeng/computaitional_physics_N2013301020040/blob/master/Assignment_4/pictures/CodeCogsEqn(1).gif?raw=true to  allow for the fact that food will become harder to find when the population becomes large. Begin by solving the equation above, with using the Euler method, and compare your numerical result with the exact solution. Then solve the equation with nonzero values . Give an intuitive explanation of your results. Interesting values of and depend on the initial population . For small ,is a good choice, while for a good choice is .

- ***methods and program ***
From the given information, it is clear that the first-order rate equation has been given, so we can use the Euler method to calculate the expect value of population, given the initial value. The formula to that is shown as following:

With these theoretical preparations, the source program is written. [click here to cheek the program](https://github.com/wuweipeng/computaitional_physics_N2013301020040/blob/master/Assignment_4/assignment_4.py)

- ***results and discussion***
And finally, with the help of Matplotlib, I have drawn several pictures shown below with different parameters and initial values. They are shown below.

it is very clear that with different parameters, a and b, the curve develops quite different, as well, which can be easily accounted by the balance between birth rate and death rate. When a>bN, which means the number of new members overpasses that of death, hence the population goes up in term of explosion rate. On the contrary, when a<bN, which means human beings suffer from great catastrophes and the death rate suddenly rises up, in this case, man kind are dying out and the population goes down.
while when a=bN, which means the birth rate almost equals the death rate, then the population will level out and stays in the same degree, which is a ideal society we have dreamed.

## ***Acknowledgement***
The main structures of my program are adapted from the example program of my computational physics teacher--[Hao Cai](https://github.com/caihao). I really appreciate it. My roommate Qiang Zhang also helped when I was picturing the curve. Thanks a lot.  
> Written with [StackEdit](https://stackedit.io/).