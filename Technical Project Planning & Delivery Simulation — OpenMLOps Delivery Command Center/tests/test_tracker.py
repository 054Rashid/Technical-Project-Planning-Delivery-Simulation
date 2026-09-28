import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from tracker import load_csv, project_health, TASKS, KPIS


class TrackerTests(unittest.TestCase):
    def test_project_is_green(self):
        tasks = load_csv(TASKS)
        kpis = load_csv(KPIS)
        completion, open_high, kpi_rate, health = project_health(tasks, kpis)
        self.assertEqual(health, "GREEN")
        self.assertEqual(completion, 100)
        self.assertEqual(open_high, 0)
        self.assertEqual(kpi_rate, 100)

    def test_task_and_kpi_files_load(self):
        self.assertGreater(len(load_csv(TASKS)), 10)
        self.assertGreater(len(load_csv(KPIS)), 5)


if __name__ == "__main__":
    unittest.main()
