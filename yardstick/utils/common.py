import os
import subprocess
import yaml

import config as CONF


def execute_command(cmd):
    exec_msg = "Executing command: '%s'" % cmd
    print exec_msg

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    results = iter(p.stdout.readline, b'')

    lines = [r.replace('\n', '') for r in results]

    p.stdout.close()

    return lines


def get_config(args):

    value = None
    if os.path.exists(CONF.CUSTOM_CONFIG_YAML_PATH):
        value = _get_para_from_yaml(args)

    if value is None:
        value = _get_para_from_py(args)

    if value is None:
        print 'parameter %s not found' % args

    return value


def _get_para_from_yaml(args):

    def func(a, b):
        if a is None:
            return None
        return a.get(b)

    with open(CONF.CUSTOM_CONFIG_YAML_PATH) as f:
        value = yaml.safe_load(f)
        value = reduce(func, args.split('.'), value)
        return value


def _get_para_from_py(args):
    param_list = args.split('.')

    param = reduce(lambda a, b: a + '_' + b.upper(), param_list, '')
    param = param[1:]

    try:
        value = getattr(CONF, param)
        return value
    except:
        return None

if __name__ == '__main__':
    # execute_command('source /etc/yardstick/openstack.creds')
    get_config('general.directories.dir_yardstick_con')
