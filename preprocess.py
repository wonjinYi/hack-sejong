import pandas as pd

def Grouped_10min(df):
    # 시간 및 분 데이터를 기반으로 datetime 생성
    df['Datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])

    # 10분 단위로 그룹화
    df['10MinGroup'] = df['Datetime'].dt.floor('10T')  # '10T'는 10분 단위

    # 그룹화하여 평균 계산
    grouped_data = df.groupby('10MinGroup').mean().reset_index()

    # 반환할 열 이름을 변수로 정의
    columns = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Energy_consumption', 'Temperature', 'Wind', 'CloudCover', 'Precipitation', 'Snowfall']

    # 그룹화한 데이터에서 해당 열 반환
    return grouped_data[columns]


def split_by_weekdays(df):
    # 날짜 열 추가
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    # 요일 계산 (0: 월요일, 6: 일요일)
    df['DayOfWeek'] = df['Date'].dt.dayofweek

    # 평일/토요일/일요일,공휴일로 분류
    def categorize_day(day_of_week):
        if day_of_week < 5:
            return 'Weekday'
        elif day_of_week == 5:
            return 'Saturday'
        else:
            return 'Sunday/Public Holiday'

    df['DayCategory'] = df['DayOfWeek'].apply(categorize_day)

    week_df = df[df['DayCategory'].isin(['Weekday'])]
    sat_df = df[df['DayCategory'].isin(['Saturday'])]
    sun_df = df[df['DayCategory'].isin(['Sunday'])]

    # 반환할 열 이름을 변수로 정의
    columns = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Energy_consumption', 'Temperature', 'Wind', 'CloudCover', 'Precipitation', 'Snowfall']

    return week_df[columns], sat_df[columns], sun_df[columns]