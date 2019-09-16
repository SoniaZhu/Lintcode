## mine
class Solution:
    """
    @param emails:
    @return: The number of the different email addresses
    """
    def numUniqueEmails(self, emails):
        # write your code here
        s = set()
        for email in emails:
            idx = email.index('@')
            local = email[:idx]
            domain = email[idx:]
            s.add(self.simplify(local) + domain)
        return len(s)

    def simplify(self, s):
        if '+' in s:
            s = s[:s.index('+')]
        res = []
        for c in s:
            if c != '.':
                res.append(c)
        return ''.join(res)

## answer
class Solution:
    """
    @param emails:
    @return: The number of the different email addresses
    """
    def numUniqueEmails(self, emails):
        # write your code here
        different = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.split('+')[0].replace('.', '')
            # local_name = "".join(local_name.split('+')[0].split('.'))
            email = local_name + '@' + domain_name
            different.add(email)
        return len(different)
