import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('command', [
    'java'
])
def test_java_binary(host, command):
    cmd = host.run('. /etc/profile && ' + command + ' -version')
    assert cmd.rc == 0
    assert '1.8.0_' in cmd.stderr


@pytest.mark.parametrize('version_dir_pattern', [
    '1\\.8\\.0_[0-9]+$'
])
def test_java_installed(host, version_dir_pattern):

    java_home = host.check_output(
                        'find `$JAVA_HOME` | grep --color=never -E %s',
                        version_dir_pattern)

    java_bin = host.file(java_home + '/bin/java')

    assert java_bin.exists
    assert java_bin.is_file
    assert java_bin.user == 'root'
    assert java_bin.group == 'root'
    assert oct(java_bin.mode) == '0755'
