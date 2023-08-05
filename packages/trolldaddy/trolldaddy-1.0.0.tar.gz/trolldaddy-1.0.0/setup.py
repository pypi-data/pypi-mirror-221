from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="trolldaddy",
    version="1.0.0",
    author="PyModuleDev",
    author_email="pxcom@mail.com",
    description="haha",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["trolldaddy"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ],
    python_requires=">=3.6"
)
