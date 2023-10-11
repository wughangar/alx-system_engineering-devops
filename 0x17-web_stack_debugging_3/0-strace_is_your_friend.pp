# manifest that dowloads apache to fix 500 error

exce{ 'fixing wordpress error':
command => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
}
