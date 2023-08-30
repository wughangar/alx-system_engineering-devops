# configurations usings puppet

file { '/root/.ssh':
  ensure => directory,
  mode   => '0700',
}

file{'/root/.ssh/config':
ensure  => file,
content => "Host server\n
      IdentityFile ~/.ssh/school\n
      PasswordAuthentication no\n",
}
