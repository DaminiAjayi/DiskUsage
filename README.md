# DiskUsage
Get disk usage for all files in a mount point

# Dependencies
This script was developed using python3 and requires python3 for usage. 
The application only uses std libraries, therefore there are no other external dependencies required to be installed

# Usage
Clone this repository and run the script such that it takes in the mount point as an argument. Used as follows:

``` 
python3 getdiskusage.py mountpoint
mountpoint is the argument passed when calling the script 
```

## Example
```
Oluwadaminis-MacBook-Pro:Diskusage ajayi$ python3 getdiskusage.py ~/Desktop/Sample
{'files': [OrderedDict([('/Users/ajayi/Desktop/Sample/WEEK1HOMEWORK-fall.pdf',
111222),
('/Users/ajayi/Desktop/Sample/headers.txt', 22500),
('/Users/ajayi/Desktop/Sample/credit_card_data.txt',
22461),
('/Users/ajayi/Desktop/Sample/Homework1.2.2.R', 5415),
('/Users/ajayi/Desktop/Sample/Homework1.2.1.R', 5329),
('/Users/ajayi/Desktop/Sample/2.2.1_real.Rd', 858)])]}
```

