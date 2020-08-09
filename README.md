# Data_parser
A small data parser that reads the ip sheet and display the total number of used ips BRAS wise.

To excute this file you will need to install the pandas package for python. The command below will install the 
package if python and pip are insatlled locally and the ENV Path is set for python and pip.

    pip install pandas

Here is a small guide to install python and the pandas package on windows.

https://data-flair.training/blogs/install-pandas-on-windows/

the output of the script will display the pool name, used_ips, remaining_ips, total_ips. below is the format in which it will be displayed.

pool: khi-cbbr2
used_ips: 61603
remaining_ips: 1885
total_ips: 63488
pool: khi-cbbr3
used_ips: 57482
remaining_ips: 6006
total_ips: 63488
pool: cbbr3-activity
used_ips: 3532
remaining_ips: 2612

A screen shot is also attched in the repositry to show the output of the script.

to run this file directly from the cmd. cd into the directory Data_parser and run the below command.
  

    python data_parser.py
  

