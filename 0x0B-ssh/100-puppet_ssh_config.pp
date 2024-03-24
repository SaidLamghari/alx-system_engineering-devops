######################################################################
# Puppet Manifest: 100-puppet_ssh_config.pp
# Autor: Said LAMGHARI

# TurnOff Pword authent. in SSH client config.

file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  content => "PasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
}
