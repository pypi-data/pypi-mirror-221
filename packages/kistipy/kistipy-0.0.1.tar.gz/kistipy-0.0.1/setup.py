import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kistipy",
    version="0.0.1",
    author="prosopher",
    author_email="prosopher@gmail.com",
    description="kistipy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prosopher/kistipy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.12',
)