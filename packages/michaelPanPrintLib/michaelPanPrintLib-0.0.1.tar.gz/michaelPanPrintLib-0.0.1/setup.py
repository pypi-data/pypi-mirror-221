import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="michaelPanPrintLib",  # 库的名称
    version="0.0.1",  # 库的版本号
    author="chuntong pan",  # 库的作者
    author_email="panzhang1314@gmail.com",  # 作者邮箱
    description="change output style",  # 库的简述
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
    install_requires=['colorama']
)
