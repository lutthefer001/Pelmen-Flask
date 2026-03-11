<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PUBG Mobile - UC & Skin Shop</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary: #f39c12; /* PUBG sarg'ish rangi */
            --dark: #121212;
            --card-bg: #1e1e1e;
            --text: #ffffff;
        }

        body {
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--dark);
            color: var(--text);
        }

        header {
            background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&q=80&w=1000');
            background-size: cover;
            height: 400px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            border-bottom: 4px solid var(--primary);
        }

        .logo h1 {
            font-size: 3rem;
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 5px;
            margin: 0;
        }

        .container {
            width: 90%;
            max-width: 1200px;
            margin: 50px auto;
        }

        h2 {
            border-left: 5px solid var(--primary);
            padding-left: 15px;
            text-transform: uppercase;
            margin-bottom: 30px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        /* Card Style */
        .card {
            background-color: var(--card-bg);
            border-radius: 10px;
            overflow: hidden;
            transition: transform 0.3s;
            border: 1px solid #333;
            text-align: center;
            padding-bottom: 20px;
        }

        .card:hover {
            transform: translateY(-10px);
            border-color: var(--primary);
        }

        .card img {
            width: 100%;
            height: 180px;
            object-fit: cover;
        }

        .price {
            font-size: 1.5rem;
            color: var(--primary);
            font-weight: bold;
            margin: 15px 0;
        }

        .buy-btn {
            background-color: var(--primary);
            color: black;
            border: none;
            padding: 10px 25px;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            text-transform: uppercase;
        }

        .buy-btn:hover {
            background-color: #e67e22;
        }

        .uc-icon {
            color: #ffd700;
            margin-right: 5px;
        }
    </style>
</head>
<body>

<header>
    <div class="logo">
        <h1>PUBG DONATE CENTER</h1>
    </div>
    <p>Arzon va xavfsiz UC hamda Eksklyuziv Qurollar!</p>
</header>

<div class="container">
    
    <h2><i class="fas fa-coins uc-icon"></i> UC Paketlari</h2>
    <div class="grid">
        <div class="card">
            <div style="padding: 20px;">
                <h3>60 UC</h3>
                <p class="price">12,000 UZS</p>
                <button class="buy-btn" onclick="order('60 UC')">Sotib olish</button>
            </div>
        </div>
        <div class="card">
            <div style="padding: 20px;">
                <h3>325 UC</h3>
                <p class="price">55,000 UZS</p>
                <button class="buy-btn" onclick="order('325 UC')">Sotib olish</button>
            </div>
        </div>
        <div class="card">
            <div style="padding: 20px;">
                <h3>660 UC</h3>
                <p class="price">105,000 UZS</p>
                <button class="buy-btn" onclick="order('660 UC')">Sotib olish</button>
            </div>
        </div>
    </div>

    <br><br>

    <h2><i class="fas fa-gun"></i> Top Qurollar (Skins)</h2>
    <div class="grid">
        <div class="card">
            <img src="https://images.unsplash.com/photo-1595231712325-9feda07d43f3?q=80&w=400" alt="M416">
            <h3>M416 - Glacier</h3>
            <p class="price">2,500,000 UZS</p>
            <button class="buy-btn" onclick="order('M416 Glacier')">Sotib olish</button>
        </div>
        <div class="card">
            <img src="https://images.unsplash.com/photo-1584036561566-baf8f5f1b144?q=80&w=400" alt="AKM">
            <h3>AKM - Hellfire</h3>
            <p class="price">1,800,000 UZS</p>
            <button class="buy-btn" onclick="order('AKM Hellfire')">Sotib olish</button>
        </div>
        <div class="card">
            <img src="https://images.unsplash.com/photo-1628113310821-93426589a631?q=80&w=400" alt="AWM">
            <h3>AWM - Mauve Avenger</h3>
            <p class="price">3,200,000 UZS</p>
            <button class="buy-btn" onclick="order('AWM Mauve')">Sotib olish</button>
        </div>
    </div>

</div>
<script>
    function sendToTelegram() {
        const id = document.getElementById('pubgId').value;
        if (!id) { alert("ID kiriting!"); return; }

        fetch('/order', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                product: currentProduct,
                price: currentPrice,
                pubg_id: id
            })
        })
        .then(res => res.json())
        .then(data => {
            if(data.status === "success") {
                alert("Buyurtma qabul qilindi!");
                closeModal();
            } else {
                alert("Xatolik: " + data.msg);
            }
        });
    }
</script>
</script>

</body>
</html>

