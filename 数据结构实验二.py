import time
def bf(s,t):
    slen,tlen=len(s),len(t)
    i,j= 0,0
    while i<slen and j<tlen:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j == tlen:
        return i-j
    else:
        return -1

def next(t):
    j,k,tlen= 0,-1,len(t)
    pnext = [-1]*tlen
    while j < tlen - 1:
        if k == -1 or t[j] == t[k]:
            pnext[j+1] = k + 1
            j,k = j + 1,k + 1
        else:
            k =pnext[k]
    return pnext

def kmp(s,t,pnext):
    i,j = 0,0
    slen,tlen = len(s),len(t)
    while i<slen and j<tlen:
        if j == -1 or s[i] == t[j]:
            i,j = i+1,j+1
        else:
            j = pnext[j]
    if j == tlen:
        return i-j
    else:
        return -1

# 病毒DNA列表
virus_dna_list = [
    "aba", "aba", "aabb", "aabb", "abcd",
    "abcd", "abcde", "acc", "abcaby", "abcaby"
]

# 疑似患者DNA列表
possibility_dna_list = [
    "bcbaabbaba", "aaabbbbba", "abceaabb", "abaabcea",
    "cdabbbab", "cabbbbab", "bcdedbda", "bdedbcda",
    "abcabcababbaabcabybc", "abcabcabaababcabcabc"
]

#BF方法遍历
start_time = time.perf_counter() #计时开始！！！

for i in range(len(virus_dna_list)):
    virus_dna = virus_dna_list[i]
    possibility_dna = possibility_dna_list[i]
    bf_result = bf(possibility_dna, virus_dna)  # 逐个遍历
    if bf_result != -1:
        print(f"BF算法：第{i+1}个患者感染了病毒，匹配位置: {bf_result + 1}")
    else:
        print(f"BF算法：第{i+1}个患者未感染病毒")

end_time = time.perf_counter()
print(f"BF算法总运行时间: {end_time - start_time:.10f} 秒")


#kmp方法遍历
start_time = time.perf_counter()

for i in range(len(virus_dna_list)):
    virus_dna = virus_dna_list[i]
    possibility_dna = possibility_dna_list[i]

    pnext = next(virus_dna)  # 为每个病毒DNA生成pnext表！

    kmp_result = kmp(possibility_dna, virus_dna, pnext)  # 逐一匹配
    if kmp_result != -1:
        print(f"KMP算法：第{i+1}个患者感染了病毒，匹配位置: {kmp_result + 1}")
    else:
        print(f"KMP算法：第{i+1}个患者未感染病毒")

end_time = time.perf_counter()
print(f"KMP算法总运行时间: {end_time - start_time:.10f} 秒")

