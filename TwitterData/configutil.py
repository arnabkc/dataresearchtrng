__author__ = 'arnab'

import ConfigParser

class ConfigUtil:
    config_dict = {}

    def __init__(self, cFile = 'twitter_oauth_config.cfg'):
        config = ConfigParser.SafeConfigParser()
        config.read(cFile)

        ConfigUtil.config_dict['access_token'] = config.get('oauth', 'access_token')
        ConfigUtil.config_dict['access_token_secret'] = config.get('oauth', 'access_token_secret')
        ConfigUtil.config_dict['consumer_key'] = config.get('oauth', 'consumer_key')
        ConfigUtil.config_dict['consumer_secret'] = config.get('oauth', 'consumer_secret')

    def get_config(self):
        return ConfigUtil.config_dict


c = ConfigUtil()
c_dict = c.get_config()

print c_dict
