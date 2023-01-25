docker run --init -it -d `
    -v ${PWD}/dataset:/root/catkin_ws/src/LIO-SAM/dataset `
    --name=liosam-melodic `
    liosam-melodic `
    bash
