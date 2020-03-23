from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("entry_points.ini", "r") as fh:
    entry_points = fh.read()


setup(
    name="tnc",
    version="0.0.2",
    author="TurBoss",
    author_email="j.l.toledano.l@gmail.com",
    description="TurBo NC - A QtPyVCP based Virtual Control Panel for LinuxCNC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TurBoss/tnc",
    download_url="https://github.com/TurBoss/tnc/tarball/master",
    packages=find_packages(),
    include_package_data=True,
    entry_points=entry_points,
    install_requires=[
        'qtpyvcp',
        'opencv-python==3.2.0.8'
    ],
)
