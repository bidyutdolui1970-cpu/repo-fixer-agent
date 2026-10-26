import tempfile
from pathlib import Path

from repo_fixer_agent import scan_repository


def test_scan_repository_reports_missing_readme_and_todo_markers():
    with tempfile.TemporaryDirectory() as temp_dir:
        repo = Path(temp_dir)
        (repo / "src").mkdir()
        (repo / "src" / "app.py").write_text("# TODO: improve this\nprint('hello')\n", encoding="utf-8")

        findings = scan_repository(repo)

        assert "README.md is missing" in findings
        assert "src/app.py contains TODO/FIXME markers" in findings


def test_scan_repository_reports_no_issues_when_clean():
    with tempfile.TemporaryDirectory() as temp_dir:
        repo = Path(temp_dir)
        (repo / "README.md").write_text("Project docs\n", encoding="utf-8")
        (repo / "app.py").write_text("print('clean')\n", encoding="utf-8")

        findings = scan_repository(repo)

        assert findings == ["No obvious issues found"]
