# fixing nginx to avoid failed requeests

exec { 'increase nginx request limit':
  command  => 'echo "worker_connections 4096;" > /etc/nginx/nginx.conf && sudo service nginx restart',
  provider => shell,
}
