# Using Puppet, install `flask` from `pip3`.

package { 'flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
}
