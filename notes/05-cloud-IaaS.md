# Module 05 - Cloud & Infrastructure as a Service Basics
Last updated: 8 May 2024
Status:  [in progress]


### Best Practices to remember
Security best practice: create a separate user that is not root, for every app

#### Process of configuring the user-zero on a Linux server
adduser <name>
usermod -aG sudo <name>
su - <name>
# versus $

then you need to get ssh <name>@<ip> working (instead of ssh root@<ip>)
exit log back in as root@<ip>
switch to <name>
cat your public sh key (~/.ssh/id_rsa.pub)
in ~ create .ssh directory

sudo vim .ssh/authorized_keys    --> put your public ssh key in here

exit and try to come back in as ssh <name>@<ip>



### Commands 
cat ~/.ssh/id_rsa.pub

###### running things in detached
& just add an ampersand?   java -jar <filename.jar> &
nohup is a 'no hangup' approach?  don't know more

###### ways to check if your app is running: 
ps aux | grep java
netstat -lpnt
jobs

###### to kill the app running
(sudo) kill <pid>
kill -9 <pid> is more forceful

### Setup Issues / configs that came up
- java sdk 17 is compatible with gradle 7.3.1  
- gradle WSL is installed in your ~/opt


### To dos 
- probably should try to fully uninstall the extra gradle 4.4 that's on WSL (usr\share\gradle i think?)  - there's already 7.5 and 7.3.1 in /opt
