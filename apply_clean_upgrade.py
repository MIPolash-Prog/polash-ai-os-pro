import os
path = r"C:\Users\mipol\polash-ai-upgraded\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

aurora = '<div class="aurora"></div>'
canvas = '<div class="aurora"></div>\n    <canvas id="neuralCanvas" style="position:fixed;inset:0;z-index:-1;pointer-events:none;opacity:0.45;"></canvas>'
if 'id="neuralCanvas"' not in text and aurora in text:
    text = text.replace(aurora, canvas, 1)

widget = """
    <style>
        #polashAiBtn { position: fixed; bottom: 24px; right: 24px; z-index: 9999; background: linear-gradient(135deg, #f6c453, #00d4ff); color: #0b1020; border: none; border-radius: 999px; padding: 12px 20px; font-weight: 800; font-size: 13.5px; box-shadow: 0 10px 30px rgba(0, 212, 255, 0.35); cursor: pointer; display: flex; align-items: center; gap: 8px; transition: 0.3s; }
        #polashAiBtn:hover { transform: scale(1.06); }
        #aiModal { position: fixed; bottom: 80px; right: 24px; width: 350px; max-width: calc(100vw - 32px); background: #151d30; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 18px; box-shadow: 0 20px 50px rgba(2, 6, 18, 0.6); z-index: 9999; display: none; flex-direction: column; overflow: hidden; font-family: system-ui, sans-serif; backdrop-filter: blur(16px); }
        #aiModal.active { display: flex; }
        .aim-header { background: linear-gradient(135deg, rgba(246, 196, 83, 0.15), rgba(0, 212, 255, 0.15)); padding: 12px 16px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(148, 163, 184, 0.15); }
        .aim-title { font-weight: 700; font-size: 14px; color: #e9eefb; display: flex; align-items: center; gap: 8px; }
        .aim-close { background: none; border: none; color: #9aa6bd; font-size: 16px; cursor: pointer; }
        .aim-body { padding: 14px; max-height: 260px; overflow-y: auto; display: flex; flex-direction: column; gap: 8px; }
        .aim-msg { padding: 8px 12px; border-radius: 10px; font-size: 13px; line-height: 1.4; max-width: 90%; }
        .aim-msg.bot { background: #1a2438; color: #e9eefb; align-self: flex-start; }
        .aim-msg.user { background: #f6c453; color: #0b1020; align-self: flex-end; font-weight: 600; }
        .aim-footer { padding: 10px 14px; border-top: 1px solid rgba(148, 163, 184, 0.15); display: flex; gap: 8px; background: #111827; }
        .aim-input { flex: 1; background: #1a2438; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 8px; padding: 7px 10px; color: #e9eefb; font-size: 13px; outline: none; }
        .aim-send { background: #f6c453; color: #0b1020; border: none; border-radius: 8px; padding: 0 12px; font-weight: 700; cursor: pointer; font-size: 13px; }
    </style>
    <button id="polashAiBtn" onclick="document.getElementById('aiModal').classList.toggle('active')"><span>✨ Polash AI Assistant</span></button>
    <div id="aiModal">
        <div class="aim-header">
            <div class="aim-title"><span>🤖</span> Polash AI OS Assistant</div>
            <button class="aim-close" onclick="document.getElementById('aiModal').classList.remove('active')">✕</button>
        </div>
        <div class="aim-body" id="aimStream">
            <div class="aim-msg bot">Hello! I am Monjurul Islam Polash's AI Assistant. How can I help you today regarding web development, SEO, AI tools, or hiring Polash?</div>
        </div>
        <div class="aim-footer">
            <input type="text" id="aimInput" class="aim-input" placeholder="Ask anything..." onkeydown="if(event.key==='Enter')this.nextElementSibling.click()">
            <button class="aim-send" onclick="var i=document.getElementById('aimInput'),s=document.getElementById('aimStream');if(i.value.trim()){var m=document.createElement('div');m.className='aim-msg user';m.textContent=i.value;s.appendChild(m);i.value='';setTimeout(function(){var b=document.createElement('div');b.className='aim-msg bot';b.textContent='Polash AI OS helps you Build, Learn, Earn, and Grow. Monjurul Islam Polash is an expert Web Developer & SEO Specialist!';s.appendChild(b);s.scrollTop=s.scrollHeight;},500);s.scrollTop=s.scrollHeight;}">Send</button>
        </div>
    </div>
    <script>
    window.addEventListener('DOMContentLoaded', function() {
        var canvas = document.getElementById('neuralCanvas');
        if (!canvas) return;
        var ctx = canvas.getContext('2d'), w, h, particles = [];
        function resize() { w = canvas.width = window.innerWidth; h = canvas.height = window.innerHeight; }
        window.addEventListener('resize', resize); resize();
        for (let i = 0; i < 35; i++) particles.push({ x: Math.random() * w, y: Math.random() * h, vx: (Math.random() - 0.5) * 0.5, vy: (Math.random() - 0.5) * 0.5, r: Math.random() * 2 + 0.8 });
        function anim() {
            ctx.clearRect(0, 0, w, h);
            ctx.fillStyle = 'rgba(0, 212, 255, 0.35)';
            ctx.strokeStyle = 'rgba(246, 196, 83, 0.1)';
            ctx.lineWidth = 1;
            for (let i = 0; i < particles.length; i++) {
                let p = particles[i]; p.x += p.vx; p.y += p.vy;
                if (p.x < 0 || p.x > w) p.vx *= -1;
                if (p.y < 0 || p.y > h) p.vy *= -1;
                ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
                for (let j = i + 1; j < particles.length; j++) {
                    let p2 = particles[j];
                    if (Math.hypot(p.x - p2.x, p.y - p2.y) < 95) {
                        ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(p2.x, p2.y); ctx.stroke();
                    }
                }
            }
            requestAnimationFrame(anim);
        }
        anim();
    });
    </script>
"""

if 'polashAiBtn' not in text:
    text = text.replace('</body>', widget + '\n</body>')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS")
else:
    print("EXISTS")
