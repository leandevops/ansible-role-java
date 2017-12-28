# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = 2

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  config.vm.define 'centos7' do |centos|
    centos.vm.box = 'centos/7'    
    config.vm.provider :virtualbox do |vb|
      vb.name = 'centos7'
    end
    config.vm.provision 'ansible' do |ansible|
    
      ansible.playbook = 'tests/test.yml'
      ansible.become = true
      ansible.galaxy_roles_path = '../'
      ansible.compatibility_mode = '2.0'
      # ansible.extra_vars = {
      #   container: false
      # }
      # ansible.raw_arguments = ["-vvvv"]
     
    end
  end

  config.vm.define 'ubuntu16' do |ubuntu|
    ubuntu.vm.box = 'ubuntu/xenial64'
    config.vm.provider :virtualbox do |vb|
      vb.name = 'ubuntu16'
    end
    config.vm.provision 'shell', inline: 'sudo apt-get update -y; sudo apt-get install -y python-minimal'
    config.vm.provision 'ansible' do |ansible|
    
      ansible.playbook = 'tests/test.yml'
      ansible.become = true
      ansible.galaxy_roles_path = '../'
      ansible.compatibility_mode = '2.0'
      # ansible.extra_vars = {
      #   container: false
      # }
      # ansible.raw_arguments = ["-vvvv"]     
    end
  end
  
end
