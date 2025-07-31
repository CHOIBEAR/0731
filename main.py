#=========================================1교시=============================================

# import pandas as pd

# # data=pd.Series([1,2,3,4],["행1","행2","행3","행4"])

# # print (data.loc ["행1":"행3"]) # 라벨 기준으로 범위를 찾아 출력하기 슬라이싱과 매우 유사함.
# # print (data.loc ["행1":"행3"].drop("행3"))#.drop 을 이용해서 지정 라벨을 빼고 출력

# arr=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# idx = ["행1","행2","행3"]
# col = ["열1","열2","열3"]

# data1 = pd.DataFrame(arr,idx,col) # data=arr 이런식으로도 넣는게 가능.
# data2 = pd.DataFrame(arr[1:],idx[1:],col) #index 부분도 슬라이싱이 가능.

# # print(data1)
# # print(data2)

# print(data1+data2) #데이터 프레임 + 데이터 프레임 은 위치에 맞는 값끼리 더해진다.
#                      #없는 값이 더해지면 NaN으로 바뀐다.
# data3=data1+data2

# s=pd.Series() #빈 객체를 만들오 전부 NaN이 나오게 유도
# print(data3+s)
# ==========================================2교시=============================================
# import pandas as pd
# a1 = [60, 84, 80, 70, 19]
# a2 = [77, 62, 95, 85, 17]
# a3 = [61, 97, 72, 67, 15]
# a4 = [75, 65, 95, 51, 18]
# cols = ["국어", "영어", "수학", "과학", "나이"]
# idx = ["A","B","C","D"]
# data = pd.DataFrame([a1, a2, a3, a4], index=idx, columns=cols)
#ascending 어센딩. 오름 차순. 여기에 false를 하면 내림차순.
# print(data)
# print(data.sort_values("영어",ascending=True)) # 트루일경우 올림차순, 폴스일 경우 내림차순
#            #ㄴ정렬 함수.        #ㄴ인수를 활용하여 올림인지 내림인지 정하는것이가능.
# print(data.sort_values(by=["영어","수학"],ascending=[0,1]))
                                            #ㄴ인수에 ture false 대신 0,1을 사용해서 오름내림을 결정
#print(data.sort_values(by=["수학","영어"],ascending=[0,1]))

#q1 위의 성적표에서 수학 점수가 동률인것만출력하시오.
#수학점수를 정렬하는것이 우선.
# d1= data["수학"].sort_values(ascending=False) #false로 내림차순 정렬.
# cnt=d1.value_counts()
# print 
# print(cnt[cnt>1])
# print(cnt[cnt>1].index[0])
# print(d1[d1==cnt[cnt>1].index[0]])
# ==================================================3교시=============================================================
import pandas as pd
data = pd.read_csv('./data1_20220731.csv',index_col=0)
print(data)

#문제1 위의 인구수 표에서 '세대수'가 가장 높은 농명은 무엇인가?
d1= data ["세대수"].sort_values(ascending=0)
print(d1.index[0])
#문제2 위의 인구수 표에서 '남(65세이상)'인구수가 가장 높은 농명은 무엇인가?
d2= data ["남(65세이상)"].sort_values(ascending=0)
print(d2.index[0])

#문제3 위의 인구수 표에서 '세대수'의 평균 이상의 인구수를 보유한 동명은?
평균값=data['세대수'].mean().astype(int)
print(평균값)
print(data['세대수']>=평균값)
print(data[data['세대수']>=평균값])
print(data[data['세대수']>=평균값].index)
#위가 내 문제 풀이

# #아래가 선생님 풀이
# import pandas as pd
# data = pd.read_csv('./data1_20220731.csv')

# # #문제1 위의 인구수 표에서 '세대수'가 가장 높은 농명은 무엇인가?
# d1 = data.sort_values(by='세대수', ascending=False)
# print("Q2", d1.iloc[0].loc['동명'])

# # #문제2 위의 인구수 표에서 '남(65세이상)'인구수가 가장 높은 농명은 무엇인가?
# d2 = data.sort_values(by='남(65세이상)', ascending=False)
# print("Q3", d2.iloc[0].loc['동명'])

# # #문제3 위의 인구수 표에서 '세대수'의 평균 이상의 인구수를 보유한 동명은?
# 평균값 = data['세대수'].mean().astype(int)
# d3 = data[data['세대수'] > 평균값]
# print("Q4", d3['동명'])

