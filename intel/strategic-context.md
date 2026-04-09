# Strategic Intelligence Context: DPRK Cyber Operations & the 19-Day Campaign

## The Financial Machine

The Lazarus Group's 19-day A/B test campaign is not an isolated incident — it's a small cog in the most profitable state-sponsored cybercrime operation in history.

### DPRK Theft Timeline

| Year | Amount Stolen | Notable Operations |
|------|--------------|-------------------|
| 2016 | $81M | Bangladesh Bank SWIFT heist |
| 2017 | $571M | Cryptocurrency exchange spree |
| 2018 | $400M+ | Continued exchange targeting |
| 2022 | $600M | Ronin Bridge (Axie Infinity) |
| 2023 | $660.5M | Multiple DeFi exploits |
| 2024 | $1.3B | Escalated DeFi/bridge attacks |
| 2025 | $2.06B | **Bybit ($1.5B)**, exchange/DeFi raids |
| 2026 (YTD) | $285M+ | **Drift Protocol ($285M)**, ongoing operations |
| **All-time** | **~$6.75B+** | |

Source: [BlockEden.xyz](https://blockeden.xyz/blog/2026/02/03/lazarus-group-playbook-north-korea-crypto-theft-6-75-billion/), [Chainalysis](https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/), [38 North](https://www.38north.org/2026/01/from-digital-kleptocracy-to-rogue-crypto-superpower/)

### Why Developer Targeting Matters

The 19-day campaign targets the **supply side** of the crypto ecosystem. While direct exchange hacks yield larger payouts, developer-targeted campaigns serve multiple strategic objectives:

1. **Access multiplication**: One compromised developer credential can unlock CI/CD pipelines, npm publish rights, and infrastructure access
2. **Supply chain leverage**: The March 2026 axios compromise (CVE-2026-33634) demonstrates this — a single maintainer compromise poisoned a package with 50M+ weekly downloads
3. **Talent recruitment pipeline**: Contagious Interview campaigns serve dual purpose — infecting targets AND identifying candidates for DPRK's fake IT worker program (16,952 LinkedIn profiles in target lists)
4. **Low cost, high optionality**: A phishing campaign costs almost nothing to run; each compromised developer is a potential entry point to their employer, their open source projects, and their financial assets

---

## Front Company Infrastructure

### Known DPRK Front Companies (Silent Push Research)

| Company | Status | Registration | Notes |
|---------|--------|-------------|-------|
| **BlockNovas LLC** | **FBI Seized** | NameCheap, July 2024 | Cloudflare DNS, AI-generated employee photos |
| **SoftGlide LLC** | **Still Active** | New Mexico | Active lure infrastructure |
| **Angeloper Agency** | **Active** | Unknown | Third front identified |

These companies deliver the same malware trilogy: **BeaverTail** (JS stealer) -> **InvisibleFerret** (Python backdoor) -> **OtterCookie** (modular RAT).

Source: [Silent Push](https://www.silentpush.com/blog/contagious-interview-front-companies/)

---

## Campaign Cluster Relationships

```
DPRK RGB (Reconnaissance General Bureau)
├── Lazarus Group (G0032)
│   ├── Operation Dream Job (since 2019)
│   │   ├── ClickFake Interview (Sekoia, Mar 2025)
│   │   │   └── Wave 3: Uniswap Recruitment ← THIS CAMPAIGN
│   │   └── Fake DeFi Audit Challenges
│   │       └── lazarus-code repo pattern ← RECONSTRUCTED BY TOXY4NY
│   │
│   ├── Contagious Interview / DeceptiveDevelopment (G1052)
│   │   ├── BeaverTail / OtterCookie / InvisibleFerret
│   │   ├── Front Companies (BlockNovas, SoftGlide, Angeloper)
│   │   ├── VS Code tasks.json / StoatWaffle
│   │   └── Wave 2: Fake VS Code CVE ← THIS CAMPAIGN
│   │
│   ├── Supply Chain Operations
│   │   ├── axios npm compromise (CVE-2026-33634)
│   │   ├── TeamPCP CI/CD campaign
│   │   └── GitHub Actions poisoning (trivy-action, setup-trivy)
│   │
│   └── Direct Financial Operations
│       ├── Bybit ($1.5B, Feb 2025)
│       ├── Drift Protocol ($285M, Apr 2026)
│       └── Ronin Bridge ($600M, 2022)
│
├── BlueNoroff / UNC1069
│   ├── axios npm compromise (overlap)
│   └── WAVESHAPER backdoor family
│
└── Famous Chollima / WaterPlum / WageMole
    ├── GolangGhost RAT
    ├── PylangGhost RAT
    ├── Fake IT Worker Program
    └── Wave 1: OpenClaw Airdrop ← THIS CAMPAIGN
```

---

## CVE-2026-33634: The Supply Chain Nexus

This CVE deserves special attention as it connects the 19-day phishing campaign to a much larger supply chain attack.

| Attribute | Value |
|-----------|-------|
| CVE | CVE-2026-33634 |
| CVSS | 9.4 CRITICAL |
| EPSS | 0.2115 (95.65th percentile) |
| KEV | Yes (actively exploited) |
| CWE | CWE-506 (Embedded Malicious Code) |
| Exploit Maturity | WEAPONIZED (3 public PoCs) |
| Affected Packages | aquasecurity/trivy-action, aquasecurity/setup-trivy, BerriAI/LiteLLM, telnyx, npm:axios |
| Attribution | UNC1069 / BlueNoroff (Lazarus umbrella) |

**The attack chain**: Social engineering of maintainer -> RAT deployment -> npm 2FA bypass -> trojan dependency injection (`plain-crypto-js@4.2.1`) -> postinstall hook execution -> WAVESHAPER backdoor on every `npm install`.

This is the same actor umbrella running the 19-day A/B test — the phishing campaign is the **talent scout** feeding the supply chain operation.

---

## The Lazarus Software Arsenal (26 Known Tools from VulnGraph G0032)

| MITRE ID | Tool | Type |
|----------|------|------|
| S0103 | Attor | Espionage platform |
| S0108 | netsh | Network utility abuse |
| S0174 | Responder | LLMNR/NBT-NS poisoning |
| S0180 | Volgmer | Backdoor |
| S0181 | FALLCHILL | RAT |
| S0238 | Proxysvc | Proxy tool |
| S0239 | Bankshot | Trojan |
| S0241 | RATANKBA | RAT |
| S0245 | TYPEFRAME | Backdoor |
| S0246 | HARDRAIN | Trojan |
| S0263 | TYPEFRAME | Backdoor |
| S0271 | KEYMARBLE | Backdoor |
| S0347 | AuditCred | Credential theft |
| S0364 | RawDisk | Disk wiper |
| S0366 | WannaCry | Ransomware |
| S0376 | HOPLIGHT | Trojan |
| S0431 | DRATzarus | RAT |
| S0497 | Dacls | RAT (cross-platform) |
| S0498 | Manuscrypt | Backdoor |
| S0520 | BLINDINGCAN | RAT |
| S0567 | Dtrack | Spyware |
| S0584 | AppleJeus | Crypto trojan |
| S0586 | ECCENTRICBANDWAGON | Keylogger |
| S0593 | COPPERHEDGE | RAT |
| S0665 | LightlessCan | RAT |
| S1182 | MISTPEN | Backdoor |

**Not yet in MITRE but active in 2025-2026:**
- BeaverTail (JavaScript stealer)
- InvisibleFerret (Python backdoor)
- OtterCookie (Modular RAT, 27 wallet extensions)
- GolangGhost (Go RAT)
- PylangGhost (Python RAT, AI-assisted port)
- StoatWaffle (VS Code tasks.json malware)
- eleven.js (Wallet drainer)
- WAVESHAPER (npm supply chain)

---

## The Honeypot Question

Red Asgard's Part III infrastructure analysis raised a critical assessment:

> **70% probability that the standardized Contagious Interview C2 servers are a honeypot or counter-intelligence operation.**

Supporting evidence:
- Perfect security posture across all 11 vulnerability test classes
- `/cert/private.pem` endpoint returning an "exposed" private key (likely bait)
- Every file upload returned `DONE` with no actual validation
- Trivial rate-limit bypass that seems intentional
- Long-poll C2 endpoints showed no real victim management
- All infrastructure deployed identically in January 2025

**Implication**: Some of the "Lazarus infrastructure" researchers find may be deliberately planted — either by intelligence agencies monitoring DPRK operations, or by DPRK itself as counterintelligence. This doesn't invalidate the IOCs for blocking purposes, but it means attribution confidence should be modulated.

---

## Defensive Recommendations (Priority Order)

### Immediate (This Week)
1. **Block all IOCs** from `ioc-blocklist.txt` at DNS/firewall/proxy layer
2. **Audit npm dependencies** for `plain-crypto-js`, `axios@1.14.1`, `axios@0.30.4`
3. **Verify VS Code setting** `task.allowAutomaticTasks` is `false` across all developer machines
4. **Alert on** `notifications@github.com` emails containing `share.google/` URLs

### Short-term (This Month)
5. **Deploy Sigma rules** from `detection-rules/sigma/` to SIEM
6. **Deploy Suricata rules** from `detection-rules/suricata/` to network sensors
7. **Run nuclei templates** against infrastructure for proactive scanning
8. **Import STIX bundle** into MISP/OpenCTI for threat intel sharing
9. **Brief developers** on GitHub notification phishing pattern — the trust model is the vulnerability

### Strategic (Ongoing)
10. **Hardware wallet mandate** for any crypto operations
11. **npm lockfile auditing** in CI/CD with automated CVE checking
12. **GitHub notification filtering** — consider disabling email notifications for @mentions from unknown users
13. **Salary sanity checks** in recruitment — $300K-$450K remote crypto dev positions are red flags
14. **Source code review** before opening any cloned repo in VS Code — check `.vscode/tasks.json` and `package.json` scripts

---

## Sources

- [Silent Push: Contagious Interview Front Companies](https://www.silentpush.com/blog/contagious-interview-front-companies/)
- [BlockEden: Lazarus $6.75B Playbook](https://blockeden.xyz/blog/2026/02/03/lazarus-group-playbook-north-korea-crypto-theft-6-75-billion/)
- [38 North: DPRK Digital Kleptocracy to Crypto Superpower](https://www.38north.org/2026/01/from-digital-kleptocracy-to-rogue-crypto-superpower/)
- [Chainalysis: 2025 Crypto Hacking Report](https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/)
- [TRM Labs: Bybit Hack Analysis](https://www.trmlabs.com/resources/blog/the-bybit-hack-following-north-koreas-largest-exploit)
- [Red Asgard: Infrastructure Too Perfect](https://redasgard.com/blog/hunting-lazarus-part3-infrastructure-too-perfect)
- [MITRE ATT&CK: Lazarus Group G0032](https://attack.mitre.org/groups/G0032/)
- VulnGraph (vulngraph.tools) — Graph queries for G0032 software arsenal
