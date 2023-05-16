#DONE! EXTRACT DATA FROM LOAD CELL AND CURRENT SENSOR INTO CSV FILE W/O HEADER
import serial
import csv

ser = serial.Serial('COM3',9600)
#columns = defaultdict(list) #each value in each column appended to a listoo

while (1==1):
    Data = (ser.readline().strip())
    b = Data.decode('utf-8') 
    y = b.split()
    print (y)
    
    with open('C:\\Users\\HP\\Desktop\\FYP Experiment Anas 2022\\Pytho\\.csv','a') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(y)

    #f.close('C:\\Users\\HP\\Desktop\\FYP Experiments 2022\\Python\\Motor.csv')
       
 
    ##column_names = ['Actual Angle','Target Angle'])
    ##the writer = csv.Dictwriter(f, column_names = column_names) 