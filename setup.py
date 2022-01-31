from setuptools import setup, find_packages

setup(
    name="py3ddose",
    version="0.0.1",
    author="markusbaker",
    author_email="samuel.ouellet.10@ulaval.ca",
    description="3ddose reader",
    url="https://github.com/smichi23/py3ddose.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=["numpy"],
    python_requires=">=3.8"
)
