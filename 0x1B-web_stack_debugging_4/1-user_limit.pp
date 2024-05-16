# Puppet manifest pour modifier la configuration du système
# d'exploitation afin d'augmenter la limite du nombre maximal
# de fichiers ouverts pour l'utilisateur holberton
# Autor SAID LAMGHARI

exec { 'change_user_limit':
  # Modifie la limite du nombre maximal
  # de fichiers ouverts pour l'utilisateur holberton
  command => 'ulimit -n 4096',
  # Commande à exécuter pour modifier la limite
  user    => 'holberton',
  # Utilisateur auquel appliquer la modification
}
