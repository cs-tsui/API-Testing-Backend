## Simple Backend for API Testing
Serves as an Arbitrary API Endpoint for Testing Purposes

## Run Locally
```
pip install -r requirements.txt

python myflask.py

```

## Build

```
docker build -t cstsui/flask-api .
docker push cstsui/flask-api
```

## Deploy on Openshift

```
oc new-project api-backend

# Creates route/service/deployment
oc applyh -f deploy.yaml
```