# Puppet Manifest: 1-install_a_package.pp
#
# This installs Flask using pip3 with the specified version.
#
# Requirements:
#   - Package: Flask
#   - Version: 2.1.0
#
# Author: Said Lamghari
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
