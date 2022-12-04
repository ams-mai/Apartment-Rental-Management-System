## Salazar-Apartment-Rental-Management-System
### Requirements
Python installed (version 3 or higher)
### Download source code
```
git clone https://github.com/ams-mai/Salazar-Apartment-Rental-Management-System.git
```
<br>

### Create virtual environment
1. Install virtualenv library.  
Command:
```
pip install virtualenv  
```
2. Go to the project directory and create a virtual environment.  
Command:
```
virtualenv venv
```
3. Activate virtualenv.  
Command in git bash:
```
source venv/Scripts/activate  
```
<br>

### Install libraries
Make sure you are inside your virtual environment.  
Command:
```
pip install -r requirements.txt  
```
<br>

### Set-up database
Make sure you are inside your virtual environment.  
Command:
```
flask create_tables  
```
<br>

### Running the app
Make sure you are inside your virtual environment.  
Command:
```
python run.py  
```
<br>

Enter http://localhost:5000/ in your browser to go to app.            
<br><br>

## Note
To access admin page, input this as the admin key:  
```
EdFer@12!90
```
