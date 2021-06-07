from flask import Flask, render_template
from flask_mail import Mail, Message
import webbrowser
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
mail = Mail(app)
"""
# DBの接続の設定
engine = create_engine('sqlite:///user.db', echo=True)

# DBのモデルを作成する
bs = declarative_base()


# DBを作成(今回は、userの情報を入れる。numberを入れないとerrorになるので注意)
class User(bs):
    __tablename__ = "user_information"
    number = Column(Integer, primary_key=True, unique=True)
    id = Column(String)
    old_password = Column(String)
    new_password = Column(String)

    # DBの情報について確認
    def __repr__(self):
        return "Users<id:{},old_password:{},new_password:{}>".format(self.id, self.old_password, self.new_password)


bs.metadata.create_all(engine)

session_maker = sessionmaker(bind=engine)

session = session_maker()
"""
# gmailの設定
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['NAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = ''  # 送信者 <=セキュリティレベルを低くする必要あり
app.config['MAIL_PASSWORD'] = ''
mail = Mail(app)


#スタート画面
@app.route("/")
def index():
    return render_template('start.html')


#Gmailが届く画面
@app.route('/mail', methods=['POST'])
def send_mail():
    msg = Message('不正ログインについて',
                  sender='',  # 送信者
                  recipients=[''])  # 受信者
    msg.html = render_template('mail.html')
    mail.send(msg)
    url = ""#メールの受信ボックスのurl
    webbrowser.open(url)
    return "メール送信中"


#入力画面
@app.route('/signin')
def sign():
    return render_template('sign.html')


#完了画面
@app.route('/login', methods=['POST'])
def login():
    return render_template('end.html')

#メイン文
if __name__ == '__main__':
    app.run(debug=True)
