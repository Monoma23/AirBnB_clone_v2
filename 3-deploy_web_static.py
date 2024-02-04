#!/usr/bin/python3
""" Createing and distributing an archive to web servers,
using created function deploy and pack"""
from fabric.api import *
import os
from datetime import datetime
from fabric.decorators import runs_once

# do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['34.232.69.7', '18.209.179.17']


@runs_once
def do_pack():
    """Packing all contents in web_static directory
    a tar archive"""

    try:
        my_local("mkdir -p versions")
        my_time = datetime.now()
        date_string = '%Y%m%d%H%M%S'
        my_date = my_time.strftime(date_string)

        file_path = "versions/web_static_{}.tgz".format(my_date)
        my_local("tar -czvf {} web_static".format(file_path))
        return file_path

    except Exception:
        return None


def deploy():
    """pack + deploy all file """
    file_path = do_pack()
    if not file_path:
        return False

    run_cmd = do_deploy(file_path)
    return run_cmd


def do_deploy(archive_path):
    """Archivi,g distributor"""
    try:
        try:
            if os.path.exists(archive_path):
                arc_tgz = archive_path.split("/")
                arg_save = arc_tgz[1]
                arc_tgz = arc_tgz[1].split('.')
                arc_tgz = arc_tgz[0]

                """Uploadi,g archive to server"""
                put(archive_path, '/tmp')

                """Savi,g folder paths in variables"""
                uncomp_foldd = '/data/web_static/releases/{}'.format(arc_tgz)
                tmp_locationnn = '/tmp/{}'.format(arg_save)

                """running remote commands on thee server"""
                run('mkdir -p {}'.format(uncomp_foldd))
                run('tar -xvzf {} -C {}'.format(tmp_locationnn, uncomp_foldd))
                run('rm {}'.format(tmp_locationnn))
                run('mv {}/web_static/* {}'.format(uncomp_foldd, uncomp_foldd))
                run('rm -rf {}/web_static'.format(uncomp_foldd))
                run('rm -rf /data/web_static/current')
                run('ln -sf {} /data/web_static/current'.format(uncomp_foldd))
                run('sudo service nginx restart')
                return True
            else:
                print('File does not exist')
                return False
        except Exception as err:
            print(err)
            return False
    except Exception:
        print('Error')
        return False