from setuptools import setup

try:
   import pypandoc
   description = pypandoc.convert("README.md", "rst")
except:
   description = "Library to use Free Mobile SMS service with Python"

try:
    with open(".version", "r") as file:
        version = file.read()
except:
    version = "0.0.0"

setup(
    name="freemobilesms",
    description="Free Mobile SMS Service",
    long_description=description,
    version=version,
    url="https://github.com/hug33k/FreeMobileSMS",
    download_url="https://github.com/hug33k/FreeMobileSMS/archive/{version}.tar.gz".format(version=version),
    author="Hugo SCHOCH",
    author_email="schoch.hugo@gmail.com",
    license="Apache2",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2"
    ],
    keywords=[
        "free mobile",
        "freemobile",
        "free",
        "sms"
    ],
    packages=[
        "freemobilesms"
    ],
    install_requires=[
        "urllib3",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "sms=freemobilesms.cli:main"
        ]
    }
)