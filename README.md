# DevSecOps CI/CD Pipeline

Automated security scanning on every code push using GitHub Actions.

## Tools

| Tool | Purpose | What it catches |
|------|---------|-----------------|
| Bandit | Python SAST | Hardcoded secrets, shell injection, unsafe calls |
| pip-audit | Dependency scanning | Known CVEs in Python packages |
| Trivy | Filesystem / container scan | Misconfigs, vulnerable deps, secrets |

## Pipeline

Every `git push` triggers three parallel security jobs. Results appear in:
- The **Actions** tab (per-run logs)
- The **Security → Code scanning** tab (SARIF findings, persistent)
- **Artifacts** on each run (downloadable JSON/SARIF reports)

## Running locally

```bash
pip install bandit[sarif] pip-audit
bandit -r app/ -f text
pip-audit -r requirements.txt
```
