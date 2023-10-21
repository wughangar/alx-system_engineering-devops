# fixing nginx to avoid failed requeests

exec { 'increase nginx request limit':
  command  => 'sed -i "s/15/11000/g" /etc/default/nginx; sudo service nginx restart',
  provider => shell,
}
