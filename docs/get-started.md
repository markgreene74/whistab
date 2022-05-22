# Create a development environment

It is possible to use [Vagrant](#vagrant) or [pyenv](#pyenv) to create the environment.

After creating the environment continue with [Install the requirements](#install-the-requirements).

## Vagrant

- move to the project directory
    ```bash
    cd whistab
    ```

- create the Vagrant box
    ```bash
    vagrant up 2>&1 | tee -a $(date +%F)-vagrant-up.log
    ```

- wait until the Vagrant box is up, then
    ```bash
    vagrant ssh
    ```

- go to the next section to [install the requirements](#install-the-requirements)

## Pyenv

- install `pyenv` ([documentation](https://github.com/pyenv/pyenv#installation)) and `pyenv-virtualenv` ([documentation](https://github.com/pyenv/pyenv-virtualenv#installation))


- install Python `3.10.4`
  ```bash
  pyenv install 3.10.4
  ```

- create a virtual environment
  ```bash
  pyenv virtualenv 3.10.4 whistab-3-10-4
  ```

- activate the virtual environment
  ```bash
  pyenv activate whistab-3-10-4
  ```

- go to the next section to [install the requirements](#install-the-requirements)

# Install the requirements

Make sure to install the requirements in the development environment. Run `pip` while the `pyenv-virtualenv` is active, or while logged in on the Vagrant box).

- update `pip`
  ```bash
  pip install --upgrade pip
  ```

- install the requirements
  ```bash
  pip install -r requirements.txt
  ```
