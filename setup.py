import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flowersegmentationtool",
    version="0.1.8",
    author="Anna Tenberg",
    author_email="Anna.Tenberg@saturn.uni-freiburg.de",
    description="A tool to segment yellow arnica flowers in rgb images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnnaTe/arnica",
    packages=setuptools.find_packages(exclude=['tests*', 'scripts', 'src', '*.git']),
    python_requires='>=3.5',
    install_requires=[
        'PyQt5-sip',
        'PyQt5',
        'numpy',
        'opencv-python',
        'matplotlib',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Intended Audience :: Science/Research",
    ],
)
