import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="foundation-model-package",
    version="0.0.13",
    author="Matthew DeGuzman",
    author_email="t-madeguzman@microsoft.com",
    description="Package to use Foundation Models in Prompt Flow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    entry_points={"package_tools": ["foundation_model = foundation_model_pkg.tools.utils:list_package_tools"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
