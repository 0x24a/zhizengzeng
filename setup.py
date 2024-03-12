from setuptools import setup, find_packages

setup(
    name="zhizengzeng",
    version="0.1.1",
    author="0x24a",
    author_email="tanhanze@qq.com",
    description="A 3rd party SDK for ZhiZengZeng AI",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/0x24a/zhizengzeng",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)