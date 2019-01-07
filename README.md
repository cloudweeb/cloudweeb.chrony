Ansible: cloudweeb.chrony
=========

Role untuk konfigurasi service chrony client untuk linux server, based on [geerlingguy.ntp](https://github.com/geerlingguy/ansible-role-ntp/)

Requirements
------------

* Ansible >= 2.4

Role Variables
--------------

| Nama                      | Default Value |  Deskripsi |
|---------------------------|---------------|------------|
| chrony_timezone           | Asia/Jakarta  | Timezone server |
| chrony_area               | asia          | set ntp pool area |
| chrony_servers            | []            | set ntp pool server sesuai dengan pool area, default value ada di default.yml |

Dependencies
------------

None

Example Playbook
----------------

```YAML
- hosts: servers
  vars:
    chrony_area: europe
  roles:
    - cloudweeb.chrony
```

License
-------

MIT

Author Information
------------------

* [Agnesius Santo Naibaho](http://tosabyte.com/)
