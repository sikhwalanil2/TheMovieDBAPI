#### bynder-demo

### 1. Fork this repo

After forking this project in `Github`, run these commands:

```bash
## clone this repo to a local directory
git clone git@github.com:sikhwalanil2/TheMovieDBAPI.git

```

### 2. Install required packages
```bash
## install the python modules
pip install -r requirements.txt

```
### 3. Run Test Suite

```bash

## Run all testcases
pytest
<img width="1355" alt="Screenshot 2023-05-09 at 8 24 48 AM" src="https://user-images.githubusercontent.com/31472941/236984303-8f273a22-4e74-453a-8762-597e2ad69aeb.png">

## Run testcases with html report
pytest --html=report.html 
<img width="1354" alt="Screenshot 2023-05-09 at 8 25 38 AM" src="https://user-images.githubusercontent.com/31472941/236984245-24b8a197-82ed-4863-9d52-3dbd6935b365.png">

##HTML report will look like this
<img width="1554" alt="Screenshot 2023-05-09 at 8 25 54 AM" src="https://user-images.githubusercontent.com/31472941/236984556-7d9818cf-8dbc-4125-aced-b391112f42b3.png">
```

###4. Dockerized Jenkins build
```bash

## build docker image
DOCKER_BUILDKIT=0 docker build -t jenkins-docker-image -f JenkinsDockerfile .

## run docker image
docker run -d -p 8080:8080 --name jenkins-docker-container -v /var/run/docker.sock:/var/run/docker.sock jenkins-docker-image

```
## Jenkins Setup

http://localhost:8080/

Complete the setup
Create new Freestyle project
Setup git repo 
in 'Build steps'
Add below script
```bash
IMAGE_NAME="test-image"
CONTAINER_NAME="test-container"
echo "Check current working directory"
pwd
echo "Build docker image and run container"
DOCKER_BUILDKIT=0 docker build -t $IMAGE_NAME .
docker run -d --name $CONTAINER_NAME $IMAGE_NAME
echo "Copy result.xml into Jenkins container"
rm -rf reports; mkdir reports
docker cp $CONTAINER_NAME:/TheMovieDBAPI/reports/result.xml reports/
echo "Cleanup"
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker rmi $IMAGE_NAME
```

In post-build actions, 
choose Publish JUnit test result report'
Add 'reports/result.xml' 
Click on 'Build now'

<img width="1569" alt="Screenshot 2023-05-09 at 10 37 35 AM" src="https://user-images.githubusercontent.com/31472941/236999205-13e8a1dc-7a51-48f0-b8de-cb47673d7c50.png">

<img width="1035" alt="Screenshot 2023-05-09 at 10 37 29 AM" src="https://user-images.githubusercontent.com/31472941/236999236-3c440840-9ea0-4890-a716-f16e685c3efc.png">


