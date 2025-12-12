Install-WindowsFeature -Name AD-Domain-Services, DNS, DHCP -IncludeManagementTools

$name = Read-Host "Enter Domain Name" # Example: mc5644.com. NOT the full FQDN which is <hostname>.<rit-username>.com
$netbiosName = Read-Host "Enter Net BIOS Name" # Basically domain name but in all caps, without the .com

Import-Module ADDSDeployment
Install-ADDSForest `
-CreateDnsDelegation:$false `
-DatabasePath "C:\WINDOWS\NTDS" `
-DomainMode "Win2025" `
-DomainName "$name" `
-DomainNetbiosName "$netbiosName" `
-ForestMode "Win2025" `
-InstallDns:$true `
-LogPath "C:\WINDOWS\NTDS" `
-NoRebootOnCompletion:$false `
-SysvolPath "C:\WINDOWS\SYSVOL" `
-Force:$true