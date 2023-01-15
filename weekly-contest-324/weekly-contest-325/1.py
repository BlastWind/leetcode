from itertools import chain
from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        rightDist, leftDist = -1, -1 
        rightAcc, leftAcc = 0, 0
        print(len(words))
        if words[startIndex] == target: return 0

        for i in chain(range(startIndex, len(words))):
            print(i)
            if words[i] == target: 
                rightDist = rightAcc
                break 
            rightAcc += 1
        if rightDist == -1: 
            for i in range(0, startIndex+1):
                print(i)

                if words[i] == target: 
                    rightDist = rightAcc
                    break    
                rightAcc += 1

        for i in chain(range(startIndex, -1, -1)):
            print(i)

            if words[i] == target: 
                leftDist = leftAcc
                break 
            leftAcc += 1

        if leftDist == -1:


            for i in range(len(words)-1, startIndex-1, -1):
                print(i)
                if words[i] == target: 
                    leftDist = leftAcc
                    break
                leftAcc += 1

        if leftDist == -1: return rightDist
        if rightDist == -1: return leftDist

        return min([rightDist, leftDist])

a = Solution()
# print(a.closetTarget(["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"], "zemkwvqrww", 8))

print(a.closetTarget(
["aawyoesnjcwqruglyfcnpegnuldlwptcumkiphobxwuxyiwjlf","eaqdovsrujhtcicbfatmipvbwpbmlxanetmalajsfvdwovchtt","quwmjnluvdieyslkkzfvcezbapnpgpdpzeicxnsbxbdjyigogu","xwniqsgthhyrnaljcsbuljblwhyvinlrhcflqdonygyihcezoy","ozxpozhjxckidlryiuwpozxxzazegqwdpsghqpqsoxurwexgnx","quwmjnluvdieyslkkzfvcezbapnpgpdpzeicxnsbxbdjyigogu","chzkqmmgqwtqhdobgiupjqdaxjexhpjssucwtvkajrpazgbbst","chzkqmmgqwtqhdobgiupjqdaxjexhpjssucwtvkajrpazgbbst","beizsenkmlrqhbthcnglbkkysynbwljyxourgqxhhdbrqjwjbe","oooxxzyydbdjvhyhzvlwwlxbefmwbieadomipfvdmoujusdqnr","kgctiokinrfnnnxnbeetjcaswztgtljyisrbjojachfgbujxmn","aawyoesnjcwqruglyfcnpegnuldlwptcumkiphobxwuxyiwjlf","chmffhayhvjezcmcrrdzmtwfatovtesmeaysnaajwzpzktvkhy","xwniqsgthhyrnaljcsbuljblwhyvinlrhcflqdonygyihcezoy","hddpcgzsiixrorozrifikpweqvdfjlankmcunqajyawnpweqep","beizsenkmlrqhbthcnglbkkysynbwljyxourgqxhhdbrqjwjbe","jzoeisnzvqaucssvezmedymvlvlivkuymirmjkaidwrfszmwey","quvrpqrtieoxatfruuininiunzyksoiirytfajdvskovglfyst","fquwwwuqddzzmghlsjkgntrdxcjjdhaturygnwpkqzurwhsnbs","ldimkhaogodsnggnncrlgqjhhrziqlipnpdnalobqtqomhivzb","gedkpyeefquljywyynyyloueewjukvvrflvzbqkslygbjxevln","hddpcgzsiixrorozrifikpweqvdfjlankmcunqajyawnpweqep","chzkqmmgqwtqhdobgiupjqdaxjexhpjssucwtvkajrpazgbbst","quwmjnluvdieyslkkzfvcezbapnpgpdpzeicxnsbxbdjyigogu","xosljdqelacotjmjykzqwfezqyqrzclwaxwnsshxqmfkkbxbsv","holorligkqqbwmuhtdxknbauoaapztgnvzspahmawfnguuxeet","kgctiokinrfnnnxnbeetjcaswztgtljyisrbjojachfgbujxmn","lnsxyyvxwktfrfcnaksfmjcylnuspghtibgobyzbcfndncfqkr","xmmwhwqosxlboizfpjtqtjumqzkfbsqnalpgkhpqlpjyzqbhyn","jurfxnusubbwddfhkixdrtiktmkmdwteemopttiejxvvtdxody","beizsenkmlrqhbthcnglbkkysynbwljyxourgqxhhdbrqjwjbe","uvexttjbcqitczkkfdufmzltnzgrcjkiezbcdgrriehpdbsdno","beizsenkmlrqhbthcnglbkkysynbwljyxourgqxhhdbrqjwjbe","jzoeisnzvqaucssvezmedymvlvlivkuymirmjkaidwrfszmwey","ldnzxsgcpqgiozbbxdjxpgxnlighxtdljbpfjwbbimduusgeam","kgctiokinrfnnnxnbeetjcaswztgtljyisrbjojachfgbujxmn","qciwepmpfsthcshewvuavzditrhuyenwsmaobkvjlzzsunpbok","ozxpozhjxckidlryiuwpozxxzazegqwdpsghqpqsoxurwexgnx","qciwepmpfsthcshewvuavzditrhuyenwsmaobkvjlzzsunpbok","aawyoesnjcwqruglyfcnpegnuldlwptcumkiphobxwuxyiwjlf","kyizgfbeppozaehswgeclpwgomayeujewtkgztdbdzalwfqclm","xmbxnviporjutaxljbfssthsxcagltaltpbvkjaairgauihead","ozxpozhjxckidlryiuwpozxxzazegqwdpsghqpqsoxurwexgnx","uvexttjbcqitczkkfdufmzltnzgrcjkiezbcdgrriehpdbsdno","ptbaikdzpyvjgqttnysohdujpjrkhmvpntmemjrpyewbqanmye","xosljdqelacotjmjykzqwfezqyqrzclwaxwnsshxqmfkkbxbsv","acfztjxiwvceveumejuvzkcpjkrdalaaobwzoystqbreeohirt","eaofhcezozzbrpaecxdccpbvdwvobcrfoizbuqzydburmybxli","wwbonwqbrtuhioyhtzkmqeprjkqzqcfmjxbkigbcsjxtuwfgmv","uwstockselmfmmxukqxjlfzjkkofkglcftenehhahqhjpeyoow"]
,

"qciwepmpfsthcshewvuavzditrhuyenwsmaobkvjlzzsunpbok"
,
5

))
print(a.closetTarget(["a", "a", "a", "a", "a", "a", "a", "d", "a"], "d", 2))