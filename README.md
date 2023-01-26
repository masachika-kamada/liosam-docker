# LIO-SAM Docker for Windows

This repository is for building a docker environment for [LIO-SAM](https://github.com/TixiaoShan/LIO-SAM) on windows

## usage

### Docker

```ps1
./build.ps1
./run.ps1
```

### Dataset

* Download from [Google Drive](https://drive.google.com/drive/folders/1gJHwfdHCRdjP7vuT556pv8atqrCJPbUq)
* Create a dataset directory and save the downloaded bag file in it.

### Run

* Start XLaunch with [config.xlaunch](https://github.com/masachika-kamada/liosam-docker/blob/main/config.xlaunch)
* An introduction to xlaunch is available [here](https://github.com/masachika-kamada/ros-docker-windows#preparation)

```bash
docker exec -it liosam-melodic bash
$ roslaunch lio_sam run.launch
$ rosbag play ./src/LIO-SAM/dataset/walking_dataset-004.bag -r 3
```
