######################################################################
# Puppet Manifest: 100-puppet_ssh_config.pp
# Autor: Said LAMGHARI

# TurnOff Pword authent. in SSH client config.
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}

# Declare the file identity in SSH client config.
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#?IdentityFile',
}
