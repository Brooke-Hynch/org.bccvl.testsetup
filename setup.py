from setuptools import setup, find_packages
import os

version = '1.14.0.dev0'

setup(
    name='org.bccvl.testsetup',
    version=version,
    description="BCCVL Test Content Setup",
    # long_description=open("README.txt").read() + "\n" +
    #                  open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='',
    author='',
    author_email='',
    url='http://svn.plone.org/svn/collective/',
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['org', 'org.bccvl'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    [zopectl.command]
    testsetup = org.bccvl.testsetup.main:zopectl
    manage = org.bccvl.testsetup.manage:zopectl
    """,
    )
