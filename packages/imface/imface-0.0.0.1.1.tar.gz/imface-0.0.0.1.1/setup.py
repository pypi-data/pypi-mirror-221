from setuptools import setup, find_packages
from setuptools.command.install import install
from pathlib import Path
import gdown
import os

home_dir = Path.home()
def downloadWeights():
    facenet512_url = "https://github.com/serengil/deepface_models/releases/download/v1.0/facenet512_weights.h5"
    retinaface_url = "https://github.com/serengil/deepface_models/releases/download/v1.0/retinaface.h5"
    if os.path.isfile(str(home_dir) + "/.deepface/weights/facenet512_weights.h5") != True:
        print("facenet512_weights.h5 will be downloaded...")

        output = str(home_dir) + "/.deepface/weights/facenet512_weights.h5"
        gdown.download(facenet512_url, output, quiet=False)
    if os.path.isfile(str(home_dir) + "/.deepface/weights/retinaface.h5") != True:
        print("retinaface.h5 will be downloaded...")

        output = str(home_dir) + "/.deepface/weights/retinaface.h5"
        gdown.download(retinaface_url, output, quiet=False)

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        downloadWeights()

with open("README.md", "r") as file:
    description = file.read()

requirements = ["deepface"]

setup(
    name='imface',
    version='0.0.0.1.1',
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["imface=imface.main:main"]},
    author="Achmad Alfazari",
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Programming Language :: Python",
    ],
    long_description=description,
    long_description_content_type="text/markdown",
    python_requires=">=3.5.5",
    cmdclass={
        'install': CustomInstallCommand,
    },
)