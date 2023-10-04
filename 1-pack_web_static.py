#!/usr/bin/python3
"""
Module to generate a .tgz archive from the web_static folder
"""
from fabric.api import local
from time import strftime


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
