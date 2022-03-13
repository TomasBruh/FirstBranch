from cryptography.fernet import Fernet
import keys
FERNET = Fernet(keys.key)


class User:
    def __int__(self, user_name, user_password):
        self.name = user_name
        self.password = user_password
        self.high_score = 0


class Login:
    def __int__(self, user):
        self.user = user
        self.all_users = self.get_all_users()

    def register_user(self):
        with open("logins.txt", 'a') as write_stream:
            string_to_write = ""
            string_to_write += FERNET.encrypt(self.user.name.encode()) + " ".encode() + FERNET.encrypt(self.user.password.encode())
            write_stream.writelines([string_to_write])

    def get_all_users(self):
        all_users = dict()

        try:
            with open("logins.txt", 'r') as read_stream:
                raw_data = read_stream.readlines()
                read_stream.close()
            for item in raw_data:
                items = item.split(' ')
                user_name = items[0]
                user_password = items[1]
                user_name = str.encode(user_name)
                user_name = FERNET.decrypt(user_name).decode()
                user_password = str.encode(user_password)
                user_password = FERNET.decrypt(user_password).decode()
                all_users[user_name] = user_password
            return all_users
        except FileNotFoundError:
            return all_users
