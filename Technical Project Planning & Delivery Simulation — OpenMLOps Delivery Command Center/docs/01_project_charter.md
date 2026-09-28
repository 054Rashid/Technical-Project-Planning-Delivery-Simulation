# Project Charter

## 1. Purpose

Create a repeatable delivery framework for an enterprise MLOps platform that enables Northstar Retail Group to move demand-forecasting models from experimentation to controlled production releases.

## 2. Problem statement

The current forecasting workflow relies on disconnected notebooks, manual data preparation, spreadsheet-based handoffs, and undocumented model changes. This causes release delays, inconsistent outputs, weak traceability, and operational risk.

## 3. Objectives

- Reduce the model-release cycle from 10 business days to four or fewer.
- Reduce manual release effort by at least 50%.
- Achieve at least 95% reproducibility for tracked experiments.
- Establish feature ownership and lineage for pilot features.
- Launch one business pilot with documented rollback and support processes.

## 4. Success criteria

| Area | Success criterion |
|---|---|
| Schedule | Pilot operational by end of Week 16 |
| Quality | Critical validation failures blocked before release |
| Reproducibility | >= 95% of pilot experiments traceable |
| Operations | Rollback procedure tested before go-live |
| Business | Product owner accepts forecast outputs |
| Documentation | Architecture, runbooks, ownership and handover complete |

## 5. In scope

- Pilot demand-forecasting use case
- Data quality controls
- Experiment tracking
- Feature management
- Containerized model packaging
- Kubernetes deployment path
- CI quality gates
- Monitoring and release readiness
- User acceptance and handover

## 6. Out of scope

- Full enterprise-wide rollout to all 240 stores
- Replacing the client's ERP
- Building a new data warehouse
- Developing a proprietary cloud platform
- Long-term production support beyond the pilot handover

## 7. Governance

- Sponsor: budget and strategic decisions
- Project manager: schedule, scope, risks, communications, dependencies
- Product owner: business acceptance and priority
- Tech lead: technical design and engineering decisions
- Data/ML leads: model and data delivery
- Security: review of access and deployment controls
