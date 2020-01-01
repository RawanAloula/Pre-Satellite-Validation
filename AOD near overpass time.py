import pandas as pd 


# ------ Step 1 ------

# read the  original csv file you have 
File = pd.read_csv('/Users/Rawan/Desktop/File.csv')
File.head()
File.dtypes

# creat DataFrame format (to merge date and time)
file=pd.DataFrame(data=File)
file.head()
file.dtypes
file['DT']=pd.to_datetime(file['Date'] + ' ' + file['Time'])

# create a second file that takes the first file data and resample it so that you have hourly means
AVG=file.groupby([file["DT"].dt.year, file["DT"].dt.month,file["DT"].dt.day,file["DT"].dt.hour]).Observation.mean()
AVG.head()
AVG.dtypes

# save it as csv file to use it in Step 2
AVG.to_csv('/Users/Rawan/Desktop/AGVoutput.csv', sep='\t')


# ------ Step 2 ------

# filtering the hourly mean file (2ed file created and saved) 

# import the File 
File2=pd.read_csv('/Users/Rawan/Desktop/AGVoutput.csv')

# # creat a DataFrame format to be filtered and saved seperatly
AvgT=pd.DataFrame(data=File2)
AvgT.head()
AvgT.dtypes

# filter only by hour 10 , that means take all the measurments in this file are for 10 am 
T10=AvgT[AvgT.Hour==10]
T10.head()
T10.to_csv('/Users/Rawan/Desktop/AOD_T10.csv', sep='\t')

# take the avrage monthly and export
T10_2=pd.DataFrame()
T10_2=T10.groupby('Month').AOD.mean()
T10_2.to_csv('/Users/Rawan/Desktop/AOD_T10_2.csv', sep='\t')

