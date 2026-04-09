# Vajra — Deterministic Semantic Reduction Engine

## What It Is

Vajra is a CLI tool that performs deterministic structural analysis on data files. Given any structured input, it extracts shape, entropy, anomalies, fingerprints, cross-field relationships, and drift — producing byte-identical output for identical inputs. It is installed globally at `/home/ops/.local/bin/vajra`.

## Supported Input Formats

| Format | Extensions | Notes |
|--------|-----------|-------|
| JSON | `.json` | Single documents |
| NDJSON | `.ndjson`, `.jsonl` | Newline-delimited records |
| YAML | `.yaml`, `.yml` | Multi-document supported |
| CSV | `.csv` | Comma-separated |
| TSV | `.tsv` | Tab-separated |
| Markdown | `.md`, `.markdown` | Parsed into section tree |
| PDF | `.pdf` | Text extraction |
| Source code | any | Requires `--input-format source --lang <language>` |
| Compressed | `.gz`, `.zst`, `.zstd` | Double extensions work: `.json.gz` |
| URLs | `http://`, `https://` | Fetched automatically |
| Stdin | `-` | Pipe data in |

---

## Commands

### `vajra inspect <INPUT>`
Full structural analysis. Returns:
- **Document metadata**: total nodes, max depth, distinct paths, raw size
- **Wildcard paths table**: every JSONPath with dominant type, count, type instability, null rate
- **BLAKE3 fingerprints**: path set hash, typed path hash, shape hash
- **Domain type recognition**: auto-detected semantic types (email, snake_case, etc.)

```bash
vajra inspect data.json
vajra inspect config.yaml --format json
```

### `vajra stats <INPUT>`
Statistical profile of every field:
- Shannon entropy (raw and normalized)
- Cardinality, count, max rarity (in bits)
- Numeric fields: min, max, mean, median, MAD, percentiles (p05, p25, p75, p95)
- Top values with frequency counts

```bash
vajra stats transactions.csv
vajra stats events.ndjson --format markdown
```

### `vajra anomalies <INPUT>`
Detects three classes of anomalies:
- **Type instabilities**: fields that change type across records
- **Numeric outliers**: MAD-based detection with z_mad scores (e.g., z_mad=10.97)
- **Rare values**: self-information rarity scoring

```bash
vajra anomalies claims.json
vajra anomalies logs.ndjson --format json
```

### `vajra fingerprint <INPUT>`
Structural identity hashes:
- **Path set hash**: BLAKE3 of all unique paths
- **Typed path hash**: BLAKE3 of paths + their types
- **Shape hash**: Merkle tree of document structure
- **Repeated motifs**: recurring subtree patterns with frequency

```bash
vajra fingerprint schema.json
```

### `vajra essence <INPUT>`
Concern-oriented reduction. Scores observations against the active profile's weight vector, ranks by importance, and renders in the requested format. This is the primary command for getting a human- or AI-readable summary.

```bash
# Plain-language narrative for non-technical readers
vajra essence data.json --profile staff

# Formal numbered findings for compliance
vajra essence data.json --profile auditor --format markdown

# Machine-optimized with token budget for LLM consumption
vajra essence data.json --profile ai --format compact-ai --budget 500

# Investigative framing with RISK/ALERT labels
vajra essence data.json --profile fraud

# Show score decomposition
vajra essence data.json --profile engineer --explain
```

### `vajra drift <BASELINE> <CANDIDATE>`
Schema drift detection between two documents:
- **Structural similarity**: Jaccard coefficient
- **Severity classification**: None / Low / Medium / High / Critical
- **Added/removed paths**
- **Distribution shifts**: Jensen-Shannon Divergence, 1D Wasserstein distance

```bash
vajra drift v1-api.json v2-api.json
vajra drift baseline.yaml candidate.yaml --format json
```

### `vajra cluster <INPUTS>...`
Groups structurally similar documents using MinHash signatures with Locality-Sensitive Hashing.

```bash
vajra cluster batch/*.json
vajra cluster responses_dir/
```

### `vajra invariants <INPUT> [--top-k N]`
Discovers cross-field relationships:
- **Conditional entropy** H(Y|X): how much knowing X reduces uncertainty about Y
- **Pointwise Mutual Information** (PMI): co-occurrence strength
- **Functional dependencies**: fields that perfectly determine others (strength=1.0)

```bash
vajra invariants users.json
vajra invariants events.csv --top-k 20
```

### `vajra query <INPUT> <EXPRESSION>`
Run analytical queries against a document. Returns scalar values.

**Available functions:**
| Function | Returns |
|----------|---------|
| `entropy($.path)` | Shannon entropy of values at path |
| `cardinality($.path)` | Number of distinct values |
| `null_rate($.path)` | Fraction of null values |
| `instability($.path)` | Type instability score |
| `count($.path)` | Number of values |
| `rarity($.path)` | Max self-information in bits |
| `depth($.path)` | Nesting depth |

**Supports comparisons:** `entropy($.status) > 0.5`

```bash
vajra query data.json 'entropy($.users[*].role)'
vajra query data.json 'cardinality($.events[*].type)'
vajra query data.json 'count($.records[*])'
```

### `vajra batch <DIRECTORY>`
Parallel batch analysis (Rayon) of all JSON files in a directory. Reports per-document summaries and aggregate statistics including common and rare paths.

```bash
vajra batch ./api_responses/
vajra batch ./logs/ --format json
```

### `vajra profiles`
Lists all available profiles (built-in and custom from `--config`).

---

## Profiles

Profiles control how `essence` scores and renders observations. Each has a distinct weight vector, vocabulary level, and rendering style.

| Profile | Weights Focus | Vocabulary | Rendering | Use Case |
|---------|--------------|------------|-----------|----------|
| **staff** | anomaly_strength=0.30, structural_coverage=0.25 | Plain language | Narrative: "What Stands Out" / "What This Likely Means" | Non-technical stakeholders |
| **engineer** | instability=0.25, balanced | Technical with JSONPath | List-based with scores | Development, debugging |
| **auditor** | concern_relevance=0.30, instability=0.20 | Formal | Numbered findings, completeness table, fingerprints | Compliance, audit trails |
| **ai** | entropy_signal=0.20, structural_coverage=0.20, anomaly_strength=0.20 | Terse, short keys | compact-ai JSON: `p`=path, `s`=score, `t`=type, `v`=value, `z`=z-score, `n`=count; includes `drill` section | LLM pipelines, automated processing |
| **fraud** | anomaly_strength=0.35, rarity=0.25 | Investigative | RISK/ALERT labels, pattern analysis | Fraud detection, investigation |

Custom profiles can be defined in a TOML config file and loaded with `--config`.

---

## Global Options

| Flag | Values | Description |
|------|--------|-------------|
| `--format` | `text` (default), `json`, `markdown`, `compact-ai` | Output format |
| `--profile` | `staff`, `engineer`, `auditor`, `ai`, `fraud` | Scoring/rendering profile |
| `--budget N` | integer | Token budget for essence (greedy knapsack by score-per-token) |
| `--redact` | flag | Redact SSN, email, phone, credit card with deterministic BLAKE3 hashes (preserves correlation) |
| `--streaming` | flag | Bounded-memory pipeline: DDSketch quantiles, Count-Min Sketch frequencies, Space-Saving top-k |
| `--input-format` | `json`, `ndjson`, `yaml`, `csv`, `tsv`, `markdown`, `pdf`, `source` | Force input format |
| `--lang` | `rust`, `python`, `javascript`, `go`, etc. | Source code language (with `--input-format source`) |
| `--config PATH` | file path | TOML file with custom profile definitions |
| `--explain` | flag | Include score decomposition in essence output |
| `--quiet` | flag | Suppress progress output |

---

## Algorithms

All algorithms satisfy: O(n) or O(n log n) time, peer-reviewed, fully deterministic.

| Algorithm | Purpose |
|-----------|---------|
| **BLAKE3** | All hashing (3-7x faster than SHA-256) |
| **Shannon Entropy** | Value diversity — distinguishes boilerplate from signal |
| **MAD** (Median Absolute Deviation) | Robust outlier detection with 50% breakdown point |
| **DDSketch** | Streaming quantile estimation with relative error guarantees |
| **Count-Min Sketch** | Streaming frequency estimation with conservative update |
| **Jensen-Shannon Divergence** | Symmetric distribution comparison, bounded [0,1] |
| **MinHash + LSH** | Scalable similarity search, O(n) indexing, sublinear queries |
| **1D Wasserstein** | Distribution shift magnitude in drift detection |

---

## Key Patterns for AI Usage

### Getting a quick data summary for context
```bash
vajra essence data.json --profile ai --format compact-ai --budget 500
```
Returns a token-efficient JSON with scored observations, anomalies, structural motifs, and a `drill` section suggesting follow-up queries.

### Checking if a data file has changed structurally
```bash
vajra fingerprint data.json
```
Compare BLAKE3 hashes across versions. Identical hashes = identical structure.

### Pre-flight check before processing
```bash
vajra anomalies input.json --format json
```
Machine-parseable anomaly report to validate data quality.

### Investigating suspicious records
```bash
vajra essence transactions.json --profile fraud
vajra query transactions.json 'rarity($.transactions[*].amount)'
```

### Comparing API versions
```bash
vajra drift old_response.json new_response.json --format json
```

### Redacting PII before analysis
```bash
vajra essence patient_records.json --profile staff --redact
```
Deterministic BLAKE3 redaction preserves correlation without exposing raw values.

### Discovering hidden field relationships
```bash
vajra invariants dataset.csv --top-k 30
```
Finds functional dependencies and co-occurrence patterns via conditional entropy and PMI.

### Source code structural analysis
```bash
vajra inspect app.rs --input-format source --lang rust
```
Parses into AST and analyzes as a tree structure.

---

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Analysis completed but anomalies found (with `--strict`) |
| 2 | Input error (file not found, parse failure) |
| 3 | Configuration error (invalid profile, bad config) |

---

## Configuration

Default config location: `~/.vajra/config.toml`

Custom profiles can be defined in TOML and loaded with `--config path/to/profiles.toml`.
