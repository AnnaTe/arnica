# Flower Segmentation Tool

The Flower Segmentation Tool is a software to segment yellow arnica flowers in aerial drone images. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Download and Installation from the Python Packaging Index

For installing the flower segmentation tool first download package from github:
https://github.com/AnnaTe/arnica or clone repository from github

```
git clone git@github.com:AnnaTe/arnica.git
```

### Installing

For installation first go inside of the package directory.
Try:

```
python setup.py install
```

install dependencies:

```
pip install -r requirements.txt
```

## Running the programm

To open the GUI and run the programm call in python environment:
```
Python3 segtool.py
```

### Testing

There are two tests, to check for missing dependencies.

tests/test.py and tests/testgui.py

## Troubleshooting

if there were still Errors or dependencies not fullfilled, here are some common Errors explained and solutions presented.

Error Message:
```
ModuleNotFoundError: No module named 'PyQt5.sip'
```
It is important, that sip is installed before pyqt5. Try unistalling both and the try new installation:
```
pip uninstall pyqt5
pip uninstall pyqt5-sip
pip install -I PyQt5-sip
pip install -I PyQt5
```

For Error Message: zlib not found:
```
Try, for new installation:
```
Go to: 
https://sourceforge.net/projects/libpng/files/zlib/1.2.9/ 
and install zlib newest version according to your architecture.


## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - The Python IDE used
* [Anaconda](https://maven.apache.org/) - Virtual Python environment manager used
* [DesignerQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/designer.html) - Used to design GUI

## Versioning

We use [GitHub](https://github.com/AnnaTe/arnica) for versioning.

## Authors

* **Anna Tenberg** - *Initial work* - [GitHub](https://github.com/AnnaTe)

## License

This project is licensed under the GPLv3 LICENSE - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This programm was developed as part of a bachelors thesis in environmental science at the university in Freiburg. 
