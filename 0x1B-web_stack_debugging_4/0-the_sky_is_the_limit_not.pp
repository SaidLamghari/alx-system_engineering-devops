# Puppet manifeste pour corriger la configuration de Nginx afin d'avoir zéro requête échouée
# Auteur : SAID LAMGHARI

exec { 'nginx_and_fix_limit_setting':
  # Commande pour modifier la configuration de Nginx et redémarrer le service
  command     => "sed -i 's/-n 15/-n 4096/' /etc/default/nginx && service nginx restart",
  # Vérifie si le fichier /etc/default/nginx existe et si la configuration par défaut contient "-n 15"
  onlyif      => 'test -e /etc/default/nginx && grep "-n 15" /etc/default/nginx',
  # Chemin d'accès aux exécutables requis par la commande
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
  # Ne s'exécute que lorsqu'il est notifié par une autre ressource
  refreshonly => true,
}
