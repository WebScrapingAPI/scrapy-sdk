from setuptools import setup

setup(
    name='webscrapingapi_scrapy_sdk',
    version="1.0.7",
    url='https://github.com/WebScrapingAPI/scrapy-sdk',
    description='WebScrapingApi Python Scrapy SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sorin-Gabriel Marica',
    author_email='sorin.marica@jeco.dev',
    maintainer='webscrapingapi',
    maintainer_email='account@jeco.dev',
    license='MIT',
    packages=['webscrapingapi_scrapy_sdk'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    install_requires=['scrapy'],
)