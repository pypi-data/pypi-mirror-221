from setuptools import setup, find_packages

setup(
    name="card91BusinessSDK",
    version="0.0.14",
    description="This package is used to access the bunch of Card91 fintech business services",
    url="https://github.com/nk2909/Python-SDK.git",
    author="Card91",
    author_email="tech.apps@card91.io",
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    keywords=["python"],
    packages=find_packages(),
)
