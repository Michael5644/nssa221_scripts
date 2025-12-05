Import-Module DHCPServer
Import-Module ActiveDirectory

$name = Read-Host "Enter scope name"
$scopeStart = Read-Host "Enter Scope Start IP" # xxx.xxx.xxx.1 (Usually, refer to instructions)
$scopeEnd = Read-Host "Enter Scope End IP" # xxx.xxx.xxx.254 (Usually, refer to instructions)
$subnetMask = Read-Host "Enter Subnet Mask" # Usually 255.255.255.0, length is 24 (This command does not need length)
$gateway = Read-Host "Enter Default Gateway IP" # Use PFSenses' gateway IP
$dnsPrimary = Read-Host "Enter Primary DNS IP" # Put the web server's IP in this section. NOT 127.0.0.1
$dnsSecondary = Read-Host "Enter Secondary DNS IP" # 8.8.8.8

$scopeID = ($scopeStart.Split('.')[0..2] -join ".") + ".0"

# Authorize DHCP
$serverIP = (Get-NetIPAddress -AddressFamily IPv4 | Select-Object -First 1).IPAddress
Add-DhcpServerInDC -DnsName $env:COMPUTERNAME -IPAddress $serverIP

# Create DHCP Scope
Add-DhcpServerv4Scope -Name $name -StartRange $scopeStart -EndRange $scopeEnd -SubnetMask $subnetMask

# Exclusions
Add-DhcpServerv4ExclusionRange -ScopeId $scopeID -StartRange $exStart1 -EndRange $exEnd1 # Excludes your gateway's IP ONLY. (PFsenses' gateway, write the same IP for both fields)
Add-DhcpServerv4ExclusionRange -ScopeId $scopeID -StartRange $exStart2 -EndRange $exEnd2 # The actual exclusion range. It can be something like: 192.168.1.1 to 192.168.1.10

# Gateway
Set-DhcpServerv4OptionValue -ScopeId $scopeID -Router $gateway

# DNS Servers
Set-DhcpServerv4OptionValue -ScopeId $scopeID -DnsServer $dnsPrimary, $dnsSecondary