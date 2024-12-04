#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = input("Enter your name")
weight = int(input("Enter your weight"))
height = int(input("Enter your height"))
BMI = (weight * 703) / (height * height)
print(BMI)

if BMI >0:
    if(BMI <18.5):
        print(name +", you are under weight.")
    elif(BMI<=24.5):
        print(name +", you are normal weight.")
    elif(BMI<29.9):
        print(name +", you are over weight.you need to excercise more and stop sitting and writing so many python tutorial.")
    elif(BMI<34.9):
        print(name +", you are obese weight.")
    elif(BMI<39.9):
        print(name +", you are severly obese.")
    else:
        print(name +", you are morbidily obese.")
else:
    print("Enter valid input.") 


# In[ ]:





# In[ ]:





# In[ ]:




