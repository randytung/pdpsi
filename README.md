# Website for Cornellpdpsi
This webapp will use Django as the python web framework in the backend to describe all of the models we use. Then, we will use Restless API in order to serialize all of the data into JSON and send it back to the front end. 

##Setting up the virtual environment
First install virtual environment by inputting
```
$ pip install virtualenv
```
Second, create a virtual environment by inputting 
```
$ virtualenv pdpsi
```

Third,  you have to navigate into the newly created virtual environment folder and activate it, then clone the repo
```
$ cd pdpsi
$ source bin/activate
$ git clone https://github.com/randytung/pdpsi.git
```
Fourth, you have to navigate into the cloned repository and download all of the python dependencies that this website will use. They are all located in ``requirements.txt``. They can all be downloaded by running the command:|
```
$ pip install -r requirements.txt
```

## Setting up Database
To install all of the brothers into the database, cd into the file with manage.py and run
```
$ python manage.py add_brothers
```




