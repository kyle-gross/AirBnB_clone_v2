#!/usr/bin/python3
"""first fabric script"""


from fabric.api import local, run, put, env
from datetime import datetime

def do_pack():
    """stuff"""
    env.abort_exception = FabricException
    time = datetime.now()
    arch_name = "web_static" + time.strftime("%Y:%M:%d:%H:%M:%S") + ".tgz"
    v_path = "versions/" + arch_name
    tzg = "tar -cvzf " + v_path + " web_static"
    try:
        local("mkdir -p versions")
        local(tzg)
        return v_path
    except FabricException:
        return None