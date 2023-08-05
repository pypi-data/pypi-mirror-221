from setuptools import setup


VERSION='0.0.3'


with open('README.md', 'r', encoding='utf-8') as f:
    longdescription = f.read()

setup(
    name='pyvalidata',
    version='0.0.1',
    description='A Python package for data validation',
    long_description=longdescription,
    long_description_content_type='text/markdown', 
    author='Eklavya Tomar',
    author_email='eklavyaprogramming@gmail.com',
    url='https://github.com/EklavyaT/pyvalidata',
    packages=['pyvalidata'],
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        
    ],
)

