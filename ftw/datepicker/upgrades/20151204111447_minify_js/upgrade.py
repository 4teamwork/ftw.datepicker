from ftw.upgrade import UpgradeStep


class MinifyJS(UpgradeStep):
    """Minify js.
    """

    def __call__(self):
        self.install_upgrade_profile()
