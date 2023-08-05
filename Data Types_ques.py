#!/usr/bin/env python
# coding: utf-8

# # Assessment - 2 Gradable
# 
# - Each question carries 3 marks
# - Marks will be assigned in terms of:
#     
#     **1. Expected output**
#     
#     **2. Quality and Explainability of code**
# 
#     ***Go back through the script and type a comment above each line explaining in English what it does.***
# 
#     **3. Copied code, if found, will result in 0 marks for that question. To avoid this make as much comments in the code to explain the approach**

# ### 1.
# 
# Write a Python program to perform following tasks on a list
# 
# <ol>
#     <li>Create an empty list with name l1</li>
#     <li>Add atleast 5 number to the l1</li>
#     <li>Add 100 at 2<sup>nd</sup> position</li>
#     <li>Add 1000 at front of the l1</li>
#     <li>Delete element at 3<sup>rd</sup> position</li>
#     <li>Display elements at even position</li>
#     <li>Display elements in reverse order</li>
# </ol>

# In[2]:


#(1.1)=Create an empty list with name l1.

# first we Declare List vaeiable

l1=[]       #l1 is list variable
print("Create empty list: ",l1)   # we print empty list


#(1.2)=Add atleast 5 number to the l1.

# we tack input for empty list from user
n = int(input("Enter the number of element you want to list :")) # show print msg

# create for loop for multiple inputs

for i in range(n):            # here this loop i (iteration) start with 0 by difault run upto nth value 
    element = int(input("Enter element :"))
    l1.append(element)        # add all input elements in list 
    
print(f"Take input {n} list element from user :",l1)  # print list

#(1.3)Add 100 at 2nd Position

l1.insert(1,100)     # here we use insert method for input value in particuler index 
print("After Add 100 at 2nd position :",l1)   #print massage and list

#(1.4)Add 1000 at front of l1

l1.insert(0,1000)    # here we use insert method for input value in particuler index 
print("Add 1000 at front position: ",l1)   #print massage and list

#(1.5)Delete element at 3rd position

l1.pop(2)  # here we use pop method for paticuler index deletion
print("After Delete 3rd position element:",l1)   #print massage and list

#(1.6)Display elements at even position

print("All even position element in list is : ")   # we show massage for user
list2=[]   # create another list for contain even position element 
for i in range(len(l1)):     
    if i%2==0:             # apply if condition for find even position list
       list2.append(l1[i])    # use append method for add element in to the list
       
print(list2)   # print list 
        
#(1.7) Display elements in reverse order

l1.reverse()         # we just use reverse() keyword 
print("After reverse the list:",l1)  #print the output


# ### 2. 
# 
# Grab ``StarAgile`` from the following Dictionaries
# 
# d_difficult = {'k1':[{'nest_key':['this is deep',['StarAgile']]}]}
# 
# d_irritating = {'k1':[1,2,{'k2':['this is not easy',{'VeryIrriating':[1,2,['StarAgile']]}]}]}

# In[27]:


#Grab ``StarAgile`` from the following Dictionaries

#here we can acces the value StarAgile in d_difficult

d_difficult = {'k1':[{'nest_key':['this is deep',['StarAgile']]}]}
print(d_difficult['k1'][0]['nest_key'][1][0])

#here we can acces the value StarAgile in d_irritating

'''
There Are Two way to print it.
first is use multiple variable...

d_irritating = {'k1':[1,2,{'k2':['this is not easy',{'VeryIrriating':[1,2,['StarAgile']]}]}]}
value1 =  d_irritating['k1']
print(value1)
value2 = value1[2]
print(value2)
value3 = value2['k2']
print(value3)
value4 = value3[1]
print(value4)
value5 = value4['VeryIrriating']
print(value5)
value6 = value5[2]
value7 = value6[0]
print(value7)'''

# Second is single veriable

print(d_irritating['k1'][2]['k2'][1]['VeryIrriating'][2][0])


# ### 3.
# 
# Write a program to accept a string from the user and display characters that are present at an even index number.
# 
# For example, str = "judgemental" so you should display ‘j’, ‘d’, ‘e’, ‘e’, ‘t’, ‘l’.

# In[5]:


#take String input from user

name = input("Enter name of String :")

# Create empty list for Storing the values
list1 = []

# use for loop for strorint multiple String Charecter in saprate index
for i in range(len(name)):     #we give a condition 
    name1 = name[i]
    
    if i%2==0:       # here we use if statement for find even index values
        list1.append(name1)    # add all even index value in list
    
print("List is :",list1)   # print list and massage
   


# ### 4. 
# 
# Convert the Float Value of '3.8' into Integer, Complex, Binary and Hexidecimal format

# In[8]:


value1 = 3.8

# we use type cast method for converting values
#1.convert float into intiger 
int_1 = int(value1)
print("After convert float into intiger number value is = ",int_1)

#2.convert float into complex
complex_1 = complex(value1)
print("After convert float into complex number value is  = ",complex_1)

#3. convert float into binary


# ### 5. 
# 
# Write a program to accept five names from the user and store it in a Tuple 'T1'

# In[7]:


# 5 Accept five name from user and store it in Tuple 'T1'

T1=[]      #create empty List
n=int(input('enter number of elements:'))    #take length of list from user
print("Enter Name :")    #give msg for user

for i in range(n):    # use for loop for storing multiple values in list
    T1.append(input())  #use append method for add String elements in list

T1 = tuple(T1) #convert list into Tuple 

print(f"Tuple of {n} given Name is :") # print the tuple
print(T1)


# In[ ]:




