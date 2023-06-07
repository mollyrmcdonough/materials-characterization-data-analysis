from setuptools import setup, find_packages

setup(
    name='mcda',
    version='0.1',    
    description='A useful description',
    author='Your Name',
    author_email='your.email@example.com',
    url='http://example.com',
    packages=find_packages(),    
    install_requires=[
        'pandas>=1.2.0',
        'matplotlib',
        'scipy',
        'numpy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',      
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
