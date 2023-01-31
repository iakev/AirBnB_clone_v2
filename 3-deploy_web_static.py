#!/usr/bin/python3
"""
Script to create and distribute an archive to my web servers using 
deploy function
"""
from datetime import datetime
from fabric.api import run, put, env, local
import os
env.user = "ubuntu"
env.hosts = ['18.204.5.6', '100.26.241.83']
env.key_filename = "/home/vagrant/.ssh/school"


def do_pack():
    """"
    A function to create a folder and an archive to store
    web_static folder contents
    """

    local("mkdir -p versions")
    date_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date_str)
    print("Packing web_static to {}".format(file_name))
    result = local("tar -cvzf {} web_static".format(file_name))
    if result.failed:
        return None
    else:
        return file_name

def do_deploy(archive_path):
    """
    uploads archives to web servers, ucompresses the archives
    deletes the archives
    """

    if os.path.exists(archive_path):
        result = put(archive_path, "/tmp/")
        if result.succeeded:
            name_with_ext = archive_path.replace("versions/", "")
            name_wto_ext = name_with_ext.replace(".tgz", "")
            result = run("mkdir -p /data/web_static/releases/{}"
                         .format(name_wto_ext))
            if result.succeeded:
                result = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
                             .format(name_with_ext, name_wto_ext))
                if result.succeeded:
                    result = run("mv -f /data/web_static/releases/{}/"
                                 "web_static/* /data/web_static/releases/{}"
                                 .format(name_wto_ext, name_wto_ext))
                    if result.succeeded:
                        result = run("rm /tmp/{}".format(name_with_ext))
                        if result.succeeded:
                            result = run("rm -rf /data/web_static/current")
                            if result.succeeded:
                                result = run("ln -s /data/web_static/releases/"
                                             "{} /data/web_static/current"
                                             .format(name_wto_ext))
                                if result.succeeded:
                                    print("New version deployed!")
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

def deploy():
    """
    function that calls do_pack and do_deploy to generate
    an archive and deploy it to the web servers
    """

    archive_path = do_pack()
    if archive_path:
        do_deploy(archive_path)