class Solution:
    def numUniqueEmails(self, emails):
        _dict = {}
        for email in emails:
            at_idx = email.index('@')
            if email[:at_idx].count('+') == 0:
                if email[:at_idx].count('.') == 0:
                    new_mail_address = email
                else:
                    new_mail_address = email[:at_idx].replace('.', '') + email[at_idx:]
            else:
                if email[:at_idx].count('.') == 0:
                    new_mail_address = email[:email.index('+')] + email[at_idx:]
                else:
                    new_mail_address = email[:email.index('+')].replace('.', '') + email[at_idx:]
            if new_mail_address not in _dict.keys():
                _dict[new_mail_address] = 1
        return len(_dict.keys())


class Solution2:
    def numUniqueEmails(self, emails):
        _dict = {}
        for email in emails:
            tmp = email.split('@')
            local_name = tmp[0].split('+')[0].replace('.', '')
            if local_name + '@' + tmp[1] not in _dict.keys():
                _dict[local_name+'@'+tmp[1]] = 1
        return len(_dict.keys())
