# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:24:12 2023

@author: Annabel

"""

# the following liberies are requird: numpy, matplotlib, mpl_toolkits (Basemap)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#################### Warning ###########################
"""
before you start, you need to do the actuall analysis using the HYSPLIT GUI and/or extentions like PySplit
HYSPLIT https://www.ready.noaa.gov/HYSPLIT.php (do not use the web interface, the GUI has to be installed)
Pysplit https://github.com/mscross/pysplit can be used to run HYSPLIT over several years/months/hours
please follow the instructions in the readme to perform cluster analysis, then return here

"""



# load cluster list, depending on how many clusters you defined in the GUI this file will
# be called "CLUSLIST_X", where X is number of clusters
filename = r'C:\hysplit\cluster\working\CLUSLIST_3' 


list_traj_in_cluster = np.loadtxt(filename, usecols=7, dtype=str)# get list of clusters and their filepaths
clust_number=np.loadtxt(filename, usecols=0, dtype=str)# get cluster each file is associated with

# the cluster analysis in HYSPLIT uses the clipped trajectories, 
# but here we need the initial trajectory files containing the meteorological variables, 
# so we'll just delete that part of the filepath
list_traj_in_cluster = list(map(lambda st: str.replace(st, 'clippedtraj/', ''), list_traj_in_cluster))
list_traj_in_cluster = list(map(lambda st: str.replace(st, 'CLIPPED', ''), list_traj_in_cluster))


assigned_clust= np.array([clust_number, list_traj_in_cluster])# assign these trajectory files to the cluster numbers
assigned_clust=assigned_clust.T 

""" 
Now, we'll extract 1 meteo varible from all trajectories in a certain cluster and calcluate the mean.
To do so, you need to chose one of the following meteo variable names and replace the "SPCHUMID" in usecols=SPCHUMID. 
For cluster 1 this is in line 70 of this file:"meteo_traj = [np.loadtxt(f,skiprows=11,usecols=SPCHUMID, dtype=float) for f in filename]"
Don't forget to do the same for each cluster.

"""
PRESSURE = 12 # pressure
THETA    = 13 # potential temperature
AIR_TEMP = 14 # air temperature
RAINFALL = 15 # precipation
MIXDEPTH = 16 # mixing depth
RELHUMID = 17 # relative humidity
SPCHUMID = 18 # specific humidity
H2OMIXRA = 19 # water vapor mixing ratio
TERR_MSL = 20 # terrain height
SUN_FLUX = 21 # solar radiance


#########################################################
#### cluster mean for cluster 1 ####

# get the file names of cluster 1
mask = (assigned_clust[:,0].astype(np.float) != 0)
cluster_individual=np.delete(assigned_clust, mask, axis=0)
filename = cluster_individual[:,1]


# load all text files associated with cluster 1 and safe data into workspace
meteo_traj = [np.loadtxt(f,skiprows=11,usecols=SPCHUMID, dtype=float) for f in filename]

meteo_traj_data=np.ones((np.max([len(ps) for ps in meteo_traj]),len(meteo_traj)))*np.nan # define empty array
for i,c in enumerate(meteo_traj):  # fill columns
    meteo_traj_data[:len(c),i]=c

# calculate the mean of all trajectoires in cluster 1 
mean_proxy1=np.nanmean(meteo_traj_data, axis=1)

""" 
Repeat this step for more cluster. This example is for 3 clusters, thus 2 more clusters loaded below 

"""
#########################################################
#### cluster mean for cluster 2 ####

# get the file names of cluster 2
mask = (assigned_clust[:,0].astype(np.float) != 1)
cluster_individual=np.delete(assigned_clust, mask, axis=0)
filename = cluster_individual[:,1]

# load all text files associated with cluster 2 and safe data into workspace
meteo_traj = [np.loadtxt(f,skiprows=11,usecols=SPCHUMID, dtype=float) for f in filename]

meteo_traj_data=np.ones((np.max([len(ps) for ps in meteo_traj]),len(meteo_traj)))*np.nan # define empty array
for i,c in enumerate(meteo_traj):  # fill columns
    meteo_traj_data[:len(c),i]=c

#calculate the mean of all trajectoires in cluster 2 
mean_proxy2=np.nanmean(meteo_traj_data, axis=1)


#### cluster mean for cluster 3 ####

# get the file names of cluster 3
mask = (assigned_clust[:,0].astype(np.float) != 2)
cluster_individual=np.delete(assigned_clust, mask, axis=0)
filename = cluster_individual[:,1]

# load all text files associated with cluster 3 and safe data into workspace
meteo_traj = [np.loadtxt(f,skiprows=11,usecols=SPCHUMID, dtype=float) for f in filename]

meteo_traj_data=np.ones((np.max([len(ps) for ps in meteo_traj]),len(meteo_traj)))*np.nan # define empty array
for i,c in enumerate(meteo_traj):  # fill columns
    meteo_traj_data[:len(c),i]=c

#calculate the mean of all trajectoires in cluster 3 
mean_proxy3=np.nanmean(meteo_traj_data, axis=1)

###########################################################
#### load trajectory coordinates from the HYSPLIT cluster working directory

filename = r'C:\hysplit\cluster\working\C1_3mean.tdump'
cluster_coordinates1 = np.loadtxt(filename,skiprows=5,usecols=range(9,11), dtype=float)

filename = r'C:\hysplit\cluster\working\C2_3mean.tdump'
cluster_coordinates2 = np.loadtxt(filename,skiprows=5,usecols=range(9,11), dtype=float)

filename = r'C:\hysplit\cluster\working\C3_3mean.tdump'
cluster_coordinates3 = np.loadtxt(filename,skiprows=5,usecols=range(9,11), dtype=float)


##########################################################

""" 
Plot the 3 clusters using Basemap. This is just an example for clusters in Mexico,
you need to chnage the coordinates if you want to plot a different area. E.g. for Asia use:
map = Basemap(projection='cyl',llcrnrlon=40.,llcrnrlat=-10.,urcrnrlon=140.,
              urcrnrlat=50.,resolution='c') # projection, lat/lon extents and resolution of polygons to draw

"""
    
fig = plt.figure(figsize=(11.93,15.98))

map = Basemap(projection='cyl',llcrnrlon=-140.,llcrnrlat=-10.,urcrnrlon=-40.,
              urcrnrlat=50.,resolution='c') # projection, lat/lon extents and resolution of polygons to draw

parallels = np.arange(0,70,20) # make latitude lines ever 20 degrees from 0-70N
meridians = np.arange(0,360,40) # make longitude lines every 40 degrees from 0 to 360
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
map.drawmeridians(meridians,labels=[1,0,0,1],fontsize=10)
map.fillcontinents()
map.drawcoastlines()


i, j = map(cluster_coordinates1[0:len(mean_proxy1),1], cluster_coordinates1[0:len(mean_proxy1),0])  # transform coordinates
map.scatter(i, j, c=mean_proxy1,s=40,cmap=plt.cm.get_cmap('BrBG', 8),edgecolors=None,zorder=14) #,alpha=0.5,zorder=10

i, j = map(cluster_coordinates2[0:len(mean_proxy2),1], cluster_coordinates2[0:len(mean_proxy2),0])  # transform coordinates
map.scatter(i, j, c=mean_proxy2,s=40,cmap=plt.cm.get_cmap('BrBG', 8),edgecolors=None,zorder=14) #,alpha=0.5,zorder=10

i, j = map(cluster_coordinates3[0:len(mean_proxy3),1], cluster_coordinates3[0:len(mean_proxy3),0])  # transform coordinates
map.scatter(i, j, c=mean_proxy3,s=40,cmap=plt.cm.get_cmap('BrBG', 8),edgecolors=None,zorder=14) #,alpha=0.5,zorder=10

"""
Repeat or delete i, j = map(cluster_coordinates3[:,1], cluster_coordinates3[:,0])  # transform coordinates
map.scatter(i, j, c=mean_proxy3,s=40,cmap=plt.cm.get_cmap('BrBG', 8),edgecolors=None,zorder=14) #,alpha=0.5,zorder=10
depending on how many clusters you have
"""

p=plt.colorbar(orientation="horizontal");
p.set_label('Change in " name of meteo variable" along cluster means')
# safe figure 
plt.savefig(r'C:\Figures\Name_of_File.pdf')

#################################### end ###############################################
