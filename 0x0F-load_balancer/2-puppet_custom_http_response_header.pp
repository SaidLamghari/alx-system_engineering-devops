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

# Configure theNginx andlisten on port 80
file { '/etc/nginx/sites-available/default':
  ensure => present,
  replace => true,
  source => 'puppet:///modules/nginx/default',
}


# Create HTML file
file { '/var/www/html/index.html':
  ensure => present,
  content => 'Hello World!',
}


# Configure Redir.
file { '/etc/nginx/sites-available/default':
  ensure => present,
  mode => '0644',
  content => template('nginx/custom_redirect.erb'),
}


# Create 404 HTML file
file { '/var/www/html/404.html':
  ensure => present,
  content => "Ceci n'est pas une page",
}


# Configure Nginx to use 404 page
file { '/etc/nginx/sites-available/default':
  ensure => present,
  mode => '0644',
  content => template('nginx/custom_404.erb'),
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
