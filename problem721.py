class Solution(object):
	def accountsMerge(self, accounts):
		"""
		:type accounts: List[List[str]]
		:rtype: List[List[str]]
		"""
		names = []
		emails = []

		for account in accounts:
			has = False
			for i in range(len(names)):
				if names[i] == account[0]:
					for email in account[1:]:
						if email in emails[i]:
							has = True
							break
					if has:
						for email in account[1:]:
							emails[i].add(email)
						break
			if not has:
				names.append(account[0])
				emails.append(set(account[1:]))
		rst = [[names[i]] + sorted(list(emails[i])) for i in range(len(names))]
		if len(rst) != len(accounts):
			anotherRst = self.accountsMerge(rst)
			return anotherRst
		else:
			return rst

s = Solution()
accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]

print s.accountsMerge(accounts)