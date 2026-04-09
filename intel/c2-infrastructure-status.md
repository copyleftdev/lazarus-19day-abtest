# Lazarus C2 Infrastructure Status Report — April 8, 2026

## Domain Status

| Domain | Role | Status |
|--------|------|--------|
| `tetrismic.vercel.app` | OtterCookie staging | **PARTIALLY ACTIVE** — Takedown requested, GitHub account (stardev0914) removed |
| `server-check-genimi.vercel.app` | **NEW** OtterCookie replacement | **ACTIVE** — endpoint `/defy/v3`, Bearer token "logo" |
| `token-claw.xyz` | OpenClaw phishing | **ACTIVE** — No confirmed sinkhole despite reports |
| `watery-compost.today` | eleven.js C2 | **ACTIVE** |
| `360scanner.store` | PylangGhost C2 | **ACTIVE** — Serving payloads, evasion via User-Agent decoy |
| `nvidiasdk.fly.dev` | InvisibleFerret C2 | **ACTIVE** — Breakglass cluster |
| `api.videodriverzone.cloud` | BeaverTail C2 | **ACTIVE** |
| `api.videotechdrivers.cloud` | BeaverTail C2 | **ACTIVE** |
| `api.driversnap.cloud` | BeaverTail C2 | **ACTIVE** |
| `api.camdriverstore.cloud` | BeaverTail C2 | **ACTIVE** |
| `api.driverstream.cloud` | BeaverTail C2 | **ACTIVE** |

## IP Address Status

### Majestic Hosting AS396073 (SpinServers, Carrollton TX)

| IP | Hostname | Port(s) | Status |
|----|----------|---------|--------|
| 147.124.213.232 | WR232 | 1244, 21, 3389, 5985 | **ACTIVE** |
| 147.124.212.125 | W9_125 | 1244, 21, 3389, 5985 | **ACTIVE** |
| 216.250.251.87 | WIN-8OA3CCQAE4D | 1247, 21, 3389, 5985 | **ACTIVE** |
| 147.124.214.129 | — | 1244 | **ACTIVE** — Listed on URLhaus |

### TIER-NET AS397423 (Florida)

| IP | Hostname | Role | Status |
|----|----------|------|--------|
| 45.43.11.199 | WIN-4MOD9QVI0EN | Router | **OFFLINE** |
| 66.235.63.55 | — | MetaMask Injector | **ACTIVE** |
| 66.235.168.238 | Z238 | Chrome Stealer + binary protocol | **ACTIVE (DEFENSIVE)** — Ports closed after researcher probes |
| 45.59.163.55 | PS55 | Chrome Stealer | **ACTIVE** |
| 45.59.163.23 | — | BeaverTail variant | **ACTIVE** — Different from .55 |

### NEW Infrastructure (April 2026)

| IP | ASN | Role | Ports | Status |
|----|-----|------|-------|--------|
| **216.126.237.71** | AS14956 RouterHosting | OtterCookie v2 | 4891 (RAT), 4896 (cred theft), 4899 (file exfil), 80 (clipboard) | **ACTIVE** |
| 95.216.37.186 | Hetzner (Finland) | InvisibleFerret | 5000, 3011 | **ACTIVE** |
| 95.164.17.24 | TheHosting (Netherlands) | BeaverTail | 1224 | **ACTIVE** |
| 172.86.93.139 | FranTech/BuyVM | InvisibleFerret | 3000 | **ACTIVE** |

### OtterCookie C2 Cluster

| IP | Port | Status |
|----|------|--------|
| 172.86.105.40 | 5918 | **ACTIVE** — Primary |
| 172.86.116.178 | 5918 | **ACTIVE** |
| 86.106.85.234 | 5918 | **ACTIVE** |
| 144.172.104.117 | 5918 | **ACTIVE** |
| 144.172.101.45 | 5918 | **ACTIVE** |

## Victim Impact (as of Feb 2026)

- **857 compromised developers** across 90 countries
- **241,764 stolen credentials** in plaintext on unauthenticated endpoints
- Top countries: India (2.8%), Bangladesh (2.1%), Vietnam (1.4%), Pakistan (1.2%), US (1.0%)
- Stolen credential categories: banking (HDFC, BofA, Schwab, Revolut), crypto wallets (MetaMask, Phantom, Coinbase), payment (PayPal, Payoneer, Stripe), developer platforms (GitHub: 2,647 creds, Upwork: 969 creds, Google: 4,280 creds)
- FBI IC3 report filed January 29, 2026
- Supplementary CISA report filed February 2, 2026

## New Attack Vectors (April 2026)

**OtterCookie is now targeting AI coding tools:**
- Malicious npm packages: `gemini-ai-checker`, `express-flowlimit`, `chai-extensions-extras`
- PylangGhost packages: `@jaime9008/math-service`, `react-refresh-update`
- Targets: Gemini, Cursor, Claude integrations

## Operator Behavior

- **Active defensive monitoring**: Operators detected researcher reconnaissance and closed ports within hours
- **Rapid infrastructure rotation**: Takedowns of individual domains result in replacement infrastructure within days
- **Vercel domains returning HTTP 451** (Unavailable For Legal Reasons) after legal requests

## Sources

- [Red Asgard: Hunting Lazarus C2](https://redasgard.com/blog/hunting-lazarus-contagious-interview-c2-infrastructure)
- [Red Asgard Part III](https://redasgard.com/blog/hunting-lazarus-part3-infrastructure-too-perfect)
- [Red Asgard Part IV: Real Blood on the Wire](https://redasgard.com/blog/hunting-lazarus-part4-real-blood-on-the-wire)
- [OtterCookie Targets AI Coding Tools](https://cyberandramen.net/2026/04/04/ottercookie-expands-targeting-to-ai-coding-tools-analysis-of-a-trojanized-npm-campaign/)
- [Breakglass: InvisibleFerret Infrastructure](https://intel.breakglass.tech/post/invisibleferret-contagious-interview-dprk-lazarus-kimsuky-crossover)
- [Microsoft: Contagious Interview](https://www.microsoft.com/en-us/security/blog/2026/03/11/contagious-interview-malware-delivered-through-fake-developer-job-interviews/)
- [URLhaus: 147.124.214.129](https://urlhaus.abuse.ch/url/3235725/)
