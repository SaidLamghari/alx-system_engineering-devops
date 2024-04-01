# Autor: Said LAMGHARI
package { 'nginx':
  ensure => installed,
}

# Configure HTTP response header
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => present,
  content => "server_tokens off;\nadd_header X-Served-By $::hostname;",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart
service { 'nginx':
  ensure => running,
  enable => true,
}
