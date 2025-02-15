from setuptools import setup, find_packages

print(find_packages())

setup(
    name="hrpdrebin",
    version="1.2",
    description='High-resolution powder diffraction rebin',
    author="Peter Chang",
    author_email="scientificsoftware@diamond.ac.uk",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    install_requires=['numpy>=1.6', 'scisoftpy>=2.17'],
    entry_points={'console_scripts': ['rebin = hrpdrebin.maincmd:main'],
                    'gui_scripts': ['rebin-gui = hrpdrebin.mainui:main']},
    url='https://github.com/DiamondLightSource/python-hrpd-rebin',
)
