import time
import os


def docker_ubuntu():

    os.system("sudo apt-get remove docker docker-engine docker.io containerd runc")
    os.system("sudo apt-get update")
    time.sleep(15.0)
    os.system("sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common")
    os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -")
    os.system('sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"')
    os.system("sudo apt-get update")
    time.sleep(30.0)
    os.system("sudo apt-get install docker-ce docker-ce-cli containerd.io")
    time.sleep(10.0)
    os.system("sudo systemctl start docker")
    os.system("sudo systemctl enable docker")
    os.system("sudo service docker start")

    print("Be happy !")