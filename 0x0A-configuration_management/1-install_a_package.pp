# Puppet Manifest: 1-install_a_package.pp
# Author: Said Lamghari
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
