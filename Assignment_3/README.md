# Third Assignment

## ***Requirement***
There are three levels for the assignment:
- level one: write a program to show your own name with stars on the screen.
- level two: write a program to display any input word in any order with stars on the screen.
- level three: write a program to display anything you want to draw with a 8*8 point lattice star on the screen.

## ***Abstract and Introduction***
I wrote a program to show letters composed of stars on the screen. The total procedures are divided into three parts or three levels. For the first level, I just wrote a code to display my own name in letters on the screen; For the second level, I wrote two versions level2_2.0 and level2_2.1 to achieve my goal step by step. In version one, I wrote a program only to display one letter once, but the letter are randomly chosen by the user; In version two, I improved the code by adding  a loop to read and output  multiple letters. So in version two, you can input any letters with random order and any length.

## ***Details and code***
For level one, it's quite simple, just write the name with stars and print it out. It is presented downward:
![level1_code](https://github.com/wuweipeng/computational_physics_N2013301020040/blob/master/Assignment_3/resources/level1_code.png)
![level1](https://github.com/wuweipeng/computational_physics_N2013301020040/blob/master/Assignment_3/resources/level1.png)
For level two, as I have said above, I just split the procedure into two parts, the division shows my progress in the program design. In version one, I spent five lines to write every letter with stars and use "**if**" dialog to determine which word the user want to print, hence I could only print one letter at one time.[click here to see the code](https://github.com/wuweipeng/computational_physics_N2013301020040/blob/master/Assignment_3/level2_2.0.pyrrr) some outcomes are listed below:
![level2_2.0](https://github.com/wuweipeng/computational_physics_N2013301020040/blob/master/Assignment_3/resources/level2_2.0.png)
 Then, in version two, I improved the program  by putting all letters into groups and cased them in one array, which provided all sections a number--from 0 to 129; next, the computer only needs to read the contents and order of the letters, and then determine which letters the user have put in and finds the relevant number of the letter and print it out on the screen. [click here to see the code](https://github.com/wuweipeng/computational_physics_N2013301020040/blob/master/Assignment_3/level2_2.1.py). The following are some examples:
 ![level2_2.1](https://github.com/wuweipeng/computational_physics_N2013301020040/blob/master/Assignment_3/resources/level2_2.1.png)

## ***Conclusion***
In conclusion, I have write a program to read and display letters with any length and order. 

## ***Acknowledgement***
While I was writing the code for version 2 level two, I met with problems dealing the connection between the input letters and output letters, thanks to my roommate Xi Cheng, who gave me inspiration to use array to cut letters into pieces and mark them with letters. 