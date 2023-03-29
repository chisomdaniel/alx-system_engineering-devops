# Client configuration file with puppet

file_line { 'private_key':
  path   => '/etc/ssh/ssh_config',
  line   => '	HostKey ~/.ssh/school'
}

file_line { 'password_auth':
  path   => '/etc/ssh/ssh_config',
  line   => '	PasswordAuthentication no'
}
