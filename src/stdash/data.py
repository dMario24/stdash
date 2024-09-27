import requests
import pandas as pd
import random
import uuid
from datetime import datetime, timedelta

def load_data():
    # url = 'http://43.202.66.118:8077/all'
    url = 'http://43.202.66.118:8077/all'
    try:
        r = requests.get(url)
        d = r.json()
        df = pd.DataFrame(d)
        return df
    except (requests.RequestException, ValueError) as e:
        print(f"Error occurred: {e}. Returning dummy data instead.")
        return generate_random_data(1000)


def generate_random_data(num_rows):
    data = []
    
    # request_time은 2024-01-01 부터 시작
    start_time = datetime(2024, 1, 1, 0, 0, 0)
    
    # 'n01'부터 'n25'까지의 값을 생성
    user_model_choices = [f"n{str(i).zfill(2)}" for i in range(1, 26)]
    
    # 첫 번째 request_time 초기화
    previous_request_time = start_time
    
    for i in range(1, num_rows + 1):
        num = i
        file_name = f"{random.randint(1, 9)}_{random.randint(10000, 99999)}.png"
        label = random.choice(["", "label_a", "label_b"])
        file_path = f"/home/ubuntu/images/n11/{str(uuid.uuid4())}.png"
        
        # request_time은 이전 시간에 랜덤한 분수 추가
        # 0에서 60분 사이의 랜덤 값 생성 (중복 가능성 있음)
        minutes_to_add = random.randint(0, 60)  # 0에서 60분 사이의 랜덤 분
        request_time = previous_request_time + timedelta(minutes=minutes_to_add)
        previous_request_time = request_time  # 이전 시간 업데이트
        
        # 'n01' ~ 'n25' 사이의 랜덤 값 선택
        request_user = random.choice(user_model_choices)
        prediction_model = random.choice(user_model_choices)
        
        prediction_result = random.randint(0, 9)
        
        # prediction_time은 request_time보다 1시간에서 5시간 사이로 증가
        prediction_time = request_time + timedelta(hours=random.uniform(1, 5))
        
        data.append([num, file_name, label, file_path, request_time, request_user, prediction_model, prediction_result, prediction_time])
    
    # 데이터프레임 생성
    df = pd.DataFrame(data, columns=[
        "num", "file_name", "label", "file_path", "request_time", "request_user", 
        "prediction_model", "prediction_result", "prediction_time"
    ])
    
    return df