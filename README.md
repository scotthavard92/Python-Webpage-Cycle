# Python Webpage Cycle
Automatically open webpages listed in a .csv file

## Requisites
This script requires a .csv file, and is currently configured to spreadsheets that have no more than 100 rows. This 
script also requires [Pandas](https://github.com/pandas-dev/pandas).

## Usage
* Configure spreadsheet so that the desired URL's are in the THIRD column.
* Save .csv in a known location.
* Run the script (Run 'python OrphanSlayer.py' if running from the command line).
* When prompted, enter the absolute path where the .csv file is located. Click Enter.
* When prompted, enter the name of the .csv file, including the ".csv". Click Enter.
* The first webpage associated with the first URL in the spreadsheet will open in the default browser. 
* Press one to access the next webpage.
* Press two to exit the program. 
