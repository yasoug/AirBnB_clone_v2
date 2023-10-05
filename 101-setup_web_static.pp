# Set up web servers for the deployment of web_static using Puppet

exec { 'update':
  command => 'apt-get update',
  provider => shell,
}

-> exec { 'install':
  command => 'apt-get -y install nginx',
  provider => shell,
}

-> exec { 'create_shared':
  command => 'mkdir -p /data/web_static/shared/',
  provider => shell,
}

-> exec { 'create_test':
  command => 'mkdir -p /data/web_static/releases/test/',
  provider => shell,
}

}
-> exec { 'Madara':
  command => 'echo "Wake up to Reality" > /data/web_static/releases/test/index.html',
  provider => shell,
}

-> exec { 'simlink':
  command => 'ln -sfn /data/web_static/releases/test /data/web_static/current',
  provider => shell,
}

-> exec { 'permission':
  command => 'chown -R ubuntu:ubuntu /data/',
  provider => shell,
}

-> exec { 'changes':
  command => 'sudo sed -i "s|server_name _;|server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}|" /etc/nginx/sites-enabled/default',
  provider => shell,
}

-> exec { 'restart':
  command => 'sudo service nginx restart',
  provider => shell,
}
