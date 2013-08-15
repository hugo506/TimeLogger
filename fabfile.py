from fabric.api import *
from contextlib import contextmanager as _contextmanager

env.user = "captain"
env.activate = "source /home/captain/django_apps/django_env/bin/activate"
env.directory = "/home/captain/django_apps/TimeLogger"

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
    prepare_deploy()
    with cd(env.directory):
        run("git pull")

def restart_service():
    run("sudo supervisorctl restart django_app")

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
