# whistab
Where Have I Seen This Actor|Actress Before - A simple application to answer a simple question

## Requirements
- Python `>=3.10.4`
- `pyenv`, `pyenv-virtualenv`
- `poetry`
- Vagrant
- VirtualBox

## Initial set up

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
