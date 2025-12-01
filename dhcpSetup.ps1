$name = Read-Host "Enter scope name"
$scopeStart = Read-Host "Enter Scope Start IP"
$scopeEnd = Read-Host "Enter Scope End IP"
$subnetMask = Read-Host "Enter Subnet Mask"
# Create DHCP Scope
Add-DhcpServerv4Scope -Name $name -StartRange $scopeStart -EndRange $scopeEnd -SubnetMask $subnetMask

# Exclusions
Add-DhcpServerv4ExclusionRange -ScopeId ($ScopeStart.Split('.')[0..2] -join ".")+".0" -StartRange $ExStart1 -EndRange $ExEnd1
Add-DhcpServerv4ExclusionRange -ScopeId ($ScopeStart.Split('.')[0..2] -join ".")+".0" -StartRange $ExStart2 -EndRange $ExEnd2

# Gateway
Set-DhcpServerv4OptionValue -ScopeId ($ScopeStart.Split('.')[0..2] -join ".")+".0" -Router $Gateway

# DNS Servers
Set-DhcpServerv4OptionValue -ScopeId ($ScopeStart.Split('.')[0..2] -join ".")+".0" -DnsServer $PrimaryDNS, $SecondaryDNS
