from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Vercel uchun app obyekti kerak bo'ladi, lokal ishlash uchun esa pastdagi kod ishlaydi
if __name__ == '__main__':
    app.run(debug=True)