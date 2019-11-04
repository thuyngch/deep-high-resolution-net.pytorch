# Installation

* Create pip environment:
```
cd ~/.virtualenvs
virtualenv -p python3.6 posehrnet
workon posehrnet
```

* Clone Git repository:
```
git clone git@github.com:thuyngch/deep-high-resolution-net.pytorch.git
cd deep-high-resolution-net.pytorch
```

* Install required packages:
```
pip install numpy cython opencv-python tqdm scikit-image pandas pylint shapely scipy yacs json_tricks
pip install ipython jupyter jupyterlab
pip install tensorflow tensorboard tensorboardX
pip install torch torchvision onnx
python setup.py develop
ipython kernel install --user --name=posehrnet
```

* Build libraries:
```
cd lib/
make -j4
cd ../
```

* Install COCO API:
```
export COCOAPI=$HOME/thuync/cocoapi
git clone https://github.com/cocodataset/cocoapi.git $COCOAPI
cd $COCOAPI/PythonAPI
make install
```

* Config the VSCode remember the last commit message:
```
echo "update" > .mycommitmsg.txt
git config --local commit.template .mycommitmsg.txt
printf "`git log -1 --pretty=%s`" > .gitmessage.txt
chmod +x .git/hooks/post-commit
```
