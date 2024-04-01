# For task #0,
# Automate the task
# creating a HTTP header response
# Puppet.
# 2-puppet_custom_http_response_header.pp

# Autor: Said LAMGHARI

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define header
$hostname = $::fqdn

# Configure Nginx and add header
file { '/etc/nginx/sites-available/default':
  ensure => present,
  mode => '0644',
  content => template('nginx/custom_header.erb'),
}

# Reload Nginx and  apply change
exec { 'nginx_reload':
  command => '/usr/sbin/service nginx reload',
  refreshonly => true,
}

# Restart
service { 'nginx':
  ensure => running,
  enable => true,
  require => [File['/etc/nginx/sites-available/default'], Exec['nginx_reload']],
}

