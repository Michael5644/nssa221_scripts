Import-Module ActiveDirectory

$first = Read-Host "Enter First Name (ex: John)"
$last = Read-Host "Enter Last Name (ex: Smith)"
$sam = Read-Host "Enter SAMAccountName (ex: jsmith)"
$passwordPlain = Read-Host "Enter Password for the User"
$password = ConvertTo-SecureString $passwordPlain -AsPlainText -Force

$domain = (Get-ADDomain).DNSRoot
$userlogon = "$sam@$domain"

# Creates the user (standard domain user)
New-ADUser `
-Name "$first $last" `
-GivenName $first `
-Surname $last `
-SamAccountName $sam `
-UserPrincipalName $userlogon `
-AccountPassword $password `
-Enabled $true `
-ChangePasswordAtLogon $false `
-PasswordNeverExpires $true