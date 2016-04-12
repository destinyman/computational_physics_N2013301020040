# Sixth Assignment

## ***Abstract***
The problem of picture the trace of firing a shell from a cannon is presented and solved with Euler Method, taking the air drag into account. Given the initial velocity and the firing angle of the shell, one can easily picture the trace in photo and hence get the range of the cannon. 

## ***Introduction***
To shot a shell into the right place with certainty and more accurately has been being  a worldwide problem in military field. Plenty of researched have been done to decrease the deviation to make the bombing more efficiently. One most ideal model to handle the problem is the frictionless "throwing ball" model, where no extra force is considered except for the gravitation. In this case, the trace of the shell is a parabole. The model is intuitive and effective in vacuum atmosphere or in imaginary experiments. When it comes to real life, however, the results deviate much from its actual situation, since the existence of air friction. The atmospheric drag is major factor that affect the movement of the shell in air. In this article, I have taken into the account of the air drag and calculated the position of the shell every "dt" time, and pictured its trace. 
	   In the following, I will introduce the fundamental theory on how to solve the problem physically and the method to calculate the results numerically with Euler method. Then, I will show some pictures with different initial values of the trajectory of the shell.

## ***Theory and Method***
Firstly, I will show the the problem I'm working on, and discuss how to solve the problem. 
**Problem 2.9** 
	Calculate the trajectory of our cannon shell including both the air drag and the reduced air density at high altitudes so that you can reproduce the results. Perform your results with different firing angles and determine the value of the angle that gives the maximum range. 
	To solve this typical mechanics problem, we have to first determine its equations of motion. If we ignore the air resistance, and use Newton's second law, we can obtain:
$$   \frac{d^2x}{dt^2}=0  $$
$$    \frac{d^2y}{dt^2}=-g  $$
where x and y are the horizontal and vertical coordinates of the projectile, and g is the acceleration due to gravity. 
Then, we can rewrite each of the second-order equations as two first -order differential equations 
$$\frac{dx}{dt}=v_{x}$$$$\frac{dv_{x}}{dt}=0$$$$\frac{dy}{dt}=v_{y}$$$$\frac{v_{y}}{dt}=-g$$
where  $v_{x}$ and $v_{y}$ are the $x$ and $y$ components of the velocity. With the above four equations, we can use our standard Euler method to solve each one. Then the equation leads to 
$$x_{i+1}=x_{i}+v_{x,i}\Delta t$$$$v_{x,i+1}=v_{x,i}$$$$y_{i+1}=y_{i}+v_{y,i}\Delta t$$$$v_{y,i+1}=v_{y,i}-g\Delta t.$$

## ***Discussion and Conclusion***

## ***Acknowledgement***



> Written with [StackEdit](https://stackedit.io/).