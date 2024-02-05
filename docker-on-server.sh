# for vGPU

https://help.aliyun.com/zh/egs/user-guide/use-cloud-assistant-to-automatically-install-and-upgrade-grid-drivers?spm=5176.28426678.J_HeJR_wZokYt378dwP-lLl.19.a4dc5181Ioj3kS&scm=20140722.S_help@@%E6%96%87%E6%A1%A3@@2526616.S_BB1@bl+BB2@bl+RQW@ag0+os0.ID_2526616-RL_GPU%E8%99%9A%E6%8B%9F%E5%8C%96-LOC_search~UND~helpdoc~UND~item-OR_ser-V_3-P0_3

# for GPU

nvcc -V
sudo apt-get remove --purge nvidia* # 卸载驱动
sudo apt update
ubuntu-drivers devices
ubuntu-drivers autoinstall
nvidia-smi

# install docker
https://docs.docker.com/engine/install/ubuntu/
# test docker
sudo docker run hello-world

# NVIDIA Container Toolkit
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

# test 
sudo docker run --rm --gpus all nvidia/cuda:11.4.3-cudnn8-runtime-ubi8 nvidia-smi

# change docker source
https://cloud.tencent.com/document/product/1207/45596

# reference
https://blog.csdn.net/qq_39638989/article/details/121275230

