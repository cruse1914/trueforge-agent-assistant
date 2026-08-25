import unittest
import tempfile
import json
from pathlib import Path
from src.agent import SafeGuardAgent

class TestSafeGuardAgent(unittest.TestCase):
    def setUp(self):
        self.agent = SafeGuardAgent()

    def test_config_loaded(self):
        self.assertIsNotNone(self.agent.config)
        self.assertEqual(self.agent.config.get("agent_name"), "SafeGuard Assistant")

    def test_sandbox_containment(self):
        # Ensure target directory resolves safely using proper ancestry check
        self.assertTrue(self.agent.target_dir.is_relative_to(self.agent.sandbox_root))

    def test_path_traversal_rejection(self):
        # Verify that escaping targets are properly blocked by security checks
        with tempfile.TemporaryDirectory() as tmpdir:
            bad_config_path = Path(tmpdir) / "agent_config.json"
            bad_config = {
                "agent_name": "BadAgent",
                "target_directory": "../outside_sandbox"
            }
            with open(bad_config_path, "w") as f:
                json.dump(bad_config, f)
            
            with self.assertRaises(ValueError):
                SafeGuardAgent(config_path=bad_config_path)

    def test_audit_workspace_isolated(self):
        # Isolate workspace auditing completely using a managed temporary directory
        with tempfile.TemporaryDirectory() as tmpdir:
            agent = SafeGuardAgent()
            temp_target = Path(tmpdir) / "isolated_sandbox"
            agent.target_dir = temp_target
            
            files = agent.audit_workspace()
            self.assertIsInstance(files, list)
            self.assertTrue(temp_target.exists())
            self.assertTrue(temp_target.is_dir())

    def test_auto_approval_bypass(self):
        self.agent.config["approval_required"] = False
        result = self.agent.request_approval("Test safe action")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()