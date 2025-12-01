Install-WindowsFeature -Name AD-DomainServices, DNS, DHCP -IncludeManagementTools

Import-Module ADDSDeployment
Install-ADDSForest `
-CreateDnsDelegation:$false `
-DatabasePath "C:\WINDOWS\NTDS" `
-DomainMode "Win2025" `

$name = Read-Host "Enter Domain Name: "
-DomainName "$name" `

$netbiosName = Read-Host "Enter Net BIOS Name: "
-DomainNetbiosName "$netbiosName" `

-ForestMode "Win2025" `
-InstallDns:$true `
-LogPath "C:\WINDOWS\NTDS" `
-NoRebootOnCompletion:$false `
-SysvolPath "C:\WINDOWS\SYSVOL" `
-Force:$true