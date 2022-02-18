def get_middle(s):
    return f"{s[int(len(s)/2) - 1]}{s[int(len(s)/2)]}" if len(s) % 2 == 0 else s[int(len(s)/2)]