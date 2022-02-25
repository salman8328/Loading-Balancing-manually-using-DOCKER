# Loading-Balancing-manually-using-DOCKER

Create a directory of any name- <name>
In that <name> directory paste the Docker file given this repository.
Then in the same directory paste server.py file in backend servers.
####################################
Be in the same <name> directory and run the following commands in terminal-

docker build -t <name> .
  
docker run --name foo -d -p 8080:80 <name>

 #######################################################################
Load_balancer configuration-
  
Create a directory of any name- <name>
In that <name> directory paste the Docker file given this repository.
Then in the same directory paste load_balancer.py file in backend servers.
####################################
Be in the same <name> directory and run the following commands in terminal-

docker build -t <name> .
  
docker run --name foo -d -p 8080:80 <name>
  
  
!!!!!!!!!!!!!!!!!voila!!!!!!!!!!!!!!!!!!! load balancing will be done and you can check By googling https://<load-balancer-ip-address:8080>
keep refreshing so that you can the change in the webpage!
#####################################################
#common errors:
After running the above commands the port 8080 will be allocated to some container and when you try to rerun the above commands it gives a error named port alloted!
To remove that error type below command in terminal-
  
sudo lsof -i :8080|grep "python3"|cut -d " " -f2|xargs kill -9

When you install docker and try to run the above commands it will give an error named access denied, thats because docker needs sudo access to create and manage containers, so type sudo before any docker commands.

  example: sudo docker ps
