from setuptools import setup, find_packages

setup(
    name='veris-priv-tab',
    version='0.1.0',
    author='Aditya Rai',
    author_email='team@veris.ai',
    packages=find_packages(),
    description='Generates a "private duplicate" of a given table, obfuscating any potential PII.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://veris.ai',  # replace with the real url of your package
    install_requires=[
        "pandas",
        "requests",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
