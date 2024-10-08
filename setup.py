import setuptools

setuptools.setup(
    name="z-eveng",
    version="0.0.1.6",
    author="Prajwal",
    author_email="pkumarjha@zscaler.com",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    python_requires=">=3.8"
)
