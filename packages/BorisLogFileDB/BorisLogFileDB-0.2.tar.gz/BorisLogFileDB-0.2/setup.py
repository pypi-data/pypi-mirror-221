from setuptools import setup, find_packages

setup(
    name="BorisLogFileDB",
    version="0.2",
    author="boris.zhang",
    author_email="bodiz2007@163.com",
    description="python packages about logging, database process and folder or file operation.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
