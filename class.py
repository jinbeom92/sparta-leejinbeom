import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        sha256 = hashlib.sha256()
        sha256.update(password.encode("utf-8"))
        return sha256.hexdigest()

    def display(self):
        print(f"Name: {self.name}\nUsername: {self.username}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


member_list = []
while True:
    name = input("등록할 ID를 입력해주세요!: ")
    username = input("닉네임을 입력해주세요!: ")
    password = input("비밀번호를 입력해주세요!: ")
    member = Member(name, username, password)
    member_list.append(member)

    more_members = input("회원 등록 하시겠습니까? (yes/no): ")
    if more_members.lower() != "yes":
        break

post_list = []
for member in member_list:
    for i in range(3):
        title = input(f"{member.name}회원 {i+1}의 제목을 입력해주세요!: ")
        content = input(f"{member.name}회원 {i+1}의 내용을 입력해주세요!: ")
        post_instance = Post(title, content, member.username)
        post_list.append(post_instance)

print("\n등록된 회원들:")
for member in member_list:
    print(member.name)

specific_user = input("\n게시물을 보려면 닉네임을 입력하세요!: ")
print(f"\nPosts by {specific_user}:")
for post in post_list:
    if post.author == specific_user:
        print(post.title)

specific_word = input("\n검색할 단어(내용): ")
print(f"\n검색된 단어들 '{specific_word}' in content:")
for post in post_list:
    if specific_word in post.content:
        print(post.title)
