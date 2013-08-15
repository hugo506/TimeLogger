from fabric.api import local

def prepare_deploy():
    local("echo DEPLOYING APP TO PRODUCTION...")
    local("git add . && git commit")
    local("git push -u origin master")
