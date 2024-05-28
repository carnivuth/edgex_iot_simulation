Vagrant.configure('2') do |config|
  config.vm.box = 'ubuntu/jammy64'
  config.ssh.insert_key = true

  # edgex runtime node
  config.vm.define 'edgex-runtime' do |machine|
    machine.vm.hostname = 'edgex-runtime'
    machine.vm.network 'forwarded_port', id: 'ssh', host: 2221, guest: 22
    machine.vm.network 'forwarded_port', id: 'ceph-console', host: 8443, guest: 8443
    machine.vm.network 'forwarded_port', id: 'http', host: 8080, guest: 80
    machine.vm.network 'private_network', virtualbox__intnet: 'ceph-cluster', ip: '192.168.0.10'
    machine.vm.disk :disk, name: 'storage-1', size: '10GB'
  end
  
  # port to forward
  # 48095/tcp, 127.0.0.1:59701->59701/tcp
  #127.0.0.1:59900->59900/tcp
  #127.0.0.1:59986->59986/tcp
  #127.0.0.1:59880->59880/tcp
  #127.0.0.1:59882->59882/tcp
  #127.0.0.1:59861->59861/tcp
  #
  #127.0.0.1:59860->59860/tcp
  #127.0.0.1:59881->59881/tcp
  #9081/tcp, 20498/tcp, 127.0.0.1:59720->59720/tcp
  #0.0.0.0:4000->4000/tcp, :::4000->4000/tcp
  #127.0.0.1:6379->6379/tcp
  #8300-8302/tcp, 8301-8302/udp, 8600/tcp, 8600/udp, 127.0.0.1:8500->8500/tcp

  # iot nodes
  config.vm.define 'iot-node-1' do |machine|
    machine.vm.hostname = 'iot-node-1'
    machine.vm.network 'forwarded_port', id: 'ssh', host: 2222, guest: 22
    machine.vm.network 'private_network', virtualbox__intnet: 'ceph-cluster', ip: '192.168.0.20'
    machine.vm.disk :disk, name: 'storage-2', size: '10GB'
  end
  config.vm.define 'iot-node-2' do |machine|
    machine.vm.hostname = 'iot-node-2'
    machine.vm.network 'forwarded_port', id: 'ssh', host: 2223, guest: 22
    machine.vm.network 'private_network', virtualbox__intnet: 'ceph-cluster', ip: '192.168.0.30'
    machine.vm.disk :disk, name: 'storage-3', size: '10GB'
  end
  config.vm.define 'iot-node-3' do |machine|
    machine.vm.hostname = 'iot-node-3'
    machine.vm.network 'forwarded_port', id: 'ssh', host: 2224, guest: 22
    machine.vm.network 'private_network', virtualbox__intnet: 'ceph-cluster', ip: '192.168.0.40'
    machine.vm.disk :disk, name: 'storage-4', size: '10GB'
  end
end
