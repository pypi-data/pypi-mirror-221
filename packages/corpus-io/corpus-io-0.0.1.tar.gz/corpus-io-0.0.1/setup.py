import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="corpus-io",
    version="0.0.1",
    author="postBG",
    author_email="profile2697@gmail.com",
    description="Read/write nikl corpus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/re-writers/corpusIO.python",
    project_urls={
        "Bug Tracker": "https://github.com/re-writers/corpusIO.python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
)
