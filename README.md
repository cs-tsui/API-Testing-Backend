## Simple Backend for API Testing
Serves as an Arbitrary API Endpoint for Testing Purposes

## Run Locally
```
pip install -r requirements.txt

python introspect-dummy.py
```

## Build

```
docker build -t cstsui/introspect-dummy .
docker push cstsui/introspect-dummy
```

## Deploy on Openshift

```
oc new-project api-backend

# Creates route/service/deployment
oc apply -f deploy.yaml
```