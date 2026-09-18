with open('img_b64.txt') as f:
    b64 = f.read().strip()

html = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Registro de Encuesta</title>
<style>
  :root {
    --azul: #05339C;
    --dorado: #E5C95F;
    --blanco: #FFFFFF;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: 'Segoe UI', Arial, sans-serif;
    background: var(--azul);
    color: var(--blanco);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }
  .card {
    background: var(--blanco);
    color: var(--azul);
    max-width: 420px;
    width: 100%;
    border-radius: 12px;
    padding: 30px 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    text-align: center;
  }
  h1 {
    color: var(--azul);
    font-size: 22px;
    margin-bottom: 5px;
  }
  p.sub {
    color: #555;
    font-size: 14px;
    margin-top: 0;
    margin-bottom: 20px;
  }
  label {
    display: block;
    text-align: left;
    font-size: 14px;
    font-weight: 600;
    margin: 12px 0 5px;
    color: var(--azul);
  }
  input {
    width: 100%;
    padding: 10px 12px;
    border: 2px solid var(--dorado);
    border-radius: 6px;
    font-size: 15px;
    outline: none;
  }
  input:focus {
    border-color: var(--azul);
  }
  button {
    margin-top: 22px;
    width: 100%;
    padding: 13px;
    background: var(--dorado);
    color: var(--azul);
    border: none;
    border-radius: 6px;
    font-size: 16px;
    font-weight: 700;
    cursor: pointer;
  }
  button:hover { opacity: 0.9; }

  /* Loading screen */
  #loading {
    display: none;
    text-align: center;
  }
  .spinner {
    margin: 0 auto 20px;
    width: 55px;
    height: 55px;
    border: 6px solid var(--dorado);
    border-top: 6px solid var(--azul);
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }
  @keyframes spin { 100% { transform: rotate(360deg); } }
  .warning {
    background: #FFF4D6;
    border: 2px solid var(--dorado);
    border-radius: 8px;
    padding: 12px;
    font-size: 13px;
    font-weight: 700;
    color: var(--azul);
    margin-top: 15px;
  }
  #timer {
    font-size: 26px;
    font-weight: 700;
    color: var(--azul);
    margin: 10px 0;
  }

  /* Result screen */
  #result {
    display: none;
    text-align: center;
  }
  #result img {
    width: 100%;
    border-radius: 10px;
    margin-top: 10px;
  }
</style>
</head>
<body>

<div class="card" id="formCard">
  <img src="1789762050075_image.png">
  <h1>Registro de Encuesta</h1>
  <p class="sub">Complete sus datos personales</p>
  <form id="regForm">
    <label>Nombre</label>
    <input type="text" required>
    <label>Apellido</label>
    <input type="text" required>
    <label>Sección</label>
    <input type="text" required>
    <label>Edad</label>
    <input type="number" min="1" required>
    <label>Cédula</label>
    <input type="text" required>
    <label>Correo estudiantil</label>
    <input type="email" required>
    <button type="submit">Enviar</button>
  </form>
</div>

<div class="card" id="loading">
  <div class="spinner"></div>
  <p>Procesando su registro...</p>
  <div id="timer">15:00</div>
  <div class="warning">⚠️ IMPORTANTE: no cerrar esta ventana. Su registro está siendo procesado.</div>
</div>

<div class="card" id="result">
  <h1>Registro completado</h1>
  <img src="data:image/png;base64,__IMG_B64__" alt="resultado">
</div>

<script>
document.getElementById('regForm').addEventListener('submit', function(e) {
  e.preventDefault();
  document.getElementById('formCard').style.display = 'none';
  document.getElementById('loading').style.display = 'block';

  var totalSeconds = 6 * 60;
  var timerEl = document.getElementById('timer');

  var interval = setInterval(function() {
    totalSeconds--;
    var m = Math.floor(totalSeconds / 60);
    var s = totalSeconds % 60;
    timerEl.textContent = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
    if (totalSeconds <= 0) {
      clearInterval(interval);
      document.getElementById('loading').style.display = 'none';
      document.getElementById('result').style.display = 'block';
    }
  }, 1000);
});
</script>

</body>
</html>
"""

html = html.replace("__IMG_B64__", b64)

with open('/mnt/user-data/outputs/registro.html', 'w') as f:
    f.write(html)

print("done", len(html))
