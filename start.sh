source .envrc
pip install -r requirements.txt
flask db init
flask db migrate -m 'init'
flask db upgrade
flask run