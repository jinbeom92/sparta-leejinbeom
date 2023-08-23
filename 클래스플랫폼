import hashlib
import csv


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def _hash_password(self, password):
        return password

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


csv_path_members = "class1.csv"  # csv파일을 class1.csv로 만들기
csv_path_posts = "class2.csv"  # csv파일을 class2.csv로 만들기

member_list = load_members_from_csv(csv_path_members)
post_list = load_posts_from_csv(csv_path_posts)

logged_in_user = None

while True:
    if logged_in_user:
        action = input(
            f"{logged_in_user.username}님, 어떤 업무를 하시겠습니까? (글쓰기/검색/로그아웃/나가기): ").strip()
    else:
        action = input(
            "어떤 업무를 하시겠습니까? (등록/로그인/검색/나가기): ").strip()

    if action.lower() == "등록":
        name = input("이름을 등록해주세요(나가기): ")
        if name.lower() == "나가기":
            break
        username = input("닉네임을 입력해주세요(나가기): ")
        if username.lower() == "나가기":
            break
        password = input("비밀번호를 입력해주세요(나가기): ")
        if password.lower() == "나가기":
            break

        member = Member(name, username, password)
        member_list.append(member)
        save_members_to_csv(member_list, csv_path_members)

    elif action.lower() == "로그인":
        username = input("닉네임을 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")

        for member in member_list:
            if member.username == username and member.password == password:
                logged_in_user = member
                print(f"{logged_in_user.username}님, 로그인 되었습니다.")
                break
        else:
            print("잘못된 닉네임 또는 비밀번호입니다.")

    elif action.lower() == "글쓰기":
        if logged_in_user:
            title = input("제목을 입력하세요: ")
            content = input("내용을 입력하세요: ")
            post = Post(title, content, logged_in_user.username)
            post_list.append(post)
            save_posts_to_csv(post_list, csv_path_posts)
            print("글이 성공적으로 작성되었습니다.")
        else:
            print("로그인 후에 글쓰기가 가능합니다.")

    elif action.lower() == "검색":
        search_option = input("어떤 항목으로 검색하시겠습니까? (제목/내용): ").strip().lower()

        if search_option == "제목":
            specific_title = input("검색할 제목을 입력하세요: ")
            print(f"'{specific_title}' 제목으로 검색한 결과:")
            for post in post_list:
                if specific_title.lower() in post.title.lower():
                    print(
                        f"작성자: {post.author}\n제목: {post.title}\n내용: {post.content}\n")
        elif search_option == "내용":
            specific_content = input("검색할 내용을 입력하세요: ")
            print(f"'{specific_content}' 내용으로 검색한 결과:")
            for post in post_list:
                if specific_content.lower() in post.content.lower():
                    print(
                        f"작성자: {post.author}\n제목: {post.title}\n내용: {post.content}\n")
        else:
            print("올바른 검색 옵션을 선택해주세요.")

    elif action.lower() == "로그아웃":
        logged_in_user = None
        print("로그아웃 되었습니다.")

    elif action.lower() == "나가기":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 옵션을 선택해주세요.")

