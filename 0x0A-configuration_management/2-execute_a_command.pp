# Using Puppet, create a manifest that kills a process named `killmenow`.

exec { 'pkill':
  path    => '/usr/bin/',
  command => 'pkill killmenow',
  returns => [0, 1]
}
