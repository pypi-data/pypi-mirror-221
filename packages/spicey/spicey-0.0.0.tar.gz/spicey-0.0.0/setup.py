import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spicey",
    version="0.0.0",
    author="Liberocks",
    author_email="tirtadwipa.manunggal@gmail.com",
    description="Scientific libraries in Rust",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liberocks/spice",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
