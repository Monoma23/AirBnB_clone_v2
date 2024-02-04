#!/usr/bin/python3
""" Fabfile that creating .tgz archive from
 contents of web_static folder"""

# if __name__ == '__main__':
from fabric.api import local
from datetime import datetime


def do_pack():
    """Packing all contents in the web_static directory
    as tar archive"""

    try:
        local("mkdir -p versions")
        my_time = datetime.now()
        Mydate_string = '%Y%m%d%H%M%S'
        my_date = my_time.strftime(Mydate_string)

        file_path = "versions/web_static_{}.tgz".format(my_date)
        local("tar -czvf {} web_static".format(file_path))
        return file_path

    except Exception:
        return None