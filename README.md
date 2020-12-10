### Nvidia Jetson
1. Libegl-mesa0:armhf dependency error:
  ```
   cd /usr/share/glvnc/egl_vender.d/
   sudo mv 50_mesa.json 50_mesa-old.json
   sudo apt --fix-broken install
  ```
2. Install SSH
```
sudo apt install openssh-server
```
3. Install CUDA - deb (local)
https://developer.nvidia.com/cuda-downloads
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.1.1/local_installers/cuda-repo-ubuntu2004-11-1-local_11.1.1-455.32.00-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2004-11-1-local_11.1.1-455.32.00-1_amd64.deb
sudo apt-key add /var/cuda-repo-ubuntu2004-11-1-local/7fa2af80.pubsudo apt-get updatesudo apt-get -y install cuda
```
