# Keypoint Detection in Cephalometric X-ray Images

## Flask web API for Cephalometric X-ray Keypoint Detection

### Create GCP VM for Ubuntu 20.04 LTS
1. 更新 

 `~$ sudo apt update`

2. 下載 Miniconda

 `~$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`

3. 安裝 Miniconda

`~$ bash ./Miniconda3-latest-Linux-x86_64.sh`

4. 可以選擇移除

`~$ rm ./Miniconda3-latest-Linux-x86_64.sh`

5. 查看是哪種 shell

`~$ echo $SHELL`

6. 更新後的配置檔案

`$ source ~/.bashrc`

### 創建環境
`$ conda create -n kpdt python=3.9`
activate 環境

`$ conda activate kpdt`
`$ conda install pytorch torchvision torchaudio cpuonly -c pytorch`
從GitHub複製檔案至VM

`$ git clone https://github.com/Anson0411/Keypoint-Detection-in-Cephalometric-X-ray-Images.git`
`$ cd Keypoint-Detection-in-Cephalometric-X-ray-Images/`
`$ conda install --file requirements.txt`


使用conda安裝requirement.txt (找不到安裝包就用pip安裝)

`while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt`

如果在運行時無法找到 libGL.so.1 這個共享庫

`sudo apt-get install libgl1-mesa-glx libgl1-mesa-dri`

從Google雲端下載訓練好的模型
`gdown https://drive.google.com/uc?id=1Ao1sFYhp1fvJ1dJMC6mn540VrFASXg8w`





pth: https://drive.google.com/file/d/1Ao1sFYhp1fvJ1dJMC6mn540VrFASXg8w/view?usp=sharing
