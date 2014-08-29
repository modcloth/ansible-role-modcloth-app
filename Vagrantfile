# vim:filetype=ruby

dockercfg = File.expand_path('~/.dockercfg')
FileUtils.cp(dockercfg, './.dockercfg') if File.exists?(dockercfg)

Vagrant.configure('2') do |config|
  config.vm.box = 'modcloth/trusty64'

  config.vm.provision 'shell', path: '.vagrant-pre-provision.sh'
  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = 'example.yml'
    ansible.sudo = true
    ansible.verbose = 'vvvv'

    if ENV['ANSIBLE_RAW_ARGUMENTS']
      ansible.raw_arguments = %W(#{ENV['ANSIBLE_RAW_ARGUMENTS']})
    end
  end
end
