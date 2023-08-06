from setuptools import setup, find_packages

setup(
    name="gpt_automation",
    version="0.1.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "autogpt = src.main:main",
        ],
    },
)