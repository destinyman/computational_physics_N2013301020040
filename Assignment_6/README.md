# Seventh Assignment

## ***Abstract***
　　This time, we will talk about a very popular sports(maybe the most popular one in America)--the baseball in America. In this report,  I will show you almost a very close model that is usually used in real life when we talk about the trajectory, then we use the model to calculate the real movement of the baseball after throwing it towards the home plate.

## ***Introduction***
　　The baseball game has fascinated fans in America for many year. There are quite a lot of books and papers written on the physics of baseball than any other sports. In this section, I will consider the trajectory of a batted ball with a more realistic model to take the effect of atmospheric drag into account. The basic equations of motions for a baseball is the same as a shell. In the following, I have written in detail of the problem, and  method to draw the trajectory of the baseball in three dimensional space. Code to fulfill the goal are available.[click here](). 

## ***Theory and calculation***
**problem 2.19**
　　Model the effect of the backspin on the range of a batted ball. Assume an angular velocity of 2000 rpm.
solution to this problem is quite direct and similar to that of the solution of the cannon shell. At least. the basic equations of motion are of the same, which reads:
$$x_{i+1}=x_{i}+v_{x,i}\Delta t$$$$v_{x,i+1}=v_{x,i}$$$$y_{i+1}=y_{i}+v_{y,i}\Delta t$$$$v_{y,i+1}=v_{y,i}-g\Delta t.$$ <br>　　Given the initial values of $x$, $y$, $v_{x}$ and $v_{y}$, we can use equations above to estimate their values at later times.<br>
　　However, a baseball in real life as the expected outcome above. To make the model more realistic, we must modify the force on the baseball when it's flying. In this chapter, I take three major factors into account: the air drag, the effect of the wind velocity and last, the spin of the ball. So in the following, I will explain how these factors affect the motion of the baseball and calculate the collective of these factors overall in one formula.<br>
　　Firstly, we include the air resistance and the effect of the wind velocity to the model and modify the calculation of the trajectory.  Before we do the calculation, we can catch a glimpse of how the air drag influences the motion of the baseball through a picture which show how the drag coefficient changes with the velocity of the baseball.<br>

![p33](https://github.com/wuweipeng/computational_physics_N2013301020040/blob/master/Assignment_7/resources/p33.png)

　　It's evident in the graph that different appearance of the baseball has dramatic influence on the drag coefficient. While the air drag has the relation with the velocity listed below:<br>
$$F_{drag}=-B_{2}v^2$$
with $v=\sqrt{v_{x}^2+v_{y}^2+v_{z}^2}$ <br>
　　After careful modification, the drag factor for a normal ball is described reasonably as <br>
$$\frac{B_{2}}{m}=0.0039+\frac{0.0058}{1+exp[(v-v_{d})/\Delta]}$$$<br>
$with $v_{d}=35m/s$ and $\Delta=5m/s$.<br>
　　Then we add the effect of the wind velocity. Assume that the wind blows at a constant magnitude so that we can simplify the calculation. In that case, the relation between the air drag and the relative velocity of baseball in the air is <br>
$$F_{drag,x}=-B_{2}\left |\overrightarrow{v}-\overrightarrow{v}_{wind}\right |(v_{x}-v_{wind,x})$$$$F_{drag,y}=-B_{2}\left |\overrightarrow{v}-\overrightarrow{v}_{wind}\right |(v_{y}-v_{wind,y})$$where $v_{wind}$ is the velocity of the wind.<br>
　　Finally, I will take the effect of the spin into consideration and solve the problem overall at once.<br>
　　As we have introduced, the origin of the force that makes a spinning ball curve can be appreciated if we recall that the drag force has the form $F_{drag}\sim v_{2}$ , where $v$ is the speed of the object relative to the air. For a ball spinning about an axis perpendicular to the direction of the travel, this speed will be different on opposite edges of the ball, the effect can be graphed as below:<br>

![p37](https://github.com/wuweipeng/computational_physics_N2013301020040/blob/master/Assignment_7/resources/p37.png)
<br>
　　Then for a ball in backspin, the edge of the ball at the bottom will have a larger velocity relative to the air than that of the ball at the top of the ball. This will result in a larger drag force edge of the ball where the velocity is higher. This is known as the Magnus force. In this problem, we assume that the axis of the backspin is along $y$ axis. To gain a more quantitative result, we have to determine the dependence of the Magnus force on the speed. Owing to its incompatible with the real situation if we expect this force to be proportional to $B_{2}$, we will simply argue for general functional form of the force. Under this circumstance, the Magnus force can be written as <br>
$$F_{M}\propto (v+r\omega)^{2}-(v-r\omega)^{2} \sim vr\omega$$
　Thus the net spin-dependent force have the general form <br>
　$$F_{M}=S_{0}\omega v_{x}$$
　 and we have measured the coefficient through experiment,  and estimated that$S_{0}/m \approx 4.1 \times 10^{-4}$ , where $m=149g$ is the mass of the ball.<br>
　 After all considerations, the equations of motion for the baseball are then<br>
$$\frac{dx}{dt}=v_{x}$$$$\frac{dv_{x}}{dt}=-\frac{B_{2}}{m}v v_{x}$$$$\frac{dy}{dt}=v_{y}$$$$\frac{dv_{y}}{dt}=-g$$$$\frac{dz}{dt}=v_{z}$$$$\frac{dv_{z}}{dt}=-\frac{S_{0}v_{x}\omega}{m}$$<br>
the final step is the use the Euler method to solve the above equations. Some typical results are shown below.

![]()


You can also [click here]() to see the source code.
 
##***Acknowledgement***
Thanks to my classmate Feng Cheng for using his code while writing the program.


> Written with [StackEdit](https://stackedit.io/).
