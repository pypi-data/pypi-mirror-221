from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()


DESCRIPTION = 'hello world'
LONG_DESCRIPTION = 'A package that allows showing hellow worldo.'

# Setting up
setup(
    name="hellow_worldo",
    version="0.0.16",
    author="RohitMishra (The Great DEV)",
    author_email="RKMDEV@DEV.com",
    description=DESCRIPTION,
    long_description_content_type="text/plain",  # Use text/plain for reST
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],  # Replace with actual dependencies if needed
    keywords=['python', 'hello'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
