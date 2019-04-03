import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_package(host):
    p = host.package("chrony")
    assert p.is_installed


def test_service(host):
    if host.system_info.distribution == "debian":
        chrony = "chrony"
    elif host.system_info.distribution == "centos":
        chrony = "chronyd"

    s = host.service(chrony)
    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    s = host.socket("udp://127.0.0.1:323")
    assert s.is_listening
