# Jenkins Docker Troubleshooting Nightmare
## Getting Jenkins Ready for Docker
- This Guide is assuming that we are connecting to an EC2 Instance with Jenkins already installed and running
- Docker has not been installed however
- First SSH into your EC2 Instance
- Install docker on jenkins server, standard Ubuntu Docker Install - Follow the online guide
- Then you need to edit sudoers so Jenkins can use sudo
- Navigate with `cd /etc` then `sudo nano sudoers`
- Should look like this inside
```
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults    env_reset
Defaults    mail_badpass
Defaults    secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# Host alias specification

# User alias specification

# Cmnd alias specification

# User privilege specification
root    ALL=(ALL:ALL) ALL

# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
```

- at the end under
```
# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
```
- add `jenkins ALL=(ALL) NOPASSWD: ALL`
- so it looks like
```
# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
jenkins ALL=(ALL) NOPASSWD: ALL
```
- add jenkins and docker to group `sudo usermod -a -G docker jenkins`
- restart jenkins
```
sudo service jenkins stop
sudo service jenkins start
```
- update or install Token Macro on jenkins in Manage Jenkins -> Manage Plugins
- restart Jenkins again as above
- return to Manage Plugins and go to available
- search docker
- install `CloudBees Docker Build and Publish plugin`
- this doesn't require a restart to work but is probably advised

### Jenkins Won't Start after stop
- Run `ps auxw | grep jenkins`
- Then kill all processes that come up

## Jenkins Job
- Once you have done the standard job setup, select the Github Project tickbox and add your https link to it
- Next set up the ssh keys to be able to interact with your repository
- For this navigate to your `.ssh` directory `cd ~/.ssh` should get you there
- Then run `ssh-keygen -t rsa -b 4096 -C "your@email"`, give the key a name and you can give it a passphrase
- For security a passphrase is good but can't be changed if you forget
- Next `cat` the `yourkey.pub` file and copy they key, as that is your public key
- Got to your github repo online, got to settings and then deploy keys
- Add a new key, give it a name and paste in your public key, allows write access then add key
- Return to Jenkins, go down to source code management and select git
- Copy in your SSH link from your repo
- Go back to your terminal and cat your `yourkey` and copy the private key
- Then add your credentials selecting SSH in jenkins, give it a name then select enter private key directly and paste in the key
- Select that SSH and change branches to build to your dev branch
- Select in Build Environment, Delete workspace before build starts
- For build, choose execute shell and enter `sudo docker build . -t dockerusername/dockerrepo`
- Next select Docker Build and Publish
- For Repository name put `dockerusername/dockerrepo`
- You can put a tag but don't need to
- For Docker host URI put `unix:///var/run/docker.sock`, this is the same for all Linux. Windows have a different one
- Server Credentials add nothing and Docker Registry URL add nothing
- For Registry Credentials, click the add button, use Username with Password
- Add your username and password for docker, you can give an ID but don't have to as will use your username if not
- Then the job is complete
