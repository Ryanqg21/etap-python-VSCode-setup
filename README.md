# ETAP Python Automation

Repeatable power system studies in **ETAP 24**, driven from **Python** and **VS Code**.

## Why this repo

Running a study by hand in the ETAP interface works for one case, but it gets slow when I need to repeat it, compare scenarios or collect results. The ETAP Python API lets me run studies and read results from scripts instead. This repository is where I document that workflow, one small project at a time.

## Projects

| # | Project | What it covers | Status |
| - | ------- | -------------- | ------ |
| 1 | [ConectEtap](1.ConectEtap) | Environment setup, API connection test and a load flow on the IEEE 4-bus example | ✅ Done |
| 2 | CortoCircuito | Short-circuit study driven from Python | 🔜 Next |
| 3 | Results to Power BI | Exporting study results to tables for dashboards | 📝 Planned |

## Tools

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)

**Power systems:** ETAP 24 · ETAP Python API

## Getting started

Each project has its own README with step-by-step instructions. All projects share one virtual environment (`.venv`) in the repository root, which is not uploaded, so run commands from this folder. Start with [1.ConectEtap](1.ConectEtap), which explains how to create the environment and connect to ETAP.

## Repository structure

```
ETAP 24\
├── 1.ConectEtap\        connection setup and load flow example
├── 2.CortoCircuito\     (coming soon)
├── .gitignore
└── README.md
```

---

Made by [@Ryanqg21](https://github.com/Ryanqg21). ETAP and its Python API belong to their respective owner and require a valid license.