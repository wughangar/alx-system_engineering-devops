# confirm nginx is installed
package { 'nginx':
  ensure => 'installed',
}

# Modify Nginx configuration to add custom HTTP header
exec { 'configure_nginx':
  command => "sed -i '/listen 80 default_server;/a add_header X-Served-By \$HOSTNAME;' /etc/nginx/sites-available/default",
  require => Package['nginx'],
  notify  => Service['nginx'],
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
