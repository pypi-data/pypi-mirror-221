
__version__ = "1.0.3"
__author__ = 'Caleb OConnor'
__credits__ = 'MD Anderson Cancer Center'

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='MedicalImageConverter',
    author=__author__,
    author_email='csoconnor@mdanderson.org',
    version=__version__,
    description='Reads in medical images and converts them into numpy arrays.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'MedicalImageConverter': 'src/MedicalImageConverter'},
    packages=['MedicalImageConverter'],
    include_package_data=True,
    url='https://github.com/caleb-oconnor/MedicalImageConverter',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3"
    ],
    install_requires=['numpy>=1.24.2',
                      'pandas>=2.0.3',
                      'psutil>=5.9.5',
                      'pydicom>=2.4.2',
                      'opencv-python>=4.7.0.72']
)
