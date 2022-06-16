import menu

class Account(object):
    def __init__(self, username, password, site):
        self.username = username
        self.username_insensitive = username.lower()
        self.password = password
        self.site = site
        self.site_insensitive = site.lower()

    def get_username(self):
        return self.username

    def get_username_insensitive(self):
        return self.username_insensitive

    def get_password(self):
        return self.password

    def get_site(self):
        return self.site

    def get_site_insensitive(self):
        return self.site_insensitive

    def show(self):
        info = 'Site: {}, Username: {}, Password: {}'.format(self.site, self.username, self.password)
        menu.print_msg(info, 'green')
        