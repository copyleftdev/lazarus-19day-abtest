#!/usr/bin/env python3
"""
Lazarus 19-Day A/B Test Campaign — Diagram Generator
Produces publication-quality PNG diagrams using the `diagrams` library.
Run: cd diagrams && python3 generate_all.py
"""

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ─────────────────────────────────────────────────────────────────────────────
# 1. KILL CHAIN
# ─────────────────────────────────────────────────────────────────────────────

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User, Users
from diagrams.onprem.network import Internet
from diagrams.programming.language import JavaScript, Python, Go
from diagrams.generic.os import Windows
from diagrams.generic.blank import Blank
from diagrams.generic.database import SQL
from diagrams.onprem.compute import Server
from diagrams.saas.chat import Slack

graph_attr = {
    "bgcolor": "#0d1117",
    "fontcolor": "#c9d1d9",
    "fontname": "Helvetica Neue",
    "fontsize": "14",
    "pad": "0.8",
    "ranksep": "1.2",
    "nodesep": "0.8",
}

node_attr = {
    "fontcolor": "#c9d1d9",
    "fontname": "Helvetica Neue",
    "fontsize": "11",
}

edge_attr = {
    "color": "#58a6ff",
    "fontcolor": "#8b949e",
    "fontname": "Helvetica Neue",
    "fontsize": "10",
}

with Diagram(
    "Lazarus 19-Day Campaign — Kill Chain",
    filename="01_kill_chain",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png",
):
    with Cluster(
        "STAGE 1: INITIAL ACCESS",
        graph_attr={
            "bgcolor": "#161b2233",
            "style": "rounded",
            "color": "#3498db",
            "penwidth": "2",
            "fontcolor": "#3498db",
            "fontsize": "13",
            "labeljust": "l",
        },
    ):
        attacker = Users("Attacker creates\nGitHub Discussion\nMass @mentions devs")
        github = Internet("notifications@\ngithub.com")
        redirect = Internet("share.google/*\nbypasses email filters")
        attacker >> Edge(label="triggers") >> github >> Edge(label="victim clicks") >> redirect

    with Cluster(
        "STAGE 2: WEAPONIZED LANDING",
        graph_attr={
            "bgcolor": "#161b2233",
            "style": "rounded",
            "color": "#e74c3c",
            "penwidth": "2",
            "fontcolor": "#e74c3c",
            "fontsize": "13",
            "labeljust": "l",
        },
    ):
        wave1_land = JavaScript("token-claw.xyz\nWallet clone site")
        wave2_land = Windows("Fake CVE-2026-40271\nVS Code update")
        wave3_land = Go("Fake Uniswap interview\nClickFix technique")

    redirect >> Edge(label="Wave 1: GREED", color="#27ae60", style="bold") >> wave1_land
    redirect >> Edge(label="Wave 2: FEAR", color="#e74c3c", style="bold") >> wave2_land
    redirect >> Edge(label="Wave 3: AMBITION", color="#2980b9", style="bold") >> wave3_land

    with Cluster(
        "STAGE 3: PAYLOAD EXECUTION",
        graph_attr={
            "bgcolor": "#161b2233",
            "style": "rounded",
            "color": "#f39c12",
            "penwidth": "2",
            "fontcolor": "#f39c12",
            "fontsize": "13",
            "labeljust": "l",
        },
    ):
        payload1 = JavaScript("eleven.js\nWallet drainer")
        payload2 = JavaScript("StoatWaffle\ntasks.json auto-run")
        payload3 = Go("GolangGhost\nPylangGhost RAT")

    wave1_land >> Edge(color="#27ae60") >> payload1
    wave2_land >> Edge(color="#e74c3c") >> payload2
    wave3_land >> Edge(color="#2980b9") >> payload3

    with Cluster(
        "STAGE 4: COMMAND & CONTROL",
        graph_attr={
            "bgcolor": "#161b2233",
            "style": "rounded",
            "color": "#f39c12",
            "penwidth": "2",
            "fontcolor": "#f39c12",
            "fontsize": "13",
            "labeljust": "l",
        },
    ):
        c2_wallet = Server("watery-compost.today\nTracks: PromptTx\nApproved / Declined")
        c2_infra = Server("Contagious Interview\nMajestic Hosting AS396073\nPorts 1244 / 5918")

    payload1 >> Edge(color="#27ae60") >> c2_wallet
    payload2 >> Edge(color="#e74c3c") >> c2_infra
    payload3 >> Edge(color="#2980b9") >> c2_infra

    with Cluster(
        "STAGE 5: EXFILTRATION",
        graph_attr={
            "bgcolor": "#161b2233",
            "style": "rounded",
            "color": "#8e44ad",
            "penwidth": "2",
            "fontcolor": "#8e44ad",
            "fontsize": "13",
            "labeljust": "l",
        },
    ):
        exfil_wallet = SQL("0x6981...aFCf5\nDORMANT — 0 txns\nZero victims")
        exfil_ftp = Server("FTP exfil servers\n857 devs compromised\n241,764 creds stolen")
        nuke = Server("nuke() anti-forensics\nWipes localStorage\nsessionStorage, DOM")

    c2_wallet >> Edge(label="drain attempt", color="#8e44ad", style="bold") >> exfil_wallet
    c2_infra >> Edge(label="credential dump", color="#8e44ad", style="bold") >> exfil_ftp
    c2_wallet >> Edge(label="evidence destruction", color="#2c3e50", style="dashed") >> nuke


# ─────────────────────────────────────────────────────────────────────────────
# 2. C2 INFRASTRUCTURE MAP
# ─────────────────────────────────────────────────────────────────────────────

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.network import Internet
from diagrams.onprem.compute import Server
from diagrams.onprem.client import Users
from diagrams.generic.database import SQL

with Diagram(
    "Lazarus 19-Day Campaign — C2 Infrastructure",
    filename="02_c2_infrastructure",
    show=False,
    direction="TB",
    graph_attr={**graph_attr, "ranksep": "1.0", "nodesep": "0.6"},
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png",
):
    with Cluster(
        "DELIVERY",
        graph_attr={
            "bgcolor": "#1a1f2933",
            "style": "rounded",
            "color": "#3498db",
            "penwidth": "2.5",
            "fontcolor": "#3498db",
            "fontsize": "14",
        },
    ):
        gh = Users("GitHub Discussions\nMass @mentions")
        email = Internet("notifications@\ngithub.com")
        redir = Internet("share.google/*\nRedirects")
        gh >> email >> redir

    with Cluster(
        "LANDING PAGES",
        graph_attr={
            "bgcolor": "#1a1f2933",
            "style": "rounded",
            "color": "#e74c3c",
            "penwidth": "2.5",
            "fontcolor": "#e74c3c",
            "fontsize": "14",
        },
    ):
        lp1 = Internet("token-claw.xyz\nWallet phishing")
        lp2 = Internet("Fake CVE advisory")
        lp3 = Internet("Fake job portal")

    redir >> Edge(color="#27ae60") >> lp1
    redir >> Edge(color="#e74c3c") >> lp2
    redir >> Edge(color="#2980b9") >> lp3

    with Cluster(
        "COMMAND & CONTROL",
        graph_attr={
            "bgcolor": "#1a1f2933",
            "style": "rounded",
            "color": "#f39c12",
            "penwidth": "2.5",
            "fontcolor": "#f39c12",
            "fontsize": "14",
        },
    ):
        wc = Server("watery-compost.today\neleven.js C2")
        pg = Server("360scanner.store\nPylangGhost C2")

        with Cluster(
            "Vercel Staging",
            graph_attr={
                "bgcolor": "#0d111733",
                "style": "dashed,rounded",
                "color": "#8b949e",
                "fontcolor": "#8b949e",
            },
        ):
            v1 = Server("tetrismic\n.vercel.app")
            v2 = Server("server-check-genimi\n.vercel.app")

        with Cluster(
            "Majestic Hosting — AS396073",
            graph_attr={
                "bgcolor": "#0d111733",
                "style": "dashed,rounded",
                "color": "#e74c3c",
                "fontcolor": "#e74c3c",
            },
        ):
            m1 = Server("147.124.213.232\n:1244")
            m2 = Server("147.124.212.125\n:1244")
            m3 = Server("216.250.251.87\n:1247")
            m4 = Server("147.124.214.129\n:1244")

        with Cluster(
            "TIER-NET — AS397423",
            graph_attr={
                "bgcolor": "#0d111733",
                "style": "dashed,rounded",
                "color": "#f39c12",
                "fontcolor": "#f39c12",
            },
        ):
            t1 = Server("66.235.63.55\nMetaMask injector")
            t2 = Server("66.235.168.238\n:22411 binary proto")
            t3 = Server("45.59.163.55\nChrome stealer")

    lp1 >> Edge(color="#27ae60") >> wc
    lp2 >> Edge(color="#e74c3c") >> m1
    lp3 >> Edge(color="#2980b9") >> v1
    v1 >> Edge(style="dashed", color="#8b949e") >> m2
    v2 >> Edge(style="dashed", color="#8b949e") >> m3

    with Cluster(
        "EXFILTRATION",
        graph_attr={
            "bgcolor": "#1a1f2933",
            "style": "rounded",
            "color": "#8e44ad",
            "penwidth": "2.5",
            "fontcolor": "#8e44ad",
            "fontsize": "14",
        },
    ):
        ftp1 = Server("195.201.104.53\nFTP :21")
        ftp2 = Server("144.172.89.198\nFTP :21")
        ftp3 = Server("216.126.227.239\nFTP :21")
        wallet = SQL("0x6981...aFCf5\nDORMANT")

    m1 >> Edge(color="#8e44ad") >> ftp1
    m4 >> Edge(color="#8e44ad") >> ftp2
    t1 >> Edge(color="#8e44ad") >> ftp3
    wc >> Edge(label="drain attempt", color="#8e44ad", style="bold") >> wallet


# ─────────────────────────────────────────────────────────────────────────────
# 3. ATTRIBUTION TREE
# ─────────────────────────────────────────────────────────────────────────────

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.programming.language import JavaScript, Python, Go
from diagrams.generic.blank import Blank

with Diagram(
    "Lazarus 19-Day Campaign — Attribution",
    filename="03_attribution",
    show=False,
    direction="TB",
    graph_attr={**graph_attr, "ranksep": "1.4", "nodesep": "1.0"},
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png",
):
    rgb = Server("DPRK RGB\nReconnaissance\nGeneral Bureau")

    with Cluster(
        "LAZARUS GROUP — G0032",
        graph_attr={
            "bgcolor": "#1a1f2933",
            "style": "rounded",
            "color": "#e74c3c",
            "penwidth": "3",
            "fontcolor": "#e74c3c",
            "fontsize": "15",
        },
    ):
        with Cluster(
            "Famous Chollima / WaterPlum",
            graph_attr={
                "bgcolor": "#0d111733",
                "style": "dashed,rounded",
                "color": "#d35400",
                "fontcolor": "#d35400",
                "fontsize": "12",
            },
        ):
            golangghost = Go("GolangGhost\nRAT")
            pylangghost = Python("PylangGhost\nRAT")
            w1 = Server("WAVE 1\nOpenClaw Airdrop\n2026-03-20")

        with Cluster(
            "Contagious Interview / G1052",
            graph_attr={
                "bgcolor": "#0d111733",
                "style": "dashed,rounded",
                "color": "#d35400",
                "fontcolor": "#d35400",
                "fontsize": "12",
            },
        ):
            beavertail = JavaScript("BeaverTail\nJS stealer")
            ottercookie = JavaScript("OtterCookie\nModular RAT")
            stoatwaffle = JavaScript("StoatWaffle\nVS Code malware")
            invisibleferret = Python("InvisibleFerret\nBackdoor")
            w2 = Server("WAVE 2\nFake VS Code CVE\n2026-03-27")

            with Cluster(
                "Front Companies",
                graph_attr={
                    "bgcolor": "#0d111733",
                    "style": "dashed,rounded",
                    "color": "#922b21",
                    "fontcolor": "#922b21",
                },
            ):
                f1 = Server("BlockNovas LLC\nFBI SEIZED")
                f2 = Server("SoftGlide LLC\nACTIVE")
                f3 = Server("Angeloper Agency\nACTIVE")

        with Cluster(
            "BlueNoroff / UNC1069",
            graph_attr={
                "bgcolor": "#0d111733",
                "style": "dashed,rounded",
                "color": "#d35400",
                "fontcolor": "#d35400",
                "fontsize": "12",
            },
        ):
            axios = Server("axios npm compromise\nCVE-2026-33634\nCVSS 9.4, KEV-listed")

        w3 = Server("WAVE 3\nUniswap Recruitment\n2026-04-08")

        with Cluster(
            "Major Financial Operations",
            graph_attr={
                "bgcolor": "#0d111733",
                "style": "dashed,rounded",
                "color": "#8e44ad",
                "fontcolor": "#8e44ad",
            },
        ):
            bybit = Server("Bybit — $1.5B\nFeb 2025")
            drift = Server("Drift Protocol — $285M\nApr 2026")
            total = Server("ALL-TIME TOTAL\n$6.75B+ stolen")

    rgb >> Edge(label="commands", color="#c0392b", style="bold") >> w1
    rgb >> Edge(color="#c0392b", style="bold") >> w2
    rgb >> Edge(color="#c0392b", style="bold") >> w3
    rgb >> Edge(color="#c0392b", style="bold") >> bybit


# ─────────────────────────────────────────────────────────────────────────────
# 4. WAVE COMPARISON
# ─────────────────────────────────────────────────────────────────────────────

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet
from diagrams.programming.language import JavaScript, Go
from diagrams.generic.os import Windows
from diagrams.generic.database import SQL

with Diagram(
    "Lazarus 19-Day Campaign — Three Waves",
    filename="04_wave_comparison",
    show=False,
    direction="LR",
    graph_attr={**graph_attr, "ranksep": "0.8", "nodesep": "0.6"},
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png",
):
    with Cluster(
        "WAVE 1: GREED\nMar 20, 2026",
        graph_attr={
            "bgcolor": "#1a1f2933",
            "style": "rounded",
            "color": "#27ae60",
            "penwidth": "3",
            "fontcolor": "#27ae60",
            "fontsize": "14",
        },
    ):
        w1_lure = Internet("Fake $5K CLAW\ntoken airdrop")
        w1_land = Internet("token-claw.xyz")
        w1_pay = JavaScript("eleven.js\nwallet drainer")
        w1_c2 = Server("watery-compost\n.today")
        w1_stat = SQL("SINKHOLED")
        w1_lure >> w1_land >> w1_pay >> w1_c2 >> w1_stat

    with Cluster(
        "WAVE 2: FEAR\nMar 27, 2026",
        graph_attr={
            "bgcolor": "#1a1f2933",
            "style": "rounded",
            "color": "#e74c3c",
            "penwidth": "3",
            "fontcolor": "#e74c3c",
            "fontsize": "14",
        },
    ):
        w2_lure = Internet("Fake critical\nVS Code CVE")
        w2_land = Windows("Fake security\nadvisory page")
        w2_pay = JavaScript("StoatWaffle\nVS Code malware")
        w2_c2 = Server("Majestic Hosting\nAS396073")
        w2_stat = Server("ACTIVE")
        w2_lure >> w2_land >> w2_pay >> w2_c2 >> w2_stat

    with Cluster(
        "WAVE 3: AMBITION\nApr 8, 2026",
        graph_attr={
            "bgcolor": "#1a1f2933",
            "style": "rounded",
            "color": "#2980b9",
            "penwidth": "3",
            "fontcolor": "#2980b9",
            "fontsize": "14",
        },
    ):
        w3_lure = Internet("Fake Uniswap job\n$300K-$450K")
        w3_land = Internet("Fake recruiter\ninterview portal")
        w3_pay = Go("GolangGhost\nPylangGhost RAT")
        w3_c2 = Server("Contagious Interview\ninfrastructure")
        w3_stat = Server("ACTIVE")
        w3_lure >> w3_land >> w3_pay >> w3_c2 >> w3_stat


# ─────────────────────────────────────────────────────────────────────────────
# 5. STIX BUNDLE COMPOSITION
# ─────────────────────────────────────────────────────────────────────────────

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.generic.blank import Blank

with Diagram(
    "Lazarus 19-Day Campaign — STIX 2.1 Bundle",
    filename="05_stix_bundle",
    show=False,
    direction="TB",
    graph_attr={**graph_attr, "ranksep": "0.8"},
    node_attr=node_attr,
    edge_attr=edge_attr,
    outformat="png",
):
    with Cluster(
        "80 STIX 2.1 OBJECTS",
        graph_attr={
            "bgcolor": "#1a1f2933",
            "style": "rounded",
            "color": "#58a6ff",
            "penwidth": "2",
            "fontcolor": "#58a6ff",
            "fontsize": "15",
        },
    ):
        with Cluster(
            "Core Objects",
            graph_attr={
                "bgcolor": "#0d111733",
                "style": "dashed,rounded",
                "color": "#8b949e",
                "fontcolor": "#8b949e",
            },
        ):
            ta = Server("1 Threat Actor\nLazarus Group")
            camp = Server("3 Campaigns\nAirdrop / CVE / Job")
            mal = Server("6 Malware\neleven.js / GolangGhost\nPylangGhost / StoatWaffle\nBeaverTail / OtterCookie")

        with Cluster(
            "Indicators (26)",
            graph_attr={
                "bgcolor": "#0d111733",
                "style": "dashed,rounded",
                "color": "#3498db",
                "fontcolor": "#3498db",
            },
        ):
            ind_dom = Server("4 Domains")
            ind_ip = Server("13 IP Addresses")
            ind_url = Server("3 URLs")
            ind_hash = Server("5 SHA-256 Hashes")
            ind_wallet = Server("1 Crypto Wallet")

        with Cluster(
            "Context",
            graph_attr={
                "bgcolor": "#0d111733",
                "style": "dashed,rounded",
                "color": "#8b949e",
                "fontcolor": "#8b949e",
            },
        ):
            ap = Server("4 Attack Patterns\nT1566.003 / T1204.002\nT1555.003 / T1059.007")
            vuln = Server("1 Vulnerability\nCVE-2026-40271\nFABRICATED")
            infra = Server("1 Infrastructure\nC2 network")

        rels = Server("34 Relationships\nuses / attributed-to\ncommunicates-with / indicates")

    ta >> Edge(color="#58a6ff", style="dashed") >> camp
    camp >> Edge(color="#58a6ff", style="dashed") >> mal
    mal >> Edge(color="#58a6ff", style="dashed") >> rels


print("\nAll diagrams generated successfully:")
for f in sorted(os.listdir(".")):
    if f.endswith(".png"):
        size_kb = os.path.getsize(f) / 1024
        print(f"  {f} ({size_kb:.0f} KB)")
