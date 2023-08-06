from setuptools import setup

readme = open("./README.md", "r")

setup(
    name="Widget Controller",
    packages=["WC"],
    version="2.0.1",
    description="Una libreria para crear facilmente UI (traducido de Tkinter y otros)",
    long_description=readme.read(),
    long_description_content_type="text/markdown",
    author="Z3R0_GT",
    author_email="contac.es.z3r0.gt@gmail.com",
    url="https://github.com/Z3R0GT/WC",
    download_url="https://github.com/Z3R0GT/WC/releases/tag/BUILD-2.0",
    keywords=["ui", "UI", "Tkinter", "logging", "build"],
    classifiers=[ ],
    requires=["Tk", "Pillow"],
    license="OTHER",
    
    include_package_data=True
)