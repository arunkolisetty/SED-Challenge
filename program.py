T=int(input())
for _ in range(T):
    cNum=input()
    merge=''.join(cNum.split('-'))
    if cNum[0] in ['4','5','6']:
        if (len(cNum)==16) or (len(cNum)==19 and cNum.count('-')==3):
            if all([len(each)==4 for each in cNum.split('-')]) or cNum.isdigit():
                if any( merge.count((i*4))>=1 for i in ('0123456789')):
                    pass
                else:
                    print("Valid")
                    continue
    print("Invalid")