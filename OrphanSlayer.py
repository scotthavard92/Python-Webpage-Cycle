import os
import webbrowser
import csv
import pandas as pd

                          
def Access_CSV():
       with open(filename,'rb') as orphans:
               full_list = csv.reader(orphans)
               #for row in fulllist:
                       #print row
               df = pd.DataFrame(list(full_list), columns = ['number', 'hits', 'url'])
               #Debug 
               #URL_loc = df.at[0,'url'] 
               #print(URL_loc)
               return df

def Webpage_Cycle():
        i=0
        while (i < 100):
                URL=df.at[i,'url']
                webbrowser.open(URL)
                x = input('1 for next, 2 to exit: ')
                if x == 1:
                        i=i+1
                elif x == 2:
                        print("exit")
                        return 0
                else:
                        print("error")
                        return 0

 

f_path = raw_input('Please enter the path for the CSV file:')
if os.path.isdir(f_path):
       os.chdir(f_path)
       filename = raw_input('Please enter the filename, including the ".csv":')
       df = Access_CSV()
       Webpage_Cycle()
else:
       print('Error')

               

