docker run --init -it -d `
    -v ${PWD}/dataset:/root/catkin_ws/src/LIO-SAM/dataset `
    -v ${PWD}/config/params.yaml:/root/catkin_ws/src/LIO-SAM/config/params.yaml `
    -v ${PWD}/pcd:/root/catkin_ws/src/LIO-SAM/pcd `
    --name=liosam-melodic `
    liosam-melodic `
    bash
