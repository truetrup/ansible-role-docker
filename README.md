docker
=========

Ansible role for install docker on Debian jessie or CentOS 7.


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ansible-role-docker }

Variables and defaults
----------------

docker_tls: False - support for tls on 2376 port
docker_version: 17.05.0 - version of docker package to install
docker_pip_version: 9.0.1 - version of pip to install
dockerpy_version: 1.7.0 - version of docker-py python module

Attention
----------------

Will be good previously update kernel to 4.x, because old kernels going with CentOS 7 and Debian jessie have some issues with aufs storage driver (switch to overlayfs not possible, because available from 3.18).


License
-------

GPLv2
