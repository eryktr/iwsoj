# iwsoj
Intelligent Web-Based Scalable Online Judge

## Brief Overview
**iwsoj** is a web app hosting a set of coding exercises. It is equipped with its own solution validator (container-based machine able to compile and execute code and match it against expected results). The backend is written using **Django**. The frontend uses **JavaScript**.

## Docs
Docs are generated using **Sphinx**. To build, you need to have it installed. Then,

    cd doc
    make html

## Environment setup
Create a new python virtual environment (requires python >= 3.7) and install deps

    python3 -m venv env
    source env/bin/activate
    pip3 install -r requirements.txt
    

## Tests
Tests were written using **pytest**. In order to run them:

    pytest -m "not integration"
    
Integration tests take a lot more of time for they run docker.

    pytet -m "integration"
    
