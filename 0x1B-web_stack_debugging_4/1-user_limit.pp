# Puppet manifest pour modifier la configuration du système
# d'exploitation afin d'augmenter la limite du nombre maximal
# de fichiers ouverts pour l'utilisateur holberton
# Autor SAID LAMGHARI

# Ouvrir un fichier sans message d'erreur.

exec {'change OS_sec_config':
  # Modification de la configuration de
  # sécurité du système d'exploitation
  command => "sed -i 's/holberton/foo/' /etc/security/limits.conf",
  # Commande pour ajouter une ligne spécifiant
  # la limite du nombre maximal
  # de fichiers ouverts pour l'utilisateur
  # holberton dans le fichier limits.conf
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
  # Chemin d'accès aux exécutables requis par la commande
}
