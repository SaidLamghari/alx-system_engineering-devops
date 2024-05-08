# Fichier : 0-strace_is_your_friend.pp

# Manifeste Puppet pour corriger une erreur 500
# d'Apache en modifiant wp-settings.php
# Autor : Said LAMGHARI

# Ressource pour corriger le problème
# en remplaçant 'phpp' par 'php' dans wp-settings.php

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub("phpp", "php") %>'),
  notify  => Service['apache2'],
}

