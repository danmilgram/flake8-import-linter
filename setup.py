# Third party
from setuptools import setup

setup(
    name='flake8_import_linter',
    description='Flake8 plugin that checks for forbidden imports in your code',
    classifiers=[
        'Environment :: Console',
        'Framework :: Flake8',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    keywords='flake8 import linter',
    version='0.1.0',
    author='Dan Milgram',
    author_email='ddmilgram@gmail.com',
    install_requires=['flake8'],
    entry_points={
        'flake8.extension': [
            'IMP=flake8_import_linter:Plugin',
        ],
    },
    url='https://github.com/best-doctor/flake8-annotations-complexity',
    license='MIT',
    py_modules=[package_name],
    zip_safe=False,
)