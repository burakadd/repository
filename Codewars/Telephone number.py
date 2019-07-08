import re


def create_phone_number(n):
    return f"""({
re.findall(r'^[0-9]{3}', "".join(map(str, n)))[0]}) {
re.findall(r'.{3}([0-9]{3})', "".join(map(str, n)))[0]}-{
re.findall(r'[0-9]{4}$', "".join(map(str, n)))[0]}"""


print(create_phone_number(list(range(10))))

re.sub(