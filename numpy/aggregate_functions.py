import numpy as np
#Aggregate functions = summarize data and typically return a single value

array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#print(array)
#print(np.sum(array))
#print(np.mean(array))
#print(np.std(array)) #standard deviation
#print(np.var(array)) #variance (square of the standard deviation)
#print(np.min(array))
#print(np.max(array))
#print(np.argmin(array)) #(argument min), locates the index of the lowest value
#print(np.argmax(array))

print(np.sum(array,axis=0)) #if axis = 0 ur summing all the columns
print(np.sum(array,axis=1)) #if axis = 1 ur summing all the rows
