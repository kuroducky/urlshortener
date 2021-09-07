# urlshortener Program

URL Shortener program

Installation

Database
Ensure that MySQL Community Server is downloaded

For this application, you must run 2 servers(frontend and backend)

Frontend
The frontend code is created using Python

Backend

It is suggested that the user creates a virtual environment first before installing all dependencies and modules

Run the code below on your command line on the directory you would want to activate the virtual environment
Do take note that the second argument 'venv' is the name of the virtual environment created

```console
foo@bar:~$ python3 -m venv venv
foo
```

Next, after creating the virtual environment, activate it

```console
foo@bar:~$ source venv/bin/activate
```

Terminal will then be changed to look like this :

```console
(venv)foo@bar:~$ source venv/bin/activate
```

Next, install all required dependencies before running the backend Flask Server.
There is a requirements.txt files which has been included for easy installing

Navigate to the directory where the requirements.txt file is located and run this line:

```console
(venv)foo@bar:~$ pip install requirements.txt
```

Lastly, from the repository that was cloned, navigate to urlhortener/backend/src/ and run the python file 'main.py'

```console
(venv)foo@bar:~$ python3 main.py
```

If there is an error 'NameError: name '\_mysql' is not defined', just run this line
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib
