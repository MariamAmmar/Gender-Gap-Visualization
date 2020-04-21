#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']

fig = plt.figure(figsize=(20, 20))

for sp in range(0,6):
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if sp == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif sp == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')
plt.show()


# In[5]:


get_ipython().magic('matplotlib inline')

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

fig = plt.figure(figsize = (16,20))


for sp in range (0,18,3):
    cat_index = int(sp/3)
    ax = fig.add_subplot (6,3,sp+1)
    ax.plot(women_degrees["Year"], women_degrees[stem_cats[cat_index]], c=cb_dark_blue, label = "Women", linewidth =3)
    ax.plot(women_degrees["Year"], 100-women_degrees[stem_cats[cat_index]], c=cb_orange, label = "Men", linewidth = 3)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(stem_cats[cat_index])
    ax.set_xlim(1968,2011)
    ax.set_ylim(0,100)
    ax.axhline(50, c=(171/255,171/255,171/255), alpha=0.3)

    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom = "off") 
    ax.set_yticks([0,100])
    
    if cat_index == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif cat_index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women') 
        ax.tick_params(labelbottom="on")


for sp in range (1,16,3):
    cat_index=int((sp-1)/3)
    ax = fig.add_subplot (6,3,sp+1)
    ax.plot(women_degrees["Year"],women_degrees[lib_arts_cats[cat_index]], c=cb_dark_blue, label = "Women", linewidth=3)
    ax.plot(women_degrees["Year"],100-women_degrees[lib_arts_cats[cat_index]], c=cb_orange,label = "Men", linewidth = 3)
    ax.set_title(lib_arts_cats[cat_index])
    ax.set_xlim(1968,2011)
    ax.set_ylim(0,100)
    ax.axhline(50, c=(171/255,171/255,171/255), alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(top = "off", right="off",left="off",bottom = "off", labelbottom = "off")
    ax.set_yticks([0,100])

    if cat_index == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
        
    elif cat_index == 4:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')
        ax.tick_params(labelbottom = "on")

for sp in range (2,20,3):
    cat_index = int((sp-2)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees["Year"],women_degrees[other_cats[cat_index]], c=cb_dark_blue, label="Women", linewidth = 3)
    ax.plot(women_degrees["Year"],100-women_degrees[other_cats[cat_index]], c=cb_orange, label="Women",linewidth = 3)
    ax.set_title(other_cats[cat_index])
    ax.set_xlim(1968,2011)
    ax.set_ylim(0,100)
    ax.axhline(50, c=(171/255,171/255,171/255), alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(top="off",bottom="off", left = "off", right = "off", labelbottom = "off")
    ax.set_yticks([0,100])

    if cat_index ==0:
        ax.text(2005,90,"Men")
        ax.text(2002,5,"Women")
        
    elif cat_index == 5:
        ax.text(2005,62,"Men")
        ax.text(2001,32,"Women")
        ax.tick_params(labelbottom = "on")

plt.savefig("gender_degrees.png")
plt.show()







