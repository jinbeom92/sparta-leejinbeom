import hashlib
import csv


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


def save_members_to_csv(member_list, csv_path):
    with open(csv_path, "w", newline='', encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Name", "Username", "Password"])
        for member in member_list:
            csv_writer.writerow(
                [member.name, member.username, member.password])


def load_members_from_csv(csv_path):
    member_list = []
    with open(csv_path, "r", newline='', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if len(row) == 3:
                name, username, password = row
                member = Member(name, username, password)
                member_list.append(member)
    return member_list


def save_posts_to_csv(post_list, csv_path):
    with open(csv_path, "w", newline='', encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Title", "Content", "Author"])
        for post in post_list:
            csv_writer.writerow([post.title, post.content, post.author])


def load_posts_from_csv(csv_path):
    post_list = []
    with open(csv_path, "r", newline='', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if len(row) == 3:
                title, content, author = row
                post = Post(title, content, author)
                post_list.append(post)
    return post_list


csv_path_members = "class1.csv"
csv_path_posts = "class2.csv"

member_list = load_members_from_csv(csv_path_members)
post_list = load_posts_from_csv(csv_path_posts)

search_option = input(
    "사용자 등록을 하시겠습니까? 아니면 검색을 바로 하시겠습니까? (등록/검색): ").strip()

if search_option.lower() == "등록":
    while True:
        name = input("이름을 등록해주세요: ")
        username = input("닉네임을 입력해주세요: ")
        password = input("비밀번호를 입력해주세요: ")
        member = Member(name, username, password)
        member_list.append(member)

        more_members = input("회원 등록 하시겠습니까? (yes/no): ").strip()
        if more_members.lower() != "yes":
            break

    save_members_to_csv(member_list, csv_path_members)
    save_posts_to_csv(post_list, csv_path_posts)

elif search_option.lower() == "검색":
    specific_user = input("\n닉네임을 검색하여 게시물을 불러옵니다. 닉네임을 입력하세요: ")
    print(f"\n'{specific_user}'님의 게시물:")
    for post in post_list:
        if post.author == specific_user:
            print(f"제목: {post.title}\n내용: {post.content}\n")

    specific_word = input("\n검색할 단어(제목 또는 내용)를 입력하세요: ")
    print(f"\n'{specific_word}' 단어로 검색한 결과:")
    for post in post_list:
        if specific_word.lower() in post.title.lower() or specific_word.lower() in post.content.lower():
            print(f"작성자: {post.author}\n제목: {post.title}\n내용: {post.content}\n")
else:
    print("올바른 옵션을 선택해주세요.")

