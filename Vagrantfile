# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = 2

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = 'centos/7'  
    
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
