from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import numpy as np, os, hashlib
from pathlib import Path
SRC=Path('/mnt/data/imagegen.png')
OUT=Path('/mnt/data/skeptopus_github_v5')
OUT.mkdir(exist_ok=True)
base=Image.open(SRC).convert('RGB')
# Desktop: exact already-generated editorial artwork, scaled only for GitHub weight.
desktop=base.resize((1800,600),Image.Resampling.LANCZOS)
desktop.save(OUT/'skeptopus-editorial-desktop.webp','WEBP',quality=91,method=6)
desktop.save(OUT/'skeptopus-editorial-desktop.png',optimize=True)
# Mobile layout: recomposes faithful portions of the generated horizontal key art
# rather than shrinking a desktop illustration into an illegible column.
W,H=900,1120
# sophisticated dark teal gradient base, with atmosphere derived from actual generated pixels.
yy,xx=np.mgrid[0:H,0:W]
t=np.clip(xx/W*0.65+yy/H*0.2,0,1)
arr=np.zeros((H,W,3),dtype=np.uint8)
for i,(a,b) in enumerate([(1,6),(37,55),(35,46)]):
    arr[:,:,i]=(a+(b-a)*t+0.0).astype('uint8')
canvas=Image.fromarray(arr,'RGB').convert('RGBA')
# The right-hand generated image contributes atmospheric emerald gradient, no text.
atmo=base.crop((1120,12,1890,705)).resize((900,1120),Image.Resampling.LANCZOS)
atmo=atmo.filter(ImageFilter.GaussianBlur(48))
atmo=ImageEnhance.Brightness(atmo).enhance(0.45).convert('RGBA')
canvas=Image.blend(canvas,atmo,.62)
def feather_paste(crop, box, maskfade=38, radius=0):
    global canvas
    x,y,w,h=box
    cut=base.crop(crop).resize((w,h),Image.Resampling.LANCZOS).convert('RGBA')
    if radius: cut=cut.filter(ImageFilter.GaussianBlur(radius))
    mask=Image.new('L',(w,h),0)
    dr=ImageDraw.Draw(mask)
    dr.rectangle((maskfade,maskfade,w-maskfade,h-maskfade), fill=255)
    mask=mask.filter(ImageFilter.GaussianBlur(maskfade*.75))
    # Make edges soft, core opaque for faithful original pixels.
    canvas.paste(cut,(x,y),mask)
# Native source wordmark, retaining its real letters, treatment and original warm coral.
feather_paste((40,195,1205,480),(28,190,840,252),23)
# Original luminous network, recropped and laid out for a tall viewport.
feather_paste((1175,124,2172,634),(16,478,858,510),22)
# Header & footer authored as layout, source image typography remains inside hero.
draw=ImageDraw.Draw(canvas)
mono='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
font22=ImageFont.truetype(mono,22)
font31=ImageFont.truetype(mono,31)
col=(244,243,234,245); mint=(185,222,203,245); coral=(242,119,105,250)
# Short handmade header consistent with the desktop's label but mobile-sized.
draw.text((52,60),'SYSTASYS / PUBLIC PRODUCT',fill=col,font=font22)
draw.text((52,100),'SKEPTOPUS',fill=mint,font=font22)
draw.line((52,146,847,146),fill=(185,222,203,145),width=2)
# Footer is legible at native GitHub mobile width, uses fewer words, no false proof.
draw.line((52,1016,847,1016),fill=(185,222,203,110),width=2)
draw.text((52,1040),'QUESTION',font=font31,fill=col)
draw.text((253,1040),'/',font=font31,fill=coral)
draw.text((301,1040),'TRACE',font=font31,fill=col)
draw.text((473,1040),'/',font=font31,fill=coral)
draw.text((525,1040),'VERIFY',font=font31,fill=col)
mobile=canvas.convert('RGB')
mobile.save(OUT/'skeptopus-editorial-mobile.webp','WEBP',quality=93,method=6)
mobile.save(OUT/'skeptopus-editorial-mobile.png',optimize=True)
for name in ['skeptopus-editorial-desktop.webp','skeptopus-editorial-mobile.webp']:
    f=OUT/name
    img=Image.open(f)
    print(name,img.size,f.stat().st_size,'sha256',hashlib.sha256(f.read_bytes()).hexdigest())
