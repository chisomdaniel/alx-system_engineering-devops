# Client configuration file with puppet

file_line { 'private_key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	HostKey ~/.ssh/school'
}

file_line { 'password_auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	PasswordAuthentication no'
}
