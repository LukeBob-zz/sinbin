# Author: LukeBob

import requests

class PasteBinApi:
    def __init__(self, dev_key=None):

        self.url             = "https://pastebin.com/api/"
        self.api_url         = self.url+"api_post.php"
        self.login_url       = self.url+"api_login.php"
        self.raw_url         = self.url+"api_raw.php"
        self.dev_key         = dev_key

    def user_key(self, username, password):
        try:
            paste_vars = {
                'api_dev_key'       : self.dev_key,
                'api_user_name'     : username,
                'api_user_password' : password
            }

            req = requests.post(self.login_url, data=paste_vars)
            return(req.text)

        except:
            raise
            return(None)

    def paste(self, user_key, title='Untitled', raw_code=None, private=None, api_paste_format=None, expire_date=None):
        try:
            paste_vars = {
                'api_option'       : 'paste',
                'api_paste_code'   : raw_code,
                'api_user_key'     : user_key,
                'api_dev_key'      : self.dev_key,
                'api_paste_name'   : title,
                'api_paste_format' : api_paste_format,
                'api_paste_private': private,
                'api_expire_date'  : expire_date
            }

            req = requests.post(self.api_url, data=paste_vars)
            return(req.text)

        except:
            raise
            return(None)

    def trends(self):

        try:
            paste_vars = {
                'api_option'  : 'trends',
                'api_dev_key' : self.dev_key
            }

            req = requests.post(self.api_url, data=paste_vars)
            return(req.text)

        except:
            raise
            return(None)

    def list_pastes(self, user_key=None, limit=50):

        try:
            paste_vars = {
                'api_option'        : 'list',
                'api_dev_key'       : self.dev_key,
                'api_user_key'      : user_key,
                'api_results_limit' : limit
            }
            req = requests.post(self.api_url, data=paste_vars)
            return(req.text)

        except:
            raise
            return(None)

    def get_raw(self, user_key=None, paste_key=None):
        try:
            paste_vars = {
                'api_option'       : 'show_paste',
                'api_user_key'     : user_key,
                'api_dev_key'      : self.dev_key,
                'api_paste_key'    : paste_key
            }
            req = requests.post(self.raw_url, data=paste_vars)
            return(req.text)

        except:
            raise
            return(None)

    def user_info(self, user_key=None,):
        try:
            paste_vars = {
                'api_option'  : 'userdetails',
                'api_user_key': user_key,
                'api_dev_key' : self.dev_key
            }
            req = requests.post(self.api_url, data=paste_vars)
            return(req.text)
        except:
            raise
            return(None)

    def delete_paste(self, user_key, paste_key):
        try:
            paste_vars = {
                'api_option'       : 'delete',
                'api_user_key'     : user_key,
                'api_dev_key'      : self.dev_key,
                'api_paste_key'    : paste_key
            }
            req = requests.post(self.api_url, data=paste_vars)
            print(req.text)

        except:
            raise
            return(None)
