import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # Since the algkit is deleted from testpypi, so suffix a test when upload to testpypi.
    name="algkit-test",
    version="0.0.4",
    author="ishiahirake",
    author_email="ishiahirake@gmail.com",
    description="Algorithm toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ishiahirake/algkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)