from ftw.upgrade import UpgradeStep


class FixResourceBundles(UpgradeStep):
    """Fix resource bundles.
    """

    def __call__(self):
        self.install_upgrade_profile()
