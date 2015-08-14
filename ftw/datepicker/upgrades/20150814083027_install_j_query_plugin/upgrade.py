from ftw.upgrade import UpgradeStep


class InstallJQueryPlugin(UpgradeStep):
    """Install j query plugin.
    """

    def __call__(self):
        self.install_upgrade_profile()
