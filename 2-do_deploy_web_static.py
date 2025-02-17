#!/usr/bin/python3
# Fabfile distributing archive to a web server.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["34.232.69.7", "18.209.179.17"]


def do_deploy(archive_path):
    """Distributeing archive to a web server

    Args:
        archive_path (str):path of the archive to be distributed
    Returns:
        If the file doesnt exist at archive_path or an error occurs - False
        ifnot True
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    my_name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(my_name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(my_name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, my_name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(my_name, my_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(my_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(my_name)).failed is True:
        return False
    return True