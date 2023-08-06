import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="michael-pan-first-lib",  # 库名
    version="0.0.1",  # 库版本
    author="chuntong pan",  # 作者
    author_email="panzhang1314@gmail.com",  # 作者邮箱
    description="第一个测试库",  # 简述
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/p110120p1/Logistics",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)