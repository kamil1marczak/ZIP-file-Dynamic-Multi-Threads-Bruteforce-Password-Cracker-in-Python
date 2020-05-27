# ZIP File Dynamic Bruteforce Password Cracker in Python
> Simple but powerful tool to crack passwords of zip file

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Instructions](#instructions)
* [Code Examples](#code-examples)
* [Status](#status)
* [Contact](#contact)

## General info
The project is motivated by my desire to develop my skills in pentesting and general python skills. Feel free to copy but use it in ethical way only ;) 

## Technologies
* colorama==0.4.1

## Setup
execute from bash terminal: `source install.sh` script from general folder will install and activate virtual env  

## Instructions
To execute help: `python3 zip_cracker.py -h`

It will return:
```
usage: zip_cracker.py [-h] [--max MAX] [-t THREADS] [-l] [-u] [-d] [-p] file

ZIP File Dynamic Bruteforce Password Cracker in Python

positional arguments:
  file                  name of file to bruteforce.

optional arguments:
  -h, --help            show this help message and exit
  --max MAX             Maximal len of password default = 14
  -t THREADS, --threads THREADS
                        Number of threads, default = 1
  -l, --lowercase       Password generator will include lowercase
  -u, --uppercase       Password generator will include uppercase
  -d, --digits          Password generator will include digits
  -p, --punctuation     Password generator will include punctuation
```


## Code Examples
to run zip file password cracker:
- on file zip_file.zip
- determine password no longer than 4 characters
- operate on 5 threads
- check combinations of password including uppercase only

`python3 zip_cracker.py zip_file.zip --max 4 -u -t 5`
## Status
Project is: finished, I am looking for new inspirations, please reach me for that purpose/ suggestions (email below)

## Contact
Created by @kamil1marczak - kamil1marczak@gmail.com - feel free to contact me!