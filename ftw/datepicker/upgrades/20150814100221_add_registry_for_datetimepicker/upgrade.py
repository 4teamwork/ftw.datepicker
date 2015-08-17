from ftw.upgrade import UpgradeStep


class AddRegistryForDatetimepicker(UpgradeStep):
    """Add registry for datetimepicker.
    """

    def __call__(self):
        self.install_upgrade_profile()
