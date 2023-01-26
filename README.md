# EasHyClustering
Use Python to plot meteorological data from HYSPLIT clustering

## Setup
This is a very simple code to help you plot cluster trajectories made in HYSPLIT **_with_ meteorological information**. Simply download 'EasHyClustering.py'.

You also need: 
- NumPy >= 1.19.1
- Matplotlib >= 3.2.2
- Basemap >= 1.2.1

## Before you start
The cluster analysis requires using the [HYSPLIT GUI](https://www.ready.noaa.gov/HYSPLIT.php) and/or extentions like [PySPLIT](https://github.com/mscross/pysplit). 


##### 1. Trajectory calculation:
First you need to calculate the trajectories for your location of choice, either using the HYSPLIT GUI or PySPLIT. 
Examples on how to do so can be found here:
[HYSPLIT](https://www.ready.noaa.gov/documents/Videos/Video/test_traj.mp4) and [PySPLIT](https://github.com/mscross/pysplit/blob/master/docs/examples/bulk_trajgen_example.py)

**It is crucial to export meteorological variables along the trajectory path in this step!!!
This is how to do it:
  click: Menu -> advanced -> Configuration setup -> Trajectory -> Add METEROLOGY output along the trajectory (6) (click on “menu”) 
  -> select the variable you want to output, I usually tick all of them -> safe -> safe (again, it’s important).** 



##### 2. Cluster analysis:
Once your trajectories are ready you can perform the cluster analysis. This can only be done in HYSPLIT, tutorials can be found here:
[HYSPLIT](https://www.ready.noaa.gov/documents/Videos/Video/traj_clus.mp4)
[PySplit](https://github.com/mscross/pysplit/blob/master/docs/examples/hysplit_clustering.py)


##### 3. Now open the 'EasHyClustering.py' and follow instructions in the file

## How to cite

Please cite DOI: 10.5281/zenodo.7574382 when using this code. _Other citations are required for the use of HYSPLIT and PySPLIT! Please read their requirements._
Many thanks to NOAA Air Research Laboratory for the HYSPLIT model.

This is program is free software and runs under MIT Licence.

## Further reading
[Wolf, A., Roberts, W.H.G., Ersek, V. et al. Rainwater isotopes in central Vietnam controlled by two oceanic moisture sources and rainout effects. Sci Rep 10, 16482 (2020). https://doi.org/10.1038/s41598-020-73508-z](https://www.nature.com/articles/s41598-020-73508-z)

Stein, A.F., Draxler, R.R, Rolph, G.D., Stunder, B.J.B., Cohen, M.D., and Ngan, F., (2015). NOAA's HYSPLIT atmospheric transport and dispersion modeling system, Bull. Amer. Meteor. Soc., 96, 2059-2077, http://dx.doi.org/10.1175/BAMS-D-14-00110.1

M. S. C. Warner, "Introduction to PySPLIT: A Python Toolkit for NOAA ARL’s HYSPLIT Model," in Computing in Science & Engineering, vol. 20, no. 5, pp. 47-62, Sep./Oct. 2018, doi: 10.1109/MCSE.2017.3301549.
