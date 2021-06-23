import setuptools

setuptools.setup(
    name = 'ArithmaticPackage',
    version = "0.0.1",
    author = "Pooja Solaikannu",
    author_email = "poojasolai97@gmail.com",
    description = "Simple arithmatic problem",
    long_description = "Just a simple function which does addition of two numbers given inputs of two numbers(a, b)",
    long_description_content_type = "text",
    url="",
    packages=setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python",
        "Licence :: OSI Approved :: MIT Licence",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)