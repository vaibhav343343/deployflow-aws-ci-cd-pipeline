<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DeployFlow · modern CI/CD</title>
  <style>
    /* ----- reset / base ----- */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
    }

    body {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at 20% 30%, #0c0b1f, #02020a 70%, #000000);
      padding: 1.5rem;
      position: relative;
      overflow-x: hidden;
    }

    /* subtle animated grid / tech overlay */
    body::before {
      content: "";
      position: absolute;
      inset: 0;
      background-image: 
        linear-gradient(rgba(90, 60, 255, 0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(90, 60, 255, 0.02) 1px, transparent 1px);
      background-size: 60px 60px;
      pointer-events: none;
      z-index: 0;
    }

    /* floating glow orbs */
    body::after {
      content: "";
      position: absolute;
      width: 40vw;
      height: 40vw;
      right: -5vw;
      top: -10vw;
      background: radial-gradient(circle, rgba(140, 70, 255, 0.25) 0%, transparent 70%);
      border-radius: 50%;
      filter: blur(80px);
      z-index: 0;
    }

    /* main card – glass / neumorphism fusion */
    .card {
      position: relative;
      z-index: 10;
      max-width: 820px;
      width: 100%;
      background: rgba(10, 8, 25, 0.6);
      backdrop-filter: blur(12px) saturate(180%);
      -webkit-backdrop-filter: blur(12px) saturate(180%);
      border: 1px solid rgba(160, 130, 255, 0.18);
      border-radius: 3.5rem;
      padding: 3.5rem 3rem;
      box-shadow: 
        0 30px 60px -15px rgba(0, 0, 0, 0.8),
        0 0 0 1px rgba(200, 180, 255, 0.1) inset,
        0 0 30px 0 rgba(130, 70, 255, 0.25);
      transition: transform 0.25s ease, box-shadow 0.3s ease;
      animation: floatIn 0.9s cubic-bezier(0.15, 0.9, 0.25, 1) forwards;
    }

    .card:hover {
      box-shadow: 
        0 40px 70px -10px rgba(0, 0, 0, 0.9),
        0 0 0 1px rgba(220, 190, 255, 0.3) inset,
        0 0 50px 5px rgba(150, 90, 255, 0.4);
      transform: scale(1.01) translateY(-3px);
    }

    /* header area */
    .header-row {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem 1rem;
      margin-bottom: 2rem;
    }

    .title-section {
      display: flex;
      flex-direction: column;
    }

    .project-title {
      font-size: 3.2rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      background: linear-gradient(115deg, #ffffff 0%, #dac8ff 45%, #b79aff 70%, #8d6aff);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      line-height: 1.1;
      text-shadow: 0 0 20px rgba(170, 130, 255, 0.5);
      margin-bottom: 0.3rem;
    }

    .subtitle {
      font-size: 1.1rem;
      font-weight: 400;
      color: rgba(210, 195, 255, 0.75);
      letter-spacing: 0.3px;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .badge-status {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      background: rgba(10, 25, 20, 0.3);
      backdrop-filter: blur(8px);
      padding: 0.7rem 1.4rem 0.7rem 1.2rem;
      border-radius: 60px;
      border: 1px solid rgba(70, 255, 150, 0.25);
      box-shadow: 0 0 12px rgba(0, 255, 180, 0.2), inset 0 1px 2px rgba(255,255,255,0.2);
    }

    .status-text {
      font-weight: 500;
      color: rgba(230, 255, 240, 0.9);
      text-transform: uppercase;
      font-size: 0.9rem;
      letter-spacing: 0.06em;
    }

    .glowing-green {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      background: rgba(0, 255, 150, 0.08);
      padding: 0.25rem 1rem 0.25rem 0.8rem;
      border-radius: 40px;
      border-left: 2px solid #2effb2;
    }

    .dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #20ff9f;
      box-shadow: 0 0 12px #2effb2, 0 0 25px #0affa0;
      animation: pulseGlow 1.8s infinite ease-in-out;
    }

    .badge-status span:last-child {
      font-weight: 600;
      color: white;
      font-size: 1.05rem;
    }

    /* icon row — tech stack */
    .tech-strip {
      display: flex;
      flex-wrap: wrap;
      gap: 1.2rem 2rem;
      margin: 2.5rem 0 2.8rem 0;
      justify-content: center;
    }

    .tech-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(20, 15, 45, 0.5);
      backdrop-filter: blur(4px);
      padding: 0.5rem 1.4rem 0.5rem 1.2rem;
      border-radius: 60px;
      border: 1px solid rgba(180, 150, 255, 0.25);
      font-size: 1.1rem;
      font-weight: 450;
      color: rgba(235, 225, 255, 0.9);
      transition: all 0.2s ease;
      box-shadow: 0 6px 12px -8px rgba(0,0,0,0.8);
    }

    .tech-item:hover {
      border-color: #ad8dff;
      background: rgba(45, 30, 75, 0.7);
      transform: translateY(-3px);
      box-shadow: 0 15px 20px -10px #6229ff40;
    }

    .tech-icon {
      font-size: 1.7rem;
      filter: drop-shadow(0 0 6px #aa88ff);
    }

    /* pipeline visual / progress bar – futuristic */
    .pipeline-visual {
      margin: 2.2rem 0 2rem;
    }

    .pipeline-label {
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: rgba(200, 180, 255, 0.7);
      margin-bottom: 0.5rem;
    }

    .stages {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .stage {
      flex: 1;
      height: 10px;
      background: rgba(255, 255, 255, 0.06);
      border-radius: 40px;
      box-shadow: inset 0 1px 4px #00000080;
      position: relative;
      overflow: hidden;
    }

    .stage.active::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(90deg, #9b6dff, #c86eff, #6eb2ff);
      border-radius: 40px;
      box-shadow: 0 0 20px #a47eff;
      animation: stageFlow 2.2s infinite ease-in-out;
      width: 100%;
    }

    .stage.completed {
      background: linear-gradient(90deg, #9f7aff, #b088ff);
      box-shadow: 0 0 12px #aa80ff;
    }

    /* metrics (minimalistic) */
    .meta-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.2rem;
      margin: 2rem 0 1.2rem;
    }

    .meta-card {
      background: rgba(12, 8, 28, 0.6);
      backdrop-filter: blur(4px);
      border-radius: 2rem;
      padding: 1.2rem 0.8rem;
      text-align: center;
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-bottom: 2px solid rgba(170, 130, 255, 0.3);
      box-shadow: 0 10px 20px -12px black;
      transition: 0.2s;
    }

    .meta-card:hover {
      border-bottom-color: #caa6ff;
      background: rgba(25, 15, 45, 0.7);
    }

    .meta-value {
      font-size: 1.8rem;
      font-weight: 650;
      background: linear-gradient(145deg, #f0ebff, #cfbaff);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      line-height: 1.2;
    }

    .meta-label {
      color: #9c8bc0;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }

    /* CTA / futuristic link */
    .action-row {
      display: flex;
      justify-content: flex-end;
      align-items: center;
      margin-top: 2rem;
      padding-top: 0.5rem;
      border-top: 1px dashed rgba(200, 160, 255, 0.3);
    }

    .deploy-link {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.05);
      padding: 0.6rem 1.8rem;
      border-radius: 60px;
      color: #ddd6ff;
      text-decoration: none;
      font-weight: 500;
      letter-spacing: 0.01em;
      backdrop-filter: blur(4px);
      transition: 0.2s;
      box-shadow: 0 0 10px rgba(180, 130, 255, 0.2);
    }

    .deploy-link:hover {
      background: rgba(70, 30, 130, 0.6);
      border-color: #b185ff;
      color: white;
      box-shadow: 0 0 25px #b47cff;
      transform: scale(1.02);
    }

    .arrow-icon {
      transition: transform 0.15s;
    }
    .deploy-link:hover .arrow-icon {
      transform: translateX(5px);
    }

    /* animations */
    @keyframes floatIn {
      0% { opacity: 0; transform: translateY(20px) scale(0.97); }
      100% { opacity: 1; transform: translateY(0) scale(1); }
    }

    @keyframes pulseGlow {
      0% { opacity: 1; box-shadow: 0 0 8px #38ffb0, 0 0 18px #00ffa2; }
      50% { opacity: 0.6; box-shadow: 0 0 14px #75ffc0, 0 0 40px #00f7a7; }
      100% { opacity: 1; box-shadow: 0 0 8px #38ffb0, 0 0 18px #00ffa2; }
    }

    @keyframes stageFlow {
      0% { opacity: 0.7; filter: brightness(1); }
      50% { opacity: 1; filter: brightness(1.3); }
      100% { opacity: 0.7; filter: brightness(1); }
    }

    /* responsive */
    @media (max-width: 600px) {
      .card {
        padding: 2.2rem 1.5rem;
        border-radius: 2.5rem;
      }
      .project-title {
        font-size: 2.5rem;
      }
      .header-row {
        flex-direction: column;
        align-items: flex-start;
      }
      .badge-status {
        width: 100%;
        justify-content: center;
      }
      .meta-grid {
        grid-template-columns: 1fr;
        gap: 0.8rem;
      }
      .tech-strip {
        justify-content: flex-start;
        gap: 0.8rem;
      }
    }

    @media (max-width: 380px) {
      .tech-item {
        width: 100%;
        justify-content: center;
      }
    }

    /* extra glow line */
    .glow-line {
      width: 100%;
      height: 2px;
      background: linear-gradient(90deg, transparent, #9f7aff, #c884ff, #9f7aff, transparent);
      filter: blur(2px);
      margin: 1.8rem 0 0.5rem;
      opacity: 0.6;
    }

    /* small print / version */
    .version-hint {
      text-align: right;
      font-size: 0.7rem;
      color: #524f7a;
      letter-spacing: 0.5px;
      margin-top: 0.8rem;
    }
  </style>
  <!-- Inter font (optional but clean) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400;14..32,500;14..32,600;14..32,700&display=swap" rel="stylesheet">
</head>
<body>
  <main class="card">
    <!-- header with title + status -->
    <div class="header-row">
      <div class="title-section">
        <h1 class="project-title">DeployFlow</h1>
        <div class="subtitle">
          <span class="emoji-icon">⚡</span> CI/CD Pipeline Automation on AWS
        </div>
      </div>
      <div class="badge-status">
        <span class="status-text">status</span>
        <div class="glowing-green">
          <span class="dot"></span>
          <span>Operational</span>
        </div>
      </div>
    </div>

    <!-- icons / devops cluster -->
    <div class="tech-strip">
      <div class="tech-item"><span class="tech-icon">☁️</span> AWS</div>
      <div class="tech-item"><span class="tech-icon">🐳</span> Docker</div>
      <div class="tech-item"><span class="tech-icon">⚙️</span> CI/CD</div>
      <div class="tech-item"><span class="tech-icon">📦</span> Kubernetes</div>
      <div class="tech-item"><span class="tech-icon">🔁</span> GitOps</div>
    </div>

    <!-- pipeline stages (visual + animation) -->
    <div class="pipeline-visual">
      <div class="pipeline-label">
        <span>🚀 build</span>
        <span>🧪 test</span>
        <span>📦 deploy</span>
        <span>✅ monitor</span>
      </div>
      <div class="stages">
        <div class="stage completed" style="flex:1.2;"></div>
        <div class="stage completed"></div>
        <div class="stage active"></div>
        <div class="stage"></div>
      </div>
    </div>

    <!-- modern metrics / glass grid -->
    <div class="meta-grid">
      <div class="meta-card">
        <div class="meta-value">147</div>
        <div class="meta-label">deploys today</div>
      </div>
      <div class="meta-card">
        <div class="meta-value">1.2s</div>
        <div class="meta-label">avg. rollback</div>
      </div>
      <div class="meta-card">
        <div class="meta-value">100%</div>
        <div class="meta-label">success rate</div>
      </div>
    </div>

    <!-- subtle glow separator -->
    <div class="glow-line"></div>

    <!-- call to action / futuristic link + version -->
    <div class="action-row">
      <a href="#" class="deploy-link">
        <span>View pipeline</span>
        <span class="arrow-icon">➡️</span>
      </a>
    </div>
    <div class="version-hint">deployflow · edge v2.4.1 · fleet ready</div>

    <!-- hidden little extra pulse on the dot is already there -->
  </main>

  <!-- optional extra animation (pure css, no js needed) 
       but we add a tiny JS just to set a fake "active" time? no, it's fine -->
  <script>
    // (optional minimal js for dynamic feel – zero framework)
    // simply ensure the pipeline animation is playful
    // you can leave it out, but we add a tiny updater to change stage glow?
    // no need — the css stages give the feeling. 
    // but for a tiny interactive effect: click on card? no, we avoid.
    // however a micro-interaction: hover on meta cards shows small transition (already in css)
    // we keep it clean, no mandatory js. 
    // (this block can be removed, but it's here to show we could add)
    window.addEventListener('load', ()=>{
      // just for demo: add a small dynamic timestamp? but not required.
      // however we want pure css solution? yes.
      // I'll leave a console remark (invisible to ui) 
      console.log('DeployFlow UI ready — zero framework, all glass.');
    });
  </script>
  <!-- no extra frameworks — everything embedded -->
</body>
</html>
