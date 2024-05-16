# Puppet manifeste pour corriger la configuration de Nginx afin d'avoir zéro requête échouée
# Auteur : SAID LAMGHARI

# Puppet manifest pour modifier le paramètre de limite maximale de fichiers ouverts
exec {'modify_max_open_files_limit':
  # Modifie la limite maximale de fichiers ouverts
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  # Commande pour modifier le fichier de configuration de Nginx
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
  # Chemin d'accès aux exécutables requis
}

# Redémarre le service Nginx
exec {'restart_nginx_service':
  # Commande pour redémarrer le service Nginx
  command => 'sudo service nginx restart',
  # Chemin d'accès aux exécutables requis
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}

