Ansible Role Chrony
=========

[![Build Status](https://travis-ci.com/cloudweeb/cloudweeb.chrony.svg?branch=master)](https://travis-ci.com/cloudweeb/cloudweeb.chrony)

Ansible role to install Chrony service on Linux servers.

Requirements
------------

None

Role Variables
--------------

| Variable            | Default Value         | Description                               |
|---------------------|-----------------------|-------------------------------------------|
| chrony_timezone     | Asia/Jakarta          | Timezone that wants to be set on a server |
| chrony_area         | asia                  | Chrony public server region               |
| chrony_servers      | []                    | Chrony public server                      |
| chrony_service_name | chronyd               | Chrony service name                       |
| chrony_driftfile    | /var/lib/chrony/drift | file location that stores drift files     |
| chrony_config_path  | /etc/chrony.conf      | Chrony config file location               |


Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: cloudweeb.chrony

License
-------

BSD/MIT

Author Information
------------------

Agnesius Santo Naibaho
