import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="cachier-client",
    version="0.3.0",
    author="apinanyogaratnam",
    author_email="apinanapinan@icloud.com",
    description="A cachier python client package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cachier-cache/cachier-python-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[],
)
