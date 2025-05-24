def make_day(date):
    # 문자열로 받은 날짜를 년, 월, 일로 '.'을 기준으로 분류
    year_str, month_str, day_str = date.split('.') 
    
    year = int(year_str) * 12 * 28
    month = int(month_str) * 28
    day = int(day_str)
    
    return year + month + day  

def solution(today, terms, privacies):
    answer = []
    maked_terms = {} # 조회하기 쉽게 dict로
    
    for t in terms:
        # 약관 종류와 유효기간을 공백을 기준으로 분류
        # n: 약관종류, month: 유효기간
        n, month = t.split() 
        maked_terms[n] = int(month) * 28
        # print(maked_terms)
    
    # 인덱스, 수집일자, 약관종류로 구분해야 하기에 enumerate() 사용
    for idx, p in enumerate(privacies):
        number = idx + 1 # 생성된 인덱스에 + 1
        # 만료기간과 약관 종류를 공백으로 구분, 
        # date: 만료기간, n: 약관 종류
        date, n = p.split() 
        # print(answer, date, n)

        # 오늘날짜보다 만료기간이 짧으면 
        if make_day(today) > make_day(date) + maked_terms[n] -1:
            answer.append(number)    
    
    return answer


today = "2022.05.19"	
terms = ["A 6", "B 12", "C 3"]	
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	

print(solution(today, terms, privacies))