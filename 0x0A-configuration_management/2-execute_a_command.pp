# Puppet Manifest: 2-execute_a_command.pp
#
# This kills a process named "killmenow"
# using the exec resource and pkill command.
# Author: Said Lamghari

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/bin',
  onlyif  => 'pgrep -f killmenow',
}
