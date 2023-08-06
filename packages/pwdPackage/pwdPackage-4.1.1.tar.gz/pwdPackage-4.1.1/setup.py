import setuptools

setuptools.setup(
    name='pwdPackage',
    version="4.1.1",
    author="Anant Chaudhary",
    zip_safe=False,
    description="password generator package",
    long_description="A package for generating passwords.",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={'pwdPackage': ['data/*.csv']},  # Correct the package_data key
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['pwdPackage'],
    package_dir={'':'.'},
    install_requires=[
        # Add any dependencies here
    ]
)


