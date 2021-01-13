# Python v env Windows

Erstellen:
py -m venv ./env     

Aktivieren:

.\env\Scripts\activate

Dependencies installieren

pip install -r requirements.txt

Dependencies speichern

pip freeze > requirements.txt

Dockerfile Docker starten

docker build -t test-client .

Docker Container starten

docker run test-client