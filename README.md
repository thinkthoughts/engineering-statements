# engineering-statements

Structured claims, constraints, and artifacts for agentic science workflows.

Engineering Statements are portable specifications that translate scientific intent into reproducible next steps.

---

## Core idea

Scientific papers describe discoveries.

Engineering Statements specify how those discoveries can be inspected, communicated, and extended.

```text
paper or source
↓
Engineering Statement (YAML)
↓
notebook
↓
lab report
↓
infographic
↓
published artifact
```

The goal is not to replace papers, repositories, or researchers.

The goal is to preserve scientific intent while making next steps more accessible and reproducible.

---

## Repository structure

```text
engineering-statements/
├── notebooks/
├── outputs/
├── src/
│   └── engineering_statements/
├── statements/
├── templates/
├── LICENSE
├── README.md
└── pyproject.toml
```

### `statements/`

Primary Engineering Statement artifacts.

Human-readable YAML specifications describing:

* objectives
* contexts
* constraints
* evidence
* outputs
* next steps

Examples:

```text
statements/
├── agapi-agents.yaml
├── 2606-13619.yaml
├── 2606-13590.yaml
└── 2606-12618.yaml
```

---

### `notebooks/`

Companion notebooks.

Reader-facing demonstrations that introduce vocabulary, inspect toy examples, generate specifications, and support comprehension.

Examples:

```text
notebooks/
├── 00_2606-13619.ipynb
├── 00_2606-13590.ipynb
└── 00_2606-12618.ipynb
```

---

### `src/engineering_statements/`

Lightweight Python utilities supporting Engineering Statements.

Responsibilities may include:

* YAML loading
* schema validation
* notebook helpers
* report utilities

The source code supports the statements.

The statements remain primary.

---

### `templates/`

Reusable templates.

Examples:

```text
templates/
├── statement.yaml
├── notebook.md
├── lab_report.md
└── infographic.md
```

Templates help establish consistent workflows without constraining scientific content.

---

### `outputs/`

Generated local artifacts.

This directory is intended for derived files and experiments.

Primary specifications should remain in `statements/`.

---

## Workflow

```text
discover paper
↓
read abstract and introduction
↓
identify scientific intent
↓
draft Engineering Statement YAML
↓
generate notebook
↓
generate lab report
↓
generate infographic
↓
publish artifacts
```

---

## Current examples

### Number Theory

**arXiv:2606.13619**

Split primes and the Elekes–Rónyai problem

Outputs:

* Engineering Statement
* notebook
* lab report
* infographic

---

**arXiv:2606.13590**

Some new modular Nahm sums of ranks 3 and 4

Outputs:

* Engineering Statement
* notebook
* lab report
* infographic

---

### AI Safety

**arXiv:2606.12618**

Did you lie? Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms

Outputs:

* Engineering Statement
* notebook
* lab report
* infographic

---

## AGAPI connection

Engineering Statements are intended to complement agentic scientific systems.

The initial demonstration focuses on AGAPI as a bridge between:

```text
scientific infrastructure
↓
structured specifications
↓
reproducible next steps
```

See:

```text
statements/agapi-agents.yaml
```

for the current Engineering Statement derived from AGAPI-related work.

---

## Related projects

Climate Reality

https://climatereality.app

Engineering Statements feature

https://climatereality.app/statements/

Lab Reports

https://labreports.app

---

## Philosophy

Climate Reality describes contexts and constraints.

Engineering Statements specify next steps in context.

Climate Democracy prescribes collaborative action.

Scientific intent can remain inspectable, reproducible, and portable across communities, disciplines, and tools.
