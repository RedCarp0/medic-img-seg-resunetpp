# medic-img-seg-resunetpp


## File Structure
* Working Directory:
```
medic-img-seg-resunetpp/
├── 2d_from_3d.py
├── Data_Loader.pygi
├── datasets
│   ├── after_trans
│   └── origin
├── LICENSE
├── losses.py
├── Metrics.py
├── Models.py
├── ploting.py
├── README.md
├── requirements.txt
└── train_val.py
```
* Dataset Directory:
```
<datasets path>
├── after_trans
│   ├── test
│   ├── test_label
│   ├── train
│   └── train_label
└── origin
    ├── test
    ├── test_label
    ├── train
    └── train_label
```

## Getting Started
* Clone this repo
```
https://github.com/RedCarp0/medic-img-seg-resunetpp
```
* Install all dependencies
```
pip install -r requirements.txt
```
* Modified file path in `train_val.py`
```
t_data = '<your path>/medic-img-seg-resunetpp/datasets/after_trans/train/'
l_data = '<your path>/medic-img-seg-resunetpp/datasets/after_trans/train_label/'
test_image = '<your path>/medic-img-seg-resunetpp/datasets/after_trans/test/0001.jpg'
test_label = '<your path>/medic-img-seg-resunetpp/datasets/after_trans/test_label/0001.png'
test_folderP = '<your path>/medic-img-seg-resunetpp/datasets/after_trans/test/*'
test_folderL = '<your path>/medic-img-seg-resunetpp/datasets/after_trans/test_label/*'
```
* Run `train_val.py`

## Acknowledgement
* The code is modified from [this repository](https://github.com/bigmb/Unet-Segmentation-Pytorch-Nest-of-Unets)





