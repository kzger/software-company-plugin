"""Check the files and discovery contract of the local Codex App plugin."""

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "plugins/software-company"
SKILL = PACKAGE / "skills/software-company"


class PackageTests(unittest.TestCase):
    def test_marketplace_resolves_local_app_plugin(self):
        marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
        manifest = json.loads((PACKAGE / "plugin.json").read_text(encoding="utf-8"))
        entry = next(item for item in marketplace["plugins"] if item["name"] == manifest["name"])
        self.assertEqual(entry["source"]["source"], "local")
        self.assertEqual((ROOT / entry["source"]["path"]).resolve(), PACKAGE)
        self.assertEqual(entry["policy"]["installation"], "AVAILABLE")
        self.assertIs(manifest["extensions"]["com.openai"]["requires_local_executor"], True)

    def test_skill_workflow_references_are_packaged(self):
        content = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        metadata = content.split("---", 2)[1]
        self.assertIn(f"name: {SKILL.name}", metadata)
        references = set(re.findall(r"\]\((references/[^)]+\.md)\)", content))
        self.assertEqual(references, {"references/plan.md", "references/delivery.md"})
        for target in references:
            self.assertTrue((SKILL / target).is_file(), target)

    def test_plugin_contains_only_skill_and_documentation_files(self):
        packaged_files = set()
        for file in PACKAGE.rglob("*"):
            if file.is_file():
                packaged_files.add(file.relative_to(PACKAGE).as_posix())
        self.assertEqual(packaged_files, {
            "plugin.json",
            "AGENTS.md",
            "skills/software-company/AGENTS.md",
            "skills/software-company/SKILL.md",
            "skills/software-company/references/plan.md",
            "skills/software-company/references/delivery.md",
        })


if __name__ == "__main__":
    unittest.main()
