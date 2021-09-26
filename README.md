# GetMyRoom

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)<br>
This app will allow you to enable the entire hotel management system, available for both the Room Manager and the Customer.

##  Starting the Project

1. Clone the project in the virtual environment directory.

    ```
    git clone https://github.com/RitabrataDas343/GetMyRoom.git

    ```

2. Create a **virtual environment** with venv (install virtualenv, if its not installed).

    ```
    python3 -m venv env

    ```

3. Activate the virtual environemnt.
    ```
    source env/bin/activate

    ```
    
4. Install the requirements.

    ```
    pip3 install -r requirements.txt

    ```


5. Run the Migrations
    ```
    python3 manage.py makemigrations

    python3 manage.py migrate --run-syncdb

    ```
6. Run the development server
    ```
    python3 manage.py runserver

    ```
7. Head to server http://localhost:8000


## For contributors

This app uses the following technologies:

+ HTML/CSS/JS
+ Materialise CSS
+ Python(Django)

If you want to contribute to this project, then you are very much welcome to do that.
