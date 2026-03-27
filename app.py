import streamlit as st

st.set_page_config(page_title="⚽ Haiti Soccer – GlobalInternet.py", layout="centered")

# Sidebar with license & purchase info
with st.sidebar:
    st.markdown("## 🇭🇹 Haiti Soccer Game")
    st.markdown("**A fast‑paced arcade soccer game**")
    st.markdown("---")
    st.markdown("### 📜 License")
    st.markdown("""
    **Proprietary Commercial Software**  
    Copyright © 2025 Gesner Deslandes. All rights reserved.

    This software is **licensed**, not sold.  
    Unauthorized copying, distribution, or resale is prohibited.
    """)
    st.markdown("### 💸 Purchase")
    st.markdown("""
    - **Price:** $19 USD (one‑time license)
    - Payment via **Prisme Transfer** (Digicel Moncash) to:
    📞 **(509) 4738-5663**  
    *Reference: “Soccer Game”*
    - Email confirmation to **deslandes78@gmail.com** with your name.
    - You’ll receive the game code within 24 hours.
    """)
    st.markdown("---")
    st.caption("© 2025 Gesner Deslandes – GlobalInternet.py")

st.title("⚽ Haiti Soccer – Gesner Deslandes & Family")
st.markdown("**Control Haiti's team** – use arrow keys (desktop) or swipe/tap (mobile) to move, shoot, and score from the golden zones!")

# The full HTML of the soccer game (copied from your original code)
game_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>⚽ Haiti Soccer – Gesner Deslandes & Family</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      background: linear-gradient(145deg, #0a3a1a 0%, #05200a 100%);
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: 'Segoe UI', 'Poppins', system-ui, sans-serif;
      padding: 20px;
    }

    .game-wrapper {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100%;
      max-width: 1300px;
      margin: 0 auto;
    }

    .canvas-container {
      background: #0c2a18;
      border-radius: 2rem;
      padding: 12px;
      box-shadow: 0 25px 40px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.1);
      display: flex;
      justify-content: center;
      overflow: visible;
    }

    canvas {
      display: block;
      width: 100%;
      height: auto;
      max-width: 100%;
      background: #2c8c2c;
      border-radius: 1.2rem;
      box-shadow: 0 8px 20px black;
      cursor: pointer;
    }

    .dashboard {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.8rem;
      margin: 1rem 0.5rem 0.8rem;
      width: 100%;
    }

    .score-panel {
      background: #f9e7b3;
      padding: 0.4rem 1.5rem;
      border-radius: 3rem;
      font-weight: bold;
      box-shadow: inset 0 -2px 0 #b97f3a, 0 4px 10px rgba(0,0,0,0.2);
      display: flex;
      gap: 2rem;
    }

    .score-panel div {
      font-size: 1.2rem;
    }

    .score-panel span {
      font-size: 1.8rem;
      font-weight: 800;
      margin-left: 0.5rem;
      color: #c43d0b;
    }

    .timer-box {
      background: #1e2a2f;
      padding: 0.3rem 1.5rem;
      border-radius: 3rem;
      font-weight: bold;
      color: #ffd966;
      font-size: 1.6rem;
      font-family: monospace;
    }

    .controls {
      display: flex;
      gap: 0.8rem;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
    }

    select, button {
      background: #ffcd7e;
      border: none;
      font-size: 0.9rem;
      font-weight: bold;
      padding: 0.5rem 1.2rem;
      border-radius: 2rem;
      cursor: pointer;
      font-family: inherit;
      transition: 0.05s linear;
      box-shadow: 0 3px 0 #a05e1a;
      color: #3b2a1f;
    }

    button:active, select:active {
      transform: translateY(2px);
      box-shadow: 0 1px 0 #a05e1a;
    }

    .pause-btn {
      background: #f4a261;
      box-shadow: 0 3px 0 #b85c1a;
    }

    .message-area {
      text-align: center;
      margin-top: 0.8rem;
      font-weight: bold;
      background: #000000aa;
      backdrop-filter: blur(4px);
      padding: 0.4rem 1rem;
      border-radius: 2rem;
      width: auto;
      color: #fceea7;
      font-size: 0.9rem;
    }

    .footer {
      text-align: center;
      font-size: 0.7rem;
      margin-top: 1rem;
      color: #c6e6b0;
    }

    /* Splash overlay */
    .splash-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle at center, #001033 0%, #000000 100%);
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 1000;
      flex-direction: column;
      animation: fadeOut 0.5s ease-in-out 5s forwards;
    }

    @keyframes fadeOut {
      to {
        opacity: 0;
        visibility: hidden;
      }
    }

    .star {
      position: absolute;
      background-color: white;
      border-radius: 50%;
      animation: twinkle 1.5s infinite alternate;
    }

    @keyframes twinkle {
      0% { opacity: 0.2; transform: scale(0.8); }
      100% { opacity: 1; transform: scale(1.2); }
    }

    .flag-container {
      position: relative;
      animation: floatLeftRight 2s ease-in-out infinite;
      z-index: 2;
    }

    @keyframes floatLeftRight {
      0% { transform: translateX(-15px); }
      50% { transform: translateX(15px); }
      100% { transform: translateX(-15px); }
    }

    .haiti-flag {
      width: 300px;
      height: 200px;
      background: linear-gradient(to bottom, #00209f 50%, #d21034 50%);
      border-radius: 20px;
      box-shadow: 0 0 30px rgba(0,0,0,0.5), 0 0 15px gold;
      position: relative;
    }

    .names {
      margin-top: 30px;
      text-align: center;
      color: #ffd966;
      font-size: 1.3rem;
      font-weight: bold;
      background: rgba(0,0,0,0.6);
      padding: 15px 30px;
      border-radius: 60px;
      backdrop-filter: blur(4px);
      z-index: 2;
    }

    .names p {
      margin: 5px 0;
    }

    .names .owner {
      font-size: 1.6rem;
      color: #ffaa33;
    }

    @media (max-width: 600px) {
      .haiti-flag { width: 200px; height: 133px; }
      .names { font-size: 0.9rem; padding: 10px 20px; }
      .names .owner { font-size: 1.1rem; }
    }
  </style>
</head>
<body>
<div class="splash-overlay" id="splashOverlay"></div>

<div class="game-wrapper">
  <div class="canvas-container">
    <canvas id="gameCanvas"></canvas>
  </div>
  
  <div class="dashboard">
    <div class="score-panel">
      <div>🇭🇹 HAITI <span id="haitiScore">0</span></div>
      <div id="opponentLabel">🇫🇷 FRANCE <span id="opponentScore">0</span></div>
    </div>
    <div class="timer-box">⏱️ <span id="gameTimer">01:30</span></div>
  </div>

  <div class="controls">
    <select id="opponentSelect">
      <option value="France">🇫🇷 France</option>
      <option value="Brazil">🇧🇷 Brazil</option>
      <option value="Argentina">🇦🇷 Argentina</option>
      <option value="Germany">🇩🇪 Germany</option>
      <option value="England">🏴󠁧󠁢󠁥󠁮󠁧󠁿 England</option>
      <option value="Mexico">🇲🇽 Mexico</option>
    </select>
    <button id="startGameBtn">▶ KICK OFF!</button>
    <button id="resetGameBtn">🔄 RESTART</button>
    <button id="pauseBtn" class="pause-btn">⏸️ PAUSE</button>
    <button id="audioBtn">🔊 ENABLE SOUND</button>
  </div>
  <div id="gameMessage" class="message-area">⚡ Choose opponent, press START. Desktop: ARROWS move, ENTER shoot, P to pause | Mobile: SWIPE move, TAP shoot, double-tap pass ⚡</div>
  <div class="footer">🎮 Shoot only from the 3 GOLDEN ZONES. GK catches & clears the area, then throws to teammate.</div>
</div>

<script>
  // ------------------------------- AUDIO -----------------------------
  let audioCtx = null;
  let crowdActive = false;
  let crowdGain = null;
  let crowdSources = [];
  let crowdNodes = [];
  let crowdWaveInterval = null;

  function getCtx() {
    if (!audioCtx) {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    return audioCtx;
  }

  function resumeAudio() {
    const ctx = getCtx();
    if (ctx.state === "suspended") ctx.resume();
  }

  function playTone(freq, duration, vol = 0.5, type = "sine", offset = 0) {
    try {
      const ctx = getCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.type = type;
      osc.frequency.value = freq;
      const t = ctx.currentTime + offset;
      gain.gain.setValueAtTime(vol, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + duration);
      osc.start(t);
      osc.stop(t + duration + 0.05);
    } catch (e) {}
  }

  function playWhistle() { playTone(2000, 0.35, 0.7, "square"); }
  function playCheer() { playTone(440, 0.4, 0.3); playTone(550, 0.3, 0.3, "sine", 0.15); }
  function playGoal() { playTone(880, 0.3, 0.8); playTone(1100, 0.3, 0.8, "sine", 0.2); playTone(1320, 0.6, 0.8, "sine", 0.45); playTone(1760, 0.8, 0.7, "sine", 0.8); }
  function playKick() { playTone(120, 0.1, 0.35, "sawtooth"); playTone(320, 0.08, 0.25, "square", 0.02); }
  function playWhistleShort() { playTone(1500, 0.2, 0.5, "square"); }
  function playCatch() { playTone(300, 0.1, 0.4, "sine"); }

  function playWelcomeFanfare() {
    try {
      const ctx = getCtx();
      const notes = [
        [523, 0.3, 0], [659, 0.3, 0.3], [784, 0.3, 0.6], [1047, 0.5, 0.9],
        [880, 0.25, 1.5], [784, 0.25, 1.8], [659, 0.25, 2.1], [784, 0.5, 2.4],
        [880, 0.3, 3.0], [1047, 0.3, 3.3], [1175, 0.6, 3.7], [1319, 1.2, 4.3]
      ];
      notes.forEach(([f, d, o]) => playTone(f, d, 0.6, "sine", o));
      const harmony = [[261, 0.5, 0], [329, 0.5, 0.5], [392, 0.5, 1.0], [523, 0.5, 1.5], [392, 0.5, 2.0], [440, 0.5, 2.5], [523, 1.0, 3.0], [659, 1.2, 3.5]];
      harmony.forEach(([f, d, o]) => playTone(f, d, 0.3, "triangle", o));
    } catch(e) {}
  }

  function playFanfare() {
    try {
      const ctx = getCtx();
      const melody = [[523,0.3,0],[659,0.3,0.25],[784,0.3,0.5],[1047,0.5,0.75],[880,0.25,1.25],[784,0.25,1.5],[659,0.25,1.75],[784,0.5,2.0],[880,0.25,2.55],[1047,0.25,2.8],[1175,0.5,3.05],[1319,0.9,3.55]];
      melody.forEach(([f,d,o]) => playTone(f,d,0.55,"sine",o));
      const harmony = [[261,0.5,0],[329,0.5,0.5],[392,0.5,1.0],[523,0.5,1.5],[392,0.5,2.0],[440,0.5,2.5],[523,1.0,3.0],[659,1.2,3.5]];
      harmony.forEach(([f,d,o]) => playTone(f,d,0.25,"triangle",o));
      const bass = [[130,0.4,0],[130,0.4,0.5],[164,0.4,1.0],[174,0.4,1.5],[196,0.4,2.0],[220,0.4,2.5],[261,0.8,3.0],[261,1.2,3.8]];
      bass.forEach(([f,d,o]) => playTone(f,d,0.3,"sawtooth",o));
      [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0].forEach((offset) => {
        const gain = ctx.createGain();
        const bufferSize = ctx.sampleRate * 0.08;
        const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) data[i] = (Math.random() * 2 - 1) * (1 - i / bufferSize);
        const src = ctx.createBufferSource();
        src.buffer = buffer;
        const filter = ctx.createBiquadFilter();
        filter.type = "bandpass";
        filter.frequency.value = 1800;
        filter.Q.value = 0.5;
        src.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);
        gain.gain.setValueAtTime(0.18, ctx.currentTime + offset);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + offset + 0.09);
        src.start(ctx.currentTime + offset);
      });
    } catch(e) {}
  }

  // Crowd generation
  function buildCrowdBuffer(ctx, seconds, lowFreq, highFreq, modFreq) {
    const rate = ctx.sampleRate;
    const len = rate * seconds;
    const buffer = ctx.createBuffer(2, len, rate);
    for (let ch = 0; ch < 2; ch++) {
      const data = buffer.getChannelData(ch);
      for (let i = 0; i < len; i++) {
        const t = i / rate;
        let noise = Math.random() * 2 - 1;
        let envelope = 0.6 + 0.25 * Math.sin(2 * Math.PI * modFreq * t);
        envelope += 0.15 * Math.sin(2 * Math.PI * (modFreq * 0.6) * t + 1.2);
        envelope = Math.min(0.9, Math.max(0.3, envelope));
        data[i] = noise * envelope;
      }
    }
    return buffer;
  }

  function startCrowd() {
    if (crowdActive) return;
    try {
      const ctx = getCtx();
      crowdGain = ctx.createGain();
      crowdGain.gain.value = 0;
      
      const lowBuffer = buildCrowdBuffer(ctx, 8, 200, 600, 0.7);
      const lowSrc = ctx.createBufferSource();
      lowSrc.buffer = lowBuffer;
      lowSrc.loop = true;
      const lowFilter = ctx.createBiquadFilter();
      lowFilter.type = "lowpass";
      lowFilter.frequency.value = 400;
      lowFilter.Q.value = 1.2;
      lowSrc.connect(lowFilter);
      lowFilter.connect(crowdGain);
      
      const midBuffer = buildCrowdBuffer(ctx, 8, 600, 1800, 1.2);
      const midSrc = ctx.createBufferSource();
      midSrc.buffer = midBuffer;
      midSrc.loop = true;
      const midFilter = ctx.createBiquadFilter();
      midFilter.type = "bandpass";
      midFilter.frequency.value = 1000;
      midFilter.Q.value = 0.8;
      midSrc.connect(midFilter);
      midFilter.connect(crowdGain);
      
      const highBuffer = buildCrowdBuffer(ctx, 8, 1800, 3000, 1.8);
      const highSrc = ctx.createBufferSource();
      highSrc.buffer = highBuffer;
      highSrc.loop = true;
      const highFilter = ctx.createBiquadFilter();
      highFilter.type = "bandpass";
      highFilter.frequency.value = 2200;
      highFilter.Q.value = 1.5;
      highSrc.connect(highFilter);
      highFilter.connect(crowdGain);
      
      let clapInterval = setInterval(() => {
        if (!crowdActive || !gameRunning || paused) return;
        const clapGain = ctx.createGain();
        const bufferSize = ctx.sampleRate * 0.1;
        const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) data[i] = (Math.random() * 2 - 1) * (1 - i / bufferSize);
        const src = ctx.createBufferSource();
        src.buffer = buffer;
        const filter = ctx.createBiquadFilter();
        filter.type = "bandpass";
        filter.frequency.value = 1800;
        filter.Q.value = 0.5;
        src.connect(filter);
        filter.connect(clapGain);
        clapGain.connect(ctx.destination);
        clapGain.gain.setValueAtTime(0.15, ctx.currentTime);
        clapGain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.12);
        src.start(ctx.currentTime);
      }, 2200);
      
      let waveTimer = null;
      function scheduleWave() {
        if (!crowdActive || !gameRunning || paused) return;
        const now = ctx.currentTime;
        crowdGain.gain.linearRampToValueAtTime(0.65, now + 0.3);
        crowdGain.gain.linearRampToValueAtTime(0.45, now + 2.5);
        waveTimer = setTimeout(() => scheduleWave(), 12000 + Math.random() * 6000);
      }
      scheduleWave();
      
      lowSrc.start();
      midSrc.start();
      highSrc.start();
      
      crowdSources = [lowSrc, midSrc, highSrc];
      crowdNodes = [lowFilter, midFilter, highFilter, crowdGain];
      crowdActive = true;
      
      window._crowdClapInterval = clapInterval;
      window._crowdWaveTimer = waveTimer;
      
      crowdGain.gain.linearRampToValueAtTime(0.42, ctx.currentTime + 0.8);
    } catch(e) { console.warn("Crowd error:", e); }
  }

  function stopCrowd() {
    if (!crowdActive) return;
    try {
      const ctx = getCtx();
      if (crowdGain) {
        crowdGain.gain.linearRampToValueAtTime(0, ctx.currentTime + 0.6);
        setTimeout(() => {
          crowdSources.forEach(s => { try { s.stop(); } catch {} });
          crowdSources = [];
          crowdNodes.forEach(n => { try { n.disconnect(); } catch {} });
          crowdNodes = [];
          if (window._crowdClapInterval) clearInterval(window._crowdClapInterval);
          if (window._crowdWaveTimer) clearTimeout(window._crowdWaveTimer);
          crowdActive = false;
        }, 700);
      } else {
        crowdActive = false;
      }
    } catch(e) {}
  }

  function setCrowdVolume(vol) {
    if (!crowdGain || !crowdActive) return;
    try {
      const target = Math.min(0.65, Math.max(0.2, vol));
      crowdGain.gain.linearRampToValueAtTime(target, getCtx().currentTime + 0.3);
    } catch {}
  }

  // ------------------------------- GAME -------------------------------
  const canvas = document.getElementById('gameCanvas');
  const ctxDraw = canvas.getContext('2d');

  function resizeCanvas() {
    const container = canvas.parentElement;
    const maxWidth = Math.min(1200, window.innerWidth - 60);
    canvas.width = maxWidth;
    canvas.height = maxWidth * 0.6;
    updateFieldBounds();
  }

  let FIELD = { left: 0, right: 0, top: 0, bottom: 0 };
  let GOAL_LEFT = { x: 0, y: 0, width: 0, height: 0 };
  let GOAL_RIGHT = { x: 0, y: 0, width: 0, height: 0 };
  let scoringZones = [];

  function updateFieldBounds() {
    const margin = canvas.width * 0.05;
    const goalWidth = canvas.width * 0.035;
    const goalHeight = canvas.height * 0.28;

    FIELD.left = margin + goalWidth;
    FIELD.right = canvas.width - margin - goalWidth;
    FIELD.top = canvas.height * 0.1;
    FIELD.bottom = canvas.height - canvas.height * 0.1;

    GOAL_LEFT = { x: margin, y: (canvas.height - goalHeight) / 2, width: goalWidth, height: goalHeight };
    GOAL_RIGHT = { x: canvas.width - margin - goalWidth, y: (canvas.height - goalHeight) / 2, width: goalWidth, height: goalHeight };

    const zoneWidth = 45;
    const zoneHeight = 55;
    const startX = GOAL_RIGHT.x - zoneWidth - 5;
    const startY = GOAL_RIGHT.y;
    scoringZones = [
      { x: startX, y: startY, width: zoneWidth, height: zoneHeight },
      { x: startX, y: startY + (goalHeight/2) - zoneHeight/2, width: zoneWidth, height: zoneHeight },
      { x: startX, y: startY + goalHeight - zoneHeight, width: zoneWidth, height: zoneHeight }
    ];
  }

  window.addEventListener('resize', () => {
    resizeCanvas();
    if (allPlayers.length) repositionPlayers();
  });

  class Player {
    constructor(x, y, team, role, id) {
      this.x = x; this.y = y;
      this.vx = 0; this.vy = 0;
      this.team = team;
      this.role = role;
      this.id = id;
      this.radius = 12;
      this.hasBall = false;
      this.speed = 3.2;
      this.control = (team === 'haiti' && role === 'fwd' && id === 0);
      this.throwTimer = null;
    }

    draw() {
      ctxDraw.beginPath();
      ctxDraw.arc(this.x, this.y, this.radius, 0, 2*Math.PI);
      if (this.team === 'haiti') {
        ctxDraw.fillStyle = "#0033a0";
        ctxDraw.fill();
        ctxDraw.fillStyle = "#d21034";
        ctxDraw.fillRect(this.x-8, this.y+2, 16, 7);
        ctxDraw.fillStyle = "white";
        ctxDraw.font = "bold 12px 'Segoe UI'";
        ctxDraw.fillText("HT", this.x-5, this.y+4);
      } else {
        ctxDraw.fillStyle = opponentColors.primary;
        ctxDraw.fill();
        ctxDraw.fillStyle = opponentColors.secondary;
        ctxDraw.fillRect(this.x-8, this.y+2, 16, 7);
        ctxDraw.fillStyle = "white";
        ctxDraw.font = "bold 12px 'Segoe UI'";
        ctxDraw.fillText(opponentShort, this.x-5, this.y+4);
      }
      if (this.control) {
        ctxDraw.beginPath();
        ctxDraw.arc(this.x, this.y, this.radius+2, 0, 2*Math.PI);
        ctxDraw.strokeStyle = "gold";
        ctxDraw.lineWidth = 2;
        ctxDraw.stroke();
      }
      if (this.hasBall) {
        ctxDraw.fillStyle = "#f5b642";
        ctxDraw.beginPath();
        ctxDraw.arc(this.x-3, this.y-4, 4, 0, 2*Math.PI);
        ctxDraw.fill();
      }
    }

    update() {
      if (!gameRunning || paused) return;
      if (this.control) {
        this.x += this.vx;
        this.y += this.vy;
        this.vx *= 0.95;
        this.vy *= 0.95;
        this.x = Math.min(FIELD.right - this.radius, Math.max(FIELD.left + this.radius, this.x));
        this.y = Math.min(FIELD.bottom - this.radius, Math.max(FIELD.top + this.radius, this.y));
      } else {
        let targetX = ball.x, targetY = ball.y;
        if (this.role === 'gk') {
          targetX = this.team === 'haiti' ? FIELD.left + 18 : FIELD.right - 18;
          targetY = Math.min(GOAL_LEFT.y + GOAL_LEFT.height - 15, Math.max(GOAL_LEFT.y + 15, ball.y));
        }
        let dx = targetX - this.x, dy = targetY - this.y;
        let dist = Math.hypot(dx, dy);
        if (dist > 1) {
          let move = Math.min(this.speed, dist) / dist;
          this.x += dx * move * 0.85;
          this.y += dy * move * 0.85;
        }
        this.x = Math.min(FIELD.right - this.radius, Math.max(FIELD.left + this.radius, this.x));
        this.y = Math.min(FIELD.bottom - this.radius, Math.max(FIELD.top + this.radius, this.y));
      }
    }
  }

  let haitiPlayers = [], opponentPlayers = [], allPlayers = [];
  let ball = { x: 0, y: 0, vx: 0, vy: 0, radius: 6, owner: null, stuckTimer: null };
  let gameRunning = false;
  let paused = false;
  let matchTime = 90;
  let timerInterval = null;
  let haitiScore = 0, opponentScore = 0;
  let selectedOpponent = "France";
  let opponentColors = { primary: "#2c5f8a", secondary: "#e6e6e6" };
  let opponentShort = "FR";
  let lastTapTime = 0;

  function repositionPlayers() {
    const centerY = (FIELD.top + FIELD.bottom) / 2;
    if (haitiPlayers.length === 5) {
      haitiPlayers[0].x = FIELD.left+35; haitiPlayers[0].y = centerY-50;
      haitiPlayers[1].x = FIELD.left+80; haitiPlayers[1].y = centerY-70;
      haitiPlayers[2].x = FIELD.left+80; haitiPlayers[2].y = centerY+20;
      haitiPlayers[3].x = FIELD.left+140; haitiPlayers[3].y = centerY-30;
      haitiPlayers[4].x = FIELD.left+180; haitiPlayers[4].y = centerY+10;
      opponentPlayers[0].x = FIELD.right-35; opponentPlayers[0].y = centerY-50;
      opponentPlayers[1].x = FIELD.right-80; opponentPlayers[1].y = centerY-70;
      opponentPlayers[2].x = FIELD.right-80; opponentPlayers[2].y = centerY+20;
      opponentPlayers[3].x = FIELD.right-140; opponentPlayers[3].y = centerY-30;
      opponentPlayers[4].x = FIELD.right-180; opponentPlayers[4].y = centerY+10;
    }
  }

  function evacuatePlayersAroundGK() {
    const oppGK = opponentPlayers.find(p => p.role === 'gk');
    if (!oppGK) return;
    const gkX = oppGK.x, gkY = oppGK.y;
    for (let p of allPlayers) {
      if (p !== oppGK) {
        if (p.team === 'haiti') {
          p.x = Math.max(FIELD.left + 40, Math.min(FIELD.left + 150, p.x));
          p.y = Math.min(FIELD.bottom - 40, Math.max(FIELD.top + 40, p.y));
        } else {
          p.x = Math.min(FIELD.right - 40, Math.max(FIELD.right - 150, p.x));
          p.y = Math.min(FIELD.bottom - 40, Math.max(FIELD.top + 40, p.y));
        }
        let distToGK = Math.hypot(p.x - gkX, p.y - gkY);
        if (distToGK < 60) {
          let angle = Math.atan2(p.y - gkY, p.x - gkX);
          p.x = gkX + Math.cos(angle) * 70;
          p.y = gkY + Math.sin(angle) * 70;
          p.x = Math.min(FIELD.right - p.radius, Math.max(FIELD.left + p.radius, p.x));
          p.y = Math.min(FIELD.bottom - p.radius, Math.max(FIELD.top + p.radius, p.y));
        }
      }
    }
  }

  function initTeams() {
    const centerY = (FIELD.top + FIELD.bottom) / 2;
    haitiPlayers = [
      new Player(FIELD.left+35, centerY-50, 'haiti', 'gk', 0),
      new Player(FIELD.left+80, centerY-70, 'haiti', 'def', 1),
      new Player(FIELD.left+80, centerY+20, 'haiti', 'mid', 2),
      new Player(FIELD.left+140, centerY-30, 'haiti', 'fwd', 3),
      new Player(FIELD.left+180, centerY+10, 'haiti', 'fwd', 4)
    ];
    haitiPlayers[4].control = true;
    opponentPlayers = [
      new Player(FIELD.right-35, centerY-50, 'opponent', 'gk', 0),
      new Player(FIELD.right-80, centerY-70, 'opponent', 'def', 1),
      new Player(FIELD.right-80, centerY+20, 'opponent', 'mid', 2),
      new Player(FIELD.right-140, centerY-30, 'opponent', 'fwd', 3),
      new Player(FIELD.right-180, centerY+10, 'opponent', 'fwd', 4)
    ];
    allPlayers = [...haitiPlayers, ...opponentPlayers];
  }

  function resetBall() {
    ball.x = canvas.width/2;
    ball.y = canvas.height/2;
    ball.vx = 0; ball.vy = 0;
    if (ball.owner) ball.owner.hasBall = false;
    ball.owner = null;
    for (let p of allPlayers) p.hasBall = false;
    if (ball.stuckTimer) clearTimeout(ball.stuckTimer);
  }

  function checkBallStuck() {
    if (!gameRunning || paused) return;
    if (Math.abs(ball.vx) < 0.3 && Math.abs(ball.vy) < 0.3 && ball.owner === null) {
      if (!ball.stuckTimer) {
        ball.stuckTimer = setTimeout(() => {
          if (gameRunning && !paused && Math.abs(ball.vx) < 0.3 && Math.abs(ball.vy) < 0.3 && ball.owner === null) {
            resetBall();
            playWhistleShort();
          }
          ball.stuckTimer = null;
        }, 1000);
      }
    } else {
      if (ball.stuckTimer) { clearTimeout(ball.stuckTimer); ball.stuckTimer = null; }
    }
  }

  function goalScored(team) {
    if (team === 'haiti') {
      haitiScore++;
      document.getElementById("haitiScore").innerText = haitiScore;
      setCrowdVolume(0.65);
      playGoal(); playCheer();
      setTimeout(() => setCrowdVolume(0.45), 1000);
    } else {
      opponentScore++;
      document.getElementById("opponentScore").innerText = opponentScore;
      setCrowdVolume(0.65);
      playGoal();
      setTimeout(() => setCrowdVolume(0.45), 1000);
    }
    resetBall();
    playWhistleShort();
    repositionPlayers();
  }

  function updateBall() {
    if (!gameRunning || paused) return;
    ball.x += ball.vx;
    ball.y += ball.vy;
    ball.vx *= 0.99;
    ball.vy *= 0.99;

    if (ball.x - ball.radius < FIELD.left) { ball.x = FIELD.left + ball.radius; ball.vx *= -0.5; if (ball.owner) ball.owner.hasBall = false; ball.owner = null; }
    if (ball.x + ball.radius > FIELD.right) { ball.x = FIELD.right - ball.radius; ball.vx *= -0.5; if (ball.owner) ball.owner.hasBall = false; ball.owner = null; }
    if (ball.y - ball.radius < FIELD.top) { ball.y = FIELD.top + ball.radius; ball.vy *= -0.5; if (ball.owner) ball.owner.hasBall = false; ball.owner = null; }
    if (ball.y + ball.radius > FIELD.bottom) { ball.y = FIELD.bottom - ball.radius; ball.vy *= -0.5; if (ball.owner) ball.owner.hasBall = false; ball.owner = null; }

    if (ball.x + ball.radius >= GOAL_LEFT.x && ball.x - ball.radius <= GOAL_LEFT.x + GOAL_LEFT.width &&
        ball.y + ball.radius >= GOAL_LEFT.y && ball.y - ball.radius <= GOAL_LEFT.y + GOAL_LEFT.height) {
      goalScored('opponent');
      return;
    }
    if (ball.x + ball.radius >= GOAL_RIGHT.x && ball.x - ball.radius <= GOAL_RIGHT.x + GOAL_RIGHT.width &&
        ball.y + ball.radius >= GOAL_RIGHT.y && ball.y - ball.radius <= GOAL_RIGHT.y + GOAL_RIGHT.height) {
      goalScored('haiti');
      return;
    }

    for (let p of allPlayers) {
      const dist = Math.hypot(p.x - ball.x, p.y - ball.y);
      if (dist < p.radius + ball.radius) {
        if (ball.owner) ball.owner.hasBall = false;
        ball.owner = p;
        p.hasBall = true;
        const angle = Math.atan2(ball.y - p.y, ball.x - p.x);
        const force = 3.2;
        ball.vx = Math.cos(angle) * force;
        ball.vy = Math.sin(angle) * force;
        if (p.role === 'gk') {
          ball.vx = 0; ball.vy = 0;
          evacuatePlayersAroundGK();
          if (p.throwTimer) clearTimeout(p.throwTimer);
          p.throwTimer = setTimeout(() => {
            if (p.hasBall && gameRunning && !paused) {
              const teammates = p.team === 'haiti' ? haitiPlayers : opponentPlayers;
              let target = null;
              let minDist = 999;
              for (let t of teammates) {
                if (t !== p && Math.hypot(t.x-p.x, t.y-p.y) < 180) {
                  let d = Math.hypot(t.x-p.x, t.y-p.y);
                  if (d < minDist) { minDist = d; target = t; }
                }
              }
              if (target) {
                const dx = target.x - p.x, dy = target.y - p.y;
                const len = Math.hypot(dx, dy);
                if (len > 0.1) {
                  ball.vx = (dx/len) * 7;
                  ball.vy = (dy/len) * 7;
                }
                p.hasBall = false;
                ball.owner = null;
                playKick();
              }
            }
            p.throwTimer = null;
          }, 450);
        }
        break;
      }
    }
    checkBallStuck();
  }

  function isInScoringZone(x, y) {
    for (let zone of scoringZones) {
      if (x >= zone.x && x <= zone.x + zone.width && y >= zone.y && y <= zone.y + zone.height) {
        return true;
      }
    }
    return false;
  }

  function shoot(player) {
    if (!player.hasBall) return false;
    if (!isInScoringZone(player.x, player.y)) {
      const oppGK = opponentPlayers.find(p => p.role === 'gk');
      if (oppGK) {
        if (ball.owner) ball.owner.hasBall = false;
        ball.owner = oppGK;
        oppGK.hasBall = true;
        ball.vx = 0; ball.vy = 0;
        playCatch();
        evacuatePlayersAroundGK();
      }
      player.hasBall = false;
      return false;
    }

    const dir = player.team === 'haiti' ? 1 : -1;
    const power = 9 + Math.random() * 4;
    ball.vx = dir * power + (Math.random() - 0.5) * 1.2;
    ball.vy = (Math.random() - 0.5) * 2.5;
    player.hasBall = false;
    ball.owner = null;
    playKick();
    return true;
  }

  function pass(player, targetPlayer) {
    if (!player.hasBall) return false;
    if (targetPlayer) {
      const dx = targetPlayer.x - player.x, dy = targetPlayer.y - player.y;
      const len = Math.hypot(dx, dy);
      if (len > 0.1) {
        ball.vx = (dx/len) * 6;
        ball.vy = (dy/len) * 6;
      }
      player.hasBall = false;
      ball.owner = null;
      playKick();
      return true;
    }
    return false;
  }

  function aiTeammateDecision() {
    if (!gameRunning || paused) return;
    const user = haitiPlayers.find(p => p.control);
    if (!user) return;
    for (let p of haitiPlayers) {
      if (p !== user && p.hasBall && p.role !== 'gk') {
        if (isInScoringZone(p.x, p.y)) {
          shoot(p);
        } else {
          pass(p, user);
        }
      }
    }
  }

  function aiOpponentActions() {
    if (!gameRunning || paused) return;
    for (let p of opponentPlayers) {
      if (p.hasBall && p.role !== 'gk') {
        const nearGoal = p.x < FIELD.left + 90;
        if (nearGoal || Math.random() < 0.012) shoot(p);
        else if (Math.random() < 0.008) {
          const teammates = opponentPlayers.filter(t => t !== p);
          if (teammates.length) {
            let best = teammates.reduce((a,b) => Math.hypot(a.x-p.x, a.y-p.y) < Math.hypot(b.x-p.x, b.y-p.y) ? a : b);
            pass(p, best);
          }
        }
      }
    }
  }

  function drawField() {
    ctxDraw.fillStyle = "#2e7d32";
    ctxDraw.fillRect(0, 0, canvas.width, canvas.height);
    ctxDraw.strokeStyle = "#f9f3cf";
    ctxDraw.lineWidth = 3;
    ctxDraw.strokeRect(FIELD.left, FIELD.top, FIELD.right-FIELD.left, FIELD.bottom-FIELD.top);
    ctxDraw.beginPath();
    ctxDraw.arc(canvas.width/2, canvas.height/2, 40, 0, 2*Math.PI);
    ctxDraw.stroke();
    ctxDraw.beginPath();
    ctxDraw.moveTo(canvas.width/2, FIELD.top);
    ctxDraw.lineTo(canvas.width/2, FIELD.bottom);
    ctxDraw.stroke();
    ctxDraw.fillStyle = "#00000066";
    ctxDraw.fillRect(GOAL_LEFT.x, GOAL_LEFT.y, GOAL_LEFT.width, GOAL_LEFT.height);
    ctxDraw.fillRect(GOAL_RIGHT.x, GOAL_RIGHT.y, GOAL_RIGHT.width, GOAL_RIGHT.height);
    ctxDraw.fillStyle = "#f9eeb0";
    ctxDraw.font = "bold 22px monospace";
    ctxDraw.fillText("🇭🇹", FIELD.left-28, canvas.height/2);
    ctxDraw.fillText(opponentShort, FIELD.right+12, canvas.height/2);

    ctxDraw.fillStyle = "rgba(255, 215, 0, 0.4)";
    for (let zone of scoringZones) {
      ctxDraw.fillRect(zone.x, zone.y, zone.width, zone.height);
    }

    if (paused && gameRunning) {
      ctxDraw.font = "bold 48px 'Segoe UI'";
      ctxDraw.fillStyle = "rgba(0,0,0,0.7)";
      ctxDraw.fillText("⏸ PAUSED", canvas.width/2 - 100, canvas.height/2);
    }
  }

  function drawBall() {
    ctxDraw.beginPath();
    ctxDraw.arc(ball.x, ball.y, ball.radius, 0, 2*Math.PI);
    ctxDraw.fillStyle = "#f5bc70";
    ctxDraw.fill();
    ctxDraw.strokeStyle = "#442200";
    ctxDraw.lineWidth = 1.5;
    ctxDraw.beginPath();
    ctxDraw.moveTo(ball.x-4, ball.y); ctxDraw.lineTo(ball.x+4, ball.y);
    ctxDraw.moveTo(ball.x, ball.y-4); ctxDraw.lineTo(ball.x, ball.y+4);
    ctxDraw.stroke();
  }

  function render() {
    drawField();
    for (let p of allPlayers) p.draw();
    drawBall();
  }

  function gameUpdate() {
    if (!gameRunning || paused) return;
    for (let p of allPlayers) p.update();
    updateBall();
    aiTeammateDecision();
    aiOpponentActions();
  }

  function animate() {
    gameUpdate();
    render();
    requestAnimationFrame(animate);
  }

  function endMatch() {
    gameRunning = false;
    if (timerInterval) clearInterval(timerInterval);
    stopCrowd();
    playWhistle();
    document.getElementById("gameMessage").innerHTML = `⏰ FULL TIME! HAITI ${haitiScore} - ${opponentScore} ${selectedOpponent} ⏰`;
  }

  function startTimer() {
    if (timerInterval) clearInterval(timerInterval);
    timerInterval = setInterval(() => {
      if (gameRunning && !paused && matchTime > 0) {
        matchTime--;
        const mins = Math.floor(matchTime / 60);
        const secs = matchTime % 60;
        document.getElementById("gameTimer").innerText = `${mins.toString().padStart(2,'0')}:${secs.toString().padStart(2,'0')}`;
        if (matchTime === 0) endMatch();
      } else if (matchTime <= 0) endMatch();
    }, 1000);
  }

  function startMatch() {
    if (gameRunning) endMatch();
    stopCrowd();
    matchTime = 90;
    haitiScore = 0; opponentScore = 0;
    document.getElementById("haitiScore").innerText = "0";
    document.getElementById("opponentScore").innerText = "0";
    document.getElementById("gameTimer").innerText = "01:30";
    selectedOpponent = document.getElementById("opponentSelect").value;
    const oppMap = { France:{primary:"#2c5f8a", secondary:"#e6e6e6"}, Brazil:{primary:"#ffcc00", secondary:"#009c3b"}, Argentina:{primary:"#75aadb", secondary:"#ffffff"}, Germany:{primary:"#000000", secondary:"#dd0000"}, England:{primary:"#ffffff", secondary:"#c8102e"}, Mexico:{primary:"#006847", secondary:"#ce1126"} };
    opponentColors = oppMap[selectedOpponent];
    opponentShort = selectedOpponent.substring(0,2).toUpperCase();
    document.getElementById("opponentLabel").innerHTML = `🇫🇷 ${selectedOpponent} <span id="opponentScore">0</span>`;
    updateFieldBounds();
    initTeams();
    repositionPlayers();
    resetBall();
    gameRunning = true;
    paused = false;
    startCrowd();
    playFanfare();
    startTimer();
    document.getElementById("gameMessage").innerHTML = "⚽ MATCH LIVE! Move with ARROWS/SWIPE, shoot with ENTER/TAP. Score only from GOLDEN ZONES!";
  }

  function togglePause() {
    if (!gameRunning) return;
    paused = !paused;
    const pauseBtn = document.getElementById("pauseBtn");
    if (paused) {
      pauseBtn.innerHTML = "▶️ RESUME";
      pauseBtn.style.background = "#6ab04c";
      document.getElementById("gameMessage").innerHTML = "⏸ GAME PAUSED – Press RESUME or P key to continue";
      if (crowdGain && crowdActive) crowdGain.gain.linearRampToValueAtTime(0.2, getCtx().currentTime + 0.3);
    } else {
      pauseBtn.innerHTML = "⏸️ PAUSE";
      pauseBtn.style.background = "#f4a261";
      document.getElementById("gameMessage").innerHTML = "⚽ GAME RESUMED! Move, shoot, score!";
      if (crowdGain && crowdActive) crowdGain.gain.linearRampToValueAtTime(0.45, getCtx().currentTime + 0.5);
    }
  }

  // Controls
  window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowUp' || e.key === 'ArrowDown' || e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
      const user = haitiPlayers.find(p => p.control);
      if (user && gameRunning && !paused) {
        let dx = 0, dy = 0;
        if (e.key === 'ArrowLeft') dx = -user.speed;
        if (e.key === 'ArrowRight') dx = user.speed;
        if (e.key === 'ArrowUp') dy = -user.speed;
        if (e.key === 'ArrowDown') dy = user.speed;
        user.vx = dx;
        user.vy = dy;
      }
      e.preventDefault();
    }
    if (e.key === 'Enter' && gameRunning && !paused) {
      e.preventDefault();
      const user = haitiPlayers.find(p => p.control);
      if (user && user.hasBall) shoot(user);
    }
    if ((e.key === 'p' || e.key === 'P') && gameRunning) {
      e.preventDefault();
      togglePause();
    }
  });

  canvas.addEventListener('touchstart', (e) => {
    e.preventDefault();
    const touch = e.touches[0];
    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    const canvasX = (touch.clientX - rect.left) * scaleX;
    const canvasY = (touch.clientY - rect.top) * scaleY;
    
    const now = Date.now();
    if (now - lastTapTime < 300) {
      const user = haitiPlayers.find(p => p.control);
      if (user && user.hasBall && gameRunning && !paused) {
        const teammates = haitiPlayers.filter(t => t !== user && t.role !== 'gk');
        if (teammates.length) {
          const target = teammates.reduce((a,b) => Math.hypot(a.x-user.x, a.y-user.y) < Math.hypot(b.x-user.x, b.y-user.y) ? a : b);
          pass(user, target);
        }
      }
      lastTapTime = 0;
    } else {
      lastTapTime = now;
      const user = haitiPlayers.find(p => p.control);
      if (user && user.hasBall && gameRunning && !paused) shoot(user);
    }
    window.touchStartX = canvasX;
    window.touchStartY = canvasY;
  });

  canvas.addEventListener('touchmove', (e) => {
    e.preventDefault();
    if (!gameRunning || paused) return;
    const touch = e.touches[0];
    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    const canvasX = (touch.clientX - rect.left) * scaleX;
    const canvasY = (touch.clientY - rect.top) * scaleY;
    if (window.touchStartX !== undefined) {
      const dx = canvasX - window.touchStartX;
      const dy = canvasY - window.touchStartY;
      const user = haitiPlayers.find(p => p.control);
      if (user) {
        user.vx = dx * 0.5;
        user.vy = dy * 0.5;
      }
      window.touchStartX = canvasX;
      window.touchStartY = canvasY;
    }
  });

  canvas.addEventListener('touchend', (e) => {
    e.preventDefault();
    window.touchStartX = undefined;
    window.touchStartY = undefined;
    const user = haitiPlayers.find(p => p.control);
    if (user) { user.vx *= 0.8; user.vy *= 0.8; }
  });

  document.getElementById("startGameBtn").addEventListener("click", () => { resumeAudio(); startMatch(); });
  document.getElementById("resetGameBtn").addEventListener("click", () => { resumeAudio(); startMatch(); });
  document.getElementById("pauseBtn").addEventListener("click", togglePause);
  document.getElementById("audioBtn").addEventListener("click", () => { resumeAudio(); if(!gameRunning) document.getElementById("gameMessage").innerHTML = "🔊 Audio ready! Press KICK OFF."; });

  // Splash screen starfield
  function createStars() {
    const overlay = document.getElementById('splashOverlay');
    for (let i = 0; i < 200; i++) {
      const star = document.createElement('div');
      star.className = 'star';
      star.style.left = Math.random() * 100 + '%';
      star.style.top = Math.random() * 100 + '%';
      star.style.width = Math.random() * 3 + 1 + 'px';
      star.style.height = star.style.width;
      star.style.animationDelay = Math.random() * 2 + 's';
      star.style.animationDuration = Math.random() * 1.5 + 0.5 + 's';
      overlay.appendChild(star);
    }
    const flagContainer = document.createElement('div');
    flagContainer.className = 'flag-container';
    flagContainer.innerHTML = '<div class="haiti-flag"></div>';
    const namesDiv = document.createElement('div');
    namesDiv.className = 'names';
    namesDiv.innerHTML = `
      <p class="owner">🇭🇹 Gesner Deslandes 🇭🇹</p>
      <p>Collaborators:</p>
      <p>Gesner Junior Deslandes | Roosevelt Deslandes</p>
      <p>Sebastien Stephane Deslandes | Zendaya Christelle Deslandes</p>
    `;
    overlay.appendChild(flagContainer);
    overlay.appendChild(namesDiv);
  }
  createStars();

  // Initial setup
  resizeCanvas();
  initTeams();
  repositionPlayers();
  resetBall();
  animate();

  // Welcome fanfare and remove splash after 5 seconds
  resumeAudio();
  playWelcomeFanfare();
  setTimeout(() => {
    const splash = document.getElementById('splashOverlay');
    if (splash) splash.style.display = 'none';
    document.querySelector('.game-wrapper').style.opacity = '1';
  }, 5000);
</script>
</body>
</html>
"""

st.components.v1.html(game_html, height=650, scrolling=False)
