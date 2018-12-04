#!/usr/bin/env python
# coding: utf-8

# In[82]:


import pandas as pd
from matplotlib import font_manager as fm
get_ipython().run_line_magic('pylab', '')
ALL=pd.read_csv('vehicle_stops_2016_datasd.csv')
data=pd.DataFrame({'stop_id':ALL['stop_id'],'subject_race':ALL['subject_race'],'timestamp':ALL['timestamp'],'arrested':ALL['arrested']});
race=list(data['subject_race'])
race=list(set(race))
arrest=data[(data['arrested']=='Y')]
race_arrestdata=list(arrest['subject_race'])
race_num=[]
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
arrest_pie['other']=i
labels=['HISPANIC','WHITE','BLACK','OTHER']
sizes=list(arrest_pie.values())
plt.figure(figsize=(20,25))
patches,l_text,p_text=plt.pie(sizes, labels=labels, 
        autopct='%1.1f%%', shadow=False, startangle=90)
proptease = fm.FontProperties()
proptease.set_size('xx-large')
# font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
plt.setp(l_text, fontproperties=proptease)
plt.setp(p_text, fontproperties=proptease)

plt.axis('equal')
plt.show()
plt.legend(fontsize=20,loc=1)
plt.title("race distribution in arrested subjects",fontsize=20)


# In[83]:


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
name_list=['VIETNAMESE','ASIAN INDIAN','CAMBODIAN','HISPANIC','INDIAN','KOREAN','JAPANESE','HAWAIIAN','PACIFIC ISLANDER','WHITE','FILIPINO','OTHER ASIAN','OTHER','CHINESE','LAOTIAN','GUAMANIAN','BLACK','SAMOAN']


#calculate the percentage of arrested in each race
race_perc_uarre=[(race_pop[i]-list(arrest_bar.values())[i])*100/race_pop[i] for i in range(0,len(race_pop))]
race_perc_arre=[list(arrest_bar.values())[i]*100/race_pop[i] for i in range(0,len(race_pop))]



idx = np.arange(len(name_list))
plt.figure(figsize=(100,120))
plt.bar(idx,race_perc_uarre,label='not arrested',fc='g')
plt.bar(idx,race_perc_arre,bottom=race_perc_uarre,label='arrested',fc='r')

plt.xticks(idx,name_list,rotation=40)
plt.ylim(0,120)


plt.legend(loc=1,fontsize=20)
plt.xlabel('race',fontsize=17)
plt.ylabel('percentage of population/%',fontsize=17)
plt.title("percentage of arrested in each race",fontsize=20)


# In[ ]:





# In[ ]:




