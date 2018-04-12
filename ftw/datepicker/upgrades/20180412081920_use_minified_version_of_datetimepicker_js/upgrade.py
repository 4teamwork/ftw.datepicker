from ftw.upgrade import UpgradeStep


class UseMinifiedVersionOfDatetimepickerJS(UpgradeStep):
    """Use minified version of datetimepicker JS.
    """

    def __call__(self):
        self.install_upgrade_profile()
