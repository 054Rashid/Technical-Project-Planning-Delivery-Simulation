from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean
from html import escape

ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "data" / "project_tasks.csv"
KPIS = ROOT / "data" / "project_kpis.csv"
OUTPUT = ROOT / "output"


def load_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def as_float(value: str) -> float:
    return float(value.replace("%", ""))


def project_health(tasks, kpis):
    completion = mean(as_float(t["Percent_Complete"]) for t in tasks)
    open_high = sum(1 for t in tasks if t["Status"] != "Done" and t["Priority"] == "High")
    met = 0
    for k in kpis:
        baseline = as_float(k["Baseline"])
        target = as_float(k["Target"])
        actual = as_float(k["Simulated_Close"])
        if k["Direction"] == "Higher":
            met += actual >= target
        else:
            met += actual <= target
    kpi_rate = met / len(kpis) * 100 if kpis else 0
    if completion >= 98 and open_high == 0 and kpi_rate >= 90:
        health = "GREEN"
    elif completion >= 90 and open_high <= 1 and kpi_rate >= 70:
        health = "AMBER"
    else:
        health = "RED"
    return completion, open_high, kpi_rate, health


def build_html(tasks, kpis):
    completion, open_high, kpi_rate, health = project_health(tasks, kpis)
    rows = "".join(
        f"<tr><td>{escape(t['ID'])}</td><td>{escape(t['Workstream'])}</td>"
        f"<td>{escape(t['Task'])}</td><td>{escape(t['Owner'])}</td>"
        f"<td>{escape(t['Status'])}</td><td>{escape(t['Percent_Complete'])}%</td></tr>"
        for t in tasks
    )
    kpi_rows = "".join(
        f"<tr><td>{escape(k['KPI'])}</td><td>{escape(k['Baseline'])}</td>"
        f"<td>{escape(k['Target'])}</td><td>{escape(k['Simulated_Close'])}</td>"
        f"<td>{escape(k['Unit'])}</td></tr>"
        for k in kpis
    )
    return f"""<!doctype html>
<html lang='en'>
<head>
<meta charset='utf-8'>
<title>OpenMLOps Delivery Dashboard</title>
<style>
body{{font-family:Arial, sans-serif;max-width:1200px;margin:40px auto;padding:0 20px;background:#f5f7fa;color:#1f2937}}
.card{{background:white;border-radius:12px;padding:20px;margin:16px 0;box-shadow:0 2px 10px rgba(0,0,0,.06)}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}}
.metric{{font-size:28px;font-weight:700}} .label{{color:#64748b;font-size:13px}}
table{{width:100%;border-collapse:collapse}} th,td{{padding:9px;border-bottom:1px solid #e5e7eb;text-align:left;font-size:14px}} th{{background:#f8fafc}}
.badge{{display:inline-block;padding:5px 9px;border-radius:999px;background:#dcfce7;font-weight:700}}
.small{{font-size:13px;color:#64748b}}
</style>
</head>
<body>
<h1>OpenMLOps Delivery Command Center</h1>
<p class='small'>Self-directed technical project planning & delivery simulation.</p>
<div class='card grid'>
<div><div class='label'>Overall Health</div><div class='metric'><span class='badge'>{health}</span></div></div>
<div><div class='label'>Task Completion</div><div class='metric'>{completion:.0f}%</div></div>
<div><div class='label'>Open High-Priority Tasks</div><div class='metric'>{open_high}</div></div>
<div><div class='label'>KPIs Meeting Target</div><div class='metric'>{kpi_rate:.0f}%</div></div>
</div>
<div class='card'><h2>Delivery Tasks</h2><table><tr><th>ID</th><th>Workstream</th><th>Task</th><th>Owner</th><th>Status</th><th>Complete</th></tr>{rows}</table></div>
<div class='card'><h2>KPI Closeout</h2><table><tr><th>KPI</th><th>Baseline</th><th>Target</th><th>Simulated Close</th><th>Unit</th></tr>{kpi_rows}</table></div>
<div class='card'><h2>Management actions</h2><ul><li>Keep the post-launch backlog separate from committed release scope.</li><li>Maintain monitoring of external data-feed dependencies after handover.</li><li>Use the same health metrics for future rollout waves.</li></ul></div>
</body></html>"""


def main() -> None:
    tasks = load_csv(TASKS)
    kpis = load_csv(KPIS)
    completion, open_high, kpi_rate, health = project_health(tasks, kpis)
    print("=== OpenMLOps Delivery Command Center ===")
    print(f"Overall health: {health}")
    print(f"Task completion: {completion:.0f}%")
    print(f"Open high-priority tasks: {open_high}")
    print(f"KPIs meeting target: {kpi_rate:.0f}%")
    OUTPUT.mkdir(exist_ok=True)
    report = OUTPUT / "project_dashboard.html"
    report.write_text(build_html(tasks, kpis), encoding="utf-8")
    print(f"HTML dashboard: {report.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
