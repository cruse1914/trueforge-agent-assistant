# 🛡️ SafeGuard Agent: Approval-Gated Workspace Assistant

An autonomous workspace assistant built on **TrueForge**, designed to audit directories, manage files, and execute maintenance tasks securely with strict human-in-the-loop approval gating and path sandboxing.

---

## 🚀 Architecture & Core Features

- **TrueForge Integration:** Built on top of the TrueForge harness for reliable agent loops and session execution.
- **Configuration-Time Sandbox Containment:** Uses robust `Path.is_relative_to()` ancestry checks during initialization to prevent configuration-level path traversal attacks.
- **Configurable Approval Gating:** Pauses for manual confirmation before executing sensitive actions, with graceful fallback to fail-closed behavior in headless/non-interactive environments (`EOFError`/`KeyboardInterrupt`).
- **Resilient Error Handling:** Fully isolated workspace auditing with automatic parent directory creation and robust error recovery.

---

## 🧪 Testing & Code Quality
SafeGuard Agent features a comprehensive, concurrent-safe unit test suite utilizing Python's `unittest` and managed `tempfile.TemporaryDirectory` fixtures to guarantee clean execution without repository pollution.

To run the test suite locally:
```bash
python3 -m unittest discover tests
