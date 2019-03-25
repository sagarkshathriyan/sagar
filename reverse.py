#to reverse the name
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
s = str(input("Enter the name"))
  
print ("The original name is : ",end="") 
print (s) 
print ("The reversed name is : ",end="") 
print (reverse(s)) 