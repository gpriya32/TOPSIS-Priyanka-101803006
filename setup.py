from setuptools import setup

def readme():
    with open('README.md') as file:
        README = file.read()
    return README

setup(
    name="TOPSIS_Priyanka-101803006",
    version="1.0.0",
    description="A Python package implementing TOPSIS technique.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Priyanka Gupta",
    author_email="priyaagupta55@gmail.com",
<<<<<<< HEAD
    url = 'https://github.com/gpriya32/TOPSIS-PriyankaGupta-101803006',  
=======
    url = 'https://github.com/gpriya32/TOPSIS-PriyankaGupta-101803006/',
>>>>>>> a65d221b53c502cf6fedfbc434289ca7f9e71d79
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: 3.7",
    ],
    packages=["src"],
    include_package_data=True,
    install_requires=['scipy',
                      'tabulate',
                      'numpy',
                      'pandas',
     ],
     entry_points={
        "console_scripts": [
            "topsis=src.topsis:main",
        ]
     },
)
