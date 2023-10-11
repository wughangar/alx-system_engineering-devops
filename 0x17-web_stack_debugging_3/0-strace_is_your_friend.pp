# manifest that fixes Apache is returning a 500 error

class { 'apache':
package_name => 'apache2',
service_name => 'apache2',
docroot      => '/var/www/html',
}

file { '/var/www/html/wp-settings.php':
ensure  => file,
owner   => 'www-data',
group   => 'www-data',
mode    => '0644',
require => Class['apache'],
}

service { 'apache2':
ensure  => running,
enable  => true,
require => [File['/var/www/html/wp-settings.php'], Class['apache']],
}
