import json
import re
from collections import Counter
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
LOG_PATH = Path("/app/access.log")


def _load_report() -> dict:
    """Load the generated report."""
    return json.loads(REPORT_PATH.read_text())


def _expected_values():
    """Compute the expected values directly from the input log."""
    paths = Counter()
    ips = set()
    total = 0

    with LOG_PATH.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            total += 1
            ips.add(line.split()[0])

            m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if m:
                paths[m.group(1)] += 1

    return {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0],
    }


EXPECTED = _expected_values()


def test_total_requests_success_criterion():
    """Success Criterion 1: report.json contains the correct total_requests value."""
    report = _load_report()
    assert report["total_requests"] == EXPECTED["total_requests"]


def test_unique_ips_success_criterion():
    """Success Criterion 2: report.json contains the correct unique_ips value."""
    report = _load_report()
    assert report["unique_ips"] == EXPECTED["unique_ips"]


def test_top_path_success_criterion():
    """Success Criterion 3: report.json contains the correct top_path value."""
    report = _load_report()
    assert report["top_path"] == EXPECTED["top_path"]