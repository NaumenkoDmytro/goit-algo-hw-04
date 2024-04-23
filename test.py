


# def parse_input(user_input):
#     user_input = user_input.strip()
#     if not user_input:
#         return []
#     cmd, *args = user_input.split()
#     cmd = cmd.lower()
#     return cmd, *args

# print(parse_input('add dmytro 2323455'))

def parse_input(user_input):
    user_input = user_input.strip()
    if not user_input:
        return []
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, args

print(parse_input('add dmytro 2323455'))