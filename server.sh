cd /etc/yum.repos.d
cp CentOS-Base.repo CentOS-Base.repo.bak
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-6.10.repo
yum clean all
yum makecache

# sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
apt-get update
apt-get install conda
apt-get install screen

yum install tree
wget https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh
bash Miniconda3-py311_23.5.2-0-Linux-x86_64.sh
yum install conda

# win 追加环境变量 in cmd
path=%path%;D:\App\anaconda3\Scripts
path=%path%;D:\App\anaconda3
path=%path%;D:\App\anaconda3\Library\bin
path=%path%;D:\App\anaconda3\Library\mingw-w64\bin

conda update conda
conda create -n dev python
conda install git

pip install -r dependencies.txt
pip install psm
psm ls
psm use pypi

yum install -y screen
screen -ls
screen -S test
ctrl+a,然后输入d,退出当前窗口

# 驱动安装
nvcc -V
sudo apt-get remove --purge nvidia* # 卸载驱动
sudo apt update
ubuntu-drivers devices
ubuntu-drivers autoinstall
apt install nvidia-driver-535
nvidia-smi

conda install cudatoolkit=11.8.0 cudnn=8.8.0.121 -c  https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/win-64/ # 一键安装

conda search cudatoolkit --info
conda install cudatoolkit=xxx
conda search cudnn --info
conda install cudnn=xxx # https://developer.nvidia.com/rdp/cudnn-archive#a-collapse742-10
conda install cudnn=8.8.0.121 -c  https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/win-64/
conda install tensorflow-gpu=2.4.1
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

python -c "import torch; print(torch.cuda.is_available())"
python -c "import torch; print(torch.__version__)" 
from https://download.pytorch.org/whl/torch_stable.html
https://anaconda.org/pytorch/pytorch/files
https://mirror.sjtu.edu.cn/pytorch-wheels/cu118/?mirror_intel_list(国内强烈推荐)
pip3 install https://download.pytorch.org/whl/cu118/torch-2.0.1%2Bcu118-cp311-cp311-win_amd64.whl
or pip3 install https://mirror.sjtu.edu.cn/pytorch-wheels/cu118/torch-2.0.1+cu118-cp311-cp311-win_amd64.whl
pip3 install torch==2.0.1+cu118 torchvision torchaudio -i https://download.pytorch.org/whl/cu118  
-i https://pypi.douban.com/simple/ some-package  
-i https://pypi.tuna.tsinghua.edu.cn/simple some-package

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/fastai/
conda config --append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
conda config --set show_channel_urls yes

https://www.tensorflow.org/install/pip