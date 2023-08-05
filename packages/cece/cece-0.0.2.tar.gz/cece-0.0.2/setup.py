from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="cece",
    version="0.0.02",
    description="Semantic Edits as Counterfctual Explanations",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Giorgos Filandrianos",
    author_email="georgefilandr@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10", "numpy >= 1.20.1", "networkx >= 2.5"],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3.8.8",
)