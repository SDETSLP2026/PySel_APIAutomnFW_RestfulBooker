# All the common code is put here in utils

class Utils:
    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json",
        }
        return headers

    def common_headers_xml(self):
        headers = {
            "Content-Type": "application/xml",
        }
        return headers

    def common_header_put_patch_delete_basic_auth(self, basic_auth_value):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic " + str(basic_auth_value),
        }
        return headers

    # auth -> basic auth (admin, password -> base64)
    # auth -> bearer auth (api token) nkasdfhh893r46912vcjewgkc783...... Long alphanumeric string

    def common_header_put_patch_delete_bearer_auth(self, api_token):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + str(api_token),
        }
        return headers

    def common_header_put_delete_patch_cookie(self, token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),
        }
        return headers

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database(self):
        pass
