import setuptools


setuptools.setup(
    name="packageN",                     # This is the name of the package
    version="1.1.6",                        # The initial release version
     
    author="Nipun Dogra",                     # Full name of the author
    description="sample description",
    package_data={'packageN': ['/*.csv']},
    include_package_data = True,
    long_description_content_type="text/markdown",
 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["quicksample"],             # Name of the python package
    install_requires=[]                     # Install other dependencies if any
)
