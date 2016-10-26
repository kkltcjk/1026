import os
import subprocess


def source_credentials(rc_file):
    p = subprocess.Popen(". %s; env" % rc_file, stdout=subprocess.PIPE,
                         shell=True)
    output = p.communicate()[0]
    env = dict((line.split('=', 1) for line in output.splitlines()))
    os.environ.update(env)
    return env
