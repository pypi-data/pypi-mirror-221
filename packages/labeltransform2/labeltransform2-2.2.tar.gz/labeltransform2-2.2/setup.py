import setuptools


setuptools.setup(
    name="labeltransform2",
    version="2.2",
    author="victor",
    description="dataset label style transform tool",
    url="https://gitee.com/free_bigD/labeltransform.git",
    packages=setuptools.find_packages(),
    package_data={
        "labeltransform2": ["xml/voc.xml"]
    },
    install_requires=["opencv-python", "pandas", "scikit-learn"],
    python_requires='>=3'
)