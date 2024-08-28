from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ecoffee_database_setup import Base, Post

app = Flask(__name__)

# 데이터베이스 설정
engine = create_engine('mysql+pymysql://root:1108@localhost/ecoffee_db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()

@app.route('/mypage', methods=['GET', 'POST'])
def mypage():
    # 하드코딩된 사용자 포인트 예제
    current_points = 1000  # 실제 구현 시 동적 포인트 로직을 추가해야 함

    if request.method == 'POST':
        if 'profile_picture' in request.files:
            profile_picture = request.files['profile_picture']
            if profile_picture.filename != '':
                # 파일을 static/uploads 디렉토리에 저장
                profile_picture.save(f"{app.static_folder}/uploads/myuser.jpg")
                flash('프로필 사진이 성공적으로 변경되었습니다.')
        return redirect(url_for('mypage'))

    return render_template('mypage.html', current_points=current_points)

@app.route('/', methods=['GET'])
def main():
    # 홈 페이지에서 메인 페이지로 리다이렉트
    return redirect(url_for('mypage'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)  # 로컬 서버 실행
