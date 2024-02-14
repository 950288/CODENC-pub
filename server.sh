# auto ssh login
# windows https://blog.csdn.net/qq_45624685/article/details/122631083
type C:\Users\95028\.ssh\id_rsa.pub | ssh root@xx.xx.xx.xx "cat >> .ssh/authorized_keys"


# Screen
screen -ls
screen -S test
ctrl+a,然后输入d,退出当前窗口


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