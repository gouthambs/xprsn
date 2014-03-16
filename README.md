xprsn
=====

Setup Python
------------
Once you have downloaded WinPython, add the python installation folders to your path.
For instance, add:
```
C:\WinPython-32bit-2.7.6.3\python-2.7.6
C:\WinPython-32bit-2.7.6.3\python-2.7.6\Scripts
```

Once this is added to the path, you will be able to call ```python``` from ```cmd```.

Set Up Process
--------------

Install virtual environment library 
```
pip install virtualenv==1.11.4
```

Create the virtual env named xprsn-env for development
```
virtualenv xprsn-env
```

Activate the environment
```
xprsn-env\Scripts\activate
```

This will install all the required packages 
```
pip install -r Requirements.txt
```

Create the database
```
python db_create.py
```

Running the webapp
------------------

To run the webapp, activate the environment as shown above. Once you have activated the environment,
just run
```
python webapp.py
```


