# Disclaimer

## Purpose

This repository is published **exclusively for defensive security purposes**: threat detection, incident response, security awareness, and academic research. It contains no malware, exploit code, or offensive tooling.

## What This Repository Contains

- **Indicators of compromise (IOCs)** — domains, IP addresses, file hashes, wallet addresses, and URLs associated with observed threat actor campaigns. These are published to enable blocking and detection.
- **Detection rules** — YARA, Sigma, Suricata, and Nuclei signatures designed to identify malicious activity on defended networks and endpoints.
- **Threat intelligence reports** — analytical assessments of campaign tactics, techniques, and procedures (TTPs) intended to inform defensive posture.
- **STIX 2.1 bundle** — structured threat data formatted for import into established threat intelligence platforms (MISP, OpenCTI).
- **ATT&CK Navigator layer** — technique coverage mapping for security teams to assess detection gaps.
- **Architecture diagrams** — visual representations of attack infrastructure generated from code.

## What This Repository Does NOT Contain

- No malware samples, binaries, or executable payloads
- No exploit code or proof-of-concept attacks
- No credentials, private keys, or session tokens
- No tools that could be used to conduct attacks
- No personally identifiable information (PII) of victims

## Attribution

Attribution assessments in this repository represent analytical judgments based on publicly available information, behavioral pattern matching, and open-source threat intelligence. **They are not legal conclusions.** Attribution of cyber operations to nation-states or specific groups involves inherent uncertainty. Assessments are stated with confidence levels where applicable and should be interpreted as informed analysis, not definitive proof.

## IOC Freshness

Indicators of compromise have a limited useful lifespan. Threat actors rotate infrastructure, and domains may be re-registered by unrelated parties after abandonment. IOCs in this repository reflect the state of infrastructure as of the dates noted in the reports (March -- April 2026). Consumers of this data should:

- Verify IOCs against current threat intelligence before taking blocking actions
- Use IOCs for detection and alerting rather than blanket blocking where feasible
- Periodically review and retire stale indicators

## Third-Party Research

This repository builds upon and credits the original research of [@toxy4ny](https://github.com/toxy4ny) and incorporates findings from publicly available reports by OX Security, Red Asgard, Sekoia, ANY.RUN, Silent Push, Microsoft, Cisco Talos, and other security organizations. All sources are cited. No proprietary or embargoed information is included.

## Responsible Use

By using the contents of this repository, you agree to use them solely for lawful defensive purposes including but not limited to:

- Protecting networks and systems you are authorized to defend
- Conducting authorized security research
- Academic study and education
- Informing organizational security policy

Do not use the IOCs, infrastructure details, or attack chain descriptions in this repository to conduct unauthorized access, harassment, or any illegal activity.

## No Warranty

This threat intelligence is provided "as is" without warranty of any kind, express or implied. The authors make no representations about the accuracy, completeness, or reliability of the information. Use at your own risk.

## Contact

To report errors, request removal of specific data, or discuss responsible disclosure matters, please open an issue in this repository.
