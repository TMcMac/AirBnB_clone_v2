#!/usr/bin/python3
"""creates a .tgz archive of contents of web_static dir"""
from datetime import datetime
from fabric.operations import local


def do_pack():
    """Fabric script that generates a .tgz archive"""

    dt = datetime.now()
    dtf = dt.strftime("%Y%m%d%H%M%S")
    name = "web_static_" + dt_format + ".tgz"
    local("mkdir -p versions")

    try:
        local('tar -cvzf versions/{} web_static'.format(name))
        path = 'versions/{}'.format(name)
        path = local('tar -cvzf versions/{} web_static'.format(name))
        return path
    except:
        return None
