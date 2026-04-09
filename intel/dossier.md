# Lazarus Group 19-Day A/B Test: Deep Research Dossier

**Date:** 2026-04-08
**Original Research:** [@toxy4ny (KL3FT3Z)](https://github.com/toxy4ny) — Red Team Lead @ [Hackteam.Red](https://hackteam.red)
**Enrichment Sources:** VulnGraph (343K+ CVEs), GitHub API, OSINT web collection, Vajra structural analysis

---

## Executive Summary

Between March 20 and April 8, 2026, a threat actor attributed to **Lazarus Group (G0032)** executed a three-wave social engineering campaign against GitHub developers, each wave testing a different psychological trigger (greed, fear, ambition) against the same target pool. The campaign abuses GitHub's notification pipeline and Google Share redirects to bypass email security controls.

This dossier extends the original researcher's findings with:
- **CVE validation**: `CVE-2026-40271-64398` confirmed fabricated across MITRE, NVD, and VulnGraph (343K CVE database)
- **Attack surface mapping**: 217 real CVEs affect the OpenClaw npm package, including 11 CRITICAL and 91 HIGH severity
- **C2 infrastructure correlation**: Links to Contagious Interview infrastructure documented by Red Asgard
- **ATT&CK mapping**: 119 technique/software relationships for Lazarus Group (G0032) from VulnGraph graph
- **Supply chain context**: Connection to the axios npm compromise (CVE-2026-33634, CVSS 9.4, KEV-listed, WEAPONIZED)

---

## Campaign Timeline

```
2026-03-20  Wave 1: OpenClaw Airdrop         [GREED]   --> Wallet drainer
     |      7-day gap
2026-03-27  Wave 2: Fake VS Code CVE         [FEAR]    --> Malware dropper
     |      12-day gap
2026-04-08  Wave 3: Uniswap Recruitment      [AMBITION]--> GolangGhost/ClickFix
```

All three waves share:
- **Delivery**: GitHub discussion mass-mention -> `notifications@github.com` email -> Google Share redirect
- **Target pool**: Same developer community (researcher `@toxy4ny` appears in all three)
- **Infrastructure pattern**: Abuse of legitimate platforms (GitHub, Google) for initial delivery

---

## Wave 1: OpenClaw Airdrop (2026-03-20)

| Attribute | Value |
|-----------|-------|
| Psychological vector | Greed / FOMO |
| Lure | "5000.11 $CLAW allocation" — fake airdrop for OpenClaw contributors |
| Redirect | `share.google/eGzdhAucWKKcwkZi9` |
| Landing | `token-claw.xyz` (clone of openclaw.ai with wallet-connect injection) |
| C2 | `watery-compost.today` |
| Payload | `eleven.js` — obfuscated JS wallet drainer |
| Attacker wallet | `0x6981E9EA7023a8407E4B08ad97f186A5CBDaFCf5` (zero transactions at discovery) |
| Targeting | GitHub users who starred OpenClaw repositories |
| Status | **Sinkholed** |

### eleven.js Capabilities
- Heavy obfuscation for static analysis evasion
- Real-time command monitoring: `PromptTx`, `Approved`, `Declined` tracking
- **"Nuke" function**: Wipes `localStorage` to destroy forensic evidence
- C2 communication to `watery-compost.today` for wallet data exfiltration

### Why OpenClaw Is a Perfect Impersonation Target

The OpenClaw ecosystem has massive attack surface, making it ideal for social engineering:
- **138 CVEs tracked** across OpenClaw and predecessors (7 Critical, 49 High)
- **42,000+ instances** exposed on the public internet (Shodan)
- **63%** running with gateway authentication disabled
- **824+ malicious ClawHub skills** identified (12% of all skills)
- **CVE-2026-25253** (CVSS 8.8): RCE via WebSocket — visiting a malicious webpage compromises any running OpenClaw instance

The OpenClaw npm package alone has **217 real CVEs** — making it a high-value impersonation target:
- 11 CRITICAL severity (top: CVE-2026-28446, CVE-2026-28466, CVE-2026-28470)
- 91 HIGH severity
- 62 distinct CWE classes: CWE-863 (Authorization) x32, CWE-22 (Path Traversal) x23, CWE-78 (OS Command Injection) x20
- Only 6 of 217 have known PoC exploits

---

## Wave 2: Fake VS Code CVE (2026-03-27)

| Attribute | Value |
|-----------|-------|
| Psychological vector | Fear / Urgency |
| Lure | Fake critical VS Code vulnerability requiring immediate update |
| Redirect | `share.google/N3NwdcmyaYu9kwZ6D` |
| Fake CVE | `CVE-2026-40271-64398` |
| Fake researcher | "Nathaniel Pemberton, Precision Algorithmics" |
| Claimed versions | `1.05.0 - 1.112.4` (VS Code ~1.98.x at time; 1.112.x does not exist) |
| Target platform | Microsoft Windows only |
| Status | **Active** |

### Fake CVE Validation (VulnGraph + MITRE)

| Database | Result |
|----------|--------|
| VulnGraph (343,460 CVEs) | **Not found** |
| MITRE CVE List | **Not found** |
| NVD | **Not found** |
| GitHub Issues | **No results** |

**Format anomalies:**
- CVE IDs use format `CVE-YYYY-NNNNN` (4-7 digits). The suffix `-64398` after the sequence number is non-standard
- Claimed affected version `1.112.4` is far beyond any released VS Code version
- "Precision Algorithmics" is a real company but has no affiliation with this advisory

### Attacker GitHub Account (Burned)

The phishing was executed by GitHub account **AnalogIguana** using a typosquatted repo:
- **Repo**: `AnalogIguana/0penCIawSupport-6923876` (note: `0pen` with zero, `CIaw` with capital I)
- **Discussion URL**: `github.com/AnalogIguana/0penCIawSupport-6923876/discussions/4`
- **Account created**: ~1 week before campaign
- **Account status**: **Deleted** (404 as of 2026-04-08) — confirming burn-after-use pattern
- **Reported via**: [openclaw/openclaw#49836](https://github.com/openclaw/openclaw/issues/49836) and [#49861](https://github.com/openclaw/openclaw/issues/49861)

### Connection to StoatWaffle Campaign
In March 2026, [The Hacker News reported](https://thehackernews.com/2026/03/north-korean-hackers-abuse-vs-code-auto.html) that North Korean actors were abusing VS Code `tasks.json` auto-run to deploy **StoatWaffle** malware — a direct parallel to this wave's VS Code urgency lure. Microsoft introduced `task.allowAutomaticTasks` (disabled by default) in VS Code 1.109 (January 2026) as a direct countermeasure.

---

## Wave 3: Uniswap Recruitment (2026-04-08)

| Attribute | Value |
|-----------|-------|
| Psychological vector | Ambition / Career |
| Lure | $300,000-$450,000 remote blockchain developer position at "Uniswap" |
| Redirect | `share.google/GVTYMEMANZWqTptr2` |
| Impersonated company | Uniswap |
| Expected payload | GolangGhost / PylangGhost via ClickFix interview |
| Status | **Active** |

### Linguistic Red Flags
- "Every roles are fully online" — grammatical error consistent with non-native English
- Excessive salary range ($300K-$450K for a remote role)
- Pattern matches Operation Dream Job and ClickFake Interview campaigns

### Kill Chain (Projected from Related Campaigns)
```
GitHub mention -> Email notification -> Google Share redirect
    -> Fake recruiter landing page -> Skills assessment
    -> Video interview (ClickFix technique) -> Terminal command
    -> GolangGhost/PylangGhost RAT deployment
```

---

## Infrastructure Analysis

### Google Share Abuse
All three waves use `share.google/*` redirects because:
- Whitelisted by email security filters (Google domain)
- SSL/TLS encryption appears "secure" to victims
- Redirects to attacker infrastructure after initial hop
- No preview or warning on redirect

### GitHub Notification Pipeline Abuse
[GitHub Community Discussion #190675](https://github.com/orgs/community/discussions/190675) documents this structural exploit:
- Attackers create discussions and mass-mention thousands of users
- Triggers automated emails from `notifications@github.com` (legitimate sender)
- ~2.89% of GitHub emails on Feb 17, 2026 were attributed to this abuse pattern
- Phishing arrives from a trusted address — bypasses all standard email security

### Contagious Interview C2 Infrastructure (Red Asgard Research)

Related Lazarus C2 infrastructure documented by Red Asgard:

**Stage 1 — Vercel Distribution:**
| Domain | Endpoint | Token |
|--------|----------|-------|
| `task-hrec.vercel.app` | `/task/linux?token=` | `f93a38103457` |
| `kb102531x.vercel.app` | `/api/x` | `bc7302f71ff3` |
| `brantwork.vercel.app` | `/c/{token}` | `bc7302f71ff3` |

**Stage 2 — Dedicated C2 (Majestic Hosting AS396073):**
- `147.124.213.232` (WR232)
- `147.124.212.125` (W9_125)
- `216.250.251.87` (WIN-8OA3CCQAE4D)

**Stage 2 — Secondary (TIER-NET AS397423):**
- `45.43.11.199` (WIN-4MOD9QVI0EN)
- `66.235.63.55` (MetaMask Injector)
- `66.235.168.238` (Z238, custom binary protocol on ports 22411-22412)
- `45.59.163.55` (PS55)

**FTP Exfil Servers:**
- `195.201.104.53`, `144.172.89.198`, `216.126.227.239`

**Payload Endpoints:**
| Endpoint | Module | Purpose |
|----------|--------|---------|
| `/c/{token}` | Chrome stealer | Browser credential extraction |
| `/j/{token}` | Extended stealer | Wallet application targeting |
| `/n/{token}` | Network module | RAT + data exfiltration |
| `/dd/{token}` | MetaMask injector | Extension hijacking |
| `/bro/{token}` | Tsunami backdoor | Full RAT + XMRig miner |

**Encryption Keys (XOR/Symmetric):**
| Key | Purpose |
|-----|---------|
| `G01d*8@(` | File encryption |
| `G0Md*8@(` | Network module |
| `Vw1aGYoP` | Base85 layer |
| `!!!HappyPenguin1950!!!` | Tsunami URL encoding |
| `Xt3rqfmL` | Client/payload module |
| `Ze4pq4iT` | MetaMask injector |
| `0xcb` | Z238 binary protocol XOR |

**Timing Oracle:** Valid tokens respond ~400ms; invalid tokens ~6000ms (15x differential enables enumeration).

---

## Malware Families

### GolangGhost
- Go-based RAT; C2 via HTTP/HTTPS
- Targets browser data and cryptocurrency wallets
- Deployed via ClickFix social engineering (fake CAPTCHA -> clipboard-injected terminal command)
- [Malpedia entry](https://malpedia.caad.fkie.fraunhofer.de/details/win.golangghost)

### PylangGhost
- Python reimplementation of GolangGhost, likely AI-assisted (Go-like logic patterns, commented-out sections)
- Targets crypto workers through fake job sites
- [Cisco Talos analysis](https://www.mexc.com/news/cisco-talos-new-north-korean-threat-pylangghost-targets-crypto-workers-through-fake-job-sites/12514)

### StoatWaffle
- Deployed via malicious VS Code `tasks.json` auto-run
- Uses `"runOn": "folderOpen"` to trigger on workspace open
- Mitigated by VS Code 1.109+ (`task.allowAutomaticTasks` disabled by default)

### WAVESHAPER (axios compromise)
- Injected via `plain-crypto-js@4.2.1` trojan dependency in axios@1.14.1 / @0.30.4
- Postinstall lifecycle hook execution
- **CVE-2026-33634**: CVSS 9.4 CRITICAL, KEV-listed, WEAPONIZED, CWE-506 (Embedded Malicious Code)

---

## MITRE ATT&CK Mapping

### Techniques Observed in This Campaign

| ID | Technique | Evidence |
|----|-----------|----------|
| T1566.001 | Spearphishing Attachment | Fake security advisories |
| T1566.002 | Spearphishing Link | Google Share redirect URLs |
| T1566.003 | Spearphishing via Service | GitHub notification abuse |
| T1204.002 | User Execution: Malicious File | eleven.js, ClickFix terminal commands |
| T1027.009 | Obfuscated Files: Embedded Payloads | eleven.js obfuscation |
| T1027.013 | Obfuscated Files: Encrypted/Encoded | XOR encryption, Base85 layers |
| T1036.005 | Masquerading: Match Legitimate Name | Fake CVE, fake Uniswap |
| T1056.001 | Input Capture: Keylogging | Wallet credential capture |
| T1555 | Credentials from Password Stores | Browser/wallet targeting |
| T1573.001 | Encrypted Channel: Symmetric | XOR keys for C2 comms |
| T1102.001 | Web Service: Dead Drop Resolver | Pastebin dead drops |
| T1048.003 | Exfiltration Over Alternative Protocol | FTP exfiltration |
| T1547.001 | Boot/Logon Autostart Execution | "Windows Update Script.pyw", Scheduled Tasks |
| T1588.004 | Obtain Capabilities: Digital Certs | SSL certs for C2 domains |
| T1587.001 | Develop Capabilities: Malware | GolangGhost, PylangGhost, StoatWaffle |

### Full Lazarus Group (G0032) Arsenal from VulnGraph
119 total relationships mapped: 26 known software tools, 24 ATT&CK techniques including:
- T1053.005 (Scheduled Task), T1047 (WMI), T1033 (System Owner Discovery)
- T1218.011 (Rundll32), T1132.001 (Standard Encoding), T1561.002 (Disk Wipe)
- T1560.003 (Archive via Custom Method), T1542.003 (Bootkit)
- T1074.001 (Local Data Staging), T1489 (Service Stop)
- T1543.003 (Windows Service), T1021.004 (SSH), T1574.001 (DLL Search Order Hijacking)
- T1553.002 (Code Signing)

---

## CWE-506: Embedded Malicious Code — Supply Chain Context

VulnGraph shows **77 CVEs** classified under CWE-506. The most actively exploited:

| CVE | CVSS | EPSS | KEV | Context |
|-----|------|------|-----|---------|
| CVE-2025-30066 | 8.6 | 0.913 | Yes | tj-actions/changed-files GitHub Action compromise |
| CVE-2024-3094 | 10.0 | 0.850 | No | xz-utils backdoor (Jia Tan) |
| CVE-2025-59374 | 9.3 | 0.318 | Yes | Supply chain attack |
| **CVE-2026-33634** | **9.4** | **0.212** | **Yes** | **Axios npm compromise (this campaign cluster)** |
| CVE-2025-30154 | 8.6 | 0.154 | Yes | reviewdog/action-setup compromise |
| CVE-2024-4978 | 8.4 | 0.141 | Yes | JAVS courtroom recording supply chain |

The axios compromise (CVE-2026-33634) fits squarely in the Lazarus Group's supply chain pattern and was active during the same timeframe as this 19-day campaign.

---

## Researcher Profile

**@toxy4ny / KL3FT3Z** is a red team operator and security researcher:
- Lead of [@Hackteam-Red](https://github.com/Hackteam-Red)
- 43 public repos focused on: WAF bypass, penetration testing, OSINT, red team tooling
- Notably maintains `lazarus-code` — a VS Code phishing simulation for security awareness training
- 1,591 followers on GitHub
- Active in: APT emulation, AI security benchmarking (`kevlar-benchmark`, `redteam-ai-benchmark`, `kidnapp-ai-benchmark`)
- First-hand target of all three campaign waves — providing unique observational data

---

## Detection & Hunting Guidance

### Email/Notification Layer
- Flag emails from `notifications@github.com` containing `share.google/` URLs
- Alert on GitHub discussion mentions from accounts < 7 days old
- Monitor for CVE references not present in NVD/MITRE (query VulnGraph: `lookup_cve`)

### Network Layer
- Block/monitor: `token-claw.xyz`, `watery-compost.today`
- Monitor connections to Majestic Hosting (AS396073) and TIER-NET (AS397423)
- Alert on custom binary protocol traffic on ports 22411-22412
- Watch for FTP exfiltration to known C2 IPs

### Endpoint Layer
- VS Code: Ensure `task.allowAutomaticTasks` is `false` (default since 1.109)
- Monitor for: `eleven.js` execution, `localStorage` wipe patterns
- Detect persistence via "Windows Update Script.pyw" in Startup folder
- Alert on scheduled tasks named "Runtime Broker" at logon

### Wallet/Blockchain
- Monitor `0x6981E9EA7023a8407E4B08ad97f186A5CBDaFCf5` for any transactions
- Alert on wallet-connect calls to unknown domains

---

## Vajra Structural Analysis

Vajra fraud-profile analysis of the compiled IOC dataset reveals:
- **175 nodes across 110 distinct paths** at max depth 5
- **Delivery mechanism is invariant**: All three waves use identical `"GitHub discussion mass-mention -> email notification"` delivery (entropy = 0, H(Y|X) = 0.000)
- **Perfect functional dependencies** (strength=1.0): `date -> id -> name -> psychological_vector -> redirect_url -> trigger` — each wave is uniquely identifiable by any single field
- **Status-trigger partial dependency** (strength=0.579): Active status correlates with fear/ambition vectors; sinkholed with greed — suggesting the greed vector was detected first
- **Structural motif 1c47174c repeats 128 times** — the campaign's "atom" is a flat key-value pair pattern replicated across all IOC categories

---

## Related Campaign Clusters

| Cluster | Aliases | Active Since | Overlap |
|---------|---------|-------------|---------|
| Operation Dream Job | DeathNote, NukeSped | 2019 | Wave 3 fake recruitment |
| Contagious Interview | DeceptiveDevelopment, Famous Chollima, WaterPlum | Dec 2022 | ClickFix, GolangGhost |
| ClickFake Interview | (Sekoia naming) | Mar 2025 | Expanded targeting beyond devs |
| Axios npm Compromise | UNC1069 / BlueNoroff | Mar 2026 | Same timeframe, same actor umbrella |
| StoatWaffle VS Code | (The Hacker News) | Dec 2025 | Wave 2 VS Code lure |

---

## Sources

- [Original article (toxy4ny)](https://dev.to/toxy4ny/lazarus-groups-19-day-ab-test-how-north-korean-apt-pivoted-from-airdrops-to-fake-cves-to-dream-42af)
- [Fake CVE wave analysis (toxy4ny)](https://dev.to/toxy4ny/lazarus-group-evolves-from-fake-airdrops-to-fake-cves-new-github-phishing-wave-2bm7)
- [OpenClaw phishing analysis (toxy4ny)](https://dev.to/toxy4ny/github-developers-targeted-in-sophisticated-openclaw-phishing-scam-1lei)
- [OX Security OpenClaw Report](https://www.ox.security/blog/openclaw-github-phishing-crypto-wallet-attack/)
- [Red Asgard: Hunting Lazarus C2 Infrastructure](https://redasgard.com/blog/hunting-lazarus-contagious-interview-c2-infrastructure)
- [Red Asgard: Part III - Infrastructure Too Perfect](https://redasgard.com/blog/hunting-lazarus-part3-infrastructure-too-perfect)
- [Sekoia: ClickFake Interview Campaign](https://blog.sekoia.io/clickfake-interview-campaign-by-lazarus/)
- [The Hacker News: StoatWaffle via VS Code](https://thehackernews.com/2026/03/north-korean-hackers-abuse-vs-code-auto.html)
- [The Hacker News: GolangGhost ClickFix](https://thehackernews.com/2025/04/lazarus-group-targets-job-seekers-with.html)
- [The Cyber Express: Lazarus Axios npm Attack](https://thecyberexpress.com/lazarus-behind-axios-npm-supply-chain-attack/)
- [Axios Supply Chain Gist (N3mes1s)](https://gist.github.com/N3mes1s/0c0fc7a0c23cdb5e1c8f66b208053ed6)
- [1898 Advisories: March 2026 Supply Chain Wave](https://1898advisories.burnsmcd.com/march-2026-developer-supply-chain-attack-wave-teampcp-ci/cd-infrastructure-campaign-cve-2026-33634-and-concurrent-unc1069-axios-npm-compromise)
- [CSO Online: OpenClaw Wallet Draining](https://www.csoonline.com/article/4150456/github-phishers-use-fake-openclaw-tokens-to-drain-crypto-wallets.html)
- [CoinDesk: OpenClaw Phishing](https://www.coindesk.com/tech/2026/03/19/openclaw-developers-targeted-in-github-phishing-scam-offering-fake-token-airdrops)
- [Hackread: Fake OpenClaw Token](https://hackread.com/fake-openclaw-token-github-devs-wallet-drainer-scam/)
- [GitHub Discussion #190675: Notification Safety](https://github.com/orgs/community/discussions/190675)
- [Security Boulevard: GitHub/GitLab Phishing Abuse](https://securityboulevard.com/2026/04/the-growing-abuse-of-github-and-gitlab-in-phishing-campaigns/)
- [Cisco Talos: SaaS Notification Pipeline Weaponization](https://blog.talosintelligence.com/weaponizing-saas-notification-pipelines/)
- [MITRE ATT&CK: Lazarus Group G0032](https://attack.mitre.org/groups/G0032/)
- [JPCERT/CC: Lazarus TTP Mapping](https://github.com/JPCERTCC/Lazarus-research/blob/main/TTP/MITRE_ATT&CK_Mapping.md)
- [CSA: DPRK Dual-Track Cyber Doctrine](https://labs.cloudsecurityalliance.org/research/csa-research-note-dprk-defi-supply-chain-systemic-risk-20260/)
- VulnGraph (vulngraph.tools) — CVE, EPSS, KEV, and ATT&CK graph queries (data as of 2026-04-09)
