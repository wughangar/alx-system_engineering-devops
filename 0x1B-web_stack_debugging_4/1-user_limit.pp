#create the holberton user

user { 'holberton':
  ensure     => 'present',
  managehome => true,
  home       => '/home/holberton',
}

user { 'holberton':
  password   => 'holberton',
}

file { '/etc/sudoers.d/holberton':
  ensure  => 'file',
  content => "holberton ALL=(ALL) NOPASSWD: ALL\n",
  mode    => '0440',
  require => User['holberton'],
}

file { '/home/holberton':
  ensure => 'directory',
  owner  => 'holberton',
  group  => 'holberton',
  mode   => '0700',
}

file { '/home/holberton/somefile.txt':
  ensure  => 'file',
  owner   => 'holberton',
  group   => 'holberton',
  mode    => '0600',
  content => 'puppet content',
}
