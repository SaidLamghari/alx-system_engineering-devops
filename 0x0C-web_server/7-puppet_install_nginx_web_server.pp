# Install Nginx web server (w/ Puppet)
# Autor : Said LAMGHARI

# Install PACK of Nginx
package { 'nginx':
  ensure => installed,
}

# Configure the server of Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
    server {
      listen 80;
      server_name _;
    
      location / {
        return 200 "Hello World!\n";
      }
    
      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }
    }
  ',
}

# Enable Nginx site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart of sercice Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
