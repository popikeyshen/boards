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
3. Cuda is pre-installed but nvcc is not found:
```
export LD_LIBRARY_PATH=/usr/local/cuda/lib
export PATH=$PATH:/usr/local/cuda/bin
```
