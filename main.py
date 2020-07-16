import numpy as np

print("Hello DOcker WOrld")

file = open("deneme.txt","r")

print("First 10 CHaracters in file {}".format(file.read(10)))

file.close()

arr = np.zeros(20)

print(arr) 
