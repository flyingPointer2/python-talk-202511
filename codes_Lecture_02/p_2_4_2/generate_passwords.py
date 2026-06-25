import random
import string


def generate_password(length=16):
    """ 生成一定长度的密码 """
    characters = string.ascii_letters + string.digits + '_-+%$@#&*^'
    random_characters_list = [random.choice(characters) for _ in range(length)]
    generated_password = ''.join(random_characters_list)
    return generated_password



if __name__ == '__main__':
    password = generate_password(12)
    print(f"生成的密码: {password}")


