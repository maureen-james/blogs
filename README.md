# blogs


## By Maureen james
  
# Description  
This is a website where bloggers can post their blogs

### live link : https://bravoblogs.herokuapp.com/

 



## Setup and Installation  
To get the project .......  

##### Cloning the repository:  
 ```bash 
https://github.com/maureen-james/blogs
```
##### Navigate into the folder and install requirements  
 ```bash 
cd blogs pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations database name
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

 ### Api Endpoints
 
 * blogs api



## Technology used  

* [Python3.8.10](https://www.python.org/)  
* [Django 4.0.5](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  


## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  


## License 

* *MIT License:*
* Copyright (c) 2022 **Maureen james**

[Go Back to the top](#blogs)