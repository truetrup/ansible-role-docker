docker
=========

Ansible role for install docker on Debian jessie or CentOS 7.


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ansible-role-docker }

Attention
----------------

Will be good previously update kernel to 4.x, because old kernels going with CentOS 7 and Debian jessie have some issues with aufs storage driver (switch to overlayfs not possible, because available from 3.18).


License
-------

GPLv2
