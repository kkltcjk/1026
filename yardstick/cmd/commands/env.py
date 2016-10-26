import os
import sys
import subprocess

from yardstick.utils import config as CONF
from yardstick.utils.common import get_config
from yardstick.utils.openstack import source_credentials

YARDSTICK_CONF_DIR = get_config('general.directories.dir_yardstick_conf')
RELENG_DIR = get_config('general.directories.dir_releng')


class Environment(object):
    '''

        Set of commands to prepare environment
    '''

    def __init__(self):
        self.installer_ip = os.getenv('INSTALLER_IP', 'undefined')
        self.installer_type = os.getenv('INSTALLER_TYPE', 'undefined')
        self.scenario = os.getenv('DEPLOY_SCENARIO', 'undefined')
        self.node = os.getenv('NODE_NAME', 'undefined')
        self.build_tag = os.getenv('BUILD_TAG', 'undefined')
        self.debug = os.getenv('CI_DEBUG', 'undefined')

    def do_prepare(self, args):
        print 'Start to prepare Environment'

        self._check_variables()

        self._create_directories()

        self._source_file()

    def _check_variables(self):

        if self.installer_ip == 'undefined':
            sys.exit('Missing INSTALLER_IP')

        if self.installer_type == 'undefined':
            sys.exit('Missing INSTALLER_TYPE')
        elif self.installer_type not in CONF.INSTALLERS:
            sys.exit('INSTALLER_TYPE is not correct')

    def _create_directories(self):
        if not os.path.exists(YARDSTICK_CONF_DIR):
            print 'Create yardstick conf path'
            os.makedirs(YARDSTICK_CONF_DIR)

    def _source_file(self):

        rc_file = get_config('general.file.creds')

        self._get_remote_rc_file(rc_file)

        print 'Start to source file'
        source_credentials(rc_file)

    def _get_remote_rc_file(self, rc_file):

        cmd = RELENG_DIR + "utils/fetch_os_creds.sh >file.log -d %s -i %s \
            -a %s" % (rc_file, self.installer_type, self.installer_ip)
        p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, shell=True)
        p.communicate()[0]

        if p.returncode != 0:
            print 'Failed to fetch credentials from installer'
