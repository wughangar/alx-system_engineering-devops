# manifest that fixes Apache is returning a 500 error

class apache_install {
package { 'apache2':
ensure => 'installed',
}

service { 'apache2':
ensure  => 'running',
enable  => true,
require => Package['apache2'],
}
}
