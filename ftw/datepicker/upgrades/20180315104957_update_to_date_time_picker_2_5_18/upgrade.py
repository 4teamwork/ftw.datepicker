from ftw.upgrade import UpgradeStep


class UpdateToDateTimePicker2518(UpgradeStep):
    """Update to DateTimePicker 2.5.18.
    """

    def __call__(self):
        self.install_upgrade_profile()
