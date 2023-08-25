# using Puppet to install flask from pip-3 version 2.1.0
exec { 'install_flask_package' :
command => '/usr/bin/pip3 install flask==2.1.0',
}
