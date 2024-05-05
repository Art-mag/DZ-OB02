class User:
    def __init__(self, user_id, name, access_level='user'):
        self.user_id = user_id
        self.name = name
        self.access_level = access_level

    def __str__(self):
        return f"ID: {self.user_id}, Имя: {self.name}, Уровень доступа: {self.access_level}"


class Admin(User):
    def __init__(self, user_id, name, access_level='admin'):
        super().__init__(user_id, name, access_level)
        self.users_list = []

    def add_user(self, user):
        self.users_list.append(user)

    def remove_user(self, user_id):
        self.users_list = [user for user in self.users_list if user.user_id != user_id]

    def get_users_list(self):
        return self.users_list


# Пример использования
user1 = User(1, "Иван")
user2 = User(2, "Мария")
admin = Admin(100, "Администратор")

admin.add_user(user1)
admin.add_user(user2)

print("Список пользователей для администратора:")
for user in admin.get_users_list():
    print(user)

admin.remove_user(1)

print("\nСписок пользователей после удаления:")
for user in admin.get_users_list():
    print(user)

