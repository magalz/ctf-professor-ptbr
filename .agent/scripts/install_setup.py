#!/usr/bin/env python3
"""
Install Setup - CTF Professor
==============================
Automates environment verification, Docker build, and dependency setup.
Used by the /install workflow.
"""

import os
import sys
import subprocess
import shutil
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger("install_setup")

class InstallSetup:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.agent_dir = self.project_root / ".agent"
        self.sandbox_dir = self.agent_dir / "sandbox"
        self.image_name = "cyber-ctf-kali"
        self.required_python_libs = ["mcp", "fastmcp", "pwntools", "requests"]

    def check_core_tools(self):
        """Check for core system requirements."""
        tools = {
            "docker": "Docker is required for the sandbox environment.",
            "python": "Python 3.8+ is required for the CTF Professor scripts.",
            "git": "Git is required for version control."
        }
        
        status = {}
        for tool, reason in tools.items():
            path = shutil.which(tool)
            status[tool] = {
                "installed": path is not None,
                "path": path if path else "Not Found",
                "reason": reason
            }
        return status

    def check_docker_image(self):
        """Check if the Docker image already exists."""
        try:
            result = subprocess.run(
                ["docker", "images", "-q", self.image_name],
                capture_output=True, text=True, check=True
            )
            return len(result.stdout.strip()) > 0
        except subprocess.CalledProcessError:
            return False

    def build_docker_image(self, force: bool = False):
        """Build the Docker sandbox image."""
        if self.check_docker_image() and not force:
            logger.info(f"Docker image '{self.image_name}' already exists. Use --force to rebuild.")
            return True

        dockerfile = self.sandbox_dir / "Dockerfile"
        if not dockerfile.exists():
            logger.error(f"Dockerfile not found at {dockerfile}")
            return False

        logger.info(f"Building Docker image '{self.image_name}'...")
        try:
            subprocess.run(
                ["docker", "build", "-t", self.image_name, str(self.sandbox_dir)],
                check=True
            )
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to build Docker image: {e}")
            return False

    def check_python_libs(self):
        """Check for required Python libraries."""
        import importlib
        missing = []
        for lib in self.required_python_libs:
            try:
                importlib.import_module(lib)
            except ImportError:
                missing.append(lib)
        return missing

    def install_python_libs(self, libs: list):
        """Install missing Python libraries."""
        if not libs:
            return True
        
        logger.info(f"Installing missing libraries: {', '.join(libs)}...")
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install"] + libs,
                check=True
            )
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to install libraries: {e}")
            return False

    def run_full_setup(self, force_rebuild: bool = False):
        """Execute the full setup sequence."""
        logger.info("Starting CTF Professor environment setup...")
        
        # 1. Core Tools
        tools = self.check_core_tools()
        for tool, info in tools.items():
            if not info["installed"]:
                logger.error(f"Missing core tool: {tool.upper()} - {info['reason']}")
                return False
            logger.info(f"✅ {tool.upper()} is installed at {info['path']}")

        # 2. Python Libs
        missing_libs = self.check_python_libs()
        if missing_libs:
            logger.warning(f"Missing Python libraries: {', '.join(missing_libs)}")
            if input("Would you like to install them now? (y/n): ").lower() == 'y':
                if not self.install_python_libs(missing_libs):
                    return False
        else:
            logger.info("✅ All required Python libraries are present.")

        # 3. Docker Image
        if not self.build_docker_image(force_rebuild):
            return False
        logger.info(f"✅ Docker image '{self.image_name}' is ready.")

        logger.info("✨ Environment setup completed successfully! ✨")
        return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="CTF Professor Setup Script")
    parser.add_argument("--force-rebuild", action="store_true", help="Force rebuild the Docker image")
    parser.add_argument("--check-only", action="store_true", help="Only check for dependencies, don't install")
    
    args = parser.parse_args()
    setup = InstallSetup()
    
    if args.check_only:
        tools = setup.check_core_tools()
        for tool, info in tools.items():
            print(f"{tool.upper()}: {'OK' if info['installed'] else 'MISSING'}")
        
        missing_libs = setup.check_python_libs()
        if missing_libs:
            print(f"Missing Libraries: {', '.join(missing_libs)}")
        else:
            print("Python Libs: OK")
            
        if setup.check_docker_image():
            print(f"Docker Image '{setup.image_name}': OK")
        else:
            print(f"Docker Image '{setup.image_name}': MISSING")
    else:
        success = setup.run_full_setup(args.force_rebuild)
        sys.exit(0 if success else 1)
