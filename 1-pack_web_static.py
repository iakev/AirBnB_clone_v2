#!/usr/bin/python3
"""
A fabric script to generate a .tgz archive from the contents
of the web_static folder
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """"
    A function to create a folder and an archive to store
    web_static folder contents
    """

    local("mkdir -p versions")
    date_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_Static_{}.tgz".format(date_str)
    result = local("tar -cvzf versions/{} web_static".format(file_name))
    return "versions/{}".format(file_name) \
        if local("ls versions/{}".format(file_name)).succeeded else None
