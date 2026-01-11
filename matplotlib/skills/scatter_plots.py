import matplotlib.pyplot as plt
import numpy as np

# Scatter graphs = Shows relationship between two variables, helps to identify correlation (+,-, None)

x = np.array([0,1,1,2,3,4,5,6,7,7,8])               #hours studied
y = np.array([55,60,65,62,68,70,75,78,82,85,87])    #grades

plt.scatter(x,y,color="violet",
                alpha=0.5,      #alpha = transparency of dots
                s=25)          #s = size

plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grades")

plt.show()