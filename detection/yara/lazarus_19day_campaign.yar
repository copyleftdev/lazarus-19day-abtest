/*
    Lazarus Group 19-Day A/B Test Campaign - YARA Rules
    Date: 2026-04-08
    Author: Enriched from toxy4ny research
    References:
      - https://dev.to/toxy4ny/lazarus-groups-19-day-ab-test-how-north-korean-apt-pivoted-from-airdrops-to-fake-cves-to-dream-42af
      - https://redasgard.com/blog/hunting-lazarus-contagious-interview-c2-infrastructure
      - https://any.run/cybersecurity-blog/pylangghost-malware-analysis/
*/

rule Lazarus_ElevenJS_WalletDrainer
{
    meta:
        description = "Detects eleven.js wallet drainer used in OpenClaw phishing campaign"
        author = "vajra-sec-experiment"
        date = "2026-04-08"
        threat_actor = "Lazarus Group"
        campaign = "OpenClaw Airdrop (Wave 1)"
        reference = "https://www.ox.security/blog/openclaw-github-phishing-crypto-wallet-attack/"
        severity = "critical"

    strings:
        $c2_domain = "watery-compost.today" ascii wide
        $phishing_domain = "token-claw.xyz" ascii wide
        $wallet = "0x6981E9EA7023a8407E4B08ad97f186A5CBDaFCf5" ascii wide nocase

        $func_nuke = "nuke" ascii
        $func_prompt = "PromptTx" ascii
        $func_approved = "Approved" ascii
        $func_declined = "Declined" ascii

        $wallet_connect1 = "eth_requestAccounts" ascii
        $wallet_connect2 = "eth_getBalance" ascii
        $wallet_connect3 = "eth_sendTransaction" ascii

        $obfusc1 = "String.fromCharCode" ascii
        $obfusc2 = "atob(" ascii
        $obfusc3 = /eval\s*\(/ ascii

        $localStorage_wipe = "localStorage.clear" ascii
        $sessionStorage_wipe = "sessionStorage.clear" ascii

    condition:
        ($c2_domain or $phishing_domain or $wallet) or
        (3 of ($func_*)) or
        (all of ($wallet_connect*) and 2 of ($obfusc*)) or
        (2 of ($wallet_connect*) and ($localStorage_wipe or $sessionStorage_wipe))
}

rule Lazarus_FakeCVE_Lure
{
    meta:
        description = "Detects fake CVE phishing lures from Lazarus 19-day campaign"
        author = "vajra-sec-experiment"
        date = "2026-04-08"
        campaign = "Fake VS Code CVE (Wave 2)"

    strings:
        $fake_cve = "CVE-2026-40271" ascii wide nocase
        $fake_researcher = "Nathaniel Pemberton" ascii wide nocase
        $fake_company = "Precision Algorithmics" ascii wide nocase
        $fake_version = "1.112.4" ascii wide
        $urgency1 = "Emergency measure required" ascii wide nocase
        $urgency2 = "without delay" ascii wide nocase
        $share_google = "share.google/" ascii wide

    condition:
        $fake_cve or
        ($fake_researcher and $fake_company) or
        ($fake_version and $share_google) or
        (2 of ($urgency*) and $share_google)
}

rule Lazarus_GoogleShare_Redirect
{
    meta:
        description = "Detects Google Share URLs used as phishing redirects in Lazarus campaigns"
        author = "vajra-sec-experiment"
        date = "2026-04-08"
        campaign = "Lazarus 19-Day A/B Test (all waves)"

    strings:
        $redirect1 = "share.google/eGzdhAucWKKcwkZi9" ascii wide
        $redirect2 = "share.google/N3NwdcmyaYu9kwZ6D" ascii wide
        $redirect3 = "share.google/GVTYMEMANZWqTptr2" ascii wide

    condition:
        any of them
}

rule Lazarus_PylangGhost_RAT
{
    meta:
        description = "Detects PylangGhost RAT components"
        author = "vajra-sec-experiment"
        date = "2026-04-08"
        threat_actor = "Famous Chollima / WaterPlum"
        malware_family = "PylangGhost"
        reference = "https://any.run/cybersecurity-blog/pylangghost-malware-analysis/"

    strings:
        // Command dictionary
        $cmd_qwer = "qwer" ascii
        $cmd_asdf = "asdf" ascii
        $cmd_zxcv = "zxcv" ascii
        $cmd_vbcv = "vbcv" ascii
        $cmd_qalp = "qalp" ascii
        $cmd_ghd = "ghd" ascii
        $cmd_89io = "89io" ascii
        $cmd_gipct = "gi%#" ascii
        $cmd_kyci = "kyci" ascii
        $cmd_dghh = "dghh" ascii

        // Function signatures
        $func1 = "Packet0623make" ascii
        $func2 = "Packet0623decode" ascii
        $func3 = "Htxp0623Exchange" ascii
        $func4 = "makeMsg0623" ascii
        $func5 = "decodeMsg0623" ascii
        $func6 = "com0715press" ascii
        $func7 = "decom0715press" ascii
        $func8 = "valid0715relPath" ascii
        $func9 = "AutoGatherMode" ascii
        $func10 = "AutoCookieMode" ascii

        // C2 domain
        $c2 = "360scanner.store" ascii wide

        // File artifacts
        $artifact1 = "chrome_logins_dump.txt" ascii wide
        $artifact2 = "gather.tar.gz" ascii wide
        $artifact3 = "nvidiaRelease" ascii wide

        // Persistence
        $persist1 = "csshost.exe" ascii wide
        $persist2 = "update.vbs" ascii wide
        $persist3 = "Google Chromekey1" ascii wide

    condition:
        (4 of ($cmd_*)) or
        (3 of ($func*)) or
        ($c2 and 2 of ($artifact*)) or
        (2 of ($persist*) and any of ($func*))
}

rule Lazarus_PylangGhost_Hashes
{
    meta:
        description = "Detects known PylangGhost file hashes"
        author = "vajra-sec-experiment"
        date = "2026-04-08"

    condition:
        hash.sha256(0, filesize) == "bb794019f8a63966e4a16063dc785fafe8a5f7c7553bcd3da661c7054c6674c7" or
        hash.sha256(0, filesize) == "c4fd45bb8c33a5b0fa5189306eb65fa3db53a53c1092078ec62f3fc19bc05dcb" or
        hash.sha256(0, filesize) == "c7ecf8be40c1e9a9a8c3d148eb2ae2c0c64119ab46f51f603a00b812a7be3b45" or
        hash.sha256(0, filesize) == "a179caf1b7d293f7c14021b80deecd2b42bbd409e052da767e0d383f71625940" or
        hash.sha256(0, filesize) == "ef04a839f60911a5df2408aebd6d9af432229d95b4814132ee589f178005c72f"
}

rule Lazarus_ContagiousInterview_Workspace_Init
{
    meta:
        description = "Detects malicious VS Code workspace initialization scripts from Contagious Interview"
        author = "vajra-sec-experiment"
        date = "2026-04-08"
        reference = "https://github.com/toxy4ny/lazarus-code"

    strings:
        $tracker = "phishing-tracker" ascii wide
        $campaign = "contagious-interview" ascii wide
        $event = "vscode_workspace_opened" ascii wide
        $ua = "VSCode-Workspace-Init" ascii wide

        $telemetry1 = "collectTelemetry" ascii
        $telemetry2 = "sendToTracker" ascii
        $telemetry3 = "showAwarenessNotification" ascii

        $exec1 = "execSync" ascii
        $exec2 = "code --version" ascii
        $exec3 = "os.userInfo" ascii

    condition:
        ($campaign and $event) or
        ($tracker and $ua) or
        (2 of ($telemetry*) and 2 of ($exec*))
}

rule Lazarus_BeaverTail_C2_Ports
{
    meta:
        description = "Detects BeaverTail/OtterCookie C2 infrastructure port signature"
        author = "vajra-sec-experiment"
        date = "2026-04-08"
        reference = "https://redasgard.com/blog/hunting-lazarus-part3-infrastructure-too-perfect"

    strings:
        $port1244 = ":1244" ascii wide
        $port5918 = ":5918" ascii wide
        $port22411 = ":22411" ascii wide
        $port22412 = ":22412" ascii wide

        $xor_key1 = "G01d*8@(" ascii
        $xor_key2 = "G0Md*8@(" ascii
        $xor_key3 = "Vw1aGYoP" ascii
        $xor_key4 = "!!!HappyPenguin1950!!!" ascii
        $xor_key5 = "Xt3rqfmL" ascii
        $xor_key6 = "Ze4pq4iT" ascii

    condition:
        (2 of ($port*)) or
        (2 of ($xor_key*))
}

rule Lazarus_FakeRecruitment_Lure
{
    meta:
        description = "Detects fake recruitment lures from Operation Dream Job / Wave 3"
        author = "vajra-sec-experiment"
        date = "2026-04-08"
        campaign = "Uniswap Recruitment (Wave 3)"

    strings:
        $salary1 = "$300,000" ascii wide
        $salary2 = "$450,000" ascii wide
        $salary3 = "$300k" ascii wide nocase
        $grammar = "Every roles are fully online" ascii wide nocase
        $share = "share.google/" ascii wide
        $defi1 = "DeFi Innovations" ascii wide
        $defi2 = "defi-vault-audit-challenge" ascii wide
        $defi3 = "Senior Blockchain Developer" ascii wide

    condition:
        ($grammar and $share) or
        (any of ($salary*) and $share) or
        ($defi1 and $defi2) or
        (2 of ($defi*) and filesize < 50KB)
}

rule Lazarus_Axios_Supply_Chain
{
    meta:
        description = "Detects indicators of the Lazarus axios npm supply chain compromise"
        author = "vajra-sec-experiment"
        date = "2026-04-08"
        cve = "CVE-2026-33634"
        reference = "https://gist.github.com/N3mes1s/0c0fc7a0c23cdb5e1c8f66b208053ed6"

    strings:
        $trojan_dep = "plain-crypto-js" ascii wide
        $bad_version1 = "axios@1.14.1" ascii wide
        $bad_version2 = "axios@0.30.4" ascii wide
        $postinstall = "postinstall" ascii

    condition:
        $trojan_dep or
        (($bad_version1 or $bad_version2) and $postinstall)
}
