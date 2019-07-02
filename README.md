# Flower Segmentation Tool

The Flower Segmentation Tool is a software to segment yellow arnica flowers in aerial drone images. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Download and Installation from the Python Packaging Index

For installing the flower segmentation tool from the [Python Packaging Index](https://pypi.org/) try:

```
pip install URL package-name
```

### Installing

For installation first go inside of the package directory.

Install with pip

```
pip install PACKAGENAME
```

if there are any dependencies missing try

```
pip install -r requirements.txt
```

End with an example of getting some data out of the system or using it for a little demo

## Running the programm

To open the GUI and run the programm call in python environment:
```
Python3 segtool.py
```

### Testing

Explain what these tests test and why TODO

```
Give an example TODO
```

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
pip install --user -I PyQt5-sip
pip install --user -I PyQt5
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

We use [PyPI](http://pypi.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Anna Tenberg** - *Initial work* - [GitHub](https://github.com/AnnaTe)

## License

This project is licensed under the GPLv3 LICENSE - see the [LICENSE](LICENSE) file for details

## Acknowledgments

This programm was developed as part of a bachelors thesis in environmental science at the university in Freiburg. 
