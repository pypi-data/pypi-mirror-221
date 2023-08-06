#!/usr/bin/env python
#   -*- coding: utf-8 -*-

from setuptools import setup, Extension
from setuptools.command.install import install as _install


class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()



if __name__ == '__main__':
    setup(
        name = 'pybuilder-docstr-coverage',
        version = '0.1.0',
        description = 'PyBuilder plugin that checks documentation coverage using docstr-coverage',
        long_description = 'Uses docstr-coverage to check documentation coverage of your project.\n\nYou can configure the docstr-coverage package using the following properties:\n\n- `docstr_coverage_fail_under`: The minimum coverage percentage that must be achieved. \n  If the coverage is below this value, the build will fail. This will take\n  precedence over the value set in the configuration file.\n- `docstr_coverage_config`: The path to the configuration file for docstr-coverage.\n  Default: .docstr.yaml\n',
        long_description_content_type = None,
        classifiers = [
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3'
        ],
        keywords = '',

        author = 'Adam Chýlek',
        author_email = 'adam.chylek@amitia-ai.com',
        maintainer = '',
        maintainer_email = '',

        license = 'MIT',

        url = 'https://github.com/chylek/pybuilder-docstr-coverage',
        project_urls = {},

        scripts = [],
        packages = ['pybuilder_docstr_coverage'],
        namespace_packages = [],
        py_modules = [],
        ext_modules = [],
        entry_points = {},
        data_files = [],
        package_data = {},
        include_package_data = False,
        install_requires = [],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
