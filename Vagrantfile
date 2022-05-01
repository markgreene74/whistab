vm_name = "python-3-10-2-whistab"

Vagrant.configure("2") do |config|
  config.vm.provider :virtualbox
  config.vm.box = "debian/bullseye64"

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 1
    v.name = vm_name
  end

  config.vm.disk :disk, size: "10GB", primary: true
  config.vm.network :forwarded_port, guest: 80, host: 8000
  config.vm.network :forwarded_port, guest: 8080, host: 8080
  config.vm.hostname = vm_name
  config.vm.define vm_name

  config.vm.post_up_message = "Debian 11 (bullseye), Python 3.10, pyenv+pyenv-virtualenv, docker."

  config.vm.provision "base", type: "shell", path: "Vagrant-bootstrap.sh"
  config.vm.provision "custom", type: "shell", inline: "echo placeholder"

  config.vm.provision "docker" do |d|
    d.pull_images "hello-world"
#     d.run "hello-world"
#     d.post_install_provision "shell", inline:"echo export http_proxy='http://127.0.0.1:3128/' >> /etc/default/docker"
#     d.run "ubuntu",
#       cmd: "bash -l",
#       args: "-v '/vagrant:/var/www'"
  end

end