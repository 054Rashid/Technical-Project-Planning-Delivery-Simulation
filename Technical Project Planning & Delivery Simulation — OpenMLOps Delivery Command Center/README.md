# OpenMLOps Delivery Command Center

**Self-directed technical project planning & delivery simulation**

A portfolio project that simulates how a Junior Project Manager could plan, coordinate, control, and close an enterprise MLOps rollout for a global retail organization.

The simulated program delivers a production-oriented machine learning platform for demand forecasting using open-source technologies such as **Ubuntu, Docker, Kubernetes, MLflow, Feast, Python, and GitHub Actions**.

> **Disclosure:** This is a self-directed simulation created for portfolio and interview practice. The organization, stakeholders, financial figures, delivery dates, and project outcomes are illustrative. They are not claims of professional employment or customer work.

## Business problem

The fictional client, **Northstar Retail Group**, operates 240 stores and currently manages demand forecasting through fragmented spreadsheets and manually executed data workflows. Forecast releases take too long, data-quality issues are discovered late, and model changes are difficult to reproduce.

The project objective is to design and plan a scalable open-source MLOps delivery program that can:

- improve forecast-release reliability;
- reduce manual model-release effort;
- establish reproducible experimentation and feature management;
- create visible ownership for risks, dependencies, and third-party deliverables;
- give business and technical stakeholders a single source of project status.

## Target outcomes (illustrative)

| KPI | Baseline | Target | Simulated close | Status |
|---|---:|---:|---:|---|
| Forecast release cycle | 10 business days | <= 4 days | 3.5 days | Met |
| Manual release effort | 24 engineer-hours/release | <= 10 | 8 | Met |
| Reproducible experiments | 35% | >= 95% | 97% | Met |
| Feature lineage coverage | 20% | >= 90% | 92% | Met |
| Critical blockers open at launch | 7 | <= 2 | 1 | Met |
| Forecast accuracy improvement | Baseline | +8% relative | +9.4% | Met |

All results in this table are **simulated project-close results** for the portfolio case study.

## Why this project is relevant to technical project management

This repository demonstrates the full project lifecycle rather than only a technical model:

1. **Initiation** — business case, objectives, success criteria, assumptions, and constraints.
2. **Planning** — work breakdown structure, milestones, delivery roadmap, dependencies, resources, RACI, and communications.
3. **Execution** — sprint/release planning, issue tracking, change control, stakeholder updates, and technical coordination.
4. **Monitoring & control** — RAID management, project-health KPIs, risk escalation, schedule tracking, and change impact analysis.
5. **Closure** — acceptance criteria, outcome measurement, lessons learned, handover, and post-launch backlog.

## Repository structure

```text
openmlops-delivery-command-center/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   ├── 00_project_overview.md
│   ├── 01_project_charter.md
│   ├── 02_business_case.md
│   ├── 03_scope_wbs.md
│   ├── 04_delivery_roadmap.md
│   ├── 05_stakeholder_register.csv
│   ├── 06_raci_matrix.csv
│   ├── 07_raid_log.csv
│   ├── 08_risk_matrix.csv
│   ├── 09_communication_plan.md
│   ├── 10_release_plan.md
│   ├── 11_change_control_log.csv
│   ├── 12_status_report.md
│   ├── 13_closure_report.md
│   ├── 14_architecture.md
│   └── 15_interview_story.md
├── data/
│   ├── project_tasks.csv
│   ├── project_kpis.csv
│   └── resource_plan.csv
├── src/
│   └── tracker.py
├── tests/
│   └── test_tracker.py
└── .github/
    ├── pull_request_template.md
    └── ISSUE_TEMPLATE/
        ├── project-risk.md
        └── change-request.md
```

## Run the project dashboard

The tracker uses only Python's standard library.

```bash
python src/tracker.py
```

It prints:

- schedule completion;
- milestone health;
- open risks/issues;
- delivery KPIs;
- overall project health;
- recommended management actions.

It also creates an HTML report at `output/project_dashboard.html`.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Suggested GitHub setup

```bash
git init
git add .
git commit -m "Initial project delivery simulation"
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

## How to discuss this in an interview

Use the framing:

> “I built a self-directed project-management simulation around an enterprise MLOps rollout. I treated it like a real delivery program: I defined the business case and scope, created a WBS and roadmap, mapped stakeholders and responsibilities, maintained a RAID log and change-control process, and built a lightweight Python project-health dashboard. I also created the technical architecture so I could coordinate effectively with the engineering side. The business impact figures are simulated targets and close results, not production claims.”

## Core competencies demonstrated

- Project planning and delivery
- Schedule / milestone management
- Scope and change control
- Risk and issue management
- Stakeholder communication
- Dependency management
- Technical coordination
- MLOps architecture literacy
- KPI / project-health reporting
- Documentation and handover
- Python automation
- Open-source technology awareness
