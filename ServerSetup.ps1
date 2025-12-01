Install-WindowsFeature -Name AD-DomainServices, DNS, DHCP -IncludeManagementTools

$name = Read-Host "Enter Domain Name: "
$netbiosName = Read-Host "Enter Net BIOS Name: "

Import-Module ADDSDeployment
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