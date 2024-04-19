# Using Puppet, install `flask` from `pip3`.

package { 'flask':
  exec => '/usr/bin/pip3 install Flask==2.1.0',
}
