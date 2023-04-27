# TreeMenu

---

##### Navigation menu that can be manageable via database. For demonstration purposes the database is included. 


### How to run:

1. Create _venv_  
   `python -m venv venv`
2. Run _venv_
    * Linux - `source venv\bin\activate`
    * Windows - `venv\Scripts\activate` 
3. Migrate data from database   
    `python manage.py makemigrations`   
    `python manage.py migrate`
3. Install requirements  
    `pip install -r requirements.txt`
4. Run django server  
    `python manage.py runserver`


#### Superuser: 

login: `admin`  
password: `admin`