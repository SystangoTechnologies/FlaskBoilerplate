# APIs with Flask and MongoDB

### Setup 

## Installation in Ubuntu

  1. Install python3.7:
    `sudo apt install software-properties-common`
    `sudo add-apt-repository ppa:deadsnakes/ppa`
    `sudo apt-get update`
    `sudo apt-get install python3.7`

  2. Install pip:
    `sudo apt install python3-pip`

  3. Install pipenv:
    `pip3 install --user pipenv`

  4. Create virtual environment using pipenv:
    `pipenv shell --python python3.7`

  5. Activate virtual environment(Not necessary after step 4 but later its needed once environment is deactivated):
    `pipenv shell`

  6. Install requirements from pipfile.lock:
    `pipenv install`

**NOTE:** If you face below error on STEP 4

`pipenv: command not found` the follow the instructions in below link: https://www.ostechnix.com/pipenv-officially-recommended-python-packaging-tool/

**NOTE:** For ubuntu 18 LTS if you face below error on STEP 3

`Traceback (most recent call last):`
  `File "/usr/bin/pip3", line 9, in <module>`
    `from pip import main`
`ImportError: cannot import name 'main'`
 then run below command:
`bash --login` or follow https://superuser.com/questions/1432768/how-to-properly-install-pipenv-on-wsl-ubuntu-18-04


## Quick start

Run following command to start flask server:
    `python app.py`


## Running Tests

Run following command to run unit test cases:
    `pytest`

run below command to check test coverage:
    `pytest --cov=api --cov-report term-missing`
