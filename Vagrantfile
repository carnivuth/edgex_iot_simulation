Vagrant.configure('2') do |config|
  config.vm.box = 'ubuntu/jammy64'
  config.ssh.insert_key = true

  config.vm.provider "virtualbox" do |v|
    v.linked_clone = true
    v.memory = 6144
    v.cpus = 4
  end

  # edgex runtime node
  config.vm.define 'edgex-runtime' do |machine|
    machine.vm.hostname = 'edgex-runtime'
    machine.vm.network 'forwarded_port', id: 'ssh', host: 2221, guest: 22
    machine.vm.network 'forwarded_port', host: 59701, guest: 59701, protocol: "tcp"
    machine.vm.network 'forwarded_port', host: 59900, guest: 59900 , protocol: "tcp"
    machine.vm.network 'forwarded_port', host: 59986, guest: 59986, protocol: "tcp"
    machine.vm.network 'forwarded_port', host: 59880, guest: 59880, protocol: "tcp"
    machine.vm.network 'forwarded_port', host: 59882, guest: 59882, protocol: "tcp"
    machine.vm.network 'forwarded_port', host: 59861, guest: 59861, protocol: "tcp"
    machine.vm.network 'forwarded_port', host: 59860, guest: 59860, protocol: "tcp"
    machine.vm.network 'forwarded_port', host: 59881, guest: 59881, protocol: "tcp"
    machine.vm.network 'forwarded_port', host: 4000,  guest: 4000, protocol: "tcp"
    machine.vm.network 'forwarded_port', host: 59720, guest: 59720, protocol: "tcp"
    machine.vm.network 'forwarded_port', host: 6379,  guest: 6379, protocol: "tcp"
    machine.vm.network 'forwarded_port', host: 8500,  guest: 8500, protocol: "tcp"
    machine.vm.network 'private_network', virtualbox__intnet: 'ceph-cluster', ip: '10.0.0.10'
  end

  # port to forward
  # 48095/tcp, 127.0.0.1:59701->59701/tcp
  #127.0.0.1:->59900/tcp
  #127.0.0.1:->/tcp
  #127.0.0.1:59880->/tcp
  #127.0.0.1:59882->/tcp
  #127.0.0.1:59861->/tcp
  #127.0.0.1:59860->/tcp
  #127.0.0.1:59881->/tcp
  #9081/tcp, 20498/tcp, 127.0.0.1:->59720/tcp
  #0.0.0.0:4000->4000/tcp, :::4000->4000/tcp
  #127.0.0.1:6379->/tcp
  #8300-8302/tcp, 8301-8302/udp, 8600/tcp, 8600/udp, 127.0.0.1:8500->8500/tcp

  # iot nodes
  config.vm.define 'iot-node-1' do |machine|
    machine.vm.hostname = 'iot-node-1'
    machine.vm.network 'forwarded_port', id: 'ssh', host: 2222, guest: 22
    machine.vm.network 'private_network', virtualbox__intnet: 'ceph-cluster', ip: '10.0.0.20'
  end
  config.vm.define 'iot-node-2' do |machine|
    machine.vm.hostname = 'iot-node-2'
    machine.vm.network 'forwarded_port', id: 'ssh', host: 2223, guest: 22
    machine.vm.network 'private_network', virtualbox__intnet: 'ceph-cluster', ip: '10.0.0.30'
  end
  config.vm.define 'iot-node-3' do |machine|
    machine.vm.hostname = 'iot-node-3'
    machine.vm.network 'forwarded_port', id: 'ssh', host: 2224, guest: 22
    machine.vm.network 'private_network', virtualbox__intnet: 'ceph-cluster', ip: '10.0.0.40'
  end
end
