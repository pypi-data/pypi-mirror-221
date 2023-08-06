from setuptools import find_packages, setup

with open("./README.md", "r") as f:
    long_description = f.read()

setup(
    name="Tamil_OCR",
    version="0.0.10",
    description="Tamil OCR",
    package_dir={"": "main"},
    packages=find_packages(where="main"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Akash-Raj-ST/Tamil-OCR",
    author="Sujith",
    author_email="akashraj49070@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)