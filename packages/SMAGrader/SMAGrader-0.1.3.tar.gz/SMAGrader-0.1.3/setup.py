from setuptools import find_packages, setup

setup(
    name="SMAGrader",
    packages=find_packages(include=["SMAGrader"]),
    version="0.1.3",
    description="Library for social media analysis course autograder",
    author="arisharma",
    license="MIT",
    install_requires=["numpy", "pandas", "nltk", "praw", "firebase-admin"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
)
