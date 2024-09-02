class User:
    def __init__(self, username):
        self.username = username

    def send_message(self, chat_room, message):
        chat_room.receive_message(self, message)

    def receive_message(self, sender, message):
        print(f"{sender.username}: {message}")


class ChatRoom:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def receive_message(self, sender, message):
        for user in self.users:
            if user != sender:
                user.receive_message(sender, message)


# Example usage:
if __name__ == "__main__":
    # Create users
    user1 = User("Alice")
    user2 = User("Bob")
    user3 = User("Charlie")

    # Create a chat room
    chat_room = ChatRoom()
    chat_room.add_user(user1)
    chat_room.add_user(user2)
    chat_room.add_user(user3)

    # Users send messages
    user1.send_message(chat_room, "Hello, everyone!")
    user2.send_message(chat_room, "Hey Alice!")
    user3.send_message(chat_room, "Hi, Bob!")
