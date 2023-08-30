# configurations usings puppet

file{'/root/.ssh/config':
  ensure  => file,
  content => "Host server\n
      IdentityFile ~/.ssh/school\n
      PasswordAuthentication no\n",
  require => File['/root/.ssh'],
}

file{'/root/.ssh':
  ensure => directory,
}

