from setuptools import setup, find_packages

setup(
    name="qwewxsadld",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["helloworld=helloworld:main"],
    },
    license="MIT",
    description="A simple Hello World script",
    author="Your Name",
    author_email="your_xxxxemail@example.com",
    install_requires=[
        "typing",
    ],
)
