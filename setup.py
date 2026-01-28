from __future__ import annotations

from pathlib import Path

from setuptools import setup, find_packages


ROOT = Path(__file__).parent


setup(
    name="linux-helper",
    version="2.0.0",
    description="Natural language to Linux command helper (lh) with 692 command lines and 593 unique commands.",
    author="linux-helper",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    package_data={
        "linux_helper": ["assets/*.txt", "assets/*.json"],
    },
    install_requires=[
        "click>=8.0",
        "rich>=13.0",
        "rapidfuzz>=3.0",
        "pydantic>=2.0",
        "platformdirs>=4.0",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "lh=linux_helper.cli.app:main",
        ]
    },
    long_description=(ROOT / "README.md").read_text(encoding="utf-8")
    if (ROOT / "README.md").exists()
    else "",
    long_description_content_type="text/markdown",
)
