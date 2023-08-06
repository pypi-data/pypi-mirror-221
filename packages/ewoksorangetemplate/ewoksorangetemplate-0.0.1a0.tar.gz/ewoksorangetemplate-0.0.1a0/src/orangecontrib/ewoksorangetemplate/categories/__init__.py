import sysconfig

WIDGET_HELP_PATH = (
    # Development documentation (make htmlhelp in ./doc)
    ("{DEVELOP_ROOT}/doc/_build/htmlhelp/index.html", None),
    # Documentation included in wheel
    ("{}/help/ewoksorangetemplate/index.html".format(sysconfig.get_path("data")), None),
    # Online documentation url
    ("https://ewoksorangetemplate.readthedocs.io", ""),
)


# Entry point for main Orange categories/widgets discovery
def widget_discovery(discovery):
    import pkg_resources

    dist = pkg_resources.get_distribution("ewoksorangetemplate")
    pkgs = [
        "orangecontrib.ewoksorangetemplate.categories.examples1",
        "orangecontrib.ewoksorangetemplate.categories.examples2",
    ]
    for pkg in pkgs:
        discovery.process_category_package(pkg, distribution=dist)
