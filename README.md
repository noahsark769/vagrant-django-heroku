# vagrant-django-heroku
A virtual environment for developing django apps for heroku deployment.

## Motivation
Setting up project dependencies can be complicated. I've had at least 5 or 6 projects where I needed to set up a django stack between 5 people with the intent to push to heroku. The motivation behind this repo is that it should provide a few files which you can paste in to your project, change the variables, and run `vagrant up` to get a working app.

## Installation
Copy the entire repo into your project.

(1) Change the variables at the top of `install.sh` to reflect your preferred database usernames and passwords.
```
    DATABASE_USERNAME="your_db_user"
    DATABASE_PASSWORD="your_password"
    DATABASE_NAME="your_db_name"
```

(2) Change the variables at the top of `vmanage.py`: the `extra_commands` variable lets you define commands to run before running any manage.py command on the virtual machine: for example, put `extra_commands = 'source /vagrant/.secret_keys;'` to source a file before running any `manage.py` command. Also, make the `manage_py_path` variable have the absolute path to `manage.py` on the *virtual* machine, like `/vagrant/manage.py` (this is the default and will work if you don't change anything in step (3).
```
other_commands = "source /vagrant/.secrets;" # note: the semicolon is important
manage_py_path = "/vagrant/my_app"
```

(3) By default, this configuration syncs the directory in which the `Vagrantfile` resides with the `/vagrant` folder on the virtual machine. If you'd like to change that, you can in the `Vagrantfile`. Note that you may have to change the `manage_py_path` variable in `vmanage.py` for everything to work if you do this.

(4) `vagrant up --provision`

(5) You should now be able to run `python manage.py migrate` (or substitue any command for the `migrate`) and the script will proxy it to the appropriate ssh command for the vagrant machine. The virtual machine will run an instance of postgres and install everything from your requirements.txt. Presto!

## Questions or contributing
This is mostly just a utility for me at the time of writing. If you'd like to use it also and you have some kind of question or would like to contribute to this repo, open and issue/pull request!
