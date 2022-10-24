#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("now we will talk about for loop")
print("A for Loop is used to repeat a specific block of code a known number of times")
print("for example if we want to take an input of a class consisting of 10 students then we will use the for loop to repeat the input 10 times")


# In[3]:


print("now we will talk about for loop")
print("A for Loop is used to repeat a specific block of code a known number of times")
print("for example if we want to take an input of a class consisting of 10 students then we will use the for loop to repeat the input 10 times")
print("we will learn how to implement for loop code")


# In[4]:


print("now we will talk about for loop")
print("A for Loop is used to repeat a specific block of code a known number of times")
print("for example if we want to take an input of a class consisting of 10 students then we will use the for loop to repeat the input 10 times")
print("we will learn how to implement for loop code")
print("first of all we should use the for() function")


# In[6]:


print("now we will talk about for loop")
print("A for Loop is used to repeat a specific block of code a known number of times")
print("for example if we want to take an input of a class consisting of 10 students then we will use the for loop to repeat the input 10 times")
print("we will learn how to implement for loop code")
print("first of all we should use the for() function")
print("then we will make the condition that repeats the code 10 times by declaring a variable for example i")
print("we will give the variable any value then we will make the condition that we will end the loop for example if i = 0 this will be the first implementation of the code. if we want to repeat the code 9 times more than we will make the condition that the loop stops at i<=9 and we will make sure that i increases by 1 every single loop using i++")


# In[33]:


print("now we will talk about for loop")
print("A for Loop is used to repeat a specific block of code a known number of times")
print("for example if we want to take an input of a class consisting of 10 students then we will use the for loop to repeat the input 10 times")
print("we will learn how to implement for loop code")
print("first of all we should use the for() function")
print("then we will make the condition that repeats the code 10 times by declaring a variable for example i we will let it in a range (10)")
print("here the code will be repeated 10 times where it starts from 0 and ends in 9")
print("here is how the code should look:")
print("for i in range(10):")
print("   input your gpa")
for i in range(10):
    input("enter your gpa ")
print("note if we add just n number in the range (range(n)) by default the range starts from 0 to n-1 ")
print("for example this code for i in range(3):")
print("  print(i)")
print("the output will be 0 1 2")
for i in range(3):
    print(i)
print("if you want to make a change in range default you will make changes in the function")
print("for example if you want to start from n till 10 instead of starting from 0 you will let the range(n,10) ")
for i in range(5, 10):
    print(i)
print("note that that the range() increment by 1 as a default if you want to change the incrementation we will add the incrementation sequence to the range for example if we want to print the the even numbers from 0 to 20 the range should be (0,20,2)")
for i in range(0, 20, 2):
    print(i)
print("if we want to stop the loop at a specific point we will write the condition that we will stop at and use break")
print("for example if we want to list the number from 1 to 10 but we want the loop to stop before 5 then we will type the following code")
print("for i in range(1,10)")
print("if i == 5 (the condition)  break (to stop the loop)")
print("  print(i) (here the output will be 1 2 3 4 )")
for i in range (1, 10):
    if i==5: break
    print(i)
print("but here the code stopped at 5 and ignored the rest of the number what if we want the loop to ignore 5 and list the rest of the numbers here we will use continue instead of break")
for i in range (1, 10):
    if i==5: 
     continue
    print(i)
print("may be we want to output a message for the user after the end of the loop here we use else statement after the loop and print our message ")
print("here how the code looks ")
print("for i in range(1,5):")
print("print(i)") 
print("else:")
print("thank you")

for i in range(1,5):
    print(i)
else:
        print("thank you")


# ##### 

# In[ ]:




