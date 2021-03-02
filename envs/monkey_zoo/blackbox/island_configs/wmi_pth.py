from envs.monkey_zoo.blackbox.island_configs.base_template import BaseTemplate


class WmiPth(BaseTemplate):
    config_values = BaseTemplate.config_values

    config_values.update({
        "basic.exploiters.exploiter_classes": ["WmiExploiter"],
        "basic_network.scope.subnet_scan_list": ["10.2.2.15"],
        "basic.credentials.exploit_password_list": ["Password1!"],
        "basic.credentials.exploit_user_list": ["Administrator",
                                                "m0nk3y",
                                                "user"],
        "internal.classes.finger_classes": ["PingScanner",
                                            "HTTPFinger"],
        "internal.classes.exploits.exploit_ntlm_hash_list": ["5da0889ea2081aa79f6852294cba4a5e",
                                                             "50c9987a6bf1ac59398df9f911122c9b"]
    })
