from setuptools import setup, find_packages

from baam import VERSION

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="baam",
    version=VERSION,
    description="Deploys docker apps",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="jpedro",
    author_email="jpedro.barbosa@gmail.com",
    url="https://github.com/jpedro/baam",
    download_url="https://github.com/jpedro/baam/tarball/master",
    keywords="deploy docker apps",
    license="MIT",
    python_requires='>=3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=[
        "baam",
    ],
    install_requires=[
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "baam=baam.cli:main",
        ],
    },
)
