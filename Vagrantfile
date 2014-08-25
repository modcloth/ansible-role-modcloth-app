# vim:filetype=ruby

Vagrant.configure('2') do |config|
  config.vm.box = 'ubuntu/trusty64'

  config.vm.provision 'shell', path: '.vagrant-pre-provision.sh'
  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = 'test.yml'
    ansible.sudo = true
    ansible.verbose = 'vvvv'
    ansible.extra_vars = {
      modcloth_app_docker_command: 'env',
      modcloth_app_docker_repo: 'busybox',
      modcloth_app_env: {
        'SLEEPYTIME' => '9999',
      },
    }

    if ENV['ANSIBLE_RAW_ARGUMENTS']
      ansible.raw_arguments = %W(#{ENV['ANSIBLE_RAW_ARGUMENTS']})
    end
  end
end
