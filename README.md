# If you have trouble with downloading zip file you can download it from Dropbox ([Version 1](https://www.dropbox.com/s/7nb9g650i5m9k6c/HuGaDB.zip?dl=0), [Version 2](https://www.dropbox.com/s/406z5oqjlr6fcy9/HuGaDB%20v2.zip?dl=0)) or Google Drive ([Version 1](https://drive.google.com/file/d/16Z4NYVo85-BcziIoBwgOCnHvUQ59F3Fo/view?pli=1), [Version 2](https://drive.google.com/open?id=15zLaP5V3ltR6qro98u492eqFBSeSO-0m)) storages. 

# Relabeled dataset

The second version of the dataset contains more precisely labeled labels. The data has been re-labeled for the following activities: sitting, standing, sitting down, standing up. 

# HuGaDB
Database for human gait analysis consisting of continues recordings of combined activities, such as walking, running, taking stairs up and down, sitting down, and so on; and the data recorded are segmented and annotated.  Data were collected from a body sensor network consisting of six wearable inertial sensors (accelerometer and gyroscope) located on the right and left thighs, shins, and feet. Additionally, two EMG sensors were used on the quadriceps (front thigh) to measure muscle activity.



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

## Sensors location

<p align="center">
     <img src=https://github.com/romanchereshnev/HuGaDB/blob/master/images/Location-of-Sensors.png?raw=true" width="500" alt="no image">
</p>
	

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

## Corrupted gyroscope data

Due to gyroscope issues, some data from gyroscopes has been corrupted. Some gyroscope data was amplified 10 times which led to clipping (see image below). 

<details><summary>Open image</summary>
<p align="center">
     <img src=https://github.com/romanchereshnev/HuGaDB/blob/master/images/corrupted_example.png?raw=true" width="700" alt="no image">
</p>
	
</p>
</details>

Here is a table with a list of files with various activities which contain incorrect data.

<details><summary>Corrupted gyroscope data in files with various activities</summary>
<p>

|File| Right foot | Left foot | Right shank | Left shank | Right thigh | Left thigh |
|----|------------|-----------|------------|-----------|-------------|------------|
|HuGaDB_v1_various_03_00.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_01.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_02.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_03.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_04.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_05.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_06.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_07.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_08.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_09.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_10.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_11.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_12.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_13.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_14.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_15.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_16.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_17.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_18.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_19.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_20.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_21.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_22.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_23.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|		
|HuGaDB_v1_various_03_24.txt | 	Corrupted		|	OK		| 	Corrupted		|	OK		| 	Corrupted		|	OK		|
| HuGaDB_v1_various_04_00.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_01.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_02.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_03.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_04.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_05.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_06.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_07.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_08.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_09.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_10.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_11.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_12.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_13.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_14.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_15.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_16.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_17.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_18.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 	
| HuGaDB_v1_various_04_19.txt | 	Corrupted | 	Corrupted| 	Corrupted| 	Corrupted | 	Corrupted| 	Corrupted| 
|HuGaDB_v1_various_05_00.txt | 	Corrupted  	   |     OK	        | 	Corrupted  	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_01.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_02.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_03.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_04.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_05.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_06.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_07.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_08.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_09.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_10.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_11.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_12.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_13.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_14.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_15.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_16.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_17.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_18.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_19.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
|HuGaDB_v1_various_05_20.txt | 	Corrupted	   | 	Corrupted	| 	Corrupted	|	OK	|	OK	|	OK	|
| HuGaDB_v1_various_07_00.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      |	
| HuGaDB_v1_various_07_01.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_02.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_03.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_04.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_05.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_06.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_07.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_08.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_09.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_10.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_11.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_12.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_13.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_14.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_15.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_16.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_17.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_18.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_19.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_20.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_21.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_22.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_23.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      | 	
| HuGaDB_v1_various_07_24.txt | Corrupted  | OK        | Corrupted  | OK        |    OK       |    OK      |
| HuGaDB_v1_various_09_00.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted  |	
| HuGaDB_v1_various_09_01.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted  |	
| HuGaDB_v1_various_09_02.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted  |	
| HuGaDB_v1_various_09_03.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted  |	
| HuGaDB_v1_various_09_04.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted  |	
| HuGaDB_v1_various_09_05.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted  |	
| HuGaDB_v1_various_09_06.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted  |	
| HuGaDB_v1_various_09_07.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted  |	
| HuGaDB_v1_various_09_08.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted  |	
| HuGaDB_v1_various_09_13.txt | 	OK |	Corrupted |	OK | Corrupted |	OK |	Corrupted  |
| HuGaDB_v1_various_09_14.txt | 	OK |	Corrupted |	OK | Corrupted |	OK |	Corrupted  |
| HuGaDB_v1_various_09_15.txt | 	OK |	Corrupted |	OK | Corrupted |	OK |	Corrupted  |
| HuGaDB_v1_various_09_16.txt | 	OK |	Corrupted |	OK | Corrupted |	OK |	Corrupted  |
| HuGaDB_v1_various_09_17.txt | 	OK |	Corrupted |	OK | Corrupted |	OK |	Corrupted  |
| HuGaDB_v1_various_09_18.txt | 	OK |	Corrupted |	OK | Corrupted |	OK |	Corrupted  |
| HuGaDB_v1_various_09_19.txt | 	OK |	Corrupted |	OK | Corrupted |	OK |	Corrupted  |
| HuGaDB_v1_various_09_20.txt | 	OK |	Corrupted |	OK | Corrupted |	OK |	Corrupted  |
| HuGaDB_v1_various_11_04.txt | 	OK |	Corrupted	| OK | 	OK |	OK	| OK | 	
| HuGaDB_v1_various_11_05.txt | 	OK |	Corrupted	| OK | 	OK |	OK	| OK | 	
| HuGaDB_v1_various_11_06.txt | 	OK |	Corrupted	| OK | 	OK |	OK	| OK | 	
| HuGaDB_v1_various_11_07.txt | 	OK |	Corrupted	| OK | 	OK |	OK	| OK | 	
| HuGaDB_v1_various_11_08.txt | 	OK |	Corrupted	| OK | 	OK |	OK	| OK | 	
| HuGaDB_v1_various_11_09.txt | 	OK |	Corrupted	| OK | 	OK |	OK	| OK | 	
| HuGaDB_v1_various_11_10.txt | 	OK |	Corrupted	| OK | 	OK |	OK	| OK | 	
| HuGaDB_v1_various_11_11.txt | 	OK |	Corrupted	| OK | 	OK |	OK	| OK | 	
| HuGaDB_v1_various_11_12.txt |  	OK |	Corrupted	| OK | 	OK |	OK	| OK |	
| HuGaDB_v1_various_11_13.txt |  	OK |	Corrupted	| OK | 	OK |	OK	| OK |	
| HuGaDB_v1_various_11_14.txt |  	OK |	Corrupted	| OK | 	OK |	OK	| OK |	
| HuGaDB_v1_various_11_15.txt |  	OK |	Corrupted	| OK | 	OK |	OK	| OK |	
| HuGaDB_v1_various_11_16.txt |  	OK |	Corrupted	| OK | 	OK |	OK	| OK |	
| HuGaDB_v1_various_11_17.txt |  	OK |	Corrupted	| OK | 	OK |	OK	| OK |	
| HuGaDB_v1_various_11_18.txt |  	OK |	Corrupted	| OK | 	OK |	OK	| OK |	
| HuGaDB_v1_various_11_19.txt |  	OK |	Corrupted	| OK | 	OK |	OK	| OK |	
| HuGaDB_v1_various_11_20.txt | 	OK |	Corrupted	| OK | 	OK |	OK	| OK |
| HuGaDB_v1_various_12_00.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_01.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_02.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_03.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_04.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_05.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_06.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_07.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_08.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_09.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_11.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_10.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_12.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_13.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_14.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_15.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_16.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_17.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_12_18.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |	
| HuGaDB_v1_various_13_07.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_08.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_09.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_11.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_10.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_12.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_13.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_14.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_15.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_16.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_17.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_18.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_19.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_20.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_21.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_22.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_23.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_13_24.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_00.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_01.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_02.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_03.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_04.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_05.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_06.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_07.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_08.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_09.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_11.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_10.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_12.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_13.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_14.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_15.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_16.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_17.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_18.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_19.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_20.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_14_21.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_15_00.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_15_01.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_15_02.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_15_03.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_15_04.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_15_05.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_15_06.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_15_07.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_15_08.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_15_09.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_15_11.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_00.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_01.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_02.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_03.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_04.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_05.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_06.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_07.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_08.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_09.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_11.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_10.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_12.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_13.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_14.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_15.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_16.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_17.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_18.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_16_19.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_00.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_01.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_02.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_04.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_05.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_06.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_07.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_08.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_09.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_10.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_11.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_12.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_13.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_14.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_15.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_16.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_17.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_18.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_19.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_20.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_21.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_22.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |		
| HuGaDB_v1_various_17_23.txt | 	Corrupted |	Corrupted |	Corrupted | Corrupted |	Corrupted |	Corrupted |
| HuGaDB_v1_various_18_00.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_01.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_02.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_03.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_04.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_05.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_06.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_07.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_08.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_09.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_11.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_10.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_12.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_13.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_14.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_15.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |	
| HuGaDB_v1_various_18_16.txt | 	Corrupted	| Corrupted	| 	Corrupted	| Corrupted	| OK | Corrupted |
| HuGaDB_v1_running_03_00.txt | Corrupted    |    OK     | Corrupted   |    OK     | Corrupted     |   OK      |   
| HuGaDB_v1_running_03_01.txt | Corrupted    |    OK     | Corrupted   |    OK     | Corrupted     |   OK      |
| HuGaDB_v1_running_07_00.txt | Corrupted    |    OK     | Corrupted   |    OK     |     OK        |   OK      |
| HuGaDB_v1_running_07_01.txt | Corrupted    |    OK     | Corrupted   |    OK     |     OK        |   OK      |
| HuGaDB_v1_running_07_02.txt | Corrupted    |    OK     | Corrupted   |    OK     |     OK        |   OK      |
| HuGaDB_v1_running_09_00.txt |    OK        | Corrupted |      OK     | Corrupted |     OK        | Corrupted |
| HuGaDB_v1_running_09_01.txt |    OK        | Corrupted |      OK     | Corrupted |     OK        | Corrupted |
| HuGaDB_v1_running_09_02.txt |    OK        | Corrupted |      OK     | Corrupted |     OK        | Corrupted |
| HuGaDB_v1_sitting_03_00.txt | Corrupted   |    OK     |    OK     |     OK        | Corrupted   |    OK        |
| HuGaDB_v1_sitting_03_01.txt | Corrupted   |    OK     | Corrupted |     OK        | Corrupted   |    OK        |
| HuGaDB_v1_sitting_03_02.txt | Corrupted   |    OK     | Corrupted |     OK        | Corrupted   |    OK        |
| HuGaDB_v1_sitting_03_03.txt | Corrupted   |    OK     | Corrupted |     OK        | Corrupted   |    OK        |
| HuGaDB_v1_sitting_04_00.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_04_01.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_04_02.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_05_00.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_05_01.txt |   OK        | Corrupted |           |     OK        |    OK       |    OK        |
| HuGaDB_v1_sitting_06_04.txt | Corrupted   |    OK     | Corrupted |     OK        |    OK       | Corrupted    |
| HuGaDB_v1_sitting_07_01.txt | Corrupted   |    OK     | Corrupted |     OK        |    OK       |    OK        |
| HuGaDB_v1_sitting_07_02.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_07_03.txt | Corrupted   |     OK    | Corrupted |     OK        |    OK       |    OK        |
| HuGaDB_v1_sitting_07_04.txt | Corrupted   |     OK    | Corrupted |     OK        |    OK       |    OK        |
| HuGaDB_v1_sitting_08_00.txt | Corrupted   | Corrupted | Corrupted |  Corrupted    | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_09_00.txt | Corrupted   | Corrupted | Corrupted |  Corrupted    | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_09_01.txt | Corrupted   | Corrupted | Corrupted |  Corrupted    | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_09_02.txt | Corrupted   | Corrupted | Corrupted |  Corrupted    | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_09_03.txt | Corrupted   | Corrupted | Corrupted |  Corrupted    | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_10_00.txt | Corrupted   | Corrupted | Corrupted |  Corrupted    | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_10_04.txt | Corrupted   | Corrupted | Corrupted |  Corrupted    | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_11_00.txt |    OK       | Corrupted |    OK     |     OK        |    OK       |    OK        |
| HuGaDB_v1_sitting_11_01.txt |    OK       | Corrupted |    OK     | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_11_02.txt |    OK       | Corrupted |    OK     |     OK        |    OK       |    OK        |
| HuGaDB_v1_sitting_11_03.txt |    OK       | Corrupted | Corrupted |     OK        | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_12_00.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_12_01.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_12_02.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_12_03.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_13_00.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_13_01.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_13_02.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_13_03.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_13_04.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_13_05.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_13_06.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_14_00.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_14_01.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_14_02.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_14_03.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_15_00.txt | Corrupted   | Corrupted |    OK     | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_15_01.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_15_02.txt | Corrupted   | Corrupted |    OK     | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_15_03.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_16_00.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_16_01.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_16_02.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_16_03.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_16_04.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_16_05.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_17_00.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_17_01.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_17_02.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_17_03.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_17_04.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_17_05.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_17_06.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_18_00.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_18_01.txt | Corrupted   | Corrupted | Corrupted | Corrupted     | Corrupted   | Corrupted    |
| HuGaDB_v1_sitting_18_02.txt | Corrupted   | Corrupted | Corrupted | Corrupted     |    OK       | Corrupted    |
| HuGaDB_v1_sitting_18_03.txt | Corrupted   | Corrupted | Corrupted | Corrupted     |    OK       | Corrupted    |
 | HuGaDB_v1_sitting_in_car_01_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_04.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_05.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_06.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_08.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_09.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_10.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_11.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_12.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_13.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_sitting_in_car_01_14.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_01_00.txt  | 	 OK | 	OK | 	Corrupted | 	OK | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_01_03.txt  | 	 OK | 	Corrupted | 	OK | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_standing_03_00.txt  | 	 Corrupted | 	OK | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_04_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_04_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_04_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_04_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_05_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_05_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_standing_06_00.txt  | 	 OK | 	OK | 	OK | 	OK | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_07_00.txt  | 	 Corrupted | 	OK | 	Corrupted | 	OK | 	Corrupted | 	OK | 	
 | HuGaDB_v1_standing_07_01.txt  | 	 OK | 	OK | 	OK | 	OK | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_07_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_08_00.txt  | 	 OK | 	OK | 	OK | 	OK | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_08_01.txt  | 	 OK | 	OK | 	OK | 	OK | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_08_02.txt  | 	 OK | 	OK | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_08_03.txt  | 	 Corrupted | 	OK | 	OK | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_09_00.txt  | 	 OK | 	Corrupted | 	OK | 	Corrupted | 	OK | 	Corrupted | 	
 | HuGaDB_v1_standing_09_01.txt  | 	 OK | 	Corrupted | 	OK | 	Corrupted | 	OK | 	Corrupted | 	
 | HuGaDB_v1_standing_09_02.txt  | 	 OK | 	Corrupted | 	OK | 	Corrupted | 	OK | 	Corrupted | 	
 | HuGaDB_v1_standing_09_03.txt  | 	 OK | 	Corrupted | 	OK | 	Corrupted | 	OK | 	Corrupted | 	
 | HuGaDB_v1_standing_09_04.txt  | 	 OK | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_10_01.txt  | 	 OK | 	OK | 	Corrupted | 	Corrupted | 	Corrupted | 	OK | 	
 | HuGaDB_v1_standing_10_03.txt  | 	 OK | 	OK | 	Corrupted | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_standing_11_00.txt  | 	 OK | 	Corrupted | 	OK | 	OK | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_11_01.txt  | 	 OK | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_11_02.txt  | 	 OK | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_11_03.txt  | 	 OK | 	Corrupted | 	OK | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_11_04.txt  | 	 OK | 	Corrupted | 	OK | 	OK | 	OK | 	Corrupted | 	
 | HuGaDB_v1_standing_12_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_12_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_12_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_12_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_12_04.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_13_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_13_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_13_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_13_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_15_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_15_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_15_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_15_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_15_04.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_16_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_16_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_16_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_16_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_16_04.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_17_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_17_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_17_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_17_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_18_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_18_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_18_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_18_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_standing_18_04.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_03_00.txt  | 	 Corrupted | 	OK | 	Corrupted | 	OK | 	Corrupted | 	OK | 	
 | HuGaDB_v1_walking_03_01.txt  | 	 Corrupted | 	OK | 	Corrupted | 	OK | 	Corrupted | 	OK | 	
 | HuGaDB_v1_walking_04_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_04_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_04_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_04_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_04_04.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_04_05.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_05_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_05_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_05_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_05_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_06_03.txt  | 	 OK | 	OK | 	OK | 	OK | 	Corrupted | 	OK | 	
 | HuGaDB_v1_walking_06_05.txt  | 	 OK | 	OK | 	OK | 	OK | 	Corrupted | 	OK | 	
 | HuGaDB_v1_walking_07_00.txt  | 	 Corrupted | 	OK | 	Corrupted | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_07_01.txt  | 	 Corrupted | 	OK | 	Corrupted | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_07_02.txt  | 	 Corrupted | 	OK | 	Corrupted | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_07_03.txt  | 	 Corrupted | 	OK | 	Corrupted | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_07_04.txt  | 	 Corrupted | 	OK | 	Corrupted | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_09_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_09_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_09_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_09_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_11_00.txt  | 	 OK | 	Corrupted | 	OK | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_11_01.txt  | 	 OK | 	Corrupted | 	OK | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_11_02.txt  | 	 OK | 	Corrupted | 	OK | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_11_03.txt  | 	 OK | 	Corrupted | 	OK | 	OK | 	OK | 	OK | 	
 | HuGaDB_v1_walking_12_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_12_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_12_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_12_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_12_04.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_12_05.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_12_06.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_13_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_13_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_13_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_13_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_14_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_14_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_14_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_14_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_14_04.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_15_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_15_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_15_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_15_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_15_04.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_15_05.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_15_06.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_15_07.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_15_08.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_15_09.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_15_10.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_16_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_16_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_16_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_16_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_16_04.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_17_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_17_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_17_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_17_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_17_04.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_17_05.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_17_06.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	
 | HuGaDB_v1_walking_18_00.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	OK | 	Corrupted | 	
 | HuGaDB_v1_walking_18_01.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	OK | 	Corrupted | 	
 | HuGaDB_v1_walking_18_02.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	OK | 	Corrupted | 	
 | HuGaDB_v1_walking_18_03.txt  | 	 Corrupted | 	Corrupted | 	Corrupted | 	Corrupted | 	OK | 	Corrupted |
 
</p>
</details>

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

# Citation

Database is described in this paper: https://link.springer.com/chapter/10.1007/978-3-319-73013-4_12

If you use HuGaDB in your research and would like to cite HuGaDB you can use: Chereshnev R., Kertész-Farkas A. (2018) HuGaDB: Human Gait Database for Activity Recognition from Wearable Inertial Sensor Networks. In: van der Aalst W. et al. (eds) Analysis of Images, Social Networks and Texts. AIST 2017. Lecture Notes in Computer Science, vol 10716. Springer, Cham

In Bibtex format:
@inproceedings{chereshnev2017hugadb,
  title={HuGaDB: Human Gait Database for Activity Recognition from Wearable Inertial Sensor Networks},
  author={Chereshnev, Roman and Kert{\'e}sz-Farkas, Attila},
  booktitle={International Conference on Analysis of Images, Social Networks and Texts},
  pages={131--141},
  year={2017},
  organization={Springer}
}
