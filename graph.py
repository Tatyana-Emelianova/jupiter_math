#1. Определить корни. Корни уравнения: [-6.32174537 -3.25046383  0.40554254]
#2. Найти интервалы, на которых функция возрастает. Функция возрастает на интервалах (-∞; -5) , (-1.111; +∞)
#3 Найти интервалы, на которых функция убывает. Функция убывает на интервале (-5, -1.111)
#4 Построить график
#5 Вычислить вершину. Вершины: (-5, 7.5), (-1.111, -10.144)
#6 Определить промежутки, на котором f > 0 . При х>0.40554254
#7 Определить промежутки, на котором f < 0 При х<0.40554254

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-9, 4,40)
y = 0.6*x**3+5.5*x**2 + 10*x - 5  

fig, ax = plt.subplots()      
ax.plot(x, y, color="red", label="y'(x)") 
ax.plot(np.linspace(-9,4,40), x*0, color = "black")
ax.plot(y*0, 0.6*x**3+5.5*x**2 + 10*x - 5 , color = "black")
ax.scatter(-6.32174537, 0)
ax.scatter(-3.25046383, 0)
ax.scatter(0.40554254, 0)
ax.scatter(-5, 7.5)
ax.scatter(-1.111, -10.144)
ax.set_xlabel("x")                              
ax.set_ylabel("y")                              
ax.legend()   


plt.show()

