cd ./backend
python3.12 -m venv venv
source venv/Scripts/activate
pip install django
pip install -r requirements.txt
./manage.py migrate
cd ../frontend
npm install