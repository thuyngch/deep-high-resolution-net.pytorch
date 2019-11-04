# Installation

* Create pip environment:
```
cd ~/.virtualenvs
virtualenv -p python3.6 posehrnet
workon posehrnet
```

* Clone Git repository:
```
git clone git@github.com:antiaegis/deep-high-resolution-net.pytorch.git
cd deep-high-resolution-net.pytorch
```

* Install required packages:
```
pip install numpy cython opencv-python tqdm scikit-image onnx pandas pylint shapely scipy
pip install ipython jupyter jupyterlab
pip install tensorflow tensorboard tensorboardX
pip install torch torchvision
ipython kernel install --user --name=posehrnet
```

* Config the VSCode remember the last commit message:
```
echo "update" > .mycommitmsg.txt
git config --local commit.template .mycommitmsg.txt
printf "`git log -1 --pretty=%s`" > .gitmessage.txt
chmod +x .git/hooks/post-commit
```
