import re


def create_phone_number(n):
    a = "".join(map(str, n))
    return f'({a[:3]}) {a[3:6]}-{a[:-1]}'


#     return f"""({
# re.findall(r'^.{3}', "".join(map(str, n)))[0]}) {
# re.findall(r'.{3}(.{3})', "".join(map(str, n)))[0]}-{
# re.findall(r'.{4}$', "".join(map(str, n)))[0]}"""