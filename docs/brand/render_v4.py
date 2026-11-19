import os, json, tempfile
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

OUT=Path(tempfile.gettempdir())/"asso-gh-brand-v4-20261119"
OUT.mkdir(parents=True,exist_ok=True)
PALETTE={"deep":"#10191e","navy":"#152329","petrol":"#1b3438","mint":"#B9DECB","cream":"#F9F6EF","coral":"#F27769","blue":"#DCEFFA"}
CSS=r'''
* {box-sizing:border-box}
html,body {margin:0;padding:0}
body {background:#152329;color:#F9F6EF;font-family:"DM Sans",Arial,sans-serif}
.frame {width:100%;height:100%;overflow:hidden;position:relative;
 background:
 radial-gradient(ellipse 44% 82% at 79% 39%, rgba(94,135,125,.29),transparent 79%),
 radial-gradient(ellipse 45% 75% at 105% 110%,rgba(242,119,105,.18),transparent 80%),
 linear-gradient(125deg,#10191e 0%,#15282c 44%,#1a3738 74%,#142329 100%)}
.frame:before {content:"";position:absolute;inset:0;opacity:.30;pointer-events:none;
 background-image:linear-gradient(90deg,rgba(185,222,203,.06) 1px,transparent 1px),
 linear-gradient(rgba(185,222,203,.035) 1px,transparent 1px);background-size:94px 94px}
.rule {position:absolute;height:1px;left:6%;right:6%;top:13%;background:linear-gradient(90deg,#B9DECBaa,#F27769aa,transparent)}
.eyebrow {position:absolute;top:6.8%;left:6%;color:#B9DECB;letter-spacing:.18em;font:500 22px "DM Mono",monospace}
.edition {position:absolute;top:6.8%;right:6%;letter-spacing:.16em;font:500 21px "DM Mono",monospace;color:#E9E2FBa9}
.mark {position:absolute;width:43%;height:84%;left:55%;top:10%}
.title {position:absolute;left:6%;top:27%;width:55%;z-index:2}
.title .lead {color:#F9F6EF;font-family:"DM Sans",sans-serif;font-weight:700;font-size:124px;letter-spacing:-.067em;line-height:1}
.title .accent {color:#FF9F91;font-family:"Instrument Serif",Georgia,serif;font-weight:400;font-style:italic;font-size:135px;letter-spacing:-.02em;line-height:1.03;margin-left:2px}
.kicker {position:absolute;left:6%;bottom:10%;font:500 20px "DM Mono",monospace;letter-spacing:.13em;color:#B9DECB}
.motif {position:absolute;right:6%;top:25%;width:40%;height:64%;z-index:1}
.micro {font:500 15px "DM Mono",monospace;letter-spacing:.14em;fill:#B9DECB}
.pill {position:absolute;right:6%;bottom:10%;font:500 18px "DM Mono",monospace;letter-spacing:.08em;color:#F9F6EF}
.project .title {top:26%;width:58%}
.project .title .lead {font-size:121px}
.project .title .accent {font-size:105px}
.project .motif {right:5%;width:43%}
.profile .title .lead {font-size:126px}
.profile .title .accent {font-size:156px}
.profile .motif {right:5%;width:45%;top:20%;height:70%}
.mobile .rule {top:9%}
.mobile .eyebrow {top:4.6%;font-size:27px}
.mobile .edition {top:4.6%;font-size:26px}
.mobile .title {left:7%;top:18%;width:88%}
.mobile .title .lead {font-size:112px}
.mobile .title .accent {font-size:144px}
.mobile .motif {left:6%;right:6%;width:88%;top:47%;height:42%}
.mobile .kicker {left:7%;bottom:7%;font-size:24px;max-width:86%;line-height:1.6}
.mobile .pill {display:none}
.mobile .micro {font-size:24px}
.mobile.profile .title .lead {font-size:118px}
.mobile.profile .title .accent {font-size:151px}
.mobile.profile .motif {top:47%;height:38%}
.mobile.project .title .lead {font-size:125px}
.mobile.project .title .accent {font-size:120px}
.mobile.project .motif {top:45%;height:44%}
'''
SVG_CONVERGE='''<svg viewBox="0 0 720 450" width="100%" height="100%">
<defs><linearGradient id="line" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#B9DECB"/><stop offset=".62" stop-color="#89C2B1"/><stop offset="1" stop-color="#F27769"/></linearGradient><radialGradient id="shine"><stop stop-color="#B9DECB" stop-opacity=".30"/><stop offset="1" stop-color="#B9DECB" stop-opacity="0"/></radialGradient></defs>
<circle cx="434" cy="217" r="183" stroke="#B9DECB" stroke-opacity=".21" fill="none"/>
<circle cx="434" cy="217" r="112" stroke="#F27769" stroke-opacity=".22" fill="none"/>
<circle cx="434" cy="217" r="226" fill="url(#shine)" opacity=".5"/>
<path d="M64 104 C280 104 284 217 425 217 M64 347 C280 347 284 217 425 217 M425 217 C520 217 590 217 675 217" stroke="url(#line)" stroke-width="4" fill="none" stroke-linecap="round"/>
<circle cx="64" cy="104" r="13" fill="#B9DECB"/><circle cx="64" cy="347" r="13" fill="#F27769"/>
<circle cx="434" cy="217" r="23" fill="#152329" stroke="#B9DECB" stroke-width="3"/><circle cx="434" cy="217" r="7" fill="#F27769"/>
<circle cx="675" cy="217" r="16" fill="#F27769"/>
<text x="58" y="80" class="micro">FIELD</text><text x="58" y="382" class="micro">SYSTEMS</text>
<text x="604" y="196" class="micro">PROOF</text>
</svg>'''
SVG_RECEIPT='''<svg viewBox="0 0 650 480" width="100%" height="100%">
<defs><linearGradient id="paper" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#B9DECB"/><stop offset="1" stop-color="#74B8A9"/></linearGradient></defs>
<rect x="190" y="26" width="332" height="410" rx="24" fill="#2C5651" stroke="#B9DECB" stroke-opacity=".23" stroke-width="3" transform="rotate(7 356 231)"/>
<rect x="125" y="25" width="332" height="410" rx="23" fill="#203F42" stroke="#A6D3C5" stroke-opacity=".7" stroke-width="3"/>
<text x="165" y="83" font-family="DM Mono" font-size="19" fill="#F9F6EF">ACE / AUDIT RECEIPT</text>
<path d="M165 105H415" stroke="#B9DECB" stroke-opacity=".4" stroke-width="2"/>
<g font-family="DM Mono" font-size="25" fill="#F9F6EF"><text x="165" y="165">PROOF</text><text x="165" y="230">RISK</text><text x="165" y="295">PERMISSION</text></g>
<g fill="none" stroke-width="3"><circle cx="405" cy="151" r="13" stroke="#B9DECB"/><circle cx="405" cy="216" r="13" stroke="#F27769"/><circle cx="405" cy="281" r="13" stroke="#DCEFFA"/></g>
<path d="M165 330H411" stroke="#B9DECB" stroke-opacity=".4" stroke-width="2"/>
<path d="M166 372H350" stroke="#B9DECB" stroke-opacity=".33" stroke-width="9" stroke-linecap="round"/>
<path d="M166 396H278" stroke="#B9DECB" stroke-opacity=".21" stroke-width="9" stroke-linecap="round"/>
<circle cx="535" cy="90" r="52" fill="#F27769" opacity=".95"/><text x="517" y="107" font-family="DM Sans" font-weight="700" font-size="62" fill="#152329">?</text>
<text x="505" y="462" class="micro">INSPECT. DON'T ASSUME.</text>
</svg>'''
SVG_ANIMA='''<svg viewBox="0 0 650 470" width="100%" height="100%">
<circle cx="355" cy="229" r="185" stroke="#B9DECB" stroke-opacity=".24" stroke-width="2" fill="#B9DECB" fill-opacity=".035"/>
<circle cx="355" cy="229" r="126" stroke="#F27769" stroke-opacity=".35" stroke-width="2" fill="none"/>
<path d="M140 126 H510 M140 235 H510 M140 346 H510" stroke="#B9DECB" stroke-opacity=".15" stroke-width="2"/>
<path d="M140 126 L355 235 L520 346" stroke="#B9DECB" stroke-opacity=".85" stroke-width="4" fill="none"/>
<g font-family="DM Mono" font-size="19" font-weight="500" fill="#F9F6EF">
<text x="65" y="123">01</text><text x="78" y="156" fill="#B9DECB">MANDATE</text>
<text x="82" y="241">02</text><text x="73" y="275" fill="#B9DECB">PAYER</text>
<text x="510" y="318">03</text><text x="499" y="376" fill="#B9DECB">HUMAN</text>
</g>
<circle cx="140" cy="126" r="19" fill="#B9DECB"/>
<circle cx="355" cy="235" r="30" fill="#152329" stroke="#F27769" stroke-width="5"/>
<circle cx="520" cy="346" r="20" fill="#F27769"/>
<circle cx="355" cy="235" r="8" fill="#B9DECB"/>
<text x="216" y="434" class="micro">SANDBOX / TEST MONEY ONLY</text>
</svg>'''
SVG_EINSTEIN='''<svg viewBox="0 0 650 480" width="100%" height="100%">
<text x="37" y="150" font-family="DM Sans" font-size="114" font-weight="700" letter-spacing="-8" fill="#F9F6EF">18.5%</text>
<text x="47" y="185" font-family="DM Mono" font-size="24" fill="#B9DECB" letter-spacing="4">FASTER IN THIS BENCHMARK</text>
<path d="M46 218H610" stroke="#B9DECB" stroke-opacity=".26" stroke-width="2"/>
<text x="47" y="275" font-family="Instrument Serif" font-style="italic" font-size="58" fill="#F27769">Three fewer accepted.</text>
<text x="47" y="339" font-family="DM Mono" font-size="21" fill="#DCEFFA">SOLO</text>
<rect x="180" y="320" width="375" height="25" rx="9" fill="#2B5151"/>
<rect x="180" y="320" width="375" height="25" rx="9" fill="#B9DECB"/>
<text x="568" y="339" font-family="DM Mono" font-size="20" fill="#F9F6EF">12</text>
<text x="47" y="389" font-family="DM Mono" font-size="21" fill="#DCEFFA">PARALLEL</text>
<rect x="180" y="369" width="375" height="25" rx="9" fill="#2B5151"/>
<rect x="180" y="369" width="281" height="25" rx="9" fill="#F27769"/>
<text x="568" y="389" font-family="DM Mono" font-size="20" fill="#F9F6EF">9</text>
<text x="48" y="449" class="micro">24 CASES · LOCAL EXPERIMENT</text>
</svg>'''
spec={
 "profile":("HICHEM BENALI / MONKIDY","2026","Hichem","Benali.","I DON'T PICK A FIELD.  I PICK A PROBLEM.",SVG_CONVERGE),
 "ace":("SYSTASYS / PUBLIC TOOL","ACE RECEIPTS","ACE","Receipts","PROOF · RISK · PERMISSION",SVG_RECEIPT),
 "anima":("SYSTASYS / SANDBOX EXPERIMENT","ANIMA","ANIMA","Three gates.","PAYPAL SANDBOX · NO REAL MONEY",SVG_ANIMA),
 "einstein":("PUBLIC RESEARCH / MEASURED","EINSTEIN","EINSTEIN","The trade-off.","18.5% FASTER · THREE FEWER ACCEPTED",SVG_EINSTEIN)
}
files={}
with sync_playwright() as pw:
 browser=pw.chromium.launch(channel="chrome",headless=True,args=["--disable-extensions","--disable-gpu"])
 for name,(eyebrow,edition,first,second,kicker,motif) in spec.items():
  for mobile in (False,True):
   w,h=(900,1060) if mobile else (1840,610)
   kind="mobile" if mobile else "desktop"
   cls="frame "+name+(" project" if name!="profile" else "")+(" mobile" if mobile else "")
   html=f'''<!doctype html><html><head><meta charset="UTF-8"><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>
   <section class="{cls}" style="width:{w}px;height:{h}px">
   <div class="rule"></div><div class="eyebrow">{eyebrow}</div><div class="edition">{edition}</div>
   <div class="title"><div class="lead">{first}</div><div class="accent">{second}</div></div>
   <div class="motif">{motif}</div><div class="kicker">{kicker}</div>
   </section></body></html>'''
   ctx=browser.new_context(viewport={"width":w,"height":h},device_scale_factor=1,color_scheme="dark")
   page=ctx.new_page()
   page.set_content(html,wait_until="load",timeout=25000)
   try: page.evaluate("() => document.fonts.ready")
   except: pass
   page.wait_for_timeout(800)
   png=OUT/f"{name}-{kind}.png"
   page.screenshot(path=str(png),full_page=False)
   im=Image.open(png).convert("RGB")
   target=OUT/f"{name}-{kind}.webp"
   im.save(target,"WEBP",quality=90,method=6)
   files[f"{name}-{kind}"]={"name":str(target),"bytes":target.stat().st_size,"width":w,"height":h}
   print(name,kind,target.stat().st_size,flush=True)
   ctx.close()
 browser.close()
(OUT/"asset_manifest.json").write_text(json.dumps(files,indent=2),encoding="utf-8")
print("DIR",str(OUT))
