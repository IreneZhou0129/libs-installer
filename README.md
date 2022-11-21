# libs-installer
When we run other's code, some packages are missing in our environment. If `requirements.txt` is provided, we run `pip install -r requirements.txt`. 

This libs-installer is built for the code where `requirements.txt` is missing. 


## Before
Enter a virtual environment.
```
python3 -m venv venv_name
```
```
source venv_name/bin/activate
```
## How to run
```
python get_libs.py -f MY_CODE.py
```