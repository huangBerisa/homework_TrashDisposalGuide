import os

OUT = os.path.dirname(os.path.abspath(__file__))

SHARED_CSS = """
    :root{
      --color-primary:#55C900;
      --color-primary-light:#E5FFC7;
      --color-bg:#FFFFFF;
      --color-surface:#F8F8F8;
      --color-text:#303030;
      --color-text-muted:#9A9A9A;
      --color-alert:#FF4D4D;
      --color-alert-light:#FFE7E7;
      --color-warning:#FF9500;
      --color-warning-light:#FFF1DC;
      --color-divider:#E3E3E3;
      --radius:8px;
      --radius-card:16px;
      --fs-1:28px;
      --fs-2:20px;
      --fs-3:16px;
      --fs-4:14px;
      --fs-5:12px;
    }
    *{box-sizing:border-box;}
    html,body{margin:0;padding:0;height:100%;}
    body{
      background:var(--color-bg);
      color:var(--color-text);
      font-family:'Noto Sans JP', sans-serif;
      -webkit-font-smoothing:antialiased;
    }
    a{color:var(--color-primary);}
    a:hover{color:var(--color-primary);}
    button{font-family:inherit;}

    .screen-root{
      width:402px; min-height:874px;
      display:flex; flex-direction:column;
      background:var(--color-bg);
    }
    .app-header{
      position:relative;
      flex:0 0 auto;
      height:56px;
      display:flex; align-items:center; justify-content:center;
      border-bottom:1px solid var(--color-divider);
      background:var(--color-bg);
    }
    .app-header span{font-size:var(--fs-3); font-weight:700; color:var(--color-text); letter-spacing:0.02em;}
    .back-btn{
      position:absolute; left:8px; top:50%; transform:translateY(-50%);
      width:44px; height:44px;
      display:flex; align-items:center; justify-content:center;
      background:none; border:none; padding:0; color:var(--color-text);
    }
    .back-btn svg{width:22px; height:22px;}
    .app-body{flex:1 1 auto; padding:16px;}

    .title-1{font-size:var(--fs-1); font-weight:700; margin:0; color:var(--color-text); text-wrap:balance;}
    .title-2{font-size:var(--fs-2); font-weight:700; margin:0; color:var(--color-text);}
    .section-title{font-size:var(--fs-2); font-weight:600; margin:0; color:var(--color-text);}
    .body-2{font-size:var(--fs-4); color:var(--color-text-muted); margin:0; line-height:1.6;}
    .caption{font-size:var(--fs-5); color:var(--color-text-muted); margin:0;}

    .section{margin-bottom:24px;}
    .section:last-child{margin-bottom:0;}
    .stack-8 > * + *{margin-top:8px;}
    .stack-16 > * + *{margin-top:16px;}

    .btn{
      display:flex; align-items:center; justify-content:center; gap:8px;
      width:100%; min-height:44px;
      border-radius:var(--radius);
      font-size:var(--fs-3); font-weight:700;
      border:1px solid transparent;
    }
    .btn-primary{background:var(--color-primary); color:#FFFFFF;}
    .btn-primary svg{width:16px; height:16px; flex:0 0 auto;}
    .btn-secondary{background:var(--color-bg); color:var(--color-primary); border-color:var(--color-primary);}
    .btn-small{width:auto; min-height:44px; padding:0 16px; font-size:var(--fs-4);}

    .lang-list{list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:8px;}
    .lang-card{
      display:flex; align-items:center; gap:8px;
      width:100%; min-height:44px; padding:16px;
      background:var(--color-surface);
      border:1px solid transparent;
      border-radius:var(--radius-card);
      font-size:var(--fs-3); color:var(--color-text);
      text-align:left;
    }
    .lang-card .flag{font-size:20px; line-height:1;}
    .lang-card .name{flex:1;}
    .lang-card .check{width:16px; height:16px; flex:0 0 auto; visibility:hidden;}
    .lang-card.selected{background:var(--color-primary-light); border-color:var(--color-primary); font-weight:700;}
    .lang-card.selected .check{visibility:visible;}

    .viewfinder{
      aspect-ratio:1/1;
      background:var(--color-surface);
      border-radius:var(--radius-card);
      display:flex; align-items:center; justify-content:center;
      position:relative;
    }
    .viewfinder svg{width:64px; height:64px;}
    .viewfinder .corner{position:absolute; width:24px; height:24px; border:2px solid var(--color-text-muted);}
    .viewfinder .tl{top:8px; left:8px; border-right:none; border-bottom:none;}
    .viewfinder .tr{top:8px; right:8px; border-left:none; border-bottom:none;}
    .viewfinder .bl{bottom:8px; left:8px; border-right:none; border-top:none;}
    .viewfinder .br{bottom:8px; right:8px; border-left:none; border-top:none;}

    .item-row{display:flex; align-items:center; gap:16px;}
    .item-thumb{
      width:64px; height:64px; flex:0 0 auto;
      background:var(--color-primary);
      border-radius:var(--radius);
      display:flex; align-items:center; justify-content:center;
    }
    .item-thumb svg{width:40px; height:40px;}

    .result-card{background:var(--color-surface); border-radius:var(--radius-card); padding:16px;}

    .caution{
      display:flex; gap:8px; align-items:flex-start;
      background:var(--color-alert-light);
      border-radius:var(--radius);
      padding:16px;
      color:var(--color-alert);
    }
    .caution svg{width:16px; height:16px; flex:0 0 auto; margin-top:2px;}
    .caution p{font-size:var(--fs-4); margin:0; line-height:1.6; color:var(--color-text);}

    .howto-list{margin:0; padding:0; list-style:none; display:flex; flex-direction:column; gap:8px;}
    .howto-list li{display:flex; gap:8px; align-items:flex-start; font-size:var(--fs-3); color:var(--color-text); line-height:1.6;}
    .howto-list li svg{width:16px; height:16px; flex:0 0 auto; margin-top:3px; color:var(--color-primary);}

    .bin-list{display:flex; flex-direction:column; gap:16px;}
    .bin-card{border:1px solid var(--color-divider); border-radius:var(--radius-card); padding:16px;}
    .bin-card-top{display:flex; gap:8px;}
    .bin-icon{
      width:40px; height:40px; flex:0 0 auto;
      background:var(--color-primary-light);
      border-radius:var(--radius);
      display:flex; align-items:center; justify-content:center;
    }
    .bin-icon svg{width:22px; height:22px; color:var(--color-primary);}
    .bin-main{flex:1; min-width:0;}
    .bin-name{font-size:var(--fs-2); font-weight:700; color:var(--color-text); margin:0;}

    .chip-row{display:flex; flex-wrap:wrap; gap:8px; margin:8px 0 0;}
    .chip{
      display:inline-flex; align-items:center;
      padding:4px 12px;
      border:1px solid var(--color-divider);
      border-radius:999px;
      font-size:var(--fs-5); font-weight:500;
      color:var(--color-text-muted);
      background:var(--color-bg);
    }
    .chip-match{background:var(--color-primary-light); border-color:var(--color-primary); color:var(--color-text); font-weight:700;}

    .pill{display:inline-flex; align-items:center; gap:4px; padding:4px 12px; border-radius:999px; font-size:var(--fs-5); font-weight:700;}
    .pill svg{width:12px; height:12px;}
    .pill.positive{background:var(--color-primary-light); color:var(--color-text);}
    .pill.almost-full{background:var(--color-warning-light); color:var(--color-warning);}
    .pill.full{background:var(--color-alert-light); color:var(--color-alert);}

    .bin-meta{display:flex; align-items:center; gap:8px; flex-wrap:wrap; margin-top:16px; padding-top:16px; border-top:1px solid var(--color-divider);}
    .bin-distance{display:flex; align-items:center; gap:8px; font-size:var(--fs-3); color:var(--color-text); font-weight:500;}
    .bin-distance svg{width:16px; height:16px; color:var(--color-text-muted);}
    .bin-note{font-size:var(--fs-4); color:var(--color-text-muted); margin:8px 0 0;}
    .bin-card .btn{margin-top:16px;}

    .state-screen{
      flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center;
      text-align:center; gap:16px; padding:16px;
    }
    .state-icon{width:56px; height:56px; border-radius:50%; background:var(--color-surface); display:flex; align-items:center; justify-content:center;}
    .state-icon svg{width:28px; height:28px; color:var(--color-text-muted);}
    .state-icon.alert svg{color:var(--color-alert);}
    .state-screen .btn{max-width:280px;}

    .map-wrap{flex:1 1 auto; position:relative; background:var(--color-surface); overflow:hidden;}
    .map-svg{display:block; width:100%; height:100%; font-family:'Noto Sans JP', sans-serif;}
    .map-land{fill:var(--color-surface);}
    .map-park{fill:var(--color-primary-light); stroke:var(--color-primary); stroke-width:1;}
    .map-road{stroke:var(--color-bg); stroke-width:14; fill:none; stroke-linecap:round; stroke-linejoin:round;}
    .map-road-line{stroke:var(--color-divider); stroke-width:1; stroke-dasharray:2 6; fill:none;}
    .map-building{fill:var(--color-bg); stroke:var(--color-divider); stroke-width:1;}
    .map-landmark{fill:var(--color-primary-light); stroke:var(--color-primary); stroke-width:1;}
    .map-landmark-label{fill:var(--color-text); font-size:12px; font-weight:700; text-anchor:middle;}
    .map-road-label{fill:var(--color-text-muted); font-size:9px; font-weight:600; letter-spacing:0.03em;}
    .map-route{stroke:var(--color-primary); stroke-width:3.5; fill:none; stroke-linecap:round; stroke-linejoin:round; stroke-dasharray:2 9;}
    .map-you-ring{fill:var(--color-bg); stroke:var(--color-primary); stroke-width:2;}
    .map-you-dot{fill:var(--color-primary);}
    .map-you-label{fill:var(--color-text); font-size:10px; font-weight:700; text-anchor:middle;}
    .map-pin{fill:var(--color-primary);}
    .map-pin-badge{fill:var(--color-bg);}
    .map-pin-icon{stroke:var(--color-primary); stroke-width:1.6; fill:none;}

    .map-info{flex:0 0 auto; padding:16px; border-top:1px solid var(--color-divider); background:var(--color-bg);}
    .map-pager{display:flex; align-items:center; gap:8px;}
    .map-pager-info{flex:1 1 auto; min-width:0;}
    .pager-btn{
      width:44px; height:44px; flex:0 0 auto;
      display:flex; align-items:center; justify-content:center;
      background:var(--color-surface); border:none; border-radius:var(--radius);
      color:var(--color-text); padding:0;
    }
    .pager-btn svg{width:18px; height:18px;}
    .map-meta{display:flex; align-items:center; gap:8px; flex-wrap:wrap; margin:8px 0 0;}
    .map-distance{display:flex; align-items:center; gap:8px; margin:0; font-size:var(--fs-3); color:var(--color-text); font-weight:500;}
    .map-distance svg{width:16px; height:16px; color:var(--color-text-muted);}
    .map-accepted{margin-top:16px; padding-top:16px; border-top:1px solid var(--color-divider);}
"""

FONT_LINK = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap">'

def wrap(body):
    return f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONT_LINK}
<style>
{SHARED_CSS}
</style>
</helmet>
{body}
</x-dc>
</body>
</html>
"""

BACK_BTN = '<button class="back-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 5l-7 7 7 7" stroke-linecap="round" stroke-linejoin="round"/></svg></button>'

CHECK_SVG = '<svg class="check" viewBox="0 0 16 16" fill="none"><path d="M3 8.5L6.5 12L13 4.5" stroke="#55C900" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# ---------------- Lang.dc.html ----------------
lang_body = f"""<div class="screen-root">
  <header class="app-header"><span>ゴミナビ</span></header>
  <div class="app-body">
    <div class="section stack-16">
      <h2 class="title-1">言語を選択してください</h2>
      <p class="body-2">読める言語をお選びください。</p>
    </div>
    <ul class="lang-list">
      <li><button class="lang-card"><span class="flag">🇯🇵</span><span class="name">日本語</span>{CHECK_SVG}</button></li>
      <li><button class="lang-card"><span class="flag">🇺🇸</span><span class="name">English</span>{CHECK_SVG}</button></li>
      <li><button class="lang-card"><span class="flag">🇨🇳</span><span class="name">中文（简体）</span>{CHECK_SVG}</button></li>
      <li><button class="lang-card"><span class="flag">🇹🇼</span><span class="name">中文（繁體）</span>{CHECK_SVG}</button></li>
      <li><button class="lang-card"><span class="flag">🇰🇷</span><span class="name">한국어</span>{CHECK_SVG}</button></li>
    </ul>
  </div>
</div>"""

# ---------------- Capture.dc.html ----------------
capture_body = f"""<div class="screen-root">
  <header class="app-header">
    {BACK_BTN}
    <span>ゴミナビ</span>
  </header>
  <div class="app-body">
    <div class="section stack-16">
      <h2 class="title-1">捨てたいごみを撮影してください</h2>
      <p class="body-2">ごみ全体が写るように撮影してください。</p>
    </div>
    <div class="section">
      <div class="viewfinder">
        <span class="corner tl"></span><span class="corner tr"></span>
        <span class="corner bl"></span><span class="corner br"></span>
        <svg viewBox="0 0 24 24" fill="none" stroke="#9A9A9A" stroke-width="1.5">
          <path d="M4 8h2l1.5-2h9L18 8h2a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z" stroke-linejoin="round"/>
          <circle cx="12" cy="13" r="3.5"/>
        </svg>
      </div>
    </div>
    <div class="section stack-8">
      <button class="btn btn-primary"><span>撮影する</span><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 3l5 5-5 5" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
      <button class="btn btn-secondary">写真を選ぶ</button>
    </div>
  </div>
</div>"""

# ---------------- Main.dc.html (screen3: result + bins) ----------------
def bin_card(icon_svg, name, chips, distance, pill_class, pill_icon_svg, pill_text, note):
    chips_html = "\n".join(f'<span class="chip">{c}</span>' for c in chips)
    return f"""<div class="bin-card">
  <div class="bin-card-top">
    <div class="bin-icon">{icon_svg}</div>
    <div class="bin-main">
      <p class="bin-name">{name}</p>
      <div class="chip-row">
        {chips_html}
      </div>
    </div>
  </div>
  <div class="bin-meta">
    <span class="bin-distance"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M8 14.5S13 9.8 13 6.3A5 5 0 0 0 3 6.3C3 9.8 8 14.5 8 14.5z"/><circle cx="8" cy="6.3" r="1.7"/></svg>{distance}</span>
    <span class="pill {pill_class}">{pill_icon_svg}<span>{pill_text}</span></span>
  </div>
  <p class="bin-note">{note}</p>
  <button class="btn btn-secondary btn-small">ここへ行く</button>
</div>"""

BIN_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 7h14l-1.2 12.2A2 2 0 0 1 15.8 21H8.2a2 2 0 0 1-2-1.8L5 7z"/><path d="M3.5 7h17M9 4h6l1 3H8l1-3z" stroke-linejoin="round"/></svg>'
CHECK_PILL = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 9.5L6.5 13L13 5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
WARN_PILL = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M8 1.5l6.5 11.5H1.5L8 1.5z" stroke-linejoin="round"/><path d="M8 6.2v3" stroke-linecap="round"/><circle cx="8" cy="11" r="0.8" fill="currentColor" stroke="none"/></svg>'

main_body = f"""<div class="screen-root">
  <header class="app-header">
    {BACK_BTN}
    <span>ゴミナビ</span>
  </header>
  <div class="app-body">

    <div class="section stack-16">
      <div class="item-row">
        <div class="item-thumb">
          <svg viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="1.5">
            <path d="M9 3h6v2.2l1.4 2.1c.4.5.6 1.2.6 1.8V19a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2V9.1c0-.6.2-1.3.6-1.8L9 5.2V3z"/>
            <path d="M8.5 11h7" stroke-linecap="round"/>
          </svg>
        </div>
        <div>
          <p class="title-2">ペットボトル</p>
          <p class="body-2">中身を空にして、キャップとラベルを外します。</p>
        </div>
      </div>
    </div>

    <div class="section result-card stack-16">
      <div class="stack-8">
        <p class="caption">分類結果</p>
        <p class="title-1">資源ごみ</p>
        <p class="body-2">決められた回収日に、透明な袋に入れて出します。</p>
      </div>
      <div class="stack-8">
        <p class="title-2" style="font-size:var(--fs-3);">捨て方</p>
        <ul class="howto-list">
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8.5L6.5 12L13 4.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>キャップとラベルは外して「プラスチック」に分けます。</span></li>
          <li><svg viewBox="0 0 16 16" fill="none"><path d="M3 8.5L6.5 12L13 4.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>つぶしてから出すと、収集がスムーズです。</span></li>
        </ul>
      </div>
      <div class="caution">
        <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M8 1.5l7 12.5H1L8 1.5z" stroke-linejoin="round"/><path d="M8 6.5v3.5" stroke-linecap="round"/><circle cx="8" cy="11.7" r="0.9" fill="currentColor" stroke="none"/></svg>
        <p>洗っていないペットボトルは収集されない場合があります。</p>
      </div>
    </div>

    <div class="section stack-16">
      <p class="section-title">周辺のごみ箱</p>
      <div class="bin-list">
        {bin_card(BIN_ICON, "京都駅前 分別ステーション", ["ペットボトル","缶","びん"], "150m", "positive", CHECK_PILL, "空きあり", "ふたを閉めてから入れてください。")}
        {bin_card(BIN_ICON, "四条通 ごみ箱", ["ペットボトル","缶"], "320m", "almost-full", WARN_PILL, "満杯に近づいています", "紙ごみは入れられません。")}
        {bin_card(BIN_ICON, "河原町 リサイクルボックス", ["ペットボトル","びん","古紙"], "480m", "full", WARN_PILL, "満杯です", "収集後に空きが戻る場合があります。")}
      </div>
    </div>

  </div>
</div>"""

# ---------------- Map.dc.html (static snapshot: bin1 state) ----------------
map_body = f"""<div class="screen-root">
  <header class="app-header">
    {BACK_BTN}
    <span>ゴミナビ</span>
  </header>
  <div class="map-wrap">
    <svg class="map-svg" viewBox="-20 160 240 440" preserveAspectRatio="xMidYMid slice">
      <rect class="map-land" x="-60" y="-60" width="480" height="680"/>

      <rect class="map-park" x="300" y="0" width="60" height="500"/>
      <text class="map-landmark-label" x="330" y="250" transform="rotate(-90 330 250)">鴨川</text>
      <rect class="map-landmark" x="6" y="392" width="88" height="100" rx="4"/>
      <text class="map-landmark-label" x="50" y="446" style="font-size:11px;">京都駅</text>

      <rect class="map-building" x="130" y="15" width="70" height="95" rx="3"/>
      <rect class="map-building" x="15" y="150" width="70" height="95" rx="3"/>
      <rect class="map-building" x="130" y="150" width="70" height="95" rx="3"/>
      <rect class="map-building" x="235" y="150" width="50" height="95" rx="3"/>
      <rect class="map-building" x="130" y="280" width="70" height="85" rx="3"/>
      <rect class="map-building" x="235" y="280" width="50" height="85" rx="3"/>

      <path class="map-road" d="M100 0v500"/>
      <path class="map-road" d="M220 0v500"/>
      <path class="map-road" d="M300 0v500"/>
      <path class="map-road" d="M0 130h360"/>
      <path class="map-road" d="M0 260h360"/>
      <path class="map-road" d="M0 380h360"/>
      <path class="map-road-line" d="M100 0v500"/>
      <path class="map-road-line" d="M220 0v500"/>
      <path class="map-road-line" d="M300 0v500"/>
      <path class="map-road-line" d="M0 130h360"/>
      <path class="map-road-line" d="M0 260h360"/>
      <path class="map-road-line" d="M0 380h360"/>

      <text class="map-road-label" x="0" y="0" transform="translate(108 60) rotate(-90)">烏丸通</text>
      <text class="map-road-label" x="30" y="122">四条通</text>
      <text class="map-road-label" x="0" y="0" transform="translate(308 300) rotate(-90)">河原町通</text>

      <path class="map-route" d="M100 380 L100 260"/>

      <circle class="map-you-ring" cx="100" cy="380" r="13"/>
      <circle class="map-you-dot" cx="100" cy="380" r="5"/>
      <text class="map-you-label" x="100" y="362">現在地</text>

      <g transform="translate(100 260)">
        <path class="map-pin" d="M0 30C0 30 -18 12 -18 -6a18 18 0 1 1 36 0C18 12 0 30 0 30z"/>
        <circle class="map-pin-badge" cx="0" cy="-6" r="11"/>
        <g class="map-pin-icon" transform="translate(-6 -12)">
          <path d="M1 5h10l-1 9A1.6 1.6 0 0 1 8.4 15.5H4.6A1.6 1.6 0 0 1 3 13.9L2 5z"/>
          <path d="M0.5 5h11M3.8 2.3h4.4l0.7 2h-5.8l0.7-2z" stroke-linejoin="round"/>
        </g>
      </g>
    </svg>
  </div>
  <div class="map-info">
    <div class="map-pager">
      <button class="pager-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 5l-7 7 7 7" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
      <div class="map-pager-info">
        <p class="title-2">京都駅前 分別ステーション</p>
        <div class="map-meta">
          <p class="map-distance"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M8 14.5S13 9.8 13 6.3A5 5 0 0 0 3 6.3C3 9.8 8 14.5 8 14.5z"/><circle cx="8" cy="6.3" r="1.7"/></svg><span>150m</span></p>
          <span class="pill positive">{CHECK_PILL}<span>空きあり</span></span>
        </div>
      </div>
      <button class="pager-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
    </div>
    <div class="map-accepted">
      <p class="caption">対応ごみ</p>
      <div class="chip-row">
        <span class="chip chip-match">ペットボトル</span>
        <span class="chip">缶</span>
        <span class="chip">びん</span>
      </div>
    </div>
  </div>
</div>"""

# ---------------- Empty.dc.html ----------------
empty_body = f"""<div class="screen-root">
  <header class="app-header">
    {BACK_BTN}
    <span>ゴミナビ</span>
  </header>
  <div class="state-screen">
    <div class="state-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21" stroke-linecap="round"/></svg>
    </div>
    <p class="title-2">該当するごみが見つかりませんでした。</p>
    <p class="body-2">ごみの名前を変えて、もう一度お調べください。</p>
    <button class="btn btn-primary"><span>もう一度調べる</span><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 3l5 5-5 5" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
  </div>
</div>"""

# ---------------- Error.dc.html ----------------
error_body = f"""<div class="screen-root">
  <header class="app-header">
    {BACK_BTN}
    <span>ゴミナビ</span>
  </header>
  <div class="state-screen">
    <div class="state-icon alert">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2.5l10 17.5H2L12 2.5z" stroke-linejoin="round"/><path d="M12 9.5v5" stroke-linecap="round"/><circle cx="12" cy="17" r="1" fill="currentColor" stroke="none"/></svg>
    </div>
    <p class="title-2">分類情報を取得できませんでした。</p>
    <p class="body-2">もう一度お試しください。</p>
    <button class="btn btn-primary"><span>もう一度調べる</span><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 3l5 5-5 5" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
  </div>
</div>"""

files = {
    "Lang.dc.html": lang_body,
    "Capture.dc.html": capture_body,
    "Main.dc.html": main_body,
    "Map.dc.html": map_body,
    "Empty.dc.html": empty_body,
    "Error.dc.html": error_body,
}

for name, body in files.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(wrap(body))
    print("wrote", name)

canvas = {
    "artboards": [
        {"file": "Lang.dc.html", "x": 0, "y": 0, "w": 402, "h": 874, "title": "① 言語選択"},
        {"file": "Capture.dc.html", "x": 502, "y": 0, "w": 402, "h": 874, "title": "② 撮影"},
        {"file": "Main.dc.html", "x": 1004, "y": 0, "w": 402, "h": 874, "title": "③ 分別結果とごみ箱"},
        {"file": "Map.dc.html", "x": 1506, "y": 0, "w": 402, "h": 874, "title": "④ 地図案内"},
        {"file": "Empty.dc.html", "x": 2008, "y": 0, "w": 402, "h": 874, "title": "⑤ 見つからない場合"},
        {"file": "Error.dc.html", "x": 2510, "y": 0, "w": 402, "h": 874, "title": "⑥ 確認できない場合"}
    ],
    "launch": {"view": "canvas"}
}
import json
with open(os.path.join(OUT, "canvas.json"), "w", encoding="utf-8") as f:
    json.dump(canvas, f, ensure_ascii=False, indent=2)
print("wrote canvas.json")
