## Simple Backend for API Testing
Serves as an Arbitrary API Endpoint for Testing Purposes

## Run Locally
```
pip install -r requirements.txt

python introspect-dummy.py
```

## Build

```
docker build -t cstsui/introspect-dummy:1.0.0 .
docker push cstsui/introspect-dummy:1.0.0
```

## Deploy on Openshift

```
oc new-project api-backend

# Creates route/service/deployment
oc apply -f deploy.yaml
```