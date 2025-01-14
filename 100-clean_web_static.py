#!/usr/bin/python3
"""
Module to deploy archive to webservers
"""
from fabric.api import *
from time import strftime
from os.path import isfile
import os

env.hosts = ['35.153.18.120', '34.203.77.73']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """Generate a .tgz archive"""
    when = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        archive_name = "versions/web_static_{}.tgz".format(when)
        local("tar -czvf {} web_static".format(archive_name))
        return (archive_name)
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploy archive to web server"""
    if not isfile(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        file_name = archive_name.split(".")[0]
        path = "/data/web_static/releases/{}/".format(file_name)
        symbolic_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(path))
        run("sudo tar -xzf /tmp/{} -C {}".format(archive_name, path))
        run("sudo rm /tmp/{}".format(archive_name))
        run("sudo mv {}web_static/* {}".format(path, path))
        run("sudo rm -rf {}web_static".format(path))
        run("sudo rm -rf {}".format(symbolic_link))
        run("sudo ln -s {} {}".format(path, symbolic_link))
        print("New version deployed!")
        return True

    except Exception:
        return False


def deploy():
    """Create and deploy an archive to web servers"""
    archive_path = do_pack()
    if archive_path:
        return (do_deploy(archive_path))
    return False


def do_clean(number=0):
    """Delete out-of-date archives"""
    number = 1 if int(number) == 0 else int(number)
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
