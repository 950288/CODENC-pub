# GPU driver installation

# for GPU
nvcc -V
sudo apt-get remove --purge nvidia* # 卸载驱动
sudo apt update
ubuntu-drivers devices
ubuntu-drivers autoinstall
nvidia-smi

# for vGPU
https://help.aliyun.com/zh/egs/user-guide/use-cloud-assistant-to-automatically-install-and-upgrade-grid-drivers?spm=5176.28426678.J_HeJR_wZokYt378dwP-lLl.19.a4dc5181Ioj3kS&scm=20140722.S_help@@%E6%96%87%E6%A1%A3@@2526616.S_BB1@bl+BB2@bl+RQW@ag0+os0.ID_2526616-RL_GPU%E8%99%9A%E6%8B%9F%E5%8C%96-LOC_search~UND~helpdoc~UND~item-OR_ser-V_3-P0_3