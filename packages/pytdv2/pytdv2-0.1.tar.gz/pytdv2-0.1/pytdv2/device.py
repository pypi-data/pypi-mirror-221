class Device:
    def __init__(self, fazpass_id=None, is_active=None, scoring=None, risk_level=None, time_stamp=None,
                 platform=None, is_rooted=None, is_emulator=None, is_gps_spoof=None, is_app_tempering=None,
                 is_vpn=None, is_clone_app=None, is_screen_sharing=None, is_debug=None, application=None,
                 device_id=None, sim_serial=None, sim_operator=None, geolocation=None, client_ip=None):
        self.fazpass_id = fazpass_id
        self.is_active = is_active
        self.scoring = scoring
        self.risk_level = risk_level
        self.time_stamp = time_stamp
        self.platform = platform
        self.is_rooted = is_rooted
        self.is_emulator = is_emulator
        self.is_gps_spoof = is_gps_spoof
        self.is_app_tempering = is_app_tempering
        self.is_vpn = is_vpn
        self.is_clone_app = is_clone_app
        self.is_screen_sharing = is_screen_sharing
        self.is_debug = is_debug
        self.application = application
        self.device_id = device_id
        self.sim_serial = sim_serial
        self.sim_operator = sim_operator
        self.geolocation = geolocation
        self.client_ip = client_ip
