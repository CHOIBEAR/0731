# 0731

📘 Pandas 수업 요약 – 오늘의 학습 정리 🧠  
──────────────────────────────────────────────

📍 1교시: Series & DataFrame 기본 연산

✅ Series 슬라이싱 및 삭제  
- `data.loc["행1":"행3"]` : 라벨 기준 슬라이싱 (마지막 포함)  
- `.drop("행3")` : 특정 라벨 제거  

✅ DataFrame 생성 및 연산
data1 = pd.DataFrame(arr, idx, col)  
data2 = pd.DataFrame(arr[1:], idx[1:], col)  
- DataFrame 간 연산: 위치 일치 시 덧셈, 불일치 시 `NaN`  
- 빈 Series(`pd.Series()`) 와 연산 → 전체 `NaN`  

──────────────────────────────────────────────

📍 2교시: 정렬과 조건 필터링

✅ DataFrame 정렬  
data.sort_values(by="열이름", ascending=True/False)  
- 다중 정렬: `by=["열1", "열2"], ascending=[False, True]`  
- 0/1을 True/False 대신 사용 가능  

✅ 조건 문제 예시 – 수학 점수 동점자 찾기  
cnt = data["수학"].value_counts()  
동점_점수 = cnt[cnt > 1].index[0]  
print(data[data["수학"] == 동점_점수])  

──────────────────────────────────────────────

📍 3교시: CSV 데이터 실습 문제

✅ CSV 불러오기  
data = pd.read_csv('./data1_20220731.csv', index_col=0)  

✅ 문제1: 세대수가 가장 많은 동명  
data.sort_values(by='세대수', ascending=False).iloc[0]['동명']  

✅ 문제2: 65세 이상 남성 인구가 가장 많은 동명  
data.sort_values(by='남(65세이상)', ascending=False).iloc[0]['동명']  

✅ 문제3: 평균 세대수 이상인 동명  
평균 = data['세대수'].mean()  
print(data[data['세대수'] >= 평균]['동명'])  

──────────────────────────────────────────────

📌 추가로 꼭 알아둘 개념 정리

🔹 Series vs. DataFrame  
- Series: 1차원 / DataFrame: 2차원  
- `.loc[]`은 라벨, `.iloc[]`은 인덱스 위치  

🔹 슬라이싱 유의사항  
- `loc`은 마지막 포함 / `iloc`은 마지막 미포함  

🔹 연산 시 NaN 주의  
- 서로 다른 구조끼리 연산 시 NaN 발생  
- 해결: `.fillna(0)` 또는 `.add(other, fill_value=0)`  

🔹 값의 개수 세기  
data["열이름"].value_counts()  

🔹 조건 필터링  
data[data["수학"] >= 80]  

🔹 유용한 기본 함수  
data.head(), data.tail(), data.info(), data.describe()  

🔹 평균값 비교  
data[data["세대수"] >= data["세대수"].mean()]  

🔹 데이터 타입 변환  
평균값 = int(data["세대수"].mean())  # 또는 .astype(int)  

📌 DataFrame 요약 함수 개념 정리 📊  
──────────────────────────────────────────────

🔹 `data.describe()`  
- 수치형 데이터의 **요약 통계값(평균, 표준편차, 최솟값 등)** 출력  
- 기본적으로 숫자형 컬럼만 대상으로 동작함

🔹 `data.info()`  
- 전체 DataFrame의 **행 개수, 컬럼 수, 데이터 타입, 누락값 여부** 등을 요약해 보여줌  
- 데이터의 구조 파악에 매우 유용

🔹 `data.head(n)` / `data.tail(n)`  
- `head(n)` : 앞에서 n개의 행 출력  
- `tail(n)` : 뒤에서 n개의 행 출력  
- 기본값은 n = 5



──────────────────────────────────────────────
