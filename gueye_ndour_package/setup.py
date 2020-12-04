"""

Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, 30 Dec 2020, 19:53:46) [Computer 64 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

"""

from setuptools import setup

with open('README.md') as readme_file:
    README = readme_file.read()
    
setup(
    name='Gueye_Ndour',
    version='1.0.0',
    description='distribution example',
    long_description=README,
    keywords='distribution pypi setup.py',
    author='supinfo teams',
    author_email='mgfree01@gmail.com',
    url='https://github.com/interface22/python/Gueye_Ndour_package',
    download_url='https://pypi.org/project/Gueye_Ndour/', 
    license='GPLv3',
    packages=['Gueye_Ndour'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    python_requires='>=3.4',
    install_requires=['voluptuous']
)


if __name__ == '__main__':
    setup()
