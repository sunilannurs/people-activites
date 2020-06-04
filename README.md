#create the virtual environment#
step1:

sudo apt-get install python3-venv

#activate the virtual-env#
step2:

python3 -m venv virt_env && source virt_env/bin/activate

#install the requirement"

step 3:

python3 -m pip install -r requirements.txt



step 4:

python3 manage.py makemigrations

step 5:

python3 manage.py migrate


#for adding some dummy data#

step 6:

python manage.py add_user_activities #for add the dummy data"

step 7:

python3 manage.py runserver

step 8:

localhost:8000/api/users

#run the url in get method.