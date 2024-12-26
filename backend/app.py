import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timedelta
from pyngrok import ngrok
import time
from threading import Thread

app = Flask(__name__)
CORS(app)


power_data = pd.DataFrame()
cur = 0
power_status = False

def load_power_data(file_path):
    global power_data
    try:
        df = pd.read_csv(file_path)
         # timestamp 열 생성
        df['timestamp'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])
        # 필요한 열만 추출: timestamp와 Energy_co
        power_data = df[['timestamp', 'Energy_consumption']].rename(columns={'Energy_consumption': 'value'})
        
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        power_data = pd.DataFrame(columns=['timestamp', 'value'])  # 빈 DataFrame

# CSV 파일에서 데이터 로드
load_power_data("2010_data.csv")

def cur_update():
    global cur
    while True:
        time.sleep(5)
        cur += 1
        cur = min(cur, len(power_data) - 1)
        
        
cur_thread = Thread(target = cur_update, daemon = True)
cur_thread.start()


@app.route('/power', methods=['GET'])
def get_power():
    global power_data, cur

    try:
        start = int(request.args.get('start', 0))
    except ValueError:
        return jsonify({"error": "Invalid 'start' parameter. Must be an integer."}), 400

    if power_data.empty:
        return jsonify({"error": "No data available in power_data."}), 500

    if start < 0 or start > cur:
        return jsonify({"error": f"'start' must be between 0 and {cur}."}), 400

    # DataFrame 슬라이싱
    sliced_data = power_data.iloc[start:cur + 1].copy()

    # ISO-8601 형식으로 변환
    sliced_data['timestamp'] = sliced_data['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')

    # JSON 직렬화를 위해 to_dict 사용
    sliced_data_list = sliced_data.to_dict(orient='records')
    
    # JSON 응답 생성
    response = {
        "start": start,
        "end": cur,
        "data": sliced_data_list,
    }
    return jsonify(response)


@app.route('/power/status', methods=['POST'])
def update_power_status():
    global power_status
    
    data = request.get_json()
    
    # JSON 데이터 유효성 확인
    if not data or 'power_status' not in data:
        return jsonify({"error": "Invalid request. 'power_status' is required."}), 400

    # 요청 값 가져오기
    try:
        new_status = bool(data['power_status'])  # Boolean 값으로 변환
    except ValueError:
        return jsonify({"error": "'power_status' must be a boolean."}), 400

    # 서버 상태 업데이트
    power_status = new_status

    # 업데이트된 상태 반환
    return jsonify({"power_status": power_status}), 200


users = {
    "20011734": {"count": 10},
    "19015486": {"count": 5},
}

@app.route('/user', methods=['POST'])
def authenticate_user():
    """
    유저 인증 요청 처리.
    """
    # 요청 데이터 가져오기
    data = request.get_json()
    if not data or "id" not in data:
        return jsonify({"error": "Invalid request. 'id' is required."}), 400

    user_id = data["id"]

    # 유저 존재 여부 확인
    if user_id not in users:
        return jsonify({"error": f"User with id {user_id} not found."}), 404

    # 봉사 인정 여부 판단
    recognition_result = True

    if recognition_result:
        # 인정되면 카운트 증가
        users[user_id]["count"] += 1

    # 응답 생성
    response = {
        "id": user_id,
        "count": users[user_id]["count"],
        "result": recognition_result
    }
    return jsonify(response), 200


@app.route('/')
def home():
    return "Hello, Flask with ngrok!"

if __name__ == '__main__':
    # ngrok 터널 생성
    public_url = ngrok.connect(5000)
    print(f" * ngrok tunnel available at: {public_url}")

    # Flask 애플리케이션 실행
    app.run(port=5000)
