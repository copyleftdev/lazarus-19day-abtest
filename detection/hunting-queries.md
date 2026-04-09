# Lazarus 19-Day Campaign - Hunting Queries

## Splunk / SPL

### GitHub Notification Phishing via Google Share
```spl
index=proxy OR index=email
("share.google/" AND ("eGzdhAucWKKcwkZi9" OR "N3NwdcmyaYu9kwZ6D" OR "GVTYMEMANZWqTptr2"))
OR "token-claw.xyz"
OR "watery-compost.today"
OR "CVE-2026-40271"
| stats count by src_ip, dest, url, user
```

### BeaverTail/OtterCookie C2 Communication
```spl
index=network
(dest_ip IN ("147.124.213.232","147.124.212.125","216.250.251.87","147.124.214.129")
  AND dest_port IN (1244,5918))
OR (dest_ip IN ("172.86.105.40","172.86.116.178","86.106.85.234","144.172.104.117","144.172.101.45")
  AND dest_port=5918)
OR (dest_ip="66.235.168.238" AND dest_port IN (22411,22412))
OR dest_ip IN ("45.43.11.199","66.235.63.55","45.59.163.55")
| stats count by src_ip, dest_ip, dest_port, app
| sort -count
```

### Majestic Hosting Netblock (Lazarus Infrastructure)
```spl
index=network dest_ip="147.124.208.0/20"
| stats count values(dest_port) as ports by src_ip, dest_ip
| where mvcount(ports) > 3
```

### PylangGhost Persistence Artifacts
```spl
index=sysmon EventCode IN (1,11,12,13)
(
  (CommandLine="*NodeUpdate*" OR CommandLine="*NodeHelper*" OR CommandLine="*csshost.exe*")
  OR (TargetFilename="*nvidiaRelease*" OR TargetFilename="*chrome_logins_dump*" OR TargetFilename="*gather.tar.gz*")
  OR (TargetObject="*\\Run\\NodeHelper*")
)
| stats count by Computer, Image, CommandLine, TargetFilename
```

### Workspace Init Telemetry Exfiltration
```spl
index=proxy http_user_agent="VSCode-Workspace-Init*"
OR (index=sysmon EventCode=1 CommandLine="*init-workspace*" ParentImage="*\\Code.exe")
| stats count by src_ip, dest, url, CommandLine
```

### FTP Exfiltration to Known Lazarus Servers
```spl
index=network dest_port=21
dest_ip IN ("195.201.104.53","144.172.89.198","216.126.227.239")
| stats count sum(bytes_out) as total_exfil by src_ip, dest_ip
| sort -total_exfil
```

### Axios npm Supply Chain (CVE-2026-33634)
```spl
index=npm OR index=ci
("plain-crypto-js" OR "axios@1.14.1" OR "axios@0.30.4")
| stats count by host, source, user
```

## KQL (Microsoft Sentinel / Defender)

### Lazarus C2 Network Connections
```kql
DeviceNetworkEvents
| where RemoteIP in (
    "147.124.213.232","147.124.212.125","216.250.251.87",
    "172.86.105.40","172.86.116.178","66.235.168.238",
    "45.43.11.199","66.235.63.55","45.59.163.55",
    "195.201.104.53","144.172.89.198","216.126.227.239",
    "151.243.101.229"
  )
  or RemoteUrl has_any ("watery-compost.today","token-claw.xyz","360scanner.store","tetrismic.vercel.app")
| summarize count(), dcount(RemoteIP), make_set(RemotePort) by DeviceName, InitiatingProcessFileName
```

### PylangGhost/OtterCookie Persistence
```kql
union DeviceRegistryEvents, DeviceFileEvents, DeviceProcessEvents
| where (
    (RegistryValueName has_any ("NodeHelper","NodeUpdate") and RegistryKey has "\\Run")
    or (FileName has_any ("csshost.exe","update.vbs","nvidia.py","chrome_logins_dump.txt"))
    or (ProcessCommandLine has_any ("NodeUpdate","Windows Update Script","contagious-interview"))
  )
| project Timestamp, DeviceName, ActionType, FileName, ProcessCommandLine, RegistryKey
```

### VS Code Workspace Attack Detection
```kql
DeviceProcessEvents
| where InitiatingProcessFileName == "Code.exe"
  and FileName in~ ("node.exe","powershell.exe","cmd.exe","bash.exe")
  and ProcessCommandLine has_any ("init-workspace","collectTelemetry","sendToTracker","phishing-tracker")
| project Timestamp, DeviceName, ProcessCommandLine, AccountName
```

### Wallet Extension Data Theft
```kql
DeviceFileEvents
| where FolderPath has_any (
    "nkbihfbeogaeaoehlefnkodbefgpgknn",  // MetaMask
    "bfnaelmomeimhlpmgjnjophhpkkoljpa",  // Phantom
    "dmkamcknogkgcdfhhbddcghachkejeap",  // Keplr
    "fhbohimaelbohpjbbldcngcnapndodjp",  // Binance
    "cgeeodpfagjceefieflmdfphplkenlfk"   // Tonkeeper
  )
  and InitiatingProcessFileName !in~ ("chrome.exe","msedge.exe","brave.exe")
| project Timestamp, DeviceName, FolderPath, InitiatingProcessFileName
```

## Elastic / EQL

### Lazarus C2 Beacon Pattern
```eql
sequence by process.entity_id with maxspan=1h
  [network where destination.ip in (
    "147.124.213.232","147.124.212.125","216.250.251.87",
    "172.86.105.40","172.86.116.178","66.235.168.238"
  )]
  [network where destination.port in (1244, 5918, 22411, 22412)]
```

### Workspace Init -> Telemetry Exfil Chain
```eql
sequence by host.name with maxspan=30s
  [process where process.parent.name == "Code.exe"
    and process.name in ("node.exe","powershell.exe","bash.exe")]
  [network where destination.domain != null
    and not destination.domain in ("*.microsoft.com","*.github.com","*.npmjs.org")]
```

## Shodan / Censys Queries

### Lazarus Port Signature (Infrastructure Hunting)
```
# Shodan
port:1244 port:5918 org:"Majestic Hosting"

# Censys
services.port: 1244 AND services.port: 5918 AND autonomous_system.asn: 396073
```

### Z238 Binary Protocol Servers
```
# Shodan
port:22411 port:22412

# Censys
services.port: 22411 AND services.port: 22412
```

### BeaverTail Express.js on Non-Standard Port
```
# Shodan
port:1244 "Express" country:US org:"Majestic Hosting"
```

## VirusTotal Queries

### Known Hashes
```
content:{bb794019f8a63966e4a16063dc785fafe8a5f7c7553bcd3da661c7054c6674c7}
content:{c4fd45bb8c33a5b0fa5189306eb65fa3db53a53c1092078ec62f3fc19bc05dcb}
content:{c7ecf8be40c1e9a9a8c3d148eb2ae2c0c64119ab46f51f603a00b812a7be3b45}
content:{a179caf1b7d293f7c14021b80deecd2b42bbd409e052da767e0d383f71625940}
content:{ef04a839f60911a5df2408aebd6d9af432229d95b4814132ee589f178005c72f}
```

### Domain/IP Lookups
```
entity:domain domain:watery-compost.today
entity:domain domain:token-claw.xyz
entity:domain domain:360scanner.store
entity:ip ip:147.124.213.232
entity:ip ip:66.235.168.238
```
