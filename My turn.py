User=['흑태자',"엘린","데스","힐다"] # 유저
Team={'흑태자':"red","엘린":"red","데스":"blue","힐다":"blue"} # 팀
Area=["도쿄","뉴욕","서울","파리","런던","싱가포르"] # 지역
Supernova=["supernova1","supernova2","supernova3","supernova4",'supernova5'] # 초신성
Asura=["asura1","asura2","asura3"] # 아수라
Grima=['grima'] # 그리마
Open=['grima'] # 개방

Money={'흑태자':100000,"엘린":200000,"데스":300000,"힐다":400000} # 자산
Toll={"도쿄":100,"뉴욕":200,"서울":300,"파리":400,"런던":500,"싱가포르":600} # 통행료

Owner={"도쿄":'흑태자',"뉴욕":"엘린","서울":'흑태자',"파리":"데스","런던":"힐다","싱가포르":'흑태자',
       "supernova1":'흑태자',"supernova2":'흑태자',"supernova3":'흑태자',"supernova4":'흑태자',
       "asura1":'흑태자',"asura2":'흑태자',"asura3":'흑태자',"supernova5":'흑태자','grima':'흑태자'} # 주인
Unit={"도쿄":['도쿄'],"뉴욕":['뉴욕','엘린'],"서울":['서울','흑태자'],
      "파리":['파리','데스'],"런던":['런던','힐다'],"싱가포르":['싱가포르']} # 유닛

def Arrive(x,y): # 도착
    if x in User: # 도착 주체는 유저
        if y in Area: # 지역에 도착
            print(f"{x}이(가) {y}에 도착")
            if x=='흑태자':
                for user in User:
                    if Team[x]!=Team[user] and not any(Owner[grima]==user and grima in Open for grima in Grima):
                        Steal(x,Toll[y],user)
            if Team[x]!=Team[Owner[y]]:
                Pay(x,Toll[y],Owner[y])
            if x=='흑태자':
                area=input("초신성을 생성할 지역을 선택하세요:")
                if area in Area:
                    for supernova in Supernova:
                        if Owner[supernova]==x and not any(supernova in Unit[area2] for area2 in Area):
                            Generate(x,supernova,area)
                            break
            for supernova in Supernova:
                if any(supernova in Unit[area] and y!=area for area in Area) and Team[Owner[supernova]]!=Team[x]:
                    if any(supernova in Unit[area] and x not in Unit[area] for area in Area) and not any(Owner[grima]==x and grima in Open for grima in Grima):
                        Draw(Owner[supernova],x,supernova)
            for asura in Asura:
                if any(asura in Unit[area] and y!=area for area in Area) and Owner[asura]==x:
                    Move(x,asura)
                    for user in User:
                        if Team[x]!=Team[user] and not any(Owner[grima]==user and grima in Open for grima in Grima):
                            Call(x,user,asura)
        elif y in Asura: # 아수라에 도착
            print(f"{x}이(가) {y}에 도착")
            if x==Owner[y]:
                for user in User:
                    if Team[x]!=Team[user] and not any(Owner[grima]==user and grima in Open for grima in Grima):
                        Call(x,user,y)
            elif Team[x]!=Team[Owner[y]]:
                Pay(x,sum(Toll[area] for area in Area),Owner[y])
        elif y in Supernova: # 초신성에 도착
            print(f"{x}이(가) {y}에 도착")
            if Team[x]!=Team[Owner[y]]:
                Pay(x,sum(Toll[area] for area in Area),Owner[y])
        elif y in User and x!=y: # 유저에게 도착
            print(f"{x}이(가) {y}에게 도착")
            if any(Owner[grima]==x and grima in Open for grima in Grima) and not any(Owner[grima]==y and grima in Open for grima in Grima):
                Call(x,y,x)
            elif any(Owner[grima]==y and grima in Open for grima in Grima):
                Pay(x,sum(Toll[area] for area in Area),y)

def Generate(x,y,z): # 생성
    if x in User and z in Area:
        print(f"{x}이(가) {y}을(를) {z}에 생성")
        if y in Asura: # 아수라 생성
            for asura in Asura:
                if any(asura in Unit[area] and z!=area for area in Area) and Owner[asura]==Owner[y]:
                    for area in Area:
                        if asura in Unit[area]:
                            Unit[area].remove(asura)
            for asura in Asura:
                if asura in Unit[z] and Team[Owner[asura]]!=Team[Owner[y]]:
                    for area in Area:
                        if asura in Unit[area]:
                            Unit[area].remove(asura)
            for supernova in Supernova:
                if any(supernova in Unit[area] and z!=area for area in Area) and Team[Owner[supernova]]!=Team[Owner[y]]:
                    for area in Area:
                        if supernova in Unit[area]:
                            Unit[area].remove(supernova)
            Unit[z].append(y)
            if Owner[y]!=Owner[z]:
                Acquire(Owner[y],z)
            Move(Owner[y],y)
            for user in User:
                    if Team[Owner[y]]!=Team[user] and not any(Owner[grima]==user and grima in Open for grima in Grima):
                        Call(Owner[y],user,y)
        elif y in Supernova: # 초신성 생성
            for asura in Asura:
                if any(asura in Unit[area] and z!=area for area in Area) and Team[Owner[asura]]!=Team[Owner[y]]:
                    for area in Area:
                        if asura in Unit[area]:
                            Unit[area].remove(asura)
            for supernova in Supernova:
                if any(supernova in Unit[area] and z!=area for area in Area) and any(Team[Owner[y]]!=Team[user] and Team[user]!=Team[Owner[supernova]] for user in User):
                    for area in Area:
                        if supernova in Unit[area]:
                            Unit[area].remove(supernova)
            Unit[z].append(y)
            if Owner[y]!=Owner[z]:
                Acquire(Owner[y],z)
            for user in User:
                    if (Team[Owner[y]]!=Team[user] and not any(user in Unit[area] and y in Unit[area] for area in Area)
                        and not any(Owner[grima]==user and grima in Open for grima in Grima)):
                        Draw(Owner[y],user,y)
            
def Steal(x,y,z): # 강탈
    if x in User and z in User:
        print(f"{x}이(가) {y}원을 {z}(으)로부터 강탈")
        Money[x]+=y
        Money[z]-=y
        print(f"{x}: {Money[x]}원, {z}: {Money[z]}원")

def Pay(x,y,z): # 지불
    if x in User and z in User:
        print(f"{x}이(가) {y}원을 {z}에게 지불")
        Money[x]-=y
        Money[z]+=y
        print(f"{x}: {Money[x]}원, {z}: {Money[z]}원")

def Draw(x,y,z): # 끌어당김
    if x in User and y in User:
        if z in User:
            print(f"{x}이(가) {y}을(를) {z}에게 끌어당김")
        else:
            print(f"{x}이(가) {y}을(를) {z}(으)로 끌어당김")
        Walk(y,z)
            

def Call(x,y,z): # 호출
    if x in User and y in User:
        if z in User:
            print(f"{x}이(가) {y}을(를) {z}에게 호출")
        else:
            print(f"{x}이(가) {y}을(를) {z}(으)로 호출")
        Move(y,z)

def Move(x,y): # 이동
    if x in User:
        if y in User:
            print(f"{x}이(가) {y}에게 이동")
        else:
            print(f"{x}이(가) {y}(으)로 이동")
        for area in Area:
            if x in Unit[area]:
                Unit[area].remove(x)
        for area in Area:
            if y in Unit[area]:
                Unit[area].append(x)
                unit=Unit[area]
        for i in range(unit.index(x)-1,-1,-1):
            Arrive(x,unit[i])

def Walk(x,y): # 보행
    if x in User:
        if y in User:
            print(f"{x}이(가) {y}에게 이동")
        else:
            print(f"{x}이(가) {y}(으)로 이동")
        for area in Area:
            if x in Unit[area]:
                Unit[area].remove(x)
        for area in Area:
            if y in Unit[area]:
                Unit[area].append(x)
                unit=Unit[area]
        for i in range(unit.index(x)-1,-1,-1):
            Arrive(x,unit[i])
        
def Acquire(x,y): # 획득
    if x in User:
        print(f"{x}이(가) {y}을(를) 획득")
        Owner[y]=x

# 주사위 턴 시작

area=input("아수라를 생성할 지역을 선택하세요:")
if area in Area:
    for asura in Asura:
        if Owner[asura]=='흑태자' and not any(asura in Unit[area2] for area2 in Area):
            Generate('흑태자',asura,area)
            break
            
area=input("이동할 지역을 선택하세요:")
if area in Area:
    Walk('흑태자',area)

for user in User:
    if Team['흑태자']!=Team[user] and not any(Owner[grima]==user and grima in Open for grima in Grima):
        Steal('흑태자',sum(Toll[area] for area in Area),user)

