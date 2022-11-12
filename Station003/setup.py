from setuptools import find_packages, setup

setup(
    name='ekylenath',
    version='1.0.0',
    port='0.0.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask','flask-mail','numpy' , 'phonenumbers' , 'geocoder' , 'folium'
    ],
)
