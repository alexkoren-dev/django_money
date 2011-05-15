from distutils.core import setup


# Load in babel support, if available.
try:
    from babel.messages import frontend as babel
    cmdclass = {"compile_catalog": babel.compile_catalog,
                "extract_messages": babel.extract_messages,
                "init_catalog": babel.init_catalog,
                "update_catalog": babel.update_catalog,}
except ImportError:
    cmdclass = {}


setup(name="django-money",
      version="1.0-alpha",
      description="Adds support for using money and currency fields in django models and forms. Uses py-moneyed as money implementation, based on python-moneys django classes.",
      url="https://github.com/jakewins/django-money",
      zip_safe=False,
      packages=["djmoney",
                "djmoney.forms", 
                "djmoney.models"],
      package_dir={"": "src"},
      cmdclass = cmdclass,
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Framework :: Django",])


