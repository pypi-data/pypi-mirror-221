from setuptools import setup

setup(
    name='dukeai_lib',
    version="0.1.3",
    description="Common functions used across the DUKE.ai project environments.",
    url='',
    author='Blake Donahoo',
    author_email='blake@duke.ai',
    license='GNU General Public License v3 (GPLv3)',
    install_requires=[
        'chalice~=1.27.1',
        'requests~=2.27.1',
        'base58==2.1.1',
        'urllib3==1.26.9'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ],
)
