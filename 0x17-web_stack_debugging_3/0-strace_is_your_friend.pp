# Fichier : 0-strace_is_your_friend.pp

# Manifeste Puppet pour corriger une erreur 500
# d'Apache en modifiant wp-settings.php
# Autor : Said LAMGHARI

# Ressource pour corriger le problème
# en remplaçant 'phpp' par 'php' dans wp-settings.php

exec { 'fix_apache_error_Using_strace':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
