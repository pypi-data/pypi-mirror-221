import requests


class Cheap():
    def __init__(self, api_key, api_secret):
        self.url_base = "https://api.proxy-cheap.com"
        self.headers = {
            "X-Api-Key": api_key,
            "X-Api-Secret": api_secret,
            "accept": "application/json",
            "Content-Type": "application/json"
        }

    def _handle_request(self, endpoint, method="GET", data=None):
        try:
            if method == "GET":
                response = requests.get("{}/{}".format(self.url_base, endpoint), headers=self.headers)
            elif method == "POST":
                response = requests.post("{}/{}".format(self.url_base, endpoint), headers=self.headers,
                                         json=data)
            else:
                raise ValueError("Unsupported HTTP method")

            response.raise_for_status()  # Raise an exception for unsuccessful requests
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception("Error making API request: {}".format(str(e)))

    def get_balance(self):
        return self._handle_request("account/balance")['balance']

    def get_proxy_info(self, proxy_id):
        return self._handle_request("proxies/{}".format(proxy_id))

    def cancel_proxy(self, proxy_id):
        self._handle_request("proxies/{}/cancel".format(proxy_id), method="POST")

    def get_all_proxies(self):
        return self._handle_request("proxies")

    def set_auto_extend(self, proxy_id, auto_extend):
        if auto_extend:
            self._handle_request("proxies/{}/auto-extend/enable".format(proxy_id), method="POST")
        else:
            self._handle_request("proxies/{}/auto-extend/disable".format(proxy_id), method="POST")

    def whitelist_ip(self, proxy_id, ip_to_whitelist):
        data = {"ips": [ip_to_whitelist]}
        return self._handle_request("proxies/{}/whitelist-ip".format(proxy_id), method="POST", data=data)

    def get_bandwidth_price(self, proxy_id, gb=1):
        data = {"bandwidth": gb}
        return self._handle_request("proxies/{}/bandwidth-price".format(proxy_id), method="POST", data=data)

    def buy_bandwidth(self, proxy_id, gb=1):
        data = {"bandwidth": gb}
        return self._handle_request("proxies/{}/buy-bandwidth".format(proxy_id), method="POST", data=data)

    def get_period_extension_price(self, proxy_id, months=1):
        data = {"periodInMonths": months}
        return self._handle_request("proxies/{}/period-extension-price".format(proxy_id), method="POST", data=data)

    def extend_period(self, proxy_id, months=1):
        data = {"periodInMonths": months}
        return self._handle_request("proxies/{}/extend-period".format(proxy_id), method="POST", data=data)

    def order_configuration(self, data):

        return self._handle_request("order/configuration", method="POST", data=data)

    def order_price(self, data):

        return self._handle_request("order/price", method="POST", data=data)

    def order_execute(self, data):

        return self._handle_request("order/price", method="POST", data=data)

    def get_order_info(self, order_id):
        return self._handle_request("orders/{}".format(order_id))

    def get_order_proxies(self, order_id):
        return self._handle_request("orders/{}/proxies".format(order_id))
