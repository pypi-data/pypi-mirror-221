# -*- coding: utf-8 -*-

from pybuilder.core import depends, init, task
from pybuilder.errors import BuildFailedException


@init
def init_docstr_coverage_plugin(project):
    project.plugin_depends_on("docstr-coverage", "~=2.3.0")

@task("docstr_coverage", "Checks coverage of docstrings")
@depends("prepare")
def docstr_coverage(project, logger):
    # get location of source files
    src_dir = project.expand_path(project.get_property("dir_source_main_python"))
    docstr_args = [src_dir]

    # override default coverage threshold
    fail_under = project.get_property("docstr_coverage_fail_under", None)
    if fail_under is not None:
        docstr_args = ["--fail-under="+str(fail_under)]+docstr_args

    # override default config file
    config_path = project.get_property("docstr_coverage_config", None)
    if config_path is not None:
        docstr_args = ["--config="+str(config_path)]+docstr_args

    import docstr_coverage
    docstr_coverage.printers.logger = logger  # use pybuilder's logger

    from docstr_coverage.cli import execute
    try:
        execute.main(args=docstr_args)
    except SystemExit as e:
        if e.code != 0:
            raise BuildFailedException("Docstring coverage failed")
