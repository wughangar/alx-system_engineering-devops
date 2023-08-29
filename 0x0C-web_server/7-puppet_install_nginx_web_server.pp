#!/usr/bin/env bash
# 7-puppet_install_nginx_web_server.pp

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page.\n",
}

nginx::resource::vhost { 'default':
  www_root     => '/var/www/html',
  listen_port  => 80,
  redirect_from => '/redirect_me',
  redirect_to   => 'https://www.youtube.com',
}
