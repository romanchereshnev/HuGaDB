# HuGaDB
Database for human gait analysis consisting of continues recordings of combined activities, such as walking, running, taking stairs up and down, sitting down, and so on; and the data recorded are segmented and annotated.  Data were collected from a body sensor network consisting of six wearable inertial sensors (accelerometer and gyroscope) located on the right and left thighs, shins, and feet. Additionally, two EMG sensors were used on the quadriceps (front thigh) to measure muscle activity.

If you have trouble with downloading zip file you can download it from [Dropbox](https://www.dropbox.com/s/7nb9g650i5m9k6c/HuGaDB.zip?dl=0) or [Google Drive](https://drive.google.com/file/d/16Z4NYVo85-BcziIoBwgOCnHvUQ59F3Fo/view?pli=1) storages. 

## Data Collection

The participants were performed a combination of activities, and data were recorded continually.  For instance, a participant was instructed to perform the following activities: starting from a sitting position, sitting - standing up - walking - going up the stairs - walking - sitting down. The experimenter recorded the data using a laptop and annotated the data with the activities performed. This provided us a long, continuous sequence of segmented data annotated with activities. We developed our own data collector program. In total, 2,111,962 samples were collected from all the 18 participants, and they provided a total of 10 hours of data. Activities are dicribed in Table 1.

Table 1

|ID | Activity |Time (s) |Time (min) |Percent |Samples |Description|
|---|----------|---------|-----------|--------|--------|-----------|
|1|Walking |11544 |192 |32.15 |679073|Walking and turning at various speeds on a flat surface|
|2|Running |1218 |20 |3.39 |71653|Running at various paces|
|3|Going up |2237 |37 |6.23 |131604|Taking stairs up at various speeds|
|4|Going down |1982 |33 |5.52 |116637|Taking the stairs down at various speeds and steps|
|5|Sitting |4111 |68 |11.45 |241849| Sitting on a chair; sitting on the floor not included|
|6|Sitting down |409 |6 |1.14 |24112| Sitting on a chair; sitting down on the floor not included|
|7|Standing up |380 |6 |1.06 |22373| Standing up from a chair|
|8|Standing |5587 |93 |15.56 |328655|Static standing on a solid surface|
|9|Bicycling |2661 |44 |7.41 |156560 | Typical bicycling|
|10|Up by elevator |1515 |25 |4.22 |89144|Standing in an elevator while moving up|
|11|Down by elevator |1185 |19 |3.30 |69729|Standing in an elevator while moving down|
|12|Sitting in car |3069 |51 |8.55 |180573 |Sitting while an travelling by car as a passenger|
|Total | | 35903 |598 |100.00 |2111962| |


The data were collected from 18 participants. These participants were healthy young adults: 4 females and 14 males, average age of 23.67 (standard deviation [std]: 3.69) years, an average height of 179.06 (std: 9.85) cm, and an average weight of   73.44 (std: 16.67) kg.  Characteristics of participants are shown in Table 2. 



Table 2


|id		|weight (kg)	|height (cm)	|age	|sex (M=Male, F=Female)|
|-----|-------------|-------------|-----|----------------------|
|1 		|75 			    |177 			    |24 	|M                     |
|2 		|80 			    |183 			    |22 	|M                     |
|3 		|65 			    |183 			    |23 	|M                     |
|4 		|93 			    |189 			    |24 	|M                     |
|5 		|63 			    |183 			    |35 	|M                     |
|6 		|54 			    |168 			    |25 	|F                     |
|7 		|52 			    |161 			    |22 	|F                     |	
|8 		|80 			    |176 			    |23 	|M                     |
|9 		|65 			    |175 			    |24 	|F                     |
|10 	|118 			    |183 			    |27 	|M                     |
|11 	|85 			    |203 			    |24 	|M                     |
|12 	|85 			    |192 			    |23 	|M                     |
|13 	|64 			    |174 			    |18 	|M                     |
|14 	|68 			    |175 			    |19 	|M                     |
|15 	|72 			    |178 			    |23 	|M                     |
|16 	|48 			    |164 			    |26 	|F                     |
|17 	|85 			    |179 			    |25 	|M                     |
|18 	|70 			    |180 			    |19 	|M                     |


## Data format

The main data body of every file has 39 columns. Each column corresponds to a sensor, and one row corresponds to a sample. The order of the columns is fixed. The first 36 columns correspond to the inertial sensors, the next 2 columns correspond to the EMG sensors, and the last column contains the activity ID. Values of the gyroscopes and the accelerometers encoded by int_16 datatype. Values of the EMGs encoded by uint_8 datatype. The activities are coded as shown in Table 1. The inertial sensors are listed in the following order:  right foot (RF), right shin (RS), right thigh (RT), left foot (LT), left shin (LS), and left thigh (LT), followed by right EMG (R) and left EMG (L). Each inertial sensor produces three acceleration data on x,y,z axes and three gyroscope data on x,y,z axes. For instance, the column named 'RT_acc_z' contains data obtained from the z-axis of accelerometer located on the right thigh. 



Every file name was created according to the following template HGD_vX_ACT_PR_CNT.txt. Here is table with description of the file naming convention:


|TAG 	|Description 	      |Type	  |Comment                                      |
|-----|-------------------|-------|---------------------------------------------|
|HGD 	|Prefix 			      |fixed 	|  Data files start with this prefix          |
|vX 		|Version number 	|integer| Indicates the version of the data format    |
|ACT		|Activity 		    |string |	Indicates the type of activity              |
|PR 		|Participant ID 	|integer| Indicates the subject whos data was recorded|
|CNT		|Counter 		      |integer| Counter for repeated experiments	          |
		
For example, a file named HGD_v1_walking_17_02.txt, contains data from participant 17 while he was walking repeated for the second time.
Each file contains header. Here is table with description of the data file header:

|TAG 		    |Description 					          |Type				      |Comment                                |
|-----------|-------------------------------|-----------------|---------------------------------------|
|#Activity 	|List of the activities 			  |string 				  |  lists the activity names in this file  |
|#ActivityID |List of the ID of activities 	|list of integers |	lists the activity IDs in this file     |
|#Date-Time 	|Date and Time 					      |MM-DD-HR-MN 		  |Month-Day-Hour-Min format                |
## Sensor Network Topology
In data collection, a 3-axis accelerometer, a 3-axis gyroscope and electromyography (EMG) sensors were used. One 3-axis accelerometer and one 3-axis gyroscope were integrated into a single chip and referred to as inertial sensor. In total, three pairs of inertial sensors and one pair of EMG sensors were installed on the right and left legs with elastic bands. A pair of inertial sensors was installed on the rectus femoris muscle 5 centimetres above the knee, a pair of sensors around the middle of the shinbone at the level where the calf ends, and a pair on the feet on the metatarsal bones. The EMG sensors were placed on vastus lateralis. EMG was connected to three electrodes on the skin. Between the two electrodes was taken the electric potential. In total, 38 signals were collected, 36 from the inertial sensors and 2 from the EMG sensors. 

Data were collected with next sensors setting:
* Range of the gyroscopes from -2000 to 2000 deg/sec.
* Range of the accelerometers from -2g to 2g. Where g is gravity acceleration

# HuGaDB scripts

* loadDataFromFile.m - contains Matlab function for downloading data from HuGaDB text file
* load_HuGaDB_file.py - contains Python function for downloading data from HuGaDB text file
* create_db.py - Python script that creates SQLite database from HuGaDB text files. 

SQLite database contains two tables 'files' and 'data'. 
'Files' table contains two columns: id, filename.
'Data' table contains 42 columns: id, file_id, timestamp and data features.
'File_id' contains id of file from which data were loaded. 

To use this script type:
python create_db.py path_to_HuGaDB_folder [dbname]

Parameter in square brackets indicating the database name is optional. Default: dbname=HuGaDB
