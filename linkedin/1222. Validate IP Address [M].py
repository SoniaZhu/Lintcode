class Solution:
    """
    @param IP: the given IP
    @return: whether an input string is a valid IPv4 address or IPv6 address or neither
    """
    def validIPAddress(self, IP):
        # Write your code here
        if self.isValidIPv4(IP):
            return 'IPv4'
        if self.isValidIPv6(IP):
            return 'IPv6'
        return 'Neither'

    def isValidIPv4(self, str):
        PERIOD = '.'
        parts = str.split(PERIOD)
        if len(parts) != 4:
            return False
        for part in parts:
            if not self.isValidIPv4Part(part):
                return False
        return True

    def isValidIPv4Part(self, str):
        for c in str:
            if not c.isdigit():
                return False
        if str[0] == '0':
            return False
        return int(str) <= 255

    def isValidIPv6(self, str):
        COLONS = ':'
        parts = str.split(COLONS)
        if len(parts) != 8:
            return False
        for part in parts:
            if not self.isValidIPv6Part(part):
                return False
        return True

    def isValidIPv6Part(self, s):
        validChars = [str(i) for i in range(10)]
        validChars += ['a', 'b', 'c', 'd', 'e', 'f']
        if not s:
            return False
        if len(s) > 4:
            return False
        for c in s:
            if c.lower() not in validChars:
                return False
        return True
