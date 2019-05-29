
#import os
from clear_all import clear_all

from sub_preprocessing_S1_EW_mooring_A_1 import preprocessing_S1_EW
from sub_plot_on_map_gdal_mooring_A import sub_plot_on_map_gdal    
 

clear_all()

data_path = 'D:/Project_Data/Arctic_PRIZE/Data/S1/mooring_A/'
temp_path = 'D:/Project_Data/Arctic_PRIZE/Temp/'
out_path_hires = 'D:/Project_Data/Arctic_PRIZE/Processed_Data/S1/mooring_A/hires/'
out_path_lowres = 'D:/Project_Data/Arctic_PRIZE/Processed_Data/S1/mooring_A/lowres/'

polarization = 'HH'

lon_mooring = 18.3
lat_mooring = 81.0


text_file = open(data_path + "list_1.txt","r")
lines= text_file.readlines()
#print(lines)
#print(len(lines))

for list in lines:
    print(list[0:67])
    file1 = list[0:67]  
    preprocessing_S1_EW(file1,data_path,temp_path,out_path_hires,out_path_lowres,polarization)

    subset_file = file1 + polarization + "_terrian_40m_subset" 
    sub_plot_on_map_gdal(out_path_hires,subset_file,lon_mooring,lat_mooring)