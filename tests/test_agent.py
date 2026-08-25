import unittest
from pathlib import Path
from src.agent import SafeGuardAgent

class TestSafeGuardAgent(unittest.TestCase):
    def setUp(self):
        self.agent = SafeGuardAgent()

    def test_config_loaded(self):
        self.assertIsNotNone(self.agent.config)
        self.assertEqual(self.agent.config.get("agent_name"), "SafeGuard Assistant")

    def test_sandbox_containment(self):
        # Ensure target directory resolves safely within sandbox root
        self.assertTrue(str(self.agent.target_dir).startswith(str(self.agent.sandbox_root)))

    def test_audit_workspace_returns_list(self):
        files = self.agent.audit_workspace()
        self.assertIsInstance(files, list)

    def test_auto_approval_bypass(self):
        # Temporarily disable approval requirement in config
        self.agent.config["approval_required"] = False
        result = self.agent.request_approval("Test safe action")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()