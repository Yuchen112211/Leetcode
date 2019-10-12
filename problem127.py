class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		def distance(word1,word2):
			dis = 0
			for i in range(len(word1)):
				if word1[i] != word2[i]:
					dis += 1
			return dis == 1

		def getAllDistance(matrix,start):
			g = matrix
			visited = [0 for i in g]
			visited[start] = 1
			distances = [len(g)*2 for i in g]
			distances[start] = 0
			stack = [start]
			while stack:
				if 0 not in visited:
					break
				index_now = stack.pop()
				visited[index_now] = 1
				path_now = g[index_now]
				next_distance = distances[index_now] + 1
				for i in range(len(path_now)):
					if path_now[i] == 1 and (visited[i] == 0 or distances[i] > next_distance):
						distances[i] = min(distances[i],next_distance)
						stack.append(i)
				if len(stack) == 0 and 0 in visited:
					stack.append(visited.index(0))
					visited[visited.index(0)] = 1
			return distances

		if endWord not in wordList or len(wordList) == 0:
			return 0

		if beginWord in wordList:
			wordList.remove(beginWord)
			wordList.append(beginWord)
		else:
			wordList.append(beginWord)

		all_words = wordList
		matrix = [[0 for i in all_words] for k in all_words]
		for i in range(len(wordList)-1):
			for k in range(i,len(wordList)):
				if distance(wordList[i],wordList[k]):
					matrix[i][k] = 1
					matrix[k][i] = 1
		steps = getAllDistance(matrix,len(matrix)-1)
		for i in range(len(wordList)):
			if wordList[i] == endWord:
				tmp = steps[i] + 1
				if tmp > len(matrix):
					return 0
				else:
					return tmp
		return 0

if __name__ == '__main__':
	s = Solution()
	beginWord = 'cet'
	endWord = 'ism'
	wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
	#wordList = ['hit','cog']
	val = s.ladderLength(beginWord,endWord,wordList)
	print val