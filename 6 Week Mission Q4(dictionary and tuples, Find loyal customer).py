# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
sort = "아이디,나이,전화번호,성별,지역,구매횟수"

info_list = info.split(",")
sort_list = sort.split(",")

id = [info_list[v] for v in range(0,len(info_list), 6)]
age = [info_list[v+1] for v in range(0,len(info_list), 6)]
phone_number = ["000-0000-0000" if info_list[v+2] == "x" else info_list[v+2] for v in range(0,len(info_list), 6)]
gender = [info_list[v+3] for v in range(0,len(info_list), 6)]
area = [info_list[v+4] for v in range(0,len(info_list), 6)]
purchace = [info_list[v+5] for v in range(0,len(info_list), 6)]

after_sorting = [id, age, phone_number, gender, area, purchace]
di = {}
for n in range(len(after_sorting)):
    di[sort_list[n]] = after_sorting[n]
print(di)

list_customer = [info_list[v:v+6] for v in range(0, len(info_list), 6)]
for x in list_customer :
    if int(x[5]) > 8 :
        if x[2].startswith("010") :
            print(f"할인 쿠폰을 받을 회원정보 아이디:{x[0]}, 나이:{x[1]}, 전화번호:{x[2]}, 성별:{x[3]}, 지역:{x[4]}, 구매횟수: {x[5]}")
