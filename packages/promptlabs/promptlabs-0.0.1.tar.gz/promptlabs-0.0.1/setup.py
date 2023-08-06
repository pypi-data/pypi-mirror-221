"""
promptlabs: A Python package for PromptOps (versioning, logging, experimenting, etc.)
"""
from setuptools import setup, find_packages

setup(
    name="promptlabs",
    version="0.0.1",
    packages=find_packages(),
    description="promptlabs: A Python package for PromptOps (versioning, logging, experimenting, etc.)",
    auther="weavel",
    install_requires=['openai', 'pydantic', 'requests'],
    python_requires='>=3.7.1',
    keywords=['weavel', 'prompt', 'llm', 'promptops', 'promptlabs', 'prompt engineering']
)
