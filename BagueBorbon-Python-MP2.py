import math

x1, y1, x2, y2, x3, y3 = (int(x) for x in input('Enter the 3 data points separated by spacebars.' 
                                   'NOTE: It should be entered in this format: '
                                   'x1 y1 x2 y2 x3 y3: ').split())

D = (((x1**2-x3**2)*(x1-x2)+( y1**2-y3**2)*(x1-x2)+(x2**2-x1**2)*
          (x1-x3)+(y2**2-y1**2)*(x1-x3))//(2*((y3-y1)*(x1-x2)- 
           (y2-y1)*(x1-x3)))); 
              
E = (((x1**2-x3**2)*(y1-y2)+(y1**2-y3**2)*(y1-y2)+(x2**2-x1**2)* 
          (y1-y3)+(y2**2-y1**2)*(y1-y3))//(2*((x3-x1)*(y1-y2)-
           (x2 - x1)*(y1-y3))));  
 
F = (-x1**2-y1**2)-(2*E*x1-2*D*y1);  

H = -E;  
K = -D;  
SQUARERADIUS = (H**2)+(K**2)-F;
R = round(math.sqrt(SQUARERADIUS),2);
    
print("Given the data points: ", (x1,y1), ",", (x2,y2), ", and ", (x3,y3));
print("The center is = ", (H, K));  
print("The radius is = ", R);  
print("The vector [D, E, F] is = [" + str(D) + ", " + str(E) + ", " + str(F) +"]");

