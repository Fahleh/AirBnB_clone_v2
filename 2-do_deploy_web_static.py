#!/usr/bin/python3
"""
    A script that distributes an archive to your web servers,
    using the function do_deploy
"""
import os
from fabric.api import *


env.hosts = ["100.26.243.119", "34.203.38.86"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploys archive to servers"""
    if not os.path.exists(archive_path):
        return False

    output = []

    response = put(archive_path, "/tmp")
    output.append(response.succeeded)

    base_name = os.path.base_name(archive_path)
    if base_name[-4:] == ".tgz":
        name = base_name[:-4]
    newdir = "/data/web_static/releases/" + name
    run("mkdir -p " + newdir)
    run("tar -xzf /tmp/" + base_name + " -C " + newdir)

    run("rm /tmp/" + base_name)
    run("mv " + newdir + "/web_static/* " + newdir)
    run("rm -rf " + newdir + "/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s " + newdir + " /data/web_static/current")

    return True
