# setup.py

"""Setup script."""

from setuptools import setup

with open('requirements.txt', 'r', encoding='UTF-8') as f:
    required: list[str] = f.read().splitlines()

with open("README.md", 'r', encoding='UTF-8') as f:
    long_description: str = f.read()

setup(
    name='wolfsoftware.drawlines',
    version='0.1.0rc1',
    author='Wolf Software',
    author_email='pypi@wolfsoftware.com',
    description='Draw lines on the console with optional text',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=['wolfsoftware.drawlines'],
    tests_require=['pytest'],
    test_suite='tests',
    install_requires=required,
    keywords=['python', 'convert_size'],
    url='https://github.com/DevelopersToolbox/draw-lines-package',

    project_urls={
        ' Source': 'https://github.com/DevelopersToolbox/draw-lines-package',
        ' Tracker': 'https://github.com/DevelopersToolbox/draw-lines-package/issues/',
        ' Documentation': 'https://github.com/DevelopersToolbox/draw-lines-package',
        ' Sponsor': 'https://github.com/sponsors/WolfSoftware',
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ]
)
