from setuptools import setup, find_packages

setup(
    name='django-feedutil',
    version='0.1.0',
    description='RSS+ATOM Feed replication for django sites',
    author='Doug Napoleone',
    author_email='doug.napoleone@gmail.com',
    url='http://code.google.com/p/django-feedutil/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
    setup_requires=['setuptools_git'],
)
