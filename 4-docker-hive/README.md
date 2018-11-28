# docker-hive


![alt txt](https://high.swampscottps.org/wp-content/uploads/sites/3/2017/08/Work_In_Progress.png)


### 1. Get Docker CE for Ubuntu

[Link](https://docs.docker.com/install/linux/docker-ce/ubuntu/) :link:

**Uninstall old versions**

`sudo apt-get remove docker docker-engine docker.io`

**INSTALL DOCKER CE**

`sudo apt install apt-transport-https ca-certificates curl software-properties-common`

`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

`sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic test"`

`sudo apt update`

`sudo apt install docker-ce`




