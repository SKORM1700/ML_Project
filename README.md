# ML_Project

##Software and other requirements

1.  [github] (https://url.com)
2.  [Heroku] (https://url.com)
3.  [VS Code] (https://url.com)
4.  [git cli] (https://url.com)

## conda create -p env_name python==3.7 -y
## conda activate env_name\

## pip install -r requirements.txt

# To setup CI/CD pipeline in heroku, 3 things are required
1.  Heroku email
2.  Heroku_api_key
3.  Heroku app name


## DOCKER
docker build -t <image_name>:<tagname> .        (. represent pwd)
docker images   to check all docker images

## Run docker image (image_id is can be obtained from : docker images)
docker run -p 5000:5000 -e PORT=5000 image_id

## To check running container
docker ps 

## to stop any container (Container id can be obtained from: docker ps)
docker stop container_id