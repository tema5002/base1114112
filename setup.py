from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: Microsoft :: Windows :: Windows 11",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3"
]

setup(
    name="base1114112",
    version="1.1",
    description="who in the world would use this",
    long_description="""# base1114112
# uses full range of 0x110000 symbols available in python

>>> from base1114112 import decode, encode
>>> print(decode("ерхину 🦔 и смерть в раю и огород 😼 в отъезде на сайте 🤓 в отъезде"))
1085581978826500573834917099094155227750390464337592599588190994098279211931471014871154389828550417577513724052123002662409962029918233461555484711956218897845304422848490685660644975271155189932486684841076536492687965928344976521862018853915341616806438777131745789129299247586607127698740798528803841228574787065688494267291476876475543533242693323342966516843476252284742679242697081909
>>> print(encode(7047530565501760338737361894658820726940540227402822885687894635203120983481008233243662212034357802881306782862235760252165407918616036280427233029943797802060100190280982150662028214962892489489971962767068291095973135612183600))
асексуал с охладителем для арбуза 🤩🤩🤩🤩
""",
    url="",
    author="tema5002",
    author_email="xtema5002x@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords="base1114112",
    packages=find_packages(),
    install_requires=[""],
    long_description_content_type="text/plain"
)
