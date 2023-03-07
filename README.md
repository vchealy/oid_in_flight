# oid_in_flight

### This is just to show python code can be setup in a docker container and hopefully help others

I was converting this python app that I run on my pc daily into a docker image.
The hope was to get it hosted somewhere on the company network and save engineers from having to run this code themselves.

The code was initial set to run in windows but the code here had to be changed to function on the linux docker container.
Nothing drastic.   
There are a few system('cls') that were changed to system('clear')
In get_latest_file line 11 reportsIn\ was changed to reportsIn/

I haven't changed the console logging that gave the 'pretty' clean console look to logging in the docker desktop.
Just know that it works.

To manually run the code:
python watchdog.py
This sets the code watching the folder reportsIn. When a new csv file is added it does all the work I want giving output to ReportsOut
output is a multi-worksheet spreadsheet, a overview pdf and a multi-page pdf
If files ar rmoved from the folder the file names are logged to the console.

The report in is a csv file normally of 30_000 plus that is a list of devices and processes they have to complete.
The device ID determines the operator of the device  and thus the grouping in the output.
The device ID is a hex value where certain characters determine the operator and that value needs some bit shifting to get to decimal format.

I cannot include any example reports. The code holds nothing that is confidential.


