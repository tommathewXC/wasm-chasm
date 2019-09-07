# Web Assembly experiments

This project is for some experiments in WebAssembly
connecting C++11 source to an HTML file + JS

## Requirements

    1. Ubuntu 18.04
    2. git
    3. Python (3.5+) Tornado WebServer
    4. Node (v10+)

## Setup

### One Time setup

Starting from the root directory of the project, do the following:

    cd setup
    ./install.sh
    
### Development setup

    cd setup
    source emsdk/emsdk_env.sh  --build=Release