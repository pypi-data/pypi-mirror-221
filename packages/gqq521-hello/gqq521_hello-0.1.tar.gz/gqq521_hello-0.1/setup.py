from setuptools import setup, find_packages

setup(
    name='gqq521_hello',
    version='0.1',
    packages=find_packages(),
    description='A simple hello world package created by GQQ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='GQQ',
    author_email='ganqiu@ucdavis.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='sample setuptools development',
)
