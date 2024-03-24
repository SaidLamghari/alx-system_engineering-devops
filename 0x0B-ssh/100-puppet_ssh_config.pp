######################################################################
# Puppet Manifest: 100-puppet_ssh_config.pp
# Autor: Said LAMGHARI

# TurnOff Pword authent. in SSH client config.

newfile { '/etc/ssh/ssh_config':
  ensure  => 'newfile',
  content => "PasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
}
