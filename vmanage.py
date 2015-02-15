import os
import sys

other_commands = ""

BASE_COMMAND = "vagrant ssh -c 'source ~/venv/bin/activate; " + other_commands + " cd /vagrant/members_only && %s'"

def print_and_run_system(cmd):
    print "[Exec] " + cmd
    os.system(BASE_COMMAND % cmd)

if __name__ == '__main__':
    if sys.argv[1] == 'runserver':
        if len(sys.argv) == 2:
            sys.argv.append('[::]:8000')
        else:
            sys.argv[2] = '[::]:' + sys.argv[2]
    print_and_run_system("python manage.py " + " ".join(sys.argv[1:]))