# Python

Creating virtual environment, 

Install Virtual Environment
    sudo apt-get install virtualenv (Linux)
    pip install virtualenv
        (installing pip if not available)
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        python get-pip.py

Set Virtual Enviroment
    virtualenv --python = [select your path] [environment name] (to specify path)
    virtualenv [environment name] (default python path)

Activate Virtual Enviromnet
    source [select your path] activate
    [environment name]/Scripts/activate.bat

Update Requirement / Packages
    pip install -r requirements.txt

Run Application
    python manage.py runserver [url if required]:[specify port if any]