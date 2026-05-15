import pymysql
import bcrypt

def setup():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',          # ← Change your MySQL password
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with conn.cursor() as cur:
            cur.execute("CREATE DATABASE IF NOT EXISTS face_attendance "
                        "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            cur.execute("USE face_attendance")

            cur.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id            INT AUTO_INCREMENT PRIMARY KEY,
                    name          VARCHAR(100)  NOT NULL,
                    register_no   VARCHAR(20)   UNIQUE NOT NULL,
                    department    VARCHAR(60)   NOT NULL,
                    email         VARCHAR(120)  UNIQUE NOT NULL,
                    password_hash VARCHAR(255)  NOT NULL,
                    face_encodings LONGTEXT,
                    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS attendance (
                    id         INT AUTO_INCREMENT PRIMARY KEY,
                    student_id INT NOT NULL,
                    date       DATE NOT NULL,
                    time       TIME NOT NULL,
                    status     VARCHAR(20) DEFAULT 'Present',
                    latitude   DECIMAL(10,8),
                    longitude  DECIMAL(11,8),
                    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
                    UNIQUE KEY uq_student_date (student_id, date)
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS admins (
                    id            INT AUTO_INCREMENT PRIMARY KEY,
                    username      VARCHAR(50)  UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL
                )
            """)

            pw = bcrypt.hashpw(b'admin123', bcrypt.gensalt()).decode()
            cur.execute("INSERT IGNORE INTO admins (username, password_hash) VALUES ('admin', %s)", (pw,))
            conn.commit()

        print("=" * 45)
        print("  ✅ Database setup complete!")
        print("  Admin username : admin")
        print("  Admin password : admin123")
        print("=" * 45)
    finally:
        conn.close()

if __name__ == '__main__':
    setup()