$domain = Read-Host "Enter Domain Name (example: abc1234.com)"
$username = Read-Host "Enter Domain Username (example: tuser)"
$fullUser = "$domain\$username"

$credentials = Get-Credential -UserName $fullUser -Message "Enter password for Domain User"

Add-Computer -DomainName gpavks.com -Credential $credentials

Restart-Computer