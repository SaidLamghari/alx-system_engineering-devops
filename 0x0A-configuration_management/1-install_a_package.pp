# Flask version 2.1.0 use pip
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
