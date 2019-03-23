## Ansible Role: Java
[![Build Status](https://www.travis-ci.org/leandevops/ansible-role-java.svg?branch=master)](https://www.travis-ci.org/leandevops/ansible-role-java)

This role installs java on Linux servers (CentOS7/Ubuntu16).

### Requirements

None

### Role Variables

Available variables are listed below, along with default values:

The role installs openjdk by default unless 'install_oracle_java' parameter is set to True.

    install_oracle_java: false


Packages to install, set the version/development kit of Java to install:

    java_packages:
      - openjdk-8-jdk

The role will automatically set the `JAVA_HOME` environment variable.

### Dependencies

None

### Example

    - hosts: servers
      roles:
        - java

or put params needed inline::

    - hosts: servers
        roles:
            - { role: java, install_oracle_java: false }

or put in requirements.yml

    - src: git+git@github.com:lestex/ansible-role-java.git
           version: v1.3

### License
This code is released under the Apache 2.0 License. Please see [LICENSE](https://github.com/leandevops/ansible-role-java/blob/master/LICENSE) for more details.


### Author Information
Copyright © 2019 LeanDevops.
