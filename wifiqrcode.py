from wifi_qrcode_generator import generator


wifi_config = generator.wifi_qrcode(ssid="xyz_zyx",
                                  hidden=False,
                                  authentication_type= "WPA",
                                  password="xxxxxxx")

wifi_config.print_ascii()
