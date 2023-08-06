from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mlforce",
    version="0.1.1",
    author="Jiarui Xu",
    author_email="xujiarui98@foxmail.com",
    description="Easy-to-use toolkit with numpy, pandas, and PyTorch for beginners",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/XavierSpycy/MLForce",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=1.5.3",
        "scipy>=1.10.0",
        "torch>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "sphinx>=4.0.0",
        ],
        "data": [
            #"pandas>=1.2.0",
            #"scipy>=1.5.0",
        ],
    },
)