import re
from typing import List


class UniqueEmailAddresses:

    def numUniqueEmails(self, emails: List[str]) -> int:
        eset = set()
        for s in emails:
            name, domain = s.split('@')
            name = name.replace(".", '')
            name = re.sub('\+.*$','', name)
            eset.add((name, domain))
        return len(eset)


alg = UniqueEmailAddresses()

e = ['a.b@c', 'ab.+c+d@c']
print(f'emails:{e}, addresses:{alg.numUniqueEmails(e)}')

e = ['a@b', 'c@d']
print(f'emails:{e}, addresses:{alg.numUniqueEmails(e)}')

e = ['@']
print(f'emails:{e}, addresses:{alg.numUniqueEmails(e)}')
