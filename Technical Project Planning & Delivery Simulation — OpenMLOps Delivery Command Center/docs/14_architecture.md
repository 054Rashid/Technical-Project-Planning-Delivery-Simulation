# Technical Architecture

The architecture is intentionally simple enough for a portfolio simulation while exposing realistic coordination points between data, ML, platform, security, and business teams.

```mermaid
flowchart LR
    A[Sales / Inventory Data] --> B[Data Validation]
    B --> C[Feature Preparation]
    C --> D[Feast Feature Store]
    C --> E[ML Training]
    E --> F[MLflow Tracking & Registry]
    F --> G[Model Package]
    G --> H[Docker Image]
    H --> I[Kubernetes Deployment]
    I --> J[Forecast API / Batch Job]
    J --> K[Business Forecast Output]
    I --> L[Monitoring & Alerts]
    M[GitHub Actions CI] --> H
    M --> F
```

## Component responsibilities

| Component | Responsibility | Primary owner |
|---|---|---|
| Data validation | Schema, completeness, consistency checks | Data Lead |
| Feature store | Reusable feature definitions and serving consistency | Data/ML Leads |
| MLflow | Experiment tracking and model lifecycle metadata | ML Lead |
| Model package | Reproducible model artifact | ML Lead |
| Docker | Portable runtime image | Platform Engineer |
| Kubernetes | Deployment and scaling | Platform Engineer |
| GitHub Actions | Automated checks and packaging workflow | Engineering Lead |
| Monitoring | Service/model health visibility | Operations Lead |

## Architecture decisions

### Decision 1 — Open-source first

The simulation prioritizes open-source components to reduce platform lock-in and align the portfolio with enterprise open-source environments.

### Decision 2 — Separate technical ownership from delivery ownership

The Project Manager is accountable for coordination and delivery outcomes, while technical leads remain accountable for engineering decisions.

### Decision 3 — Gate production-like releases

A release cannot pass from technical readiness to business pilot unless data, security, deployment, rollback, and acceptance checks are complete.
