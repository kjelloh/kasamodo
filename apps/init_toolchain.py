#!/usr/bin/env python3
"""
init_toolchain: Synchronize the local build toolchain with external dependencies.

Usage:
    ./init_toolchain.py
"""

from pathlib import Path
from urllib.parse import urlparse
import subprocess
import sys
import shutil

# Hard coded list of repos 'we' depend on.
EXTERNAL_REPOS = [
    {
        "url": "https://gitlab.com/libeigen/eigen.git",
        "consume": [
            {
                "source": "Eigen/",
            },
        ],
    },
]

# Clone repositories into this workspace.
WORKSPACE = Path("./external_git_repos_workspace")


def repository_name(url: str) -> str:
    """Derive the local repository directory name from its URL."""
    path = urlparse(url).path.rstrip("/")
    name = Path(path).name

    if name.endswith(".git"):
        name = name[:-4]

    if not name:
        raise ValueError(f"Cannot determine repository name from URL: {url}")

    return name

def run_git(*args: str, root_path: Path | None = None) -> None:
    """Run a git command and fail if it returns a non-zero exit code."""
    command = ["git", *args]

    print(f"+ {' '.join(command)}")

    subprocess.run(
        command,
        cwd=root_path,
        check=True,
    )

def sync_repository(repo: dict) -> None:
    """Clone or update one external repository."""
    url = repo["url"]

    name = repository_name(url)
    destination = WORKSPACE / name

    if not destination.exists():
        print(f"Cloning {name}...")

        WORKSPACE.mkdir(parents=True, exist_ok=True)

        run_git(
            "clone",
            url,
            root_path = WORKSPACE,
        )

    else:
        if not (destination / ".git").is_dir():
            raise RuntimeError(
                f"Destination exists but is not a Git repository: "
                f"{destination}"
            )

        print(f"Updating {name}...")

        run_git(
            "pull",
            root_path =destination,
        )

def update_external_source(repo: dict) -> None:
    """Update the sources consumed from an external repository."""

    repo_name = repository_name(repo["url"])
    repo_root = WORKSPACE / repo_name

    for item in repo.get("consume", []):
        source = Path(item["source"])

        source_path = repo_root / source
        destination_path = Path("./src/foreign") / source

        if not source_path.is_dir():
            raise RuntimeError(
                f"Consumed source does not exist or is not a directory: "
                f"{source_path}"
            )

        # Ensure our copy is clean (no stale files)
        if destination_path.exists():
            shutil.rmtree(destination_path)
        
        print(
            f"Copying external source: "
            f"{source_path} -> {destination_path}"
        )

        if destination_path.exists():
            shutil.rmtree(destination_path)

        destination_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        shutil.copytree(
            source_path,
            destination_path,
        )

def main() -> int:

    # 1.  Clone or pull from a list of online git repos with source code this project depends on
    #     Note: Clones to a local folder 'external_git_repos_workspace''
    
    try:

      for repo in EXTERNAL_REPOS:
          sync_repository(repo)
          update_external_source(repo)

    except subprocess.CalledProcessError as e:
        print(
            f"ERROR: git command failed with exit code {e.returncode}",
            file=sys.stderr,
        )
        return e.returncode

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    # 2.  Copy selected source code to a local external source code folder
    #     Note: Maybe a folder under the src folder?

    # 3.  Create the meta-data about where the external source code is for the cmake and/or comopiler to find it?
    #     Note: Maybe feed this inforamtion so that cmake find_package works?
    #           Or provide meta-data to have cmake or tool-chain know how to provide compiler arguments
    #           like -I for include directories to search?
    #           But also maybe enough meta-data to even have cmake (or tool chain) compile also external cpp-files
    #           for build-from-source dependanciy resolution?

    # 4.  Call on cmake to create the tool chain (i.e., 'cmake -S . -B build')

    return 0



if __name__ == "__main__":
    sys.exit(main())
