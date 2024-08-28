DROP DATABASE IF EXISTS ecoffee_db;
CREATE DATABASE ecoffee_db default CHARACTER SET UTF8MB4;
USE ecoffee_db;

-- 사용자 테이블
CREATE TABLE user(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(1000) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    like_post TEXT,
    points INT DEFAULT 1000 -- 사용자 포인트 필드 추가, 기본값은 1000
);

-- 게시글 테이블
CREATE TABLE post (
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    username VARCHAR(20),
    title VARCHAR(80) NOT NULL,
    location VARCHAR(250),
    place VARCHAR(80),
    main_dish VARCHAR(250),
    content VARCHAR(1000),
    like_count INT DEFAULT 0,
    image_exist BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- 커피 기프티콘 테이블 (포인트 상점용)
CREATE TABLE coffee (
    coffee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    point_cost INT NOT NULL, -- 필요한 포인트
    image_url VARCHAR(255) -- 이미지 URL
);

-- 구매 기록 테이블
CREATE TABLE purchase (
    purchase_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    coffee_id INT,
    purchase_date DATETIME DEFAULT CURRENT_TIMESTAMP, -- 구매 일시
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (coffee_id) REFERENCES coffee(coffee_id)
);
