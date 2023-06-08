# this fixes error in the file `wp-settings.php`
# replaces instances of `phpp` with `php` 

$edit = '/var/www/html/wp-settings.php'

exec { 'fix-apache':
  command => "sed -i 's/phpp/php/g' ${edit}",
  path    => '/usr/bin/:/bin/'
}
