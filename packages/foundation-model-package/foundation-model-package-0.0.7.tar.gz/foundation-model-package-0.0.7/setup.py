import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="foundation-model-package",
    version="0.0.7",
    author="Matthew DeGuzman",
    author_email="t-madeguzman@microsoft.com",
    description="Package to use Foundation Models in Prompt Flow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
