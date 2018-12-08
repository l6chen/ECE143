#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from matplotlib import font_manager as fm
import matplotlib.pyplot as plt
#read data from datasets
def getdata(fname):
    """this function will read data from the datasets and extract the 
    information we need to create pie chart of race distribution"""
    assert isinstance(fname,str)
    assert len(fname)>0
    ALL=pd.read_csv(fname)      
    data=pd.DataFrame({'stop_id':ALL['stop_id'],'subject_race':ALL['subject_race'],'timestamp':ALL['timestamp'],'arrested':ALL['arrested']});
    race=list(data['subject_race'])
    race=list(set(race))                        #get all the races
    arrest=data[(data['arrested']=='Y')]
    race_arrestdata=list(arrest['subject_race'])
    race_num=[]                                 #this is the arrested population of each race
    for i in race:
        race_num.append(race_arrestdata.count(i))
    racenum_arrest=dict(zip(race,race_num))
    arrest_pie=racenum_arrest.copy()
    del arrest_pie[race[0]]
    del arrest_pie['X']

    i=0;
    for k in arrest_pie.copy():
        if arrest_pie[k]<50:
            i=i+arrest_pie[k];
            del arrest_pie[k];
    arrest_pie['other']=i                     # here we get the data we need to creat a pie chart of race distribution
    labels=['BLACK','WHITE','HISPANIC','OTHER']
    sizes=[]
    for i in labels:
        if i!='OTHER':
            sizes.append(arrest_pie[i[0]])
    sizes.append(arrest_pie['other'])                    
    return labels,sizes
def plot(labels,sizes):
    """this function will plot the pie chart of race distribution
    of arrested subjects
    """
    """input:
            labels: races
            sizes: population of races
    """
    assert isinstance(labels,list)
    assert isinstance(sizes,list)
    for p in sizes:
        assert p>=0
    plt.figure(figsize=(20,25))
    patches,l_text,p_text=plt.pie(sizes, labels=labels, 
        autopct='%1.1f%%', shadow=False, startangle=90)
    proptease = fm.FontProperties()
    proptease.set_size('xx-large')
    # font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
    plt.setp(l_text, fontproperties=proptease)
    plt.setp(p_text, fontproperties=proptease)

    plt.axis('equal')
    plt.legend(fontsize=20,loc=1)
    plt.title("race distribution in arrested subjects",fontsize=20)
    
    
def demog():
    """this function is to plot the pie chart of race demographics of San Diego in 2017"""
    Labels=['BLACK','WHITE','HISPANIC','OTHER']
    sizes=[5.5,45.5,33.9,15.1]
    plt.figure(figsize=(20,25))
    patches,l_text,p_text=plt.pie(sizes, labels=Labels, 
    autopct='%1.1f%%', shadow=False, startangle=90)
    proptease = fm.FontProperties()
    proptease.set_size('xx-large')
    # font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
    plt.setp(l_text, fontproperties=proptease)
    plt.setp(p_text, fontproperties=proptease)

    plt.axis('equal')
    plt.legend(fontsize=20,loc=1)
    plt.title("race distribution in San Diego 2017",fontsize=20)
# In[5]:


# In[ ]:




