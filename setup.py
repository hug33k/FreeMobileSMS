from setuptools import setup

setup(
    name="freemobilesms",
    description="Free Mobile SMS Service",
    long_description="Library to use Free Mobile SMS service with Python",
    version="0.1.0",
    url="https://github.com/hug33k/FreeMobileSMS",
    download_url="https://github.com/hug33k/FreeMobileSMS/archive/0.1.0.tar.gz",
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
        "urllib"
    ],
    entry_points={
        "console_scripts": [
            "sms=freemobilesms.main:run"
        ]
    }
)