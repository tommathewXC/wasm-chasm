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

The emsdk environment script will have to be sourced to be able to
build C/C++ source code with the emscripten toolchain. It is possible
to put the contents of this into bashrc or /etc/environment, but I'm
far too lazy to do that right now.

    cd setup
    source emsdk/emsdk_env.sh  --build=Release

## Running Web Pages

### Test Page

In order to run the test page start the web server on port 8081

    cd src
    make test
    cd ../server
    python3 test_server.py

Then open http://localhost:8081 in a browser

### Main Page

In order to run the main page start the web server on port 8080

    cd src
    make main
    cd ../server
    python3 server.py

Then open http://localhost:8080 in a browser