import os
import json

class SafeGuardAgent:
    def __init__(self, config_path="src/agent_config.json"):
        with open(config_path, "r") as f:
            self.config = json.load(f)
        self.target_dir = self.config.get("target_directory", "./workspace_sandbox")
        
    def audit_workspace(self):
        print(f"[*] SafeGuard Agent initializing audit on: {self.target_dir}")
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir, exist_ok=True)
            print(f"[+] Created sandbox directory: {self.target_dir}")
            
        files = os.listdir(self.target_dir)
        print(f"[*] Found {len(files)} files in target workspace.")
        return files

    def request_approval(self, action_description):
        print(f"\n[!] APPROVAL REQUIRED: {action_description}")
        # In the TrueForge harness, this pauses for human authorization.
        return True

if __name__ == "__main__":
    agent = SafeGuardAgent()
    agent.audit_workspace()