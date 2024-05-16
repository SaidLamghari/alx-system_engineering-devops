# Puppet manifest pour modifier la configuration du système
# d'exploitation afin d'augmenter la limite du nombre maximal
# de fichiers ouverts pour l'utilisateur holberton
# Autor SAID LAMGHARI

# Ouvrir un fichier sans message d'erreur.

file { '/etc/security/limits.conf':
  # Chemin du fichier de configuration à modifier
  ensure  => present,
  # Assure que le fichier existe

  content => template('your_module/limits.conf.erb'),
  # Contenu du fichier basé sur un modèle,
  # où 'your_module/limits.conf.erb' est le chemin vers le fichier modèle

  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  # Propriétaire, groupe et permissions du fichier
}

exec { 'reload_limits_conf':
  # Exécuter la commande pour recharger la configuration des limites
  command     => 'sysctl -p',
  # La commande pour recharger la configuration
  refreshonly => true,
  # Ne s'exécute que si une notification est reçue
}

