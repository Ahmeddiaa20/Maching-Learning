
# First Application ( Mean , Median , Mode ) Ahmed Diaa Monir
data = [12,18,14,20,16]
mean = sum(data)/len(data)
print(sum(data))
print(len(data))
print(mean) # the value is the numbers of array / the number of them
print(f"Mean: {mean}") # Here we do print to see Mean : the value of Mean
Sorted_Data = sorted(data)
print(Sorted_Data) #Here we can see the numbers be [ 12 , 14 , 16 , 18 , 20]
numbers = len(Sorted_Data)
print(numbers) # see how much value 
median = (Sorted_Data[numbers // 2] + Sorted_Data[(numbers - 1) // 2]) / 2 
print(median) # the middle of them 
print(f"Median : {median}")
from statistics import mode
mode_value = mode(data)
print(f"Mode = {mode_value}") # here we got the mode from statistics and do value for it 