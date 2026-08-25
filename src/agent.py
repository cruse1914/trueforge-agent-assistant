import json
from pathlib import Path

class SafeGuardAgent:
    """
    SafeGuardAgent: An autonomous workspace assistant built on TrueForge
    featuring configurable human-in-the-loop approval gating and secure path sandboxing.
    """
    def __init__(self, config_path=None):
        
        try:
            with open(config_path, "r") as f:
                self.config = json.load(f)
        except Exception as e:
            raise RuntimeError(f"Failed to load agent configuration from {config_path}: {e}")
        
        self.repo_root = Path(__file__).resolve().parent.parent
        self.sandbox_root = (self.repo_root / "workspace_sandbox").resolve()
        
        raw_target = self.config.get("target_directory", "workspace_sandbox")
        resolved_target = (self.repo_root / raw_target).resolve()
        
        # Enforce secure path ancestry containment using is_relative_to()
        try:
            if not resolved_target.is_relative_to(self.sandbox_root):
                raise ValueError(f"Security Error: Target directory '{raw_target}' escapes the sandbox root.")
        except ValueError:
            raise ValueError(f"Security Error: Target directory '{raw_target}' escapes the sandbox root.")
            
        self.target_dir = resolved_target

    def audit_workspace(self):
        print(f"[*] SafeGuard Agent initializing audit on: {self.target_dir}")
        try:
            if not self.target_dir.exists():
                self.target_dir.mkdir(parents=True, exist_ok=True)
                print(f"[+] Created sandbox directory: {self.target_dir}")
            
            if not self.target_dir.is_dir():
                raise NotADirectoryError(f"Target path is not a valid directory: {self.target_dir}")
                
            files = list(self.target_dir.iterdir())
            print(f"[*] Found {len(files)} items in target workspace.")
            return [str(f.name) for f in files]
        except Exception as e:
            print(f"[-] Error auditing workspace: {e}")
            return []

    def request_approval(self, action_description):
        print(f"\n[!] APPROVAL REQUIRED: {action_description}")
        if not self.config.get("approval_required", True):
            print("[*] Approval bypass enabled in config. Auto-approving.")
            return True
            
        # Handle non-interactive or headless environments gracefully
        try:
            choice = input("Do you approve this action? [y/N]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n[-] Non-interactive environment detected or input interrupted. Denying by default.")
            return False

        if choice in ['y', 'yes']:
            print("[+] Action approved by human operator.")
            return True
        else:
            print("[-] Action denied by human operator.")
            return False

if __name__ == "__main__":
    agent = SafeGuardAgent()
    agent.audit_workspace()