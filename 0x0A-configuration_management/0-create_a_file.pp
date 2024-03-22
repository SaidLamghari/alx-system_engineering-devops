# Puppet Manifest: 0-create_a_file.pp
#
# This creates a file at /tmp/school.
# owner, group, and content. The text "I love Puppet".
# Author: Said Lamghari

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
