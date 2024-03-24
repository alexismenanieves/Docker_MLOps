# README

## COMMANDS
Version: `docker --version`  
View working demo: `docker run hello-world`  
Fetch a busy box image (docker image registry to local): `docker pull busybox` 
View local images: `docker images` 
Load container (docker client finds images and run): `docker run busybox`  
Run command in docker: `docker run busybox echo "Hello from busybox"`  
List dockers running: `docker ps`  
List dockers running or not: `docker ps -a`  
Run multiple commands in docker (-it interactive mode, type exit if needed): `docker run -it busybox sh`  
See documentation: `docker run --help`
Remove container (you require the id): `docker rm ${id}`

## WORKING WITH DOCKER
Develop the Application:
- Start by developing your application using your preferred programming language and frameworks.
Containerize the Application:
- Create a Dockerfile that specifies the steps to build your application's Docker image.
- Use the Docker CLI to build the image: `docker build -t my-app .`
Run Containers:
- Use the Docker CLI to run containers from the created image:'docker run -d my-app'
- Multiple containers can run concurrently, each encapsulating a specific instance of your application.