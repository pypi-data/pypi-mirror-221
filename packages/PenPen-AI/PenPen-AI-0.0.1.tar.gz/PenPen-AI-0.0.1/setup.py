from setuptools import setup, find_packages

# Read requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="PenPen-AI",
    version="0.0.1",
    packages=find_packages(),
    description="A Python package for standardizing prompts for LLMs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ufirst S.r.l.",
    url="https://github.com/qurami/PenPen",
    license="MIT",
    keywords="LLM, GPT, prompting, ufirst",
    install_requires=requirements,
)