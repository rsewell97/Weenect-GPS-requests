import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weenect-gps-api",
    version="1.1.0",
    author="Robbie Sewell",
    author_email="rsewell97@gmail.com",
    description="A package for accessing the Weenect-GPS api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rsewell97/Weenect-GPS-requests",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
