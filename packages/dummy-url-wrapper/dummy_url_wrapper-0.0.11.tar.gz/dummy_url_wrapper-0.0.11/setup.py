from setuptools import setup, find_packages

setup(
    name="dummy_url_wrapper",
    version="0.0.11",
    description="This package provides the wrapping of URLs for not exposing to clients",
    url="https://github.com/nk2909/Python-SDK.git",
    author="Nishant Kabariya",
    author_email="testurl@yopmail.com",
    install_requires=["python-dotenv", "requests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    keywords=["python"],
    packages=find_packages(),
)
