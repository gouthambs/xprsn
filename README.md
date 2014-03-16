xprsn
=====

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


