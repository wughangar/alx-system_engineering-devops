# manifest that dowloads apache to fix 500 error

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => file('/var/www/html/wp-settings.php').content.gsub('.phpp', '.php'),
  notify  => Exec['Reload Apache'],
}

exec { 'Reload Apache':
  command     => 'systemctl reload apache2',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}
