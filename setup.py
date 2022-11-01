"""Setups up the Shimmy module."""
from setuptools import find_packages, setup


def get_description():
    """Gets the description from the readme."""
    with open("README.md") as fh:
        long_description = ""
        header_count = 0
        for line in fh:
            if line.startswith("##"):
                header_count += 1
            if header_count < 2:
                long_description += line
            else:
                break
    return header_count, long_description


def get_version():
    """Gets the shummy version."""
    path = "shimmy/__init__.py"
    with open(path) as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith("__version__"):
            return line.strip().split()[-1].strip().strip('"')
    raise RuntimeError("bad version data in __init__.py")


version = get_version()
header_count, long_description = get_description()


extras = {
    "dm-control": ["dm-control>=1.0.8", "pillow>=9.2.0"],
    "open-spiel": ["open-spiel>=1.2", "pettingzoo>=1.22.0"],
}
extras["all"] = list({lib for libs in extras.values() for lib in libs})
extras["testing"] = ["pre-commit>=2.20.0", "pytest>7.1.3"]

setup(
    name="Shimmy",
    version=version,
    author="Farama Foundation",
    author_email="contact@farama.org",
    description="API for converting popular non-gymnasium environments to a gymnasium compatible environment.",
    url="https://github.com/Farama-Foundation/Shimmy",
    license_files=("LICENSE.txt",),
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["Reinforcement Learning", "game", "RL", "AI"],
    python_requires=">=3.7",
    packages=find_packages(),
    install_requires=["numpy>=1.18.0", "gymnasium>=0.26.0"],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require=extras,
    include_package_data=True,
)
