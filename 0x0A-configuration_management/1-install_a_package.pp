# Puppet Manifest: 1-install_a_package.pp
#
# This installs Flask using pip3 with the specified version.
#
# Requirements:
#   - Package: Flask
#   - Version: 2.1.0
#
# Author: Said Lamghari

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin'],
  require => Package['python3-pip'],
}
