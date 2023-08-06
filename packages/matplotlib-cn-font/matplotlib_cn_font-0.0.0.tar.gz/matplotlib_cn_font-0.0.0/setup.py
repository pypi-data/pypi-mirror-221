from setuptools import find_packages, setup

# long description
with open("README.md", "r") as f:
    long_description = f.read()

# requirements
with open("requirements.txt", "r") as f:
    requirements = f.read()
    requirements = requirements.split("\n")

setup(
    name="matplotlib_cn_font",  # Need modify
    version="0.0.0",  # Need modify
    author="Yanzhong Huang",
    author_email="yanzhong.huang@outlook.com",
    description="A package to set Chinese font for matplotlib.",  # Need modify
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yanzhong-Hub/yzdb",  # Need modify
    packages=find_packages(),
    python_requires=">=3.5",  # Need modify
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    
    extras_require={
        "dev": [
            "pytest>=7.0",
            "twine>=4.0.2",]
    },
    install_requires=requirements, 
)
