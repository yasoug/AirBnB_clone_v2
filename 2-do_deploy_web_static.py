#!/usr/bin/python3
"""
Module to deploy archive to webservers
"""
from fabric.api import *
from time import strftime
from os.path import isfile

env.hosts = ['34.229.67.35', '34.207.121.74']
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
