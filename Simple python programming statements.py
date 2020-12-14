#!/usr/bin/env python
# coding: utf-8

# # Simple Python Programming Statements

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[1]:


out=[]
for i in range (2000,3201):
    if (i % 7) and (i % 5 != 0):
        out.append(i)
print(out)


# Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[2]:


fname=input("First Name")
lname=input("Last Name")
print("{firstname} {lastname}".format(firstname=lname,lastname=fname))


# Write a Python program to find the volume of a sphere with diameter 12 cm. Formula: V=4/3 * π * r^3

# In[3]:


diameter=12
r=diameter/2
pi=3.143
vol=4/3 * pi * pow(r,3)
print("Volume of Sphere when diameter is {} = {}".format(diameter,vol))

