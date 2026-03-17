import os
import subprocess
import json
import logging
from typing import Dict, Any, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("sandbox_manager")

class SandboxManager:
    """
    Manages an ephemeral Docker container for CTF agents to execute commands in
    an isolated environment.
    """
    def __init__(self, image_name: str = "cyber-ctf-kali", container_name: str = "ctf_sandbox"):
        self.image_name = image_name
        self.container_name = container_name

    def is_running(self) -> bool:
        """Check if the sandbox container is currently running."""
        try:
            result = subprocess.run(
                ["docker", "inspect", "-f", "{{.State.Running}}", self.container_name],
                capture_output=True, text=True, check=False
            )
            return result.stdout.strip() == "true"
        except Exception:
            return False

    def start(self, workdir: str = None) -> bool:
        """
        Start the sandbox container.
        Args:
            workdir: The host directory to mount into the container at /workspace.
                     Defaults to the current working directory.
        """
        if self.is_running():
            logger.info(f"Sandbox '{self.container_name}' is already running.")
            return True

        if workdir is None:
            workdir = os.getcwd()

        logger.info(f"Starting sandbox '{self.container_name}' with mount '{workdir}:/workspace'...")
        
        # Build the docker run command
        # Security: Enable bridge network, add necessary capabilities for tools like nmap/gdb, mount workspace
        # --rm automatically removes the container when stopped.
        cmd = [
            "docker", "run", "-d", "--rm",
            "--name", self.container_name,
            "--network=bridge",
            "--cap-add=NET_RAW",
            "--cap-add=NET_ADMIN",
            "--cap-add=SYS_PTRACE",
            "--security-opt", "seccomp=unconfined",
            "-v", f"{workdir}:/workspace",
            "-w", "/workspace",
            self.image_name,
            "sleep", "infinity"
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            logger.info(f"Sandbox started. ID: {result.stdout.strip()[:12]}")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to start sandbox: {e.stderr}")
            return False

    def stop(self) -> bool:
        """Stop (and automatically remove due to --rm) the sandbox container."""
        if not self.is_running():
            logger.info("Sandbox is not running.")
            return True

        logger.info(f"Stopping sandbox '{self.container_name}'...")
        try:
            subprocess.run(["docker", "kill", self.container_name], capture_output=True, text=True, check=True)
            logger.info("Sandbox stopped.")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to stop sandbox: {e.stderr}")
            return False

    def execute_command(self, command: str, timeout: int = 60) -> Tuple[int, str, str]:
        """
        Execute a command inside the running sandbox.
        
        Returns:
            Tuple[int, str, str]: (exit_code, stdout, stderr)
        """
        if not self.is_running():
            logger.warning("Sandbox is not running. Attempting to start it...")
            if not self.start():
                return 1, "", "Failed to start the sandbox environment."

        logger.info(f"Executing command in sandbox: {command}")
        
        # We wrap the command in bash to allow for piping, redirection, etc.
        cmd = [
            "docker", "exec", self.container_name,
            "bash", "-c", command
        ]

        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=timeout
            )
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            logger.error(f"Command timed out after {timeout} seconds.")
            return 124, "", f"Command timed out after {timeout} seconds."
        except Exception as e:
            logger.error(f"Execution error: {e}")
            return 1, "", str(e)


def main():
    """Simple CLI interface for testing the sandbox manager."""
    import argparse
    parser = argparse.ArgumentParser(description="CTF Sandbox Manager")
    parser.add_argument("action", choices=["start", "stop", "exec", "status"], help="Action to perform")
    parser.add_argument("--cmd", help="Command to execute (for 'exec' action)")
    parser.add_argument("--workdir", help="Directory to mount (for 'start' action)")
    
    args = parser.parse_args()
    
    manager = SandboxManager()
    
    if args.action == "status":
        is_running = manager.is_running()
        print(f"Sandbox running: {is_running}")
    elif args.action == "start":
        manager.start(args.workdir)
    elif args.action == "stop":
        manager.stop()
    elif args.action == "exec":
        if not args.cmd:
            print("Error: --cmd is required for 'exec' action")
            return
        code, out, err = manager.execute_command(args.cmd)
        print(f"Exit code: {code}")
        if out:
            print(f"Stdout:\n{out}")
        if err:
            print(f"Stderr:\n{err}")

if __name__ == "__main__":
    main()
