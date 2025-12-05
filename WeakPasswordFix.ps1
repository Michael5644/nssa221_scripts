# In case ServerAddUser fails due to the password being weak which leaves the account created, but locked
# Get-ADUser -Identity <samAccountName> -Properties Enabled <- Use this to verify the account exists and if it's disabled (Must exist to run this!)

Import-Module ActiveDirectory

$sam = Read-Host "Enter SAMAccountName of the user needing repair"
$newPasswordPlain = Read-Host "Enter NEW strong password for this user"
$newPassword = ConvertTo-SecureString $newPasswordPlain -AsPlainText -Force

Set-ADAccountPassword -Identity $sam -Reset -NewPassword $newPassword
Enable-ADAccount -Identity $sam
Add-ADGroupMember -Identity "Domain Admins" -Members $sam