import setuptools

setuptools.setup(
    name="crawler_commons",
    version="0.0.52",
    license='MIT',
    install_requires=[
        "requests",
        "numpy",
        "pyyaml"
    ],
    author="cheddars",
    author_email="nezahrish@gmail.com",
    description="crawler commons",
    long_description=open('README.md').read(),
    url="https://github.com/cheddars/crawler_commons",
    packages=setuptools.find_packages(exclude=("test",)),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
