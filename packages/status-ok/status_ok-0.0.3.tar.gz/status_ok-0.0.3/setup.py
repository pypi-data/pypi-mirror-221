from setuptools import setup, find_packages

LICENSE = 'MIT'
REQUIRES = [
    'requests',
]

setup(
    name="status_ok",
    version="0.0.3",
    description="This library is used to handle http responses.",
    long_description="This library is used to handle http responses in python.",
    long_description_content_type='text/markdown',
    author="yuvraj jaiswal",
    author_email="y.jaiswal@thesynapses.com",
    url="https://github.com/iLS-yuvrajj/statusOk/tree/main",
    license=LICENSE,
    packages=find_packages(),
    install_requires=REQUIRES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)