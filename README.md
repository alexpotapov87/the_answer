# the_answer

# test run localhost
cd app/app/
export FLASK_APP=main.py
flask run

to build new docker image:
docker build -t alexpotapov87/web_ta .
docker push alexpotapov87/web_ta

# to run in k8s see ta_infra repo