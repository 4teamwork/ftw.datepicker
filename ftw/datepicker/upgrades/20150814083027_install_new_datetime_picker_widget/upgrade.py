from ftw.upgrade import UpgradeStep


class InstallNewDateTimePickerWidget(UpgradeStep):
    """Install new date/time picker widget.
    """

    def __call__(self):
        self.install_upgrade_profile()
