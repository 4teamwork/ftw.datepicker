from ftw.upgrade import UpgradeStep


class AddVariousConfigs(UpgradeStep):
    """Add various configs.
    """

    def __call__(self):
        self.install_upgrade_profile()
