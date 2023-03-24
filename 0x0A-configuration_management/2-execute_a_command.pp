# install a package

exec { 'pkill':
  command => '/usr/bin/pkill killmenow'
}
