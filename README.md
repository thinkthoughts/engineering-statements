# engineering-statements

Canonical engineering objects for reproducible scientific publication.

Engineering Statements are human-authored YAML records that describe engineering objects and their publication metadata. They serve as the canonical source for notebooks, reports, repositories, websites, software, and other published artifacts.

---

## Engineering publication pipeline

```text
scientific source
        ↓
Engineering Statement (YAML)
        ↓
engineering object
        ↓
publication JSON
        ↓
site builders
        ↓
published artifacts
```

Scientific papers describe discoveries.

Engineering Statements specify reusable engineering objects.

The goal is to preserve scientific intent while making engineering work inspectable, reproducible, and portable across repositories, websites, and engineering workflows.

---

## Repository structure

```text
engineering-statements/

├── statements/
├── json/
├── notebooks/
├── templates/
├── src/
│   └── engineering_statements/
├── outputs/
├── LICENSE
├── README.md
└── pyproject.toml
```

---

## statements/

Canonical Engineering Statement records.

Each YAML file describes one engineering object.

Typical fields include:

```text
id
title
timestamp

primary_group
object_type
status

engineering_statement

targets

repository
artifacts

tags
```

Examples:

```text
statements/

specification-grammar.yaml
engineering-status.yaml
engineering-template.yaml

2606-13619.yaml
2606-13590.yaml
2606-12618.yaml
```

The statements are the primary authored content.

---

## json/

Generated publication objects.

JSON is generated from the Engineering Statements and consumed by websites, builders, search, and publication tools.

Current outputs include:

```text
json/

latest.json

engineering.json
research.json
models.json
hardware.json
seminars.json
notebooks.json
software.json
policies.json
context.json
```

Each JSON file contains engineering objects whose `primary_group` matches the filename.

The JSON files are generated rather than edited directly.

---

## notebooks/

Reader-facing demonstrations.

Notebooks introduce vocabulary, inspect examples, generate figures, and explain Engineering Statements.

Notebook 00 introduces reusable engineering context shared across repositories.

---

## templates/

Reusable publication templates.

Examples:

```text
templates/

statement.yaml
notebook.md
lab_report.md
infographic.md
```

Templates establish consistent engineering workflows while allowing each engineering object to remain independent.

---

## src/

Supporting utilities.

Responsibilities may include:

- YAML loading
- schema validation
- publication JSON generation
- notebook helpers
- report utilities
- site-builder helpers

The software supports the statements.

The statements remain primary.

---

## outputs/

Derived local artifacts.

Generated notebooks, figures, temporary exports, and experiments.

Canonical engineering objects remain in `statements/`.

---

# Workflow

```text
discover source
        ↓
identify engineering intent
        ↓
Engineering Statement
        ↓
engineering object
        ↓
publication JSON
        ↓
Notebook
        ↓
Lab Report
        ↓
Infographic
        ↓
Website
```

---

# Primary groups

Engineering objects currently publish into one primary group.

```text
Engineering
Research
Models
Hardware
Seminars
Notebooks
Software
Policies
Context
```

Additional publication groupings may be generated later without changing the Engineering Statements themselves.

---

# Reference standards

Engineering Statements complement several reference repositories.

## Specification Grammar

Defines relationships among engineering concepts.

## Engineering Status

Defines engineering lifecycle vocabulary.

```text
🟢 Ready

🟡 Developing

🔴 Revision Required
```

## Engineering Template

Defines reusable repository structure.

Engineering Statements connect these reference standards into publishable engineering objects.

---

# Current examples

Reference standards

- Specification Grammar
- Engineering Status
- Engineering Template

Research examples

- arXiv:2606.13619
- arXiv:2606.13590
- arXiv:2606.12618

Each engineering object may publish notebooks, reports, repositories, software, figures, websites, and other artifacts while preserving a single canonical Engineering Statement.

---

# Related projects

- Specification Grammar
- Engineering Status
- Engineering Template

- labreports.app
- danhawkley.dev
- Climate Reality

---

# Philosophy

Scientific papers communicate discoveries.

Engineering Statements communicate reusable engineering objects.

Those engineering objects become the canonical source for publication across notebooks, reports, repositories, websites, software, seminars, and future engineering workflows.

Engineering Statements preserve scientific intent while making engineering work inspectable, reproducible, and portable.
