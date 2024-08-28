# from flask import Flask, jsonify, redirect, render_template, request, url_for
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from ecoffee_database_setup import Base, Post

# app = Flask(__name__)

# engine = create_engine('mysql+pymysql://root:1108@localhost/ecoffee_db')

# Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
# session = DBSession()


# @app.route('/')
# def post():
#     post = session.query(Post).all()
#     return render_template('main.html', post=post)


# @app.route('/<string:location>')
# def goToLocation(location):
#     post = session.query(Post).filter(Post.location==location)
#     return render_template('main.html', post=post)


# @app.route('/<string:post_id>',
#            methods=['POST'])
# def likeAction(post_id):
#     thisPost = session.query(Post).filter_by(post_id=post_id).one()
#     if request.method == 'POST':
#         if thisPost.like_count==0:
#             thisPost.like_count = 1
#         elif thisPost.like_count==1:
#             thisPost.like_count = 0
#         session.add(thisPost)
#         session.commit()
#         return redirect(request.referrer)


# if __name__ == '__main__':
#     app.debug = True
#     app.run(host='127.0.0.1', port=5000)

from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ecoffee_database_setup import Base, Post

app = Flask(__name__)

# 데이터베이스 설정
engine = create_engine('mysql+pymysql://root:1108@localhost/ecoffee_db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()

@app.route('/')
def index():
    # 사용자 포인트를 조회 (예: 첫 번째 사용자의 포인트)
    # 이 부분은 실제 사용자 인증을 구현할 때 수정되어야 합니다.
    current_points = 1000  # 하드코딩된 포인트

    return render_template('main.html', current_points=current_points)

@app.route('/mypage', methods=['POST'])
def move_to_mypage():
    return redirect(url_for('mypage'))

@app.route('/pointstore', methods=['POST'])
def move_to_pointstore():
    return redirect(url_for('point_store'))

@app.route('/startmachine', methods=['POST'])
def start_machine():
    flash("기계가 동작합니다")  # 버튼 클릭 시 나타나는 메시지
    return redirect(url_for('index'))

@app.route('/pointstore')
def point_store():
    return "포인트 상점 페이지 (구현 필요)"

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)


