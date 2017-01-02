import csv
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://finviz.com/screener.ashx?v=152&t=ACCO,ATVI,AEL,AMH,AMKR,ANGO,AXE,ARRS,ASNA,ASCMA,AT,ABY,BLX,BV,BHE,BBG,BSTC,CBT,CSII,CECE,CNP,CHMG,CFG,CLNE,CNO,COMM,CNMD,CPS,CRD/B,CRY,CW,DHR,DAR,DCI,DEI,EWBC,KODK,ETN,ECR,EGN,ENS,EQC,EXAC,EXAR,EXTR,FSAM,FBP,FPO,FOR,GEN,GSOL,GEF,HAE,HYH,HSC,HTLF,HRC,HI,HRG,HUN,H,IAC,IDT,SNOW,STAR,JEC,JAKK,KAI,KOP,LUK,LYV,L,CLI,MGLN,MRLN,MGRC,MDU,MEDP,MRK,CASH,MU,MOG/A,MRC,NBR,NANO,NGS,NCR,NEM,NBL,NRF,NUS,ODP,OMN,OPY,OSK,PEBO,PIP,PHH,PJC,PRU,PWR,QDEL,RL,RBC,RMR,SANM,SCHL,SIGI,SBY,SKYW,SM,SPPI,S,SMP,STT,SCMP,SYY,TMHC,TPRE,TMK,TSE,TRNC,TTMI,UTEK,URI,UVV,VNDA,VVI,VIAV,VSH,WMT,WD,WCG,WMAR,WDC&o=-roa&c=1,6,7,8,9,11,13,16,18,20,21,32,35,36,38,40,46,48,62,65')

def getValues(path):
    elems = browser.find_elements_by_xpath(path)
    retCol = []
    for item in elems:
        retCol.append(item.text)

    print(retCol)
    return retCol


def getInitialSite(num): #cols determine what columns are scraped
    table=[]
    for i in range(1, num):
        aCol = []
        pathBase = "//table[3]/tbody/tr[3]/td/div/table/tbody/tr[4]/td/table/tbody/tr/td"
        path = pathBase + "[" + str(i) + "]"
        print(path)

        aCol = getValues(path)

        print(aCol)

        table.append(aCol)

    browser.quit()
    return table

#   print(getInitialSite(20))
data = getInitialSite(20)

formattedTable = []
for j in range(len(data[0])):
    row = []
    for column in data:
        row.append(column[j])
    formattedTable.append(row)

print(formattedTable)

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(formattedTable)
