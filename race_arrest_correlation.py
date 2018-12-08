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
    labels=['HISPANIC','WHITE','BLACK','OTHER']
    sizes=list(arrest_pie.values())
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
    for i in sizes:
        assert i>=0
    plt.figure(figsize=(20,25))
    patches,l_text,p_text=plt.pie(rap.sizes, labels=labels, 
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
    labels=['HISPANIC','WHITE','BLACK','OTHER']
    sizes=[33.9,45.5,5.5,15.1]
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
    plt.title("race distribution in San Diego 2017",fontsize=20)
# In[5]:

"""
import numpy as np
race=list(data['subject_race'])
race=list(set(race))
arrest_bar=racenum_arrest.copy()
del arrest_bar[race[0]]
del arrest_bar['X']
race_ele=race
race_ele.remove(race_ele[0])
race_ele.remove('X')
#derive the population who were not arrested
race=list(data['subject_race'])
race_pop=[]
for i in race_ele:
    race_pop.append(race.count(i))
race_pop_uarre=[race_pop[i]-list(arrest_bar.values())[i] for i in range(0,len(race_pop))]
race_list=list(arrest_bar.keys());
name_list=['CHINESE','ASIAN INDIAN','BLACK','KOREAN','PACIFIC ISLANDER','VIETNAMESE','SAMOAN','INDIAN','OTHER ASIAN','OTHER','CAMBODIAN','GUAMANIAN','HISPANIC','WHITE','LAOTIAN','JAPANESE','FILIPINO','HAWAIIAN']


#calculate the percentage of arrested in each race
race_perc_uarre=[(race_pop[i]-list(arrest_bar.values())[i])*100/race_pop[i] for i in range(0,len(race_pop))]
race_perc_arre=[list(arrest_bar.values())[i]*100/race_pop[i] for i in range(0,len(race_pop))]



idx = np.arange(len(name_list))

"""
# In[ ]:




