from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="airtime",
    version="1.0.2",
    author="Jana M. Perkins",
    author_email="mailroom@jcontd.com",
    description="""A package for analyzing transcripts
    from Zoom and Microsoft Teams meetings""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jcontd/airtime",
    license="GNU Affero General Public License v3",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ]
)
