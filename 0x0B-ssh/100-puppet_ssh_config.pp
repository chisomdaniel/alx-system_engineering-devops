# Client configuration file with puppet

file_line { 'private_key':
  ensure => 'present',
  path   => './2-ssh_config',
  line   => 'HostKey ~/.ssh/school'
}

file_line { 'password_auth':
  ensure => 'present',
  path   => './2-ssh_confing',
  line   => 'PasswordAuthentication no'
}
