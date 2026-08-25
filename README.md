# 🛡️ SafeGuard Agent: Approval-Gated Workspace Assistant

An autonomous agent built on **TrueForge** designed to audit local directories, sort files, and handle routine maintenance tasks with strict human-in-the-loop approvals before executing any irreversible actions.

## 🚀 Architecture & Features
- **TrueForge Harness:** Core runtime layer managing agent loops and sessions.
- **Approval Gating:** Automatically pauses for manual user confirmation before performing file operations.
- **Sandboxed Execution:** Executes diagnostic and sorting logic securely within an isolated environment.

## 🛠️ Setup & Local Execution
1. Ensure Node.js 22+ is installed.
2. Run TrueForge locally:
   ```bash
   npx @truefoundry/trueforge
   