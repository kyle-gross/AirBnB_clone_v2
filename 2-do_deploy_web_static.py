#!/usr/bin/python3
"""first fabric script"""


from fabric.api import local, run, put, env
from datetime import datetime
import os.path

env.hosts = ["54.242.225.135", "3.92.27.64"]


def do_deploy(archive_path):
    """deploys contetnt to servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        path_file = archive_path[9:]
        path_file_no_extension = path_file[:-4]
        new_dir = "/data/web_static/releases/" + path_file_no_extension + "/"
        put(archive_path, "/tmp/" + path_file)
        run("mkdir -p " + new_dir)
        run("tar -xzvf /tmp/" + path_file + " -C " +
            new_dir + " --strip-components=1")
        run("rm -f /tmp/" + path_file)
        run("mv " + new_dir + "web_static/* " + new_dir)
        run("rm -rf " + new_dir + "web_static")
        run("rm -rf /data/web_static/current")
        run("sudo ln -s " + new_dir + " /data/web_static/current")
        return True
    except:
        return False


def do_pack():
    """stuff"""
    time = datetime.now()
    arch_name = "web_static_" + time.strftime("%Y%M%d%H%M%S") + ".tgz"
    v_path = "versions/" + arch_name
    tzg = "tar -cvzf " + v_path + " web_static"
    try:
        local("mkdir -p versions")
        local(tzg)
        return v_path
    except:
        return None
