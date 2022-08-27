# 이름, 실적
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2],
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

di = {}
member_aver = []

for i in range(len(member_names)) :
    mem_sum = 0
    for x in range(len(member_records[i])) :
        mem_sum += member_records[i][x]
    aver = mem_sum / len(member_records[i])
    di[member_names[i]] = aver

grading = sorted([(v,k) for k,v in di.items()], reverse=True)

bonus_eligible_persons = grading[:2]
for v,k in grading :
    if v > 5 :
        print(f"보너스 대상자 {k}")

underperformer = grading[-2:]
for v,k in grading :
    if v < 3 :
        print(f"면담 대상자 {k}")
