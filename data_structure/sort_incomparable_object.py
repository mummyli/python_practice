class User:
    def __init__(self, user_id) -> None:
        self.user_id = user_id
    
    def __repr__(self) -> str:
        return "User{!r}".format(self.user_id)


users= [User(23), User(3), User(99), User(11)]

# 1、lambda表达式
print(sorted(users, key=lambda u: u.user_id))

# 2、attrgetter
from operator import attrgetter
print(sorted(users, key=attrgetter("user_id")))

# attrgetter也可以指定多个字段 sorted(users, key=attrgetter('last_name', 'first_name'))

# attrgetter会比lambda稍微快点
