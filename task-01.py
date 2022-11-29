#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle
t= turtle.Turtle ()
def circle(angle):
        t.forward(100 )
        t.right(angle )
        t.forward(3 )
        t.right(angle )
        t.forward(100 )
        t.right(angle+1)
for i in range(90):
    circle(90)

