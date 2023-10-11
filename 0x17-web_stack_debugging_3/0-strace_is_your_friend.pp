# manifest that dowloads apache to fix 500 error

exec{ 'fixing wordpress error':
command  => 'echo "$(cat /var/www/html/wp-settings.php | sed "s/.phpp/.php/")" > /var/www/html/wp-settings.php',
provider => shell
}
