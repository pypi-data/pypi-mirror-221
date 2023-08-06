from setuptools import setup, find_packages

version = "0.0.1"

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    install_requires = [x.strip() for x in f if x.strip()]

setup(
    name="awesomepython",
    version=version,
    description="CLI for discovering hand-picked awesome Python libraries, with an emphasis on data and machine learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dylanhogg/awesomepython-package",
    author="Dylan Hogg",
    author_email="dylanhogg@gmail.com",
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="awesome, python, frameworks, packages, data, libraries, pip, machine learning",
    package_dir={"": "awesomepython"},
    packages=find_packages(where="awesomepython"),
    python_requires=">=3.8, <4",
    install_requires=install_requires,
)
