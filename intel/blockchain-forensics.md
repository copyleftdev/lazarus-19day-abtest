# Blockchain Forensic Analysis: Wallet 0x6981E9EA7023a8407E4B08ad97f186A5CBDaFCf5

## On-Chain Status (April 8, 2026)

| Attribute | Value |
|-----------|-------|
| ETH Balance | **0 ETH ($0.00)** |
| Transaction Count | **0 (zero — never transacted)** |
| Token Holdings | None across 32 chains |
| Address Type | EOA (Externally Owned Account) |
| First Transaction | N/A (never activated) |
| Etherscan Labels | None |
| Internal Transactions | None |
| Contract Interactions | None |

## Assessment

**The wallet was never used.** It exists only as a derived address from a private key hardcoded in the `eleven.js` drainer payload. It has never submitted or received a single transaction on Ethereum mainnet or any EVM-compatible chain.

## How the Wallet Was Identified

OX Security extracted the address through deobfuscation of eleven.js:
```javascript
from: accounts[0],
to: '0x6981E9EA7023a8407E4B08ad97f186A5CBDaFCf5',
value: FULL_BALANCE
```

## Victim Impact

**Zero confirmed victims.** Multiple firms (OX Security, CoinDesk, The Block, CSO Online, Hackread, Decrypt) all independently confirmed zero transactions. The campaign was intercepted before any successful drains.

## Security Platform Labels

| Platform | Label |
|----------|-------|
| Etherscan | None |
| Arkham Intelligence | None |
| Chainalysis | None |
| Blockaid | None |
| OFAC SDN List | Not listed |

No labels applied because zero on-chain activity means no automated detection triggers.

## Monitoring Recommendation

The wallet remains a valid IOC — Lazarus Group is known to reuse infrastructure. Any future transaction to or from this address should trigger an immediate alert.

## Sources

- [OX Security](https://www.ox.security/blog/openclaw-github-phishing-crypto-wallet-attack/)
- [CoinDesk](https://www.coindesk.com/tech/2026/03/19/openclaw-developers-targeted-in-github-phishing-scam-offering-fake-token-airdrops)
- [Etherscan](https://etherscan.io/address/0x6981E9EA7023a8407E4B08ad97f186A5CBDaFCf5)
