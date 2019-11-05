# Samuel Dunn
# CS320, POFIS.
# This setup script manages bundling POFIS into a redistributable wheel.
# (wheel is the python package format)

from setuptools import setup, find_packages

# POFIS's version (may want to import this from POFIS
# directly in the future.)
version = '0.0.0b1'

# Dependencies for POFIS runtime.
dependencies = ('cherrypy', )

# Any non-python files to include within the distribution
# (Such as templates, html files, .rst files, etc.)
static_data = {

}

if __name__ == "__main__":
    setup(
        name="pofis",
        version=version,
        packages=find_packages(),
        package_data=static_data,
        author="Abdi Vicenciodelmoral, Andrew Cornish, Becca Daniels, Samuel Dunn",
        # include emails in the future.
        install_requires=dependencies
        entry_points={'console_scripts': ['POFIS_quicklaunch=pofis:quicklaunch']}
    )