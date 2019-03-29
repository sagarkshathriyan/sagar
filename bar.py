import matplotlib.pyplot as plt 

# x-coordinates of left sides of bars 
left = [1, 2, 3, 4, 5] 

# heights of bars 
height = [10, 24, 36, 40, 5] 

# labels for bars 
tick_label = ['DC', 'CSK', 'MI', 'RCB', 'RR'] 

# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
		width = 0.6, color = ['yellow', 'red']) 

# naming the x-axis 
plt.xlabel('x - axis') 
# naming the y-axis 
plt.ylabel('y - axis') 
# plot title 
plt.title('IPL..!') 

# function to show the plot 
plt.show() 
