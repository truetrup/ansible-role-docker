import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_hosts_file(File):
    f = File('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_docker_is_installed(Package):
    docker = Package("docker-engine")
    assert docker.is_installed


def test_docker_started(Service):
    docker = Service("docker")
    assert docker.is_running
    assert docker.is_enabled
