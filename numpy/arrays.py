import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

char_arr = np.array(['Praneeta','Nikhita','Vedas','Hardhik'],dtype=str)
print(char_arr)

print(np.linspace(0,100,20)) # 20 divisions
#print(np.linspace(0,100)) # Default 50 divisions

print(np.logspace(1,20)) # Gives logarithmic arrays from 1 to 20

print(np.arange(1,20,2))
print(np.arange(100,1,-2))

print(np.zeros(20))
print(np.ones(10))
