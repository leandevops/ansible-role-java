## Ansible Role: Java
[![Build Status](https://www.travis-ci.org/leandevops/ansible-role-java.svg?branch=master)](https://www.travis-ci.org/leandevops/ansible-role-java)

This role installs java on Linux servers (CentOS7/Ubuntu16).

### Requirements

None

### Role Variables

Available variables are listed below, along with default values:

The role installs openjdk by default unless 'install_oracle_java' parameter is set to True.

    install_oracle_java: False

For some reason packages that heavily dependent on java won't work well with openjdk (cassandra for example) so please consider using oracle version.

Packages to install, set the version/development kit of Java to install:

    java_packages:
      - java-1.8.0-openjdk

If set, the role will set the global environment variable `JAVA_HOME` to this value:

    java_home: "/opt/java"

### Dependencies

None

### Example

    - hosts: servers
      roles:
        - java

or put params needed inline::

    - hosts: servers
        roles:
            - { role: java, install_oracle_java: False }

or put in requirements.yml

    - src: git+git@github.com:lestex/ansible-role-java.git
           version: v1.3

### License

Apache 2

### Author Information

Andrey Larin
