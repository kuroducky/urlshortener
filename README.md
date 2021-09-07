# urlshortener Program

URL Shortener program

#Installation

##Database
Ensure that MySQL Community Server is downloaded
Here is a link to download MySQL[Link](https://dev.mysql.com/downloads/mysql/ "MySQL Community Server").

Once the server has been downloaded and installed properly, run in Terminal this code

```console
foo@bar:~$ mysql -u <username> -p
```

You will be prompted to enter your password.

Once, the mysql connection has been established, create a database and the table by running the code below:

```console
mysql > CREATE DATABASE url_db;
mysql > USE url_db;
mysql > CREATE TABlE url_tbl (
    url_id INT NOT NULL AUTO_INCREMENT,
    shortened_url LONGTEXT NOT NULL,
    original_url LONGTEXT NOT NULL,
    creation_date DATE NOT NULL,
    PRIMARY KEY (url_id)
)
```

With this, database has been properly established.

#Client-Server Application

##Frontend
The frontend code was created using react.

cd into frontend/ directory and run the code

```console
yarn start
```

##Backend

It is suggested that the user creates a virtual environment first before installing all dependencies and modules

Run the code below on your command line on the directory you would want to activate the virtual environment
Do take note that the second argument 'venv' is the name of the virtual environment created

```console
foo@bar:~$ python3 -m venv venv
```

Next, after creating the virtual environment, activate it:

```console
foo@bar:~$ source venv/bin/activate
```

Terminal will then be changed to look like this :

```console
(venv)foo@bar:~$
```

The last part of the installation process is to install all required dependencies/libraries before running the backend Flask Server.
There is a requirements.txt files which has been included for easy installing

Navigate to the directory where the requirements.txt file is located and run this line:

```console
(venv)foo@bar:~$ pip install -r requirements.txt
```

Lastly, from the repository that was cloned, navigate to urlhortener/backend/src/ and run the python file 'main.py'

```console
(venv)foo@bar:~$ python3 main.py
```

If there is an error 'NameError: name '\_mysql' is not defined', just run this line

export DYLD_LIBRARY_PATH=/usr/local/mysql/lib
