#!/usr/bin/env python
# coding: utf-8

# # Data Types
# - Write solution of each question in the cell given below the corresponsing question.

# #### 1. Write a program to take principal amount, rate and interest as input and calculate simple interest.

# In[7]:


amount = int(input('Enter the amount : '))                   #Enter the amount
rate = int(input('Enter the rate of interest : '))           #Enter the rate of interest
time = int(input('Enter the year for the interest : '))      #Enter the duration for the rate of interest

#Simple interest = principle amount * rate of interest * time interval  ----> Formula to calculate Simple interest

S = (amount*rate*time)/100                                   #----> Formula to calculate Simple interest

print('The simple interest = ', S)


# #### 2. Write a program that takes a string as input and prints the number of words in the string.

# In[2]:


x = str(input("Enter the command : "))                    # Enter the string to get counted
Count = 0;  
   
for i in range(0, len(x)-1):                              # Runs for loop from starting to last of string

    if(x[i] == ' ' and x[i+1].isalpha() and (i > 0)):     # Condition
        Count = Count + 1;   
Count = Count + 1;  
    
print("Total number of words in the given string: ",  str(Count))    #Displays the total number of words present in the given string 


# #### 3. Write a program to take a list of numbers as input (in a single line) and print the sum, avg, max and min elements.

# In[9]:


# 3. Write a program to take a list of numbers as input (in a single line) and print the sum, avg, max and min elements.


x = int(input("How many numbers you wanna add to list : " )) # take input length from user
l=[]   #define empty list here
sum1 = 0  # we define sum veriable

for i in range (x): #create for loop for take list value
  y = int(input("Enter element: "))
  l.append(y)
  sum1 = sum1+y    #we add list value and do sum inside for loop

avg = sum1/x    # do average for all list velue

max1 = l[0]    #we create veriable for find max and assine it value of 0th index
min1 = l[0]    #we create veriable for find min and assine it value of 0th index


for i in range(len(l)):   # use for loop for find max and min
   
     if max1<= l[i]:       #put if condition for find max 
        max1 = l[i]
     elif min1>=l[i]:       #put if condition for find max 
        min1 = l[i]
        
        
# we print all values sum,avg max,min 

print("list of element is:  ",l)
print("Sum of list element is:  ",sum1)
print("avg of list element is:  ",avg)
print("max element of the list is:  ",max1)
print("min element of the list is:  ",min1)



# #### 4. Write a program to take the marks of 3 students in five subjects each as a list (one list for each input) as input and print the average score of each student..

# In[4]:


# create empty dictionary
d = {}

# create for tack user input 
for i in range (3):
    key = input(f"Enter {i+1} student name:")

# create empty list
    l = [] 
# create sum veriable 
    sum=0
    
# create nested for tack user input   
    for j in range (5):
        val= int(input(f"Enter {j+1} subject marks :"))
        l.append(val)
        sum = val+sum

# find average to all list element
    avg = sum/5
    d[key] = avg

print("Student List is : ",d)  #print dictionary of Students


# #### 5. Write a program to take a list as input containing results of 10 coin tosses as 'H' or 'T'. Jon gets a point for each 'T' and Tom gets a point for each 'H'. print the points recieved by both.

# In[ ]:





# #### 6. Take two numbers as input and print the result after swapping them. (Without using multiple assignment and any extra variable).

# In[ ]:





# #### 7. Take a list as input in a single line containing 10 numbers as marks out of 100. The even positions in the list are marks of Tom and the odd positions are the marks of Jon. Calculate the average marks of both.

# In[1]:


# tack to empty list one for Tom and  one for Jon.
list1 = []
list2 = []

# tack user input
for i in range(10):
    val = int(input("enter number: "))
  
# put a condation for odd and even place
    if i%2 == 0:
        list1.append(val)
    else:
        list2.append(val)    

# print list of Tom and Jon
print("mark of Tom is:",list1)
print("mark of Jon is:",list2)


# #### 8. Take a string and a character as input. Print the result having the character between each word of the given string.

# In[3]:


# tack input String from user:

name = input("Enter String :")

# we create empty list
d = {}

# here we use for loop for assine value in dictionry
for i in range(len(name)):
    key = name[i]
    count=0      # we define a count veriable 
    for j in range(len(name)): # fere we use nested for loop to find repate carecters in given String
        key1 = name[j]
        if name[i]==key1:    # use if for check condition
            count+=1          # we increse count veriable 
    d[key] = count           # assine key and values 
       
    
   
# we print massage 

print("After we sort the string : ",d)   



# #### 9. Create a dictionary having three items. Key of each item is the name of a student, value associated with each key is a list of marks in five subjects. Given this dictionary print the average score of each student.

# In[ ]:





# #### 10. Take a string as input(may contain repetitive words), print a list consisting of unique words from the given string.

# In[6]:


list_1 = []
name = input("Enter String :")
for i in range(len(name)):
    value = name[i]
    list_1.append(value)
print("List we entered :",list_1)
temp_list = []

for i in list_1:
    if i not in temp_list:
        temp_list.append(i)
    list_1 = temp_list

print("after",list_1)


# In[ ]:




