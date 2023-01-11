# installing flask from pip3

#class mymodule::flask {
  package { 'flask':
    ensure => '2.1.0',
    provider => 'pip3',
  }
#}

#node 'mynode' {
 # include mymodule::flask
#}
