from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="PyRapidML", # Replace with your own username
    version="1.0.11",
    author="Zain Ali",
    author_email="zainbalouch3@gmail.com",
    description="An open source and low code machine learning library for quick and robust analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zainali5/PyRapidML",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
