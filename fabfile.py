from fabric.api import *
from contextlib import contextmanager as _contextmanager

env.user = "captain"
env.activate = "source /home/captain/Code/django_apps/django_env/bin/activate"
env.directory = "/home/captain/Code/django_apps/TimeLogger"
env.hosts = ["192.241.186.225"]

def prepare_deploy():
    local("echo ------------------------")
    local("echo DEPLOYING APP TO PRODUCTION")
    local("git add . && git commit")
    local("git push -u origin master")
    local("echo APP PUSHED TO PRODUCTION")
    local("echo ------------------------")

def commit(msg):
    local("git add . && git commit -am %s" % msg)

def deploy():
    #with cd(env.directory):
        run("git pull --rebase")
    restart_service()

def restart_service():
    run("sudo supervisorctl restart django_app")

def update_code():
    with cd(env.directory):
        run("git pull")

@_contextmanager
def virtualenv():
    with prefix(env.activate):
        with cd(env.directory):
            yield

def sync_data():
    local("python manage.py dumpdata > datadump.json")
    prepare_deploy()
    with virtualenv():
        run("git pull")
        run("python manage.py loaddata dumpdata.json")
    restart_service()
