# confirm nginx is installed
package { 'nginx':
  ensure => 'installed',
}

# http header response
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('my_module/nginx_config.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
