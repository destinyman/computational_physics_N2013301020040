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
$$x_{i+1}=x_{i}+v_{x,i}\Delta t$$$$v_{x,i+1}=v_{x,i}$$$$y_{i+1}=y_{i}+v_{y,i}\Delta t$$$$v_{y,i+1}=v_{y,i}-g\Delta t.$$ Given the initial values of $x$, $y$, $v_{x}$ and $v_{y}$, we can use equations above to estimate their values at later times.
Next we include the air resistance and the reduced air density at high altitude to the model and modify the calculation of the trajectory. We first assume that the magnitude of the drag force on our cannon shell is given by 
$$F_{drag}=-Bv^2,$$where $v=\sqrt{v_{x}^2+v_{y}^2}$  is the speed of the shell. 
Then, we consider how the air density depends on the altitude, which brings the statistical and thermal physics of the atmosphere into what had been a kinematic problem.
   - Isothermal model
  This is the simplest approximation which treats the atmosphere as an isothermal ideal gas. Then, the pressure $p$ depends on altitude according to $$p(y)=p(0)e^{-mgy/k_{B}T}$$ where $m$ is the average mass of an air molecule, $y$ is the height of the point, $k_{B}$ is the Boltzmann's constant, and $T$ is the absolute temperature. Further, for ideal gas, the density depends on altitude is decided according to $$\rho=\rho_{0}exp(-y/y_{0})$$ where $y_{0}=k_{B}T/mg\approx1.0\times10^4 m,$  and $\rho_{0}$ is the density at sea level.
 - Adiabatic model 
 Since we know that the air temperature can vary quite a bit over altitude changes, the isothermal model of atmosphere is not realistic, and hence, we adopt a more realistic and relative accurate model on account that the sir is a poor conductor of heat, which is called *adiabatic * model. In this model, the density depends on altitude according to $$\rho=\rho_{0}(1-\frac{ay}{T_{0}})^\alpha$$ where $a\approx6.5\times10^{-3}K/m$ fits measured data fairly well, and $\alpha\approx2.5$ for air.
 whatever model we choose to estimate the air resistance, the method is of the same. In this problem, the drag force  due to air resistance is proportional to the density, so 
 $$F_{drag}^{*}=\frac{\rho}{\rho_{0}}F_{drag}(y=0)$$ Then, we divide the drag force into $x$ and $y$ components respectively, to determine its equations of motion, and solve the corresponding differential equations. In that case, we find$$F_{drag,x}=F_{drag}cos\theta=F_{drag}(v_{x}/v)$$$$F_{drag,y}=F_{drag}sin\theta=F_{drag}(v_{y}/v)$$
 Overall, the force on the shell is written as $$F_{drag,x}=-\frac{\rho}{\rho_{0}}Bvv_{x}$$$$F_{drag,y}=-\frac{\rho}{\rho_{0}}Bvv_{y}$$. The corresponding equations of motion are $$x_{i+1}=x_{i}+v_{x,i}\Delta t$$$$v_{x,i+1}=v_{x,i}-\frac{\rho}{\rho_{0}}\frac{Bvv_{x,i}}{m}\Delta t$$$$y_{x,i+1}=y_{x,i}+v_{y,i}\Delta t$$$$v_{y,i+1}=v_{y,i}-g\Delta t-\frac{\rho}{\rho_{0}}\frac{Bvv_{y,i}}{m}$$
 Under all above preparation, the resource code is written.[click here](https://github.com/wuweipeng/computational_physics_N2013301020040/blob/master/Assignment_6/assignment_6.py)
 
## ***Results and Discussion***
Here I only display the outcome of the adiabatic model, and compare its corresponding trajectory with one that ignores the air drag.
initial speed $v=100m/s$ , firing angle   $\alpha=45^{\circ}$
![figure_1](https://github.com/wuweipeng/computational_physics_N2013301020040/blob/master/Assignment_6/resources/figure_1.png)

## ***Acknowledgement***
Thanks to WenTao Liu, who helped me when I was having trouble debugging the code.


> Written with [StackEdit](https://stackedit.io/).