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
*Develop the Application*:
- Start by developing your application using your preferred programming language and frameworks.
*Containerize the Application*:
- Create a Dockerfile that specifies the steps to build your application's Docker image.
- Use the Docker CLI to build the image: `docker build -t my-app .`
*Run Containers*:
- Use the Docker CLI to run containers from the created image:`docker run -d my-app`
- Multiple containers can run concurrently, each encapsulating a specific instance of your application.
*Manage Containers*:
Use Docker CLI commands to manage containers:
- `docker ps`: List running containers.
- `docker stop <container_ id>`: Stop a running container.
- `docker start <container id>`: Start a stopped container.
- `docker rm <container id>`: Remove a container.

## DOCKER REGISTRY
- Docker images are stored in a centralized repository called the Docker Registry
- The Docker Registry serves as a distribution hub for sharing and accessing Docker images  

![Image1](./img/image1.png)

## HANDS ON
Run a image (-d run in background or detach, -P expose all ports, --name assigns a name):  
`docker run -d -P --name catgif manifoldailearning/catgif`  
When running `docker ps` you'll see in catgif the command "python ./app.py", it runs a script  



