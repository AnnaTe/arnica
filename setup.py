import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flower-sementation-tool",
    version="0.1.3",
    author="Anna Tenberg",
    author_email="Anna.Tenberg@saturn.uni-freiburg.de",
    description="A tool to segment yellow flowers in rgb images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnnaTe/arnica",
    packages=setuptools.find_packages(exclude=['tests*', 'scripts', 'src', '*.git']),
    python_requires='>=3.6',
    install_requires=[
        'opencv-python',
        'PyQt5-sip',
        'pyqt5',
        'numpy',
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