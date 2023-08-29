#!/usr/bin/env bash
#  using Puppet to make changes to our configuration file

file { '/root/.ssh/config':
ensure  => present,
content => "Host 34.207.190.83\n IdentityFile ~/.ssh/school\n PasswordAuthentication no\n",}
