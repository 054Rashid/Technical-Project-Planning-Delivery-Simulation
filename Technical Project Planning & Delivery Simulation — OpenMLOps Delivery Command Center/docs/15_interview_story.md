# Interview Story

## 60-second version

“I built a self-directed project-planning and delivery simulation for an enterprise MLOps rollout. I used a demand-forecasting use case because it requires coordination between business, data, ML, platform, security, and operations teams. I started with the business case and project charter, then created the WBS, roadmap, stakeholder register, RACI, RAID log, communication plan, release gates, and change-control process. I also mapped the technical architecture using open-source components such as MLflow, Feast, Docker, Kubernetes, Ubuntu, and GitHub Actions. Finally, I wrote a small Python dashboard that converts project task and KPI data into a delivery-health report. The business impact numbers are simulated, but the project demonstrates how I think about scope, dependencies, risks, communication, and technical delivery.”

## Example STAR answer — managing a risk

**Situation:** A third-party data feed was on the critical path and a delay could have pushed UAT.

**Task:** Protect the pilot date while keeping data quality requirements intact.

**Action:** I logged the dependency in the RAID register, assigned a clear owner, moved the sample-feed validation earlier, and created a mitigation path using a controlled test dataset. I also scheduled an early schema review so the issue would be visible before the release window.

**Result:** In the simulation, the dependency was contained without moving the pilot date.

## Example STAR answer — handling a change request

**Situation:** A business stakeholder requested an extra dashboard filter during UAT.

**Task:** Decide whether the enhancement should enter the release without compromising the committed date.

**Action:** I recorded the request, assessed scope/schedule/risk impact, and compared it with the acceptance criteria. Because it was useful but not required for acceptance, the request was deferred to the post-launch backlog.

**Result:** The simulated project protected the release date while preserving the enhancement request.
