# DWOLLA-assignment
-------------
Building a web service for datetime processing using Python

## Installation: 
### Build Docker image
- Clone this project
- Navigate to project directory and build the docker image with a tag:
```
docker build -t flask-api-ws:latest .
```
<br/>

### Start web service
- Run docker container:
```  
docker run -p 5000:5000 --label=dwolla-api-n-client flask-api-ws:latest
```
If the web service starts successfully, these logging statements should appear in the console:
```
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 205-475-804
```

### View web results 
- Curl to the url http://127.0.0.1:5000/v1/currentDateTime
- Output should be something like this
```
{"currentTime": "2021-10-02 03:40:02"}
```

### Start client program
- Find the docker container id using
```
docker ps --filter "label=dwolla-api-n-client"
```
- Run the client.py
```
docker exec -ti <container id> python3 client.py
```
- Output should be something like this
```
Time is: 03:40:02
```