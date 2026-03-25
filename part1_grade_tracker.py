From: <Saved by Blink>
Snapshot-Content-Location: https://colab.research.google.com/drive/1Vp3AzLkkB_Z2otMTnqZQERpkb6TgFa4F#scrollTo=T2BNeFUZ1OGZ
Subject: part1_grade_tracker.py - Colab
Date: Wed, 25 Mar 2026 22:28:17 +0530
MIME-Version: 1.0
Content-Type: multipart/related;
	type="text/html";
	boundary="----MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----"


------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/html
Content-ID: <frame-CEDB48DBE387789D04982E80D200B3D2@mhtml.blink>
Content-Transfer-Encoding: quoted-printable
Content-Location: https://colab.research.google.com/drive/1Vp3AzLkkB_Z2otMTnqZQERpkb6TgFa4F#scrollTo=T2BNeFUZ1OGZ

<!DOCTYPE html><html lang=3D"en" theme=3D"light" editor=3D"Default Light"><=
head><meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3DUTF-=
8"><link rel=3D"stylesheet" type=3D"text/css" href=3D"cid:css-dedaa6b4-544a=
-46cc-8eb3-4c7999afa88b@mhtml.blink" /><link rel=3D"stylesheet" type=3D"tex=
t/css" href=3D"cid:css-fe8af014-6e3f-4905-acb4-c630493d54b0@mhtml.blink" />=
<link rel=3D"stylesheet" type=3D"text/css" href=3D"cid:css-4450dfb2-a027-4f=
3b-b8e8-01a5af03fae0@mhtml.blink" /><link rel=3D"stylesheet" type=3D"text/c=
ss" href=3D"cid:css-5ef9603c-81a2-456a-a733-daec7b5f7a34@mhtml.blink" /><li=
nk rel=3D"stylesheet" type=3D"text/css" href=3D"cid:css-9db2c5e4-cdee-48b4-=
8e79-cb55979ed7cd@mhtml.blink" /><link rel=3D"stylesheet" type=3D"text/css"=
 href=3D"cid:css-77556185-66c9-4dd3-b4b8-1957f3a4d71e@mhtml.blink" /><link =
rel=3D"stylesheet" type=3D"text/css" href=3D"cid:css-7f7fccf6-25fb-4460-bb6=
b-4a781765cc8b@mhtml.blink" /><link rel=3D"stylesheet" type=3D"text/css" hr=
ef=3D"cid:css-823da69d-08ed-4725-ac61-1a0a93ff7b1e@mhtml.blink" /><link rel=
=3D"stylesheet" type=3D"text/css" href=3D"cid:css-26d7c64d-9945-4e0d-9372-d=
d06c853e612@mhtml.blink" /><link rel=3D"stylesheet" type=3D"text/css" href=
=3D"cid:css-73d37a7a-4351-48e3-8997-662d892598fd@mhtml.blink" /><meta http-=
equiv=3D"origin-trial" content=3D"A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZT=
nKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczov=
L3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2V=
QYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaX=
NUaGlyZFBhcnR5Ijp0cnVlfQ=3D=3D"><meta http-equiv=3D"origin-trial" content=
=3D"A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW=
7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsIm=
ZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5I=
joxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=3D=3D=
"><meta name=3D"og-profile-acct" content=3D"monsoonpadhy02@gmail.com"><meta=
 name=3D"referrer" content=3D"origin"><meta name=3D"viewport" content=3D"wi=
dth=3Ddevice-width, initial-scale=3D1"><title>part1_grade_tracker.py - Cola=
b</title><link href=3D"https://fonts.googleapis.com/css2?family=3DGoogle+Sy=
mbols:FILL@0..1&amp;display=3Dblock" rel=3D"stylesheet"><link href=3D"https=
://fonts.googleapis.com/css?family=3DRoboto:300,400,500,600,700|Google+Sans=
:300,400,500,600,700|Google+Sans+Text:400,500,700&amp;display=3Dblock" rel=
=3D"stylesheet"><link rel=3D"search" type=3D"application/opensearchdescript=
ion+xml" href=3D"https://colab.research.google.com/opensearch.xml" title=3D=
"Google Colab"><link rel=3D"stylesheet" href=3D"https://ssl.gstatic.com/col=
aboratory-static/common/b8629101fed591b8cb8c96c45ee6f083/v2/external/bundle=
.css"><link id=3D"favicon-link" rel=3D"shortcut icon" href=3D"https://ssl.g=
static.com/colaboratory-static/common/b8629101fed591b8cb8c96c45ee6f083/img%=
2Ffavicon.ico"><meta name=3D"google-site-verification" content=3D"h4AyILcMX=
lXf3PDJKg3Fu2_dyS3jfH5im5G__oDgjOs"><meta name=3D"google-site-verification"=
 content=3D"wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name=3D"goog=
le-site-verification" content=3D"dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAI=
o"><meta name=3D"google-site-verification" content=3D"K1UdZBHJXQYnJGXIK1Kuu=
tmVy6dn3vG2sEyV9D1C6dM"><meta name=3D"google-site-verification" content=3D"=
wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name=3D"google-site-veri=
fication" content=3D"qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta nam=
e=3D"google-site-verification" content=3D"7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-=
gaoUALEYgw"><meta name=3D"google-site-verification" content=3D"PHgaSKwdxZEL=
S21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name=3D"google-site-verification" co=
ntent=3D"qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name=3D"google-=
site-verification" content=3D"gl3hNNVi7GnXImkDiRAkUxkhUD4g7Ke8L4D6Ve8FEVY">=
<meta name=3D"google-site-verification" content=3D"BQfukMqFy1nu2Q2gjGbNTDA8=
MJ_Y4L2brCYA1h6ewkY"><meta name=3D"google-site-verification" content=3D"pIZ=
q7V_Vt54MAfdQe5afm8zeJrl3o4GkRW-etNvnlKI"><meta name=3D"google-site-verific=
ation" content=3D"Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name=
=3D"google-site-verification" content=3D"z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWU=
S2Uej5pwg"><meta name=3D"google-site-verification" content=3D"rF5iXzWe9KZXJ=
es1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name=3D"google-site-verification" con=
tent=3D"vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name=3D"google-s=
ite-verification" content=3D"cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><=
meta name=3D"google-site-verification" content=3D"b6bOMRzMVX2bJABYDGBPtpGcB=
_AUZ-o2SOTggQXErkg"><meta name=3D"google-site-verification" content=3D"88fg=
sZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name=3D"google-site-verifica=
tion" content=3D"hZkpVtQ8gdGznkTfUekRWeGY05QyeLXb6q946CFw2-c"><meta name=3D=
"google-site-verification" content=3D"sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4R=
EpQPGY"><meta name=3D"google-site-verification" content=3D"26aKGBCw3XblB5Ou=
01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name=3D"google-site-verification" conten=
t=3D"DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name=3D"google-site=
-verification" content=3D"Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><met=
a name=3D"google-site-verification" content=3D"rQawcZaTEK_UrDG30cz_7nVKOVvB=
ass61QEes0Tm04g"><meta name=3D"google-site-verification" content=3D"-N1hdki=
HJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name=3D"google-site-verificatio=
n" content=3D"HwWGKCyRK7kxGyAlA30sbbTly9VW0SOM7Sh4juqiOVA"><meta name=3D"go=
ogle-site-verification" content=3D"8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DB=
tGo"><meta name=3D"google-site-verification" content=3D"Gz6pcDgVFH_aS-aPTYW=
21rSHcWl0LAgKCWJtdXPVTNo"><meta name=3D"google-site-verification" content=
=3D"KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name=3D"google-site-=
verification" content=3D"LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta=
 property=3D"og:type" content=3D"article"><meta property=3D"og:image" conte=
nt=3D"https://colab.research.google.com/img/colab_favicon_256px.png"><meta =
property=3D"og:title" content=3D"Google Colab"><meta http-equiv=3D"origin-t=
rial" content=3D"Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3=
huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2Vhc=
mNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBh=
cnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><link type=3D"text/css" href=
=3D"https://www.gstatic.com/og/_/ss/k=3Dog.qtm.vjyYcS7rQwo.L.W.O/m=3Dqcwid,=
qba,d_b_gm3,d_wi_gm3,d_lo_gm3/excm=3Dqaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhc=
h,qhga,qhid,qhin/d=3D1/ed=3D1/ct=3Dzgms/rs=3DAA2YrTtEJMqNNb04d2z46AITatL-Y6=
6Oww" rel=3D"stylesheet"><link rel=3D"stylesheet" type=3D"text/css" data-na=
me=3D"vs/editor/editor.main" href=3D"https://ssl.gstatic.com/colaboratory-s=
tatic/common/b8629101fed591b8cb8c96c45ee6f083/js%2Fmonaco_editor%2F/vs/edit=
or/editor.main.css"><link type=3D"text/css" rel=3D"stylesheet" href=3D"chro=
me-extension://fheoggkfdfchfphceeifdbepaooicaho/css/mcafee_fonts.css"></hea=
d><body class=3D"" data-new-gr-c-s-check-loaded=3D"14.1278.0" data-gr-ext-i=
nstalled=3D"" data-new-gr-c-s-loaded=3D"14.1278.0" style=3D"overscroll-beha=
vior: contain;"><div style=3D"visibility: hidden; overflow: hidden; positio=
n: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px;=
 margin: 0px; text-align: left; text-indent: 0px; text-transform: none; lin=
e-height: normal; letter-spacing: normal; word-spacing: normal;"><div id=3D=
"MathJax_Hidden"></div></div><div id=3D"MathJax_Message" style=3D"display: =
none;"></div><div class=3D"scripts"></div><colab-snackbar leading=3D"" labe=
ltext=3D"" id=3D"message-area" class=3D"message-area"><template shadowmode=
=3D"open"><!---->
      <!--?lit$516311766$-->
      <div class=3D"mdc-snackbar mdc-snackbar--leading">
        <div class=3D"mdc-snackbar__surface">
          <!--?lit$516311766$-->
          <div class=3D"mdc-snackbar__actions">
            <slot name=3D"action"></slot>
            <slot name=3D"dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class=3D"close" slot=3D"dismiss" title=3D"Close" data=
-aria-label=3D"Close" value=3D""><template shadowmode=3D"open" shadowdelega=
tesfocus=3D""><!----><button id=3D"button" class=3D"icon-button  standard "=
 aria-label=3D"Close">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
        <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!---->=
<slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading=3D"" labeltext=3D"" id=3D"mess=
age-area-secondary" class=3D"message-area"><template shadowmode=3D"open"><!=
---->
      <!--?lit$516311766$-->
      <div class=3D"mdc-snackbar mdc-snackbar--leading">
        <div class=3D"mdc-snackbar__surface">
          <!--?lit$516311766$-->
          <div class=3D"mdc-snackbar__actions">
            <slot name=3D"action"></slot>
            <slot name=3D"dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class=3D"close" slot=3D"dismiss" title=3D"Close" data=
-aria-label=3D"Close" value=3D""><template shadowmode=3D"open" shadowdelega=
tesfocus=3D""><!----><button id=3D"button" class=3D"icon-button  standard "=
 aria-label=3D"Close">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
        <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!---->=
<slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=3D""></div><div class=3D"gb_T" ng=
-non-bindable=3D""><div class=3D"gb_Rc"><div>Google Account</div><div class=
=3D"gb_g">monsoon padhy</div><div>monsoonpadhy02@gmail.com</div><div class=
=3D"gb_Sc"></div></div></div><div style=3D"position: absolute; width: 0px; =
height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><di=
v id=3D"MathJax_Font_Test" style=3D"position: absolute; visibility: hidden;=
 top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding=
: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; tex=
t-indent: 0px; text-transform: none; line-height: normal; letter-spacing: n=
ormal; word-spacing: normal; font-size: 40px; font-weight: normal; font-sty=
le: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"=
></div></div><iframe id=3D"hfcr" src=3D"cid:frame-05FCC2522AA7309086A7993BE=
8A24149@mhtml.blink" style=3D"display: none;"></iframe><div class=3D"notebo=
ok-vertical" style=3D"position: relative;">
      <!--?lit$516311766$--><colab-skip-link><template shadowmode=3D"open">=
<!----><md-elevated-button class=3D"link" href=3D"#notebook-main" value=3D"=
"><template shadowmode=3D"open" shadowdelegatesfocus=3D""><!---->
      <!--?lit$516311766$--><md-elevation part=3D"elevation" aria-hidden=3D=
"true"><template shadowmode=3D"open"><!----><span class=3D"shadow"></span><=
/template></md-elevation>
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"link" aria-hidden=3D"true">=
<template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"link" aria-hidden=3D"true"><templat=
e shadowmode=3D"open"><!----><div class=3D"surface   "></div></template></m=
d-ripple>
      <!--?lit$516311766$--><a id=3D"link" class=3D"button" href=3D"https:/=
/colab.research.google.com/drive/1Vp3AzLkkB_Z2otMTnqZQERpkb6TgFa4F#notebook=
-main"><!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </a>
    </template><!--?lit$516311766$-->Skip to main content</md-elevated-butt=
on></template></colab-skip-link>
      <div class=3D"top-floater"><div role=3D"banner">
    <!--?lit$516311766$-->
    <!--?lit$516311766$-->
         =20
       =20
    <!--?lit$516311766$--> <!--?lit$516311766$-->
   =20
 =20
    <!--?lit$516311766$-->

    <div id=3D"header" class=3D"horizontal layout">
      <div id=3D"header-background"><div></div></div>
      <div id=3D"header-content">
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><div id=3D"header-logo">
              <!--?lit$516311766$--><!--?lit$516311766$--><a href=3D"https:=
//drive.google.com/drive/search?q=3Downer%3Ame%20(type%3Aapplication%2Fvnd.=
google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;a=
uthuser=3D0" aria-label=3D"View in Google Drive">
        <!--?lit$516311766$--><md-icon class=3D"colab-large-icon" aria-hidd=
en=3D"true"><template shadowmode=3D"open"><!----><slot></slot></template><!=
--?lit$516311766$--><svg viewBox=3D"0 0 24 24"><!--?lit$516311766$-->
      <g id=3D"colab-logo">
        <path d=3D"M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.5=
9,3.59,0,0,1,4.54,9.46Z" style=3D"fill:var(--colab-logo-dark)"></path>
        <path d=3D"M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-=
.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style=3D"fill:var(--colab-logo-light)">=
</path>
        <path d=3D"M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16=
.9a6.93,6.93,0,0,0,9,.65l.11-.09" style=3D"fill:var(--colab-logo-light)"></=
path>
        <path d=3D"M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1=
,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style=3D"fill:var(--colab-log=
o-light)"></path>
        <path d=3D"M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A=
6.93,6.93,0,0,0,21.81,7.1Z" style=3D"fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id=3D"header-doc-toolbar" class=3D"flex">
          <div id=3D"document-info">
            <!--?lit$516311766$--><!--?lit$516311766$--><md-icon class=3D"f=
ile-location-icon" id=3D"file-type" aria-hidden=3D"true" title=3D"Notebook =
stored in Google Drive"><template shadowmode=3D"open"><!----><slot></slot><=
/template><!--?lit$516311766$-->
      <svg viewBox=3D"0 0 192 192">
        <path d=3D"M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.=
55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.3=
3,122z" fill=3D"#EA4335"></path>
        <path d=3D"M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6=
.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18=
.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48=
,18.41z" fill=3D"#188038"></path>
        <path d=3D"M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29=
.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill=
=3D"#1967D2"></path>
        <path d=3D"M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l=
32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill=3D"#FBBC04"></path>=
<path d=3D"M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61=
c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill=3D"#4285F4"></path>
        <path d=3D"M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83=
,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill=3D"#34A853"></path>
      </svg></md-icon>
    <input id=3D"doc-name" class=3D"doc-name" maxlength=3D"259" autocomplet=
e=3D"off" aria-label=3D"Notebook name" command=3D"rename" aria-describedby=
=3D"doc-name-tooltip" fdprocessedid=3D"wpeptn" style=3D"width: 193.125px;">=
<colab-tooltip-trigger aria-hidden=3D"true" for=3D"doc-name" id=3D"doc-name=
-tooltip"><template shadowmode=3D"open"><!----><!--?lit$516311766$--><!----=
><div><!--?lit$516311766$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden=3D"true" sty=
le=3D"left: -1000%; position: absolute; font-family: &quot;Google Sans&quot=
;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spac=
ing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">part=
1_grade_tracker.py_</colab-input-sizer>
            <!--?lit$516311766$-->
                  <md-icon-button id=3D"star-icon" command=3D"toggle-star" =
aria-describedby=3D"star-icon-tooltip" data-aria-label=3D"Star" value=3D"">=
<template shadowmode=3D"open" shadowdelegatesfocus=3D""><!----><button id=
=3D"button" class=3D"icon-button  standard " aria-label=3D"Star">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface"></div></template></md-ripple=
>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
                    <md-icon aria-hidden=3D"true"><template shadowmode=3D"o=
pen"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden=3D"tr=
ue" for=3D"star-icon" id=3D"star-icon-tooltip"><template shadowmode=3D"open=
"><!----><!--?lit$516311766$--><!----><div><!--?lit$516311766$-->Star noteb=
ook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
               =20
            <!--?lit$516311766$--><colab-last-saved-indicator aria-live=3D"=
polite" aria-atomic=3D"true"><template shadowmode=3D"open"><!----><!--?--><=
/template></colab-last-saved-indicator>
          </div>
        <div class=3D"menubar-wrapper"><div><!----><div id=3D"top-menubar" =
class=3D"goog-menubar format-lightborder" role=3D"menubar" tabindex=3D"0" s=
tyle=3D"user-select: none;"><!--?lit$516311766$--><div class=3D"goog-menu-b=
utton goog-inline-block" id=3D"file-menu-button" role=3D"button" aria-expan=
ded=3D"false" aria-haspopup=3D"true" style=3D"user-select: none;"><div clas=
s=3D"goog-inline-block goog-menu-button-outer-box" style=3D"user-select: no=
ne;"><div class=3D"goog-inline-block goog-menu-button-inner-box" style=3D"u=
ser-select: none;"><div class=3D"goog-inline-block goog-menu-button-caption=
" style=3D"user-select: none;"><!--?lit$516311766$-->File</div><div class=
=3D"goog-inline-block goog-menu-button-dropdown" style=3D"user-select: none=
;">&nbsp;</div></div></div></div><div class=3D"goog-menu-button goog-inline=
-block" id=3D"edit-menu-button" role=3D"button" aria-expanded=3D"false" ari=
a-haspopup=3D"true" style=3D"user-select: none;"><div class=3D"goog-inline-=
block goog-menu-button-outer-box" style=3D"user-select: none;"><div class=
=3D"goog-inline-block goog-menu-button-inner-box" style=3D"user-select: non=
e;"><div class=3D"goog-inline-block goog-menu-button-caption" style=3D"user=
-select: none;"><!--?lit$516311766$-->Edit</div><div class=3D"goog-inline-b=
lock goog-menu-button-dropdown" style=3D"user-select: none;">&nbsp;</div></=
div></div></div><div class=3D"goog-menu-button goog-inline-block" id=3D"vie=
w-menu-button" role=3D"button" aria-expanded=3D"false" aria-haspopup=3D"tru=
e" style=3D"user-select: none;"><div class=3D"goog-inline-block goog-menu-b=
utton-outer-box" style=3D"user-select: none;"><div class=3D"goog-inline-blo=
ck goog-menu-button-inner-box" style=3D"user-select: none;"><div class=3D"g=
oog-inline-block goog-menu-button-caption" style=3D"user-select: none;"><!-=
-?lit$516311766$-->View</div><div class=3D"goog-inline-block goog-menu-butt=
on-dropdown" style=3D"user-select: none;">&nbsp;</div></div></div></div><di=
v class=3D"goog-menu-button goog-inline-block" id=3D"insert-menu-button" ro=
le=3D"button" aria-expanded=3D"false" aria-haspopup=3D"true" style=3D"user-=
select: none;"><div class=3D"goog-inline-block goog-menu-button-outer-box" =
style=3D"user-select: none;"><div class=3D"goog-inline-block goog-menu-butt=
on-inner-box" style=3D"user-select: none;"><div class=3D"goog-inline-block =
goog-menu-button-caption" style=3D"user-select: none;"><!--?lit$516311766$-=
->Insert</div><div class=3D"goog-inline-block goog-menu-button-dropdown" st=
yle=3D"user-select: none;">&nbsp;</div></div></div></div><div class=3D"goog=
-menu-button goog-inline-block" id=3D"runtime-menu-button" role=3D"button" =
aria-expanded=3D"false" aria-haspopup=3D"true" style=3D"user-select: none;"=
><div class=3D"goog-inline-block goog-menu-button-outer-box" style=3D"user-=
select: none;"><div class=3D"goog-inline-block goog-menu-button-inner-box" =
style=3D"user-select: none;"><div class=3D"goog-inline-block goog-menu-butt=
on-caption" style=3D"user-select: none;"><!--?lit$516311766$-->Runtime</div=
><div class=3D"goog-inline-block goog-menu-button-dropdown" style=3D"user-s=
elect: none;">&nbsp;</div></div></div></div><div class=3D"goog-menu-button =
goog-inline-block" id=3D"tools-menu-button" role=3D"button" aria-expanded=
=3D"false" aria-haspopup=3D"true" style=3D"user-select: none;"><div class=
=3D"goog-inline-block goog-menu-button-outer-box" style=3D"user-select: non=
e;"><div class=3D"goog-inline-block goog-menu-button-inner-box" style=3D"us=
er-select: none;"><div class=3D"goog-inline-block goog-menu-button-caption"=
 style=3D"user-select: none;"><!--?lit$516311766$-->Tools</div><div class=
=3D"goog-inline-block goog-menu-button-dropdown" style=3D"user-select: none=
;">&nbsp;</div></div></div></div><div class=3D"goog-menu-button goog-inline=
-block" id=3D"help-menu-button" role=3D"button" aria-expanded=3D"false" ari=
a-haspopup=3D"true" style=3D"user-select: none;"><div class=3D"goog-inline-=
block goog-menu-button-outer-box" style=3D"user-select: none;"><div class=
=3D"goog-inline-block goog-menu-button-inner-box" style=3D"user-select: non=
e;"><div class=3D"goog-inline-block goog-menu-button-caption" style=3D"user=
-select: none;"><!--?lit$516311766$-->Help</div><div class=3D"goog-inline-b=
lock goog-menu-button-dropdown" style=3D"user-select: none;">&nbsp;</div></=
div></div></div></div></div></div></div>
        <div id=3D"header-right">
          <!--?lit$516311766$-->
    <colab-collaborator-bar id=3D"collaborator-bar"><template shadowmode=3D=
"open"><!----> <div class=3D"collaborator-bar">
      <!--?lit$516311766$-->
      <!--?lit$516311766$-->
    </div></template></colab-collaborator-bar>
 =20
          <!--?lit$516311766$--><md-icon-button id=3D"comments" command=3D"=
open-comments-thread" data-aria-label=3D"Open comments pane" aria-described=
by=3D"comments-tooltip" value=3D""><template shadowmode=3D"open" shadowdele=
gatesfocus=3D""><!----><button id=3D"button" class=3D"icon-button  standard=
 " aria-label=3D"Open comments pane">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
                <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"=
><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden=3D"true" =
for=3D"comments" id=3D"comments-tooltip"><template shadowmode=3D"open"><!--=
--><!--?lit$516311766$--><!----><div><!--?lit$516311766$-->Open comments pa=
ne</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$516311766$--><md-icon-button id=3D"settings-cog" command=
=3D"preferences" data-aria-label=3D"Open settings" aria-describedby=3D"sett=
ings-cog-tooltip" value=3D""><template shadowmode=3D"open" shadowdelegatesf=
ocus=3D""><!----><button id=3D"button" class=3D"icon-button  standard " ari=
a-label=3D"Open settings">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
                <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"=
><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden=3D"true" =
for=3D"settings-cog" id=3D"settings-cog-tooltip"><template shadowmode=3D"op=
en"><!----><!--?lit$516311766$--><!----><div><!--?lit$516311766$-->Open set=
tings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$516311766$--><md-filled-tonal-button id=3D"share-toolbar=
-button" command=3D"share" data-aria-label=3D"Share notebook" aria-describe=
dby=3D"share-toolbar-button-tooltip" value=3D"" has-icon=3D""><template sha=
dowmode=3D"open" shadowdelegatesfocus=3D""><!---->
      <!--?lit$516311766$--><md-elevation part=3D"elevation" aria-hidden=3D=
"true"><template shadowmode=3D"open"><!----><span class=3D"shadow"></span><=
/template></md-elevation>
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface   "></div></template><=
/md-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button" aria-lab=
el=3D"Share notebook">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template>
                <md-icon slot=3D"icon" aria-hidden=3D"true"><template shado=
wmode=3D"open"><!----><slot></slot></template><!--?lit$516311766$-->people<=
/md-icon>
                <!--?lit$516311766$-->Share
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden=
=3D"true" for=3D"share-toolbar-button" id=3D"share-toolbar-button-tooltip">=
<template shadowmode=3D"open"><!----><!--?lit$516311766$--><!----><div><!--=
?lit$516311766$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <colab-tooltip-trigger aria-hidden=3D"true" for=3D"show-chat-butt=
on" id=3D"show-chat-button-tooltip"><template shadowmode=3D"open"><!----><!=
--?lit$516311766$--><!----><div><!--?lit$516311766$-->Toggle Gemini</div><!=
----><!--?--></template>
        </colab-tooltip-trigger>
          <div class=3D"header-onegoogle-container"><div class=3D"onegoogle=
"><div class=3D"gb_Ha gb_Dd gb_yb gb_e gb_3a gb_dd" id=3D"gb"><div class=3D=
"gb_2d gb_wb gb_Sd" ng-non-bindable=3D"" data-ogsr-up=3D"" style=3D"padding=
:0;height:auto;display:block"><div class=3D"gb_Cd" style=3D"display:block">=
<div class=3D"gb_jd"></div><div class=3D"gb_z gb_vd gb_Qf gb_1"><div class=
=3D"gb_D gb_vb gb_Qf gb_1"><a class=3D"gb_B gb_0a gb_1" aria-expanded=3D"fa=
lse" aria-label=3D"Google Account: monsoon padhy =20
(monsoonpadhy02@gmail.com)" href=3D"https://accounts.google.com/SignOutOpti=
ons?hl=3Den&amp;continue=3Dhttps://colab.research.google.com/&amp;ec=3DGBRA=
qQM" tabindex=3D"0" role=3D"button"><span class=3D"gb_be"><img class=3D"gb_=
Q gbii" src=3D"https://lh3.googleusercontent.com/ogw/AF2bZyj7ZLC6_dpGKKxNuN=
CNW0BW-Z9huaPIL1m5tzZ74ZdIfX4=3Ds32-c-mo" alt=3D"" aria-hidden=3D"true" dat=
a-noaft=3D"" width=3D"32" height=3D"32"></span><div class=3D"gb_R gb_S" ari=
a-hidden=3D"true"><svg class=3D"gb_La" height=3D"14" viewBox=3D"0 0 14 14" =
width=3D"14" xmlns=3D"http://www.w3.org/2000/svg"><circle class=3D"gb_Ma" c=
x=3D"7" cy=3D"7" r=3D"7"></circle><path class=3D"gb_Oa" d=3D"M6 10H8V12H6V1=
0ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style=3D"ove=
rflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436=
px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: =
4px;"></div><div style=3D"overflow: hidden; position: absolute; top: 0px; v=
isibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 7=
0px; right: 0px; margin-right: 25px;"></div></div></div></div></div>
        </div>
      </div>
    </div>
  </div></div><colab-notebook-toolbar id=3D"top-toolbar" class=3D"horizonta=
l layout center noshrink"><!----> <!--?lit$516311766$-->
    <!--?lit$516311766$--><colab-toolbar-button icon=3D"search" id=3D"toolb=
ar-show-command-palette" command=3D"show-command-palette"><template shadowm=
ode=3D"open"><!----><md-text-button id=3D"button" data-aria-disabled=3D"fal=
se" value=3D"" has-icon=3D""><template shadowmode=3D"open" shadowdelegatesf=
ocus=3D""><!---->
      <!--?lit$516311766$-->
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface"></div></template></md=
-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template>
        <!--?lit$516311766$--><md-icon slot=3D"icon" aria-hidden=3D"true"><=
template shadowmode=3D"open"><!----><slot></slot></template><!--?lit$516311=
766$-->search</md-icon>
        <span class=3D"button-content"><slot></slot></span>
        <!--?lit$516311766$--><span class=3D"screenreader-only"><!--?lit$51=
6311766$-->Show command palette <!--?lit$516311766$-->Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$516311766$--> <colab-tooltip-trigger for=3D"button" aria-hid=
den=3D"true" id=3D"tooltip" message=3D"Show command palette" shortcut=3D"Ct=
rl+Shift+P"><template shadowmode=3D"open"><!----><!--?lit$516311766$--><!--=
--><div><!--?lit$516311766$-->Show command palette (Ctrl+Shift+P)</div><!--=
--><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
          <!--?lit$516311766$-->Commands
        </colab-toolbar-button>
    <!--?lit$516311766$--><span class=3D"toolbar-add-code-split"><colab-too=
lbar-button command=3D"insert-cell-below" icon=3D"add" id=3D"toolbar-add-co=
de" class=3D" split-button "><template shadowmode=3D"open"><!----><md-text-=
button id=3D"button" data-aria-disabled=3D"false" value=3D"" has-icon=3D"">=
<template shadowmode=3D"open" shadowdelegatesfocus=3D""><!---->
      <!--?lit$516311766$-->
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface"></div></template></md=
-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template>
        <!--?lit$516311766$--><md-icon slot=3D"icon" aria-hidden=3D"true"><=
template shadowmode=3D"open"><!----><slot></slot></template><!--?lit$516311=
766$-->add</md-icon>
        <span class=3D"button-content"><slot></slot></span>
        <!--?lit$516311766$--><span class=3D"screenreader-only"><!--?lit$51=
6311766$-->Insert code cell below <!--?lit$516311766$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$516311766$--> <colab-tooltip-trigger for=3D"button" aria-hid=
den=3D"true" id=3D"tooltip" message=3D"Insert code cell below" shortcut=3D"=
Ctrl+M B"><template shadowmode=3D"open"><!----><!--?lit$516311766$--><!----=
><div><!--?lit$516311766$-->Insert code cell below (Ctrl+M B)</div><!----><=
!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
              <!--?lit$516311766$-->Code
            </colab-toolbar-button>
            <!--?lit$516311766$--><md-icon-button touch-target=3D"none" dat=
a-aria-expanded=3D"false" data-aria-haspopup=3D"menu" id=3D"top-toolbar-add=
-code-dropdown-button" data-aria-label=3D"Insert code cell options" value=
=3D""><template shadowmode=3D"open" shadowdelegatesfocus=3D""><!----><butto=
n id=3D"button" class=3D"icon-button  standard " aria-label=3D"Insert code =
cell options" aria-haspopup=3D"menu" aria-expanded=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface"></div></template></md-ripple=
>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template>arrow_drop_down</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden=3D"true" for=3D"top-toolbar-add-code=
-dropdown-button" message=3D"Insert code cell options"><template shadowmode=
=3D"open"><!----><!--?lit$516311766$--><!----><div><!--?lit$516311766$-->In=
sert code cell options</div><!----><!--?--></template>
    </colab-tooltip-trigger></span>
          <colab-toolbar-button command=3D"add-text" icon=3D"add" id=3D"too=
lbar-add-text"><template shadowmode=3D"open"><!----><md-text-button id=3D"b=
utton" data-aria-disabled=3D"false" value=3D"" has-icon=3D""><template shad=
owmode=3D"open" shadowdelegatesfocus=3D""><!---->
      <!--?lit$516311766$-->
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface"></div></template></md=
-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template>
        <!--?lit$516311766$--><md-icon slot=3D"icon" aria-hidden=3D"true"><=
template shadowmode=3D"open"><!----><slot></slot></template><!--?lit$516311=
766$-->add</md-icon>
        <span class=3D"button-content"><slot></slot></span>
        <!--?lit$516311766$--><span class=3D"screenreader-only"><!--?lit$51=
6311766$-->Add text cell <!--?lit$516311766$--></span>
      </md-text-button>
      <!--?lit$516311766$--> <colab-tooltip-trigger for=3D"button" aria-hid=
den=3D"true" id=3D"tooltip" message=3D"Add text cell" shortcut=3D""><templa=
te shadowmode=3D"open"><!----><!--?lit$516311766$--><!----><div><!--?lit$51=
6311766$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$516311766$-->Text
          </colab-toolbar-button>
    <span class=3D"colab-separator"></span>
    <colab-notebook-toolbar-run-button><template shadowmode=3D"open"><!----=
><colab-toolbar-button class=3D"split-button" icon=3D"play_arrow" tooltipid=
=3D"toolbar-run-button-tooltip" id=3D"toolbar-run-button" tooltiptext=3D"Ru=
n all cells in notebook"><template shadowmode=3D"open"><!----><md-text-butt=
on id=3D"button" data-aria-disabled=3D"false" value=3D"" has-icon=3D""><tem=
plate shadowmode=3D"open" shadowdelegatesfocus=3D""><!---->
      <!--?lit$516311766$-->
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface"></div></template></md=
-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template>
        <!--?lit$516311766$--><md-icon slot=3D"icon" aria-hidden=3D"true"><=
template shadowmode=3D"open"><!----><slot></slot></template><!--?lit$516311=
766$-->play_arrow</md-icon>
        <span class=3D"button-content"><slot></slot></span>
        <!--?lit$516311766$--><span class=3D"screenreader-only"><!--?lit$51=
6311766$-->Run all cells in notebook <!--?lit$516311766$--></span>
      </md-text-button>
      <!--?lit$516311766$--> <colab-tooltip-trigger for=3D"button" aria-hid=
den=3D"true" id=3D"toolbar-run-button-tooltip" message=3D"Run all cells in =
notebook" shortcut=3D""><template shadowmode=3D"open"><!----><!--?lit$51631=
1766$--><!----><div><!--?lit$516311766$-->Run all cells in notebook</div><!=
----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$516311766$-->Run all
      </colab-toolbar-button>
      <!--?lit$516311766$--><md-icon-button touch-target=3D"none" data-aria=
-haspopup=3D"menu" data-aria-expanded=3D"false" id=3D"toolbar-run-button-mo=
re-actions" data-aria-label=3D"More actions" value=3D""><template shadowmod=
e=3D"open" shadowdelegatesfocus=3D""><!----><button id=3D"button" class=3D"=
icon-button  standard " aria-label=3D"More actions" aria-haspopup=3D"menu" =
aria-expanded=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
        <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!---->=
<slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden=3D"true" for=3D"toolbar-run-button=
-more-actions" message=3D"More actions"><template shadowmode=3D"open"><!---=
-><!--?lit$516311766$--><!----><div><!--?lit$516311766$-->More actions</div=
><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$516311766$--><md-menu positioning=3D"popover" quick=3D"" ari=
a-labelledby=3D"toolbar-run-button-more-actions" anchor=3D"toolbar-run-butt=
on-more-actions" aria-hidden=3D"true"><template shadowmode=3D"open"><!---->
      <div class=3D"menu   " popover=3D"manual" style=3D"display: none;">
        <!--?lit$516311766$--><md-elevation part=3D"elevation" aria-hidden=
=3D"true"><template shadowmode=3D"open"><!----><span class=3D"shadow"></spa=
n></template></md-elevation>
        <div class=3D"items">
          <div class=3D"item-padding"> <!--?lit$516311766$--><slot></slot> =
</div>
        </div>
      </div>
    </template>
    <!--?lit$516311766$--><!----><md-menu-item command=3D"restart" md-menu-=
item=3D"" tabindex=3D"-1"><template shadowmode=3D"open" shadowdelegatesfocu=
s=3D""><!---->
      <li id=3D"item" role=3D"menuitem" class=3D"list-item" tabindex=3D"0">=
<!--?lit$516311766$-->
      <md-item><template shadowmode=3D"open"><!---->
      <slot name=3D"container"></slot>
      <slot class=3D"non-text" name=3D"start"></slot>
      <div class=3D"text">
        <slot name=3D"overline"></slot>
        <slot class=3D"default-slot"></slot>
        <slot name=3D"headline"></slot>
        <slot name=3D"supporting-text"></slot>
      </div>
      <slot class=3D"non-text" name=3D"trailing-supporting-text"></slot>
      <slot class=3D"non-text" name=3D"end"></slot>
    </template>
        <div slot=3D"container">
          <!--?lit$516311766$--> <md-ripple part=3D"ripple" for=3D"item" ar=
ia-hidden=3D"true"><template shadowmode=3D"open"><!----><div class=3D"surfa=
ce   "></div></template></md-ripple> <!--?lit$516311766$--> <md-focus-ring =
part=3D"focus-ring" for=3D"item" inward=3D"" aria-hidden=3D"true"><template=
 shadowmode=3D"open"><!----></template></md-focus-ring>
        </div>
        <slot name=3D"start" slot=3D"start"></slot>
        <slot name=3D"end" slot=3D"end"></slot>
        <!--?lit$516311766$-->
      <slot></slot>
      <slot name=3D"overline" slot=3D"overline"></slot>
      <slot name=3D"headline" slot=3D"headline"></slot>
      <slot name=3D"supporting-text" slot=3D"supporting-text"></slot>
      <slot name=3D"trailing-supporting-text" slot=3D"trailing-supporting-t=
ext"></slot>
   =20
      </md-item>
    </li>
    </template>
    <span slot=3D"headline"><!--?lit$516311766$-->Restart session</span>
  </md-menu-item><!----><!----><md-menu-item command=3D"restart-and-run-all=
" md-menu-item=3D"" tabindex=3D"-1"><template shadowmode=3D"open" shadowdel=
egatesfocus=3D""><!---->
      <li id=3D"item" role=3D"menuitem" class=3D"list-item" tabindex=3D"0">=
<!--?lit$516311766$-->
      <md-item><template shadowmode=3D"open"><!---->
      <slot name=3D"container"></slot>
      <slot class=3D"non-text" name=3D"start"></slot>
      <div class=3D"text">
        <slot name=3D"overline"></slot>
        <slot class=3D"default-slot"></slot>
        <slot name=3D"headline"></slot>
        <slot name=3D"supporting-text"></slot>
      </div>
      <slot class=3D"non-text" name=3D"trailing-supporting-text"></slot>
      <slot class=3D"non-text" name=3D"end"></slot>
    </template>
        <div slot=3D"container">
          <!--?lit$516311766$--> <md-ripple part=3D"ripple" for=3D"item" ar=
ia-hidden=3D"true"><template shadowmode=3D"open"><!----><div class=3D"surfa=
ce   "></div></template></md-ripple> <!--?lit$516311766$--> <md-focus-ring =
part=3D"focus-ring" for=3D"item" inward=3D"" aria-hidden=3D"true"><template=
 shadowmode=3D"open"><!----></template></md-focus-ring>
        </div>
        <slot name=3D"start" slot=3D"start"></slot>
        <slot name=3D"end" slot=3D"end"></slot>
        <!--?lit$516311766$-->
      <slot></slot>
      <slot name=3D"overline" slot=3D"overline"></slot>
      <slot name=3D"headline" slot=3D"headline"></slot>
      <slot name=3D"supporting-text" slot=3D"supporting-text"></slot>
      <slot name=3D"trailing-supporting-text" slot=3D"trailing-supporting-t=
ext"></slot>
   =20
      </md-item>
    </li>
    </template>
    <span slot=3D"headline"><!--?lit$516311766$-->Restart session and run a=
ll</span>
  </md-menu-item><!----><!----><md-menu-item command=3D"runafter" md-menu-i=
tem=3D"" tabindex=3D"0"><template shadowmode=3D"open" shadowdelegatesfocus=
=3D""><!---->
      <li id=3D"item" role=3D"menuitem" class=3D"list-item   " tabindex=3D"=
0"><!--?lit$516311766$-->
      <md-item><template shadowmode=3D"open"><!---->
      <slot name=3D"container"></slot>
      <slot class=3D"non-text" name=3D"start"></slot>
      <div class=3D"text">
        <slot name=3D"overline"></slot>
        <slot class=3D"default-slot"></slot>
        <slot name=3D"headline"></slot>
        <slot name=3D"supporting-text"></slot>
      </div>
      <slot class=3D"non-text" name=3D"trailing-supporting-text"></slot>
      <slot class=3D"non-text" name=3D"end"></slot>
    </template>
        <div slot=3D"container">
          <!--?lit$516311766$--> <md-ripple part=3D"ripple" for=3D"item" ar=
ia-hidden=3D"true"><template shadowmode=3D"open"><!----><div class=3D"surfa=
ce   "></div></template></md-ripple> <!--?lit$516311766$--> <md-focus-ring =
part=3D"focus-ring" for=3D"item" inward=3D"" aria-hidden=3D"true"><template=
 shadowmode=3D"open"><!----></template></md-focus-ring>
        </div>
        <slot name=3D"start" slot=3D"start"></slot>
        <slot name=3D"end" slot=3D"end"></slot>
        <!--?lit$516311766$-->
      <slot></slot>
      <slot name=3D"overline" slot=3D"overline"></slot>
      <slot name=3D"headline" slot=3D"headline"></slot>
      <slot name=3D"supporting-text" slot=3D"supporting-text"></slot>
      <slot name=3D"trailing-supporting-text" slot=3D"trailing-supporting-t=
ext"></slot>
   =20
      </md-item>
    </li>
    </template>
    <span slot=3D"headline"><!--?lit$516311766$-->Run focused cell and all =
cells below</span>
  </md-menu-item><!----><!----><md-divider><template shadowmode=3D"open"><!=
----></template></md-divider><!----><!----><md-menu-item command=3D"interru=
pt" md-menu-item=3D"" tabindex=3D"-1"><template shadowmode=3D"open" shadowd=
elegatesfocus=3D""><!---->
      <li id=3D"item" role=3D"menuitem" class=3D"list-item" tabindex=3D"0">=
<!--?lit$516311766$-->
      <md-item><template shadowmode=3D"open"><!---->
      <slot name=3D"container"></slot>
      <slot class=3D"non-text" name=3D"start"></slot>
      <div class=3D"text">
        <slot name=3D"overline"></slot>
        <slot class=3D"default-slot"></slot>
        <slot name=3D"headline"></slot>
        <slot name=3D"supporting-text"></slot>
      </div>
      <slot class=3D"non-text" name=3D"trailing-supporting-text"></slot>
      <slot class=3D"non-text" name=3D"end"></slot>
    </template>
        <div slot=3D"container">
          <!--?lit$516311766$--> <md-ripple part=3D"ripple" for=3D"item" ar=
ia-hidden=3D"true"><template shadowmode=3D"open"><!----><div class=3D"surfa=
ce   "></div></template></md-ripple> <!--?lit$516311766$--> <md-focus-ring =
part=3D"focus-ring" for=3D"item" inward=3D"" aria-hidden=3D"true"><template=
 shadowmode=3D"open"><!----></template></md-focus-ring>
        </div>
        <slot name=3D"start" slot=3D"start"></slot>
        <slot name=3D"end" slot=3D"end"></slot>
        <!--?lit$516311766$-->
      <slot></slot>
      <slot name=3D"overline" slot=3D"overline"></slot>
      <slot name=3D"headline" slot=3D"headline"></slot>
      <slot name=3D"supporting-text" slot=3D"supporting-text"></slot>
      <slot name=3D"trailing-supporting-text" slot=3D"trailing-supporting-t=
ext"></slot>
   =20
      </md-item>
    </li>
    </template>
    <span slot=3D"headline"><!--?lit$516311766$-->Interrupt execution</span=
>
  </md-menu-item><!----><!----><md-menu-item command=3D"clear-outputs" md-m=
enu-item=3D"" tabindex=3D"-1"><template shadowmode=3D"open" shadowdelegates=
focus=3D""><!---->
      <li id=3D"item" role=3D"menuitem" class=3D"list-item   " tabindex=3D"=
0"><!--?lit$516311766$-->
      <md-item><template shadowmode=3D"open"><!---->
      <slot name=3D"container"></slot>
      <slot class=3D"non-text" name=3D"start"></slot>
      <div class=3D"text">
        <slot name=3D"overline"></slot>
        <slot class=3D"default-slot"></slot>
        <slot name=3D"headline"></slot>
        <slot name=3D"supporting-text"></slot>
      </div>
      <slot class=3D"non-text" name=3D"trailing-supporting-text"></slot>
      <slot class=3D"non-text" name=3D"end"></slot>
    </template>
        <div slot=3D"container">
          <!--?lit$516311766$--> <md-ripple part=3D"ripple" for=3D"item" ar=
ia-hidden=3D"true"><template shadowmode=3D"open"><!----><div class=3D"surfa=
ce   "></div></template></md-ripple> <!--?lit$516311766$--> <md-focus-ring =
part=3D"focus-ring" for=3D"item" inward=3D"" aria-hidden=3D"true"><template=
 shadowmode=3D"open"><!----></template></md-focus-ring>
        </div>
        <slot name=3D"start" slot=3D"start"></slot>
        <slot name=3D"end" slot=3D"end"></slot>
        <!--?lit$516311766$-->
      <slot></slot>
      <slot name=3D"overline" slot=3D"overline"></slot>
      <slot name=3D"headline" slot=3D"headline"></slot>
      <slot name=3D"supporting-text" slot=3D"supporting-text"></slot>
      <slot name=3D"trailing-supporting-text" slot=3D"trailing-supporting-t=
ext"></slot>
   =20
      </md-item>
    </li>
    </template>
    <span slot=3D"headline"><!--?lit$516311766$-->Clear all outputs</span>
  </md-menu-item><!---->
  </md-menu><!--?--><!--?--></template>
    </colab-notebook-toolbar-run-button>
    <!--?lit$516311766$-->
    <!--?lit$516311766$-->
    <!--?lit$516311766$-->
    <!--?lit$516311766$-->
    <!--?lit$516311766$--> <span class=3D"collapsed-options">
          <colab-last-saved-indicator aria-live=3D"polite" aria-atomic=3D"t=
rue"><template shadowmode=3D"open"><!----><!--?--></template></colab-last-s=
aved-indicator>
        </span>

    <span class=3D"flex"></span>
    <!--?lit$516311766$-->
    <!--?lit$516311766$--><colab-connect-warning-button><template shadowmod=
e=3D"open"><!----><!--?lit$516311766$--><!--?--></template></colab-connect-=
warning-button>
    <!--?lit$516311766$--><!--?lit$516311766$--><colab-connect-button><temp=
late shadowmode=3D"open"><!----> <!--?lit$516311766$--> <!--?lit$516311766$=
--><md-icon-button id=3D"connect-icon" class=3D"icon-okay" data-aria-label=
=3D"Focus the last run cell" value=3D""><template shadowmode=3D"open" shado=
wdelegatesfocus=3D""><!----><button id=3D"button" class=3D"icon-button  sta=
ndard " aria-label=3D"Focus the last run cell">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
            <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!-=
---><slot></slot></template><!--?lit$516311766$-->done</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger for=3D"connect-icon" id=3D"connect-icon-to=
oltip" aria-hidden=3D"true" message=3D"Focus the last run cell"><template s=
hadowmode=3D"open"><!----><!--?lit$516311766$--><!----><div><!--?lit$516311=
766$-->Focus the last run cell</div><!----><!--?--></template>
          </colab-tooltip-trigger>
      <colab-toolbar-button id=3D"connect" class=3D"split-button" tooltipid=
=3D"colab-connect-tooltip" tooltiptext=3D"Connected to
Python 3 Google Compute Engine backend
RAM: 1.08 GB/12.67 GB
Disk: 21.20 GB/107.72 GB"><template shadowmode=3D"open"><!----><md-text-but=
ton id=3D"button" value=3D"" data-aria-disabled=3D"false"><template shadowm=
ode=3D"open" shadowdelegatesfocus=3D""><!---->
      <!--?lit$516311766$-->
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface   "></div></template><=
/md-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template>
        <!--?lit$516311766$-->
        <span class=3D"button-content"><slot></slot></span>
        <!--?lit$516311766$--><span class=3D"screenreader-only"><!--?lit$51=
6311766$-->Connected to
Python 3 Google Compute Engine backend
RAM: 1.08 GB/12.67 GB
Disk: 21.20 GB/107.72 GB <!--?lit$516311766$--></span>
      </md-text-button>
      <!--?lit$516311766$--> <colab-tooltip-trigger for=3D"button" aria-hid=
den=3D"true" id=3D"colab-connect-tooltip" message=3D"Connected to
Python 3 Google Compute Engine backend
RAM: 1.08 GB/12.67 GB
Disk: 21.20 GB/107.72 GB" shortcut=3D""><template shadowmode=3D"open"><!---=
-><!--?lit$516311766$--><!----><div><!--?lit$516311766$-->Connected to</div=
><!----><!----><div><!--?lit$516311766$-->Python 3 Google Compute Engine ba=
ckend</div><!----><!----><div><!--?lit$516311766$-->RAM: 1.08 GB/12.67 GB</=
div><!----><!----><div><!--?lit$516311766$-->Disk: 21.20 GB/107.72 GB</div>=
<!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$516311766$--> <div id=3D"connect-button-resource-display">
          <!--?lit$516311766$--><colab-usage-sparkline class=3D"ram" label=
=3D"RAM"><template shadowmode=3D"open"><!---->
      <div class=3D"label"><!--?lit$516311766$-->RAM</div>
      <!--?lit$516311766$-->
      <canvas height=3D"14" width=3D"20"></canvas>
    </template></colab-usage-sparkline>
          <!--?lit$516311766$--><colab-usage-sparkline class=3D"disks" labe=
l=3D"Disk"><template shadowmode=3D"open"><!---->
      <div class=3D"label"><!--?lit$516311766$-->Disk</div>
      <!--?lit$516311766$-->
      <canvas height=3D"14" width=3D"20"></canvas>
    </template></colab-usage-sparkline>
        </div>
      </colab-toolbar-button>
      <!--?lit$516311766$--> <md-icon-button id=3D"connect-dropdown" class=
=3D"connect-dropdown" touch-target=3D"none" data-aria-expanded=3D"false" da=
ta-aria-haspopup=3D"menu" data-aria-label=3D"Additional connection options"=
 value=3D""><template shadowmode=3D"open" shadowdelegatesfocus=3D""><!---->=
<button id=3D"button" class=3D"icon-button  standard " aria-label=3D"Additi=
onal connection options" aria-haspopup=3D"menu" aria-expanded=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
        <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!---->=
<slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for=3D"connect-dropdown" id=3D"connect-dropdow=
n-tooltip" aria-hidden=3D"true" message=3D"Additional connection options"><=
template shadowmode=3D"open"><!----><!--?lit$516311766$--><!----><div><!--?=
lit$516311766$-->Additional connection options</div><!----><!--?--></templa=
te>
      </colab-tooltip-trigger>
      <!--?lit$516311766$--><!--?--></template></colab-connect-button><!--?=
-->
    <!--?lit$516311766$-->
    <span class=3D"collapsed-options">
      <!--?lit$516311766$--> <md-icon-button id=3D"share-button-toolbar" co=
mmand=3D"share" data-aria-label=3D"Share notebook" aria-describedby=3D"shar=
e-button-toolbar-tooltip" value=3D""><template shadowmode=3D"open" shadowde=
legatesfocus=3D""><!----><button id=3D"button" class=3D"icon-button  standa=
rd " aria-label=3D"Share notebook">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
            <md-icon filled=3D"" aria-hidden=3D"true"><template shadowmode=
=3D"open"><!----><slot></slot></template><!--?lit$516311766$-->people</md-i=
con>
          </md-icon-button><colab-tooltip-trigger aria-hidden=3D"true" for=
=3D"share-button-toolbar" id=3D"share-button-toolbar-tooltip"><template sha=
dowmode=3D"open"><!----><!--?lit$516311766$--><!----><div><!--?lit$51631176=
6$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <md-icon-button id=3D"settings-button-toolbar" command=3D"preferences=
" data-aria-label=3D"Open settings" aria-describedby=3D"settings-button-too=
lbar-tooltip" value=3D""><template shadowmode=3D"open" shadowdelegatesfocus=
=3D""><!----><button id=3D"button" class=3D"icon-button  standard " aria-la=
bel=3D"Open settings">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
        <md-icon filled=3D"" aria-hidden=3D"true"><template shadowmode=3D"o=
pen"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden=3D"true" for=3D"s=
ettings-button-toolbar" id=3D"settings-button-toolbar-tooltip"><template sh=
adowmode=3D"open"><!----><!--?lit$516311766$--><!----><div><!--?lit$5163117=
66$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$516311766$-->
      <span class=3D"colab-separator"></span>
    </span>
    <!--?lit$516311766$--><md-icon-button toggle=3D"" command=3D"toggle-hea=
der" id=3D"toggle-header-button" touch-target=3D"none" data-aria-label=3D"T=
oggle header visibility" aria-describedby=3D"toggle-header-button-tooltip" =
value=3D""><template shadowmode=3D"open" shadowdelegatesfocus=3D""><!----><=
button id=3D"button" class=3D"icon-button  standard " aria-label=3D"Toggle =
header visibility" aria-pressed=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
    <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><slo=
t></slot></template>expand_less</md-icon>
    <md-icon slot=3D"selected" aria-hidden=3D"true"><template shadowmode=3D=
"open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden=3D"true" for=3D"toggl=
e-header-button" id=3D"toggle-header-button-tooltip"><template shadowmode=
=3D"open"><!----><!--?lit$516311766$--><!----><div><!--?lit$516311766$-->To=
ggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><div class=
=3D"notebook-horizontal">
        <!--?lit$516311766$--><colab-left-pane role=3D"complementary" aria-=
label=3D"left pane"><!----><div class=3D"colab-left-pane-nib layout vertica=
l" role=3D"toolbar" aria-orientation=3D"vertical">
        <div class=3D"left-pane-top"><!----><div class=3D"left-pane-button"=
>
        <!--?lit$516311766$--><md-icon-button toggle=3D"" command=3D"show-t=
oc-pane" data-aria-label=3D"Table of contents" title=3D"Table of contents" =
value=3D""><template shadowmode=3D"open" shadowdelegatesfocus=3D""><!----><=
button id=3D"button" class=3D"icon-button  standard " aria-label=3D"Table o=
f contents" aria-pressed=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface"></div></template></md-ripple=
>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template><!--?lit$516311766$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$516311766$-->
      </div><!----><div class=3D"left-pane-button">
        <!--?lit$516311766$--><md-icon-button toggle=3D"" command=3D"find" =
data-aria-label=3D"Find and replace" title=3D"Find and replace" value=3D"" =
tabindex=3D"-1"><template shadowmode=3D"open" shadowdelegatesfocus=3D""><!-=
---><button id=3D"button" class=3D"icon-button  standard " aria-label=3D"Fi=
nd and replace" aria-pressed=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface"></div></template></md-ripple=
>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template><!--?lit$516311766$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$516311766$-->
      </div><!----><div class=3D"left-pane-button">
        <!--?lit$516311766$--><md-icon-button toggle=3D"" command=3D"snippe=
ts" data-aria-label=3D"Code snippets" title=3D"Code snippets" value=3D"" ta=
bindex=3D"-1"><template shadowmode=3D"open" shadowdelegatesfocus=3D""><!---=
-><button id=3D"button" class=3D"icon-button  standard " aria-label=3D"Code=
 snippets" aria-pressed=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface"></div></template></md-ripple=
>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template><!--?lit$516311766$-->code</md-icon>
    </md-icon-button> <!--?lit$516311766$-->
      </div><!----><div class=3D"left-pane-button">
        <!--?lit$516311766$--><md-icon-button toggle=3D"" command=3D"show-d=
ata-inspector" data-aria-label=3D"Data inspector" title=3D"Data inspector" =
value=3D"" tabindex=3D"-1"><template shadowmode=3D"open" shadowdelegatesfoc=
us=3D""><!----><button id=3D"button" class=3D"icon-button  standard " aria-=
label=3D"Data inspector" aria-pressed=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template><!--?lit$516311766$-->eye_tracking</md-icon>
    </md-icon-button> <!--?lit$516311766$-->
      </div><!----><div class=3D"left-pane-button">
        <!--?lit$516311766$--><md-icon-button toggle=3D"" command=3D"open-u=
ser-secrets" data-aria-label=3D"Secrets" title=3D"Secrets" value=3D"" tabin=
dex=3D"-1"><template shadowmode=3D"open" shadowdelegatesfocus=3D""><!----><=
button id=3D"button" class=3D"icon-button  standard " aria-label=3D"Secrets=
" aria-pressed=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface"></div></template></md-ripple=
>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template><!--?lit$516311766$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$516311766$-->
      </div><!----><div class=3D"left-pane-button">
        <!--?lit$516311766$--><md-icon-button toggle=3D"" command=3D"show-f=
iles" data-aria-label=3D"Files" title=3D"Files" value=3D"" tabindex=3D"-1">=
<template shadowmode=3D"open" shadowdelegatesfocus=3D""><!----><button id=
=3D"button" class=3D"icon-button  standard " aria-label=3D"Files" aria-pres=
sed=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface"></div></template></md-ripple=
>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template><!--?lit$516311766$-->folder</md-icon>
    </md-icon-button> <!--?lit$516311766$-->
      </div><!----><div class=3D"left-pane-button">
        <!--?lit$516311766$--><md-icon-button toggle=3D"" command=3D"show-d=
ata-explorer" data-aria-label=3D"Data explorer" title=3D"Data explorer" val=
ue=3D"" tabindex=3D"-1"><template shadowmode=3D"open" shadowdelegatesfocus=
=3D""><!----><button id=3D"button" class=3D"icon-button  standard " aria-la=
bel=3D"Data explorer" aria-pressed=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template><!--?lit$516311766$-->table</md-icon>
    </md-icon-button> <!--?lit$516311766$-->
      </div></div>
      </div></colab-left-pane>
        <div class=3D"layout vertical grow">
          <colab-tab-layout-container class=3D"layout horizontal grow flexi=
ble-tabs"><!----> <div class=3D"layout horizontal tab-pane-parent">
      <!--?lit$516311766$--> <div class=3D"layout vertical tab-pane-parent"=
>
      <!--?lit$516311766$--><colab-tab-pane class=3D"layout vertical grow n=
o-header focused" align=3D"horizontal"><!----> <div class=3D"layout vertica=
l grow">
    <div class=3D"tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowmode=3D"open"><!---->
      <div class=3D"tabs">
        <slot></slot>
      </div>
      <md-divider part=3D"divider"><template shadowmode=3D"open"><!----></t=
emplate></md-divider>
    </template><md-primary-tab noink=3D"" title=3D"" aria-labelledby=3D"tab=
-title-ELNTbs7s1OHT" class=3D"selected-tab" md-tab=3D"" active=3D"" tabinde=
x=3D"0"><template shadowmode=3D"open"><!----><div class=3D"button" role=3D"=
presentation">
      <md-focus-ring part=3D"focus-ring" inward=3D"" aria-hidden=3D"true"><=
template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-elevation part=3D"elevation" aria-hidden=3D"true"><template shado=
wmode=3D"open"><!----><span class=3D"shadow"></span></template></md-elevati=
on>
      <md-ripple aria-hidden=3D"true"><template shadowmode=3D"open"><!---->=
<div class=3D"surface   "></div></template></md-ripple>
      <div role=3D"presentation" class=3D"content  has-label stacked ">
        <slot name=3D"icon"></slot>
        <slot></slot>
        <!--?lit$516311766$--><div class=3D"indicator"></div>
      </div>
      <!--?lit$516311766$-->
    </div></template>
          <div class=3D"colab-tab-header"> <!--?lit$516311766$--><div class=
=3D"colab-tab-title">
      <!--?lit$516311766$-->
      <span id=3D"tab-title-ELNTbs7s1OHT"><!--?lit$516311766$--><!--?lit$51=
6311766$-->Notebook<!--?--></span>
    </div> <!--?lit$516311766$--> </div>
        </md-primary-tab></md-tabs>
      <div class=3D"layout grow"></div>
      <div class=3D"tab-pane-header-actions"><!----><!--?lit$516311766$--><=
!--?--></div>
      <!--?lit$516311766$--><md-icon-button data-aria-expanded=3D"false" da=
ta-aria-haspopup=3D"menu" id=3D"tab-pane-0-more-actions-button" data-aria-l=
abel=3D"More tab actions" value=3D""><template shadowmode=3D"open" shadowde=
legatesfocus=3D""><!----><button id=3D"button" class=3D"icon-button  standa=
rd " aria-label=3D"More tab actions" aria-haspopup=3D"menu" aria-expanded=
=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden=3D"true" for=3D"tab-pane-0-more-acti=
ons-button" message=3D"More tab actions"><template shadowmode=3D"open"><!--=
--><!--?lit$516311766$--><!----><div><!--?lit$516311766$-->More tab actions=
</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$516311766$--><md-icon-button id=3D"tab=
-pane-0-close-all-button" data-aria-label=3D"Close all tabs" value=3D""><te=
mplate shadowmode=3D"open" shadowdelegatesfocus=3D""><!----><button id=3D"b=
utton" class=3D"icon-button  standard " aria-label=3D"Close all tabs">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden=3D"true" for=3D"tab-pane-0-close-all=
-button" message=3D"Close all tabs"><template shadowmode=3D"open"><!----><!=
--?lit$516311766$--><!----><div><!--?lit$516311766$-->Close all tabs</div><=
!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class=3D"layout vertical grow tab-pane-container"> <colab-tab clas=
s=3D"layout vertical grow notebook-tab-content selected-tab"><!----> <div c=
lass=3D"overflow-flexbox-workaround">
      <colab-scroller role=3D"main" id=3D"notebook-main" class=3D"notebook-=
container" aria-label=3D"Notebook" tabindex=3D"-1">
        <div class=3D"notebook-scrolling-horizontal-container">
          <div class=3D"notebook-scrolling-horizontal">
            <div class=3D"notebook-content-background">
              <!--?lit$516311766$-->
              <div class=3D"notebook-content ">
                <!--?lit$516311766$--><div class=3D"add-cell">
      <div class=3D"add-cell-buttons">
        <md-outlined-button class=3D"add-code add-button" data-aria-label=
=3D"Add code cell
Ctrl+M B" title=3D"Add code cell
Ctrl+M B" value=3D"" has-icon=3D""><template shadowmode=3D"open" shadowdele=
gatesfocus=3D""><!---->
      <!--?lit$516311766$--><div class=3D"outline"></div>
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface   "></div></template><=
/md-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button" aria-lab=
el=3D"Add code cell
Ctrl+M B">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template>
          <md-icon slot=3D"icon" aria-hidden=3D"true"><template shadowmode=
=3D"open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$516311766$-->Code
        </md-outlined-button>
        <md-outlined-button class=3D"add-text add-button" data-aria-label=
=3D"Add text cell" title=3D"Add text cell" value=3D"" has-icon=3D""><templa=
te shadowmode=3D"open" shadowdelegatesfocus=3D""><!---->
      <!--?lit$516311766$--><div class=3D"outline"></div>
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface   "></div></template><=
/md-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button" aria-lab=
el=3D"Add text cell">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template>
          <md-icon slot=3D"icon" aria-hidden=3D"true"><template shadowmode=
=3D"open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$516311766$-->Text
        </md-outlined-button>
        <!--?lit$516311766$-->
        <!--?lit$516311766$-->
      </div><hr>
    </div>
                <div class=3D"notebook-cell-list"><div class=3D"cell code n=
otebook-cell focused code-has-output" id=3D"cell-T2BNeFUZ1OGZ" tabindex=3D"=
-1" role=3D"region" aria-label=3D"Cell 0: Code cell: " style=3D"opacity: 1;=
"><div class=3D"cell-tag-editor sticky"></div><div class=3D"agent-focus-lab=
el">
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template>spark</md-icon>
      <!--?lit$516311766$-->Gemini
    </div><div class=3D"cell-toolbar sticky"><colab-cell-toolbar><template =
shadowmode=3D"open"><!----><!--?lit$516311766$--><!----> <md-icon-button to=
uch-target=3D"none" aria-describedby=3D"button-move-cell-up-tooltip" data-a=
ria-label=3D"Move cell up
Ctrl+M K" command=3D"move-cell-up" id=3D"button-move-cell-up" value=3D"" so=
ft-disabled=3D""><template shadowmode=3D"open" shadowdelegatesfocus=3D""><!=
----><button id=3D"button" class=3D"icon-button  standard " aria-label=3D"M=
ove cell up
Ctrl+M K" aria-disabled=3D"true">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple disabled=3D"" aria-hidden=3D"true"=
><template shadowmode=3D"open"><!----><div class=3D"surface   "></div></tem=
plate></md-ripple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
        <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!---->=
<slot></slot></template><!--?lit$516311766$-->arrow_upward</md-icon>
        <!--?lit$516311766$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden=3D"true" for=3D"button-move-cell-u=
p" id=3D"button-move-cell-up-tooltip" message=3D"Move cell up
Ctrl+M K"><template shadowmode=3D"open"><!----><!--?lit$516311766$--><!----=
><div><!--?lit$516311766$-->Move cell up</div><!----><!----><div><!--?lit$5=
16311766$-->Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target=
=3D"none" aria-describedby=3D"button-move-cell-down-tooltip" data-aria-labe=
l=3D"Move cell down
Ctrl+M J" command=3D"move-cell-down" id=3D"button-move-cell-down" value=3D"=
" soft-disabled=3D""><template shadowmode=3D"open" shadowdelegatesfocus=3D"=
"><!----><button id=3D"button" class=3D"icon-button  standard " aria-label=
=3D"Move cell down
Ctrl+M J" aria-disabled=3D"true">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple disabled=3D"" aria-hidden=3D"true"=
><template shadowmode=3D"open"><!----><div class=3D"surface   "></div></tem=
plate></md-ripple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
        <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!---->=
<slot></slot></template><!--?lit$516311766$-->arrow_downward</md-icon>
        <!--?lit$516311766$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden=3D"true" for=3D"button-move-cell-d=
own" id=3D"button-move-cell-down-tooltip" message=3D"Move cell down
Ctrl+M J"><template shadowmode=3D"open"><!----><!--?lit$516311766$--><!----=
><div><!--?lit$516311766$-->Move cell down</div><!----><!----><div><!--?lit=
$516311766$-->Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$516311766$--><md-menu =
positioning=3D"popover" quick=3D"" aria-labelledby=3D"ai-menu-anchor-T2BNeF=
UZ1OGZ" anchor=3D"ai-menu-anchor-T2BNeFUZ1OGZ" aria-hidden=3D"true"><templa=
te shadowmode=3D"open"><!---->
      <div class=3D"menu   " popover=3D"manual" style=3D"display: none;">
        <!--?lit$516311766$--><md-elevation part=3D"elevation" aria-hidden=
=3D"true"><template shadowmode=3D"open"><!----><span class=3D"shadow"></spa=
n></template></md-elevation>
        <div class=3D"items">
          <div class=3D"item-padding"> <!--?lit$516311766$--><slot></slot> =
</div>
        </div>
      </div>
    </template>
    <!--?lit$516311766$--><!----><md-menu-item command=3D"generate-code" md=
-menu-item=3D"" tabindex=3D"0"><template shadowmode=3D"open" shadowdelegate=
sfocus=3D""><!---->
      <li id=3D"item" tabindex=3D"0" role=3D"menuitem" class=3D"list-item  =
 "><!--?lit$516311766$-->
      <md-item><template shadowmode=3D"open"><!---->
      <slot name=3D"container"></slot>
      <slot class=3D"non-text" name=3D"start"></slot>
      <div class=3D"text">
        <slot name=3D"overline"></slot>
        <slot class=3D"default-slot"></slot>
        <slot name=3D"headline"></slot>
        <slot name=3D"supporting-text"></slot>
      </div>
      <slot class=3D"non-text" name=3D"trailing-supporting-text"></slot>
      <slot class=3D"non-text" name=3D"end"></slot>
    </template>
        <div slot=3D"container">
          <!--?lit$516311766$--> <md-ripple part=3D"ripple" for=3D"item" ar=
ia-hidden=3D"true"><template shadowmode=3D"open"><!----><div class=3D"surfa=
ce   "></div></template></md-ripple> <!--?lit$516311766$--> <md-focus-ring =
part=3D"focus-ring" for=3D"item" inward=3D"" aria-hidden=3D"true"><template=
 shadowmode=3D"open"><!----></template></md-focus-ring>
        </div>
        <slot name=3D"start" slot=3D"start"></slot>
        <slot name=3D"end" slot=3D"end"></slot>
        <!--?lit$516311766$-->
      <slot></slot>
      <slot name=3D"overline" slot=3D"overline"></slot>
      <slot name=3D"headline" slot=3D"headline"></slot>
      <slot name=3D"supporting-text" slot=3D"supporting-text"></slot>
      <slot name=3D"trailing-supporting-text" slot=3D"trailing-supporting-t=
ext"></slot>
   =20
      </md-item>
    </li>
    </template>
    <span slot=3D"headline"><!--?lit$516311766$-->Generate code</span>
  </md-menu-item><!----><!----><md-menu-item command=3D"explain-cell" md-me=
nu-item=3D"" tabindex=3D"-1"><template shadowmode=3D"open" shadowdelegatesf=
ocus=3D""><!---->
      <li id=3D"item" tabindex=3D"0" role=3D"menuitem" class=3D"list-item  =
 "><!--?lit$516311766$-->
      <md-item><template shadowmode=3D"open"><!---->
      <slot name=3D"container"></slot>
      <slot class=3D"non-text" name=3D"start"></slot>
      <div class=3D"text">
        <slot name=3D"overline"></slot>
        <slot class=3D"default-slot"></slot>
        <slot name=3D"headline"></slot>
        <slot name=3D"supporting-text"></slot>
      </div>
      <slot class=3D"non-text" name=3D"trailing-supporting-text"></slot>
      <slot class=3D"non-text" name=3D"end"></slot>
    </template>
        <div slot=3D"container">
          <!--?lit$516311766$--> <md-ripple part=3D"ripple" for=3D"item" ar=
ia-hidden=3D"true"><template shadowmode=3D"open"><!----><div class=3D"surfa=
ce   "></div></template></md-ripple> <!--?lit$516311766$--> <md-focus-ring =
part=3D"focus-ring" for=3D"item" inward=3D"" aria-hidden=3D"true"><template=
 shadowmode=3D"open"><!----></template></md-focus-ring>
        </div>
        <slot name=3D"start" slot=3D"start"></slot>
        <slot name=3D"end" slot=3D"end"></slot>
        <!--?lit$516311766$-->
      <slot></slot>
      <slot name=3D"overline" slot=3D"overline"></slot>
      <slot name=3D"headline" slot=3D"headline"></slot>
      <slot name=3D"supporting-text" slot=3D"supporting-text"></slot>
      <slot name=3D"trailing-supporting-text" slot=3D"trailing-supporting-t=
ext"></slot>
   =20
      </md-item>
    </li>
    </template>
    <span slot=3D"headline"><!--?lit$516311766$-->Explain code</span>
  </md-menu-item><!----><!----><md-menu-item command=3D"transform-code" md-=
menu-item=3D"" tabindex=3D"-1"><template shadowmode=3D"open" shadowdelegate=
sfocus=3D""><!---->
      <li id=3D"item" tabindex=3D"0" role=3D"menuitem" class=3D"list-item  =
 "><!--?lit$516311766$-->
      <md-item><template shadowmode=3D"open"><!---->
      <slot name=3D"container"></slot>
      <slot class=3D"non-text" name=3D"start"></slot>
      <div class=3D"text">
        <slot name=3D"overline"></slot>
        <slot class=3D"default-slot"></slot>
        <slot name=3D"headline"></slot>
        <slot name=3D"supporting-text"></slot>
      </div>
      <slot class=3D"non-text" name=3D"trailing-supporting-text"></slot>
      <slot class=3D"non-text" name=3D"end"></slot>
    </template>
        <div slot=3D"container">
          <!--?lit$516311766$--> <md-ripple part=3D"ripple" for=3D"item" ar=
ia-hidden=3D"true"><template shadowmode=3D"open"><!----><div class=3D"surfa=
ce   "></div></template></md-ripple> <!--?lit$516311766$--> <md-focus-ring =
part=3D"focus-ring" for=3D"item" inward=3D"" aria-hidden=3D"true"><template=
 shadowmode=3D"open"><!----></template></md-focus-ring>
        </div>
        <slot name=3D"start" slot=3D"start"></slot>
        <slot name=3D"end" slot=3D"end"></slot>
        <!--?lit$516311766$-->
      <slot></slot>
      <slot name=3D"overline" slot=3D"overline"></slot>
      <slot name=3D"headline" slot=3D"headline"></slot>
      <slot name=3D"supporting-text" slot=3D"supporting-text"></slot>
      <slot name=3D"trailing-supporting-text" slot=3D"trailing-supporting-t=
ext"></slot>
   =20
      </md-item>
    </li>
    </template>
    <span slot=3D"headline"><!--?lit$516311766$-->Transform code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target=3D"none" data-aria-haspopup=3D"menu"=
 data-aria-expanded=3D"false" aria-describedby=3D"ai-menu-anchor-T2BNeFUZ1O=
GZ-tooltip" data-aria-label=3D"Available AI features" id=3D"ai-menu-anchor-=
T2BNeFUZ1OGZ" value=3D""><template shadowmode=3D"open" shadowdelegatesfocus=
=3D""><!----><button id=3D"button" class=3D"icon-button  standard " aria-la=
bel=3D"Available AI features" aria-haspopup=3D"menu" aria-expanded=3D"false=
">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
            <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!-=
---><slot></slot></template> pen_spark </md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden=3D"true" for=3D"ai-menu-anchor=
-T2BNeFUZ1OGZ" id=3D"ai-menu-anchor-T2BNeFUZ1OGZ-tooltip" message=3D"Availa=
ble AI features"><template shadowmode=3D"open"><!----><!--?lit$516311766$--=
><!----><div><!--?lit$516311766$-->Available AI features</div><!----><!--?-=
-></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-targ=
et=3D"none" aria-describedby=3D"button-toggle-edit-markdown-tooltip" data-a=
ria-label=3D"Edit" command=3D"toggle-edit-markdown" id=3D"button-toggle-edi=
t-markdown" toggle=3D"" style=3D"display: none;" value=3D""><template shado=
wmode=3D"open" shadowdelegatesfocus=3D""><!----><button id=3D"button" class=
=3D"icon-button  standard " aria-label=3D"Edit" aria-pressed=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
        <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!---->=
<slot></slot></template><!--?lit$516311766$-->edit</md-icon>
        <!--?lit$516311766$--><md-icon slot=3D"selected" aria-hidden=3D"tru=
e"><template shadowmode=3D"open"><!----><slot></slot></template><!--?lit$51=
6311766$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden=3D"true" for=3D"button-toggle-edit=
-markdown" id=3D"button-toggle-edit-markdown-tooltip" message=3D"Edit"><tem=
plate shadowmode=3D"open"><!----><!--?lit$516311766$--><!----><div><!--?lit=
$516311766$-->Edit</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target=
=3D"none" aria-describedby=3D"button-delete-cell-or-selection-tooltip" data=
-aria-label=3D"Delete cell
Ctrl+M D" command=3D"delete-cell-or-selection" id=3D"button-delete-cell-or-=
selection" value=3D""><template shadowmode=3D"open" shadowdelegatesfocus=3D=
""><!----><button id=3D"button" class=3D"icon-button  standard " aria-label=
=3D"Delete cell
Ctrl+M D">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
        <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!---->=
<slot></slot></template><!--?lit$516311766$-->delete</md-icon>
        <!--?lit$516311766$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden=3D"true" for=3D"button-delete-cell=
-or-selection" id=3D"button-delete-cell-or-selection-tooltip" message=3D"De=
lete cell
Ctrl+M D"><template shadowmode=3D"open"><!----><!--?lit$516311766$--><!----=
><div><!--?lit$516311766$-->Delete cell</div><!----><!----><div><!--?lit$51=
6311766$-->Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$516311766$--><md-icon-button =
touch-target=3D"none" data-aria-expanded=3D"false" data-aria-haspopup=3D"me=
nu" aria-describedby=3D"button-more-actions-tooltip" data-aria-label=3D"Mor=
e cell actions" class=3D"cell-toolbar-more" id=3D"button-more-actions" valu=
e=3D""><template shadowmode=3D"open" shadowdelegatesfocus=3D""><!----><butt=
on id=3D"button" class=3D"icon-button  standard " aria-label=3D"More cell a=
ctions" aria-haspopup=3D"menu" aria-expanded=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template><md-icon aria-hidden=3D"true"><template shadowmode=3D=
"open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden=3D"true" for=3D"button-more-action=
s" id=3D"button-more-actions-tooltip" message=3D"More cell actions"><templa=
te shadowmode=3D"open"><!----><!--?lit$516311766$--><!----><div><!--?lit$51=
6311766$-->More cell actions</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div=
><div class=3D"main-content"><div class=3D"cell-contents"><div class=3D"cel=
l-mask"></div><span class=3D"imported-info-area"></span><div class=3D"codec=
ell-input-output">
      <div class=3D"inputarea horizontal layout code">
        <div class=3D"cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class=3D"cell-execution-container">
            <colab-run-button><template shadowmode=3D"open"><!----> <div cl=
ass=3D"cell-execution focused stale hovered">
      <button id=3D"run-button" aria-describedby=3D"run-button-tooltip" ari=
a-label=3D"Run cell" aria-disabled=3D"false">
        <span aria-hidden=3D"true" class=3D"cell-execution-indicator"><!--?=
lit$516311766$-->
<svg xmlns=3D"http://www.w3.org/2000/svg" viewBox=3D"0 0 24 24">
  <!--?lit$516311766$-->
  <mask id=3D"playSymbolMask">
    <rect width=3D"100%" height=3D"100%" fill=3D"white"></rect>
    <polygon points=3D"10,8 17,12 10,16" fill=3D"black"></polygon>
  </mask>
  <circle cx=3D"12" cy=3D"12" r=3D"7.8" mask=3D"url(#playSymbolMask)" id=3D=
"filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$516311766$--><colab-tooltip-trigger for=3D"run-button" id=3D=
"run-button-tooltip" aria-hidden=3D"true" message=3D"Run cell (Ctrl+Enter)
cell might have changed since last executed

executed by monsoon padhy
10:15=E2=80=AFPM (9 minutes ago)
executed in 50.513s"><template shadowmode=3D"open"><!----><!--?lit$51631176=
6$--><!----><div><!--?lit$516311766$-->Run cell (Ctrl+Enter)</div><!----><!=
----><div><!--?lit$516311766$-->cell might have changed since last executed=
</div><!----><!----><br><!----><!----><div><!--?lit$516311766$-->executed b=
y monsoon padhy</div><!----><!----><div><!--?lit$516311766$-->10:15=E2=80=
=AFPM (9 minutes ago)</div><!----><!----><div><!--?lit$516311766$-->execute=
d in 50.513s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$516311766$--><div class=3D"status">
      <div class=3D"execution-count"><!--?lit$516311766$-->[11]</div>
      <!--?lit$516311766$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class=3D"editor flex lazy-editor" style=3D""><div class=3D"edito=
r flex monaco" data-keybinding-context=3D"4" data-mode-id=3D"notebook-pytho=
n" style=3D"height: 3316px; --vscode-editorCodeLens-lineHeight: 16px; --vsc=
ode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSetti=
ngs: &quot;liga&quot; off, &quot;calt&quot; off;"><div class=3D"monaco-edit=
or no-user-select  showUnused showDeprecated vs" role=3D"code" data-uri=3D"=
inmemory://model/3" style=3D"width: 1338px; height: 3316px;"><div data-mprt=
=3D"3" class=3D"overflow-guard" style=3D"width: 1338px; height: 3316px; ove=
rflow: clip;"><div class=3D"margin" role=3D"presentation" aria-hidden=3D"tr=
ue" style=3D"position: absolute; contain: strict; will-change: unset; top: =
0px; height: 3316px; width: 6px;"><div class=3D"glyph-margin" style=3D"left=
: 0px; width: 0px; height: 3316px;"></div><div class=3D"margin-view-zones" =
role=3D"presentation" aria-hidden=3D"true" style=3D"position: absolute;"></=
div><div class=3D"margin-view-overlays" role=3D"presentation" aria-hidden=
=3D"true" style=3D"position: absolute; font-family: monospace, Consolas, &q=
uot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; fon=
t-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-=
settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; heigh=
t: 3316px;"><div style=3D"position:absolute;top:0px;width:100%;height:19px;=
"></div><div style=3D"position:absolute;top:19px;width:100%;height:19px;"><=
/div><div style=3D"position:absolute;top:38px;width:100%;height:19px;"></di=
v><div style=3D"position:absolute;top:57px;width:100%;height:19px;"></div><=
div style=3D"position:absolute;top:76px;width:100%;height:19px;"></div><div=
 style=3D"position:absolute;top:95px;width:100%;height:19px;"></div><div st=
yle=3D"position:absolute;top:114px;width:100%;height:19px;"></div><div styl=
e=3D"position:absolute;top:133px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:152px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:171px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:190px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:209px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:228px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:247px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:266px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:285px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:304px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:323px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:342px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:361px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:380px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:399px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:418px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:437px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:456px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:475px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:494px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:513px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:532px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:551px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:570px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:589px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:608px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:627px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:646px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:665px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:684px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:703px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:722px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:741px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:760px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:779px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:798px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:817px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:836px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:855px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:874px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:893px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:912px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:931px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:950px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:969px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:988px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1007px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1026px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1045px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1064px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1083px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1102px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1121px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1140px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1159px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1178px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1197px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1216px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1235px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1254px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1273px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1292px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1311px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1330px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1349px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1368px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1387px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1406px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1425px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1444px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1463px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1482px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1501px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1520px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1539px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1558px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1577px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1596px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1615px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1634px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1653px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1672px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1691px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1710px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1729px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1748px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1767px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1786px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1805px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1824px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1843px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1862px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1881px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1900px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1919px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1938px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1957px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1976px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1995px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2014px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2033px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2052px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2071px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2090px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2109px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2128px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2147px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2166px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2185px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2204px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2223px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2242px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2261px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2280px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2299px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2318px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2337px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2356px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2375px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2394px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2413px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2432px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2451px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2470px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2489px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2508px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2527px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2546px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2565px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2584px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2603px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2622px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2641px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2660px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2679px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2698px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2717px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2736px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2755px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2774px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2793px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2812px;width:100%;height:19px;"><div class=3D"cur=
rent-line current-line-margin-both" style=3D"width:6px; height:19px;"></div=
></div><div style=3D"position:absolute;top:2831px;width:100%;height:19px;">=
</div><div style=3D"position:absolute;top:2850px;width:100%;height:19px;"><=
/div><div style=3D"position:absolute;top:2869px;width:100%;height:19px;"></=
div><div style=3D"position:absolute;top:2888px;width:100%;height:19px;"></d=
iv><div style=3D"position:absolute;top:2907px;width:100%;height:19px;"></di=
v><div style=3D"position:absolute;top:2926px;width:100%;height:19px;"></div=
><div style=3D"position:absolute;top:2945px;width:100%;height:19px;"></div>=
<div style=3D"position:absolute;top:2964px;width:100%;height:19px;"></div><=
div style=3D"position:absolute;top:2983px;width:100%;height:19px;"></div><d=
iv style=3D"position:absolute;top:3002px;width:100%;height:19px;"></div><di=
v style=3D"position:absolute;top:3021px;width:100%;height:19px;"></div><div=
 style=3D"position:absolute;top:3040px;width:100%;height:19px;"></div><div =
style=3D"position:absolute;top:3059px;width:100%;height:19px;"></div><div s=
tyle=3D"position:absolute;top:3078px;width:100%;height:19px;"></div><div st=
yle=3D"position:absolute;top:3097px;width:100%;height:19px;"></div><div sty=
le=3D"position:absolute;top:3116px;width:100%;height:19px;"></div><div styl=
e=3D"position:absolute;top:3135px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:3154px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:3173px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:3192px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:3211px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:3230px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:3249px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:3268px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:3287px;width:100%;height:19px;"></div></div><div =
class=3D"glyph-margin-widgets" style=3D"position: absolute; top: 0px;"></di=
v></div><div class=3D"monaco-scrollable-element editor-scrollable vs" role=
=3D"presentation" data-mprt=3D"5" style=3D"position: absolute; overflow: hi=
dden; left: 6px; width: 1332px; height: 3316px;"><div class=3D"lines-conten=
t monaco-editor-background" style=3D"position: absolute; overflow: hidden; =
width: 1e+06px; height: 3316px; contain: strict; will-change: unset; top: 0=
px; left: 0px;"><div class=3D"view-overlays" role=3D"presentation" aria-hid=
den=3D"true" style=3D"position: absolute; font-family: monospace, Consolas,=
 &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; =
font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variati=
on-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; w=
idth: 1384px;"><div style=3D"position:absolute;top:0px;width:100%;height:19=
px;"></div><div style=3D"position:absolute;top:19px;width:100%;height:19px;=
"></div><div style=3D"position:absolute;top:38px;width:100%;height:19px;"><=
/div><div style=3D"position:absolute;top:57px;width:100%;height:19px;"></di=
v><div style=3D"position:absolute;top:76px;width:100%;height:19px;"></div><=
div style=3D"position:absolute;top:95px;width:100%;height:19px;"></div><div=
 style=3D"position:absolute;top:114px;width:100%;height:19px;"></div><div s=
tyle=3D"position:absolute;top:133px;width:100%;height:19px;"></div><div sty=
le=3D"position:absolute;top:152px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:171px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:190px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:209px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:228px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:247px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:266px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:285px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:304px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:323px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:342px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:361px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:380px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:399px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:418px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:437px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:456px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:475px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:494px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:513px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:532px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:551px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:570px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:589px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:608px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:627px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:646px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:665px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:684px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:703px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:722px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:741px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:760px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:779px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:798px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:817px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:836px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:855px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:874px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:893px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:912px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:931px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:950px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:969px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:988px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1007px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1026px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1045px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1064px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1083px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1102px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1121px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1140px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1159px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1178px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1197px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1216px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1235px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1254px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1273px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1292px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1311px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1330px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1349px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1368px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1387px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1406px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1425px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1444px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1463px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1482px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1501px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1520px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1539px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1558px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1577px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1596px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1615px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1634px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1653px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1672px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1691px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1710px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1729px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1748px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1767px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1786px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1805px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1824px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1843px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1862px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1881px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1900px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1919px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1938px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1957px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1976px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:1995px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2014px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2033px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2052px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2071px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2090px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2109px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2128px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2147px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2166px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2185px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2204px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2223px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2242px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2261px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2280px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2299px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2318px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2337px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2356px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2375px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2394px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2413px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2432px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2451px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2470px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2489px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2508px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2527px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2546px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2565px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2584px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2603px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2622px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2641px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2660px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2679px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2698px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2717px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2736px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2755px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2774px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2793px;width:100%;height:19px;"></div><div style=
=3D"position:absolute;top:2812px;width:100%;height:19px;"><div class=3D"cur=
rent-line" style=3D"width:1384px; height:19px;"></div></div><div style=3D"p=
osition:absolute;top:2831px;width:100%;height:19px;"></div><div style=3D"po=
sition:absolute;top:2850px;width:100%;height:19px;"></div><div style=3D"pos=
ition:absolute;top:2869px;width:100%;height:19px;"></div><div style=3D"posi=
tion:absolute;top:2888px;width:100%;height:19px;"></div><div style=3D"posit=
ion:absolute;top:2907px;width:100%;height:19px;"></div><div style=3D"positi=
on:absolute;top:2926px;width:100%;height:19px;"></div><div style=3D"positio=
n:absolute;top:2945px;width:100%;height:19px;"></div><div style=3D"position=
:absolute;top:2964px;width:100%;height:19px;"></div><div style=3D"position:=
absolute;top:2983px;width:100%;height:19px;"></div><div style=3D"position:a=
bsolute;top:3002px;width:100%;height:19px;"></div><div style=3D"position:ab=
solute;top:3021px;width:100%;height:19px;"></div><div style=3D"position:abs=
olute;top:3040px;width:100%;height:19px;"></div><div style=3D"position:abso=
lute;top:3059px;width:100%;height:19px;"></div><div style=3D"position:absol=
ute;top:3078px;width:100%;height:19px;"></div><div style=3D"position:absolu=
te;top:3097px;width:100%;height:19px;"></div><div style=3D"position:absolut=
e;top:3116px;width:100%;height:19px;"></div><div style=3D"position:absolute=
;top:3135px;width:100%;height:19px;"></div><div style=3D"position:absolute;=
top:3154px;width:100%;height:19px;"></div><div style=3D"position:absolute;t=
op:3173px;width:100%;height:19px;"></div><div style=3D"position:absolute;to=
p:3192px;width:100%;height:19px;"></div><div style=3D"position:absolute;top=
:3211px;width:100%;height:19px;"></div><div style=3D"position:absolute;top:=
3230px;width:100%;height:19px;"></div><div style=3D"position:absolute;top:3=
249px;width:100%;height:19px;"></div><div style=3D"position:absolute;top:32=
68px;width:100%;height:19px;"></div><div style=3D"position:absolute;top:328=
7px;width:100%;height:19px;"></div></div><div role=3D"presentation" aria-hi=
dden=3D"true" class=3D"view-rulers"><div class=3D"view-ruler" style=3D"widt=
h: 2px; height: 3316px; left: 615.938px;"></div></div><div class=3D"view-zo=
nes" role=3D"presentation" aria-hidden=3D"true" style=3D"position: absolute=
;"></div><div class=3D"view-lines monaco-mouse-cursor-text" role=3D"present=
ation" aria-hidden=3D"true" data-mprt=3D"7" style=3D"position: absolute; fo=
nt-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-we=
ight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &=
quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; lett=
er-spacing: 0px; width: 1384px; height: 3316px;"><div style=3D"top:0px;heig=
ht:19px;" class=3D"view-line"><span><span class=3D"mtk8">#&nbsp;Task&nbsp;1=
:&nbsp;Data&nbsp;Cleaning</span></span></div><div style=3D"top:19px;height:=
19px;" class=3D"view-line"><span><span class=3D"mtk8">#&nbsp;RAW&nbsp;DATA<=
/span></span></div><div style=3D"top:38px;height:19px;" class=3D"view-line"=
><span><span class=3D"mtk1">raw_students&nbsp;=3D&nbsp;</span><span class=
=3D"mtk1 bracket-highlighting-0">[</span></span></div><div style=3D"top:57p=
x;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;=
&nbsp;&nbsp;</span><span class=3D"mtk1 bracket-highlighting-1">{</span><spa=
n class=3D"mtk21">"name"</span><span class=3D"mtk1">:&nbsp;</span><span cla=
ss=3D"mtk21">"&nbsp;&nbsp;ayesha&nbsp;SHARMA&nbsp;&nbsp;"</span><span class=
=3D"mtk1">,&nbsp;</span><span class=3D"mtk21">"roll"</span><span class=3D"m=
tk1">:&nbsp;</span><span class=3D"mtk21">"101"</span><span class=3D"mtk1">,=
&nbsp;</span><span class=3D"mtk21">"marks_str"</span><span class=3D"mtk1">:=
&nbsp;</span><span class=3D"mtk21">"88,&nbsp;72,&nbsp;95,&nbsp;60,&nbsp;78"=
</span><span class=3D"mtk1 bracket-highlighting-1">}</span><span class=3D"m=
tk1">,</span></span></div><div style=3D"top:76px;height:19px;" class=3D"vie=
w-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span cla=
ss=3D"mtk1 bracket-highlighting-1">{</span><span class=3D"mtk21">"name"</sp=
an><span class=3D"mtk1">:&nbsp;</span><span class=3D"mtk21">"ROHIT&nbsp;ver=
ma"</span><span class=3D"mtk1">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<=
/span><span class=3D"mtk21">"roll"</span><span class=3D"mtk1">:&nbsp;</span=
><span class=3D"mtk21">"102"</span><span class=3D"mtk1">,&nbsp;</span><span=
 class=3D"mtk21">"marks_str"</span><span class=3D"mtk1">:&nbsp;</span><span=
 class=3D"mtk21">"55,&nbsp;68,&nbsp;49,&nbsp;72,&nbsp;61"</span><span class=
=3D"mtk1 bracket-highlighting-1">}</span><span class=3D"mtk1">,</span></spa=
n></div><div style=3D"top:95px;height:19px;" class=3D"view-line"><span><spa=
n class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk1 bracket=
-highlighting-1">{</span><span class=3D"mtk21">"name"</span><span class=3D"=
mtk1">:&nbsp;</span><span class=3D"mtk21">"&nbsp;&nbsp;Priya&nbsp;Nair&nbsp=
;&nbsp;"</span><span class=3D"mtk1">,&nbsp;&nbsp;&nbsp;&nbsp;</span><span c=
lass=3D"mtk21">"roll"</span><span class=3D"mtk1">:&nbsp;</span><span class=
=3D"mtk21">"103"</span><span class=3D"mtk1">,&nbsp;</span><span class=3D"mt=
k21">"marks_str"</span><span class=3D"mtk1">:&nbsp;</span><span class=3D"mt=
k21">"91,&nbsp;85,&nbsp;88,&nbsp;94,&nbsp;79"</span><span class=3D"mtk1 bra=
cket-highlighting-1">}</span><span class=3D"mtk1">,</span></span></div><div=
 style=3D"top:114px;height:19px;" class=3D"view-line"><span><span class=3D"=
mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk1 bracket-highlighti=
ng-1">{</span><span class=3D"mtk21">"name"</span><span class=3D"mtk1">:&nbs=
p;</span><span class=3D"mtk21">"karan&nbsp;MEHTA"</span><span class=3D"mtk1=
">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk21">"=
roll"</span><span class=3D"mtk1">:&nbsp;</span><span class=3D"mtk21">"104"<=
/span><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk21">"marks_str"<=
/span><span class=3D"mtk1">:&nbsp;</span><span class=3D"mtk21">"40,&nbsp;55=
,&nbsp;38,&nbsp;62,&nbsp;50"</span><span class=3D"mtk1 bracket-highlighting=
-1">}</span><span class=3D"mtk1">,</span></span></div><div style=3D"top:133=
px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp=
;&nbsp;&nbsp;</span><span class=3D"mtk1 bracket-highlighting-1">{</span><sp=
an class=3D"mtk21">"name"</span><span class=3D"mtk1">:&nbsp;</span><span cl=
ass=3D"mtk21">"&nbsp;Sneha&nbsp;pillai&nbsp;"</span><span class=3D"mtk1">,&=
nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk21">"roll"</span><span clas=
s=3D"mtk1">:&nbsp;</span><span class=3D"mtk21">"105"</span><span class=3D"m=
tk1">,&nbsp;</span><span class=3D"mtk21">"marks_str"</span><span class=3D"m=
tk1">:&nbsp;</span><span class=3D"mtk21">"75,&nbsp;80,&nbsp;70,&nbsp;68,&nb=
sp;85"</span><span class=3D"mtk1 bracket-highlighting-1">}</span><span clas=
s=3D"mtk1">,</span></span></div><div style=3D"top:152px;height:19px;" class=
=3D"view-line"><span><span class=3D"mtk1 bracket-highlighting-0">]</span></=
span></div><div style=3D"top:171px;height:19px;" class=3D"view-line"><span>=
<span></span></span></div><div style=3D"top:190px;height:19px;" class=3D"vi=
ew-line"><span><span class=3D"mtk8">#&nbsp;LOOP&nbsp;THROUGH&nbsp;STUDENTS<=
/span></span></div><div style=3D"top:209px;height:19px;" class=3D"view-line=
"><span><span class=3D"mtk19">for</span><span class=3D"mtk1">&nbsp;student&=
nbsp;</span><span class=3D"mtk6">in</span><span class=3D"mtk1">&nbsp;raw_st=
udents:</span></span></div><div style=3D"top:228px;height:19px;" class=3D"v=
iew-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span>=
</div><div style=3D"top:247px;height:19px;" class=3D"view-line"><span><span=
 class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk8">#&nbsp;=
CLEAN&nbsp;NAME</span></span></div><div style=3D"top:266px;height:19px;" cl=
ass=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;name&n=
bsp;=3D&nbsp;student</span><span class=3D"mtk1 bracket-highlighting-0">[</s=
pan><span class=3D"mtk21">"name"</span><span class=3D"mtk1 bracket-highligh=
ting-0">]</span><span class=3D"mtk1">.strip</span><span class=3D"mtk1 brack=
et-highlighting-0">(</span><span class=3D"mtk1 bracket-highlighting-0">)</s=
pan><span class=3D"mtk1">.title</span><span class=3D"mtk1 bracket-highlight=
ing-0">(</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span><=
/div><div style=3D"top:285px;height:19px;" class=3D"view-line"><span><span =
class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style=3D"to=
p:304px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;=
&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk8">#&nbsp;CONVERT&nbsp;ROLL</spa=
n></span></div><div style=3D"top:323px;height:19px;" class=3D"view-line"><s=
pan><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;roll&nbsp;=3D&nbsp;</span>=
<span class=3D"mtk14">int</span><span class=3D"mtk1 bracket-highlighting-0"=
>(</span><span class=3D"mtk1">student</span><span class=3D"mtk1 bracket-hig=
hlighting-1">[</span><span class=3D"mtk21">"roll"</span><span class=3D"mtk1=
 bracket-highlighting-1">]</span><span class=3D"mtk1 bracket-highlighting-0=
">)</span></span></div><div style=3D"top:342px;height:19px;" class=3D"view-=
line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></di=
v><div style=3D"top:361px;height:19px;" class=3D"view-line"><span><span cla=
ss=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk8">#&nbsp;CONV=
ERT&nbsp;MARKS</span></span></div><div style=3D"top:380px;height:19px;" cla=
ss=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;marks&n=
bsp;=3D&nbsp;</span><span class=3D"mtk14">list</span><span class=3D"mtk1 br=
acket-highlighting-0">(</span><span class=3D"mtk15">map</span><span class=
=3D"mtk1 bracket-highlighting-1">(</span><span class=3D"mtk14">int</span><s=
pan class=3D"mtk1">,&nbsp;student</span><span class=3D"mtk1 bracket-highlig=
hting-2">[</span><span class=3D"mtk21">"marks_str"</span><span class=3D"mtk=
1 bracket-highlighting-2">]</span><span class=3D"mtk1">.split</span><span c=
lass=3D"mtk1 bracket-highlighting-2">(</span><span class=3D"mtk21">",&nbsp;=
"</span><span class=3D"mtk1 bracket-highlighting-2">)</span><span class=3D"=
mtk1 bracket-highlighting-1">)</span><span class=3D"mtk1 bracket-highlighti=
ng-0">)</span></span></div><div style=3D"top:399px;height:19px;" class=3D"v=
iew-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span>=
</div><div style=3D"top:418px;height:19px;" class=3D"view-line"><span><span=
 class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk8">#&nbsp;=
CHECK&nbsp;NAME&nbsp;VALID</span></span></div><div style=3D"top:437px;heigh=
t:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&=
nbsp;valid&nbsp;=3D&nbsp;</span><span class=3D"mtk6">True</span></span></di=
v><div style=3D"top:456px;height:19px;" class=3D"view-line"><span><span cla=
ss=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk19">for</span>=
<span class=3D"mtk1">&nbsp;word&nbsp;</span><span class=3D"mtk6">in</span><=
span class=3D"mtk1">&nbsp;name.split</span><span class=3D"mtk1 bracket-high=
lighting-0">(</span><span class=3D"mtk1 bracket-highlighting-0">)</span><sp=
an class=3D"mtk1">:</span></span></div><div style=3D"top:475px;height:19px;=
" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&n=
bsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk19">if</span><span class=3D"=
mtk1">&nbsp;</span><span class=3D"mtk6">not</span><span class=3D"mtk1">&nbs=
p;word.isalpha</span><span class=3D"mtk1 bracket-highlighting-0">(</span><s=
pan class=3D"mtk1 bracket-highlighting-0">)</span><span class=3D"mtk1">:</s=
pan></span></div><div style=3D"top:494px;height:19px;" class=3D"view-line">=
<span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=
&nbsp;&nbsp;&nbsp;&nbsp;valid&nbsp;=3D&nbsp;</span><span class=3D"mtk6">Fal=
se</span></span></div><div style=3D"top:513px;height:19px;" class=3D"view-l=
ine"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div=
><div style=3D"top:532px;height:19px;" class=3D"view-line"><span><span clas=
s=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk19">if</span><s=
pan class=3D"mtk1">&nbsp;valid:</span></span></div><div style=3D"top:551px;=
height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&n=
bsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk15">print</span>=
<span class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk21">"=
=E2=9C=93&nbsp;Valid&nbsp;name"</span><span class=3D"mtk1 bracket-highlight=
ing-0">)</span></span></div><div style=3D"top:570px;height:19px;" class=3D"=
view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span =
class=3D"mtk19">else</span><span class=3D"mtk1">:</span></span></div><div s=
tyle=3D"top:589px;height:19px;" class=3D"view-line"><span><span class=3D"mt=
k1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"m=
tk15">print</span><span class=3D"mtk1 bracket-highlighting-0">(</span><span=
 class=3D"mtk21">"=E2=9C=97&nbsp;Invalid&nbsp;name"</span><span class=3D"mt=
k1 bracket-highlighting-0">)</span></span></div><div style=3D"top:608px;hei=
ght:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp=
;&nbsp;</span></span></div><div style=3D"top:627px;height:19px;" class=3D"v=
iew-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span c=
lass=3D"mtk8">#&nbsp;PRINT&nbsp;PROFILE</span></span></div><div style=3D"to=
p:646px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;=
&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk15">print</span><span class=3D"m=
tk1 bracket-highlighting-0">(</span><span class=3D"mtk21">"=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D"</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span></=
div><div style=3D"top:665px;height:19px;" class=3D"view-line"><span><span c=
lass=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk15">print</s=
pan><span class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk6=
">f</span><span class=3D"mtk21">"Student&nbsp;:&nbsp;</span><span class=3D"=
mtk1 bracket-highlighting-1">{</span><span class=3D"mtk1">name</span><span =
class=3D"mtk1 bracket-highlighting-1">}</span><span class=3D"mtk21">"</span=
><span class=3D"mtk1 bracket-highlighting-0">)</span></span></div><div styl=
e=3D"top:684px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1"=
>&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk15">print</span><span cla=
ss=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk6">f</span><sp=
an class=3D"mtk21">"Roll&nbsp;No&nbsp;:&nbsp;</span><span class=3D"mtk1 bra=
cket-highlighting-1">{</span><span class=3D"mtk1">roll</span><span class=3D=
"mtk1 bracket-highlighting-1">}</span><span class=3D"mtk21">"</span><span c=
lass=3D"mtk1 bracket-highlighting-0">)</span></span></div><div style=3D"top=
:703px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&=
nbsp;&nbsp;&nbsp;</span><span class=3D"mtk15">print</span><span class=3D"mt=
k1 bracket-highlighting-0">(</span><span class=3D"mtk6">f</span><span class=
=3D"mtk21">"Marks&nbsp;&nbsp;&nbsp;:&nbsp;</span><span class=3D"mtk1 bracke=
t-highlighting-1">{</span><span class=3D"mtk1">marks</span><span class=3D"m=
tk1 bracket-highlighting-1">}</span><span class=3D"mtk21">"</span><span cla=
ss=3D"mtk1 bracket-highlighting-0">)</span></span></div><div style=3D"top:7=
22px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nb=
sp;&nbsp;&nbsp;</span><span class=3D"mtk15">print</span><span class=3D"mtk1=
 bracket-highlighting-0">(</span><span class=3D"mtk21">"=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D"</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span></div=
><div style=3D"top:741px;height:19px;" class=3D"view-line"><span><span></sp=
an></span></div><div style=3D"top:760px;height:19px;" class=3D"view-line"><=
span><span class=3D"mtk8">#&nbsp;FIND&nbsp;ROLL&nbsp;103</span></span></div=
><div style=3D"top:779px;height:19px;" class=3D"view-line"><span><span clas=
s=3D"mtk19">for</span><span class=3D"mtk1">&nbsp;student&nbsp;</span><span =
class=3D"mtk6">in</span><span class=3D"mtk1">&nbsp;raw_students:</span></sp=
an></div><div style=3D"top:798px;height:19px;" class=3D"view-line"><span><s=
pan class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk19">if<=
/span><span class=3D"mtk1">&nbsp;student</span><span class=3D"mtk1 bracket-=
highlighting-0">[</span><span class=3D"mtk21">"roll"</span><span class=3D"m=
tk1 bracket-highlighting-0">]</span><span class=3D"mtk1">&nbsp;=3D=3D&nbsp;=
</span><span class=3D"mtk21">"103"</span><span class=3D"mtk1">:</span></spa=
n></div><div style=3D"top:817px;height:19px;" class=3D"view-line"><span><sp=
an class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name&nbsp=
;=3D&nbsp;student</span><span class=3D"mtk1 bracket-highlighting-0">[</span=
><span class=3D"mtk21">"name"</span><span class=3D"mtk1 bracket-highlightin=
g-0">]</span><span class=3D"mtk1">.strip</span><span class=3D"mtk1 bracket-=
highlighting-0">(</span><span class=3D"mtk1 bracket-highlighting-0">)</span=
></span></div><div style=3D"top:836px;height:19px;" class=3D"view-line"><sp=
an><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</s=
pan><span class=3D"mtk15">print</span><span class=3D"mtk1 bracket-highlight=
ing-0">(</span><span class=3D"mtk1">name.upper</span><span class=3D"mtk1 br=
acket-highlighting-1">(</span><span class=3D"mtk1 bracket-highlighting-1">)=
</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span></div><di=
v style=3D"top:855px;height:19px;" class=3D"view-line"><span><span class=3D=
"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=
=3D"mtk15">print</span><span class=3D"mtk1 bracket-highlighting-0">(</span>=
<span class=3D"mtk1">name.lower</span><span class=3D"mtk1 bracket-highlight=
ing-1">(</span><span class=3D"mtk1 bracket-highlighting-1">)</span><span cl=
ass=3D"mtk1 bracket-highlighting-0">)</span></span></div><div style=3D"top:=
874px;height:19px;" class=3D"view-line"><span><span class=3D"mtk8">#&nbsp;T=
ask&nbsp;2:&nbsp;Marks&nbsp;Analysis</span></span></div><div style=3D"top:8=
93px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">student_n=
ame&nbsp;=3D&nbsp;</span><span class=3D"mtk21">"Ayesha&nbsp;Sharma"</span><=
/span></div><div style=3D"top:912px;height:19px;" class=3D"view-line"><span=
><span class=3D"mtk1">subjects&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=3D&nbsp;</span=
><span class=3D"mtk1 bracket-highlighting-0">[</span><span class=3D"mtk21">=
"Math"</span><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk21">"Phys=
ics"</span><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk21">"CS"</s=
pan><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk21">"English"</spa=
n><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk21">"Chemistry"</spa=
n><span class=3D"mtk1 bracket-highlighting-0">]</span></span></div><div sty=
le=3D"top:931px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1=
">marks&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=3D&nbsp;</span><spa=
n class=3D"mtk1 bracket-highlighting-0">[</span><span class=3D"mtk12">88</s=
pan><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">72</span><span=
 class=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">95</span><span class=3D=
"mtk1">,&nbsp;</span><span class=3D"mtk12">60</span><span class=3D"mtk1">,&=
nbsp;</span><span class=3D"mtk12">78</span><span class=3D"mtk1 bracket-high=
lighting-0">]</span></span></div><div style=3D"top:950px;height:19px;" clas=
s=3D"view-line"><span><span></span></span></div><div style=3D"top:969px;hei=
ght:19px;" class=3D"view-line"><span><span class=3D"mtk8">#&nbsp;PRINT&nbsp=
;SUBJECT&nbsp;+&nbsp;GRADE</span></span></div><div style=3D"top:988px;heigh=
t:19px;" class=3D"view-line"><span><span class=3D"mtk19">for</span><span cl=
ass=3D"mtk1">&nbsp;i&nbsp;</span><span class=3D"mtk6">in</span><span class=
=3D"mtk1">&nbsp;</span><span class=3D"mtk15">range</span><span class=3D"mtk=
1 bracket-highlighting-0">(</span><span class=3D"mtk15">len</span><span cla=
ss=3D"mtk1 bracket-highlighting-1">(</span><span class=3D"mtk1">subjects</s=
pan><span class=3D"mtk1 bracket-highlighting-1">)</span><span class=3D"mtk1=
 bracket-highlighting-0">)</span><span class=3D"mtk1">:</span></span></div>=
<div style=3D"top:1007px;height:19px;" class=3D"view-line"><span><span clas=
s=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;m&nbsp;=3D&nbsp;marks</span><span class=
=3D"mtk1 bracket-highlighting-0">[</span><span class=3D"mtk1">i</span><span=
 class=3D"mtk1 bracket-highlighting-0">]</span></span></div><div style=3D"t=
op:1026px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbs=
p;&nbsp;&nbsp;&nbsp;</span></span></div><div style=3D"top:1045px;height:19p=
x;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;=
</span><span class=3D"mtk19">if</span><span class=3D"mtk1">&nbsp;m&nbsp;&gt=
;=3D&nbsp;</span><span class=3D"mtk12">90</span><span class=3D"mtk1">:</spa=
n></span></div><div style=3D"top:1064px;height:19px;" class=3D"view-line"><=
span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g=
rade&nbsp;=3D&nbsp;</span><span class=3D"mtk21">"A+"</span></span></div><di=
v style=3D"top:1083px;height:19px;" class=3D"view-line"><span><span class=
=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk19">elif</span><=
span class=3D"mtk1">&nbsp;m&nbsp;&gt;=3D&nbsp;</span><span class=3D"mtk12">=
80</span><span class=3D"mtk1">:</span></span></div><div style=3D"top:1102px=
;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&=
nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;grade&nbsp;=3D&nbsp;</span><span class=
=3D"mtk21">"A"</span></span></div><div style=3D"top:1121px;height:19px;" cl=
ass=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span=
><span class=3D"mtk19">elif</span><span class=3D"mtk1">&nbsp;m&nbsp;&gt;=3D=
&nbsp;</span><span class=3D"mtk12">70</span><span class=3D"mtk1">:</span></=
span></div><div style=3D"top:1140px;height:19px;" class=3D"view-line"><span=
><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;grade=
&nbsp;=3D&nbsp;</span><span class=3D"mtk21">"B"</span></span></div><div sty=
le=3D"top:1159px;height:19px;" class=3D"view-line"><span><span class=3D"mtk=
1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk19">elif</span><span cl=
ass=3D"mtk1">&nbsp;m&nbsp;&gt;=3D&nbsp;</span><span class=3D"mtk12">60</spa=
n><span class=3D"mtk1">:</span></span></div><div style=3D"top:1178px;height=
:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&n=
bsp;&nbsp;&nbsp;&nbsp;&nbsp;grade&nbsp;=3D&nbsp;</span><span class=3D"mtk21=
">"C"</span></span></div><div style=3D"top:1197px;height:19px;" class=3D"vi=
ew-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span cl=
ass=3D"mtk19">else</span><span class=3D"mtk1">:</span></span></div><div sty=
le=3D"top:1216px;height:19px;" class=3D"view-line"><span><span class=3D"mtk=
1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;grade&nbsp;=3D&nbsp;</sp=
an><span class=3D"mtk21">"F"</span></span></div><div style=3D"top:1235px;he=
ight:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbs=
p;&nbsp;</span></span></div><div style=3D"top:1254px;height:19px;" class=3D=
"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span=
 class=3D"mtk15">print</span><span class=3D"mtk1 bracket-highlighting-0">(<=
/span><span class=3D"mtk1">subjects</span><span class=3D"mtk1 bracket-highl=
ighting-1">[</span><span class=3D"mtk1">i</span><span class=3D"mtk1 bracket=
-highlighting-1">]</span><span class=3D"mtk1">,&nbsp;</span><span class=3D"=
mtk21">"-"</span><span class=3D"mtk1">,&nbsp;m,&nbsp;</span><span class=3D"=
mtk21">"-"</span><span class=3D"mtk1">,&nbsp;grade</span><span class=3D"mtk=
1 bracket-highlighting-0">)</span></span></div><div style=3D"top:1273px;hei=
ght:19px;" class=3D"view-line"><span><span></span></span></div><div style=
=3D"top:1292px;height:19px;" class=3D"view-line"><span><span class=3D"mtk8"=
>#&nbsp;TOTAL&nbsp;&amp;&nbsp;AVERAGE</span></span></div><div style=3D"top:=
1311px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">total&n=
bsp;=3D&nbsp;</span><span class=3D"mtk15">sum</span><span class=3D"mtk1 bra=
cket-highlighting-0">(</span><span class=3D"mtk1">marks</span><span class=
=3D"mtk1 bracket-highlighting-0">)</span></span></div><div style=3D"top:133=
0px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">avg&nbsp;=
=3D&nbsp;</span><span class=3D"mtk15">round</span><span class=3D"mtk1 brack=
et-highlighting-0">(</span><span class=3D"mtk1">total&nbsp;/&nbsp;</span><s=
pan class=3D"mtk15">len</span><span class=3D"mtk1 bracket-highlighting-1">(=
</span><span class=3D"mtk1">marks</span><span class=3D"mtk1 bracket-highlig=
hting-1">)</span><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">2=
</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span></div><di=
v style=3D"top:1349px;height:19px;" class=3D"view-line"><span><span></span>=
</span></div><div style=3D"top:1368px;height:19px;" class=3D"view-line"><sp=
an><span class=3D"mtk15">print</span><span class=3D"mtk1 bracket-highlighti=
ng-0">(</span><span class=3D"mtk21">"Total:"</span><span class=3D"mtk1">,&n=
bsp;total</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span>=
</div><div style=3D"top:1387px;height:19px;" class=3D"view-line"><span><spa=
n class=3D"mtk15">print</span><span class=3D"mtk1 bracket-highlighting-0">(=
</span><span class=3D"mtk21">"Average:"</span><span class=3D"mtk1">,&nbsp;a=
vg</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span></div><=
div style=3D"top:1406px;height:19px;" class=3D"view-line"><span><span></spa=
n></span></div><div style=3D"top:1425px;height:19px;" class=3D"view-line"><=
span><span class=3D"mtk8">#&nbsp;HIGHEST&nbsp;&amp;&nbsp;LOWEST</span></spa=
n></div><div style=3D"top:1444px;height:19px;" class=3D"view-line"><span><s=
pan class=3D"mtk1">max_marks&nbsp;=3D&nbsp;</span><span class=3D"mtk15">max=
</span><span class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"m=
tk1">marks</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span=
></div><div style=3D"top:1463px;height:19px;" class=3D"view-line"><span><sp=
an class=3D"mtk1">min_marks&nbsp;=3D&nbsp;</span><span class=3D"mtk15">min<=
/span><span class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mt=
k1">marks</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span>=
</div><div style=3D"top:1482px;height:19px;" class=3D"view-line"><span><spa=
n></span></span></div><div style=3D"top:1501px;height:19px;" class=3D"view-=
line"><span><span class=3D"mtk15">print</span><span class=3D"mtk1 bracket-h=
ighlighting-0">(</span><span class=3D"mtk21">"Highest:"</span><span class=
=3D"mtk1">,&nbsp;subjects</span><span class=3D"mtk1 bracket-highlighting-1"=
>[</span><span class=3D"mtk1">marks.index</span><span class=3D"mtk1 bracket=
-highlighting-2">(</span><span class=3D"mtk1">max_marks</span><span class=
=3D"mtk1 bracket-highlighting-2">)</span><span class=3D"mtk1 bracket-highli=
ghting-1">]</span><span class=3D"mtk1">,&nbsp;max_marks</span><span class=
=3D"mtk1 bracket-highlighting-0">)</span></span></div><div style=3D"top:152=
0px;height:19px;" class=3D"view-line"><span><span class=3D"mtk15">print</sp=
an><span class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk21=
">"Lowest:"</span><span class=3D"mtk1">,&nbsp;subjects</span><span class=3D=
"mtk1 bracket-highlighting-1">[</span><span class=3D"mtk1">marks.index</spa=
n><span class=3D"mtk1 bracket-highlighting-2">(</span><span class=3D"mtk1">=
min_marks</span><span class=3D"mtk1 bracket-highlighting-2">)</span><span c=
lass=3D"mtk1 bracket-highlighting-1">]</span><span class=3D"mtk1">,&nbsp;mi=
n_marks</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span></=
div><div style=3D"top:1539px;height:19px;" class=3D"view-line"><span><span>=
</span></span></div><div style=3D"top:1558px;height:19px;" class=3D"view-li=
ne"><span><span class=3D"mtk8">#&nbsp;WHILE&nbsp;LOOP&nbsp;(ADD&nbsp;SUBJEC=
TS)</span></span></div><div style=3D"top:1577px;height:19px;" class=3D"view=
-line"><span><span class=3D"mtk1">count&nbsp;=3D&nbsp;</span><span class=3D=
"mtk12">0</span></span></div><div style=3D"top:1596px;height:19px;" class=
=3D"view-line"><span><span></span></span></div><div style=3D"top:1615px;hei=
ght:19px;" class=3D"view-line"><span><span class=3D"mtk19">while</span><spa=
n class=3D"mtk1">&nbsp;</span><span class=3D"mtk6">True</span><span class=
=3D"mtk1">:</span></span></div><div style=3D"top:1634px;height:19px;" class=
=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sub&nbsp;=
=3D&nbsp;</span><span class=3D"mtk15">input</span><span class=3D"mtk1 brack=
et-highlighting-0">(</span><span class=3D"mtk21">"Enter&nbsp;subject&nbsp;(=
or&nbsp;done):&nbsp;"</span><span class=3D"mtk1 bracket-highlighting-0">)</=
span></span></div><div style=3D"top:1653px;height:19px;" class=3D"view-line=
"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><d=
iv style=3D"top:1672px;height:19px;" class=3D"view-line"><span><span class=
=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk19">if</span><sp=
an class=3D"mtk1">&nbsp;sub.lower</span><span class=3D"mtk1 bracket-highlig=
hting-0">(</span><span class=3D"mtk1 bracket-highlighting-0">)</span><span =
class=3D"mtk1">&nbsp;=3D=3D&nbsp;</span><span class=3D"mtk21">"done"</span>=
<span class=3D"mtk1">:</span></span></div><div style=3D"top:1691px;height:1=
9px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbs=
p;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk19">break</span></span><=
/div><div style=3D"top:1710px;height:19px;" class=3D"view-line"><span><span=
 class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style=3D"t=
op:1729px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbs=
p;&nbsp;&nbsp;&nbsp;m&nbsp;=3D&nbsp;</span><span class=3D"mtk15">input</spa=
n><span class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk21"=
>"Enter&nbsp;marks:&nbsp;"</span><span class=3D"mtk1 bracket-highlighting-0=
">)</span></span></div><div style=3D"top:1748px;height:19px;" class=3D"view=
-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></d=
iv><div style=3D"top:1767px;height:19px;" class=3D"view-line"><span><span c=
lass=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk19">if</span=
><span class=3D"mtk1">&nbsp;</span><span class=3D"mtk6">not</span><span cla=
ss=3D"mtk1">&nbsp;m.isdigit</span><span class=3D"mtk1 bracket-highlighting-=
0">(</span><span class=3D"mtk1 bracket-highlighting-0">)</span><span class=
=3D"mtk1">:</span></span></div><div style=3D"top:1786px;height:19px;" class=
=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nb=
sp;&nbsp;&nbsp;</span><span class=3D"mtk15">print</span><span class=3D"mtk1=
 bracket-highlighting-0">(</span><span class=3D"mtk21">"Invalid&nbsp;marks!=
"</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span></div><d=
iv style=3D"top:1805px;height:19px;" class=3D"view-line"><span><span class=
=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span clas=
s=3D"mtk19">continue</span></span></div><div style=3D"top:1824px;height:19p=
x;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;=
</span></span></div><div style=3D"top:1843px;height:19px;" class=3D"view-li=
ne"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;m&nbsp;=3D&nbsp;</sp=
an><span class=3D"mtk14">int</span><span class=3D"mtk1 bracket-highlighting=
-0">(</span><span class=3D"mtk1">m</span><span class=3D"mtk1 bracket-highli=
ghting-0">)</span></span></div><div style=3D"top:1862px;height:19px;" class=
=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></=
span></div><div style=3D"top:1881px;height:19px;" class=3D"view-line"><span=
><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk19">=
if</span><span class=3D"mtk1">&nbsp;m&nbsp;&lt;&nbsp;</span><span class=3D"=
mtk12">0</span><span class=3D"mtk1">&nbsp;</span><span class=3D"mtk6">or</s=
pan><span class=3D"mtk1">&nbsp;m&nbsp;&gt;&nbsp;</span><span class=3D"mtk12=
">100</span><span class=3D"mtk1">:</span></span></div><div style=3D"top:190=
0px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbs=
p;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk15">print</s=
pan><span class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk2=
1">"Marks&nbsp;must&nbsp;be&nbsp;0-100"</span><span class=3D"mtk1 bracket-h=
ighlighting-0">)</span></span></div><div style=3D"top:1919px;height:19px;" =
class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbs=
p;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk19">continue</span></span></di=
v><div style=3D"top:1938px;height:19px;" class=3D"view-line"><span><span cl=
ass=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style=3D"top:=
1957px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&=
nbsp;&nbsp;&nbsp;subjects.append</span><span class=3D"mtk1 bracket-highligh=
ting-0">(</span><span class=3D"mtk1">sub</span><span class=3D"mtk1 bracket-=
highlighting-0">)</span></span></div><div style=3D"top:1976px;height:19px;"=
 class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;mar=
ks.append</span><span class=3D"mtk1 bracket-highlighting-0">(</span><span c=
lass=3D"mtk1">m</span><span class=3D"mtk1 bracket-highlighting-0">)</span><=
/span></div><div style=3D"top:1995px;height:19px;" class=3D"view-line"><spa=
n><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;count&nbsp;+=3D&nbsp;</span>=
<span class=3D"mtk12">1</span></span></div><div style=3D"top:2014px;height:=
19px;" class=3D"view-line"><span><span></span></span></div><div style=3D"to=
p:2033px;height:19px;" class=3D"view-line"><span><span class=3D"mtk15">prin=
t</span><span class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"=
mtk21">"New&nbsp;subjects&nbsp;added:"</span><span class=3D"mtk1">,&nbsp;co=
unt</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span></div>=
<div style=3D"top:2052px;height:19px;" class=3D"view-line"><span><span clas=
s=3D"mtk15">print</span><span class=3D"mtk1 bracket-highlighting-0">(</span=
><span class=3D"mtk21">"New&nbsp;average:"</span><span class=3D"mtk1">,&nbs=
p;</span><span class=3D"mtk15">round</span><span class=3D"mtk1 bracket-high=
lighting-1">(</span><span class=3D"mtk15">sum</span><span class=3D"mtk1 bra=
cket-highlighting-2">(</span><span class=3D"mtk1">marks</span><span class=
=3D"mtk1 bracket-highlighting-2">)</span><span class=3D"mtk1">/</span><span=
 class=3D"mtk15">len</span><span class=3D"mtk1 bracket-highlighting-2">(</s=
pan><span class=3D"mtk1">marks</span><span class=3D"mtk1 bracket-highlighti=
ng-2">)</span><span class=3D"mtk1">,</span><span class=3D"mtk12">2</span><s=
pan class=3D"mtk1 bracket-highlighting-1">)</span><span class=3D"mtk1 brack=
et-highlighting-0">)</span></span></div><div style=3D"top:2071px;height:19p=
x;" class=3D"view-line"><span><span class=3D"mtk8">#&nbsp;Task&nbsp;3:&nbsp=
;Class&nbsp;Summary</span></span></div><div style=3D"top:2090px;height:19px=
;" class=3D"view-line"><span><span class=3D"mtk1">class_data&nbsp;=3D&nbsp;=
</span><span class=3D"mtk1 bracket-highlighting-0">[</span></span></div><di=
v style=3D"top:2109px;height:19px;" class=3D"view-line"><span><span class=
=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk1 bracket-highli=
ghting-1">(</span><span class=3D"mtk21">"Ayesha&nbsp;Sharma"</span><span cl=
ass=3D"mtk1">,&nbsp;&nbsp;</span><span class=3D"mtk1 bracket-highlighting-2=
">[</span><span class=3D"mtk12">88</span><span class=3D"mtk1">,&nbsp;</span=
><span class=3D"mtk12">72</span><span class=3D"mtk1">,&nbsp;</span><span cl=
ass=3D"mtk12">95</span><span class=3D"mtk1">,&nbsp;</span><span class=3D"mt=
k12">60</span><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">78</=
span><span class=3D"mtk1 bracket-highlighting-2">]</span><span class=3D"mtk=
1 bracket-highlighting-1">)</span><span class=3D"mtk1">,</span></span></div=
><div style=3D"top:2128px;height:19px;" class=3D"view-line"><span><span cla=
ss=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk1 bracket-high=
lighting-1">(</span><span class=3D"mtk21">"Rohit&nbsp;Verma"</span><span cl=
ass=3D"mtk1">,&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk1 bracket-hi=
ghlighting-2">[</span><span class=3D"mtk12">55</span><span class=3D"mtk1">,=
&nbsp;</span><span class=3D"mtk12">68</span><span class=3D"mtk1">,&nbsp;</s=
pan><span class=3D"mtk12">49</span><span class=3D"mtk1">,&nbsp;</span><span=
 class=3D"mtk12">72</span><span class=3D"mtk1">,&nbsp;</span><span class=3D=
"mtk12">61</span><span class=3D"mtk1 bracket-highlighting-2">]</span><span =
class=3D"mtk1 bracket-highlighting-1">)</span><span class=3D"mtk1">,</span>=
</span></div><div style=3D"top:2147px;height:19px;" class=3D"view-line"><sp=
an><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk1 =
bracket-highlighting-1">(</span><span class=3D"mtk21">"Priya&nbsp;Nair"</sp=
an><span class=3D"mtk1">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=
=3D"mtk1 bracket-highlighting-2">[</span><span class=3D"mtk12">91</span><sp=
an class=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">85</span><span class=
=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">88</span><span class=3D"mtk1"=
>,&nbsp;</span><span class=3D"mtk12">94</span><span class=3D"mtk1">,&nbsp;<=
/span><span class=3D"mtk12">79</span><span class=3D"mtk1 bracket-highlighti=
ng-2">]</span><span class=3D"mtk1 bracket-highlighting-1">)</span><span cla=
ss=3D"mtk1">,</span></span></div><div style=3D"top:2166px;height:19px;" cla=
ss=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span>=
<span class=3D"mtk1 bracket-highlighting-1">(</span><span class=3D"mtk21">"=
Karan&nbsp;Mehta"</span><span class=3D"mtk1">,&nbsp;&nbsp;&nbsp;&nbsp;</spa=
n><span class=3D"mtk1 bracket-highlighting-2">[</span><span class=3D"mtk12"=
>40</span><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">55</span=
><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">38</span><span cl=
ass=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">62</span><span class=3D"mt=
k1">,&nbsp;</span><span class=3D"mtk12">50</span><span class=3D"mtk1 bracke=
t-highlighting-2">]</span><span class=3D"mtk1 bracket-highlighting-1">)</sp=
an><span class=3D"mtk1">,</span></span></div><div style=3D"top:2185px;heigh=
t:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&=
nbsp;</span><span class=3D"mtk1 bracket-highlighting-1">(</span><span class=
=3D"mtk21">"Sneha&nbsp;Pillai"</span><span class=3D"mtk1">,&nbsp;&nbsp;&nbs=
p;</span><span class=3D"mtk1 bracket-highlighting-2">[</span><span class=3D=
"mtk12">75</span><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">8=
0</span><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">70</span><=
span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">68</span><span clas=
s=3D"mtk1">,&nbsp;</span><span class=3D"mtk12">85</span><span class=3D"mtk1=
 bracket-highlighting-2">]</span><span class=3D"mtk1 bracket-highlighting-1=
">)</span><span class=3D"mtk1">,</span></span></div><div style=3D"top:2204p=
x;height:19px;" class=3D"view-line"><span><span class=3D"mtk1 bracket-highl=
ighting-0">]</span></span></div><div style=3D"top:2223px;height:19px;" clas=
s=3D"view-line"><span><span></span></span></div><div style=3D"top:2242px;he=
ight:19px;" class=3D"view-line"><span><span class=3D"mtk15">print</span><sp=
an class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk21">"Nam=
e&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&n=
bsp;&nbsp;|&nbsp;Average&nbsp;|&nbsp;Status"</span><span class=3D"mtk1 brac=
ket-highlighting-0">)</span></span></div><div style=3D"top:2261px;height:19=
px;" class=3D"view-line"><span><span class=3D"mtk15">print</span><span clas=
s=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk21">"----------=
------------------------------"</span><span class=3D"mtk1 bracket-highlight=
ing-0">)</span></span></div><div style=3D"top:2280px;height:19px;" class=3D=
"view-line"><span><span></span></span></div><div style=3D"top:2299px;height=
:19px;" class=3D"view-line"><span><span class=3D"mtk1">pass_count&nbsp;=3D&=
nbsp;</span><span class=3D"mtk12">0</span></span></div><div style=3D"top:23=
18px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">fail_coun=
t&nbsp;=3D&nbsp;</span><span class=3D"mtk12">0</span></span></div><div styl=
e=3D"top:2337px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1=
">averages&nbsp;=3D&nbsp;</span><span class=3D"mtk1 bracket-highlighting-0"=
>[</span><span class=3D"mtk1 bracket-highlighting-0">]</span></span></div><=
div style=3D"top:2356px;height:19px;" class=3D"view-line"><span><span></spa=
n></span></div><div style=3D"top:2375px;height:19px;" class=3D"view-line"><=
span><span class=3D"mtk19">for</span><span class=3D"mtk1">&nbsp;name,&nbsp;=
marks&nbsp;</span><span class=3D"mtk6">in</span><span class=3D"mtk1">&nbsp;=
class_data:</span></span></div><div style=3D"top:2394px;height:19px;" class=
=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;avg&nbsp;=
=3D&nbsp;</span><span class=3D"mtk15">round</span><span class=3D"mtk1 brack=
et-highlighting-0">(</span><span class=3D"mtk15">sum</span><span class=3D"m=
tk1 bracket-highlighting-1">(</span><span class=3D"mtk1">marks</span><span =
class=3D"mtk1 bracket-highlighting-1">)</span><span class=3D"mtk1">/</span>=
<span class=3D"mtk15">len</span><span class=3D"mtk1 bracket-highlighting-1"=
>(</span><span class=3D"mtk1">marks</span><span class=3D"mtk1 bracket-highl=
ighting-1">)</span><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk12"=
>2</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span></div><=
div style=3D"top:2413px;height:19px;" class=3D"view-line"><span><span class=
=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;averages.append</span><span class=3D"mtk1=
 bracket-highlighting-0">(</span><span class=3D"mtk1">avg</span><span class=
=3D"mtk1 bracket-highlighting-0">)</span></span></div><div style=3D"top:243=
2px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbs=
p;&nbsp;&nbsp;</span></span></div><div style=3D"top:2451px;height:19px;" cl=
ass=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span=
><span class=3D"mtk19">if</span><span class=3D"mtk1">&nbsp;avg&nbsp;&gt;=3D=
&nbsp;</span><span class=3D"mtk12">60</span><span class=3D"mtk1">:</span></=
span></div><div style=3D"top:2470px;height:19px;" class=3D"view-line"><span=
><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;statu=
s&nbsp;=3D&nbsp;</span><span class=3D"mtk21">"Pass"</span></span></div><div=
 style=3D"top:2489px;height:19px;" class=3D"view-line"><span><span class=3D=
"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pass_count&nbsp;+=3D=
&nbsp;</span><span class=3D"mtk12">1</span></span></div><div style=3D"top:2=
508px;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&n=
bsp;&nbsp;&nbsp;</span><span class=3D"mtk19">else</span><span class=3D"mtk1=
">:</span></span></div><div style=3D"top:2527px;height:19px;" class=3D"view=
-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp=
;&nbsp;status&nbsp;=3D&nbsp;</span><span class=3D"mtk21">"Fail"</span></spa=
n></div><div style=3D"top:2546px;height:19px;" class=3D"view-line"><span><s=
pan class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fail_cou=
nt&nbsp;+=3D&nbsp;</span><span class=3D"mtk12">1</span></span></div><div st=
yle=3D"top:2565px;height:19px;" class=3D"view-line"><span><span class=3D"mt=
k1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style=3D"top:2584px;he=
ight:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbs=
p;&nbsp;</span><span class=3D"mtk15">print</span><span class=3D"mtk1 bracke=
t-highlighting-0">(</span><span class=3D"mtk6">f</span><span class=3D"mtk21=
">"</span><span class=3D"mtk1 bracket-highlighting-1">{</span><span class=
=3D"mtk1">name</span><span class=3D"mtk12">:&lt;18</span><span class=3D"mtk=
1 bracket-highlighting-1">}</span><span class=3D"mtk21">&nbsp;</span><span =
class=3D"mtk1">|</span><span class=3D"mtk21">&nbsp;</span><span class=3D"mt=
k1 bracket-highlighting-1">{</span><span class=3D"mtk1">avg</span><span cla=
ss=3D"mtk12">:^7</span><span class=3D"mtk1 bracket-highlighting-1">}</span>=
<span class=3D"mtk21">&nbsp;</span><span class=3D"mtk1">|</span><span class=
=3D"mtk21">&nbsp;</span><span class=3D"mtk1 bracket-highlighting-1">{</span=
><span class=3D"mtk1">status</span><span class=3D"mtk1 bracket-highlighting=
-1">}</span><span class=3D"mtk21">"</span><span class=3D"mtk1 bracket-highl=
ighting-0">)</span></span></div><div style=3D"top:2603px;height:19px;" clas=
s=3D"view-line"><span><span></span></span></div><div style=3D"top:2622px;he=
ight:19px;" class=3D"view-line"><span><span class=3D"mtk15">print</span><sp=
an class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk21">"Pas=
sed:"</span><span class=3D"mtk1">,&nbsp;pass_count</span><span class=3D"mtk=
1 bracket-highlighting-0">)</span></span></div><div style=3D"top:2641px;hei=
ght:19px;" class=3D"view-line"><span><span class=3D"mtk15">print</span><spa=
n class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk21">"Fail=
ed:"</span><span class=3D"mtk1">,&nbsp;fail_count</span><span class=3D"mtk1=
 bracket-highlighting-0">)</span></span></div><div style=3D"top:2660px;heig=
ht:19px;" class=3D"view-line"><span><span></span></span></div><div style=3D=
"top:2679px;height:19px;" class=3D"view-line"><span><span class=3D"mtk8">#&=
nbsp;TOPPER</span></span></div><div style=3D"top:2698px;height:19px;" class=
=3D"view-line"><span><span class=3D"mtk1">top_avg&nbsp;=3D&nbsp;</span><spa=
n class=3D"mtk15">max</span><span class=3D"mtk1 bracket-highlighting-0">(</=
span><span class=3D"mtk1">averages</span><span class=3D"mtk1 bracket-highli=
ghting-0">)</span></span></div><div style=3D"top:2717px;height:19px;" class=
=3D"view-line"><span><span class=3D"mtk1">topper&nbsp;=3D&nbsp;class_data</=
span><span class=3D"mtk1 bracket-highlighting-0">[</span><span class=3D"mtk=
1">averages.index</span><span class=3D"mtk1 bracket-highlighting-1">(</span=
><span class=3D"mtk1">top_avg</span><span class=3D"mtk1 bracket-highlightin=
g-1">)</span><span class=3D"mtk1 bracket-highlighting-0">]</span><span clas=
s=3D"mtk1 bracket-highlighting-0">[</span><span class=3D"mtk12">0</span><sp=
an class=3D"mtk1 bracket-highlighting-0">]</span></span></div><div style=3D=
"top:2736px;height:19px;" class=3D"view-line"><span><span></span></span></d=
iv><div style=3D"top:2755px;height:19px;" class=3D"view-line"><span><span c=
lass=3D"mtk15">print</span><span class=3D"mtk1 bracket-highlighting-0">(</s=
pan><span class=3D"mtk21">"Topper:"</span><span class=3D"mtk1">,&nbsp;toppe=
r,&nbsp;top_avg</span><span class=3D"mtk1 bracket-highlighting-0">)</span><=
/span></div><div style=3D"top:2774px;height:19px;" class=3D"view-line"><spa=
n><span></span></span></div><div style=3D"top:2793px;height:19px;" class=3D=
"view-line"><span><span class=3D"mtk15">print</span><span class=3D"mtk1 bra=
cket-highlighting-0">(</span><span class=3D"mtk21">"Class&nbsp;Average:"</s=
pan><span class=3D"mtk1">,&nbsp;</span><span class=3D"mtk15">round</span><s=
pan class=3D"mtk1 bracket-highlighting-1">(</span><span class=3D"mtk15">sum=
</span><span class=3D"mtk1 bracket-highlighting-2">(</span><span class=3D"m=
tk1">averages</span><span class=3D"mtk1 bracket-highlighting-2">)</span><sp=
an class=3D"mtk1">/</span><span class=3D"mtk15">len</span><span class=3D"mt=
k1 bracket-highlighting-2">(</span><span class=3D"mtk1">averages</span><spa=
n class=3D"mtk1 bracket-highlighting-2">)</span><span class=3D"mtk1">,</spa=
n><span class=3D"mtk12">2</span><span class=3D"mtk1 bracket-highlighting-1"=
>)</span><span class=3D"mtk1 bracket-highlighting-0">)</span></span></div><=
div style=3D"top:2812px;height:19px;" class=3D"view-line"><span><span class=
=3D"mtk8">#&nbsp;Task&nbsp;4:&nbsp;String&nbsp;Operations</span></span></di=
v><div style=3D"top:2831px;height:19px;" class=3D"view-line"><span><span cl=
ass=3D"mtk1">essay&nbsp;=3D&nbsp;</span><span class=3D"mtk21">"&nbsp;&nbsp;=
python&nbsp;is&nbsp;a&nbsp;versatile&nbsp;language.&nbsp;it&nbsp;supports&n=
bsp;obj</span><span class=3D"mtk21">ect&nbsp;oriented,&nbsp;functional,&nbs=
p;and&nbsp;procedural&nbsp;programmi</span><span class=3D"mtk21">ng.&nbsp;p=
ython&nbsp;is&nbsp;widely&nbsp;used&nbsp;in&nbsp;data&nbsp;science&nbsp;and=
&nbsp;mach</span><span class=3D"mtk21">ine&nbsp;learning.&nbsp;&nbsp;"</spa=
n></span></div><div style=3D"top:2850px;height:19px;" class=3D"view-line"><=
span><span></span></span></div><div style=3D"top:2869px;height:19px;" class=
=3D"view-line"><span><span class=3D"mtk8">#&nbsp;STEP&nbsp;1</span></span><=
/div><div style=3D"top:2888px;height:19px;" class=3D"view-line"><span><span=
 class=3D"mtk1">clean_essay&nbsp;=3D&nbsp;essay.strip</span><span class=3D"=
mtk1 bracket-highlighting-0">(</span><span class=3D"mtk1 bracket-highlighti=
ng-0">)</span></span></div><div style=3D"top:2907px;height:19px;" class=3D"=
view-line"><span><span class=3D"mtk15">print</span><span class=3D"mtk1 brac=
ket-highlighting-0">(</span><span class=3D"mtk21">"Clean:"</span><span clas=
s=3D"mtk1">,&nbsp;clean_essay</span><span class=3D"mtk1 bracket-highlightin=
g-0">)</span></span></div><div style=3D"top:2926px;height:19px;" class=3D"v=
iew-line"><span><span></span></span></div><div style=3D"top:2945px;height:1=
9px;" class=3D"view-line"><span><span class=3D"mtk8">#&nbsp;STEP&nbsp;2</sp=
an></span></div><div style=3D"top:2964px;height:19px;" class=3D"view-line">=
<span><span class=3D"mtk15">print</span><span class=3D"mtk1 bracket-highlig=
hting-0">(</span><span class=3D"mtk21">"Title&nbsp;Case:"</span><span class=
=3D"mtk1">,&nbsp;clean_essay.title</span><span class=3D"mtk1 bracket-highli=
ghting-1">(</span><span class=3D"mtk1 bracket-highlighting-1">)</span><span=
 class=3D"mtk1 bracket-highlighting-0">)</span></span></div><div style=3D"t=
op:2983px;height:19px;" class=3D"view-line"><span><span></span></span></div=
><div style=3D"top:3002px;height:19px;" class=3D"view-line"><span><span cla=
ss=3D"mtk8">#&nbsp;STEP&nbsp;3</span></span></div><div style=3D"top:3021px;=
height:19px;" class=3D"view-line"><span><span class=3D"mtk15">print</span><=
span class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk21">"C=
ount:"</span><span class=3D"mtk1">,&nbsp;clean_essay.count</span><span clas=
s=3D"mtk1 bracket-highlighting-1">(</span><span class=3D"mtk21">"python"</s=
pan><span class=3D"mtk1 bracket-highlighting-1">)</span><span class=3D"mtk1=
 bracket-highlighting-0">)</span></span></div><div style=3D"top:3040px;heig=
ht:19px;" class=3D"view-line"><span><span></span></span></div><div style=3D=
"top:3059px;height:19px;" class=3D"view-line"><span><span class=3D"mtk8">#&=
nbsp;STEP&nbsp;4</span></span></div><div style=3D"top:3078px;height:19px;" =
class=3D"view-line"><span><span class=3D"mtk15">print</span><span class=3D"=
mtk1 bracket-highlighting-0">(</span><span class=3D"mtk21">"Replace:"</span=
><span class=3D"mtk1">,&nbsp;clean_essay.replace</span><span class=3D"mtk1 =
bracket-highlighting-1">(</span><span class=3D"mtk21">"python"</span><span =
class=3D"mtk1">,&nbsp;</span><span class=3D"mtk21">"Python&nbsp;=F0=9F=90=
=8D"</span><span class=3D"mtk1 bracket-highlighting-1">)</span><span class=
=3D"mtk1 bracket-highlighting-0">)</span></span></div><div style=3D"top:309=
7px;height:19px;" class=3D"view-line"><span><span></span></span></div><div =
style=3D"top:3116px;height:19px;" class=3D"view-line"><span><span class=3D"=
mtk8">#&nbsp;STEP&nbsp;5</span></span></div><div style=3D"top:3135px;height=
:19px;" class=3D"view-line"><span><span class=3D"mtk1">sentences&nbsp;=3D&n=
bsp;clean_essay.split</span><span class=3D"mtk1 bracket-highlighting-0">(</=
span><span class=3D"mtk21">".&nbsp;"</span><span class=3D"mtk1 bracket-high=
lighting-0">)</span></span></div><div style=3D"top:3154px;height:19px;" cla=
ss=3D"view-line"><span><span class=3D"mtk15">print</span><span class=3D"mtk=
1 bracket-highlighting-0">(</span><span class=3D"mtk21">"List:"</span><span=
 class=3D"mtk1">,&nbsp;sentences</span><span class=3D"mtk1 bracket-highligh=
ting-0">)</span></span></div><div style=3D"top:3173px;height:19px;" class=
=3D"view-line"><span><span></span></span></div><div style=3D"top:3192px;hei=
ght:19px;" class=3D"view-line"><span><span class=3D"mtk8">#&nbsp;STEP&nbsp;=
6</span></span></div><div style=3D"top:3211px;height:19px;" class=3D"view-l=
ine"><span><span class=3D"mtk19">for</span><span class=3D"mtk1">&nbsp;i&nbs=
p;</span><span class=3D"mtk6">in</span><span class=3D"mtk1">&nbsp;</span><s=
pan class=3D"mtk15">range</span><span class=3D"mtk1 bracket-highlighting-0"=
>(</span><span class=3D"mtk15">len</span><span class=3D"mtk1 bracket-highli=
ghting-1">(</span><span class=3D"mtk1">sentences</span><span class=3D"mtk1 =
bracket-highlighting-1">)</span><span class=3D"mtk1 bracket-highlighting-0"=
>)</span><span class=3D"mtk1">:</span></span></div><div style=3D"top:3230px=
;height:19px;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&=
nbsp;&nbsp;s&nbsp;=3D&nbsp;sentences</span><span class=3D"mtk1 bracket-high=
lighting-0">[</span><span class=3D"mtk1">i</span><span class=3D"mtk1 bracke=
t-highlighting-0">]</span></span></div><div style=3D"top:3249px;height:19px=
;" class=3D"view-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;<=
/span><span class=3D"mtk19">if</span><span class=3D"mtk1">&nbsp;</span><spa=
n class=3D"mtk6">not</span><span class=3D"mtk1">&nbsp;s.endswith</span><spa=
n class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk21">"."</=
span><span class=3D"mtk1 bracket-highlighting-0">)</span><span class=3D"mtk=
1">:</span></span></div><div style=3D"top:3268px;height:19px;" class=3D"vie=
w-line"><span><span class=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbs=
p;&nbsp;s&nbsp;+=3D&nbsp;</span><span class=3D"mtk21">"."</span></span></di=
v><div style=3D"top:3287px;height:19px;" class=3D"view-line"><span><span cl=
ass=3D"mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class=3D"mtk15">print</sp=
an><span class=3D"mtk1 bracket-highlighting-0">(</span><span class=3D"mtk6"=
>f</span><span class=3D"mtk21">"</span><span class=3D"mtk1 bracket-highligh=
ting-1">{</span><span class=3D"mtk1">i+</span><span class=3D"mtk12">1</span=
><span class=3D"mtk1 bracket-highlighting-1">}</span><span class=3D"mtk21">=
.&nbsp;</span><span class=3D"mtk1 bracket-highlighting-1">{</span><span cla=
ss=3D"mtk1">s</span><span class=3D"mtk1 bracket-highlighting-1">}</span><sp=
an class=3D"mtk21">"</span><span class=3D"mtk1 bracket-highlighting-0">)</s=
pan></span></div></div><div data-mprt=3D"1" class=3D"contentWidgets" style=
=3D"position: absolute; top: 0px;"><div class=3D"lightBulbWidget codicon co=
dicon-light-bulb" widgetid=3D"LightBulbWidget" title=3D"Show Code Actions (=
Ctrl+.)" style=3D"position: absolute; display: none; visibility: hidden; ma=
x-width: 1332px;"></div></div><div role=3D"presentation" aria-hidden=3D"tru=
e" class=3D"cursors-layer cursor-line-style cursor-solid"><div class=3D"cur=
sor monaco-mouse-cursor-text " style=3D"height: 19px; top: 2812px; left: 20=
8px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; =
font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quo=
t; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19p=
x; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0=
px; width: 1.6px;"></div></div></div><div role=3D"presentation" aria-hidden=
=3D"true" class=3D"visible scrollbar horizontal" style=3D"position: absolut=
e; width: 1318px; height: 10px; left: 0px; bottom: 0px;"><div class=3D"slid=
er" style=3D"position: absolute; top: 0px; left: 0px; height: 10px; transfo=
rm: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width:=
 1268px;"></div></div><canvas class=3D"decorationsOverviewRuler" aria-hidde=
n=3D"true" width=3D"17" height=3D"4145" style=3D"position: absolute; transf=
orm: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; wid=
th: 14px; height: 3316px; will-change: unset; display: block;"></canvas><di=
v role=3D"presentation" aria-hidden=3D"true" class=3D"invisible scrollbar v=
ertical" style=3D"position: absolute; width: 14px; height: 3316px; right: 0=
px; top: 0px;"><div class=3D"slider" style=3D"position: absolute; top: 0px;=
 left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: st=
rict; will-change: unset; height: 3316px;"></div></div></div><div role=3D"p=
resentation" aria-hidden=3D"true" style=3D"width: 1338px;"></div><textarea =
data-mprt=3D"6" class=3D"inputarea monaco-mouse-cursor-text" wrap=3D"on" au=
tocorrect=3D"off" autocapitalize=3D"off" autocomplete=3D"off" spellcheck=3D=
"false" aria-label=3D"Editor content;Press Alt+F1 for Accessibility Options=
." tabindex=3D"0" role=3D"textbox" aria-roledescription=3D"editor" aria-mul=
tiline=3D"true" aria-haspopup=3D"false" aria-autocomplete=3D"both" style=3D=
"tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&q=
uot;, monospace; font-weight: normal; font-size: 14px; font-feature-setting=
s: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal;=
 line-height: 19px; letter-spacing: 0px; top: 2812px; left: 6px; width: 769=
92px; height: 1px;"></textarea><div class=3D"monaco-editor-background textA=
reaCover" style=3D"position: absolute; top: 0px; left: 0px; width: 0px; hei=
ght: 0px;"></div><div data-mprt=3D"4" class=3D"overlayWidgets" style=3D"wid=
th: 1338px;"></div><div data-mprt=3D"8" class=3D"minimap slider-mouseover" =
role=3D"presentation" aria-hidden=3D"true" style=3D"position: absolute; lef=
t: 0px; width: 0px; height: 3316px;"><div class=3D"minimap-shadow-hidden" s=
tyle=3D"height: 3316px;"></div><canvas width=3D"0" height=3D"4145" style=3D=
"position: absolute; left: 0px; width: 0px; height: 3316px;"></canvas><canv=
as class=3D"minimap-decorations-layer" width=3D"0" height=3D"4145" style=3D=
"position: absolute; left: 0px; width: 0px; height: 3316px;"></canvas><div =
class=3D"minimap-slider" style=3D"position: absolute; transform: translate3=
d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div cl=
ass=3D"minimap-slider-horizontal" style=3D"position: absolute; width: 0px; =
height: 0px;"></div></div></div><div role=3D"presentation" aria-hidden=3D"t=
rue" class=3D"blockDecorations-container"></div></div><div data-mprt=3D"2" =
class=3D"overflowingContentWidgets" style=3D"display: none;"><div widgetid=
=3D"editor.contrib.resizableContentHoverWidget" style=3D"position: fixed; h=
eight: 29px; width: 76px; z-index: 50; display: none; visibility: hidden; m=
ax-width: 1536px; top: 154px; left: 289px;"><div class=3D"monaco-sash verti=
cal" style=3D"left: 74px;"></div><div class=3D"monaco-sash vertical disable=
d" style=3D"left: -2px;"></div><div class=3D"monaco-sash orthogonal-edge-no=
rth horizontal" style=3D"top: -2px;"><div class=3D"orthogonal-drag-handle e=
nd"></div></div><div class=3D"monaco-sash orthogonal-edge-south horizontal =
disabled" style=3D"top: 27px;"><div class=3D"orthogonal-drag-handle end"></=
div></div><div class=3D"monaco-hover hidden" tabindex=3D"0" role=3D"tooltip=
" style=3D"width: 76px; height: 29px;"><div class=3D"monaco-scrollable-elem=
ent " role=3D"presentation" style=3D"position: relative; overflow: hidden;"=
><div class=3D"monaco-hover-content" style=3D"overflow: hidden; font-size: =
14px; line-height: 1.35714; max-width: 883.08px; max-height: 829px; width: =
76px; height: 29px;"><div class=3D"hover-row markdown-hover"><div class=3D"=
hover-contents"><div class=3D"rendered-markdown"><p>Loading...</p></div></d=
iv></div></div><div role=3D"presentation" aria-hidden=3D"true" class=3D"inv=
isible scrollbar horizontal" style=3D"position: absolute; width: 66px; heig=
ht: 10px; left: 0px; bottom: 0px;"><div class=3D"slider" style=3D"position:=
 absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0=
px, 0px); contain: strict; width: 66px;"></div></div><div role=3D"presentat=
ion" aria-hidden=3D"true" class=3D"invisible scrollbar vertical" style=3D"p=
osition: absolute; width: 10px; height: 29px; right: 0px; top: 0px;"><div c=
lass=3D"slider" style=3D"position: absolute; top: 0px; left: 0px; width: 10=
px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 29px;">=
</div></div><div class=3D"shadow"></div><div class=3D"shadow"></div><div cl=
ass=3D"shadow"></div></div></div></div></div><div class=3D".in-cell-overflo=
wing"><div widgetid=3D"editor.contrib.quickInputWidget" style=3D"position: =
absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form =
class=3D"formview vertical layout flex"><div class=3D"widget-area"></div></=
colab-form></div>
    <div class=3D"output" aria-label=3D"Cell 0 output" role=3D"region"><!--=
--> <div class=3D"output-header"> </div>
        <div class=3D"output-content">
          <div class=3D"output-info"><colab-output-info><template shadowmod=
e=3D"open"><!----><!--?lit$516311766$--><md-icon-button toggle=3D"" class=
=3D"toggle-visibility-button" touch-target=3D"none" data-aria-label=3D"Show=
/hide output" id=3D"toggle-visibility-button" value=3D""><template shadowmo=
de=3D"open" shadowdelegatesfocus=3D""><!----><button id=3D"button" class=3D=
"icon-button  standard " aria-label=3D"Show/hide output" aria-pressed=3D"fa=
lse">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
        <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!---->=
<slot></slot></template>keyboard_arrow_down</md-icon>
        <md-icon slot=3D"selected" aria-hidden=3D"true"><template shadowmod=
e=3D"open"><!----><slot></slot></template>keyboard_arrow_right</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden=3D"true" for=3D"toggle-visibility-=
button" message=3D"Show/hide output"><template shadowmode=3D"open"><!----><=
!--?lit$516311766$--><!----><div><!--?lit$516311766$-->Show/hide output</di=
v><!----><!--?--></template></colab-tooltip-trigger><!--?lit$516311766$--><=
md-icon-button touch-target=3D"none" data-aria-expanded=3D"false" data-aria=
-haspopup=3D"menu" class=3D"menu-button focused hovered" data-aria-label=3D=
"Code cell output actions" id=3D"menu-button" value=3D""><template shadowmo=
de=3D"open" shadowdelegatesfocus=3D""><!----><button id=3D"button" class=3D=
"icon-button  standard " aria-label=3D"Code cell output actions" aria-haspo=
pup=3D"menu" aria-expanded=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
        <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!---->=
<slot></slot></template>more_horiz</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden=3D"true" for=3D"menu-button" messa=
ge=3D"Code cell output actions"><template shadowmode=3D"open"><!----><!--?l=
it$516311766$--><!----><div><!--?lit$516311766$-->Code cell output actions<=
/div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template><=
/colab-output-info></div>
          <div class=3D"output-iframe-container">
            <div class=3D"output-iframe-sizer" style=3D"min-height: 0px;"> =
<div><div><colab-static-output-renderer tabindex=3D"0" role=3D"group"><div>=
<div class=3D"stream output-id-3 output_text"><pre>=E2=9C=93 Valid name
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D
Student : Ayesha Sharma
Roll No : 101
Marks   : [88, 72, 95, 60, 78]
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D
=E2=9C=93 Valid name
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D
Student : Rohit Verma
Roll No : 102
Marks   : [55, 68, 49, 72, 61]
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D
=E2=9C=93 Valid name
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D
Student : Priya Nair
Roll No : 103
Marks   : [91, 85, 88, 94, 79]
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D
=E2=9C=93 Valid name
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D
Student : Karan Mehta
Roll No : 104
Marks   : [40, 55, 38, 62, 50]
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D
=E2=9C=93 Valid name
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D
Student : Sneha Pillai
Roll No : 105
Marks   : [75, 80, 70, 68, 85]
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D
PRIYA NAIR
priya nair
Math - 88 - A
Physics - 72 - B
CS - 95 - A+
English - 60 - C
Chemistry - 78 - B
Total: 393
Average: 78.6
Highest: CS 95
Lowest: English 60
Enter subject (or done): done
New subjects added: 0
New average: 78.6
Name              | Average | Status
----------------------------------------
Ayesha Sharma      |  78.6   | Pass
Rohit Verma        |  61.0   | Pass
Priya Nair         |  87.4   | Pass
Karan Mehta        |  49.0   | Fail
Sneha Pillai       |  75.6   | Pass
Passed: 4
Failed: 1
Topper: Priya Nair 87.4
Class Average: 70.32
Clean: python is a versatile language. it supports object oriented, functio=
nal, and procedural programming. python is widely used in data science and =
machine learning.
Title Case: Python Is A Versatile Language. It Supports Object Oriented, Fu=
nctional, And Procedural Programming. Python Is Widely Used In Data Science=
 And Machine Learning.
Count: 2
Replace: Python =F0=9F=90=8D is a versatile language. it supports object or=
iented, functional, and procedural programming. Python =F0=9F=90=8D is wide=
ly used in data science and machine learning.
List: ['python is a versatile language', 'it supports object oriented, func=
tional, and procedural programming', 'python is widely used in data science=
 and machine learning.']
1. python is a versatile language.
2. it supports object oriented, functional, and procedural programming.
3. python is widely used in data science and machine learning.
</pre></div></div><div></div></colab-static-output-renderer></div></div><di=
v><div></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowmode=3D"open"><!=
----></template></colab-cell-next-steps></div></div></div><div class=3D"add=
-cell">
      <hr>
    </div></div></div>
              </div>
            </div>
          <section class=3D"sidebar" aria-label=3D"Comments" style=3D"displ=
ay: none;"></section></div>
          <!--?lit$516311766$--> <div class=3D"footer-links" style=3D"paddi=
ng-bottom: 8px;">
      <a target=3D"_blank" href=3D"https://colab.research.google.com/signup=
?utm_source=3Dfooter&amp;utm_medium=3Dlink&amp;utm_campaign=3Dfooter_links"=
>
        <!--?lit$516311766$-->Colab paid products
      </a>
      -
      <a href=3D"https://colab.research.google.com/cancel-subscription" tar=
get=3D"_blank">
        <!--?lit$516311766$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-scroller>
    </div><div class=3D"right-pane-snap-hint"></div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style=3D"height: 40%" class=3D"sn-resize no-tabs"><div=
 class=3D"resizer-thumb"></div>
        <!--?lit$516311766$--><colab-tab-pane class=3D"layout vertical grow=
 no-tabs" align=3D"horizontal"><!----> <div class=3D"layout vertical grow">
    <div class=3D"tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowmode=3D"open"><!---->
      <div class=3D"tabs">
        <slot></slot>
      </div>
      <md-divider part=3D"divider"><template shadowmode=3D"open"><!----></t=
emplate></md-divider>
    </template></md-tabs>
      <div class=3D"layout grow"></div>
      <div class=3D"tab-pane-header-actions"></div>
      <!--?lit$516311766$--><md-icon-button data-aria-expanded=3D"false" da=
ta-aria-haspopup=3D"menu" id=3D"tab-pane-2-more-actions-button" data-aria-l=
abel=3D"More tab actions" value=3D""><template shadowmode=3D"open" shadowde=
legatesfocus=3D""><!----><button id=3D"button" class=3D"icon-button  standa=
rd " aria-label=3D"More tab actions" aria-haspopup=3D"menu" aria-expanded=
=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden=3D"true" for=3D"tab-pane-2-more-acti=
ons-button" message=3D"More tab actions"><template shadowmode=3D"open"><!--=
--><!--?lit$516311766$--><!----><div><!--?lit$516311766$-->More tab actions=
</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$516311766$--><md-icon-button id=3D"tab=
-pane-2-close-all-button" data-aria-label=3D"Close all tabs" value=3D""><te=
mplate shadowmode=3D"open" shadowdelegatesfocus=3D""><!----><button id=3D"b=
utton" class=3D"icon-button  standard " aria-label=3D"Close all tabs">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden=3D"true" for=3D"tab-pane-2-close-all=
-button" message=3D"Close all tabs"><template shadowmode=3D"open"><!----><!=
--?lit$516311766$--><!----><div><!--?lit$516311766$-->Close all tabs</div><=
!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class=3D"layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style=3D"width: 37%" class=3D"we-resize no-tabs"><div =
class=3D"resizer-thumb"></div>
        <!--?lit$516311766$--> <div class=3D"layout vertical tab-pane-paren=
t">
      <!--?lit$516311766$--><colab-tab-pane class=3D"layout vertical grow n=
o-tabs" align=3D"horizontal"><!----> <div class=3D"layout vertical grow">
    <div class=3D"tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowmode=3D"open"><!---->
      <div class=3D"tabs">
        <slot></slot>
      </div>
      <md-divider part=3D"divider"><template shadowmode=3D"open"><!----></t=
emplate></md-divider>
    </template></md-tabs>
      <div class=3D"layout grow"></div>
      <div class=3D"tab-pane-header-actions"><!----><!--?lit$516311766$--><=
!--?--></div>
      <!--?lit$516311766$--><md-icon-button data-aria-expanded=3D"false" da=
ta-aria-haspopup=3D"menu" id=3D"tab-pane-1-more-actions-button" data-aria-l=
abel=3D"More tab actions" value=3D""><template shadowmode=3D"open" shadowde=
legatesfocus=3D""><!----><button id=3D"button" class=3D"icon-button  standa=
rd " aria-label=3D"More tab actions" aria-haspopup=3D"menu" aria-expanded=
=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden=3D"true" for=3D"tab-pane-1-more-acti=
ons-button" message=3D"More tab actions"><template shadowmode=3D"open"><!--=
--><!--?lit$516311766$--><!----><div><!--?lit$516311766$-->More tab actions=
</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$516311766$--><md-icon-button id=3D"tab=
-pane-1-close-all-button" data-aria-label=3D"Close all tabs" value=3D""><te=
mplate shadowmode=3D"open" shadowdelegatesfocus=3D""><!----><button id=3D"b=
utton" class=3D"icon-button  standard " aria-label=3D"Close all tabs">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface"></div></template></md-ripple=
>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden=3D"true" for=3D"tab-pane-1-close-all=
-button" message=3D"Close all tabs"><template shadowmode=3D"open"><!----><!=
--?lit$516311766$--><!----><div><!--?lit$516311766$-->Close all tabs</div><=
!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class=3D"layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style=3D"height: 40%" class=3D"sn-resize no-tabs"><div=
 class=3D"resizer-thumb"></div>
        <!--?lit$516311766$--><colab-tab-pane class=3D"layout vertical grow=
 no-tabs" align=3D"horizontal"><!----> <div class=3D"layout vertical grow">
    <div class=3D"tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowmode=3D"open"><!---->
      <div class=3D"tabs">
        <slot></slot>
      </div>
      <md-divider part=3D"divider"><template shadowmode=3D"open"><!----></t=
emplate></md-divider>
    </template></md-tabs>
      <div class=3D"layout grow"></div>
      <div class=3D"tab-pane-header-actions"></div>
      <!--?lit$516311766$--><md-icon-button data-aria-expanded=3D"false" da=
ta-aria-haspopup=3D"menu" id=3D"tab-pane-3-more-actions-button" data-aria-l=
abel=3D"More tab actions" value=3D""><template shadowmode=3D"open" shadowde=
legatesfocus=3D""><!----><button id=3D"button" class=3D"icon-button  standa=
rd " aria-label=3D"More tab actions" aria-haspopup=3D"menu" aria-expanded=
=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template>more_vert</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden=3D"true" for=3D"tab-pane-3-more-acti=
ons-button" message=3D"More tab actions"><template shadowmode=3D"open"><!--=
--><!--?lit$516311766$--><!----><div><!--?lit$516311766$-->More tab actions=
</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$516311766$--><md-icon-button id=3D"tab=
-pane-3-close-all-button" data-aria-label=3D"Close all tabs" value=3D""><te=
mplate shadowmode=3D"open" shadowdelegatesfocus=3D""><!----><button id=3D"b=
utton" class=3D"icon-button  standard " aria-label=3D"Close all tabs">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
      <md-icon aria-hidden=3D"true"><template shadowmode=3D"open"><!----><s=
lot></slot></template>close</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden=3D"true" for=3D"tab-pane-3-close-all=
-button" message=3D"Close all tabs"><template shadowmode=3D"open"><!----><!=
--?lit$516311766$--><!----><div><!--?lit$516311766$-->Close all tabs</div><=
!----><!--?--></template>
    </colab-tooltip-trigger>
    </div>
    <div class=3D"layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class=3D"proxies"><div><colab-dom-lifecycle-events style=3D"di=
splay: none;"></colab-dom-lifecycle-events><iframe allow=3D"" sandbox=3D"al=
low-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-e=
scape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-=
activation" src=3D"cid:frame-E952051BCAE869AF75B67442D3AEFE77@mhtml.blink" =
style=3D"width: 1px; height: 1px; position: absolute; top: -100px;"></ifram=
e></div><div><colab-dom-lifecycle-events style=3D"display: none;"></colab-d=
om-lifecycle-events><iframe allow=3D"accelerometer; autoplay; gyroscope; ma=
gnetometer; xr-spatial-tracking; clipboard-write" sandbox=3D"allow-download=
s allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbo=
x allow-same-origin allow-scripts allow-storage-access-by-user-activation a=
llow-modals" src=3D"cid:frame-2D36B4215F9045E8DA5158ACE6E29B15@mhtml.blink"=
 style=3D"width: 1px; height: 1px; position: absolute; top: -100px;"></ifra=
me></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-composer-floating-spark><template shadowmode=3D"open"><!---->
      <md-icon-button toggle=3D"" id=3D"toggle-composer-button" data-aria-l=
abel=3D"Toggle Gemini" value=3D""><template shadowmode=3D"open" shadowdeleg=
atesfocus=3D""><!----><button id=3D"button" class=3D"icon-button  standard =
" aria-label=3D"Toggle Gemini" aria-pressed=3D"false">
        <!--?lit$516311766$--><md-focus-ring part=3D"focus-ring" for=3D"but=
ton" aria-hidden=3D"true"><template shadowmode=3D"open"><!----></template><=
/md-focus-ring>
        <!--?lit$516311766$--><md-ripple aria-hidden=3D"true"><template sha=
dowmode=3D"open"><!----><div class=3D"surface   "></div></template></md-rip=
ple>
        <!--?lit$516311766$--><span class=3D"icon"><slot></slot></span>
        <!--?lit$516311766$-->
        <!--?lit$516311766$--><span class=3D"touch"></span>
  </button></template>
        <!--?lit$516311766$--><md-icon aria-hidden=3D"true"><template shado=
wmode=3D"open"><!----><slot></slot></template>spark</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden=3D"true" for=3D"toggle-composer-bu=
tton" message=3D"Toggle Gemini"><template shadowmode=3D"open"><!----><!--?l=
it$516311766$--><!----><div><!--?lit$516311766$-->Toggle Gemini</div><!----=
><!--?--></template>
      </colab-tooltip-trigger>
    </template></colab-composer-floating-spark><colab-status-bar role=3D"re=
gion" aria-label=3D"Runtime status bar"><template shadowmode=3D"open"><!---=
-><span class=3D"left">
        <slot name=3D"bottom-pane-buttons"></slot>
      </span>
      <span class=3D"right">
        <!--?lit$516311766$--><colab-execution-status><template shadowmode=
=3D"open"><!----><md-text-button id=3D"execution-status" aria-describedby=
=3D"execution-status-tooltip" value=3D"" has-icon=3D""><template shadowmode=
=3D"open" shadowdelegatesfocus=3D""><!---->
      <!--?lit$516311766$-->
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface   "></div></template><=
/md-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template><!--?lit$516311766$--><md-icon slot=3D"icon" aria-hidden=3D"=
true"><template shadowmode=3D"open"><!----><slot></slot></template>check</m=
d-icon><!--?lit$516311766$-->10:15=E2=80=AFPM</md-text-button>
      <colab-tooltip-trigger aria-hidden=3D"true" id=3D"execution-status-to=
oltip" for=3D"execution-status" message=3D"Focus the last run cell

10:15=E2=80=AFPM (0 minutes ago)
executed in 50.483s"><template shadowmode=3D"open"><!----><!--?lit$51631176=
6$--><!----><div><!--?lit$516311766$-->Focus the last run cell</div><!---->=
<!----><br><!----><!----><div><!--?lit$516311766$-->10:15=E2=80=AFPM (0 min=
utes ago)</div><!----><!----><div><!--?lit$516311766$-->executed in 50.483s=
</div><!----><!--?--></template>
      </colab-tooltip-trigger></template></colab-execution-status><!--?lit$=
516311766$--><!--?lit$516311766$--><!--?lit$516311766$--><colab-runtime-sta=
tus><template shadowmode=3D"open"><!----><md-text-button data-aria-expanded=
=3D"false" data-aria-haspopup=3D"menu" id=3D"runtime-options" aria-describe=
dby=3D"runtime-options-tooltip" value=3D"" has-icon=3D""><template shadowmo=
de=3D"open" shadowdelegatesfocus=3D""><!---->
      <!--?lit$516311766$-->
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface   "></div></template><=
/md-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button" aria-has=
popup=3D"menu" aria-expanded=3D"false">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template><md-icon slot=3D"icon" aria-hidden=3D"true"><template shadow=
mode=3D"open"><!----><slot></slot></template>dns</md-icon><!--?lit$51631176=
6$-->Python 3</md-text-button><colab-tooltip-trigger aria-hidden=3D"true" f=
or=3D"runtime-options" id=3D"runtime-options-tooltip" message=3D"Runtime op=
tions"><template shadowmode=3D"open"><!----><!--?lit$516311766$--><!----><d=
iv><!--?lit$516311766$-->Runtime options</div><!----><!--?--></template></c=
olab-tooltip-trigger></template></colab-runtime-status>
      </span></template><md-text-button slot=3D"bottom-pane-buttons" comman=
d=3D"show-variables" value=3D"" has-icon=3D""><template shadowmode=3D"open"=
 shadowdelegatesfocus=3D""><!---->
      <!--?lit$516311766$-->
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface"></div></template></md=
-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template>
        <md-icon slot=3D"icon" aria-hidden=3D"true"><template shadowmode=3D=
"open"><!----><slot></slot></template><!--?lit$516311766$-->data_object</md=
-icon>
        <!--?lit$516311766$-->Variables</md-text-button><md-text-button slo=
t=3D"bottom-pane-buttons" command=3D"show-terminal" value=3D"" has-icon=3D"=
"><template shadowmode=3D"open" shadowdelegatesfocus=3D""><!---->
      <!--?lit$516311766$-->
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface"></div></template></md=
-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template>
        <md-icon slot=3D"icon" aria-hidden=3D"true"><template shadowmode=3D=
"open"><!----><slot></slot></template><!--?lit$516311766$-->terminal</md-ic=
on>
        <!--?lit$516311766$-->Terminal</md-text-button></colab-status-bar><=
/div><div class=3D"goog-menu" id=3D"file-menu" role=3D"menu" aria-haspopup=
=3D"true" style=3D"user-select: none; max-height: 628px; visibility: visibl=
e; left: 70px; top: 62px; display: none;"><!--?lit$516311766$--><div comman=
d=3D"locate-in-drive" class=3D"goog-menuitem" role=3D"menuitem" id=3D":2" s=
tyle=3D"user-select: none;"><div class=3D"goog-menuitem-content" style=3D"u=
ser-select: none;"><!--?lit$516311766$-->Locate in Drive<!--?lit$516311766$=
--></div></div><div command=3D"open-in-playground" class=3D"goog-menuitem" =
role=3D"menuitem" id=3D":3" style=3D"user-select: none;"><div class=3D"goog=
-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->Open =
in playground mode<!--?lit$516311766$--></div></div><div class=3D"goog-menu=
separator goog-menuitem-disabled" aria-disabled=3D"true" role=3D"separator"=
 id=3D":4" style=3D"user-select: none;"></div><div command=3D"new" class=3D=
" goog-menuitem " role=3D"menuitem" id=3D":5" style=3D"user-select: none;">=
<div class=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$=
516311766$-->New notebook in Drive<!--?lit$516311766$--></div></div><div co=
mmand=3D"open" class=3D" goog-menuitem " role=3D"menuitem" id=3D":6" style=
=3D"user-select: none;"><div class=3D"goog-menuitem-content" style=3D"user-=
select: none;"><!--?lit$516311766$-->Open notebook<!--?lit$516311766$--><sp=
an class=3D"goog-menuitem-accel">Ctrl+O</span></div></div><div command=3D"i=
mport-notebook" class=3D" goog-menuitem " role=3D"menuitem" id=3D":7" style=
=3D"user-select: none;"><div class=3D"goog-menuitem-content" style=3D"user-=
select: none;"><!--?lit$516311766$-->Upload notebook<!--?lit$516311766$--><=
/div></div><div class=3D"goog-menuseparator goog-menuitem-disabled" aria-di=
sabled=3D"true" role=3D"separator" id=3D":8" style=3D"user-select: none;"><=
/div><div command=3D"rename" class=3D"goog-menuitem" role=3D"menuitem" id=
=3D":9" style=3D"user-select: none;"><div class=3D"goog-menuitem-content" s=
tyle=3D"user-select: none;"><!--?lit$516311766$-->Rename<!--?lit$516311766$=
--></div></div><div command=3D"move-notebook" class=3D"goog-menuitem" role=
=3D"menuitem" id=3D":a" style=3D"user-select: none;"><div class=3D"goog-men=
uitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->Move<!--?=
lit$516311766$--></div></div><div command=3D"trash" class=3D"goog-menuitem"=
 role=3D"menuitem" id=3D":b" style=3D"user-select: none;"><div class=3D"goo=
g-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->Move=
 to trash<!--?lit$516311766$--></div></div><div class=3D"goog-menuseparator=
 goog-menuitem-disabled" aria-disabled=3D"true" role=3D"separator" id=3D":c=
" style=3D"user-select: none;"></div><div command=3D"clone" class=3D"goog-m=
enuitem" role=3D"menuitem" id=3D":d" style=3D"user-select: none;"><div clas=
s=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766=
$-->Save a copy in Drive<!--?lit$516311766$--></div></div><div command=3D"c=
opy-to-gist" class=3D"goog-menuitem" role=3D"menuitem" id=3D":e" style=3D"u=
ser-select: none;"><div class=3D"goog-menuitem-content" style=3D"user-selec=
t: none;"><!--?lit$516311766$-->Save a copy as a GitHub Gist<!--?lit$516311=
766$--></div></div><div command=3D"copy-to-github" class=3D"goog-menuitem" =
role=3D"menuitem" id=3D":f" style=3D"user-select: none;"><div class=3D"goog=
-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->Save =
a copy in GitHub<!--?lit$516311766$--></div></div><div class=3D"goog-menuse=
parator goog-menuitem-disabled" aria-disabled=3D"true" role=3D"separator" i=
d=3D":g" style=3D"user-select: none;"></div><div command=3D"save" class=3D"=
goog-menuitem" role=3D"menuitem" id=3D":h" style=3D"user-select: none;"><di=
v class=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$516=
311766$-->Save<!--?lit$516311766$--><span class=3D"goog-menuitem-accel">Ctr=
l+S</span></div></div><div command=3D"save-and-checkpoint" class=3D"goog-me=
nuitem" role=3D"menuitem" id=3D":i" style=3D"user-select: none;"><div class=
=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766$=
-->Save and pin revision<!--?lit$516311766$--><span class=3D"goog-menuitem-=
accel">Ctrl+M S</span></div></div><div command=3D"show-history" class=3D"go=
og-menuitem" role=3D"menuitem" id=3D":j" style=3D"user-select: none;"><div =
class=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$51631=
1766$-->Revision history<!--?lit$516311766$--></div></div><div command=3D"s=
how-fileinfo" class=3D" goog-menuitem " role=3D"menuitem" id=3D":k" style=
=3D"user-select: none;"><div class=3D"goog-menuitem-content" style=3D"user-=
select: none;"><!--?lit$516311766$-->Notebook info<!--?lit$516311766$--></d=
iv></div><div class=3D"goog-menuseparator goog-menuitem-disabled" aria-disa=
bled=3D"true" role=3D"separator" id=3D":l" style=3D"user-select: none;"></d=
iv><div class=3D"goog-submenu goog-menuitem" id=3D"download-submenu-menu-bu=
tton" role=3D"menuitem" aria-haspopup=3D"true" style=3D"user-select: none;"=
><div class=3D"goog-menuitem-content" style=3D"user-select: none;">
      <!--?lit$516311766$-->Download
    <span class=3D"goog-submenu-arrow" style=3D"user-select: none;">=E2=96=
=BA</span></div></div><div command=3D"print" class=3D"goog-menuitem" role=
=3D"menuitem" id=3D":p" style=3D"user-select: none;"><div class=3D"goog-men=
uitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->Print<!--=
?lit$516311766$--><span class=3D"goog-menuitem-accel">Ctrl+P</span></div></=
div></div><div class=3D"goog-menu" id=3D"download-submenu-menu" role=3D"men=
u" aria-haspopup=3D"true" style=3D"user-select: none; left: 397.8px; top: 6=
13.8px; display: none;"><!--?lit$516311766$--><div command=3D"download-ipyn=
b" class=3D" goog-menuitem " role=3D"menuitem" id=3D":n" style=3D"user-sele=
ct: none;"><div class=3D"goog-menuitem-content" style=3D"user-select: none;=
"><!--?lit$516311766$-->Download .ipynb<!--?lit$516311766$--></div></div><d=
iv command=3D"download-python" class=3D" goog-menuitem " role=3D"menuitem" =
id=3D":o" style=3D"user-select: none;"><div class=3D"goog-menuitem-content"=
 style=3D"user-select: none;"><!--?lit$516311766$-->Download .py<!--?lit$51=
6311766$--></div></div></div><div class=3D"goog-menu" id=3D"edit-menu" role=
=3D"menu" aria-haspopup=3D"true" style=3D"display: none; user-select: none;=
"><!--?lit$516311766$--><div command=3D"undo" class=3D" goog-menuitem " rol=
e=3D"menuitem" id=3D":r" style=3D"user-select: none;"><div class=3D"goog-me=
nuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->Undo<!--=
?lit$516311766$--></div></div><div command=3D"redo" class=3D" goog-menuitem=
 " role=3D"menuitem" id=3D":s" style=3D"user-select: none;"><div class=3D"g=
oog-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->Re=
do<!--?lit$516311766$--></div></div><div class=3D"goog-menuseparator goog-m=
enuitem-disabled" aria-disabled=3D"true" role=3D"separator" id=3D":t" style=
=3D"user-select: none;"></div><div command=3D"select-all" class=3D" goog-me=
nuitem " role=3D"menuitem" id=3D":u" style=3D"user-select: none;"><div clas=
s=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766=
$-->Select all cells<!--?lit$516311766$--></div></div><div command=3D"cut" =
class=3D" goog-menuitem " role=3D"menuitem" id=3D":v" style=3D"user-select:=
 none;"><div class=3D"goog-menuitem-content" style=3D"user-select: none;"><=
!--?lit$516311766$-->Cut cell or selection<!--?lit$516311766$--></div></div=
><div command=3D"copy" class=3D" goog-menuitem " role=3D"menuitem" id=3D":w=
" style=3D"user-select: none;"><div class=3D"goog-menuitem-content" style=
=3D"user-select: none;"><!--?lit$516311766$-->Copy cell or selection<!--?li=
t$516311766$--></div></div><div command=3D"paste" class=3D" goog-menuitem "=
 role=3D"menuitem" id=3D":x" style=3D"user-select: none;"><div class=3D"goo=
g-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->Past=
e<!--?lit$516311766$--></div></div><div command=3D"delete-cell-or-selection=
" class=3D" goog-menuitem " role=3D"menuitem" id=3D":y" style=3D"user-selec=
t: none;"><div class=3D"goog-menuitem-content" style=3D"user-select: none;"=
><!--?lit$516311766$-->Delete selected cells<!--?lit$516311766$--></div></d=
iv><div class=3D"goog-menuseparator goog-menuitem-disabled" aria-disabled=
=3D"true" role=3D"separator" id=3D":z" style=3D"user-select: none;"></div><=
div command=3D"find" class=3D" goog-menuitem " role=3D"menuitem" id=3D":10"=
 style=3D"user-select: none;"><div class=3D"goog-menuitem-content" style=3D=
"user-select: none;"><!--?lit$516311766$-->Find and replace<!--?lit$5163117=
66$--></div></div><div command=3D"find-next" class=3D" goog-menuitem " role=
=3D"menuitem" id=3D":11" style=3D"user-select: none;"><div class=3D"goog-me=
nuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->Find nex=
t<!--?lit$516311766$--></div></div><div command=3D"find-previous" class=3D"=
 goog-menuitem " role=3D"menuitem" id=3D":12" style=3D"user-select: none;">=
<div class=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$=
516311766$-->Find previous<!--?lit$516311766$--></div></div><div class=3D"g=
oog-menuseparator goog-menuitem-disabled" aria-disabled=3D"true" role=3D"se=
parator" id=3D":13" style=3D"user-select: none;"></div><div command=3D"note=
book-settings" class=3D" goog-menuitem " role=3D"menuitem" id=3D":14" style=
=3D"user-select: none;"><div class=3D"goog-menuitem-content" style=3D"user-=
select: none;"><!--?lit$516311766$-->Notebook settings<!--?lit$516311766$--=
></div></div><div class=3D"goog-menuseparator goog-menuitem-disabled" aria-=
disabled=3D"true" role=3D"separator" id=3D":15" style=3D"user-select: none;=
"></div><div command=3D"clear-outputs" class=3D" goog-menuitem " role=3D"me=
nuitem" id=3D":16" style=3D"user-select: none;"><div class=3D"goog-menuitem=
-content" style=3D"user-select: none;"><!--?lit$516311766$-->Clear all outp=
uts<!--?lit$516311766$--></div></div></div><div class=3D"goog-menu" id=3D"v=
iew-menu" role=3D"menu" aria-haspopup=3D"true" style=3D"display: none; user=
-select: none;"><!--?lit$516311766$--><div command=3D"show-toc-pane" class=
=3D"goog-menuitem goog-option" role=3D"menuitemcheckbox" aria-checked=3D"fa=
lse" id=3D":18" style=3D"user-select: none;"><div class=3D"goog-menuitem-co=
ntent" style=3D"user-select: none;"><div class=3D"goog-menuitem-checkbox" s=
tyle=3D"user-select: none;"><!----><md-icon aria-hidden=3D"true"><template =
shadowmode=3D"open"><!----><slot></slot></template>check</md-icon> </div><!=
--?lit$516311766$-->Table of contents<!--?lit$516311766$--></div></div><div=
 command=3D"show-executedcode" class=3D" goog-menuitem " role=3D"menuitem" =
id=3D":19" style=3D"user-select: none;"><div class=3D"goog-menuitem-content=
" style=3D"user-select: none;"><!--?lit$516311766$-->Executed code history<=
!--?lit$516311766$--></div></div><div command=3D"start-presentation" class=
=3D" goog-menuitem " role=3D"menuitem" id=3D":1a" style=3D"user-select: non=
e;"><div class=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?=
lit$516311766$-->Start slideshow<!--?lit$516311766$--></div></div><div comm=
and=3D"start-presentation-beginning" class=3D" goog-menuitem " role=3D"menu=
item" id=3D":1b" style=3D"user-select: none;"><div class=3D"goog-menuitem-c=
ontent" style=3D"user-select: none;"><!--?lit$516311766$-->Start slideshow =
from beginning<!--?lit$516311766$--></div></div><div class=3D"goog-submenu =
goog-menuitem" id=3D"comments-submenu-menu-button" role=3D"menuitem" aria-h=
aspopup=3D"true" style=3D"user-select: none;"><div class=3D"goog-menuitem-c=
ontent" style=3D"user-select: none;">
      <!--?lit$516311766$-->Comments
    <span class=3D"goog-submenu-arrow" style=3D"user-select: none;">=E2=96=
=BA</span></div></div><div class=3D"goog-menuseparator goog-menuitem-disabl=
ed" aria-disabled=3D"true" role=3D"separator" id=3D":1g" style=3D"user-sele=
ct: none;"></div><div command=3D"collapse-sections" class=3D" goog-menuitem=
 " role=3D"menuitem" id=3D":1h" style=3D"user-select: none;"><div class=3D"=
goog-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->C=
ollapse sections<!--?lit$516311766$--></div></div><div command=3D"expand-se=
ctions" class=3D" goog-menuitem " role=3D"menuitem" id=3D":1i" style=3D"use=
r-select: none;"><div class=3D"goog-menuitem-content" style=3D"user-select:=
 none;"><!--?lit$516311766$-->Expand sections<!--?lit$516311766$--></div></=
div><div command=3D"save-section-layout" class=3D" goog-menuitem " role=3D"=
menuitem" id=3D":1j" style=3D"user-select: none;"><div class=3D"goog-menuit=
em-content" style=3D"user-select: none;"><!--?lit$516311766$-->Save collaps=
ed section layout<!--?lit$516311766$--></div></div><div class=3D"goog-menus=
eparator goog-menuitem-disabled" aria-disabled=3D"true" role=3D"separator" =
id=3D":1k" style=3D"user-select: none;"></div><div command=3D"hide-code" cl=
ass=3D" goog-menuitem " role=3D"menuitem" id=3D":1l" style=3D"user-select: =
none;"><div class=3D"goog-menuitem-content" style=3D"user-select: none;"><!=
--?lit$516311766$-->Show/hide code<!--?lit$516311766$--></div></div><div co=
mmand=3D"toggle-output" class=3D" goog-menuitem " role=3D"menuitem" id=3D":=
1m" style=3D"user-select: none;"><div class=3D"goog-menuitem-content" style=
=3D"user-select: none;"><!--?lit$516311766$-->Show/hide output<!--?lit$5163=
11766$--></div></div><div class=3D"goog-menuseparator goog-menuitem-disable=
d" aria-disabled=3D"true" role=3D"separator" id=3D":1n" style=3D"user-selec=
t: none;"></div><div command=3D"focus-next-tab" class=3D" goog-menuitem " r=
ole=3D"menuitem" id=3D":1o" style=3D"user-select: none;"><div class=3D"goog=
-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->Focus=
 next tab<!--?lit$516311766$--></div></div><div command=3D"focus-previous-t=
ab" class=3D" goog-menuitem " role=3D"menuitem" id=3D":1p" style=3D"user-se=
lect: none;"><div class=3D"goog-menuitem-content" style=3D"user-select: non=
e;"><!--?lit$516311766$-->Focus previous tab<!--?lit$516311766$--></div></d=
iv><div command=3D"move-tab-to-next" class=3D" goog-menuitem " role=3D"menu=
item" id=3D":1q" style=3D"user-select: none;"><div class=3D"goog-menuitem-c=
ontent" style=3D"user-select: none;"><!--?lit$516311766$-->Move tab to next=
 pane<!--?lit$516311766$--></div></div><div command=3D"move-tab-to-prev" cl=
ass=3D" goog-menuitem " role=3D"menuitem" id=3D":1r" style=3D"user-select: =
none;"><div class=3D"goog-menuitem-content" style=3D"user-select: none;"><!=
--?lit$516311766$-->Move tab to previous pane<!--?lit$516311766$--></div></=
div></div><div class=3D"goog-menu" id=3D"comments-submenu-menu" role=3D"men=
u" aria-haspopup=3D"true" style=3D"display: none; user-select: none;"><!--?=
lit$516311766$--><div command=3D"hide-sidebar-comments" class=3D" goog-menu=
item goog-option-selectable " role=3D"menuitem" id=3D":1d" style=3D"user-se=
lect: none;"><div class=3D"goog-menuitem-content" style=3D"user-select: non=
e;"><!--?lit$516311766$-->Hide comments<!--?lit$516311766$--></div></div><d=
iv command=3D"show-minimized-sidebar-comments" class=3D" goog-menuitem goog=
-option-selectable " role=3D"menuitem" id=3D":1e" style=3D"user-select: non=
e;"><div class=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?=
lit$516311766$-->Minimize comments<!--?lit$516311766$--></div></div><div co=
mmand=3D"show-expanded-sidebar-comments" class=3D" goog-menuitem goog-optio=
n-selectable " role=3D"menuitem" id=3D":1f" style=3D"user-select: none;"><d=
iv class=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$51=
6311766$-->Expand comments<!--?lit$516311766$--></div></div></div><div clas=
s=3D"goog-menu" id=3D"insert-menu" role=3D"menu" aria-haspopup=3D"true" sty=
le=3D"display: none; user-select: none;"><!--?lit$516311766$--><div command=
=3D"insert-cell-below" class=3D" goog-menuitem " role=3D"menuitem" id=3D":1=
t" style=3D"user-select: none;"><div class=3D"goog-menuitem-content" style=
=3D"user-select: none;"><!--?lit$516311766$-->Code cell<!--?lit$516311766$-=
-></div></div><div command=3D"add-text" class=3D" goog-menuitem " role=3D"m=
enuitem" id=3D":1u" style=3D"user-select: none;"><div class=3D"goog-menuite=
m-content" style=3D"user-select: none;"><!--?lit$516311766$-->Text cell<!--=
?lit$516311766$--></div></div><div command=3D"add-section-header" class=3D"=
 goog-menuitem " role=3D"menuitem" id=3D":1v" style=3D"user-select: none;">=
<div class=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$=
516311766$-->Section header cell<!--?lit$516311766$--></div></div><div clas=
s=3D"goog-menuseparator goog-menuitem-disabled" aria-disabled=3D"true" role=
=3D"separator" id=3D":1w" style=3D"user-select: none;"></div><div command=
=3D"open-scratch-code-cell" class=3D" goog-menuitem " role=3D"menuitem" id=
=3D":1x" style=3D"user-select: none;"><div class=3D"goog-menuitem-content" =
style=3D"user-select: none;"><!--?lit$516311766$-->Scratch code cell<!--?li=
t$516311766$--></div></div><div command=3D"snippets" class=3D" goog-menuite=
m " role=3D"menuitem" id=3D":1y" style=3D"user-select: none;"><div class=3D=
"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->=
Code snippets<!--?lit$516311766$--></div></div><div class=3D"goog-menusepar=
ator goog-menuitem-disabled" aria-disabled=3D"true" role=3D"separator" id=
=3D":1z" style=3D"user-select: none;"></div><div command=3D"add-form-field"=
 class=3D" goog-menuitem " role=3D"menuitem" id=3D":20" style=3D"user-selec=
t: none;"><div class=3D"goog-menuitem-content" style=3D"user-select: none;"=
><!--?lit$516311766$-->Add a form field<!--?lit$516311766$--></div></div></=
div><div class=3D"goog-menu" id=3D"runtime-menu" role=3D"menu" aria-haspopu=
p=3D"true" style=3D"display: none; user-select: none;"><!--?lit$516311766$-=
-><div command=3D"runall" class=3D" goog-menuitem " role=3D"menuitem" id=3D=
":22" style=3D"user-select: none;"><div class=3D"goog-menuitem-content" sty=
le=3D"user-select: none;"><!--?lit$516311766$-->Run all<!--?lit$516311766$-=
-></div></div><div command=3D"runbefore" class=3D" goog-menuitem " role=3D"=
menuitem" id=3D":23" style=3D"user-select: none;"><div class=3D"goog-menuit=
em-content" style=3D"user-select: none;"><!--?lit$516311766$-->Run before<!=
--?lit$516311766$--></div></div><div command=3D"runfocused" class=3D" goog-=
menuitem " role=3D"menuitem" id=3D":24" style=3D"user-select: none;"><div c=
lass=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$516311=
766$-->Run the focused cell<!--?lit$516311766$--></div></div><div command=
=3D"runselected" class=3D" goog-menuitem " role=3D"menuitem" id=3D":25" sty=
le=3D"user-select: none;"><div class=3D"goog-menuitem-content" style=3D"use=
r-select: none;"><!--?lit$516311766$-->Run selection<!--?lit$516311766$--><=
/div></div><div command=3D"runafter" class=3D" goog-menuitem " role=3D"menu=
item" id=3D":26" style=3D"user-select: none;"><div class=3D"goog-menuitem-c=
ontent" style=3D"user-select: none;"><!--?lit$516311766$-->Run cell and bel=
ow<!--?lit$516311766$--></div></div><div class=3D"goog-menuseparator goog-m=
enuitem-disabled" aria-disabled=3D"true" role=3D"separator" id=3D":27" styl=
e=3D"user-select: none;"></div><div command=3D"interrupt" class=3D" goog-me=
nuitem " role=3D"menuitem" id=3D":28" style=3D"user-select: none;"><div cla=
ss=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$51631176=
6$-->Interrupt execution<!--?lit$516311766$--></div></div><div command=3D"r=
estart" class=3D" goog-menuitem " role=3D"menuitem" id=3D":29" style=3D"use=
r-select: none;"><div class=3D"goog-menuitem-content" style=3D"user-select:=
 none;"><!--?lit$516311766$-->Restart session<!--?lit$516311766$--></div></=
div><div command=3D"restart-and-run-all" class=3D" goog-menuitem " role=3D"=
menuitem" id=3D":2a" style=3D"user-select: none;"><div class=3D"goog-menuit=
em-content" style=3D"user-select: none;"><!--?lit$516311766$-->Restart sess=
ion and run all<!--?lit$516311766$--></div></div><div command=3D"powerwash-=
current-vm" class=3D" goog-menuitem " role=3D"menuitem" id=3D":2b" style=3D=
"user-select: none;"><div class=3D"goog-menuitem-content" style=3D"user-sel=
ect: none;"><!--?lit$516311766$-->Disconnect and delete runtime<!--?lit$516=
311766$--></div></div><div class=3D"goog-menuseparator goog-menuitem-disabl=
ed" aria-disabled=3D"true" role=3D"separator" id=3D":2c" style=3D"user-sele=
ct: none;"></div><div command=3D"change-runtime-type" class=3D" goog-menuit=
em " role=3D"menuitem" id=3D":2d" style=3D"user-select: none;"><div class=
=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766$=
-->Change runtime type<!--?lit$516311766$--></div></div><div class=3D"goog-=
menuseparator goog-menuitem-disabled" aria-disabled=3D"true" role=3D"separa=
tor" id=3D":2e" style=3D"user-select: none;"></div><div command=3D"manage-s=
essions" class=3D" goog-menuitem " role=3D"menuitem" id=3D":2f" style=3D"us=
er-select: none;"><div class=3D"goog-menuitem-content" style=3D"user-select=
: none;"><!--?lit$516311766$-->Manage sessions<!--?lit$516311766$--></div><=
/div><div command=3D"open-resource-viewer" class=3D" goog-menuitem " role=
=3D"menuitem" id=3D":2g" style=3D"user-select: none;"><div class=3D"goog-me=
nuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->View res=
ources<!--?lit$516311766$--></div></div><div command=3D"view-runtime-logs" =
class=3D" goog-menuitem " role=3D"menuitem" id=3D":2h" style=3D"user-select=
: none;"><div class=3D"goog-menuitem-content" style=3D"user-select: none;">=
<!--?lit$516311766$-->View runtime logs<!--?lit$516311766$--></div></div><d=
iv class=3D"goog-menuseparator goog-menuitem-disabled" aria-disabled=3D"tru=
e" role=3D"separator" id=3D":2i" style=3D"user-select: none;"></div><div co=
mmand=3D"deploy-cloud-run" class=3D" goog-menuitem " role=3D"menuitem" id=
=3D":2j" style=3D"user-select: none;"><div class=3D"goog-menuitem-content" =
style=3D"user-select: none;"><!--?lit$516311766$-->Deploy to Google Cloud R=
un<!--?lit$516311766$--></div></div></div><div class=3D"goog-menu" id=3D"to=
ols-menu" role=3D"menu" aria-haspopup=3D"true" style=3D"display: none; user=
-select: none;"><!--?lit$516311766$--><div command=3D"show-command-palette"=
 class=3D" goog-menuitem " role=3D"menuitem" id=3D":2l" style=3D"user-selec=
t: none;"><div class=3D"goog-menuitem-content" style=3D"user-select: none;"=
><!--?lit$516311766$-->Command palette<!--?lit$516311766$--></div></div><di=
v class=3D"goog-menuseparator goog-menuitem-disabled" aria-disabled=3D"true=
" role=3D"separator" id=3D":2m" style=3D"user-select: none;"></div><div com=
mand=3D"preferences" class=3D" goog-menuitem " role=3D"menuitem" id=3D":2n"=
 style=3D"user-select: none;"><div class=3D"goog-menuitem-content" style=3D=
"user-select: none;"><!--?lit$516311766$-->Settings<!--?lit$516311766$--></=
div></div><div command=3D"shortcuts" class=3D" goog-menuitem " role=3D"menu=
item" id=3D":2o" style=3D"user-select: none;"><div class=3D"goog-menuitem-c=
ontent" style=3D"user-select: none;"><!--?lit$516311766$-->Keyboard shortcu=
ts<!--?lit$516311766$--></div></div><div class=3D"goog-menuseparator goog-m=
enuitem-disabled" aria-disabled=3D"true" role=3D"separator" id=3D":2p" styl=
e=3D"user-select: none;"></div><div command=3D"open-differ" class=3D" goog-=
menuitem " role=3D"menuitem" id=3D":2q" style=3D"user-select: none;"><div c=
lass=3D"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$516311=
766$-->Diff notebooks<!--?lit$516311766$--> <span class=3D"screenreader-onl=
y" style=3D"user-select: none;"><!--?lit$516311766$-->(opens in a new tab)<=
/span></div></div></div><div class=3D"goog-menu" id=3D"help-menu" role=3D"m=
enu" aria-haspopup=3D"true" style=3D"display: none; user-select: none;"><!-=
-?lit$516311766$--><div command=3D"faq" class=3D" goog-menuitem " role=3D"m=
enuitem" id=3D":2s" style=3D"user-select: none;"><div class=3D"goog-menuite=
m-content" style=3D"user-select: none;"><!--?lit$516311766$-->Frequently as=
ked questions<!--?lit$516311766$--></div></div><div command=3D"view-relnote=
s" class=3D" goog-menuitem " role=3D"menuitem" id=3D":2t" style=3D"user-sel=
ect: none;"><div class=3D"goog-menuitem-content" style=3D"user-select: none=
;"><!--?lit$516311766$-->View release notes<!--?lit$516311766$--></div></di=
v><div command=3D"snippets" class=3D" goog-menuitem " role=3D"menuitem" id=
=3D":2u" style=3D"user-select: none;"><div class=3D"goog-menuitem-content" =
style=3D"user-select: none;"><!--?lit$516311766$-->Search code snippets<!--=
?lit$516311766$--></div></div><div class=3D"goog-menuseparator goog-menuite=
m-disabled" aria-disabled=3D"true" role=3D"separator" id=3D":2v" style=3D"u=
ser-select: none;"></div><div command=3D"report-bug" class=3D" goog-menuite=
m " role=3D"menuitem" id=3D":2w" style=3D"user-select: none;"><div class=3D=
"goog-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->=
Report a bug<!--?lit$516311766$--></div></div><div command=3D"report-abuse"=
 class=3D" goog-menuitem " role=3D"menuitem" id=3D":2x" style=3D"user-selec=
t: none;"><div class=3D"goog-menuitem-content" style=3D"user-select: none;"=
><!--?lit$516311766$-->Report Drive abuse<!--?lit$516311766$--></div></div>=
<div command=3D"send-feedback" class=3D" goog-menuitem " role=3D"menuitem" =
id=3D":2y" style=3D"user-select: none;"><div class=3D"goog-menuitem-content=
" style=3D"user-select: none;"><!--?lit$516311766$-->Send feedback<!--?lit$=
516311766$--></div></div><div command=3D"view-tos" class=3D" goog-menuitem =
" role=3D"menuitem" id=3D":2z" style=3D"user-select: none;"><div class=3D"g=
oog-menuitem-content" style=3D"user-select: none;"><!--?lit$516311766$-->Vi=
ew terms of service<!--?lit$516311766$--></div></div></div><dialog class=3D=
"doc-comments-area" aria-label=3D"Comments"><!----><div class=3D"doc-commen=
ts-buttons">
        <md-text-button command=3D"add-comment" value=3D"" has-icon=3D""><t=
emplate shadowmode=3D"open" shadowdelegatesfocus=3D""><!---->
      <!--?lit$516311766$-->
      <div class=3D"background"></div>
      <md-focus-ring part=3D"focus-ring" for=3D"button" aria-hidden=3D"true=
"><template shadowmode=3D"open"><!----></template></md-focus-ring>
      <md-ripple part=3D"ripple" for=3D"button" aria-hidden=3D"true"><templ=
ate shadowmode=3D"open"><!----><div class=3D"surface   "></div></template><=
/md-ripple>
      <!--?lit$516311766$--><button id=3D"button" class=3D"button">
      <!--?lit$516311766$-->
      <span class=3D"touch"></span>
      <!--?lit$516311766$--><slot name=3D"icon"></slot>
      <span class=3D"label"><slot></slot></span>
      <!--?lit$516311766$-->
   =20
    </button>
    </template>
          <md-icon slot=3D"icon" filled=3D"" aria-hidden=3D"true"><template=
 shadowmode=3D"open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$516311766$-->Add a comment
        </md-text-button>
      </div></dialog><div class=3D"thumbnail"></div><div class=3D"monaco-ar=
ia-container"><div class=3D"monaco-alert" role=3D"alert" aria-atomic=3D"tru=
e"></div><div class=3D"monaco-alert" role=3D"alert" aria-atomic=3D"true"></=
div><div class=3D"monaco-status" role=3D"complementary" aria-live=3D"polite=
" aria-atomic=3D"true"></div><div class=3D"monaco-status" role=3D"complemen=
tary" aria-live=3D"polite" aria-atomic=3D"true"></div></div><iframe id=3D"a=
piproxy0d36475035724b5fbf2810b397f43388795b25f80.207616108" name=3D"apiprox=
y0d36475035724b5fbf2810b397f43388795b25f80.207616108" src=3D"cid:frame-6681=
D917E1B9596489F12ED8670F4EC6@mhtml.blink" tabindex=3D"-1" aria-hidden=3D"tr=
ue" style=3D"width: 1px; height: 1px; position: absolute; top: -100px; disp=
lay: none;"></iframe><span id=3D"PING_IFRAME_FORM_DETECTION" style=3D"displ=
ay: none;"></span><iframe src=3D"cid:frame-CA6BC816279D3EABBACD8934FB5B9764=
@mhtml.blink" style=3D"display: none;"></iframe><div><div class=3D"grecaptc=
ha-badge" data-style=3D"bottomright" style=3D"width: 256px; height: 60px; p=
osition: fixed; visibility: hidden; display: block; transition: right 0.3s;=
 bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: =
2px; overflow: hidden;"><div class=3D"grecaptcha-logo"><iframe title=3D"reC=
APTCHA" width=3D"256" height=3D"60" role=3D"presentation" name=3D"a-ro24hd2=
pt33s" frameborder=3D"0" scrolling=3D"no" sandbox=3D"allow-forms allow-popu=
ps allow-same-origin allow-scripts allow-top-navigation allow-modals allow-=
popups-to-escape-sandbox allow-storage-access-by-user-activation" src=3D"ci=
d:frame-6FEA70ED9138E49B32952BF767C4F156@mhtml.blink"></iframe></div><div c=
lass=3D"grecaptcha-error"></div><textarea id=3D"g-recaptcha-response-100000=
" name=3D"g-recaptcha-response" class=3D"g-recaptcha-response" style=3D"wid=
th: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px=
 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe=
 style=3D"display: none;"></iframe></div><span id=3D"PING_CONTENT_DLS_POPUP=
" style=3D"display: none;"></span><div style=3D"background-color: transpare=
nt; border: none; bottom: 15px; display: block; margin: 0px; opacity: 1; pa=
dding: 0px; position: fixed; right: 15px; z-index: 2147483647;"><template s=
hadowmode=3D"closed"><div class=3D"dls__container">
  <div class=3D"shield" style=3D"background: transparent; opacity: 0.1; dis=
play: none;">
    <div class=3D"shield__circle" style=3D"opacity: 1;">
      <img src=3D"chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/image=
s/download_scan/mcafee_logo_white.svg?secret=3Dql650y" x-mcsrc=3D"" id=3D"d=
ls_ballon_icon" x-mcsrcparsed=3D"true">
    </div>
    <div class=3D"dls__popup__expanded" style=3D"opacity: 0;">
      <img src=3D"chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/image=
s/download_scan/download_scan_icon.svg?secret=3Dql650y" x-mcsrc=3D"" class=
=3D"dls__icon" x-mcsrcparsed=3D"true">
      <div class=3D"content">
        <div class=3D"content__images">
          <img src=3D"chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/i=
mages/download_scan/mcafee_logo_red.svg?secret=3Dql650y" x-mcsrc=3D"" id=3D=
"dls_mcafee_logo" x-mcsrcparsed=3D"true">
          <img src=3D"chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/i=
mages/download_scan/seperator_line.svg?secret=3Dql650y" x-mcsrc=3D"" class=
=3D"seperator__line" x-mcsrcparsed=3D"true">
          <img src=3D"chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/i=
mages/download_scan/webadvisor.svg?secret=3Dql650y" x-mcsrc=3D"" x-mcsrcpar=
sed=3D"true">
          <img src=3D"chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/i=
mages/download_scan/close-outline.svg?secret=3Dql650y" x-mcsrc=3D"" id=3D"d=
ls_close_icon" x-mcsrcparsed=3D"true">
        </div>
        <p id=3D"download_scan_popup_expanded_descriptions">Your download's=
 being scanned. We'll let you know if there's an issue.</p>
      </div>
    </div>
  </div>
</div></template></div><colab-callout dismisstext=3D"" tooltipstyling=3D"" =
aria-label=3D"Rename notebook" opened=3D"" role=3D"tooltip" verticaldirecti=
on=3D"below" horizontaldirection=3D"right" style=3D"visibility: visible; to=
p: 38px; left: 137.588px;"><template shadowmode=3D"open"><!----> <div id=3D=
"content"><slot name=3D"content"></slot></div>
      <!--?lit$516311766$--><!--?--></template>
      <!--?lit$516311766$--><div slot=3D"content"><!----><!--?lit$516311766=
$--><!----><div><!--?lit$516311766$-->Rename notebook</div><!----><!--?--><=
/div>
    </colab-callout></body><grammarly-desktop-integration data-grammarly-sh=
adow-root=3D"true"><template shadowmode=3D"open"><div aria-label=3D"grammar=
ly-integration" role=3D"group" tabindex=3D"-1" class=3D"grammarly-desktop-i=
ntegration" data-content=3D"{&quot;mode&quot;:&quot;limited&quot;,&quot;isA=
ctive&quot;:false,&quot;isUserDisabled&quot;:false}"></div></template></gra=
mmarly-desktop-integration><div id=3D"smartyContainer" style=3D"position: a=
bsolute; top: 0px; right: 0px; line-height: initial; z-index: 2147483647; w=
idth: auto; font-size: initial;"><template shadowmode=3D"open"></template><=
/div></html>
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: image/svg+xml
Content-Transfer-Encoding: quoted-printable
Content-Location: chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/close-outline.svg?secret=ql650y

<svg width=3D"12" height=3D"12" viewBox=3D"0 0 12 12" fill=3D"none" xmlns=
=3D"http://www.w3.org/2000/svg">
<path d=3D"M11.4671 1.1549L10.3122 0L5.73355 4.57865L1.1549 0L0 1.1549L4.57=
865 5.73355L0 10.3122L1.1549 11.4671L5.73355 6.88845L10.3122 11.4671L11.467=
1 10.3122L6.88845 5.73355L11.4671 1.1549Z" fill=3D"#6E6E6E"/>
</svg>

------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: image/svg+xml
Content-Transfer-Encoding: quoted-printable
Content-Location: chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/webadvisor.svg?secret=ql650y

<svg width=3D"64" height=3D"10" viewBox=3D"0 0 64 10" fill=3D"none" xmlns=
=3D"http://www.w3.org/2000/svg">
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M8.12091 9.7761H7.18=
323L5.53671 4.1395C5.45857 3.89001 5.37113 3.57527 5.27438 3.19527C5.17764 =
2.81527 5.1274 2.5869 5.12368 2.51013C5.04182 3.01679 4.91159 3.57143 4.732=
98 4.17405L3.13669 9.7761H2.19901L0.027832 1.35863H1.03249L2.3218 6.55766C2=
.50041 7.28695 2.63064 7.94713 2.7125 8.53824C2.81297 7.83582 2.96181 7.148=
76 3.15902 6.47705L4.62135 1.35863H5.62601L7.16091 6.52311C7.33951 7.11806 =
7.49021 7.78976 7.613 8.53824C7.6837 7.99319 7.81765 7.32917 8.01486 6.5461=
4L9.29859 1.35863H10.3033L8.12091 9.7761ZM13.7973 9.89105C12.8931 9.89105 1=
2.1796 9.60702 11.6568 9.03894C11.134 8.47086 10.8726 7.68209 10.8726 6.672=
6C10.8726 5.65544 11.1154 4.84748 11.601 4.24869C12.0866 3.64991 12.7387 3.=
35052 13.5573 3.35052C14.3238 3.35052 14.9303 3.61057 15.3768 4.13066C15.82=
33 4.65076 16.0466 5.33686 16.0466 6.18897V6.79351H11.8326C11.8512 7.53431 =
12.0326 8.09662 12.3768 8.48046C12.721 8.8643 13.2056 9.05621 13.8308 9.056=
21C14.4894 9.05621 15.1405 8.91419 15.7843 8.63016V9.48227C15.4568 9.62813 =
15.147 9.73272 14.855 9.79605C14.5629 9.85938 14.2103 9.89105 13.7973 9.891=
05ZM13.5459 4.15117C13.0548 4.15117 12.6632 4.31622 12.3711 4.64632C12.079 =
4.97642 11.9069 5.43317 11.8548 6.0166H15.0529C15.0529 5.41398 14.9227 4.95=
243 14.6622 4.63192C14.4018 4.31142 14.0297 4.15117 13.5459 4.15117ZM20.472=
6 3.3622C21.2763 3.3622 21.9005 3.64528 22.3452 4.21143C22.7898 4.77759 23.=
0122 5.57884 23.0122 6.61519C23.0122 7.65155 22.788 8.45663 22.3396 9.03047=
C21.8912 9.6043 21.2689 9.89121 20.4726 9.89121C20.0745 9.89121 19.7107 9.8=
1541 19.3814 9.66379C19.0521 9.51218 18.7759 9.279 18.5526 8.96426H18.4856L=
18.2903 9.77606H17.6261V0.817383H18.5526V2.99372C18.5526 3.48119 18.5377 3.=
91876 18.5079 4.30643H18.5526C18.9842 3.67694 19.6242 3.3622 20.4726 3.3622=
ZM20.3389 4.1626C19.7063 4.1626 19.2505 4.34971 18.9714 4.72395C18.6924 5.0=
9819 18.5528 5.72863 18.5528 6.61529C18.5528 7.50196 18.6961 8.13623 18.982=
6 8.51815C19.2691 8.90007 19.7287 9.09102 20.3612 9.09102C20.9305 9.09102 2=
1.3547 8.87704 21.6338 8.44906C21.9129 8.02108 22.0524 7.406 22.0524 6.6037=
8C22.0524 5.78237 21.9129 5.17016 21.6338 4.76714C21.3547 4.36411 20.9231 4=
.1626 20.3389 4.1626ZM29.8995 9.77594L28.8837 7.0987H25.613L24.6083 9.77594=
H23.6483L26.8744 1.32393H27.6725L30.8819 9.77594H29.8995ZM28.5879 6.21798L2=
7.6391 3.60982C27.5163 3.27972 27.3897 2.87478 27.2595 2.39499C27.1776 2.76=
347 27.0604 3.16841 26.9079 3.60982L25.9479 6.21798H28.5879ZM36.0283 8.9297=
1H35.978C35.5501 9.57072 34.9101 9.89121 34.058 9.89121C33.258 9.89121 32.6=
357 9.6091 32.191 9.04486C31.7464 8.48062 31.5241 7.67842 31.5241 6.63822C3=
1.5241 5.59803 31.7473 4.79007 32.1938 4.21431C32.6403 3.63856 33.2617 3.35=
069 34.058 3.35069C34.8878 3.35069 35.5241 3.66159 35.9669 4.2834H36.0394L3=
6.0004 3.82856L35.978 3.38523V0.817383H36.9045V9.77606H36.1511L36.0283 8.92=
971ZM34.175 9.09111C34.8076 9.09111 35.2662 8.91359 35.5508 8.55855C35.8355=
 8.2035 35.9778 7.63063 35.9778 6.83993V6.63842C35.9778 5.74408 35.8336 5.1=
0596 35.5452 4.72404C35.2569 4.34213 34.7964 4.15117 34.1638 4.15117C33.620=
6 4.15117 33.2048 4.369 32.9164 4.80465C32.628 5.2403 32.4838 5.85539 32.48=
38 6.64993C32.4838 7.45599 32.6271 8.06436 32.9136 8.47506C33.2001 8.88577 =
33.6206 9.09111 34.175 9.09111ZM40.2084 9.77585L37.8865 3.46563H38.88L40.19=
73 7.208C40.4949 8.08315 40.6698 8.65122 40.7219 8.91223H40.7666C40.8075 8.=
70879 40.9368 8.28754 41.1545 7.64845C41.3721 7.00937 41.8605 5.61511 42.61=
96 3.46563H43.6131L41.2912 9.77585H40.2084ZM45.5221 9.77585H44.5956V3.46563=
H45.5221V9.77585ZM44.5173 1.75582C44.5173 1.53703 44.5694 1.37678 44.6736 1=
.27507C44.7777 1.17335 44.908 1.12249 45.0642 1.12249C45.2131 1.12249 45.34=
14 1.17431 45.4494 1.27795C45.5573 1.38158 45.6112 1.54087 45.6112 1.75582C=
45.6112 1.97077 45.5573 2.13102 45.4494 2.23657C45.3414 2.34213 45.2131 2.3=
9491 45.0642 2.39491C44.908 2.39491 44.7777 2.34213 44.6736 2.23657C44.5694=
 2.13102 44.5173 1.97077 44.5173 1.75582ZM51.4329 8.05441C51.4329 8.64167 5=
1.2208 9.09459 50.7966 9.41318C50.3724 9.73176 49.7771 9.89105 49.0106 9.89=
105C48.1994 9.89105 47.5668 9.75863 47.1129 9.49378V8.60713C47.4068 8.76066=
 47.7222 8.88157 48.0589 8.96985C48.3957 9.05813 48.7203 9.10227 49.0329 9.=
10227C49.5166 9.10227 49.8887 9.02263 50.1492 8.86333C50.4096 8.70404 50.53=
99 8.46127 50.5399 8.13501C50.5399 7.88936 50.4366 7.67921 50.2301 7.50456C=
50.0236 7.32992 49.6208 7.12361 49.0217 6.88563C48.4524 6.66684 48.0478 6.4=
7589 47.8078 6.31276C47.5678 6.14963 47.3892 5.96443 47.2719 5.75716C47.154=
7 5.54989 47.0961 5.30232 47.0961 5.01444C47.0961 4.5001 47.2989 4.0942 47.=
7045 3.79673C48.1101 3.49925 48.6664 3.35052 49.3733 3.35052C50.032 3.35052=
 50.6757 3.4887 51.3045 3.76506L50.9752 4.54233C50.3613 4.28132 49.805 4.15=
081 49.3064 4.15081C48.8673 4.15081 48.5361 4.22182 48.3129 4.36384C48.0896=
 4.50586 47.978 4.70161 47.978 4.95111C47.978 5.12 48.0199 5.26393 48.1036 =
5.38292C48.1873 5.50191 48.3222 5.61514 48.5082 5.72261C48.6943 5.83009 49.=
0515 5.98554 49.5799 6.18897C50.3054 6.4615 50.7957 6.73593 51.0506 7.0123C=
51.3054 7.28866 51.4329 7.63602 51.4329 8.05441ZM58.2201 6.61503C58.2201 7.=
64371 57.9689 8.44687 57.4666 9.02455C56.9642 9.60222 56.2703 9.89105 55.38=
47 9.89105C54.8377 9.89105 54.3521 9.75863 53.9279 9.49378C53.5037 9.22894 =
53.1763 8.84894 52.9456 8.3538C52.7149 7.85865 52.5995 7.27906 52.5995 6.61=
503C52.5995 5.58635 52.8488 4.7851 53.3475 4.21127C53.8461 3.63743 54.5382 =
3.35052 55.4238 3.35052C56.2796 3.35052 56.9596 3.64415 57.4638 4.23142C57.=
968 4.81869 58.2201 5.61322 58.2201 6.61503ZM53.5593 6.61529C53.5593 7.4213=
5 53.7156 8.03548 54.0281 8.4577C54.3407 8.87992 54.8002 9.09102 55.4068 9.=
09102C56.0133 9.09102 56.4738 8.88088 56.7882 8.46058C57.1026 8.04028 57.25=
98 7.42519 57.2598 6.61529C57.2598 5.81308 57.1026 5.20375 56.7882 4.78729C=
56.4738 4.37083 56.0096 4.1626 55.3956 4.1626C54.7891 4.1626 54.3314 4.3679=
5 54.0226 4.77865C53.7137 5.18935 53.5593 5.80156 53.5593 6.61529ZM62.6347 =
3.35052C62.9063 3.35052 63.15 3.37355 63.3658 3.41961L63.2375 4.30627C62.98=
44 4.24869 62.7612 4.2199 62.5677 4.2199C62.0728 4.2199 61.6495 4.42717 61.=
2979 4.84172C60.9463 5.25626 60.7704 5.77251 60.7704 6.39049V9.7759H59.8439=
V3.46567H60.6086L60.7146 4.63445H60.7593C60.9863 4.22374 61.2598 3.90708 61=
.5798 3.68446C61.8998 3.46183 62.2514 3.35052 62.6347 3.35052Z" fill=3D"#C0=
1818"/>
</svg>

------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: image/svg+xml
Content-Transfer-Encoding: quoted-printable
Content-Location: chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/seperator_line.svg?secret=ql650y

<svg width=3D"1" height=3D"13" viewBox=3D"0 0 1 13" fill=3D"none" xmlns=3D"=
http://www.w3.org/2000/svg">
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M0.571726 11.6904V0.=
875681V11.6904Z" fill=3D"#FF1C1C"/>
<path d=3D"M0.571726 11.6904V0.875681" stroke=3D"#FF1C1C" stroke-width=3D"0=
.866667" stroke-linecap=3D"square"/>
</svg>

------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: image/svg+xml
Content-Transfer-Encoding: quoted-printable
Content-Location: chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/mcafee_logo_red.svg?secret=ql650y

<svg width=3D"76" height=3D"16" viewBox=3D"0 0 76 16" fill=3D"none" xmlns=
=3D"http://www.w3.org/2000/svg">
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M37.7977 9.90788L35.=
8231 8.69787L35.6761 8.93505C35.226 9.6643 34.6111 10.034 33.8486 10.0333C3=
2.5424 10.0328 31.5581 9.01666 31.5588 7.66935C31.5594 6.32276 32.5451 5.30=
793 33.8511 5.30848C34.6244 5.30921 35.2051 5.65942 35.6791 6.41113L35.8265=
 6.64466L37.8105 5.43209L37.6391 5.1761C36.6914 3.76032 35.4527 3.07214 33.=
8525 3.07105C30.8275 3.06958 29.1939 5.4383 29.1929 7.66788C29.1916 9.89783=
 30.8224 12.2687 33.8472 12.2702C35.3884 12.2711 36.8426 11.4628 37.6428 10=
.1604L37.7977 9.90788Z" fill=3D"#C01818"/>
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M43.3073 4.8923L44.4=
124 7.75346L42.187 7.75219L43.3073 4.8923ZM37.6988 12.2726L40.4293 12.274L4=
1.2405 10.1933L45.3379 10.1953L46.1468 12.2773L48.889 12.2792L43.9977 0.082=
4538L41.5624 0.0808105L42.211 1.69781L37.6988 12.2726Z" fill=3D"#C01818"/>
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M50.0191 12.2794L52.=
415 12.2809L52.418 6.80706L53.9803 6.80815L53.9815 4.51174L52.4193 4.51083L=
52.4198 3.42552C52.42 2.95974 52.7224 2.46511 53.283 2.46547C53.5907 2.4656=
6 53.7766 2.51989 53.9619 2.60168L54.2285 2.72018L55.224 0.479462L54.9371 0=
.358589C54.492 0.17034 53.8717 0.102783 53.4392 0.102418C52.3529 0.10187 51=
.4573 0.468142 50.8487 1.16143C50.3175 1.76671 50.0244 2.60862 50.0237 3.53=
124L50.0232 4.50937L48.9654 4.50882L48.9642 6.80541L50.0221 6.80559L50.0191=
 12.2794Z" fill=3D"#C01818"/>
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M17.8979 0.0106201V1=
2.261L20.5011 12.2628L20.505 5.25912L23.0282 7.19748L25.5533 5.25912V12.265=
8L28.1526 12.267L28.1594 0.0106201L23.0298 4.00748L17.8979 0.0106201Z" fill=
=3D"#C01818"/>
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M57.2864 6.56615C57.=
5992 5.73045 58.2739 5.24257 59.1459 5.24294C60.0272 5.24348 60.7151 5.7213=
2 61.0798 6.56834L57.2864 6.56615ZM59.376 3.11328C56.3604 3.11164 54.7314 5=
.47378 54.73 7.69661C54.7291 9.92017 56.3553 12.2834 59.3711 12.2852H59.372=
5H59.3744C60.7573 12.2699 62.0541 11.6201 63.0579 10.4482L61.1038 9.34922C6=
0.6029 9.87836 59.9943 10.1566 59.3229 10.1563C58.3388 10.1555 57.4664 9.47=
94 57.2381 8.59494L63.7543 8.59841L63.7547 7.98839C63.7566 4.62767 61.1954 =
3.11438 59.376 3.11328Z" fill=3D"#C01818"/>
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M67.0804 6.57129C67.=
3931 5.73558 68.0673 5.24752 68.9399 5.24807C69.8212 5.24862 70.5091 5.7264=
5 70.8738 6.57348L67.0804 6.57129ZM69.1698 3.11878C66.1538 3.11695 64.5253 =
5.47909 64.5239 7.7021C64.5229 9.92566 66.1487 12.2889 69.1648 12.2907H69.1=
662H69.1678C70.5512 12.2754 71.8481 11.6252 72.8517 10.4537L70.8976 9.35471=
C70.3963 9.88385 69.7881 10.1621 69.1168 10.1617C68.1325 10.161 67.2599 9.4=
8489 67.0319 8.60044L73.5481 8.60391L73.5486 7.99388C73.5506 4.63298 70.989=
1 3.11987 69.1698 3.11878Z" fill=3D"#C01818"/>
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M73.2422 2.70959H74.=
2565V2.90496H73.8581V4.00141H73.6389V2.90496H73.2422V2.70959Z" fill=3D"#C01=
818"/>
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M74.3988 2.70959H74.=
7076L75.0532 3.72113H75.0568L75.3937 2.70959H75.6989V4.00141H75.4902V3.0044=
7H75.4865L75.1394 4.00141H74.9585L74.6109 3.00447H74.6076V4.00141H74.3988V2=
.70959Z" fill=3D"#C01818"/>
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M2.63757 10.4604V4.2=
526L6.4351 6.06369V3.0687L0 0.00012207V12.1965L6.4351 15.2676V12.2722L2.637=
57 10.4604Z" fill=3D"#C01818"/>
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M10.2328 10.4603V4.2=
5248L6.4353 6.06357V3.06858L12.8704 0V12.1963L6.4353 15.2675V12.2721L10.232=
8 10.4603Z" fill=3D"#C01818"/>
</svg>

------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: image/svg+xml
Content-Transfer-Encoding: quoted-printable
Content-Location: chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/download_scan_icon.svg?secret=ql650y

<svg width=3D"73" height=3D"65" viewBox=3D"0 0 73 65" fill=3D"none" xmlns=
=3D"http://www.w3.org/2000/svg">
<rect width=3D"72.7844" height=3D"65" fill=3D"white"/>
<path d=3D"M62.6649 32.891C62.6649 47.186 51.0766 58.7743 36.7817 58.7743C2=
2.4868 58.7743 10.8984 47.186 10.8984 32.891C10.8984 18.5961 22.4868 7.0078=
1 36.7817 7.00781C51.0766 7.00781 62.6649 18.5961 62.6649 32.891ZM17.1182 3=
2.891C17.1182 43.7509 25.9218 52.5545 36.7817 52.5545C47.6415 52.5545 56.44=
52 43.7509 56.4452 32.891C56.4452 22.0312 47.6415 13.2276 36.7817 13.2276C2=
5.9218 13.2276 17.1182 22.0312 17.1182 32.891Z" fill=3D"#4258FF"/>
<circle cx=3D"36.9763" cy=3D"55.6605" r=3D"3.11377" fill=3D"#4258FF"/>
<path fill-rule=3D"evenodd" clip-rule=3D"evenodd" d=3D"M42.0805 31.351L37.6=
252 35.8064L37.6249 23.356L35.549 23.356L35.5493 35.8071L31.0933 31.351L29.=
6255 32.8189L35.1191 38.3125C35.9297 39.1232 37.2441 39.1232 38.0548 38.312=
5L43.5484 32.8189L42.0805 31.351ZM27.2456 43.0765H45.9282V41.0007H27.2456V4=
3.0765Z" fill=3D"#4258FF"/>
</svg>

------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: image/svg+xml
Content-Transfer-Encoding: quoted-printable
Content-Location: chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/images/download_scan/mcafee_logo_white.svg?secret=ql650y

<svg width=3D"25" height=3D"30" viewBox=3D"0 0 25 30" fill=3D"none" xmlns=
=3D"http://www.w3.org/2000/svg">
<path stroke=3D"white" stroke-width=3D"0.15" d=3D"M5.23996 8.57177V20.1982L=
12.5768 23.5918V29.2021L0.144043 23.4498V0.606491L12.5768 6.35377V11.9634L5=
.23996 8.57177Z" fill=3D"white"/>
<path stroke=3D"white" stroke-width=3D"0.15" d=3D"M19.9137 8.5722V20.1986L1=
2.5768 23.5918V29.2021L25.0097 23.4502V0.606925L12.5768 6.35377V11.9634L19.=
9137 8.5722Z" fill=3D"white"/>
</svg>

------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: image/jpeg
Content-Transfer-Encoding: base64
Content-Location: https://lh3.googleusercontent.com/ogw/AF2bZyj7ZLC6_dpGKKxNuNCNW0BW-Z9huaPIL1m5tzZ74ZdIfX4=s32-c-mo

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
rY3sqSdwSfzGiNzuQBZPFF7Q/dcN8K//2Q==

------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: chrome-extension://fheoggkfdfchfphceeifdbepaooicaho/css/mcafee_fonts.css

@charset "utf-8";

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-T=
hin.ttf") format("truetype"); font-weight: 100; font-style: normal; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-T=
hinItalic.ttf") format("truetype"); font-weight: 100; font-style: italic; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-E=
xtraLight.ttf") format("truetype"); font-weight: 200; font-style: normal; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-E=
xtraLightItalic.ttf") format("truetype"); font-weight: 200; font-style: ita=
lic; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-L=
ight.ttf") format("truetype"); font-weight: 300; font-style: normal; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-L=
ightItalic.ttf") format("truetype"); font-weight: 300; font-style: italic; =
}

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-R=
egular.ttf") format("truetype"); font-weight: 400; font-style: normal; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-I=
talic.ttf") format("truetype"); font-weight: 400; font-style: italic; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-M=
edium.ttf") format("truetype"); font-weight: 500; font-style: normal; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-M=
ediumItalic.ttf") format("truetype"); font-weight: 500; font-style: italic;=
 }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-S=
emiBold.ttf") format("truetype"); font-weight: 600; font-style: normal; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-S=
emiBoldItalic.ttf") format("truetype"); font-weight: 600; font-style: itali=
c; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-B=
old.ttf") format("truetype"); font-weight: 700; font-style: normal; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-B=
oldItalic.ttf") format("truetype"); font-weight: 700; font-style: italic; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-E=
xtraBold.ttf") format("truetype"); font-weight: 800; font-style: normal; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-E=
xtraBoldItalic.ttf") format("truetype"); font-weight: 800; font-style: ital=
ic; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-B=
lack.ttf") format("truetype"); font-weight: 900; font-style: normal; }

@font-face { font-family: McAfeePoppins; src: url("../../../fonts/Poppins-B=
lackItalic.ttf") format("truetype"); font-weight: 900; font-style: italic; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: https://ssl.gstatic.com/colaboratory-static/common/b8629101fed591b8cb8c96c45ee6f083/js%2Fmonaco_editor%2F/vs/editor/editor.main.css

@charset "utf-8";

.monaco-action-bar { white-space: nowrap; height: 100%; }

.monaco-action-bar .actions-container { display: flex; margin: 0px auto; pa=
dding: 0px; height: 100%; width: 100%; align-items: center; }

.monaco-action-bar.vertical .actions-container { display: inline-block; }

.monaco-action-bar .action-item { display: block; align-items: center; just=
ify-content: center; cursor: pointer; position: relative; }

.monaco-action-bar .action-item.disabled { cursor: default; }

.monaco-action-bar .action-item .codicon, .monaco-action-bar .action-item .=
icon { display: block; }

.monaco-action-bar .action-item .codicon { display: flex; align-items: cent=
er; width: 16px; height: 16px; }

.monaco-action-bar .action-label { display: flex; font-size: 11px; padding:=
 3px; border-radius: 5px; }

.monaco-action-bar .action-item.disabled .action-label, .monaco-action-bar =
.action-item.disabled .action-label::before, .monaco-action-bar .action-ite=
m.disabled .action-label:hover { opacity: 0.6; }

.monaco-action-bar.vertical { text-align: left; }

.monaco-action-bar.vertical .action-item { display: block; }

.monaco-action-bar.vertical .action-label.separator { display: block; borde=
r-bottom: 1px solid rgb(187, 187, 187); padding-top: 1px; margin-left: 0.8e=
m; margin-right: 0.8em; }

.monaco-action-bar .action-item .action-label.separator { width: 1px; heigh=
t: 16px; cursor: default; min-width: 1px; padding: 0px; background-color: r=
gb(187, 187, 187); margin: 5px 4px !important; }

.secondary-actions .monaco-action-bar .action-label { margin-left: 6px; }

.monaco-action-bar .action-item.select-container { overflow: hidden; flex: =
1 1 0%; max-width: 170px; min-width: 60px; display: flex; align-items: cent=
er; justify-content: center; margin-right: 10px; }

.monaco-action-bar .action-item.action-dropdown-item { display: flex; }

.monaco-action-bar .action-item.action-dropdown-item > .action-dropdown-ite=
m-separator { display: flex; align-items: center; cursor: default; }

.monaco-action-bar .action-item.action-dropdown-item > .action-dropdown-ite=
m-separator > div { width: 1px; }

.monaco-aria-container { position: absolute; left: -999em; }

.monaco-text-button { box-sizing: border-box; display: flex; width: 100%; p=
adding: 4px; border-radius: 2px; text-align: center; cursor: pointer; justi=
fy-content: center; align-items: center; border: 1px solid var(--vscode-but=
ton-border,transparent); line-height: 18px; }

.monaco-text-button:focus { outline-offset: 2px !important; }

.monaco-text-button:hover { text-decoration: none !important; }

.monaco-button.disabled, .monaco-button.disabled:focus { opacity: 0.4 !impo=
rtant; cursor: default; }

.monaco-text-button .codicon { margin: 0px 0.2em; color: inherit !important=
; }

.monaco-text-button.monaco-text-button-with-short-label { flex-flow: wrap; =
padding: 0px 4px; overflow: hidden; height: 28px; }

.monaco-text-button.monaco-text-button-with-short-label > .monaco-button-la=
bel { flex-basis: 100%; }

.monaco-text-button.monaco-text-button-with-short-label > .monaco-button-la=
bel-short { flex-grow: 1; width: 0px; overflow: hidden; }

.monaco-text-button.monaco-text-button-with-short-label > .monaco-button-la=
bel, .monaco-text-button.monaco-text-button-with-short-label > .monaco-butt=
on-label-short { display: flex; justify-content: center; align-items: cente=
r; font-weight: 400; font-style: inherit; padding: 4px 0px; }

.monaco-button-dropdown { display: flex; cursor: pointer; }

.monaco-button-dropdown.disabled { cursor: default; }

.monaco-button-dropdown > .monaco-button:focus { outline-offset: -1px !impo=
rtant; }

.monaco-button-dropdown.disabled > .monaco-button-dropdown-separator, .mona=
co-button-dropdown.disabled > .monaco-button.disabled, .monaco-button-dropd=
own.disabled > .monaco-button.disabled:focus { opacity: 0.4 !important; }

.monaco-button-dropdown > .monaco-button.monaco-text-button { border-right-=
width: 0px !important; }

.monaco-button-dropdown .monaco-button-dropdown-separator { padding: 4px 0p=
x; cursor: default; }

.monaco-button-dropdown .monaco-button-dropdown-separator > div { height: 1=
00%; width: 1px; }

.monaco-button-dropdown > .monaco-button.monaco-dropdown-button { border-to=
p-color: ; border-top-style: ; border-top-width: ; border-right-color: ; bo=
rder-right-style: ; border-right-width: ; border-bottom-color: ; border-bot=
tom-style: ; border-bottom-width: ; border-left-color: ; border-left-style:=
 ; border-image-source: ; border-image-slice: ; border-image-width: ; borde=
r-image-outset: ; border-image-repeat: ; border-radius: 0px 2px 2px 0px; bo=
rder-left-width: 0px !important; }

.monaco-button-dropdown > .monaco-button.monaco-text-button { border-radius=
: 2px 0px 0px 2px; }

.monaco-description-button { display: flex; flex-direction: column; align-i=
tems: center; margin: 4px 5px; }

.monaco-description-button .monaco-button-description { font-style: italic;=
 font-size: 11px; padding: 4px 20px; }

.monaco-description-button .monaco-button-description, .monaco-description-=
button .monaco-button-label { display: flex; justify-content: center; align=
-items: center; }

.monaco-description-button .monaco-button-description > .codicon, .monaco-d=
escription-button .monaco-button-label > .codicon { margin: 0px 0.2em; colo=
r: inherit !important; }

.monaco-button-dropdown.default-colors > .monaco-button, .monaco-button.def=
ault-colors { color: var(--vscode-button-foreground); background-color: var=
(--vscode-button-background); }

.monaco-button-dropdown.default-colors > .monaco-button:hover, .monaco-butt=
on.default-colors:hover { background-color: var(--vscode-button-hoverBackgr=
ound); }

.monaco-button-dropdown.default-colors > .monaco-button.secondary, .monaco-=
button.default-colors.secondary { color: var(--vscode-button-secondaryForeg=
round); background-color: var(--vscode-button-secondaryBackground); }

.monaco-button-dropdown.default-colors > .monaco-button.secondary:hover, .m=
onaco-button.default-colors.secondary:hover { background-color: var(--vscod=
e-button-secondaryHoverBackground); }

.monaco-button-dropdown.default-colors .monaco-button-dropdown-separator { =
background-color: var(--vscode-button-background); border-top: 1px solid va=
r(--vscode-button-border); border-bottom: 1px solid var(--vscode-button-bor=
der); }

.monaco-button-dropdown.default-colors .monaco-button.secondary + .monaco-b=
utton-dropdown-separator { background-color: var(--vscode-button-secondaryB=
ackground); }

.monaco-button-dropdown.default-colors .monaco-button-dropdown-separator > =
div { background-color: var(--vscode-button-separator); }

@font-face { font-family: codicon; font-display: block; src: url("../base/b=
rowser/ui/codicons/codicon/codicon.ttf") format("truetype"); }

.codicon[class*=3D"codicon-"] { font: 16px / 1 codicon; display: inline-blo=
ck; text-decoration: none; text-rendering: auto; text-align: center; text-t=
ransform: none; -webkit-font-smoothing: antialiased; user-select: none; }

.codicon-wrench-subaction { opacity: 0.5; }

@keyframes codicon-spin {=20
  100% { transform: rotate(1turn); }
}

.codicon-gear.codicon-modifier-spin, .codicon-loading.codicon-modifier-spin=
, .codicon-notebook-state-executing.codicon-modifier-spin, .codicon-sync.co=
dicon-modifier-spin { animation: 1.5s steps(30) 0s infinite normal none run=
ning codicon-spin; }

.codicon-modifier-disabled { opacity: 0.4; }

.codicon-loading, .codicon-tree-item-loading::before { animation-duration: =
1s !important; animation-timing-function: cubic-bezier(0.53, 0.21, 0.29, 0.=
67) !important; }

.context-view { position: absolute; }

.context-view.fixed { color-scheme: initial; forced-color-adjust: initial; =
math-depth: initial; position: fixed; position-anchor: initial; text-size-a=
djust: initial; appearance: initial; color: inherit; font-family: inherit; =
font-feature-settings: initial; font-kerning: initial; font-language-overri=
de: initial; font-optical-sizing: initial; font-palette: initial; font-size=
: 13px; font-size-adjust: initial; font-stretch: initial; font-style: initi=
al; font-synthesis: initial; font-variant: initial; font-variation-settings=
: initial; font-weight: initial; position-area: initial; text-orientation: =
initial; text-rendering: initial; text-spacing-trim: initial; -webkit-font-=
smoothing: initial; -webkit-locale: initial; -webkit-text-orientation: init=
ial; -webkit-writing-mode: initial; writing-mode: initial; zoom: initial; a=
ccent-color: initial; place-content: initial; place-items: initial; place-s=
elf: initial; alignment-baseline: initial; anchor-name: initial; anchor-sco=
pe: initial; animation-composition: initial; animation: initial; animation-=
trigger: initial; app-region: initial; aspect-ratio: initial; backdrop-filt=
er: initial; backface-visibility: initial; background: initial; background-=
blend-mode: initial; baseline-shift: initial; baseline-source: initial; blo=
ck-size: initial; border-block: initial; border: initial; border-radius: in=
itial; border-collapse: initial; border-end-end-radius: initial; border-end=
-start-radius: initial; border-inline: initial; border-start-end-radius: in=
itial; border-start-start-radius: initial; inset: initial; box-decoration-b=
reak: initial; box-shadow: initial; box-sizing: initial; break-after: initi=
al; break-before: initial; break-inside: initial; buffered-rendering: initi=
al; caption-side: initial; caret-animation: initial; caret-color: initial; =
caret-shape: initial; clear: initial; clip: initial; clip-path: initial; cl=
ip-rule: initial; color-interpolation: initial; color-interpolation-filters=
: initial; color-rendering: initial; columns: initial; column-fill: initial=
; gap: initial; column-rule: initial; column-span: initial; contain: initia=
l; contain-intrinsic-block-size: initial; contain-intrinsic-size: initial; =
contain-intrinsic-inline-size: initial; container: initial; content: initia=
l; content-visibility: initial; corner-shape: initial; corner-block-end-sha=
pe: initial; corner-block-start-shape: initial; counter-increment: initial;=
 counter-reset: initial; counter-set: initial; cursor: initial; cx: initial=
; cy: initial; d: initial; display: initial; dominant-baseline: initial; dy=
namic-range-limit: initial; empty-cells: initial; field-sizing: initial; fi=
ll: initial; fill-opacity: initial; fill-rule: initial; filter: initial; fl=
ex: initial; flex-flow: initial; float: initial; flood-color: initial; floo=
d-opacity: initial; grid: initial; grid-area: initial; height: initial; hyp=
henate-character: initial; hyphenate-limit-chars: initial; hyphens: initial=
; image-orientation: initial; image-rendering: initial; initial-letter: ini=
tial; inline-size: initial; inset-block: initial; inset-inline: initial; in=
teractivity: initial; interest-delay: initial; interpolate-size: initial; i=
solation: initial; letter-spacing: initial; lighting-color: initial; line-b=
reak: initial; line-height: initial; list-style: initial; margin-block: ini=
tial; margin: initial; margin-inline: initial; marker: initial; mask: initi=
al; mask-type: initial; math-shift: initial; math-style: initial; max-block=
-size: initial; max-height: initial; max-inline-size: initial; max-width: i=
nitial; min-block-size: initial; min-height: initial; min-inline-size: init=
ial; min-width: initial; mix-blend-mode: initial; object-fit: initial; obje=
ct-position: initial; object-view-box: initial; offset: initial; opacity: i=
nitial; order: initial; orphans: initial; outline: initial; outline-offset:=
 initial; overflow-anchor: initial; overflow-block: initial; overflow-clip-=
margin: initial; overflow-inline: initial; overflow-wrap: initial; overflow=
: initial; overlay: initial; overscroll-behavior-block: initial; overscroll=
-behavior-inline: initial; overscroll-behavior: initial; padding-block: ini=
tial; padding: initial; padding-inline: initial; page: initial; page-orient=
ation: initial; paint-order: initial; perspective: initial; perspective-ori=
gin: initial; pointer-events: initial; position-try: initial; position-visi=
bility: initial; print-color-adjust: initial; quotes: initial; r: initial; =
reading-flow: initial; reading-order: initial; resize: initial; rotate: ini=
tial; ruby-align: initial; ruby-position: initial; rx: initial; ry: initial=
; scale: initial; scroll-behavior: initial; scroll-initial-target: initial;=
 scroll-margin-block: initial; scroll-margin: initial; scroll-margin-inline=
: initial; scroll-marker-group: initial; scroll-padding-block: initial; scr=
oll-padding: initial; scroll-padding-inline: initial; scroll-snap-align: in=
itial; scroll-snap-stop: initial; scroll-snap-type: initial; scroll-target-=
group: initial; scroll-timeline: initial; scrollbar-color: initial; scrollb=
ar-gutter: initial; scrollbar-width: initial; shape-image-threshold: initia=
l; shape-margin: initial; shape-outside: initial; shape-rendering: initial;=
 size: initial; speak: initial; stop-color: initial; stop-opacity: initial;=
 stroke: initial; stroke-dasharray: initial; stroke-dashoffset: initial; st=
roke-linecap: initial; stroke-linejoin: initial; stroke-miterlimit: initial=
; stroke-opacity: initial; stroke-width: initial; tab-size: initial; table-=
layout: initial; text-align: initial; text-align-last: initial; text-anchor=
: initial; text-autospace: initial; text-box: initial; text-combine-upright=
: initial; text-decoration: initial; text-decoration-skip-ink: initial; tex=
t-emphasis: initial; text-emphasis-position: initial; text-indent: initial;=
 text-justify: initial; text-overflow: initial; text-shadow: initial; text-=
transform: initial; text-underline-offset: initial; text-underline-position=
: initial; text-wrap: initial; timeline-scope: initial; timeline-trigger: i=
nitial; touch-action: initial; transform: initial; transform-box: initial; =
transform-origin: initial; transform-style: initial; transition: initial; t=
ranslate: initial; trigger-scope: initial; user-select: initial; vector-eff=
ect: initial; vertical-align: initial; view-timeline: initial; view-transit=
ion-class: initial; view-transition-group: initial; view-transition-name: i=
nitial; visibility: initial; border-spacing: initial; -webkit-box-align: in=
itial; -webkit-box-decoration-break: initial; -webkit-box-direction: initia=
l; -webkit-box-flex: initial; -webkit-box-ordinal-group: initial; -webkit-b=
ox-orient: initial; -webkit-box-pack: initial; -webkit-box-reflect: initial=
; -webkit-line-break: initial; -webkit-line-clamp: initial; -webkit-mask-bo=
x-image: initial; -webkit-rtl-ordering: initial; -webkit-ruby-position: ini=
tial; -webkit-tap-highlight-color: initial; -webkit-text-combine: initial; =
-webkit-text-decorations-in-effect: initial; -webkit-text-fill-color: initi=
al; -webkit-text-security: initial; -webkit-text-stroke: initial; -webkit-u=
ser-drag: initial; white-space-collapse: initial; widows: initial; width: i=
nitial; will-change: initial; word-break: initial; word-spacing: initial; x=
: initial; y: initial; z-index: initial; }

.monaco-count-badge { padding: 3px 6px; border-radius: 11px; font-size: 11p=
x; min-width: 18px; min-height: 18px; line-height: 11px; font-weight: 400; =
text-align: center; display: inline-block; box-sizing: border-box; }

.monaco-count-badge.long { padding: 2px 3px; border-radius: 2px; min-height=
: auto; line-height: normal; }

.monaco-dropdown { height: 100%; padding: 0px; }

.monaco-dropdown > .dropdown-label { cursor: pointer; height: 100%; display=
: flex; align-items: center; justify-content: center; }

.monaco-dropdown > .dropdown-label > .action-label.disabled { cursor: defau=
lt; }

.monaco-dropdown-with-primary { flex-direction: row; border-radius: 5px; di=
splay: flex !important; }

.monaco-dropdown-with-primary > .action-container > .action-label { margin-=
right: 0px; }

.monaco-dropdown-with-primary > .dropdown-action-container > .monaco-dropdo=
wn > .dropdown-label .codicon[class*=3D"codicon-"] { font-size: 12px; paddi=
ng-left: 0px; padding-right: 0px; line-height: 16px; margin-left: -3px; }

.monaco-dropdown-with-primary > .dropdown-action-container > .monaco-dropdo=
wn > .dropdown-label > .action-label { display: block; background-size: 16p=
x; background-position: 50% center; background-repeat: no-repeat; }

.monaco-findInput { position: relative; }

.monaco-findInput .monaco-inputbox { font-size: 13px; width: 100%; }

.monaco-findInput > .controls { position: absolute; top: 3px; right: 2px; }

.vs .monaco-findInput.disabled { background-color: rgb(225, 225, 225); }

.vs-dark .monaco-findInput.disabled { background-color: rgb(51, 51, 51); }

.hc-light .monaco-findInput.highlight-0 .controls, .monaco-findInput.highli=
ght-0 .controls { animation: 0.1s linear 0s 1 normal none running monaco-fi=
ndInput-highlight-0; }

.hc-light .monaco-findInput.highlight-1 .controls, .monaco-findInput.highli=
ght-1 .controls { animation: 0.1s linear 0s 1 normal none running monaco-fi=
ndInput-highlight-1; }

.hc-black .monaco-findInput.highlight-0 .controls, .vs-dark .monaco-findInp=
ut.highlight-0 .controls { animation: 0.1s linear 0s 1 normal none running =
monaco-findInput-highlight-dark-0; }

.hc-black .monaco-findInput.highlight-1 .controls, .vs-dark .monaco-findInp=
ut.highlight-1 .controls { animation: 0.1s linear 0s 1 normal none running =
monaco-findInput-highlight-dark-1; }

@keyframes monaco-findInput-highlight-0 {=20
  0% { background: rgba(253, 255, 0, 0.8); }
  100% { background: transparent; }
}

@keyframes monaco-findInput-highlight-1 {=20
  0% { background: rgba(253, 255, 0, 0.8); }
  99% { background: transparent; }
}

@keyframes monaco-findInput-highlight-dark-0 {=20
  0% { background: rgba(255, 255, 255, 0.44); }
  100% { background: transparent; }
}

@keyframes monaco-findInput-highlight-dark-1 {=20
  0% { background: rgba(255, 255, 255, 0.44); }
  99% { background: transparent; }
}

.monaco-hover { cursor: default; position: absolute; overflow: hidden; user=
-select: text; box-sizing: border-box; animation: 0.1s linear 0s 1 normal n=
one running fadein; line-height: 1.5em; }

.monaco-hover.hidden { display: none; }

.monaco-hover a:hover:not(.disabled) { cursor: pointer; }

.monaco-hover .hover-contents:not(.html-hover-contents) { padding: 4px 8px;=
 }

.monaco-hover .markdown-hover > .hover-contents:not(.code-hover-contents) {=
 max-width: 500px; overflow-wrap: break-word; }

.monaco-hover .markdown-hover > .hover-contents:not(.code-hover-contents) h=
r { min-width: 100%; }

.monaco-hover .code, .monaco-hover h1, .monaco-hover h2, .monaco-hover h3, =
.monaco-hover h4, .monaco-hover h5, .monaco-hover h6, .monaco-hover p, .mon=
aco-hover ul { margin: 8px 0px; }

.monaco-hover h1, .monaco-hover h2, .monaco-hover h3, .monaco-hover h4, .mo=
naco-hover h5, .monaco-hover h6 { line-height: 1.1; }

.monaco-hover code { font-family: var(--monaco-monospace-font); }

.monaco-hover hr { box-sizing: border-box; border-left: 0px; border-right: =
0px; margin: 4px -8px -4px; height: 1px; }

.monaco-hover .code:first-child, .monaco-hover p:first-child, .monaco-hover=
 ul:first-child { margin-top: 0px; }

.monaco-hover .code:last-child, .monaco-hover p:last-child, .monaco-hover u=
l:last-child { margin-bottom: 0px; }

.monaco-hover ol, .monaco-hover ul { padding-left: 20px; }

.monaco-hover li > p { margin-bottom: 0px; }

.monaco-hover li > ul { margin-top: 0px; }

.monaco-hover code { border-radius: 3px; padding: 0px 0.4em; }

.monaco-hover .monaco-tokenized-source { white-space: pre-wrap; }

.monaco-hover .hover-row.status-bar { font-size: 12px; line-height: 22px; }

.monaco-hover .hover-row.status-bar .info { font-style: italic; padding: 0p=
x 8px; }

.monaco-hover .hover-row.status-bar .actions { display: flex; padding: 0px =
8px; }

.monaco-hover .hover-row.status-bar .actions .action-container { margin-rig=
ht: 16px; cursor: pointer; }

.monaco-hover .hover-row.status-bar .actions .action-container .action .ico=
n { padding-right: 4px; }

.monaco-hover .markdown-hover .hover-contents .codicon { color: inherit; fo=
nt-size: inherit; vertical-align: middle; }

.monaco-hover .hover-contents a.code-link, .monaco-hover .hover-contents a.=
code-link:hover { color: inherit; }

.monaco-hover .hover-contents a.code-link::before { content: "("; }

.monaco-hover .hover-contents a.code-link::after { content: ")"; }

.monaco-hover .hover-contents a.code-link > span { text-decoration: underli=
ne; border-bottom: 1px solid transparent; text-underline-position: under; c=
olor: var(--vscode-textLink-foreground); }

.monaco-hover .hover-contents a.code-link > span:hover { color: var(--vscod=
e-textLink-activeForeground); }

.monaco-hover .markdown-hover .hover-contents:not(.code-hover-contents):not=
(.html-hover-contents) span { margin-bottom: 4px; display: inline-block; }

.monaco-hover-content .action-container a { user-select: none; }

.monaco-hover-content .action-container.disabled { pointer-events: none; op=
acity: 0.4; cursor: default; }

.monaco-icon-label { display: flex; overflow: hidden; text-overflow: ellips=
is; }

.monaco-icon-label::before { background-size: 16px; background-position: 0p=
x center; background-repeat: no-repeat; padding-right: 6px; width: 16px; he=
ight: 22px; display: inline-block; -webkit-font-smoothing: antialiased; ver=
tical-align: top; flex-shrink: 0; line-height: inherit !important; }

.monaco-icon-label-container.disabled { color: var(--vscode-disabledForegro=
und); }

.monaco-icon-label > .monaco-icon-label-container { min-width: 0px; overflo=
w: hidden; text-overflow: ellipsis; flex: 1 1 0%; }

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-name-conta=
iner > .label-name { color: inherit; white-space: pre; }

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-name-conta=
iner > .label-name > .label-separator { margin: 0px 2px; opacity: 0.5; }

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-descriptio=
n-container > .label-description { opacity: 0.7; margin-left: 0.5em; font-s=
ize: 0.9em; white-space: pre; }

.monaco-icon-label.nowrap > .monaco-icon-label-container > .monaco-icon-des=
cription-container > .label-description { white-space: nowrap; }

.vs .monaco-icon-label > .monaco-icon-label-container > .monaco-icon-descri=
ption-container > .label-description { opacity: 0.95; }

.monaco-icon-label.italic > .monaco-icon-label-container > .monaco-icon-des=
cription-container > .label-description, .monaco-icon-label.italic > .monac=
o-icon-label-container > .monaco-icon-name-container > .label-name { font-s=
tyle: italic; }

.monaco-icon-label.deprecated { text-decoration: line-through; opacity: 0.6=
6; }

.monaco-icon-label.italic::after { font-style: italic; }

.monaco-icon-label.strikethrough > .monaco-icon-label-container > .monaco-i=
con-description-container > .label-description, .monaco-icon-label.striketh=
rough > .monaco-icon-label-container > .monaco-icon-name-container > .label=
-name { text-decoration: line-through; }

.monaco-icon-label::after { opacity: 0.75; font-size: 90%; font-weight: 600=
; margin: auto 16px 0px 5px; text-align: center; }

.monaco-list:focus .selected .monaco-icon-label, .monaco-list:focus .select=
ed .monaco-icon-label::after { color: inherit !important; }

.monaco-list-row.focused.selected .label-description, .monaco-list-row.sele=
cted .label-description { opacity: 0.8; }

.monaco-inputbox { position: relative; display: block; padding: 0px; box-si=
zing: border-box; border-radius: 2px; font-size: inherit; }

.monaco-inputbox > .ibwrapper > .input, .monaco-inputbox > .ibwrapper > .mi=
rror { padding: 4px 6px; }

.monaco-inputbox > .ibwrapper { position: relative; width: 100%; height: 10=
0%; }

.monaco-inputbox > .ibwrapper > .input { display: inline-block; box-sizing:=
 border-box; width: 100%; height: 100%; line-height: inherit; border: none;=
 font-family: inherit; font-size: inherit; resize: none; color: inherit; }

.monaco-inputbox > .ibwrapper > input { text-overflow: ellipsis; }

.monaco-inputbox > .ibwrapper > textarea.input { display: block; scrollbar-=
width: none; outline: none; }

.monaco-inputbox > .ibwrapper > textarea.input::-webkit-scrollbar { display=
: none; }

.monaco-inputbox > .ibwrapper > textarea.input.empty { white-space: nowrap;=
 }

.monaco-inputbox > .ibwrapper > .mirror { position: absolute; display: inli=
ne-block; width: 100%; top: 0px; left: 0px; box-sizing: border-box; white-s=
pace: pre-wrap; visibility: hidden; overflow-wrap: break-word; }

.monaco-inputbox-container { text-align: right; }

.monaco-inputbox-container .monaco-inputbox-message { display: inline-block=
; overflow: hidden; text-align: left; width: 100%; box-sizing: border-box; =
padding: 0.4em; font-size: 12px; line-height: 17px; margin-top: -1px; overf=
low-wrap: break-word; }

.monaco-inputbox .monaco-action-bar { position: absolute; right: 2px; top: =
4px; }

.monaco-inputbox .monaco-action-bar .action-item { margin-left: 2px; }

.monaco-inputbox .monaco-action-bar .action-item .codicon { background-repe=
at: no-repeat; width: 16px; height: 16px; }

.monaco-keybinding { display: flex; align-items: center; line-height: 10px;=
 }

.monaco-keybinding > .monaco-keybinding-key { display: inline-block; border=
-style: solid; border-width: 1px; border-radius: 3px; vertical-align: middl=
e; font-size: 11px; padding: 3px 5px; margin: 0px 2px; }

.monaco-keybinding > .monaco-keybinding-key:first-child { margin-left: 0px;=
 }

.monaco-keybinding > .monaco-keybinding-key:last-child { margin-right: 0px;=
 }

.monaco-keybinding > .monaco-keybinding-key-separator { display: inline-blo=
ck; }

.monaco-keybinding > .monaco-keybinding-key-chord-separator { width: 6px; }

.monaco-list { position: relative; height: 100%; width: 100%; white-space: =
nowrap; }

.monaco-list.mouse-support { user-select: none; }

.monaco-list > .monaco-scrollable-element { height: 100%; }

.monaco-list-rows { position: relative; width: 100%; height: 100%; }

.monaco-list.horizontal-scrolling .monaco-list-rows { width: auto; min-widt=
h: 100%; }

.monaco-list-row { position: absolute; box-sizing: border-box; overflow: hi=
dden; width: 100%; }

.monaco-list.mouse-support .monaco-list-row { cursor: pointer; touch-action=
: none; }

.monaco-list-row.scrolling { display: none !important; }

.monaco-list.element-focused, .monaco-list.selection-multiple, .monaco-list=
.selection-single { outline: 0px !important; }

.monaco-drag-image { display: inline-block; padding: 1px 7px; border-radius=
: 10px; font-size: 12px; position: absolute; z-index: 1000; }

.monaco-list-type-filter-message { position: absolute; box-sizing: border-b=
ox; width: 100%; height: 100%; top: 0px; left: 0px; padding: 40px 1em 1em; =
text-align: center; white-space: normal; opacity: 0.7; pointer-events: none=
; }

.monaco-list-type-filter-message:empty { display: none; }

.monaco-mouse-cursor-text { cursor: text; }

.monaco-progress-container { width: 100%; height: 5px; overflow: hidden; }

.monaco-progress-container .progress-bit { width: 2%; height: 5px; position=
: absolute; left: 0px; display: none; }

.monaco-progress-container.active .progress-bit { display: inherit; }

.monaco-progress-container.discrete .progress-bit { left: 0px; transition: =
width 0.1s linear; }

.monaco-progress-container.discrete.done .progress-bit { width: 100%; }

.monaco-progress-container.infinite .progress-bit { animation-name: progres=
s; animation-duration: 4s; animation-iteration-count: infinite; transform: =
translateZ(0px); animation-timing-function: linear; }

.monaco-progress-container.infinite.infinite-long-running .progress-bit { a=
nimation-timing-function: steps(100); }

@keyframes progress {=20
  0% { transform: translateX(0px) scaleX(1); }
  50% { transform: translateX(2500%) scaleX(3); }
  100% { transform: translateX(4900%) scaleX(1); }
}

:root { --vscode-sash-size: 4px; }

.monaco-sash { position: absolute; z-index: 35; touch-action: none; }

.monaco-sash.disabled { pointer-events: none; }

.monaco-sash.mac.vertical { cursor: col-resize; }

.monaco-sash.vertical.minimum { cursor: e-resize; }

.monaco-sash.vertical.maximum { cursor: w-resize; }

.monaco-sash.mac.horizontal { cursor: row-resize; }

.monaco-sash.horizontal.minimum { cursor: s-resize; }

.monaco-sash.horizontal.maximum { cursor: n-resize; }

.monaco-sash.disabled { cursor: default !important; pointer-events: none !i=
mportant; }

.monaco-sash.vertical { cursor: ew-resize; top: 0px; width: var(--vscode-sa=
sh-size); height: 100%; }

.monaco-sash.horizontal { cursor: ns-resize; left: 0px; width: 100%; height=
: var(--vscode-sash-size); }

.monaco-sash:not(.disabled) > .orthogonal-drag-handle { content: " "; heigh=
t: calc(var(--vscode-sash-size)*2); width: calc(var(--vscode-sash-size)*2);=
 z-index: 100; display: block; cursor: all-scroll; position: absolute; }

.monaco-sash.horizontal.orthogonal-edge-north:not(.disabled) > .orthogonal-=
drag-handle.start, .monaco-sash.horizontal.orthogonal-edge-south:not(.disab=
led) > .orthogonal-drag-handle.end { cursor: nwse-resize; }

.monaco-sash.horizontal.orthogonal-edge-north:not(.disabled) > .orthogonal-=
drag-handle.end, .monaco-sash.horizontal.orthogonal-edge-south:not(.disable=
d) > .orthogonal-drag-handle.start { cursor: nesw-resize; }

.monaco-sash.vertical > .orthogonal-drag-handle.start { left: calc(var(--vs=
code-sash-size)*-0.5); top: calc(var(--vscode-sash-size)*-1); }

.monaco-sash.vertical > .orthogonal-drag-handle.end { left: calc(var(--vsco=
de-sash-size)*-0.5); bottom: calc(var(--vscode-sash-size)*-1); }

.monaco-sash.horizontal > .orthogonal-drag-handle.start { top: calc(var(--v=
scode-sash-size)*-0.5); left: calc(var(--vscode-sash-size)*-1); }

.monaco-sash.horizontal > .orthogonal-drag-handle.end { top: calc(var(--vsc=
ode-sash-size)*-0.5); right: calc(var(--vscode-sash-size)*-1); }

.monaco-sash::before { content: ""; pointer-events: none; position: absolut=
e; width: 100%; height: 100%; background: transparent; }

.monaco-workbench:not(.reduce-motion) .monaco-sash::before { transition: ba=
ckground-color 0.1s ease-out; }

.monaco-sash.active::before, .monaco-sash.hover::before { background: var(-=
-vscode-sash-hoverBorder); }

.monaco-sash.vertical::before { width: var(--vscode-sash-hover-size); left:=
 calc(50% - var(--vscode-sash-hover-size)/2); }

.monaco-sash.horizontal::before { height: var(--vscode-sash-hover-size); to=
p: calc(50% - var(--vscode-sash-hover-size)/2); }

.pointer-events-disabled { pointer-events: none !important; }

.monaco-sash.debug { background: rgb(0, 255, 255); }

.monaco-sash.debug.disabled { background: rgba(0, 255, 255, 0.2); }

.monaco-sash.debug:not(.disabled) > .orthogonal-drag-handle { background: r=
ed; }

.monaco-scrollable-element > .scrollbar > .scra { cursor: pointer; font-siz=
e: 11px !important; }

.monaco-scrollable-element > .visible { opacity: 1; background: transparent=
; transition: opacity 0.1s linear; z-index: 11; }

.monaco-scrollable-element > .invisible { opacity: 0; pointer-events: none;=
 }

.monaco-scrollable-element > .invisible.fade { transition: opacity 0.8s lin=
ear; }

.monaco-scrollable-element > .shadow { position: absolute; display: none; }

.monaco-scrollable-element > .shadow.top { display: block; top: 0px; left: =
3px; height: 3px; width: 100%; box-shadow: var(--vscode-scrollbar-shadow) 0=
 6px 6px -6px inset; }

.monaco-scrollable-element > .shadow.left { display: block; top: 3px; left:=
 0px; height: 100%; width: 3px; box-shadow: var(--vscode-scrollbar-shadow) =
6px 0 6px -6px inset; }

.monaco-scrollable-element > .shadow.top-left-corner { display: block; top:=
 0px; left: 0px; height: 3px; width: 3px; }

.monaco-scrollable-element > .shadow.top.left { box-shadow: var(--vscode-sc=
rollbar-shadow) 6px 0 6px -6px inset; }

.monaco-scrollable-element > .scrollbar > .slider { background: var(--vscod=
e-scrollbarSlider-background); }

.monaco-scrollable-element > .scrollbar > .slider:hover { background: var(-=
-vscode-scrollbarSlider-hoverBackground); }

.monaco-scrollable-element > .scrollbar > .slider.active { background: var(=
--vscode-scrollbarSlider-activeBackground); }

.monaco-select-box { width: 100%; cursor: pointer; border-radius: 2px; }

.monaco-select-box-dropdown-container { font-size: 13px; font-weight: 400; =
text-transform: none; }

.monaco-action-bar .action-item.select-container { cursor: default; }

.monaco-action-bar .action-item .monaco-select-box { cursor: pointer; min-w=
idth: 100px; min-height: 18px; padding: 2px 23px 2px 8px; }

.mac .monaco-action-bar .action-item .monaco-select-box { font-size: 11px; =
border-radius: 5px; }

.monaco-select-box-dropdown-padding { --dropdown-padding-top: 1px; --dropdo=
wn-padding-bottom: 1px; }

.hc-black .monaco-select-box-dropdown-padding, .hc-light .monaco-select-box=
-dropdown-padding { --dropdown-padding-top: 3px; --dropdown-padding-bottom:=
 4px; }

.monaco-select-box-dropdown-container { display: none; box-sizing: border-b=
ox; }

.monaco-select-box-dropdown-container > .select-box-details-pane > .select-=
box-description-markdown * { margin: 0px; }

.monaco-select-box-dropdown-container > .select-box-details-pane > .select-=
box-description-markdown a:focus { outline: -webkit-focus-ring-color solid =
1px; outline-offset: -1px; }

.monaco-select-box-dropdown-container > .select-box-details-pane > .select-=
box-description-markdown code { line-height: 15px; font-family: var(--monac=
o-monospace-font); }

.monaco-select-box-dropdown-container.visible { display: flex; flex-directi=
on: column; text-align: left; width: 1px; overflow: hidden; border-bottom-l=
eft-radius: 3px; border-bottom-right-radius: 3px; }

.monaco-select-box-dropdown-container > .select-box-dropdown-list-container=
 { flex: 0 0 auto; align-self: flex-start; padding-top: var(--dropdown-padd=
ing-top); padding-bottom: var(--dropdown-padding-bottom); padding-left: 1px=
; padding-right: 1px; width: 100%; overflow: hidden; box-sizing: border-box=
; }

.monaco-select-box-dropdown-container > .select-box-details-pane { padding:=
 5px; }

.hc-black .monaco-select-box-dropdown-container > .select-box-dropdown-list=
-container { padding-top: var(--dropdown-padding-top); padding-bottom: var(=
--dropdown-padding-bottom); }

.monaco-select-box-dropdown-container > .select-box-dropdown-list-container=
 .monaco-list .monaco-list-row { cursor: pointer; }

.monaco-select-box-dropdown-container > .select-box-dropdown-list-container=
 .monaco-list .monaco-list-row > .option-text { text-overflow: ellipsis; ov=
erflow: hidden; padding-left: 3.5px; white-space: nowrap; float: left; }

.monaco-select-box-dropdown-container > .select-box-dropdown-list-container=
 .monaco-list .monaco-list-row > .option-detail { text-overflow: ellipsis; =
overflow: hidden; padding-left: 3.5px; white-space: nowrap; float: left; op=
acity: 0.7; }

.monaco-select-box-dropdown-container > .select-box-dropdown-list-container=
 .monaco-list .monaco-list-row > .option-decorator-right { text-overflow: e=
llipsis; overflow: hidden; padding-right: 10px; white-space: nowrap; float:=
 right; }

.monaco-select-box-dropdown-container > .select-box-dropdown-list-container=
 .monaco-list .monaco-list-row > .visually-hidden { position: absolute; lef=
t: -10000px; top: auto; width: 1px; height: 1px; overflow: hidden; }

.monaco-select-box-dropdown-container > .select-box-dropdown-container-widt=
h-control { flex: 1 1 auto; align-self: flex-start; opacity: 0; }

.monaco-select-box-dropdown-container > .select-box-dropdown-container-widt=
h-control > .width-control-div { overflow: hidden; max-height: 0px; }

.monaco-select-box-dropdown-container > .select-box-dropdown-container-widt=
h-control > .width-control-div > .option-text-width-control { padding-left:=
 4px; padding-right: 8px; white-space: nowrap; }

.monaco-split-view2 { position: relative; width: 100%; height: 100%; }

.monaco-split-view2 > .sash-container { position: absolute; width: 100%; he=
ight: 100%; pointer-events: none; }

.monaco-split-view2 > .sash-container > .monaco-sash { pointer-events: auto=
; }

.monaco-split-view2 > .monaco-scrollable-element { width: 100%; height: 100=
%; }

.monaco-split-view2 > .monaco-scrollable-element > .split-view-container { =
width: 100%; height: 100%; white-space: nowrap; position: relative; }

.monaco-split-view2 > .monaco-scrollable-element > .split-view-container > =
.split-view-view { white-space: normal; position: absolute; }

.monaco-split-view2 > .monaco-scrollable-element > .split-view-container > =
.split-view-view:not(.visible) { display: none; }

.monaco-split-view2.vertical > .monaco-scrollable-element > .split-view-con=
tainer > .split-view-view { width: 100%; }

.monaco-split-view2.horizontal > .monaco-scrollable-element > .split-view-c=
ontainer > .split-view-view { height: 100%; }

.monaco-split-view2.separator-border > .monaco-scrollable-element > .split-=
view-container > .split-view-view:not(:first-child)::before { content: " ";=
 position: absolute; top: 0px; left: 0px; z-index: 5; pointer-events: none;=
 background-color: var(--separator-border); }

.monaco-split-view2.separator-border.horizontal > .monaco-scrollable-elemen=
t > .split-view-container > .split-view-view:not(:first-child)::before { he=
ight: 100%; width: 1px; }

.monaco-split-view2.separator-border.vertical > .monaco-scrollable-element =
> .split-view-container > .split-view-view:not(:first-child)::before { heig=
ht: 1px; width: 100%; }

.monaco-table { display: flex; flex-direction: column; position: relative; =
height: 100%; width: 100%; white-space: nowrap; overflow: hidden; }

.monaco-table > .monaco-split-view2 { border-bottom: 1px solid transparent;=
 }

.monaco-table > .monaco-list { flex: 1 1 0%; }

.monaco-table-tr { display: flex; height: 100%; }

.monaco-table-th { width: 100%; height: 100%; font-weight: 700; overflow: h=
idden; text-overflow: ellipsis; }

.monaco-table-td, .monaco-table-th { box-sizing: border-box; flex-shrink: 0=
; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }

.monaco-table > .monaco-split-view2 .monaco-sash.vertical::before { content=
: ""; position: absolute; left: calc(var(--vscode-sash-size)/2); width: 0px=
; border-left: 1px solid transparent; }

.monaco-workbench:not(.reduce-motion) .monaco-table > .monaco-split-view2, =
.monaco-workbench:not(.reduce-motion) .monaco-table > .monaco-split-view2 .=
monaco-sash.vertical::before { transition: border-color 0.2s ease-out; }

.monaco-custom-toggle { margin-left: 2px; float: left; cursor: pointer; ove=
rflow: hidden; width: 20px; height: 20px; border-radius: 3px; border: 1px s=
olid transparent; padding: 1px; box-sizing: border-box; user-select: none; =
}

.monaco-custom-toggle:hover { background-color: var(--vscode-inputOption-ho=
verBackground); }

.hc-black .monaco-custom-toggle:hover, .hc-light .monaco-custom-toggle:hove=
r { border: 1px dashed var(--vscode-focusBorder); }

.hc-black .monaco-custom-toggle, .hc-black .monaco-custom-toggle:hover, .hc=
-light .monaco-custom-toggle, .hc-light .monaco-custom-toggle:hover { backg=
round: none; }

.monaco-custom-toggle.monaco-checkbox { height: 18px; width: 18px; border: =
1px solid transparent; border-radius: 3px; margin-right: 9px; margin-left: =
0px; padding: 0px; opacity: 1; background-size: 16px !important; }

.monaco-custom-toggle.monaco-checkbox:not(.checked)::before { visibility: h=
idden; }

.monaco-toolbar { height: 100%; }

.monaco-toolbar .toolbar-toggle-more { display: inline-block; padding: 0px;=
 }

.monaco-tl-row { display: flex; height: 100%; align-items: center; position=
: relative; }

.monaco-tl-row.disabled { cursor: default; }

.monaco-tl-indent { height: 100%; position: absolute; top: 0px; left: 16px;=
 pointer-events: none; }

.hide-arrows .monaco-tl-indent { left: 12px; }

.monaco-tl-indent > .indent-guide { display: inline-block; box-sizing: bord=
er-box; height: 100%; border-left: 1px solid transparent; }

.monaco-workbench:not(.reduce-motion) .monaco-tl-indent > .indent-guide { t=
ransition: border-color 0.1s linear; }

.monaco-tl-contents, .monaco-tl-twistie { height: 100%; }

.monaco-tl-twistie { font-size: 10px; text-align: right; padding-right: 6px=
; flex-shrink: 0; width: 16px; align-items: center; justify-content: center=
; transform: translateX(3px); display: flex !important; }

.monaco-tl-contents { flex: 1 1 0%; overflow: hidden; }

.monaco-tl-twistie::before { border-radius: 20px; }

.monaco-tl-twistie.collapsed::before { transform: rotate(-90deg); }

.monaco-tl-twistie.codicon-tree-item-loading::before { animation: 1.25s ste=
ps(30) 0s infinite normal none running codicon-spin; }

.monaco-tree-type-filter { position: absolute; top: 0px; display: flex; pad=
ding: 3px; max-width: 200px; z-index: 100; margin: 0px 6px; border: 1px sol=
id var(--vscode-widget-border); border-bottom-left-radius: 4px; border-bott=
om-right-radius: 4px; }

.monaco-workbench:not(.reduce-motion) .monaco-tree-type-filter { transition=
: top 0.3s; }

.monaco-tree-type-filter.disabled { top: -40px !important; }

.monaco-tree-type-filter-grab { align-items: center; justify-content: cente=
r; cursor: grab; margin-right: 2px; display: flex !important; }

.monaco-tree-type-filter-grab.grabbing { cursor: grabbing; }

.monaco-tree-type-filter-input { flex: 1 1 0%; }

.monaco-tree-type-filter-input .monaco-inputbox { height: 23px; }

.monaco-tree-type-filter-input .monaco-inputbox > .ibwrapper > .input, .mon=
aco-tree-type-filter-input .monaco-inputbox > .ibwrapper > .mirror { paddin=
g: 2px 4px; }

.monaco-tree-type-filter-input .monaco-findInput > .controls { top: 2px; }

.monaco-tree-type-filter-actionbar { margin-left: 4px; }

.monaco-tree-type-filter-actionbar .monaco-action-bar .action-label { paddi=
ng: 2px; }

.monaco-editor .inputarea { min-width: 0px; min-height: 0px; margin: 0px; p=
adding: 0px; position: absolute; resize: none; border: none; overflow: hidd=
en; color: transparent; background-color: transparent; z-index: -10; outlin=
e: none !important; }

.monaco-editor .inputarea.ime-input { z-index: 10; caret-color: var(--vscod=
e-editorCursor-foreground); color: var(--vscode-editor-foreground); }

.monaco-editor .blockDecorations-container { position: absolute; top: 0px; =
pointer-events: none; }

.monaco-editor .blockDecorations-block { position: absolute; box-sizing: bo=
rder-box; }

.monaco-editor .margin-view-overlays .current-line, .monaco-editor .view-ov=
erlays .current-line { display: block; position: absolute; left: 0px; top: =
0px; box-sizing: border-box; }

.monaco-editor .margin-view-overlays .current-line.current-line-margin.curr=
ent-line-margin-both { border-right: 0px; }

.monaco-editor .lines-content .cdr { position: absolute; }

.monaco-editor .glyph-margin { position: absolute; top: 0px; }

.monaco-editor .glyph-margin-widgets .cgmr { position: absolute; display: f=
lex; align-items: center; }

.monaco-editor .lines-content .core-guide { position: absolute; box-sizing:=
 border-box; }

.monaco-editor .lines-content .core-guide-indent { box-shadow: 1px 0 0 0 va=
r(--vscode-editorIndentGuide-background) inset; }

.monaco-editor .lines-content .core-guide-indent-active { box-shadow: 1px 0=
 0 0 var(--vscode-editorIndentGuide-activeBackground,--vscode-editorIndentG=
uide-background) inset; }

.monaco-editor .margin-view-overlays .line-numbers { font-variant-numeric: =
tabular-nums; position: absolute; text-align: right; display: inline-block;=
 vertical-align: middle; box-sizing: border-box; cursor: default; height: 1=
00%; }

.monaco-editor .relative-current-line-number { text-align: left; display: i=
nline-block; width: 100%; }

.monaco-editor .margin-view-overlays .line-numbers.lh-odd { margin-top: 1px=
; }

.monaco-editor .line-numbers { color: var(--vscode-editorLineNumber-foregro=
und); }

.monaco-editor .line-numbers.active-line-number { color: var(--vscode-edito=
rLineNumber-activeForeground); }

.mtkcontrol { color: rgb(255, 255, 255) !important; background: rgb(150, 0,=
 0) !important; }

.mtkoverflow { background-color: var(--vscode-button-background,--vscode-ed=
itor-background); color: var(--vscode-button-foreground,--vscode-editor-for=
eground); border: 1px solid var(--vscode-contrastBorder); border-radius: 2p=
x; padding: 4px; cursor: pointer; }

.mtkoverflow:hover { background-color: var(--vscode-button-hoverBackground)=
; }

.monaco-editor.no-user-select .lines-content, .monaco-editor.no-user-select=
 .view-line, .monaco-editor.no-user-select .view-lines { user-select: none;=
 }

.monaco-editor.mac .lines-content:hover, .monaco-editor.mac .view-line:hove=
r, .monaco-editor.mac .view-lines:hover { user-select: text; }

.monaco-editor.enable-user-select { user-select: initial; }

.monaco-editor .view-lines { white-space: nowrap; }

.monaco-editor .view-line { position: absolute; width: 100%; }

.monaco-editor .mtkw, .monaco-editor .mtkz { color: var(--vscode-editorWhit=
espace-foreground) !important; }

.monaco-editor .mtkz { display: inline-block; }

.monaco-editor .lines-decorations { position: absolute; top: 0px; backgroun=
d: rgb(255, 255, 255); }

.monaco-editor .margin-view-overlays .cldr { position: absolute; height: 10=
0%; }

.monaco-editor .margin { background-color: var(--vscode-editorGutter-backgr=
ound); }

.monaco-editor .margin-view-overlays .cmdr { position: absolute; left: 0px;=
 width: 100%; height: 100%; }

.monaco-editor .minimap.slider-mouseover .minimap-slider { opacity: 0; tran=
sition: opacity 0.1s linear; }

.monaco-editor .minimap.slider-mouseover .minimap-slider.active, .monaco-ed=
itor .minimap.slider-mouseover:hover .minimap-slider { opacity: 1; }

.monaco-editor .minimap-slider .minimap-slider-horizontal { background: var=
(--vscode-minimapSlider-background); }

.monaco-editor .minimap-slider:hover .minimap-slider-horizontal { backgroun=
d: var(--vscode-minimapSlider-hoverBackground); }

.monaco-editor .minimap-slider.active .minimap-slider-horizontal { backgrou=
nd: var(--vscode-minimapSlider-activeBackground); }

.monaco-editor .minimap-shadow-visible { box-shadow: var(--vscode-scrollbar=
-shadow) -6px 0 6px -6px inset; }

.monaco-editor .minimap-shadow-hidden { position: absolute; width: 0px; }

.monaco-editor .minimap-shadow-visible { position: absolute; left: -6px; wi=
dth: 6px; }

.monaco-editor.no-minimap-shadow .minimap-shadow-visible { position: absolu=
te; left: -1px; width: 1px; }

.minimap.autohide { opacity: 0; transition: opacity 0.5s; }

.minimap.autohide:hover { opacity: 1; }

.monaco-editor .overlayWidgets { position: absolute; top: 0px; left: 0px; }

.monaco-editor .view-ruler { position: absolute; top: 0px; box-shadow: 1px =
0 0 0 var(--vscode-editorRuler-foreground) inset; }

.monaco-editor .scroll-decoration { position: absolute; top: 0px; left: 0px=
; height: 6px; box-shadow: var(--vscode-scrollbar-shadow) 0 6px 6px -6px in=
set; }

.monaco-editor .lines-content .cslr { position: absolute; }

.monaco-editor .focused .selected-text { background-color: var(--vscode-edi=
tor-selectionBackground); }

.monaco-editor .selected-text { background-color: var(--vscode-editor-inact=
iveSelectionBackground); }

.monaco-editor .top-left-radius { border-top-left-radius: 3px; }

.monaco-editor .bottom-left-radius { border-bottom-left-radius: 3px; }

.monaco-editor .top-right-radius { border-top-right-radius: 3px; }

.monaco-editor .bottom-right-radius { border-bottom-right-radius: 3px; }

.monaco-editor.hc-black .top-left-radius { border-top-left-radius: 0px; }

.monaco-editor.hc-black .bottom-left-radius { border-bottom-left-radius: 0p=
x; }

.monaco-editor.hc-black .top-right-radius { border-top-right-radius: 0px; }

.monaco-editor.hc-black .bottom-right-radius { border-bottom-right-radius: =
0px; }

.monaco-editor.hc-light .top-left-radius { border-top-left-radius: 0px; }

.monaco-editor.hc-light .bottom-left-radius { border-bottom-left-radius: 0p=
x; }

.monaco-editor.hc-light .top-right-radius { border-top-right-radius: 0px; }

.monaco-editor.hc-light .bottom-right-radius { border-bottom-right-radius: =
0px; }

.monaco-editor .cursors-layer { position: absolute; top: 0px; }

.monaco-editor .cursors-layer > .cursor { position: absolute; overflow: hid=
den; box-sizing: border-box; }

.monaco-editor .cursors-layer.cursor-smooth-caret-animation > .cursor { tra=
nsition: 80ms; }

.monaco-editor .cursors-layer.cursor-block-outline-style > .cursor { border=
-style: solid; border-width: 1px; background: transparent !important; }

.monaco-editor .cursors-layer.cursor-underline-style > .cursor { border-bot=
tom-width: 2px; border-bottom-style: solid; background: transparent !import=
ant; }

.monaco-editor .cursors-layer.cursor-underline-thin-style > .cursor { borde=
r-bottom-width: 1px; border-bottom-style: solid; background: transparent !i=
mportant; }

@keyframes monaco-cursor-smooth {=20
  0%, 20% { opacity: 1; }
  60%, 100% { opacity: 0; }
}

@keyframes monaco-cursor-phase {=20
  0%, 20% { opacity: 1; }
  90%, 100% { opacity: 0; }
}

@keyframes monaco-cursor-expand {=20
  0%, 20% { transform: scaleY(1); }
  80%, 100% { transform: scaleY(0); }
}

.cursor-smooth { animation: 0.5s ease-in-out 0s 20 alternate none running m=
onaco-cursor-smooth; }

.cursor-phase { animation: 0.5s ease-in-out 0s 20 alternate none running mo=
naco-cursor-phase; }

.cursor-expand > .cursor { animation: 0.5s ease-in-out 0s 20 alternate none=
 running monaco-cursor-expand; }

.monaco-editor .mwh { position: absolute; color: var(--vscode-editorWhitesp=
ace-foreground) !important; }

.monaco-editor .diff-hidden-lines-widget { width: 100%; }

.monaco-editor .diff-hidden-lines { height: 0px; transform: translateY(-10p=
x); font-size: 13px; line-height: 14px; }

.diff-hidden-lines .bottom.dragging, .diff-hidden-lines .top.dragging, .dif=
f-hidden-lines:not(.dragging) .bottom:hover, .monaco-editor .diff-hidden-li=
nes:not(.dragging) .top:hover { background-color: var(--vscode-focusBorder)=
; }

.diff-hidden-lines .bottom, .monaco-editor .diff-hidden-lines .top { transi=
tion: background-color 0.1s ease-out; height: 4px; background-color: transp=
arent; background-clip: padding-box; border-bottom: 2px solid transparent; =
border-top: 4px solid transparent; cursor: ns-resize; }

.monaco-editor .diff-hidden-lines .top { transform: translateY(4px); }

.monaco-editor .diff-hidden-lines .bottom { transform: translateY(-6px); }

.monaco-editor .diff-unchanged-lines { background: var(--vscode-diffEditor-=
unchangedCodeBackground); }

.monaco-editor .noModificationsOverlay { z-index: 1; background: var(--vsco=
de-editor-background); display: flex; justify-content: center; align-items:=
 center; }

.monaco-editor .diff-hidden-lines .center { background: var(--vscode-diffEd=
itor-unchangedRegionBackground); color: var(--vscode-diffEditor-unchangedRe=
gionForeground); overflow: hidden; display: block; text-overflow: ellipsis;=
 white-space: nowrap; height: 24px; }

.monaco-editor .diff-hidden-lines .center span.codicon { vertical-align: mi=
ddle; }

.monaco-editor .diff-hidden-lines .center a:hover .codicon { cursor: pointe=
r; color: var(--vscode-editorLink-activeForeground) !important; }

.monaco-editor .movedModified, .monaco-editor .movedOriginal { border: 2px =
solid var(--vscode-diffEditor-move-border); }

.monaco-diff-editor .moved-blocks-lines { position: absolute; pointer-event=
s: none; }

.monaco-diff-editor .moved-blocks-lines path { fill: none; stroke: var(--vs=
code-diffEditor-move-border); stroke-width: 2; }

.monaco-editor .char-delete.diff-range-empty { margin-left: -1px; border-le=
ft: 3px solid var(--vscode-diffEditor-removedTextBackground); }

.monaco-editor .char-insert.diff-range-empty { border-left: 3px solid var(-=
-vscode-diffEditor-insertedTextBackground); }

.monaco-editor .fold-unchanged { cursor: pointer; }

.monaco-diff-editor .diffOverview { z-index: 9; }

.monaco-diff-editor .diffOverview .diffViewport { z-index: 10; }

.monaco-diff-editor.vs .diffOverview { background: rgba(0, 0, 0, 0.03); }

.monaco-diff-editor.vs-dark .diffOverview { background: rgba(255, 255, 255,=
 0.01); }

.monaco-scrollable-element.modified-in-monaco-diff-editor.vs-dark .scrollba=
r, .monaco-scrollable-element.modified-in-monaco-diff-editor.vs .scrollbar =
{ background: transparent; }

.monaco-scrollable-element.modified-in-monaco-diff-editor.hc-black .scrollb=
ar, .monaco-scrollable-element.modified-in-monaco-diff-editor.hc-light .scr=
ollbar { background: none; }

.monaco-scrollable-element.modified-in-monaco-diff-editor .slider { z-index=
: 10; }

.modified-in-monaco-diff-editor .slider.active { background: rgba(171, 171,=
 171, 0.4); }

.modified-in-monaco-diff-editor.hc-black .slider.active, .modified-in-monac=
o-diff-editor.hc-light .slider.active { background: none; }

.monaco-diff-editor .delete-sign, .monaco-diff-editor .insert-sign, .monaco=
-editor .delete-sign, .monaco-editor .insert-sign { align-items: center; fo=
nt-size: 11px !important; opacity: 0.7 !important; display: flex !important=
; }

.monaco-diff-editor.hc-black .delete-sign, .monaco-diff-editor.hc-black .in=
sert-sign, .monaco-diff-editor.hc-light .delete-sign, .monaco-diff-editor.h=
c-light .insert-sign, .monaco-editor.hc-black .delete-sign, .monaco-editor.=
hc-black .insert-sign, .monaco-editor.hc-light .delete-sign, .monaco-editor=
.hc-light .insert-sign { opacity: 1; }

.monaco-editor .inline-added-margin-view-zone, .monaco-editor .inline-delet=
ed-margin-view-zone { text-align: right; }

.monaco-editor .arrow-revert-change { z-index: 10; position: absolute; }

.monaco-editor .arrow-revert-change:hover { cursor: pointer; }

.monaco-editor .view-zones .view-lines .view-line span { display: inline-bl=
ock; }

.monaco-editor .margin-view-zones .lightbulb-glyph:hover { cursor: pointer;=
 }

.monaco-diff-editor .char-insert, .monaco-editor .char-insert { background-=
color: var(--vscode-diffEditor-insertedTextBackground); }

.monaco-diff-editor .line-insert, .monaco-editor .line-insert { background-=
color: var(--vscode-diffEditor-insertedLineBackground,--vscode-diffEditor-i=
nsertedTextBackground); }

.monaco-editor .char-insert, .monaco-editor .line-insert { box-sizing: bord=
er-box; border: 1px solid var(--vscode-diffEditor-insertedTextBorder); }

.monaco-editor.hc-black .char-insert, .monaco-editor.hc-black .line-insert,=
 .monaco-editor.hc-light .char-insert, .monaco-editor.hc-light .line-insert=
 { border-style: dashed; }

.monaco-editor .char-delete, .monaco-editor .line-delete { box-sizing: bord=
er-box; border: 1px solid var(--vscode-diffEditor-removedTextBorder); }

.monaco-editor.hc-black .char-delete, .monaco-editor.hc-black .line-delete,=
 .monaco-editor.hc-light .char-delete, .monaco-editor.hc-light .line-delete=
 { border-style: dashed; }

.monaco-diff-editor .gutter-insert, .monaco-editor .gutter-insert, .monaco-=
editor .inline-added-margin-view-zone { background-color: var(--vscode-diff=
EditorGutter-insertedLineBackground,--vscode-diffEditor-insertedLineBackgro=
und,--vscode-diffEditor-insertedTextBackground); }

.monaco-diff-editor .char-delete, .monaco-editor .char-delete { background-=
color: var(--vscode-diffEditor-removedTextBackground); }

.monaco-diff-editor .line-delete, .monaco-editor .line-delete { background-=
color: var(--vscode-diffEditor-removedLineBackground,--vscode-diffEditor-re=
movedTextBackground); }

.monaco-diff-editor .gutter-delete, .monaco-editor .gutter-delete, .monaco-=
editor .inline-deleted-margin-view-zone { background-color: var(--vscode-di=
ffEditorGutter-removedLineBackground,--vscode-diffEditor-removedLineBackgro=
und,--vscode-diffEditor-removedTextBackground); }

.monaco-diff-editor.side-by-side .editor.modified { box-shadow: -6px 0 5px =
-5px var(--vscode-scrollbar-shadow); border-left: 1px solid var(--vscode-di=
ffEditor-border); }

.monaco-diff-editor .diffViewport { background: var(--vscode-scrollbarSlide=
r-background); }

.monaco-diff-editor .diffViewport:hover { background: var(--vscode-scrollba=
rSlider-hoverBackground); }

.monaco-diff-editor .diffViewport:active { background: var(--vscode-scrollb=
arSlider-activeBackground); }

.monaco-diff-editor .diff-review-line-number { text-align: right; display: =
inline-block; color: var(--vscode-editorLineNumber-foreground); }

.monaco-diff-editor .diff-review { position: absolute; user-select: none; z=
-index: 99; }

.monaco-diff-editor .diff-review-summary { padding-left: 10px; }

.monaco-diff-editor .diff-review-shadow { position: absolute; box-shadow: v=
ar(--vscode-scrollbar-shadow) 0 -6px 6px -6px inset; }

.monaco-diff-editor .diff-review-row { white-space: pre; }

.monaco-diff-editor .diff-review-table { display: table; min-width: 100%; }

.monaco-diff-editor .diff-review-row { display: table-row; width: 100%; }

.monaco-diff-editor .diff-review-spacer { display: inline-block; width: 10p=
x; vertical-align: middle; }

.monaco-diff-editor .diff-review-spacer > .codicon { font-size: 9px !import=
ant; }

.monaco-diff-editor .diff-review-actions { display: inline-block; position:=
 absolute; right: 10px; top: 2px; z-index: 100; }

.monaco-diff-editor .diff-review-actions .action-label { width: 16px; heigh=
t: 16px; margin: 2px 0px; }

.monaco-editor .editor-widget input { color: inherit; }

.monaco-editor { position: relative; overflow: visible; text-size-adjust: 1=
00%; color: var(--vscode-editor-foreground); }

.monaco-editor, .monaco-editor-background { background-color: var(--vscode-=
editor-background); }

.monaco-editor .rangeHighlight { background-color: var(--vscode-editor-rang=
eHighlightBackground); box-sizing: border-box; border: 1px solid var(--vsco=
de-editor-rangeHighlightBorder); }

.monaco-editor.hc-black .rangeHighlight, .monaco-editor.hc-light .rangeHigh=
light { border-style: dotted; }

.monaco-editor .symbolHighlight { background-color: var(--vscode-editor-sym=
bolHighlightBackground); box-sizing: border-box; border: 1px solid var(--vs=
code-editor-symbolHighlightBorder); }

.monaco-editor.hc-black .symbolHighlight, .monaco-editor.hc-light .symbolHi=
ghlight { border-style: dotted; }

.monaco-editor .overflow-guard { position: relative; overflow: hidden; }

.monaco-editor .view-overlays { position: absolute; top: 0px; }

.monaco-editor .squiggly-error { border-bottom: 4px double var(--vscode-edi=
torError-border); }

.monaco-editor .squiggly-error::before { display: block; content: ""; width=
: 100%; height: 100%; background: var(--vscode-editorError-background); }

.monaco-editor .squiggly-warning { border-bottom: 4px double var(--vscode-e=
ditorWarning-border); }

.monaco-editor .squiggly-warning::before { display: block; content: ""; wid=
th: 100%; height: 100%; background: var(--vscode-editorWarning-background);=
 }

.monaco-editor .squiggly-info { border-bottom: 4px double var(--vscode-edit=
orInfo-border); }

.monaco-editor .squiggly-info::before { display: block; content: ""; width:=
 100%; height: 100%; background: var(--vscode-editorInfo-background); }

.monaco-editor .squiggly-hint { border-bottom: 2px dotted var(--vscode-edit=
orHint-border); }

.monaco-editor.showUnused .squiggly-unnecessary { border-bottom: 2px dashed=
 var(--vscode-editorUnnecessaryCode-border); }

.monaco-editor.showDeprecated .squiggly-inline-deprecated { text-decoration=
-line: line-through; text-decoration-thickness: initial; text-decoration-st=
yle: initial; text-decoration-color: var(--vscode-editor-foreground,inherit=
); }

.monaco-editor .selection-anchor { background-color: rgb(0, 122, 204); widt=
h: 2px !important; }

.monaco-editor .bracket-match { box-sizing: border-box; background-color: v=
ar(--vscode-editorBracketMatch-background); border: 1px solid var(--vscode-=
editorBracketMatch-border); }

.monaco-editor .lightBulbWidget { display: flex; align-items: center; justi=
fy-content: center; }

.monaco-editor .lightBulbWidget:hover { cursor: pointer; }

.monaco-editor .lightBulbWidget.codicon-light-bulb { color: var(--vscode-ed=
itorLightBulb-foreground); }

.monaco-editor .lightBulbWidget.codicon-lightbulb-autofix { color: var(--vs=
code-editorLightBulbAutoFix-foreground,var(--vscode-editorLightBulb-foregro=
und)); }

.monaco-editor .lightBulbWidget::before { position: relative; z-index: 2; }

.monaco-editor .lightBulbWidget::after { position: absolute; top: 0px; left=
: 0px; content: ""; display: block; width: 100%; height: 100%; opacity: 0.3=
; background-color: var(--vscode-editor-background); z-index: 1; }

.monaco-editor .codelens-decoration { overflow: hidden; display: inline-blo=
ck; text-overflow: ellipsis; white-space: nowrap; color: var(--vscode-edito=
rCodeLens-foreground); line-height: var(--vscode-editorCodeLens-lineHeight)=
; font-size: var(--vscode-editorCodeLens-fontSize); padding-right: calc(var=
(--vscode-editorCodeLens-fontSize)*0.5); font-feature-settings: var(--vscod=
e-editorCodeLens-fontFeatureSettings); font-family: var(--vscode-editorCode=
Lens-fontFamily),var(--vscode-editorCodeLens-fontFamilyDefault); }

.monaco-editor .codelens-decoration > a, .monaco-editor .codelens-decoratio=
n > span { user-select: none; white-space: nowrap; vertical-align: sub; }

.monaco-editor .codelens-decoration > a { text-decoration: none; }

.monaco-editor .codelens-decoration > a:hover { cursor: pointer; }

.monaco-editor .codelens-decoration > a:hover, .monaco-editor .codelens-dec=
oration > a:hover .codicon { color: var(--vscode-editorLink-activeForegroun=
d) !important; }

.monaco-editor .codelens-decoration .codicon { vertical-align: middle; line=
-height: var(--vscode-editorCodeLens-lineHeight); font-size: var(--vscode-e=
ditorCodeLens-fontSize); color: currentcolor !important; }

.monaco-editor .codelens-decoration > a:hover .codicon::before { cursor: po=
inter; }

@keyframes fadein {=20
  0% { opacity: 0; visibility: visible; }
  100% { opacity: 1; }
}

.monaco-editor .codelens-decoration.fadein { animation: 0.1s linear 0s 1 no=
rmal none running fadein; }

.colorpicker-widget { height: 190px; user-select: none; }

.colorpicker-color-decoration, .hc-light .colorpicker-color-decoration { bo=
rder: 0.1em solid rgb(0, 0, 0); box-sizing: border-box; margin: 0.1em 0.2em=
 0px; width: 0.8em; height: 0.8em; line-height: 0.8em; display: inline-bloc=
k; cursor: pointer; }

.hc-black .colorpicker-color-decoration, .vs-dark .colorpicker-color-decora=
tion { border: 0.1em solid rgb(238, 238, 238); }

.colorpicker-header { display: flex; height: 24px; position: relative; back=
ground: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp=
8Z5+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAA=
ZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTZEaa/1AAAAHUlEQVQYV2PYvXu3JAi7uLiAMa=
YAjAGTQBPYLQkAa/0Zef3qRswAAAAASUVORK5CYII=3D") 0% 0% / 9px 9px; image-rende=
ring: pixelated; }

.colorpicker-header .picked-color { width: 240px; display: flex; align-item=
s: center; justify-content: center; line-height: 24px; cursor: pointer; col=
or: rgb(255, 255, 255); flex: 1 1 0%; }

.colorpicker-header .picked-color .codicon { color: inherit; font-size: 14p=
x; position: absolute; left: 8px; }

.colorpicker-header .picked-color.light { color: rgb(0, 0, 0); }

.colorpicker-header .original-color { width: 74px; z-index: inherit; cursor=
: pointer; }

.standalone-colorpicker { color: var(--vscode-editorHoverWidget-foreground)=
; background-color: var(--vscode-editorHoverWidget-background); border: 1px=
 solid var(--vscode-editorHoverWidget-border); }

.colorpicker-header.standalone-colorpicker { border-bottom: none; }

.colorpicker-header .close-button { cursor: pointer; background-color: var(=
--vscode-editorHoverWidget-background); border-left: 1px solid var(--vscode=
-editorHoverWidget-border); }

.colorpicker-header .close-button-inner-div { width: 100%; height: 100%; te=
xt-align: center; }

.colorpicker-header .close-button-inner-div:hover { background-color: var(-=
-vscode-toolbar-hoverBackground); }

.colorpicker-header .close-icon { padding: 3px; }

.colorpicker-body { display: flex; padding: 8px; position: relative; }

.colorpicker-body .saturation-wrap { overflow: hidden; height: 150px; posit=
ion: relative; min-width: 220px; flex: 1 1 0%; }

.colorpicker-body .saturation-box { height: 150px; position: absolute; }

.colorpicker-body .saturation-selection { width: 9px; height: 9px; margin: =
-5px 0px 0px -5px; border: 1px solid rgb(255, 255, 255); border-radius: 100=
%; box-shadow: rgba(0, 0, 0, 0.8) 0px 0px 2px; position: absolute; }

.colorpicker-body .strip { width: 25px; height: 150px; }

.colorpicker-body .standalone-strip { width: 25px; height: 122px; }

.colorpicker-body .hue-strip { position: relative; margin-left: 8px; cursor=
: grab; background: linear-gradient(red 0px, rgb(255, 255, 0) 17%, rgb(0, 2=
55, 0) 33%, rgb(0, 255, 255) 50%, rgb(0, 0, 255) 67%, rgb(255, 0, 255) 83%,=
 red); }

.colorpicker-body .opacity-strip { position: relative; margin-left: 8px; cu=
rsor: grab; background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA=
AAQAAAAECAYAAACp8Z5+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsM=
AAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTZEaa/1AAAAHUlEQVQYV2=
PYvXu3JAi7uLiAMaYAjAGTQBPYLQkAa/0Zef3qRswAAAAASUVORK5CYII=3D") 0% 0% / 9px =
9px; image-rendering: pixelated; }

.colorpicker-body .strip.grabbing { cursor: grabbing; }

.colorpicker-body .slider { position: absolute; top: 0px; left: -2px; width=
: calc(100% + 4px); height: 4px; box-sizing: border-box; border: 1px solid =
rgba(255, 255, 255, 0.71); box-shadow: rgba(0, 0, 0, 0.85) 0px 0px 1px; }

.colorpicker-body .strip .overlay { height: 150px; pointer-events: none; }

.colorpicker-body .standalone-strip .standalone-overlay { height: 122px; po=
inter-events: none; }

.standalone-colorpicker-body { display: block; border-top: 1px solid transp=
arent; border-right: 1px solid transparent; border-left: 1px solid transpar=
ent; border-image: initial; border-bottom: 1px solid var(--vscode-editorHov=
erWidget-border); overflow: hidden; }

.colorpicker-body .insert-button { position: absolute; height: 20px; width:=
 58px; padding: 0px; right: 8px; bottom: 8px; background: var(--vscode-butt=
on-background); color: var(--vscode-button-foreground); border-radius: 2px;=
 border: none; cursor: pointer; }

.colorpicker-body .insert-button:hover { background: var(--vscode-button-ho=
verBackground); }

.monaco-editor.hc-light .dnd-target, .monaco-editor.vs .dnd-target { border=
-right: 2px dotted rgb(0, 0, 0); color: rgb(255, 255, 255); }

.monaco-editor.vs-dark .dnd-target { border-right: 2px dotted rgb(174, 175,=
 173); color: rgb(81, 80, 79); }

.monaco-editor.hc-black .dnd-target { border-right: 2px dotted rgb(255, 255=
, 255); color: rgb(0, 0, 0); }

.monaco-editor.hc-black.mac.mouse-default .view-lines, .monaco-editor.hc-li=
ght.mac.mouse-default .view-lines, .monaco-editor.mouse-default .view-lines=
, .monaco-editor.vs-dark.mac.mouse-default .view-lines { cursor: default; }

.monaco-editor.hc-black.mac.mouse-copy .view-lines, .monaco-editor.hc-light=
.mac.mouse-copy .view-lines, .monaco-editor.mouse-copy .view-lines, .monaco=
-editor.vs-dark.mac.mouse-copy .view-lines { cursor: copy; }

.post-edit-widget { box-shadow: 0 0 8px 2px var(--vscode-widget-shadow); bo=
rder: 1px solid var(--vscode-widget-border,transparent); border-radius: 4px=
; background-color: var(--vscode-editorWidget-background); overflow: hidden=
; }

.post-edit-widget .monaco-button { padding: 2px; border: none; border-radiu=
s: 0px; }

.post-edit-widget .monaco-button:hover { background-color: var(--vscode-but=
ton-secondaryHoverBackground) !important; }

.post-edit-widget .monaco-button .codicon { margin: 0px; }

.monaco-editor .findOptionsWidget { background-color: var(--vscode-editorWi=
dget-background); color: var(--vscode-editorWidget-foreground); box-shadow:=
 0 0 8px 2px var(--vscode-widget-shadow); border: 2px solid var(--vscode-co=
ntrastBorder); }

.monaco-editor .find-widget { position: absolute; z-index: 35; height: 33px=
; overflow: hidden; line-height: 19px; transition: transform 0.2s linear; p=
adding: 0px 4px; box-sizing: border-box; transform: translateY(calc(-100% -=
 10px)); border-bottom-left-radius: 4px; border-bottom-right-radius: 4px; }

.monaco-workbench.reduce-motion .monaco-editor .find-widget { transition: t=
ransform linear; }

.monaco-editor .find-widget textarea { margin: 0px; }

.monaco-editor .find-widget.hiddenEditor { display: none; }

.monaco-editor .find-widget.replaceToggled > .replace-part { display: flex;=
 }

.monaco-editor .find-widget.visible { transform: translateY(0px); }

.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline: -we=
bkit-focus-ring-color solid 1px; outline-offset: -1px; }

.monaco-editor .find-widget .monaco-inputbox .input { background-color: tra=
nsparent; min-height: 0px; }

.monaco-editor .find-widget .monaco-findInput .input { font-size: 13px; }

.monaco-editor .find-widget > .find-part, .monaco-editor .find-widget > .re=
place-part { margin: 3px 25px 0px 17px; font-size: 12px; display: flex; }

.monaco-editor .find-widget > .find-part .monaco-inputbox, .monaco-editor .=
find-widget > .replace-part .monaco-inputbox { min-height: 25px; }

.monaco-editor .find-widget > .replace-part .monaco-inputbox > .ibwrapper >=
 .mirror { padding-right: 22px; }

.monaco-editor .find-widget > .find-part .monaco-inputbox > .ibwrapper > .i=
nput, .monaco-editor .find-widget > .find-part .monaco-inputbox > .ibwrappe=
r > .mirror, .monaco-editor .find-widget > .replace-part .monaco-inputbox >=
 .ibwrapper > .input, .monaco-editor .find-widget > .replace-part .monaco-i=
nputbox > .ibwrapper > .mirror { padding-top: 2px; padding-bottom: 2px; }

.monaco-editor .find-widget > .find-part .find-actions, .monaco-editor .fin=
d-widget > .replace-part .replace-actions { height: 25px; display: flex; al=
ign-items: center; }

.monaco-editor .find-widget .monaco-findInput { vertical-align: middle; dis=
play: flex; flex: 1 1 0%; }

.monaco-editor .find-widget .monaco-findInput .monaco-scrollable-element { =
width: 100%; }

.monaco-editor .find-widget .monaco-findInput .monaco-scrollable-element .s=
crollbar.vertical { opacity: 0; }

.monaco-editor .find-widget .matchesCount { display: flex; flex: initial; m=
argin: 0px 0px 0px 3px; padding: 2px 0px 0px 2px; height: 25px; vertical-al=
ign: middle; box-sizing: border-box; text-align: center; line-height: 23px;=
 }

.monaco-editor .find-widget .button { width: 16px; height: 16px; padding: 3=
px; border-radius: 5px; flex: initial; margin-left: 3px; background-positio=
n: 50% center; background-repeat: no-repeat; cursor: pointer; display: flex=
; align-items: center; justify-content: center; }

.monaco-editor .find-widget .codicon-find-selection { width: 22px; height: =
22px; padding: 3px; border-radius: 5px; }

.monaco-editor .find-widget .button.left { margin-left: 0px; margin-right: =
3px; }

.monaco-editor .find-widget .button.wide { width: auto; padding: 1px 6px; t=
op: -1px; }

.monaco-editor .find-widget .button.toggle { position: absolute; top: 0px; =
left: 3px; width: 18px; height: 100%; border-radius: 0px; box-sizing: borde=
r-box; }

.monaco-editor .find-widget .button.toggle.disabled { display: none; }

.monaco-editor .find-widget .disabled { color: var(--vscode-disabledForegro=
und); cursor: default; }

.monaco-editor .find-widget > .replace-part { display: none; }

.monaco-editor .find-widget > .replace-part > .monaco-findInput { position:=
 relative; display: flex; vertical-align: middle; flex: 0 0 auto; }

.monaco-editor .find-widget > .replace-part > .monaco-findInput > .controls=
 { position: absolute; top: 3px; right: 2px; }

.monaco-editor .find-widget.reduced-find-widget .matchesCount { display: no=
ne; }

.monaco-editor .find-widget.narrow-find-widget { max-width: 257px !importan=
t; }

.monaco-editor .find-widget.collapsed-find-widget { max-width: 170px !impor=
tant; }

.monaco-editor .find-widget.collapsed-find-widget .button.next, .monaco-edi=
tor .find-widget.collapsed-find-widget .button.previous, .monaco-editor .fi=
nd-widget.collapsed-find-widget .button.replace, .monaco-editor .find-widge=
t.collapsed-find-widget .button.replace-all, .monaco-editor .find-widget.co=
llapsed-find-widget > .find-part .monaco-findInput .controls { display: non=
e; }

.monaco-editor .findMatch { animation-name: inherit !important; }

.monaco-editor .find-widget .monaco-sash { left: 0px !important; }

.monaco-editor.hc-black .find-widget .button::before { position: relative; =
top: 1px; left: 2px; }

.monaco-editor .find-widget > .button.codicon-widget-close { position: abso=
lute; top: 5px; right: 4px; }

.monaco-editor .margin-view-overlays .codicon-folding-collapsed, .monaco-ed=
itor .margin-view-overlays .codicon-folding-expanded, .monaco-editor .margi=
n-view-overlays .codicon-folding-manual-collapsed, .monaco-editor .margin-v=
iew-overlays .codicon-folding-manual-expanded { cursor: pointer; opacity: 0=
; transition: opacity 0.5s; display: flex; align-items: center; justify-con=
tent: center; font-size: 140%; margin-left: 2px; }

.monaco-workbench.reduce-motion .monaco-editor .margin-view-overlays .codic=
on-folding-collapsed, .monaco-workbench.reduce-motion .monaco-editor .margi=
n-view-overlays .codicon-folding-expanded, .monaco-workbench.reduce-motion =
.monaco-editor .margin-view-overlays .codicon-folding-manual-collapsed, .mo=
naco-workbench.reduce-motion .monaco-editor .margin-view-overlays .codicon-=
folding-manual-expanded { transition: initial; }

.monaco-editor .margin-view-overlays .codicon.alwaysShowFoldIcons, .monaco-=
editor .margin-view-overlays .codicon.codicon-folding-collapsed, .monaco-ed=
itor .margin-view-overlays .codicon.codicon-folding-manual-collapsed, .mona=
co-editor .margin-view-overlays:hover .codicon { opacity: 1; }

.monaco-editor .inline-folded::after { color: grey; margin: 0.1em 0.2em 0px=
; content: "=E2=8B=AF"; display: inline; line-height: 1em; cursor: pointer;=
 }

.monaco-editor .folded-background { background-color: var(--vscode-editor-f=
oldBackground); }

.monaco-editor .cldr.codicon.codicon-folding-collapsed, .monaco-editor .cld=
r.codicon.codicon-folding-expanded, .monaco-editor .cldr.codicon.codicon-fo=
lding-manual-collapsed, .monaco-editor .cldr.codicon.codicon-folding-manual=
-expanded { color: var(--vscode-editorGutter-foldingControlForeground) !imp=
ortant; }

.monaco-editor .peekview-widget .head .peekview-title .severity-icon { disp=
lay: inline-block; vertical-align: text-top; margin-right: 4px; }

.monaco-editor .marker-widget { text-overflow: ellipsis; white-space: nowra=
p; }

.monaco-editor .marker-widget > .stale { opacity: 0.6; font-style: italic; =
}

.monaco-editor .marker-widget .title { display: inline-block; padding-right=
: 5px; }

.monaco-editor .marker-widget .descriptioncontainer { position: absolute; w=
hite-space: pre; user-select: text; padding: 8px 12px 0px 20px; }

.monaco-editor .marker-widget .descriptioncontainer .message { display: fle=
x; flex-direction: column; }

.monaco-editor .marker-widget .descriptioncontainer .message .details { pad=
ding-left: 6px; }

.monaco-editor .marker-widget .descriptioncontainer .message .source, .mona=
co-editor .marker-widget .descriptioncontainer .message span.code { opacity=
: 0.6; }

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link { =
opacity: 0.6; color: inherit; }

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link::b=
efore { content: "("; }

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link::a=
fter { content: ")"; }

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link > =
span { text-decoration: underline; border-bottom: 1px solid transparent; te=
xt-underline-position: under; color: var(--vscode-textLink-activeForeground=
); }

.monaco-editor .marker-widget .descriptioncontainer .filename { cursor: poi=
nter; }

.monaco-editor .goto-definition-link { text-decoration: underline; cursor: =
pointer; color: var(--vscode-editorLink-activeForeground) !important; }

.monaco-editor .zone-widget .zone-widget-container.reference-zone-widget { =
border-top-width: 1px; border-bottom-width: 1px; }

.monaco-editor .reference-zone-widget .inline { display: inline-block; vert=
ical-align: top; }

.monaco-editor .reference-zone-widget .messages { height: 100%; width: 100%=
; text-align: center; padding: 3em 0px; }

.monaco-editor .reference-zone-widget .ref-tree { line-height: 23px; backgr=
ound-color: var(--vscode-peekViewResult-background); color: var(--vscode-pe=
ekViewResult-lineForeground); }

.monaco-editor .reference-zone-widget .ref-tree .reference { text-overflow:=
 ellipsis; overflow: hidden; }

.monaco-editor .reference-zone-widget .ref-tree .reference-file { display: =
inline-flex; width: 100%; height: 100%; color: var(--vscode-peekViewResult-=
fileForeground); }

.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .selecte=
d .reference-file { color: inherit !important; }

.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .monaco-=
list-rows > .monaco-list-row.selected:not(.highlighted) { background-color:=
 var(--vscode-peekViewResult-selectionBackground); color: var(--vscode-peek=
ViewResult-selectionForeground) !important; }

.monaco-editor .reference-zone-widget .ref-tree .reference-file .count { ma=
rgin-right: 12px; margin-left: auto; }

.monaco-editor .reference-zone-widget .ref-tree .referenceMatch .highlight =
{ background-color: var(--vscode-peekViewResult-matchHighlightBackground); =
}

.monaco-editor .reference-zone-widget .preview .reference-decoration { back=
ground-color: var(--vscode-peekViewEditor-matchHighlightBackground); border=
: 2px solid var(--vscode-peekViewEditor-matchHighlightBorder); box-sizing: =
border-box; }

.monaco-editor .reference-zone-widget .preview .monaco-editor .inputarea.im=
e-input, .monaco-editor .reference-zone-widget .preview .monaco-editor .mon=
aco-editor-background { background-color: var(--vscode-peekViewEditor-backg=
round); }

.monaco-editor .reference-zone-widget .preview .monaco-editor .margin { bac=
kground-color: var(--vscode-peekViewEditorGutter-background); }

.monaco-editor.hc-black .reference-zone-widget .ref-tree .reference-file, .=
monaco-editor.hc-light .reference-zone-widget .ref-tree .reference-file { f=
ont-weight: 700; }

.monaco-editor.hc-black .reference-zone-widget .ref-tree .referenceMatch .h=
ighlight, .monaco-editor.hc-light .reference-zone-widget .ref-tree .referen=
ceMatch .highlight { border: 1px dotted var(--vscode-contrastActiveBorder,t=
ransparent); box-sizing: border-box; }

.monaco-editor .hoverHighlight { background-color: var(--vscode-editor-hove=
rHighlightBackground); }

.monaco-editor .monaco-hover { color: var(--vscode-editorHoverWidget-foregr=
ound); background-color: var(--vscode-editorHoverWidget-background); border=
: 1px solid var(--vscode-editorHoverWidget-border); border-radius: 3px; }

.monaco-editor .monaco-hover a { color: var(--vscode-textLink-foreground); =
}

.monaco-editor .monaco-hover a:hover { color: var(--vscode-textLink-activeF=
oreground); }

.monaco-editor .monaco-hover .hover-row .actions { background-color: var(--=
vscode-editorHoverWidget-statusBarBackground); }

.monaco-editor .monaco-hover code { background-color: var(--vscode-textCode=
Block-background); }

.monaco-editor.vs .valueSetReplacement { outline: solid 2px var(--vscode-ed=
itorBracketMatch-border); }

.monaco-editor .suggest-preview-additional-widget { white-space: nowrap; }

.monaco-editor .suggest-preview-additional-widget .content-spacer { color: =
transparent; white-space: pre; }

.monaco-editor .suggest-preview-additional-widget .button { display: inline=
-block; cursor: pointer; text-decoration: underline; text-underline-positio=
n: under; }

.monaco-editor .ghost-text-hidden { opacity: 0; font-size: 0px; }

.monaco-editor .ghost-text-decoration, .monaco-editor .suggest-preview-text=
 .ghost-text { font-style: italic; }

.monaco-editor .inline-completion-text-to-replace { text-decoration: underl=
ine; text-underline-position: under; }

.monaco-editor .ghost-text-decoration, .monaco-editor .ghost-text-decoratio=
n-preview, .monaco-editor .suggest-preview-text .ghost-text { background-co=
lor: var(--vscode-editorGhostText-background); border: 1px solid var(--vsco=
de-editorGhostText-border); color: var(--vscode-editorGhostText-foreground)=
 !important; }

.monaco-editor .inlineSuggestionsHints.withBorder { z-index: 39; color: var=
(--vscode-editorHoverWidget-foreground); background-color: var(--vscode-edi=
torHoverWidget-background); border: 1px solid var(--vscode-editorHoverWidge=
t-border); }

.monaco-editor .inlineSuggestionsHints a, .monaco-editor .inlineSuggestions=
Hints a:hover { color: var(--vscode-foreground); }

.monaco-editor .inlineSuggestionsHints .keybinding { display: flex; margin-=
left: 4px; opacity: 0.6; }

.monaco-editor .inlineSuggestionsHints .keybinding .monaco-keybinding-key {=
 font-size: 8px; padding: 2px 3px; }

.monaco-editor .inlineSuggestionsHints .custom-actions .action-item:nth-chi=
ld(2) a { display: flex; min-width: 19px; justify-content: center; }

.monaco-editor .inlineSuggestionStatusBarItemLabel { margin-right: 2px; }

.inline-editor-progress-decoration { display: inline-block; width: 1em; hei=
ght: 1em; }

.inline-progress-widget { justify-content: center; align-items: center; dis=
play: flex !important; }

.inline-progress-widget .icon { font-size: 80% !important; }

.inline-progress-widget:hover .icon { animation: auto ease 0s 1 normal none=
 running none; font-size: 90% !important; }

.inline-progress-widget:hover .icon::before { content: "=EE=A9=B6"; }

.monaco-editor .linked-editing-decoration { background-color: var(--vscode-=
editor-linkedEditingBackground); min-width: 1px; }

.monaco-editor .detected-link, .monaco-editor .detected-link-active { text-=
decoration: underline; text-underline-position: under; }

.monaco-editor .detected-link-active { cursor: pointer; color: var(--vscode=
-editorLink-activeForeground) !important; }

.monaco-editor .rendered-markdown kbd { background-color: var(--vscode-keyb=
indingLabel-background); color: var(--vscode-keybindingLabel-foreground); b=
order-radius: 3px; border-top-color: ; border-top-style: ; border-top-width=
: ; border-right-color: ; border-right-style: ; border-right-width: ; borde=
r-bottom-style: ; border-bottom-width: ; border-left-color: ; border-left-s=
tyle: ; border-left-width: ; border-image-source: ; border-image-slice: ; b=
order-image-width: ; border-image-outset: ; border-image-repeat: ; border-b=
ottom-color: var(--vscode-keybindingLabel-bottomBorder); box-shadow: inset =
0 -1px 0 var(--vscode-widget-shadow); vertical-align: middle; padding: 1px =
3px; }

.monaco-editor .monaco-editor-overlaymessage { padding-bottom: 8px; z-index=
: 10000; }

.monaco-editor .monaco-editor-overlaymessage.below { padding-bottom: 0px; p=
adding-top: 8px; z-index: 10000; }

@keyframes fadeIn {=20
  0% { opacity: 0; }
  100% { opacity: 1; }
}

.monaco-editor .monaco-editor-overlaymessage.fadeIn { animation: 0.15s ease=
-out 0s 1 normal none running fadeIn; }

@keyframes fadeOut {=20
  0% { opacity: 1; }
  100% { opacity: 0; }
}

.monaco-editor .monaco-editor-overlaymessage.fadeOut { animation: 0.1s ease=
-out 0s 1 normal none running fadeOut; }

.monaco-editor .monaco-editor-overlaymessage .message { padding: 2px 4px; c=
olor: var(--vscode-editorHoverWidget-foreground); background-color: var(--v=
scode-editorHoverWidget-background); border: 1px solid var(--vscode-inputVa=
lidation-infoBorder); border-radius: 3px; }

.monaco-editor .monaco-editor-overlaymessage .message p { margin-block: 0px=
; }

.monaco-editor .monaco-editor-overlaymessage .message a { color: var(--vsco=
de-textLink-foreground); }

.monaco-editor .monaco-editor-overlaymessage .message a:hover { color: var(=
--vscode-textLink-activeForeground); }

.monaco-editor.hc-black .monaco-editor-overlaymessage .message, .monaco-edi=
tor.hc-light .monaco-editor-overlaymessage .message { border-width: 2px; }

.monaco-editor .monaco-editor-overlaymessage .anchor { z-index: 1000; borde=
r: 8px solid transparent; position: absolute; left: 2px; width: 0px !import=
ant; height: 0px !important; }

.monaco-editor .monaco-editor-overlaymessage .anchor.top { border-bottom-co=
lor: var(--vscode-inputValidation-infoBorder); }

.monaco-editor .monaco-editor-overlaymessage .anchor.below { border-top-col=
or: var(--vscode-inputValidation-infoBorder); }

.monaco-editor .monaco-editor-overlaymessage.below .anchor.below, .monaco-e=
ditor .monaco-editor-overlaymessage:not(.below) .anchor.top { display: none=
; }

.monaco-editor .monaco-editor-overlaymessage.below .anchor.top { display: i=
nherit; top: -8px; }

.monaco-editor .parameter-hints-widget { z-index: 39; display: flex; flex-d=
irection: column; line-height: 1.5em; cursor: default; color: var(--vscode-=
editorHoverWidget-foreground); background-color: var(--vscode-editorHoverWi=
dget-background); border: 1px solid var(--vscode-editorHoverWidget-border);=
 }

.hc-black .monaco-editor .parameter-hints-widget, .hc-light .monaco-editor =
.parameter-hints-widget { border-width: 2px; }

.monaco-editor .parameter-hints-widget > .phwrapper { max-width: 440px; dis=
play: flex; flex-direction: row; }

.monaco-editor .parameter-hints-widget.multiple { min-height: 3.3em; paddin=
g: 0px; }

.monaco-editor .parameter-hints-widget.multiple .body::before { content: ""=
; display: block; height: 100%; position: absolute; opacity: 0.5; border-le=
ft: 1px solid var(--vscode-editorHoverWidget-border); }

.monaco-editor .parameter-hints-widget p, .monaco-editor .parameter-hints-w=
idget ul { margin: 8px 0px; }

.monaco-editor .parameter-hints-widget .body, .monaco-editor .parameter-hin=
ts-widget .monaco-scrollable-element { display: flex; flex: 1 1 0%; flex-di=
rection: column; min-height: 100%; }

.monaco-editor .parameter-hints-widget .signature { padding: 4px 5px; posit=
ion: relative; }

.monaco-editor .parameter-hints-widget .signature.has-docs::after { content=
: ""; display: block; position: absolute; left: 0px; width: 100%; padding-t=
op: 4px; opacity: 0.5; border-bottom: 1px solid var(--vscode-editorHoverWid=
get-border); }

.monaco-editor .parameter-hints-widget .docs { padding: 0px 10px 0px 5px; w=
hite-space: pre-wrap; }

.monaco-editor .parameter-hints-widget .docs.empty { display: none; }

.monaco-editor .parameter-hints-widget .docs a { color: var(--vscode-textLi=
nk-foreground); }

.monaco-editor .parameter-hints-widget .docs a:hover { color: var(--vscode-=
textLink-activeForeground); cursor: pointer; }

.monaco-editor .parameter-hints-widget .docs .markdown-docs { white-space: =
normal; }

.monaco-editor .parameter-hints-widget .docs code { font-family: var(--mona=
co-monospace-font); border-radius: 3px; padding: 0px 0.4em; background-colo=
r: var(--vscode-textCodeBlock-background); }

.monaco-editor .parameter-hints-widget .docs .code, .monaco-editor .paramet=
er-hints-widget .docs .monaco-tokenized-source { white-space: pre-wrap; }

.monaco-editor .parameter-hints-widget .controls { display: none; flex-dire=
ction: column; align-items: center; min-width: 22px; justify-content: flex-=
end; }

.monaco-editor .parameter-hints-widget.multiple .controls { display: flex; =
padding: 0px 2px; }

.monaco-editor .parameter-hints-widget.multiple .button { width: 16px; heig=
ht: 16px; background-repeat: no-repeat; cursor: pointer; }

.monaco-editor .parameter-hints-widget .button.previous { bottom: 24px; }

.monaco-editor .parameter-hints-widget .overloads { text-align: center; hei=
ght: 12px; line-height: 12px; font-family: var(--monaco-monospace-font); }

.monaco-editor .parameter-hints-widget .signature .parameter.active { color=
: var(--vscode-editorHoverWidget-highlightForeground); font-weight: 700; }

.monaco-editor .parameter-hints-widget .documentation-parameter > .paramete=
r { font-weight: 700; margin-right: 0.5em; }

.monaco-editor .peekview-widget .head { box-sizing: border-box; display: fl=
ex; justify-content: space-between; flex-wrap: nowrap; }

.monaco-editor .peekview-widget .head .peekview-title { display: flex; alig=
n-items: baseline; font-size: 13px; margin-left: 20px; min-width: 0px; text=
-overflow: ellipsis; overflow: hidden; }

.monaco-editor .peekview-widget .head .peekview-title.clickable { cursor: p=
ointer; }

.monaco-editor .peekview-widget .head .peekview-title .dirname:not(:empty) =
{ font-size: 0.9em; margin-left: 0.5em; }

.monaco-editor .peekview-widget .head .peekview-title .dirname, .monaco-edi=
tor .peekview-widget .head .peekview-title .filename, .monaco-editor .peekv=
iew-widget .head .peekview-title .meta { white-space: nowrap; overflow: hid=
den; text-overflow: ellipsis; }

.monaco-editor .peekview-widget .head .peekview-title .meta:not(:empty)::be=
fore { content: "-"; padding: 0px 0.3em; }

.monaco-editor .peekview-widget .head .peekview-actions { flex: 1 1 0%; tex=
t-align: right; padding-right: 2px; }

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-ba=
r { display: inline-block; }

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-ba=
r, .monaco-editor .peekview-widget .head .peekview-actions > .monaco-action=
-bar > .actions-container { height: 100%; }

.monaco-editor .peekview-widget > .body { border-top: 1px solid; position: =
relative; }

.monaco-editor .peekview-widget .head .peekview-title .codicon { margin-rig=
ht: 4px; align-self: center; }

.monaco-editor .peekview-widget .monaco-list .monaco-list-row.focused .codi=
con { color: inherit !important; }

.monaco-editor .rename-box { z-index: 100; color: inherit; border-radius: 4=
px; }

.monaco-editor .rename-box.preview { padding: 4px 4px 0px; }

.monaco-editor .rename-box .rename-input { padding: 3px; border-radius: 2px=
; }

.monaco-editor .rename-box .rename-label { display: none; opacity: 0.8; }

.monaco-editor .rename-box.preview .rename-label { display: inherit; }

.monaco-editor .snippet-placeholder { min-width: 2px; outline-style: solid;=
 outline-width: 1px; background-color: var(--vscode-editor-snippetTabstopHi=
ghlightBackground,transparent); outline-color: var(--vscode-editor-snippetT=
abstopHighlightBorder,transparent); }

.monaco-editor .finish-snippet-placeholder { outline-style: solid; outline-=
width: 1px; background-color: var(--vscode-editor-snippetFinalTabstopHighli=
ghtBackground,transparent); outline-color: var(--vscode-editor-snippetFinal=
TabstopHighlightBorder,transparent); }

.monaco-editor .sticky-line { color: var(--vscode-editorLineNumber-foregrou=
nd); overflow: hidden; white-space: nowrap; display: inline-block; }

.monaco-editor .sticky-line-number { text-align: right; float: left; }

.monaco-editor .sticky-line-root { background-color: inherit; overflow: hid=
den; white-space: nowrap; width: 100%; }

.monaco-editor.hc-black .sticky-widget, .monaco-editor.hc-light .sticky-wid=
get { border-bottom: 1px solid var(--vscode-contrastBorder); }

.monaco-editor .sticky-line-root:hover { background-color: var(--vscode-edi=
torStickyScrollHover-background); cursor: pointer; }

.monaco-editor .sticky-widget { width: 100%; box-shadow: var(--vscode-scrol=
lbar-shadow) 0 3px 2px -2px; z-index: 4; background-color: var(--vscode-edi=
torStickyScroll-background); }

.monaco-editor .sticky-widget.peek { background-color: var(--vscode-peekVie=
wEditorStickyScroll-background); }

.monaco-editor .suggest-widget { width: 430px; z-index: 40; display: flex; =
flex-direction: column; border-radius: 3px; }

.monaco-editor .suggest-widget.message { flex-direction: row; align-items: =
center; }

.monaco-editor .suggest-details, .monaco-editor .suggest-widget { flex: 0 1=
 auto; width: 100%; border: 1px solid var(--vscode-editorSuggestWidget-bord=
er); background-color: var(--vscode-editorSuggestWidget-background); }

.monaco-editor.hc-black .suggest-details, .monaco-editor.hc-black .suggest-=
widget, .monaco-editor.hc-light .suggest-details, .monaco-editor.hc-light .=
suggest-widget { border-width: 2px; }

.monaco-editor .suggest-widget .suggest-status-bar { box-sizing: border-box=
; display: none; flex-flow: row; justify-content: space-between; width: 100=
%; font-size: 80%; padding: 0px 4px; border-top: 1px solid var(--vscode-edi=
torSuggestWidget-border); overflow: hidden; }

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar { displa=
y: flex; }

.monaco-editor .suggest-widget .suggest-status-bar .left { padding-right: 8=
px; }

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar .action-=
label { color: var(--vscode-editorSuggestWidgetStatus-foreground); }

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar .action-=
item:not(:last-of-type) .action-label { margin-right: 0px; }

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar .action-=
item:not(:last-of-type) .action-label::after { content: ", "; margin-right:=
 0.3em; }

.monaco-editor .suggest-widget.with-status-bar .monaco-list .monaco-list-ro=
w.focused.string-label > .contents > .main > .right > .readMore, .monaco-ed=
itor .suggest-widget.with-status-bar .monaco-list .monaco-list-row > .conte=
nts > .main > .right > .readMore { display: none; }

.monaco-editor .suggest-widget.with-status-bar:not(.docs-side) .monaco-list=
 .monaco-list-row:hover > .contents > .main > .right.can-expand-details > .=
details-label { width: 100%; }

.monaco-editor .suggest-widget > .message { padding-left: 22px; }

.monaco-editor .suggest-widget > .tree { height: 100%; width: 100%; }

.monaco-editor .suggest-widget .monaco-list { user-select: none; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row { display: fle=
x; box-sizing: border-box; padding-right: 10px; background-repeat: no-repea=
t; background-position: 2px 2px; white-space: nowrap; cursor: pointer; touc=
h-action: none; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused { colo=
r: var(--vscode-editorSuggestWidget-selectedForeground); }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused .codic=
on { color: var(--vscode-editorSuggestWidget-selectedIconForeground); }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents { =
flex: 1 1 0%; height: 100%; overflow: hidden; padding-left: 2px; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main { display: flex; overflow: hidden; text-overflow: ellipsis; white-spa=
ce: pre; justify-content: space-between; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main > .left, .monaco-editor .suggest-widget .monaco-list .monaco-list-row=
 > .contents > .main > .right { display: flex; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row:not(.focused) =
> .contents > .main .monaco-icon-label { color: var(--vscode-editorSuggestW=
idget-foreground); }

.monaco-editor .suggest-widget:not(.frozen) .monaco-highlighted-label .high=
light { font-weight: 700; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main .monaco-highlighted-label .highlight { color: var(--vscode-editorSugg=
estWidget-highlightForeground); }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused > .con=
tents > .main .monaco-highlighted-label .highlight { color: var(--vscode-ed=
itorSuggestWidget-focusHighlightForeground); }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .hea=
der > .codicon-close, .monaco-editor .suggest-widget .monaco-list .monaco-l=
ist-row > .contents > .main > .right > .readMore::before { color: inherit; =
opacity: 1; font-size: 14px; cursor: pointer; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .hea=
der > .codicon-close { position: absolute; top: 6px; right: 2px; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .hea=
der > .codicon-close:hover, .monaco-editor .suggest-widget .monaco-list .mo=
naco-list-row > .contents > .main > .right > .readMore:hover { opacity: 1; =
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main > .right > .details-label { opacity: 0.7; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main > .left > .signature-label { overflow: hidden; text-overflow: ellipsi=
s; opacity: 0.6; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main > .left > .qualifier-label { margin-left: 12px; opacity: 0.4; font-si=
ze: 85%; line-height: normal; text-overflow: ellipsis; overflow: hidden; al=
ign-self: center; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main > .right > .details-label { font-size: 85%; margin-left: 1.1em; overf=
low: hidden; text-overflow: ellipsis; white-space: nowrap; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main > .right > .details-label > .monaco-tokenized-source { display: inlin=
e; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main > .right > .details-label { display: none; }

.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row.focu=
sed:not(.string-label) > .contents > .main > .right > .details-label, .mona=
co-editor .suggest-widget .monaco-list .monaco-list-row:not(.string-label) =
> .contents > .main > .right > .details-label, .monaco-editor .suggest-widg=
et:not(.shows-details) .monaco-list .monaco-list-row.focused > .contents > =
.main > .right > .details-label { display: inline; }

.monaco-editor .suggest-widget:not(.docs-side) .monaco-list .monaco-list-ro=
w.focused:hover > .contents > .main > .right.can-expand-details > .details-=
label { width: calc(100% - 26px); }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main > .left { flex-shrink: 1; flex-grow: 1; overflow: hidden; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main > .left > .monaco-icon-label { flex-shrink: 0; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row:not(.string-la=
bel) > .contents > .main > .left > .monaco-icon-label { max-width: 100%; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.string-label >=
 .contents > .main > .left > .monaco-icon-label { flex-shrink: 1; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main > .right { overflow: hidden; flex-shrink: 4; max-width: 70%; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > =
.main > .right > .readMore { display: inline-block; position: absolute; rig=
ht: 10px; width: 18px; height: 18px; visibility: hidden; }

.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row > .c=
ontents > .main > .right > .readMore { display: none !important; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.string-label >=
 .contents > .main > .right > .readMore { display: none; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused.string=
-label > .contents > .main > .right > .readMore { display: inline-block; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused:hover =
> .contents > .main > .right > .readMore { visibility: visible; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-l=
abel.deprecated { opacity: 0.66; text-decoration: unset; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-l=
abel.deprecated > .monaco-icon-label-container > .monaco-icon-name-containe=
r { text-decoration: line-through; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-l=
abel::before { height: 100%; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon { displa=
y: block; height: 16px; width: 16px; margin-left: 2px; background-repeat: n=
o-repeat; background-size: 80%; background-position: 50% center; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.hide { d=
isplay: none; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .suggest-icon =
{ display: flex; align-items: center; margin-right: 4px; }

.monaco-editor .suggest-widget.no-icons .monaco-list .monaco-list-row .icon=
, .monaco-editor .suggest-widget.no-icons .monaco-list .monaco-list-row .su=
ggest-icon::before { display: none; }

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.customco=
lor .colorspan { margin: 0px 0px 0px 0.3em; border: 0.1em solid rgb(0, 0, 0=
); width: 0.7em; height: 0.7em; display: inline-block; }

.monaco-editor .suggest-details-container { z-index: 41; }

.monaco-editor .suggest-details { display: flex; flex-direction: column; cu=
rsor: default; color: var(--vscode-editorSuggestWidget-foreground); }

.monaco-editor .suggest-details.focused { border-color: var(--vscode-focusB=
order); }

.monaco-editor .suggest-details a { color: var(--vscode-textLink-foreground=
); }

.monaco-editor .suggest-details a:hover { color: var(--vscode-textLink-acti=
veForeground); }

.monaco-editor .suggest-details code { background-color: var(--vscode-textC=
odeBlock-background); }

.monaco-editor .suggest-details.no-docs { display: none; }

.monaco-editor .suggest-details > .monaco-scrollable-element { flex: 1 1 0%=
; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body { box-=
sizing: border-box; height: 100%; width: 100%; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .hea=
der > .type { flex: 2 1 0%; overflow: hidden; text-overflow: ellipsis; opac=
ity: 0.7; white-space: pre; margin: 0px 24px 0px 0px; padding: 4px 0px 12px=
 5px; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .hea=
der > .type.auto-wrap { white-space: normal; word-break: break-all; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .doc=
s { margin: 0px; padding: 4px 5px; white-space: pre-wrap; }

.monaco-editor .suggest-details.no-type > .monaco-scrollable-element > .bod=
y > .docs { margin-right: 24px; overflow: hidden; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .doc=
s.markdown-docs { padding: 0px; white-space: normal; min-height: calc(8px +=
 1rem); }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .doc=
s.markdown-docs > div, .monaco-editor .suggest-details > .monaco-scrollable=
-element > .body > .docs.markdown-docs > span:not(:empty) { padding: 4px 5p=
x; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .doc=
s.markdown-docs > div > p:first-child { margin-top: 0px; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .doc=
s.markdown-docs > div > p:last-child { margin-bottom: 0px; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .doc=
s.markdown-docs .monaco-tokenized-source { white-space: pre; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .doc=
s .code { white-space: pre-wrap; overflow-wrap: break-word; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > .doc=
s.markdown-docs .codicon { vertical-align: sub; }

.monaco-editor .suggest-details > .monaco-scrollable-element > .body > p:em=
pty { display: none; }

.monaco-editor .suggest-details code { border-radius: 3px; padding: 0px 0.4=
em; }

.monaco-editor .suggest-details ol, .monaco-editor .suggest-details ul { pa=
dding-left: 20px; }

.monaco-editor .suggest-details p code { font-family: var(--monaco-monospac=
e-font); }

.monaco-editor .codicon.codicon-symbol-array, .monaco-workbench .codicon.co=
dicon-symbol-array { color: var(--vscode-symbolIcon-arrayForeground); }

.monaco-editor .codicon.codicon-symbol-boolean, .monaco-workbench .codicon.=
codicon-symbol-boolean { color: var(--vscode-symbolIcon-booleanForeground);=
 }

.monaco-editor .codicon.codicon-symbol-class, .monaco-workbench .codicon.co=
dicon-symbol-class { color: var(--vscode-symbolIcon-classForeground); }

.monaco-editor .codicon.codicon-symbol-method, .monaco-workbench .codicon.c=
odicon-symbol-method { color: var(--vscode-symbolIcon-methodForeground); }

.monaco-editor .codicon.codicon-symbol-color, .monaco-workbench .codicon.co=
dicon-symbol-color { color: var(--vscode-symbolIcon-colorForeground); }

.monaco-editor .codicon.codicon-symbol-constant, .monaco-workbench .codicon=
.codicon-symbol-constant { color: var(--vscode-symbolIcon-constantForegroun=
d); }

.monaco-editor .codicon.codicon-symbol-constructor, .monaco-workbench .codi=
con.codicon-symbol-constructor { color: var(--vscode-symbolIcon-constructor=
Foreground); }

.monaco-editor .codicon.codicon-symbol-enum, .monaco-editor .codicon.codico=
n-symbol-value, .monaco-workbench .codicon.codicon-symbol-enum, .monaco-wor=
kbench .codicon.codicon-symbol-value { color: var(--vscode-symbolIcon-enume=
ratorForeground); }

.monaco-editor .codicon.codicon-symbol-enum-member, .monaco-workbench .codi=
con.codicon-symbol-enum-member { color: var(--vscode-symbolIcon-enumeratorM=
emberForeground); }

.monaco-editor .codicon.codicon-symbol-event, .monaco-workbench .codicon.co=
dicon-symbol-event { color: var(--vscode-symbolIcon-eventForeground); }

.monaco-editor .codicon.codicon-symbol-field, .monaco-workbench .codicon.co=
dicon-symbol-field { color: var(--vscode-symbolIcon-fieldForeground); }

.monaco-editor .codicon.codicon-symbol-file, .monaco-workbench .codicon.cod=
icon-symbol-file { color: var(--vscode-symbolIcon-fileForeground); }

.monaco-editor .codicon.codicon-symbol-folder, .monaco-workbench .codicon.c=
odicon-symbol-folder { color: var(--vscode-symbolIcon-folderForeground); }

.monaco-editor .codicon.codicon-symbol-function, .monaco-workbench .codicon=
.codicon-symbol-function { color: var(--vscode-symbolIcon-functionForegroun=
d); }

.monaco-editor .codicon.codicon-symbol-interface, .monaco-workbench .codico=
n.codicon-symbol-interface { color: var(--vscode-symbolIcon-interfaceForegr=
ound); }

.monaco-editor .codicon.codicon-symbol-key, .monaco-workbench .codicon.codi=
con-symbol-key { color: var(--vscode-symbolIcon-keyForeground); }

.monaco-editor .codicon.codicon-symbol-keyword, .monaco-workbench .codicon.=
codicon-symbol-keyword { color: var(--vscode-symbolIcon-keywordForeground);=
 }

.monaco-editor .codicon.codicon-symbol-module, .monaco-workbench .codicon.c=
odicon-symbol-module { color: var(--vscode-symbolIcon-moduleForeground); }

.monaco-editor .codicon.codicon-symbol-namespace, .monaco-workbench .codico=
n.codicon-symbol-namespace { color: var(--vscode-symbolIcon-namespaceForegr=
ound); }

.monaco-editor .codicon.codicon-symbol-null, .monaco-workbench .codicon.cod=
icon-symbol-null { color: var(--vscode-symbolIcon-nullForeground); }

.monaco-editor .codicon.codicon-symbol-number, .monaco-workbench .codicon.c=
odicon-symbol-number { color: var(--vscode-symbolIcon-numberForeground); }

.monaco-editor .codicon.codicon-symbol-object, .monaco-workbench .codicon.c=
odicon-symbol-object { color: var(--vscode-symbolIcon-objectForeground); }

.monaco-editor .codicon.codicon-symbol-operator, .monaco-workbench .codicon=
.codicon-symbol-operator { color: var(--vscode-symbolIcon-operatorForegroun=
d); }

.monaco-editor .codicon.codicon-symbol-package, .monaco-workbench .codicon.=
codicon-symbol-package { color: var(--vscode-symbolIcon-packageForeground);=
 }

.monaco-editor .codicon.codicon-symbol-property, .monaco-workbench .codicon=
.codicon-symbol-property { color: var(--vscode-symbolIcon-propertyForegroun=
d); }

.monaco-editor .codicon.codicon-symbol-reference, .monaco-workbench .codico=
n.codicon-symbol-reference { color: var(--vscode-symbolIcon-referenceForegr=
ound); }

.monaco-editor .codicon.codicon-symbol-snippet, .monaco-workbench .codicon.=
codicon-symbol-snippet { color: var(--vscode-symbolIcon-snippetForeground);=
 }

.monaco-editor .codicon.codicon-symbol-string, .monaco-workbench .codicon.c=
odicon-symbol-string { color: var(--vscode-symbolIcon-stringForeground); }

.monaco-editor .codicon.codicon-symbol-struct, .monaco-workbench .codicon.c=
odicon-symbol-struct { color: var(--vscode-symbolIcon-structForeground); }

.monaco-editor .codicon.codicon-symbol-text, .monaco-workbench .codicon.cod=
icon-symbol-text { color: var(--vscode-symbolIcon-textForeground); }

.monaco-editor .codicon.codicon-symbol-type-parameter, .monaco-workbench .c=
odicon.codicon-symbol-type-parameter { color: var(--vscode-symbolIcon-typeP=
arameterForeground); }

.monaco-editor .codicon.codicon-symbol-unit, .monaco-workbench .codicon.cod=
icon-symbol-unit { color: var(--vscode-symbolIcon-unitForeground); }

.monaco-editor .codicon.codicon-symbol-variable, .monaco-workbench .codicon=
.codicon-symbol-variable { color: var(--vscode-symbolIcon-variableForegroun=
d); }

.editor-banner { box-sizing: border-box; cursor: default; width: 100%; font=
-size: 12px; display: flex; overflow: visible; height: 26px; background: va=
r(--vscode-banner-background); }

.editor-banner .icon-container { display: flex; flex-shrink: 0; align-items=
: center; padding: 0px 6px 0px 10px; }

.editor-banner .icon-container.custom-icon { background-repeat: no-repeat; =
background-position: 50% center; background-size: 16px; width: 16px; paddin=
g: 0px; margin: 0px 6px 0px 10px; }

.editor-banner .message-container { display: flex; align-items: center; lin=
e-height: 26px; text-overflow: ellipsis; white-space: nowrap; overflow: hid=
den; }

.editor-banner .message-container p { margin-block: 0px; }

.editor-banner .message-actions-container { flex-grow: 1; flex-shrink: 0; l=
ine-height: 26px; margin: 0px 4px; }

.editor-banner .message-actions-container a.monaco-button { width: inherit;=
 margin: 2px 8px; padding: 0px 12px; }

.editor-banner .message-actions-container a { padding: 3px; margin-left: 12=
px; text-decoration: underline; }

.editor-banner .action-container { padding: 0px 10px 0px 6px; }

.editor-banner { background-color: var(--vscode-banner-background); }

.editor-banner, .editor-banner .action-container .codicon, .editor-banner .=
message-actions-container .monaco-link { color: var(--vscode-banner-foregro=
und); }

.editor-banner .icon-container .codicon { color: var(--vscode-banner-iconFo=
reground); }

.monaco-editor .unicode-highlight { border: 1px solid var(--vscode-editorUn=
icodeHighlight-border); background-color: var(--vscode-editorUnicodeHighlig=
ht-background); box-sizing: border-box; }

.monaco-editor .focused .selectionHighlight { background-color: var(--vscod=
e-editor-selectionHighlightBackground); box-sizing: border-box; border: 1px=
 solid var(--vscode-editor-selectionHighlightBorder); }

.monaco-editor.hc-black .focused .selectionHighlight, .monaco-editor.hc-lig=
ht .focused .selectionHighlight { border-style: dotted; }

.monaco-editor .wordHighlight { background-color: var(--vscode-editor-wordH=
ighlightBackground); box-sizing: border-box; border: 1px solid var(--vscode=
-editor-wordHighlightBorder); }

.monaco-editor.hc-black .wordHighlight, .monaco-editor.hc-light .wordHighli=
ght { border-style: dotted; }

.monaco-editor .wordHighlightStrong { background-color: var(--vscode-editor=
-wordHighlightStrongBackground); box-sizing: border-box; border: 1px solid =
var(--vscode-editor-wordHighlightStrongBorder); }

.monaco-editor.hc-black .wordHighlightStrong, .monaco-editor.hc-light .word=
HighlightStrong { border-style: dotted; }

.monaco-editor .wordHighlightText { background-color: var(--vscode-editor-w=
ordHighlightTextBackground); box-sizing: border-box; border: 1px solid var(=
--vscode-editor-wordHighlightTextBorder); }

.monaco-editor.hc-black .wordHighlightText, .monaco-editor.hc-light .wordHi=
ghlightText { border-style: dotted; }

.monaco-editor .zone-widget { position: absolute; z-index: 10; }

.monaco-editor .zone-widget .zone-widget-container { border-top-style: soli=
d; border-bottom-style: solid; border-top-width: 0px; border-bottom-width: =
0px; position: relative; }

.monaco-editor .iPadShowKeyboard { width: 58px; min-width: 0px; height: 36p=
x; min-height: 0px; margin: 0px; padding: 0px; position: absolute; resize: =
none; overflow: hidden; background: url("data:image/svg+xml;base64,PHN2ZyB3=
aWR0aD0iNTMiIGhlaWdodD0iMzYiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9=
yZy8yMDAwL3N2ZyI+PGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwKSI+PHBhdGggZmlsbC1ydWxlPS=
JldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00OC4wMzYgNC4wMUg0LjAwOFYzMi4wM=
2g0NC4wMjhWNC4wMXpNNC4wMDguMDA4QTQuMDAzIDQuMDAzIDAgMDAuMDA1IDQuMDFWMzIuMDNh=
NC4wMDMgNC4wMDMgMCAwMDQuMDAzIDQuMDAyaDQ0LjAyOGE0LjAwMyA0LjAwMyAwIDAwNC4wMDM=
tNC4wMDJWNC4wMUE0LjAwMyA0LjAwMyAwIDAwNDguMDM2LjAwOEg0LjAwOHpNOC4wMSA4LjAxM2=
g0LjAwM3Y0LjAwM0g4LjAxVjguMDEzem0xMi4wMDggMGgtNC4wMDJ2NC4wMDNoNC4wMDJWOC4wM=
TN6bTQuMDAzIDBoNC4wMDJ2NC4wMDNoLTQuMDAyVjguMDEzem0xMi4wMDggMGgtNC4wMDN2NC4w=
MDNoNC4wMDNWOC4wMTN6bTQuMDAyIDBoNC4wMDN2NC4wMDNINDAuMDNWOC4wMTN6bS0yNC4wMTU=
gOC4wMDVIOC4wMXY0LjAwM2g4LjAwNnYtNC4wMDN6bTQuMDAyIDBoNC4wMDN2NC4wMDNoLTQuMD=
Azdi00LjAwM3ptMTIuMDA4IDBoLTQuMDAzdjQuMDAzaDQuMDAzdi00LjAwM3ptMTIuMDA4IDB2N=
C4wMDNoLTguMDA1di00LjAwM2g4LjAwNXptLTMyLjAyMSA4LjAwNUg4LjAxdjQuMDAzaDQuMDAz=
di00LjAwM3ptNC4wMDMgMGgyMC4wMTN2NC4wMDNIMTYuMDE2di00LjAwM3ptMjguMDE4IDBINDA=
uMDN2NC4wMDNoNC4wMDN2LTQuMDAzeiIgZmlsbD0iIzQyNDI0MiIvPjwvZz48ZGVmcz48Y2xpcF=
BhdGggaWQ9ImNsaXAwIj48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMCAwaDUzdjM2SDB6Ii8+PC9jb=
GlwUGF0aD48L2RlZnM+PC9zdmc+") 50% center no-repeat; border: 4px solid rgb(2=
46, 246, 246); border-radius: 4px; }

.monaco-editor.vs-dark .iPadShowKeyboard { background: url("data:image/svg+=
xml;base64,PHN2ZyB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIGZpbGw9Im5vbmUiIHhtbG5zPSJo=
dHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwKSI+PHB=
hdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00OC4wMzYgNC=
4wMUg0LjAwOFYzMi4wM2g0NC4wMjhWNC4wMXpNNC4wMDguMDA4QTQuMDAzIDQuMDAzIDAgMDAuM=
DA1IDQuMDFWMzIuMDNhNC4wMDMgNC4wMDMgMCAwMDQuMDAzIDQuMDAyaDQ0LjAyOGE0LjAwMyA0=
LjAwMyAwIDAwNC4wMDMtNC4wMDJWNC4wMUE0LjAwMyA0LjAwMyAwIDAwNDguMDM2LjAwOEg0LjA=
wOHpNOC4wMSA4LjAxM2g0LjAwM3Y0LjAwM0g4LjAxVjguMDEzem0xMi4wMDggMGgtNC4wMDJ2NC=
4wMDNoNC4wMDJWOC4wMTN6bTQuMDAzIDBoNC4wMDJ2NC4wMDNoLTQuMDAyVjguMDEzem0xMi4wM=
DggMGgtNC4wMDN2NC4wMDNoNC4wMDNWOC4wMTN6bTQuMDAyIDBoNC4wMDN2NC4wMDNINDAuMDNW=
OC4wMTN6bS0yNC4wMTUgOC4wMDVIOC4wMXY0LjAwM2g4LjAwNnYtNC4wMDN6bTQuMDAyIDBoNC4=
wMDN2NC4wMDNoLTQuMDAzdi00LjAwM3ptMTIuMDA4IDBoLTQuMDAzdjQuMDAzaDQuMDAzdi00Lj=
AwM3ptMTIuMDA4IDB2NC4wMDNoLTguMDA1di00LjAwM2g4LjAwNXptLTMyLjAyMSA4LjAwNUg4L=
jAxdjQuMDAzaDQuMDAzdi00LjAwM3ptNC4wMDMgMGgyMC4wMTN2NC4wMDNIMTYuMDE2di00LjAw=
M3ptMjguMDE4IDBINDAuMDN2NC4wMDNoNC4wMDN2LTQuMDAzeiIgZmlsbD0iI0M1QzVDNSIvPjw=
vZz48ZGVmcz48Y2xpcFBhdGggaWQ9ImNsaXAwIj48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMCAwaD=
UzdjM2SDB6Ii8+PC9jbGlwUGF0aD48L2RlZnM+PC9zdmc+") 50% center no-repeat; bord=
er: 4px solid rgb(37, 37, 38); }

.monaco-editor .tokens-inspect-widget { z-index: 50; user-select: text; pad=
ding: 10px; color: var(--vscode-editorHoverWidget-foreground); background-c=
olor: var(--vscode-editorHoverWidget-background); border: 1px solid var(--v=
scode-editorHoverWidget-border); }

.monaco-editor.hc-black .tokens-inspect-widget, .monaco-editor.hc-light .to=
kens-inspect-widget { border-width: 2px; }

.monaco-editor .tokens-inspect-widget .tokens-inspect-separator { height: 1=
px; border: 0px; background-color: var(--vscode-editorHoverWidget-border); =
}

.monaco-editor .tokens-inspect-widget .tm-token { font-family: var(--monaco=
-monospace-font); }

.monaco-editor .tokens-inspect-widget .tm-token-length { font-weight: 400; =
font-size: 60%; float: right; }

.monaco-editor .tokens-inspect-widget .tm-metadata-table { width: 100%; }

.monaco-editor .tokens-inspect-widget .tm-metadata-value { font-family: var=
(--monaco-monospace-font); text-align: right; }

.monaco-editor .tokens-inspect-widget .tm-token-type { font-family: var(--m=
onaco-monospace-font); }

.quick-input-widget { font-size: 13px; }

.quick-input-widget .monaco-highlighted-label .highlight { color: rgb(0, 10=
2, 191); }

.vs .quick-input-widget .monaco-list-row.focused .monaco-highlighted-label =
.highlight { color: rgb(157, 221, 255); }

.vs-dark .quick-input-widget .monaco-highlighted-label .highlight { color: =
rgb(0, 151, 251); }

.hc-black .quick-input-widget .monaco-highlighted-label .highlight { color:=
 rgb(243, 133, 24); }

.hc-light .quick-input-widget .monaco-highlighted-label .highlight { color:=
 rgb(15, 74, 133); }

.monaco-keybinding > .monaco-keybinding-key { background-color: rgba(221, 2=
21, 221, 0.4); border-width: 1px; border-style: solid; border-color: rgba(2=
04, 204, 204, 0.4) rgba(204, 204, 204, 0.4) rgba(187, 187, 187, 0.4); borde=
r-image: initial; box-shadow: rgba(187, 187, 187, 0.4) 0px -1px 0px inset; =
color: rgb(85, 85, 85); }

.hc-black .monaco-keybinding > .monaco-keybinding-key { background-color: t=
ransparent; border: 1px solid rgb(111, 195, 223); box-shadow: none; color: =
rgb(255, 255, 255); }

.hc-light .monaco-keybinding > .monaco-keybinding-key { background-color: t=
ransparent; border: 1px solid rgb(15, 74, 133); box-shadow: none; color: rg=
b(41, 41, 41); }

.vs-dark .monaco-keybinding > .monaco-keybinding-key { background-color: rg=
ba(128, 128, 128, 0.17); border-width: 1px; border-style: solid; border-col=
or: rgba(51, 51, 51, 0.6) rgba(51, 51, 51, 0.6) rgba(68, 68, 68, 0.6); bord=
er-image: initial; box-shadow: rgba(68, 68, 68, 0.6) 0px -1px 0px inset; co=
lor: rgb(204, 204, 204); }

.monaco-editor { font-family: -apple-system, BlinkMacSystemFont, "Segoe WPC=
", "Segoe UI", HelveticaNeue-Light, system-ui, Ubuntu, "Droid Sans", sans-s=
erif; --monaco-monospace-font: "SF Mono",Monaco,Menlo,Consolas,"Ubuntu Mono=
","Liberation Mono","DejaVu Sans Mono","Courier New",monospace; }

.monaco-editor.hc-black .monaco-menu .monaco-action-bar.vertical .action-me=
nu-item:focus .action-label, .monaco-editor.hc-light .monaco-menu .monaco-a=
ction-bar.vertical .action-menu-item:focus .action-label, .monaco-editor.vs=
-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .act=
ion-label, .monaco-menu .monaco-action-bar.vertical .action-item .action-me=
nu-item:focus .action-label { stroke-width: 1.2px; }

.monaco-hover p { margin: 0px; }

.monaco-aria-container { top: 0px; height: 1px; width: 1px; margin: -1px; o=
verflow: hidden; padding: 0px; clip: rect(1px, 1px, 1px, 1px); clip-path: i=
nset(50%); position: absolute !important; }

.action-widget { font-size: 13px; border-radius: 0px; min-width: 160px; max=
-width: 500px; z-index: 40; display: block; width: 100%; background-color: =
var(--vscode-editorWidget-background); color: var(--vscode-editorWidget-for=
eground); border: 1px solid var(--vscode-editorWidget-border) !important; }

.context-view-block { z-index: -1; }

.context-view-block, .context-view-pointerBlock { position: fixed; cursor: =
auto; left: 0px; top: 0px; width: 100%; height: 100%; }

.context-view-pointerBlock { z-index: 2; }

.action-widget .monaco-list { user-select: none; border: 0px !important; }

.action-widget .monaco-list:focus::before { outline: 0px !important; }

.action-widget .monaco-list .monaco-scrollable-element { overflow: visible;=
 }

.action-widget .monaco-list .monaco-list-row { padding: 0px 10px; white-spa=
ce: nowrap; cursor: pointer; touch-action: none; width: 100%; }

.action-widget .monaco-list .monaco-list-row.action.focused:not(.option-dis=
abled) { color: var(--vscode-quickInputList-focusForeground); outline: 1px =
solid var(--vscode-menu-selectionBorder,transparent); outline-offset: -1px;=
 background-color: var(--vscode-quickInputList-focusBackground) !important;=
 }

.action-widget .monaco-list-row.group-header { color: var(--vscode-pickerGr=
oup-foreground) !important; font-weight: 600; }

.action-widget .monaco-list .group-header, .action-widget .monaco-list .opt=
ion-disabled, .action-widget .monaco-list .option-disabled .focused, .actio=
n-widget .monaco-list .option-disabled .focused::before, .action-widget .mo=
naco-list .option-disabled::before { user-select: none; cursor: default !im=
portant; background-color: transparent !important; outline: solid 0px !impo=
rtant; }

.action-widget .monaco-list-row.action { display: flex; gap: 6px; align-ite=
ms: center; }

.action-widget .monaco-list-row.action.option-disabled { color: var(--vscod=
e-disabledForeground); }

.action-widget .monaco-list-row.action.option-disabled .codicon { opacity: =
0.4; }

.action-widget .monaco-list-row.action:not(.option-disabled) .codicon { col=
or: inherit; }

.action-widget .monaco-list-row.action .title { flex: 1 1 0%; overflow: hid=
den; text-overflow: ellipsis; }

.action-widget .action-widget-action-bar { background-color: var(--vscode-e=
ditorHoverWidget-statusBarBackground); border-top: 1px solid var(--vscode-e=
ditorHoverWidget-border); }

.action-widget .action-widget-action-bar::before { display: block; content:=
 ""; width: 100%; }

.action-widget .action-widget-action-bar .actions-container { padding: 0px =
8px; }

.action-widget-action-bar .action-label { color: var(--vscode-textLink-acti=
veForeground); font-size: 12px; line-height: 22px; padding: 0px; pointer-ev=
ents: all; }

.action-widget-action-bar .action-item { margin-right: 16px; pointer-events=
: none; }

.action-widget-action-bar .action-label:hover { background-color: transpare=
nt !important; }

.monaco-action-bar .action-item.menu-entry .action-label.icon { width: 16px=
; height: 16px; background-repeat: no-repeat; background-position: 50% cent=
er; background-size: 16px; }

.monaco-dropdown-with-default { flex-direction: row; border-radius: 5px; di=
splay: flex !important; }

.monaco-dropdown-with-default > .action-container > .action-label { margin-=
right: 0px; }

.monaco-dropdown-with-default > .action-container.menu-entry > .action-labe=
l.icon { width: 16px; height: 16px; background-repeat: no-repeat; backgroun=
d-position: 50% center; background-size: 16px; }

.monaco-dropdown-with-default > .dropdown-action-container > .monaco-dropdo=
wn > .dropdown-label .codicon[class*=3D"codicon-"] { font-size: 12px; paddi=
ng-left: 0px; padding-right: 0px; line-height: 16px; margin-left: -3px; }

.monaco-dropdown-with-default > .dropdown-action-container > .monaco-dropdo=
wn > .dropdown-label > .action-label { display: block; background-size: 16p=
x; background-position: 50% center; background-repeat: no-repeat; }

.monaco-link { color: var(--vscode-textLink-foreground); }

.monaco-link:hover { color: var(--vscode-textLink-activeForeground); }

.quick-input-widget { position: absolute; width: 600px; z-index: 2550; left=
: 50%; margin-left: -300px; app-region: no-drag; border-radius: 6px; }

.quick-input-titlebar { display: flex; align-items: center; border-top-left=
-radius: 5px; border-top-right-radius: 5px; }

.quick-input-left-action-bar { display: flex; margin-left: 4px; flex: 1 1 0=
%; }

.quick-input-title { padding: 3px 0px; text-align: center; text-overflow: e=
llipsis; overflow: hidden; }

.quick-input-right-action-bar { display: flex; margin-right: 4px; flex: 1 1=
 0%; }

.quick-input-right-action-bar > .actions-container { justify-content: flex-=
end; }

.quick-input-titlebar .monaco-action-bar .action-label.codicon { background=
-position: 50% center; background-repeat: no-repeat; padding: 2px; }

.quick-input-description { margin: 6px; }

.quick-input-header .quick-input-description { margin: 4px 2px; }

.quick-input-header { display: flex; padding: 8px 6px 6px; }

.quick-input-widget.hidden-input .quick-input-header { padding: 0px; margin=
-bottom: 0px; }

.quick-input-and-message { display: flex; flex-direction: column; flex-grow=
: 1; min-width: 0px; position: relative; }

.quick-input-check-all { align-self: center; margin: 0px; }

.quick-input-filter { flex-grow: 1; display: flex; position: relative; }

.quick-input-box { flex-grow: 1; }

.quick-input-widget.show-checkboxes .quick-input-box, .quick-input-widget.s=
how-checkboxes .quick-input-message { margin-left: 5px; }

.quick-input-visible-count { position: absolute; left: -10000px; }

.quick-input-count { align-self: center; position: absolute; right: 4px; di=
splay: flex; align-items: center; }

.quick-input-count .monaco-count-badge { vertical-align: middle; padding: 2=
px 4px; border-radius: 2px; min-height: auto; line-height: normal; }

.quick-input-action { margin-left: 6px; }

.quick-input-action .monaco-text-button { font-size: 11px; padding: 0px 6px=
; display: flex; height: 25px; align-items: center; }

.quick-input-message { margin-top: -1px; padding: 5px; overflow-wrap: break=
-word; }

.quick-input-message > .codicon { margin: 0px 0.2em; vertical-align: text-b=
ottom; }

.quick-input-message a { color: inherit; }

.quick-input-progress.monaco-progress-container { position: relative; }

.quick-input-progress.monaco-progress-container, .quick-input-progress.mona=
co-progress-container .progress-bit { height: 2px; }

.quick-input-list { line-height: 22px; }

.quick-input-widget.hidden-input .quick-input-list { margin-top: 4px; paddi=
ng-bottom: 4px; }

.quick-input-list .monaco-list { overflow: hidden; max-height: 440px; paddi=
ng-bottom: 5px; }

.quick-input-list .monaco-scrollable-element { padding: 0px 5px; }

.quick-input-list .quick-input-list-entry { box-sizing: border-box; overflo=
w: hidden; display: flex; height: 100%; padding: 0px 6px; }

.quick-input-list .quick-input-list-entry.quick-input-list-separator-border=
 { border-top-width: 1px; border-top-style: solid; }

.quick-input-list .monaco-list-row { border-radius: 3px; }

.quick-input-list .monaco-list-row[data-index=3D"0"] .quick-input-list-entr=
y.quick-input-list-separator-border { border-top-style: none; }

.quick-input-list .quick-input-list-label { overflow: hidden; display: flex=
; height: 100%; flex: 1 1 0%; }

.quick-input-list .quick-input-list-checkbox { align-self: center; margin: =
0px; }

.quick-input-list .quick-input-list-icon { background-size: 16px; backgroun=
d-position: 0px center; background-repeat: no-repeat; padding-right: 6px; w=
idth: 16px; height: 22px; display: flex; align-items: center; justify-conte=
nt: center; }

.quick-input-list .quick-input-list-rows { overflow: hidden; text-overflow:=
 ellipsis; display: flex; flex-direction: column; height: 100%; flex: 1 1 0=
%; margin-left: 5px; }

.quick-input-widget.show-checkboxes .quick-input-list .quick-input-list-row=
s { margin-left: 10px; }

.quick-input-widget .quick-input-list .quick-input-list-checkbox { display:=
 none; }

.quick-input-widget.show-checkboxes .quick-input-list .quick-input-list-che=
ckbox { display: inline; }

.quick-input-list .quick-input-list-rows > .quick-input-list-row { display:=
 flex; align-items: center; }

.quick-input-list .quick-input-list-rows > .quick-input-list-row .monaco-ic=
on-label, .quick-input-list .quick-input-list-rows > .quick-input-list-row =
.monaco-icon-label .monaco-icon-label-container > .monaco-icon-name-contain=
er { flex: 1 1 0%; }

.quick-input-list .quick-input-list-rows > .quick-input-list-row .codicon[c=
lass*=3D"codicon-"] { vertical-align: text-bottom; }

.quick-input-list .quick-input-list-rows .monaco-highlighted-label > span {=
 opacity: 1; }

.quick-input-list .quick-input-list-entry .quick-input-list-entry-keybindin=
g { margin-right: 8px; }

.quick-input-list .quick-input-list-label-meta { opacity: 0.7; line-height:=
 normal; text-overflow: ellipsis; overflow: hidden; }

.quick-input-list .monaco-highlighted-label .highlight { font-weight: 700; =
}

.quick-input-list .quick-input-list-entry .quick-input-list-separator { mar=
gin-right: 4px; }

.quick-input-list .quick-input-list-entry-action-bar { display: flex; flex:=
 0 1 0%; overflow: visible; }

.quick-input-list .quick-input-list-entry-action-bar .action-label { displa=
y: none; }

.quick-input-list .quick-input-list-entry-action-bar .action-label.codicon =
{ margin-right: 4px; padding: 0px 2px 2px; }

.quick-input-list .quick-input-list-entry-action-bar { margin-top: 1px; mar=
gin-right: 4px; }

.quick-input-list .monaco-list-row.focused .quick-input-list-entry-action-b=
ar .action-label, .quick-input-list .quick-input-list-entry .quick-input-li=
st-entry-action-bar .action-label.always-visible, .quick-input-list .quick-=
input-list-entry:hover .quick-input-list-entry-action-bar .action-label { d=
isplay: flex; }

.quick-input-list .monaco-list-row.focused .monaco-keybinding-key, .quick-i=
nput-list .monaco-list-row.focused .quick-input-list-entry .quick-input-lis=
t-separator { color: inherit; }

.quick-input-list .monaco-list-row.focused .monaco-keybinding-key { backgro=
und: none; }

.extension-editor .codicon.codicon-error, .extensions-viewlet > .extensions=
 .codicon.codicon-error, .markers-panel .marker-icon .codicon.codicon-error=
, .markers-panel .marker-icon.error, .monaco-editor .zone-widget .codicon.c=
odicon-error, .preferences-editor .codicon.codicon-error, .text-search-prov=
ider-messages .providerMessage .codicon.codicon-error { color: var(--vscode=
-problemsErrorIcon-foreground); }

.extension-editor .codicon.codicon-warning, .extensions-viewlet > .extensio=
ns .codicon.codicon-warning, .markers-panel .marker-icon .codicon.codicon-w=
arning, .markers-panel .marker-icon.warning, .monaco-editor .zone-widget .c=
odicon.codicon-warning, .preferences-editor .codicon.codicon-warning, .text=
-search-provider-messages .providerMessage .codicon.codicon-warning { color=
: var(--vscode-problemsWarningIcon-foreground); }

.extension-editor .codicon.codicon-info, .extensions-viewlet > .extensions =
.codicon.codicon-info, .markers-panel .marker-icon .codicon.codicon-info, .=
markers-panel .marker-icon.info, .monaco-editor .zone-widget .codicon.codic=
on-info, .preferences-editor .codicon.codicon-info, .text-search-provider-m=
essages .providerMessage .codicon.codicon-info { color: var(--vscode-proble=
msInfoIcon-foreground); }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: https://www.gstatic.com/og/_/ss/k=og.qtm.vjyYcS7rQwo.L.W.O/m=qcwid,qba,d_b_gm3,d_wi_gm3,d_lo_gm3/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTtEJMqNNb04d2z46AITatL-Y66Oww

@charset "utf-8";

.gb_Vc.gb_he:focus-visible { outline: rgb(32, 33, 36) solid 1px; border-rad=
ius: 4px; }

.gb_2c .gb_Vc.gb_he:focus-visible { outline-color: rgb(241, 243, 244); }

.gb_Tc { display: inline-block; position: relative; overflow: hidden; top: =
2px; user-select: none; }

.gb_de { max-width: 100%; }

.gb_ee .gb_Tc { display: none; }

.gb_Kd .gb_Uc { line-height: normal; position: relative; padding-left: 16px=
; }

.gb_rd.gb_sd .gb_Uc { padding-left: 0px; }

.gb_rd .gb_Uc { padding-left: 12px; }

.gb_Vc { -webkit-box-align: center; align-items: center; display: flex; out=
line: none; text-decoration: none; }

.gb_Vc.gb_fe { direction: ltr; }

.gb_Vc.gb_fe .gb_Qd { padding-left: 8px; padding-right: 0px; }

.gb_e .gb_Vc .gb_ge::before { background-image: url("https://www.gstatic.co=
m/images/branding/googlelogo/svg/googlelogo_clr_74x24px.svg"); background-r=
epeat: no-repeat; background-position: center center; background-size: cont=
ain; content: ""; display: inline-block; height: 24px; width: 74px; }

.gb_Vc .gb_ge { height: 24px; width: 74px; }

.gb_Vc .gb_ge, .gb_Vc { vertical-align: middle; }

.gb_Vc .gb_ge { display: inline-block; outline: none; }

.gb_8a { display: inline-block; vertical-align: middle; }

.gb_Zc { border: none; display: block; visibility: hidden; }

img.gb_0c { border: 0px; vertical-align: middle; }

.gb_3a:not(.gb_H) .gb_Vc .gb_ge::before { background-image: url("https://ww=
w.gstatic.com/images/branding/googlelogo/svg/googlelogo_surface_dark_74x24p=
x.svg"); }

.gb_2a:not(.gb_H) .gb_Vc .gb_ge::before { background-image: url("https://ww=
w.gstatic.com/images/branding/googlelogo/svg/googlelogo_on_surface_dark_74x=
24px.svg"); }

.gb_e.gb_bd .gb_Vc .gb_ge::before, .gb_e.gb_H .gb_Vc .gb_ge::before { backg=
round-image: url("https://www.gstatic.com/images/branding/googlelogo/svg/go=
oglelogo_light_clr_74x24px.svg"); }

.gb_2a.gb_H .gb_Vc .gb_ge::before { background-image: url("https://www.gsta=
tic.com/images/branding/googlelogo/svg/googlelogo_on_surface_light_74x24px.=
svg"); }

@media screen and (-ms-high-contrast:black-on-white) {
  .gb_e .gb_2c .gb_Vc .gb_ge::before { background-image: url("https://www.g=
static.com/images/branding/googlelogo/svg/googlelogo_dark_clr_74x24px.svg")=
; }
}

@media screen and (-ms-high-contrast:white-on-black) {
  .gb_9d .gb_Vc .gb_ge::before { background-image: url("https://www.gstatic=
.com/images/branding/googlelogo/svg/googlelogo_light_clr_74x24px.svg"); }
}

.gb_8a { background-repeat: no-repeat; }

.gb_Qd { display: block; font-family: "Product Sans", Arial, sans-serif; fo=
nt-size: 22px; line-height: 48px; overflow: hidden; padding-left: 8px; posi=
tion: relative; text-overflow: ellipsis; top: -1.5px; vertical-align: middl=
e; }

.gb_rd .gb_Qd { padding-left: 4px; }

.gb_rd .gb_Qd.gb_ie { padding-left: 0px; }

.gb_0c.gb_ae { padding-right: 4px; }

.gb_bd .gb_qd.gb_Qd { opacity: 1; }

.gb_de:focus .gb_Qd { text-decoration: underline; }

.gb_je img.gb_0c { margin-bottom: 4px; }

.gb_ke { display: none; }

.gb_R { border-radius: 50%; bottom: 2px; height: 18px; position: absolute; =
right: 0px; width: 18px; }

.gb_La { border-radius: 50%; box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px =
0px, rgba(60, 64, 67, 0.15) 0px 1px 3px 1px; margin: 2px; }

.gb_Ma { fill: rgb(249, 171, 0); }

.gb_H .gb_Ma { fill: rgb(253, 214, 99); }

.gb_Na > .gb_Ma { fill: rgb(217, 48, 37); }

.gb_H .gb_Na > .gb_Ma { fill: rgb(242, 139, 130); }

.gb_Na > .gb_Oa { fill: white; }

.gb_Oa, .gb_H .gb_Na > .gb_Oa { fill: rgb(32, 33, 36); }

.gb_Pa { clip-path: path("M 16 0 C 24.8366 0 32 7.16344 32 16 C 32 16.4964 =
31.9774 16.9875 31.9332 17.4723 C 30.5166 16.5411 28.8215 16 27 16 C 22.029=
4 16 18 20.0294 18 25 C 18 27.4671 18.9927 29.7024 20.6004 31.3282 C 19.144=
3 31.7653 17.5996 32 16 32 C 7.16344 32 0 24.8366 0 16 C 0 7.16344 7.16344 =
0 16 0 Z"); }

.gb_B .gb_R { display: block; }

.gb_Qc { background: rgba(60, 64, 67, 0.9); border-radius: 4px; color: rgb(=
255, 255, 255); font: 500 12px / 16px Roboto, arial, sans-serif; letter-spa=
cing: 0.8px; margin-top: 4px; min-height: 14px; padding: 4px 8px; position:=
 absolute; outline: transparent solid 1px; user-select: text; z-index: 1000=
; -webkit-font-smoothing: antialiased; }

.gb_Rc, .gb_Sc { text-align: left; }

.gb_Rc > * { color: rgb(196, 199, 197); line-height: 16px; }

.gb_Rc div:first-child { color: white; }

.gb_Fa { background: none; border: 1px solid transparent; border-radius: 50=
%; box-sizing: border-box; cursor: pointer; height: 40px; margin: 8px; outl=
ine: none; padding: 1px; position: absolute; right: 0px; top: 0px; width: 4=
0px; }

.gb_Fa:hover { background-color: rgba(68, 71, 70, 0.08); }

.gb_Fa:focus, .gb_Fa:active { background-color: rgba(68, 71, 70, 0.12); }

.gb_Fa:focus-visible { border-color: rgb(11, 87, 208); outline: transparent=
 solid 1px; outline-offset: -1px; }

.gb_H .gb_Fa:hover { background-color: rgba(227, 227, 227, 0.08); }

.gb_H .gb_Fa:focus, .gb_H .gb_Fa:active { background-color: rgba(227, 227, =
227, 0.08); }

.gb_H .gb_Fa:focus-visible { border-color: rgb(168, 199, 250); }

.gb_Ha .gb_Ia { border: 1px solid transparent; border-radius: 4px; color: r=
gb(11, 87, 208); }

.gb_Ia:hover { color: rgb(8, 66, 160); }

.gb_Ia:focus, .gb_Ia:active { color: rgb(6, 46, 111); }

.gb_Ia:focus-visible { border-color: rgb(11, 87, 208); text-decoration: non=
e; }

.gb_H .gb_Ia { color: rgb(168, 199, 250); }

.gb_H .gb_Ia:hover { color: rgb(211, 227, 253); }

.gb_H .gb_Ia:focus, .gb_H .gb_Ia:active { color: rgb(236, 243, 254); }

.gb_H .gb_Ia:focus-visible { border-color: rgb(168, 199, 250); color: rgb(1=
68, 199, 250); outline: none; }

.gb_Ja { box-shadow: rgba(60, 64, 67, 0.3) 0px -1px 2px 0px, rgba(60, 64, 6=
7, 0.15) 0px -2px 6px 2px; height: calc(100% - 16px); left: 0px; margin: 8p=
x; position: absolute; top: 0px; width: calc(100% - 16px); }

.gb_Ka.gb_Ja { border-radius: 28px; box-shadow: rgba(0, 0, 0, 0.15) 0px 2px=
 6px 2px, rgba(0, 0, 0, 0.3) 0px 1px 2px 0px; height: 290px; }

@media only screen and (max-width: 452px) {
  .gb_Ka.gb_Ja { border-radius: 0px; height: 100%; margin: 0px; max-width: =
unset; padding: 0px; width: 100%; }
}

@-webkit-keyframes focus-animation-2px {=20
  0% { outline-color: transparent; outline-offset: 0px; outline-width: 0px;=
 }
  100% { outline-offset: 2px; outline-width: 1px; }
}

.gb_Ha a.gb_Va::before { content: " "; position: absolute; top: 0px; left: =
0px; width: 100%; height: 100%; opacity: 0; border-radius: 100px; backgroun=
d: var(--gm3-sys-color-on-primary,#fff); transition: opacity 0.5s ease-out;=
 }

.gb_Ha a.gb_Va:hover { cursor: pointer; box-shadow: rgba(0, 0, 0, 0.3) 0px =
1px 2px 0px, rgba(0, 0, 0, 0.15) 0px 1px 3px 1px; }

.gb_Ha a.gb_Va:hover::before { opacity: 0.08; }

.gb_Ha a.gb_Va:active, .gb_Ha a.gb_Va:active:focus { box-shadow: none; }

.gb_Ha a.gb_Va:active::before, .gb_Ha a.gb_Va:active:focus::before { opacit=
y: 0.12; }

.gb_Ha a.gb_Va:focus-visible { box-shadow: none; }

.gb_Ha a.gb_Va:focus-visible::before { opacity: 0.12; }

.gb_Ha a.gb_Va:focus-visible { outline-style: solid; outline-color: var(--g=
m3-sys-color-primary,#0b57d0); animation: 0.3s ease-in-out 0s 1 normal forw=
ards running focus-animation-2px; }

@media (forced-colors: active) {
  .gb_Ha a.gb_Va { border-width: 1px; border-style: solid; border-image: in=
itial; border-color: var(--gm3-sys-color-outline,#747775); }
  .gb_Ha a.gb_Va:focus-visible { outline: transparent solid 2px; }
}

@keyframes focus-animation-2px {=20
  0% { outline-color: transparent; outline-offset: 0px; outline-width: 0px;=
 }
  100% { outline-offset: 2px; outline-width: 1px; }
}

.gb_Ha a.gb_Wa::before { content: " "; position: absolute; top: 0px; left: =
0px; width: 100%; height: 100%; opacity: 0; border-radius: 100px; backgroun=
d: var(--gm3-sys-color-primary,#0b57d0); transition: opacity 0.5s ease-out;=
 }

.gb_Ha a.gb_Wa:hover { cursor: pointer; background: none; border-color: var=
(--gm3-sys-color-outline,#747775); }

.gb_Ha a.gb_Wa:hover::before { opacity: 0.08; }

.gb_Ha a.gb_Wa:active, .gb_Ha a.gb_Wa:active:focus { border-color: var(--gm=
3-sys-color-outline,#747775); }

.gb_Ha a.gb_Wa:active::before, .gb_Ha a.gb_Wa:active:focus::before { opacit=
y: 0.12; }

.gb_Ha a.gb_Wa:focus-visible { border-color: var(--gm3-sys-color-primary,#0=
b57d0); }

.gb_Ha a.gb_Wa:focus-visible::before { opacity: 0.12; }

@media (forced-colors: active) {
  .gb_Ha a.gb_Wa { border-width: 1px; border-style: solid; border-image: in=
itial; border-color: var(--gm3-sys-color-outline,#747775); }
  .gb_Ha a.gb_Wa:focus-visible { outline: transparent solid 2px; }
}

.gb_1a.gb_H a.gb_Va::before, .gb_2a.gb_H a.gb_Va::before, .gb_3a.gb_H a.gb_=
Va::before { background: var(--gm3-sys-color-on-secondary-fixed,#001d35); }

.gb_1a.gb_H a.gb_Va:focus-visible, .gb_2a.gb_H a.gb_Va:focus-visible, .gb_3=
a.gb_H a.gb_Va:focus-visible { outline-color: var(--gm3-sys-color-secondary=
-fixed,#c2e7ff); }

@media (forced-colors: active) {
  .gb_1a.gb_H a.gb_Va, .gb_2a.gb_H a.gb_Va, .gb_3a.gb_H a.gb_Va { border-co=
lor: var(--gm3-sys-color-outline,#8e918f); }
}

.gb_Ha.gb_H a.gb_Wa::before { background: var(--gm3-sys-color-primary,#a8c7=
fa); }

.gb_Ha.gb_H a.gb_Wa:focus-visible { background: none; border-color: var(--g=
m3-sys-color-primary,#a8c7fa); }

@media (forced-colors: active) {
  .gb_Ha.gb_H a.gb_Wa { border-color: var(--gm3-sys-color-outline,#8e918f);=
 }
}

@media (forced-colors: active) {
  .gb_Ha .gb_Ed:not(.gb_Md):focus { outline: transparent solid 2px; }
}

.gb_Ha { transition: box-shadow 0.25s; }

a.gb_Z:focus { outline-offset: 2px; }

a.gb_Z:hover { text-decoration: underline; }

.gb_Nd { transition: background-color 0.4s; }

.gb_vd { display: inline-block; vertical-align: middle; }

.gb_wd .gb_R { bottom: -3px; right: -5px; }

.gb_vd:first-child { padding-left: 0px; }

.gb_D { position: relative; }

.gb_B { display: inline-block; outline: none; vertical-align: middle; borde=
r-radius: 50%; box-sizing: border-box; height: 40px; width: 40px; }

.gb_B, #gb#gb a.gb_B { cursor: pointer; text-decoration: none; }

.gb_B, a.gb_B { color: rgb(0, 0, 0); }

.gb_ma { background: rgb(255, 255, 255); border: 1px solid rgba(0, 0, 0, 0.=
2); color: rgb(0, 0, 0); box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 10px; displ=
ay: none; outline: none; overflow: hidden; position: absolute; right: 0px; =
top: 54px; animation: 0.2s ease 0s 1 normal none running gb__a; border-radi=
us: 2px; user-select: text; }

.gb_vd.gb_5a .gb_ma, .gb_5a.gb_ma { display: block; }

.gb_Ad { position: absolute; right: 0px; top: 54px; z-index: -1; }

.gb_pb .gb_ma { margin-top: -10px; }

.gb_Ha .gb_Ed:not(.gb_Ra):focus img { background-color: rgba(0, 0, 0, 0.2);=
 outline: none; border-radius: 50%; }

.gb_B::before, .gb_Fd button::before { background: var(--gm3-sys-color-on-s=
urface-variant,#444746); border-radius: 100px; content: " "; height: 100%; =
left: 0px; opacity: 0; position: absolute; top: 0px; transition: opacity 0.=
3s ease-out; width: 100%; }

.gb_Fd button::before { height: 40px; left: 8px; top: 4px; width: 40px; }

.gb_Ha.gb_H .gb_B::before, .gb_Ha.gb_H .gb_Fd button::before { background: =
var(--gm3-sys-color-on-surface-variant,#c4c7c5); }

.gb_Fd button:focus:not(:focus-visible) svg, .gb_Fd button:hover svg, .gb_F=
d button:active svg, .gb_B:focus:not(:focus-visible), .gb_B:hover, .gb_B:ac=
tive, .gb_B[aria-expanded=3D"true"] { outline: none; }

.gb_Fd button:focus-visible svg, .gb_B:focus-visible { outline-style: solid=
; outline-width: 1px; outline-offset: 0px; outline-color: var(--gm3-sys-col=
or-primary,#0b57d0); }

.gb_Ha.gb_H .gb_Fd button:focus-visible svg, .gb_Ha.gb_H .gb_B:focus-visibl=
e { outline-color: var(--gm3-sys-color-primary,#a8c7fa); }

@media (forced-colors: active) {
  .gb_Fd button:focus-visible svg { outline: currentcolor solid 1px; }
}

.gb_Fd button:focus::before, .gb_Fd button:focus:hover::before, .gb_B:focus=
::before, .gb_B:focus:hover::before { opacity: 0.12; }

.gb_Fd button:active::before, .gb_B:active::before { opacity: 0.16; }

.gb_B:hover::before, .gb_Fd button:hover::before { opacity: 0.08; }

.gb_Xa .gb_B.gb_0a:hover::before { opacity: 0; }

.gb_B[aria-expanded=3D"true"]::before, .gb_B:hover[aria-expanded=3D"true"]:=
:before { opacity: 0.16; }

.gb_B::after { content: ""; position: absolute; inset: -4px; }

@media only screen and (max-width: 732px) {
  .gb_Fd button::before { right: 1px; top: 3px; left: auto; }
}

sentinel { }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: https://ssl.gstatic.com/colaboratory-static/common/b8629101fed591b8cb8c96c45ee6f083/v2/external/bundle.css

@charset "utf-8";

colab-cell-pair-slide, colab-cell-slide { --colab-chrome-font-size: 18px; -=
-colab-code-font-size: var(--colab-chrome-font-size); --colab-run-button-po=
sition: static; }

colab-cell-pair-slide .toolbar, colab-cell-slide .toolbar { height: 40px; }

colab-cell-pair-slide .cell, colab-cell-slide .cell { margin: 4px; }

colab-cell-pair-slide .code.cell, colab-cell-slide .code.cell { margin-left=
: 44px; }

colab-cell-pair-slide .mirror-cell div.inputarea, colab-cell-slide .mirror-=
cell div.inputarea { overflow: visible; padding-left: 0px; }

colab-cell-pair-slide .slide, colab-cell-slide .slide { display: flex; -web=
kit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: co=
lumn; height: 100%; }

colab-cell-pair-slide .content, colab-cell-slide .content { -webkit-box-fle=
x: 1; flex: 1 1 0%; height: calc(100% - 56px); display: flex; -webkit-box-a=
lign: center; align-items: center; }

colab-cell-pair-slide colab-scroller, colab-cell-slide colab-scroller { min=
-height: 0px; max-height: 100%; overflow: auto; padding: 0px 4px 4px 0px; }

colab-cell-pair-slide .toolbar-root, colab-cell-slide .toolbar-root { heigh=
t: fit-content; position: sticky; top: 0px; width: 100%; z-index: 1; }

colab-cell-pair-slide .markdown, colab-cell-slide .markdown { font-size: va=
r(--colab-chrome-font-size); }

colab-cell-pair-slide .markdown h1, colab-cell-slide .markdown h1 { font-si=
ze: 44px; }

colab-cell-pair-slide .markdown h2, colab-cell-slide .markdown h2 { font-si=
ze: 40px; }

colab-cell-pair-slide .markdown h3, colab-cell-slide .markdown h3 { font-si=
ze: 36px; }

colab-cell-pair-slide .markdown h4, colab-cell-slide .markdown h4 { font-si=
ze: 32px; }

colab-cell-pair-slide .markdown h5, colab-cell-slide .markdown h5 { font-si=
ze: 28px; }

colab-cell-pair-slide .markdown h6, colab-cell-slide .markdown h6 { font-si=
ze: 24px; }

colab-cell-pair-slide .markdown ol, colab-cell-pair-slide .markdown p, cola=
b-cell-pair-slide .markdown span table, colab-cell-pair-slide .markdown spa=
n td, colab-cell-pair-slide .markdown span th, colab-cell-pair-slide .markd=
own span tr, colab-cell-pair-slide .markdown ul, colab-cell-slide .markdown=
 ol, colab-cell-slide .markdown p, colab-cell-slide .markdown span table, c=
olab-cell-slide .markdown span td, colab-cell-slide .markdown span th, cola=
b-cell-slide .markdown span tr, colab-cell-slide .markdown ul { font-size: =
var(--colab-chrome-font-size); }

.slideshow-settings-content md-filled-select { padding: 12px 0px; }

.goog-modalpopup, .modal-dialog { box-shadow: rgba(0, 0, 0, 0.2) 0px 4px 16=
px; background: padding-box rgb(255, 255, 255); border: 1px solid rgba(0, 0=
, 0, 0.333); outline: 0px; position: absolute; }

.goog-modalpopup-bg, .modal-dialog-bg { background: rgb(255, 255, 255); lef=
t: 0px; position: absolute; top: 0px; }

div.goog-modalpopup-bg, div.modal-dialog-bg { opacity: 0.75; }

.modal-dialog { color: rgb(0, 0, 0); padding: 30px 42px; }

.modal-dialog-title { background-color: rgb(255, 255, 255); color: rgb(0, 0=
, 0); cursor: default; font-size: 16px; font-weight: 400; line-height: 24px=
; margin: 0px 0px 16px; }

.modal-dialog-title-close { height: 11px; opacity: 0.7; padding: 17px; posi=
tion: absolute; right: 0px; top: 0px; width: 11px; }

.modal-dialog-title-close::after { content: ""; background: url("https://ss=
l.gstatic.com/ui/v1/dialog/close-x.png"); position: absolute; height: 11px;=
 width: 11px; right: 17px; }

.modal-dialog-title-close:hover { opacity: 1; }

.modal-dialog-content { background-color: rgb(255, 255, 255); line-height: =
1.4em; overflow-wrap: break-word; }

.modal-dialog-buttons { margin-top: 16px; }

.modal-dialog-buttons button { border-radius: 2px; background-color: rgb(24=
5, 245, 245); background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, fr=
om(rgb(245, 245, 245)), to(rgb(241, 241, 241))); border: 1px solid rgba(0, =
0, 0, 0.1); color: rgb(68, 68, 68); cursor: default; font-family: inherit; =
font-size: 11px; font-weight: 700; height: 29px; line-height: 27px; margin:=
 0px 16px 0px 0px; min-width: 72px; outline: 0px; padding: 0px 8px; }

.modal-dialog-buttons button:active, .modal-dialog-buttons button:hover { b=
ox-shadow: rgba(0, 0, 0, 0.1) 0px 1px 1px; background-color: rgb(248, 248, =
248); background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(rgb(2=
48, 248, 248)), to(rgb(241, 241, 241))); border: 1px solid rgb(198, 198, 19=
8); color: rgb(51, 51, 51); }

.modal-dialog-buttons button:active { box-shadow: rgba(0, 0, 0, 0.1) 0px 1p=
x 2px inset; }

.modal-dialog-buttons button:focus { border: 1px solid rgb(77, 144, 254); }

.modal-dialog-buttons button[disabled] { box-shadow: none; background: none=
 rgb(255, 255, 255); border: 1px solid rgba(0, 0, 0, 0.05); color: rgb(184,=
 184, 184); }

.modal-dialog-buttons .goog-buttonset-action { background-color: rgb(77, 14=
4, 254); background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(rg=
b(77, 144, 254)), to(rgb(71, 135, 237))); border: 1px solid rgb(48, 121, 23=
7); color: rgb(255, 255, 255); }

.modal-dialog-buttons .goog-buttonset-action:active, .modal-dialog-buttons =
.goog-buttonset-action:hover { background-color: rgb(53, 122, 232); backgro=
und-image: linear-gradient(rgb(77, 144, 254), rgb(53, 122, 232)); border: 1=
px solid rgb(47, 91, 183); color: rgb(255, 255, 255); }

.modal-dialog-buttons .goog-buttonset-action:active { box-shadow: rgba(0, 0=
, 0, 0.3) 0px 1px 2px inset; }

.modal-dialog-buttons .goog-buttonset-action:focus { box-shadow: rgb(255, 2=
55, 255) 0px 0px 0px 1px inset; border: 1px solid transparent; outline: tra=
nsparent 0px; }

.modal-dialog-buttons .goog-buttonset-action[disabled] { box-shadow: none; =
background: rgb(77, 144, 254); color: rgb(255, 255, 255); opacity: 0.5; }

.jfk-alert, .jfk-confirm, .jfk-prompt { width: 512px; }

.share-client-dialog { overflow: auto; box-sizing: border-box; max-height: =
100% !important; width: auto !important; }

.share-client-dialog:focus { outline: 0px; }

* html .share-client-dialog { max-height: none !important; overflow: visibl=
e !important; }

:first-child + html .share-client-dialog { max-height: none !important; ove=
rflow: visible !important; }

.share-client-dialog .modal-dialog-content, .share-client-dialog .modal-dia=
log-title { padding: 0px; }

.share-client-dialog .share-client-dialog-hidden-title { height: 0px; margi=
n: 0px; padding: 0px; }

.share-client-dialog .modal-dialog-title { font-family: arial, sans-serif; =
font-weight: 400; }

.share-client-content-iframe { display: flex; height: 100%; width: 100%; bo=
rder: none; }

.share-client-dialog .modal-dialog-buttons { display: none; }

.share-client-error-dialog { font-family: arial, sans-serif; font-size: 12p=
x; width: 400px; z-index: 3000; }

.share-client-loading-contents { height: 99px; text-align: center; width: 4=
54px; }

.share-client-spinner { background-image: url("https://ssl.gstatic.com/docs=
/documents/share/images/spinner-2.gif"); background-size: 24px; display: in=
line-block; margin-top: 24px; width: 24px; height: 24px; }

.inline-share-ui-status { font-size: 12pt; font-weight: 700; height: 19px; =
padding: 5px 10px; background-color: rgb(241, 244, 255); }

.inline-share-ui-overlay { position: absolute; z-index: 150; background-col=
or: rgb(255, 255, 255); opacity: 0; }

.share-client-panel-dialog-share { height: 100%; width: 100%; }

.share-client-panel-dialog-overlay { position: absolute; z-index: 150; }

.share-client-offscreen { position: absolute !important; left: -10000px !im=
portant; top: -10000px !important; }

.share-client-loading-dialog { font-family: arial, sans-serif; z-index: 300=
0; }

.share-client-loading-dialog:focus { outline: 0px; }

.modeElementsDark .share-client-loading-dialog .modal-dialog-title { color:=
 rgb(227, 227, 227); }

.share-client-debug { display: none; position: absolute; bottom: 0px; right=
: 0px; color: rgb(119, 119, 119); font-size: 10px; }

.team-drive-share-client-dialog { border: none; border-radius: 2px; box-sha=
dow: rgba(0, 0, 0, 0.14) 0px 24px 38px 3px, rgba(0, 0, 0, 0.12) 0px 9px 46p=
x 8px, rgba(0, 0, 0, 0.2) 0px 11px 15px -7px; padding: 0px; }

.full-screen-share-client-dialog { height: 100vh; overflow: hidden; backgro=
und-color: transparent !important; border: none !important; padding: 0px !i=
mportant; width: 100vw !important; }

.full-screen-share-client-dialog .modal-dialog-content { background: transp=
arent; height: 100%; width: 100%; }

.modal-dialog.share-client-dialog.team-drive-share-client-dialog { padding:=
 0px; }

.full-screen-share-client-dialog .modal-dialog-title, .team-drive-share-cli=
ent-dialog .modal-dialog-title { display: none; }

.google-visualization-table { box-sizing: border-box; display: inline-block=
; vertical-align: bottom; }

.google-visualization-table * { box-sizing: inherit; }

.google-visualization-table > div:first-child { border: 0px solid rgb(238, =
238, 238); }

.google-visualization-table > div:first-child.scrolling .google-visualizati=
on-table-table .frozen-column, .google-visualization-table > div:first-chil=
d.scrolling .google-visualization-table-table th { visibility: hidden; opac=
ity: 0; color: transparent; }

.google-visualization-table > div:first-child.doneScrolling .google-visuali=
zation-table-table th { transition: opacity 0.25s ease-in 0.1s; }

.google-visualization-table > div:first-child.doneScrolling .google-visuali=
zation-table-table .frozen-column { transition: visibility, opacity 0.15s e=
ase-in 0.15s; }

.google-visualization-table-table { font-family: arial, helvetica; font-siz=
e: 10pt; cursor: default; margin: 0px; background: rgb(255, 255, 255); bord=
er-spacing: 0px; border-collapse: separate; }

.google-visualization-table-table * { margin: 0px; }

.google-visualization-table .gradient { background-image: linear-gradient(r=
gba(255, 255, 255, 0.8) 0px, rgba(255, 255, 255, 0.7) 30%, rgba(255, 255, 2=
55, 0.5) 60%, rgba(255, 255, 255, 0)); }

.google-visualization-table-tr-head { background-color: rgb(228, 233, 244);=
 font-weight: 700; text-align: center; }

.google-visualization-table-sorthdr { cursor: pointer; }

.google-visualization-table-sortind { color: rgb(204, 204, 204); padding-le=
ft: 4px; }

.unsorted .google-visualization-table-sortind { display: none; }

.unsorted .google-visualization-table-sortind::after { content: "=E2=80=83"=
; }

.sort-ascending .google-visualization-table-sortind::after { content: "=E2=
=96=B2"; }

.sort-descending .google-visualization-table-sortind::after { content: "=E2=
=96=BC"; }

.google-visualization-table-th { cursor: pointer; white-space: nowrap; }

.google-visualization-table-td { overflow: hidden; }

.google-visualization-table-td, .google-visualization-table-th { padding: 2=
px 0.35em; background-color: inherit; background-clip: padding-box; }

.google-visualization-table-table td, .google-visualization-table-table th =
{ border-style: solid; border-color: rgb(238, 238, 238); border-image: init=
ial; border-width: 0px 1px 1px 0px; padding: 2px 0.35em; }

.google-visualization-table-table th { position: relative; z-index: 10; }

.google-visualization-table-table td.frozen-column { position: relative; z-=
index: 5; }

.google-visualization-table-table thead th.frozen-column { z-index: 15; }

.google-visualization-table-table .last-frozen-column { border-right: 2px r=
idge rgb(238, 238, 238); }

.google-visualization-table-tr-even { background-color: rgb(255, 255, 255);=
 }

.google-visualization-table-tr-odd { background-color: rgb(250, 250, 250); =
}

.google-visualization-table-tr-sel { background-color: rgb(214, 233, 248); =
}

.google-visualization-table-tr-over { background-color: rgb(231, 233, 249);=
 }

.google-visualization-table-td.google-visualization-table-type-bool { text-=
align: center; font-family: "Arial Unicode MS", Arial, Helvetica; }

.google-visualization-table-td.google-visualization-table-type-date { text-=
align: center; }

.google-visualization-table-td.google-visualization-table-type-number { tex=
t-align: right; white-space: nowrap; }

.google-visualization-table-seq { text-align: right; color: rgb(102, 102, 1=
02); }

.google-visualization-table-div-page { display: inline-block; width: 100%; =
padding: 1px 0px 0px 1px; border: 0px; background-color: rgb(228, 233, 244)=
; font-family: Arial, sans-serif; }

.google-visualization-table-div-page [role=3D"button"] { display: inline-bl=
ock; cursor: pointer; margin-top: 2px; margin-bottom: 2px; font-family: "Ar=
ial Unicode MS", Arial, Helvetica; font-size: 10px; line-height: 10px; }

.google-visualization-table-div-page [role=3D"button"] .goog-custom-button-=
inner-box { padding: 1px 1px 2px; }

.google-visualization-table-page-prev::before { content: "=E2=97=84"; }

.google-visualization-table-page-next::before { content: "=E2=96=BA"; }

.google-visualization-table-page-numbers { display: inline-block; zoom: 1; =
margin: 0px; vertical-align: middle; }

.ie8 .google-visualization-table-page-numbers { display: inline; }

.google-visualization-table-page-number { display: inline-block; background=
-color: rgb(228, 233, 244); border: 1px outset buttonshadow; border-radius:=
 3px; color: rgb(0, 0, 0); font-size: 10px; min-width: 10px; margin: 2px; p=
adding: 0px 2px; text-align: center; text-decoration: none; vertical-align:=
 middle; }

.google-visualization-table-page-number.current { font-weight: 700; font-si=
ze: 11px; background: rgb(254, 254, 254); border-style: inset; }

.google-visualization-table-page-number:hover { background: rgb(254, 254, 2=
54); border-style: inset; }

.google-visualization-table .transparent { background-image: none; backgrou=
nd-color: transparent; border-color: transparent; }

.google-visualization-table .transparentIE6 { background: none; }

.google-visualization-table td .transparent, .google-visualization-table th=
 .transparent { color: transparent; opacity: 0; }

.google-visualization-table .google-visualization-hidden { visibility: hidd=
en; pointer-events: none; }

.google-visualization-table-loadtest { padding-left: 6px; }

.peopleKitStyleGm3 { --pkw-background: var(--gm3-sys-color-background,#fff)=
; --pkw-outline: var(--gm3-sys-color-outline,#747775); --pkw-outline-varian=
t: var(--gm3-sys-color-outline-variant,#c4c7c5); --pkw-scrim: rgba(0,0,0,.3=
2); --pkw-primary: var(--gm3-sys-color-primary,#0b57d0); --pkw-secondary-co=
ntainer: var(--gm3-sys-color-secondary-container,#c2e7ff); --pkw-on-seconda=
ry-container: var(--gm3-sys-color-on-secondary-container,#001d35); --pkw-er=
ror: var(--gm3-sys-color-error,#b3261e); --pkw-on-error: var(--gm3-sys-colo=
r-on-error,#fff); --pkw-error-container: var(--gm3-sys-color-error-containe=
r,#f9dedc); --pkw-error-container-low: #ffedea; --pkw-on-error-container: v=
ar(--gm3-sys-color-on-error-container,#410e0b); --pkw-caution: #7d5800; --p=
kw-caution-container: #ffdea9; --pkw-caution-container-low: #ffefd4; --pkw-=
on-caution-container: #271900; --pkw-on-surface: var(--gm3-sys-color-on-sur=
face,#1f1f1f); --pkw-on-surface-variant: var(--gm3-sys-color-on-surface-var=
iant,#444746); --pkw-surface-container: var(--gm3-sys-color-surface-contain=
er,#f0f4f9); --pkw-surface-container-high: var(--gm3-sys-color-surface-cont=
ainer-high,#e9eef6); --pkw-inverse-surface: var(--gm3-sys-color-inverse-sur=
face,#303030); --pkw-inverse-on-surface: var(--gm3-sys-color-inverse-on-sur=
face,#f2f2f2); }

.peoplekitThemeDark .peopleKitStyleGm3 { --pkw-background: var(--gm3-sys-co=
lor-background,#131314); --pkw-outline: var(--gm3-sys-color-outline,#8e918f=
); --pkw-outline-variant: var(--gm3-sys-color-outline-variant,#444746); --p=
kw-scrim: rgba(0,0,0,.32); --pkw-primary: var(--gm3-sys-color-primary,#a8c7=
fa); --pkw-secondary-container: var(--gm3-sys-color-secondary-container,#00=
4a77); --pkw-on-secondary-container: var(--gm3-sys-color-on-secondary-conta=
iner,#c2e7ff); --pkw-error: var(--gm3-sys-color-error,#f2b8b5); --pkw-on-er=
ror: var(--gm3-sys-color-on-error,#601410); --pkw-error-container: var(--gm=
3-sys-color-error-container,#8c1d18); --pkw-error-container-low: #410001; -=
-pkw-on-error-container: var(--gm3-sys-color-on-error-container,#f9dedc); -=
-pkw-caution: #ffba28; --pkw-caution-container: #5e4100; --pkw-caution-cont=
ainer-low: #503700; --pkw-on-caution-container: #ffdea9; --pkw-on-surface: =
var(--gm3-sys-color-on-surface,#e3e3e3); --pkw-on-surface-variant: var(--gm=
3-sys-color-on-surface-variant,#c4c7c5); --pkw-surface-container: var(--gm3=
-sys-color-surface-container,#1e1f20); --pkw-surface-container-high: var(--=
gm3-sys-color-surface-container-high,#282a2c); --pkw-inverse-surface: var(-=
-gm3-sys-color-inverse-surface,#e3e3e3); --pkw-inverse-on-surface: var(--gm=
3-sys-color-inverse-on-surface,#303030); }

.peoplekitComponentsAvatarImplAvatarContainer { position: relative; }

.peoplekitComponentsAvatarImplAvatar { border-radius: 50%; outline: transpa=
rent solid 1px; overflow: hidden; }

.peoplekitComponentsAvatarImplBadgeIconImage { margin: auto; display: block=
; height: 100%; width: 100%; }

.peoplekitComponentsAvatarImplAvatarBadge { position: absolute; bottom: 0px=
; right: 0px; display: none; height: 30%; width: 30%; min-height: 30%; min-=
width: 30%; object-fit: cover; overflow: hidden; }

.peoplekitComponentsAvatarImplAvatarBadge.visible { display: inline; }

.isSelected .peoplekitComponentsAvatarImplAvatarBadge { display: none; }

.peoplekitComponentsAvatarImplContainer { display: flex; -webkit-box-orient=
: horizontal; -webkit-box-direction: normal; flex-direction: row; height: i=
nherit; width: inherit; }

.peoplekitComponentsAvatarImplColumn { display: flex; -webkit-box-orient: v=
ertical; -webkit-box-direction: normal; flex-direction: column; -webkit-box=
-flex: 1; flex: 1 1 0%; overflow: hidden; height: inherit; -webkit-box-alig=
n: stretch; align-items: stretch; }

.peoplekitComponentsAvatarImplRow { display: flex; -webkit-box-flex: 1; fle=
x: 1 1 0%; overflow: hidden; }

.peoplekitComponentsAvatarImplDivider { margin: 1px; }

.peoplekitComponentsAvatarImplImageRoot { display: flex; -webkit-box-orient=
: vertical; -webkit-box-direction: normal; flex-direction: column; -webkit-=
box-flex: 1; flex: 1 1 auto; -webkit-box-align: center; place-items: center=
; transition: background 50ms ease-in-out; }

.peoplekitComponentsAvatarImplImageRoot.isLoading { background-clip: paddin=
g-box; background-color: var(--pkw-on-surface-variant,#bdc1c6); }

.peoplekitComponentsAvatarImplDefaultAvatarImage { display: none; }

.isNotLoaded .peoplekitComponentsAvatarImplDefaultAvatarImage { display: bl=
ock; fill: var(--pkw-on-surface-variant,#5f6368); }

.peoplekitThemeDark .isNotLoaded .peoplekitComponentsAvatarImplDefaultAvata=
rImage { fill: var(--pkw-on-surface-variant,#9aa0a6); }

.peoplekitComponentsAvatarImplImage { opacity: 1; display: block; transitio=
n: opacity 50ms ease-in-out; }

.isLoading .peoplekitComponentsAvatarImplImage { opacity: 0; }

.isNotLoaded .peoplekitComponentsAvatarImplImage { display: none; }

.peoplekitComponentsChipChip { background: var(--pkw-background,#fff); bord=
er-radius: 50vh; box-shadow: 0 0 0 1px var(--pkw-outline,#dadce0) inset; co=
lor: var(--pkw-on-surface-variant,#5f6368); cursor: pointer; display: inlin=
e-block; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-=
direction: column; -webkit-box-pack: center; justify-content: center; margi=
n: 4px; min-width: 1px; outline: transparent solid 1px; user-select: none; =
}

.peoplekitComponentsChipChip:hover { background: var(--pkw-background,#f8f9=
fa); color: var(--pkw-on-surface-variant,#202124); }

.peoplekitComponentsChipChip.isActive { background: var(--pkw-secondary-con=
tainer,#e8f0fe); box-shadow: none; color: var(--pkw-on-secondary-container,=
#1967d2); outline-width: 2px; }

.peoplekitComponentsChipChip.isActive:hover { background: var(--pkw-seconda=
ry-container,#d2e3fc); color: var(--pkw-on-secondary-container,#174ea6); }

.peoplekitComponentsChipChip.isSpotlit { box-shadow: 0 0 0 2px var(--pkw-pr=
imary,#669df6) inset; outline-width: 3px; }

.peoplekitComponentsChipChip.isWarning { background: var(--pkw-caution-cont=
ainer-low,#fef7e0); box-shadow: 0 0 0 1px var(--pkw-caution,#fbbc04) inset;=
 color: var(--pkw-caution,#5f6368); }

.peoplekitComponentsChipChip.isWarning.isActive { background: var(--pkw-cau=
tion-container,#fdd663); color: var(--pkw-on-caution-container,#3c4043); bo=
x-shadow: none; }

.peoplekitComponentsChipChip.isWarning.isActive:hover { background: var(--p=
kw-caution-container,#fcc934); color: var(--pkw-on-caution-container,#20212=
4); }

.peoplekitComponentsChipChip.isWarning.isSpotlit { box-shadow: 0 0 0 2px va=
r(--pkw-on-caution-container,#202124) inset; }

.peoplekitComponentsChipChip.isWarning:hover { background: var(--pkw-cautio=
n-container,#feefc3); color: var(--pkw-caution,#202124); }

.peoplekitComponentsChipChip.isError { background: var(--pkw-error-containe=
r-low,#fff); box-shadow: 0 0 0 1px var(--pkw-error,#ea4335) inset; color: v=
ar(--pkw-error,#c5221f); }

.peoplekitComponentsChipChip.isError.isActive { background: var(--pkw-error=
-container,rgba(217,48,37,.2)); color: var(--pkw-on-error-container,#a50e0e=
); box-shadow: none; }

.peoplekitComponentsChipChip.isError.isActive:hover { background: var(--pkw=
-error-container,rgba(217,48,37,.24)); color: var(--pkw-on-error-container,=
#a50e0e); }

.peoplekitComponentsChipChip.isError.isSpotlit { box-shadow: 0 0 0 2px var(=
--pkw-on-error-container,#a50e0e) inset; }

.peoplekitComponentsChipChip.isError:hover { background: var(--pkw-error-co=
ntainer,#fad2cf); color: var(--pkw-error,#a50e0e); }

.peoplekitComponentsChipChip.isDragged, .peoplekitComponentsChipChip.isDrag=
ged.isActive, .peoplekitComponentsChipChip.isDragged.isError, .peoplekitCom=
ponentsChipChip.isDragged.isSpotlit, .peoplekitComponentsChipChip.isDragged=
.isWarning { border-width: 0px; box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2=
px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px; }

.peoplekitComponentsChipChip.isDragged.isActive .mdc-elevation-overlay, .pe=
oplekitComponentsChipChip.isDragged.isError .mdc-elevation-overlay, .people=
kitComponentsChipChip.isDragged.isSpotlit .mdc-elevation-overlay, .peopleki=
tComponentsChipChip.isDragged.isWarning .mdc-elevation-overlay { opacity: 0=
; }

.peoplekitThemeDark .peoplekitComponentsChipChip.isDragged.isActive, .peopl=
ekitThemeDark .peoplekitComponentsChipChip.isDragged.isError, .peoplekitThe=
meDark .peoplekitComponentsChipChip.isDragged.isSpotlit, .peoplekitThemeDar=
k .peoplekitComponentsChipChip.isDragged.isWarning { border-width: 0px; box=
-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px =
2px 6px 2px; }

.peoplekitComponentsChipChip.isDragged .mdc-elevation-overlay, .peoplekitTh=
emeDark .peoplekitComponentsChipChip.isDragged.isActive .mdc-elevation-over=
lay, .peoplekitThemeDark .peoplekitComponentsChipChip.isDragged.isError .md=
c-elevation-overlay, .peoplekitThemeDark .peoplekitComponentsChipChip.isDra=
gged.isSpotlit .mdc-elevation-overlay, .peoplekitThemeDark .peoplekitCompon=
entsChipChip.isDragged.isWarning .mdc-elevation-overlay { opacity: 0; }

.peoplekitComponentsChipChip.isDragged.peopleKitStyleGm3 { box-shadow: rgba=
(0, 0, 0, 0.3) 0px 1px 3px 0px, rgba(0, 0, 0, 0.15) 0px 4px 8px 3px; }

.peoplekitComponentsChipChip.isDisabled, .peoplekitComponentsChipChip.isDis=
abled:hover { cursor: default; opacity: 0.5; }

.peoplekitComponentsChipChip.isDeletionDisabled .peoplekitComponentsChipDel=
eteButton { display: none; }

.peoplekitThemeDark .peoplekitComponentsChipChip { background: var(--pkw-ba=
ckground,linear-gradient(0deg,rgba(232,234,237,.08),rgba(232,234,237,.08)),=
#202124); border-radius: 50vh; box-shadow: 0 0 0 1px var(--pkw-outline,#5f6=
368) inset; color: var(--pkw-on-surface-variant,#9aa0a6); cursor: pointer; =
display: inline-block; -webkit-box-orient: vertical; -webkit-box-direction:=
 normal; flex-direction: column; -webkit-box-pack: center; justify-content:=
 center; margin: 4px; min-width: 1px; outline: transparent solid 1px; user-=
select: none; }

.peoplekitThemeDark .peoplekitComponentsChipChip:hover { background: var(--=
pkw-background,linear-gradient(0deg,rgba(232,234,237,.04),rgba(232,234,237,=
.04)),linear-gradient(0deg,rgba(232,234,237,.08),rgba(232,234,237,.08)),#20=
2124); color: var(--pkw-on-surface-variant,#e8eaed); }

.peoplekitThemeDark .peoplekitComponentsChipChip.isActive { background: var=
(--pkw-secondary-container,linear-gradient(0deg,rgba(138,180,248,.24),rgba(=
138,180,248,.24)),linear-gradient(0deg,rgba(232,234,237,.08),rgba(232,234,2=
37,.08)),#202124); box-shadow: none; color: var(--pkw-on-secondary-containe=
r,#d2e3fc); outline-width: 2px; }

.peoplekitThemeDark .peoplekitComponentsChipChip.isActive:hover { backgroun=
d: var(--pkw-secondary-container,linear-gradient(0deg,rgba(138,180,248,.32)=
,rgba(138,180,248,.32)),linear-gradient(0deg,rgba(232,234,237,.08),rgba(232=
,234,237,.08)),#202124); color: var(--pkw-on-secondary-container,#fff); }

.peoplekitThemeDark .peoplekitComponentsChipChip.isSpotlit { box-shadow: 0 =
0 0 2px var(--pkw-primary,#aecbfa) inset; outline-width: 3px; }

.peoplekitThemeDark .peoplekitComponentsChipChip.isWarning { background: va=
r(--pkw-caution-container-low,linear-gradient(0deg,rgba(232,234,237,.08),rg=
ba(232,234,237,.08)),#202124); box-shadow: 0 0 0 1px var(--pkw-caution,#fdd=
663) inset; color: var(--pkw-caution,#fdd663); }

.peoplekitThemeDark .peoplekitComponentsChipChip.isWarning.isActive { backg=
round: var(--pkw-caution-container,linear-gradient(0deg,rgba(253,214,99,.24=
),rgba(253,214,99,.24)),linear-gradient(0deg,rgba(232,234,237,.08),rgba(232=
,234,237,.08)),#202124); color: var(--pkw-on-caution-container,#feefc3); bo=
x-shadow: none; }

.peoplekitThemeDark .peoplekitComponentsChipChip.isWarning.isActive:hover {=
 background: var(--pkw-caution-container,linear-gradient(0deg,rgba(253,214,=
99,.36),rgba(253,214,99,.36)),linear-gradient(0deg,rgba(232,234,237,.08),rg=
ba(232,234,237,.08)),#202124); color: var(--pkw-on-caution-container,#fff);=
 }

.peoplekitThemeDark .peoplekitComponentsChipChip.isWarning.isSpotlit { box-=
shadow: 0 0 0 2px var(--pkw-on-caution-container,#e8eaed) inset; }

.peoplekitThemeDark .peoplekitComponentsChipChip.isWarning:hover { backgrou=
nd: var(--pkw-caution-container,linear-gradient(0deg,rgba(253,214,99,.04),r=
gba(253,214,99,.04)),linear-gradient(0deg,rgba(232,234,237,.08),rgba(232,23=
4,237,.08)),#202124); color: var(--pkw-caution,#feefc3); }

.peoplekitThemeDark .peoplekitComponentsChipChip.isError { background: var(=
--pkw-error-container-low,linear-gradient(0deg,rgba(232,234,237,.08),rgba(2=
32,234,237,.08)),#202124); box-shadow: 0 0 0 1px var(--pkw-error,#f28b82) i=
nset; color: var(--pkw-error,#f28b82); }

.peoplekitThemeDark .peoplekitComponentsChipChip.isError.isActive { backgro=
und: var(--pkw-error-container,linear-gradient(0deg,hsla(5,81%,73%,.24),hsl=
a(5,81%,73%,.24)),linear-gradient(0deg,rgba(232,234,237,.08),rgba(232,234,2=
37,.08)),#202124); color: var(--pkw-on-error-container,#fad2cf); box-shadow=
: none; }

.peoplekitThemeDark .peoplekitComponentsChipChip.isError.isActive:hover { b=
ackground: var(--pkw-error-container,linear-gradient(0deg,hsla(5,81%,73%,.3=
6),hsla(5,81%,73%,.36)),linear-gradient(0deg,rgba(232,234,237,.08),rgba(232=
,234,237,.08)),#202124); color: var(--pkw-on-error-container,#fce8e6); }

.peoplekitThemeDark .peoplekitComponentsChipChip.isError.isSpotlit { box-sh=
adow: 0 0 0 2px var(--pkw-on-error-container,#fad2cf) inset; }

.peoplekitThemeDark .peoplekitComponentsChipChip.isError:hover { background=
: var(--pkw-error-container,linear-gradient(0deg,hsla(5,81%,73%,.04),hsla(5=
,81%,73%,.04)),linear-gradient(0deg,rgba(232,234,237,.08),rgba(232,234,237,=
.08)),#202124); color: var(--pkw-error,#fad2cf); }

.peoplekitThemeDark .peoplekitComponentsChipChip.isDragged, .peoplekitTheme=
Dark .peoplekitComponentsChipChip.isDragged.isActive, .peoplekitThemeDark .=
peoplekitComponentsChipChip.isDragged.isError, .peoplekitThemeDark .peoplek=
itComponentsChipChip.isDragged.isSpotlit, .peoplekitThemeDark .peoplekitCom=
ponentsChipChip.isDragged.isWarning { border-width: 0px; box-shadow: rgba(6=
0, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px; }

.peoplekitThemeDark .peoplekitComponentsChipChip.isDragged.isActive .mdc-el=
evation-overlay, .peoplekitThemeDark .peoplekitComponentsChipChip.isDragged=
.isError .mdc-elevation-overlay, .peoplekitThemeDark .peoplekitComponentsCh=
ipChip.isDragged.isSpotlit .mdc-elevation-overlay, .peoplekitThemeDark .peo=
plekitComponentsChipChip.isDragged.isWarning .mdc-elevation-overlay { opaci=
ty: 0; }

.peoplekitThemeDark .peoplekitThemeDark .peoplekitComponentsChipChip.isDrag=
ged.isActive, .peoplekitThemeDark .peoplekitThemeDark .peoplekitComponentsC=
hipChip.isDragged.isError, .peoplekitThemeDark .peoplekitThemeDark .peoplek=
itComponentsChipChip.isDragged.isSpotlit, .peoplekitThemeDark .peoplekitThe=
meDark .peoplekitComponentsChipChip.isDragged.isWarning { border-width: 0px=
; box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15)=
 0px 2px 6px 2px; }

.peoplekitThemeDark .peoplekitComponentsChipChip.isDragged .mdc-elevation-o=
verlay, .peoplekitThemeDark .peoplekitThemeDark .peoplekitComponentsChipChi=
p.isDragged.isActive .mdc-elevation-overlay, .peoplekitThemeDark .peoplekit=
ThemeDark .peoplekitComponentsChipChip.isDragged.isError .mdc-elevation-ove=
rlay, .peoplekitThemeDark .peoplekitThemeDark .peoplekitComponentsChipChip.=
isDragged.isSpotlit .mdc-elevation-overlay, .peoplekitThemeDark .peoplekitT=
hemeDark .peoplekitComponentsChipChip.isDragged.isWarning .mdc-elevation-ov=
erlay { opacity: 0; }

.peoplekitThemeDark .peoplekitComponentsChipChip.isDragged.peopleKitStyleGm=
3 { box-shadow: rgba(0, 0, 0, 0.3) 0px 1px 3px 0px, rgba(0, 0, 0, 0.15) 0px=
 4px 8px 3px; }

.peoplekitThemeDark .peoplekitComponentsChipChip.isDisabled, .peoplekitThem=
eDark .peoplekitComponentsChipChip.isDisabled:hover { cursor: default; opac=
ity: 0.5; }

.peoplekitThemeDark .peoplekitComponentsChipChip.isDeletionDisabled .people=
kitComponentsChipDeleteButton { display: none; }

.peopleKitStyleGm3 .peoplekitComponentsChipChip { position: relative; }

.peopleKitStyleGm3 .peoplekitComponentsChipChip::before { background: var(-=
-pkw-on-surface-variant,var(--gm3-sys-color-on-surface-variant,#444746)); b=
order-radius: 50vh; content: ""; height: 100%; left: 0px; opacity: 0; posit=
ion: absolute; top: 0px; width: 100%; }

.peoplekitThemeDark .peopleKitStyleGm3 .peoplekitComponentsChipChip::before=
 { background: var(--pkw-on-surface-variant,var(--gm3-sys-color-on-surface-=
variant,#c4c7c5)); }

.peopleKitStyleGm3 .peoplekitComponentsChipChip:hover::before { opacity: 0.=
08; }

.peopleKitStyleGm3 .peoplekitComponentsChipChip.isActive:hover::before { op=
acity: 0.1; }

.peopleKitStyleGm3 .peoplekitComponentsChipChip.isWarning:hover::before { o=
pacity: 0.08; }

.peopleKitStyleGm3 .peoplekitComponentsChipChip.isWarning.isActive:hover::b=
efore { opacity: 0.1; }

.peopleKitStyleGm3 .peoplekitComponentsChipChip.isError:hover::before { opa=
city: 0.08; }

.peopleKitStyleGm3 .peoplekitComponentsChipChip.isError.isActive:hover::bef=
ore { opacity: 0.1; }

.peoplekitComponentsChipChipRow { -webkit-box-align: stretch; align-items: =
stretch; display: flex; -webkit-box-orient: horizontal; -webkit-box-directi=
on: normal; flex-flow: row; padding: 2px; }

.peoplekitComponentsChipLeft { -webkit-box-flex: initial; flex: initial; }

.peoplekitComponentsChipCenter { -webkit-box-align: stretch; place-items: s=
tretch; display: flex; -webkit-box-flex: 1; flex: 1 1 auto; overflow: hidde=
n; }

.peoplekitComponentsChipRight { -webkit-box-align: center; align-items: cen=
ter; display: flex; -webkit-box-flex: initial; flex: initial; }

.peoplekitComponentsChipLabelContainer { display: flex; -webkit-box-orient:=
 vertical; -webkit-box-direction: normal; flex-flow: column; -webkit-box-pa=
ck: center; justify-content: center; margin-left: 8px; margin-right: 8px; o=
verflow: hidden; }

.peoplekitComponentsChipLabelRow { -webkit-box-flex: initial; flex: initial=
; }

.peoplekitComponentsChipLabel { letter-spacing: 0.0214286em; font-family: R=
oboto, Arial, sans-serif; font-size: 0.875rem; font-weight: 500; line-heigh=
t: unset; max-width: 400px; overflow: hidden; text-overflow: ellipsis; whit=
e-space: nowrap; display: flex; }

.peopleKitStyleGm3 .peoplekitComponentsChipLabel { font-family: "Google San=
s Text", "Google Sans", Roboto, Arial, sans-serif; font-size: 0.875rem; fon=
t-weight: 500; letter-spacing: 0px; line-height: 1.25rem; }

.peoplekitComponentsChipDisambiguationLabel.hasDisambiguationLabel { margin=
-left: 4px; }

.peoplekitComponentsChipDisplayLabel { -webkit-box-flex: 1; flex: 1 0 auto;=
 overflow: hidden; text-overflow: ellipsis; max-width: 100%; }

.peoplekitComponentsChipDisambiguationLabel { overflow: hidden; text-overfl=
ow: ellipsis; }

.peoplekitComponentsChipAvatar { position: relative; }

.peoplekitComponentsChipAvatarContainer { height: inherit; width: inherit; =
position: relative; }

.peoplekitComponentsChipAvatarExclamationOverlay { border-radius: 50%; heig=
ht: 100%; left: 0px; outline: transparent solid 1px; position: absolute; to=
p: 0px; width: 100%; display: flex; -webkit-box-align: center; align-items:=
 center; -webkit-box-pack: center; justify-content: center; }

.peoplekitComponentsChipAvatarExclamationOverlay.isError { background-color=
: var(--pkw-error,#c5221f); }

.peoplekitThemeDark .peoplekitComponentsChipAvatarExclamationOverlay.isErro=
r { background-color: var(--pkw-error,#f28b82); }

.peoplekitComponentsChipExclamationIcon { display: inline-flex; height: 85%=
; width: 85%; }

.peoplekitComponentsChipExclamationIcon.isError { fill: var(--pkw-on-error,=
#fff); }

.peoplekitThemeDark .peoplekitComponentsChipExclamationIcon.isError { fill:=
 var(--pkw-on-error,#202124); }

@media (forced-colors: active) {
  .peoplekitComponentsChipExclamationIcon { filter: brightness(0); }
}

.peoplekitComponentsChipDeleteButton { -webkit-box-align: center; align-ite=
ms: center; display: flex; height: 100%; max-height: 24px; margin-left: -3p=
x; margin-right: 1px; width: 24px; z-index: 1; }

.peoplekitComponentsChipDeleteIcon { display: block; fill: currentcolor; ma=
rgin: 0px auto; }

.peoplekitComponentsChipPlaceholderAvatarPlaceholder { border-radius: 50%; =
background-color: var(--pkw-secondary-fixed-dim,#aecbfa); }

.peoplekitComponentsChipPlaceholderLabelPlaceholder { align-self: center; b=
ackground-color: var(--pkw-secondary-fixed-dim,#aecbfa); border-radius: 8px=
; height: 16px; margin-left: 8px; margin-right: 8px; width: 150px; }

.peoplekitComponentsChipPlaceholderShimmer { animation: 1.4s cubic-bezier(0=
.5, 0, 0.5, 1) 0s infinite normal none running fadeinout; }

@-webkit-keyframes fadeinout {=20
  0% { opacity: 0.75; }
  50% { opacity: 1; }
  100% { opacity: 0.75; }
}

@keyframes fadeinout {=20
  0% { opacity: 0.75; }
  50% { opacity: 1; }
  100% { opacity: 0.75; }
}

.peoplekitComponentsTooltipImplTooltip { font-family: Roboto, Arial, sans-s=
erif; font-size: 0.75rem; letter-spacing: 0.025em; background-color: var(--=
pkw-inverse-surface,#3c4043); color: var(--pkw-inverse-on-surface,#f1f3f4);=
 border-radius: 5px; box-sizing: border-box; font-weight: 700; line-height:=
 16px; min-width: 40px; max-width: 200px; min-height: 24px; max-height: 40v=
h; overflow: hidden; padding: 4px 8px; position: absolute; outline: transpa=
rent solid 1px; text-align: center; width: max-content; z-index: 9; }

.peoplekitThemeDark .peoplekitComponentsTooltipImplTooltip { background-col=
or: var(--pkw-inverse-surface,#3c4043); color: var(--pkw-inverse-on-surface=
,#e8eaed); }

.peopleKitStyleGm3 .peoplekitComponentsTooltipImplTooltip { font-family: "G=
oogle Sans Text", "Google Sans", Roboto, Arial, sans-serif; font-size: 0.75=
rem; font-weight: 400; letter-spacing: 0.00625rem; line-height: 1rem; borde=
r-radius: 4px; }

.peoplekitComponentsButtonIconIconButton { background: none; border: none; =
border-radius: 50%; cursor: pointer; }

.peoplekitComponentsButtonIconIconButton:hover { background-color: var(--pk=
w-background,#dadce0); }

.peoplekitComponentsButtonIconIconButton:active { background-color: var(--p=
kw-background,#bdc1c6); }

.peoplekitComponentsButtonIconIconButton.isFocused { background-color: var(=
--pkw-background,#dadce0); outline: transparent solid 3px; }

.peoplekitComponentsButtonIconIconButton.googleMaterialDefaultDensity { hei=
ght: 40px; padding: 8px; width: 40px; }

.peoplekitComponentsButtonIconIconButton.googleMaterialDefaultDensity .peop=
lekitComponentsButtonIconAdaptableIcon { height: 24px; width: 24px; }

.peoplekitComponentsButtonIconIconButton.workspaceMaterialComfortableDensit=
y { height: 32px; padding: 6px; width: 32px; }

.peoplekitComponentsButtonIconIconButton.workspaceMaterialComfortableDensit=
y .peoplekitComponentsButtonIconAdaptableIcon { height: 20px; width: 20px; =
}

.peoplekitComponentsButtonIconIconButton.workspaceMaterialCompactDensity { =
height: 28px; padding: 5px; width: 28px; }

.peoplekitComponentsButtonIconIconButton.workspaceMaterialCompactDensity .p=
eoplekitComponentsButtonIconAdaptableIcon { height: 18px; width: 18px; }

.peoplekitThemeDark .peoplekitComponentsButtonIconIconButton { background: =
none; border: none; border-radius: 50%; cursor: pointer; }

.peoplekitThemeDark .peoplekitComponentsButtonIconIconButton:hover { backgr=
ound-color: var(--pkw-background,#5f6368); }

.peoplekitThemeDark .peoplekitComponentsButtonIconIconButton:active { backg=
round-color: var(--pkw-background,#80868b); }

.peoplekitThemeDark .peoplekitComponentsButtonIconIconButton.isFocused { ba=
ckground-color: var(--pkw-background,#5f6368); outline: transparent solid 3=
px; }

.peoplekitThemeDark .peoplekitComponentsButtonIconIconButton.googleMaterial=
DefaultDensity { height: 40px; padding: 8px; width: 40px; }

.peoplekitThemeDark .peoplekitComponentsButtonIconIconButton.googleMaterial=
DefaultDensity .peoplekitComponentsButtonIconAdaptableIcon { height: 24px; =
width: 24px; }

.peoplekitThemeDark .peoplekitComponentsButtonIconIconButton.workspaceMater=
ialComfortableDensity { height: 32px; padding: 6px; width: 32px; }

.peoplekitThemeDark .peoplekitComponentsButtonIconIconButton.workspaceMater=
ialComfortableDensity .peoplekitComponentsButtonIconAdaptableIcon { height:=
 20px; width: 20px; }

.peoplekitThemeDark .peoplekitComponentsButtonIconIconButton.workspaceMater=
ialCompactDensity { height: 28px; padding: 5px; width: 28px; }

.peoplekitThemeDark .peoplekitComponentsButtonIconIconButton.workspaceMater=
ialCompactDensity .peoplekitComponentsButtonIconAdaptableIcon { height: 18p=
x; width: 18px; }

.peopleKitStyleGm3 .peoplekitComponentsButtonIconIconButton { position: rel=
ative; }

.peopleKitStyleGm3 .peoplekitComponentsButtonIconIconButton::before { backg=
round: var(--pkw-on-surface-variant,var(--gm3-sys-color-on-surface-variant,=
#444746)); border-radius: 50%; content: ""; height: 100%; left: 0px; opacit=
y: 0; position: absolute; top: 0px; width: 100%; }

.peoplekitThemeDark .peopleKitStyleGm3 .peoplekitComponentsButtonIconIconBu=
tton::before { background: var(--pkw-on-surface-variant,var(--gm3-sys-color=
-on-surface-variant,#c4c7c5)); }

.peopleKitStyleGm3 .peoplekitComponentsButtonIconIconButton:hover::before {=
 opacity: 0.16; }

.peopleKitStyleGm3 .peoplekitComponentsButtonIconIconButton:active::before =
{ opacity: 0.2; }

.peopleKitStyleGm3 .peoplekitComponentsButtonIconIconButton.isFocused::befo=
re { opacity: 0.2; }

@media (forced-colors: none) {
  .peopleKitStyleGm3 .peoplekitComponentsButtonIconAdaptableIcon { filter: =
brightness(0) saturate(100%) invert(25%) sepia(11%) saturate(129%) hue-rota=
te(109deg) brightness(93%) contrast(86%); }
  .peoplekitThemeDark .peopleKitStyleGm3 .peoplekitComponentsButtonIconAdap=
tableIcon { filter: brightness(0) saturate(100%) invert(88%) sepia(2%) satu=
rate(246%) hue-rotate(87deg) brightness(92%) contrast(88%); }
}

@media (forced-colors: active) and (prefers-color-scheme: dark) {
  .peoplekitComponentsButtonIconAdaptableIcon { filter: brightness(0) inver=
t(1); }
}

@media (forced-colors: active) and (prefers-color-scheme: light) {
  .peoplekitComponentsButtonIconAdaptableIcon { filter: brightness(0); }
}

.peoplekitComponentsResultlistitemResultListItem { background: var(--pkw-ba=
ckground,#fff); display: flex; -webkit-box-orient: vertical; -webkit-box-di=
rection: normal; flex-direction: column; -webkit-box-pack: center; justify-=
content: center; cursor: pointer; }

.peoplekitComponentsResultlistitemResultListItem:hover { background: var(--=
pkw-background,hsla(0,0%,4%,.04)); }

.peoplekitComponentsResultlistitemResultListItem:hover .peoplekitComponents=
ResultlistitemDisabledIconIndicator { background: var(--pkw-background,#f1f=
3f4); }

.peoplekitComponentsResultlistitemResultListItem.isActive { background: var=
(--pkw-background,hsla(0,0%,4%,.12)); outline: transparent solid 3px; outli=
ne-offset: -3px; }

.peoplekitComponentsResultlistitemResultListItem.isActive .peoplekitCompone=
ntsResultlistitemDisabledIconIndicator { background: var(--pkw-background,#=
f1f3f4); }

.peoplekitThemeDark .peoplekitComponentsResultlistitemResultListItem { back=
ground: var(--pkw-background,linear-gradient(0deg,rgba(232,234,237,.08),rgb=
a(232,234,237,.08)),#202124); display: flex; -webkit-box-orient: vertical; =
-webkit-box-direction: normal; flex-direction: column; -webkit-box-pack: ce=
nter; justify-content: center; cursor: pointer; }

.peoplekitThemeDark .peoplekitComponentsResultlistitemResultListItem:hover =
{ background: var(--pkw-background,linear-gradient(0deg,rgba(232,234,237,.1=
4),rgba(232,234,237,.14)),#202124); }

.peoplekitThemeDark .peoplekitComponentsResultlistitemResultListItem:hover =
.peoplekitComponentsResultlistitemDisabledIconIndicator { background: var(-=
-pkw-background,rgba(241,243,244,.14)); }

.peoplekitThemeDark .peoplekitComponentsResultlistitemResultListItem.isActi=
ve { background: var(--pkw-background,linear-gradient(0deg,rgba(232,234,237=
,.19),rgba(232,234,237,.19)),#202124); outline: transparent solid 3px; outl=
ine-offset: -3px; }

.peoplekitThemeDark .peoplekitComponentsResultlistitemResultListItem.isActi=
ve .peoplekitComponentsResultlistitemDisabledIconIndicator { background: va=
r(--pkw-background,rgba(241,243,244,.14)); }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemResultListItem { posit=
ion: relative; }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemResultListItem::before=
 { background: var(--pkw-on-surface-variant,var(--gm3-sys-color-on-surface-=
variant,#444746)); content: ""; height: 100%; left: 0px; opacity: 0; positi=
on: absolute; top: 0px; width: 100%; }

.peoplekitThemeDark .peopleKitStyleGm3 .peoplekitComponentsResultlistitemRe=
sultListItem::before { background: var(--pkw-on-surface-variant,var(--gm3-s=
ys-color-on-surface-variant,#c4c7c5)); }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemResultListItem:hover::=
before { opacity: 0.08; }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemResultListItem.isActiv=
e::before { opacity: 0.1; }

.peoplekitComponentsResultlistitemResultListItem.googleMaterialDefaultDensi=
ty { min-height: 64px; }

.peoplekitComponentsResultlistitemResultListItem.googleMaterialDefaultDensi=
ty .peoplekitComponentsResultlistitemLabel { font-family: Roboto, Arial, sa=
ns-serif; line-height: 1.5rem; font-size: 1rem; letter-spacing: 0.00625em; =
font-weight: 400; }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemResultListItem.googleM=
aterialDefaultDensity .peoplekitComponentsResultlistitemLabel { font-family=
: "Google Sans Text", "Google Sans", Roboto, Arial, sans-serif; line-height=
: 1.5rem; font-size: 1rem; letter-spacing: 0px; font-weight: 400; }

.peoplekitComponentsResultlistitemResultListItem.googleMaterialDefaultDensi=
ty .peoplekitComponentsResultlistitemSublabel { font-family: Roboto, Arial,=
 sans-serif; line-height: 1.25rem; font-size: 0.875rem; letter-spacing: 0.0=
142857em; font-weight: 400; }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemResultListItem.googleM=
aterialDefaultDensity .peoplekitComponentsResultlistitemSublabel { font-fam=
ily: "Google Sans Text", "Google Sans", Roboto, Arial, sans-serif; font-siz=
e: 0.875rem; font-weight: 400; letter-spacing: 0px; line-height: 1.25rem; }

.peoplekitComponentsResultlistitemResultListItem.googleMaterialDefaultDensi=
ty .peoplekitComponentsResultlistitemWhiteCheckSvg { width: 24px; height: 2=
4px; }

.peoplekitComponentsResultlistitemResultListItem.googleMaterialDefaultDensi=
ty .peoplekitComponentsResultlistitemMetaIcon { width: 25px; height: 25px; =
}

.peoplekitComponentsResultlistitemResultListItem.googleMaterialDefaultDensi=
ty .peoplekitComponentsResultlistitemResultListItemRow { padding: 8px 16px;=
 }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemResultListItem.googleM=
aterialDefaultDensity { min-height: 72px; }

.peoplekitComponentsResultlistitemResultListItem.workspaceMaterialComfortab=
leDensity { min-height: 52px; }

.peoplekitComponentsResultlistitemResultListItem.workspaceMaterialComfortab=
leDensity .peoplekitComponentsResultlistitemLabel { font-family: Roboto, Ar=
ial, sans-serif; font-size: 0.875rem; letter-spacing: 0.0142857em; font-wei=
ght: 400; line-height: 1.25rem; }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemResultListItem.workspa=
ceMaterialComfortableDensity .peoplekitComponentsResultlistitemLabel { font=
-family: "Google Sans Text", "Google Sans", Roboto, Arial, sans-serif; font=
-size: 0.875rem; font-weight: 400; letter-spacing: 0px; line-height: 1.25re=
m; }

.peoplekitComponentsResultlistitemResultListItem.workspaceMaterialComfortab=
leDensity .peoplekitComponentsResultlistitemSublabel { font-family: Roboto,=
 Arial, sans-serif; font-size: 0.75rem; letter-spacing: 0.025em; font-weigh=
t: 400; line-height: 1rem; }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemResultListItem.workspa=
ceMaterialComfortableDensity .peoplekitComponentsResultlistitemSublabel { f=
ont-family: "Google Sans Text", "Google Sans", Roboto, Arial, sans-serif; f=
ont-size: 0.75rem; font-weight: 400; letter-spacing: 0.00625rem; line-heigh=
t: 1rem; }

.peoplekitComponentsResultlistitemResultListItem.workspaceMaterialComfortab=
leDensity .peoplekitComponentsResultlistitemWhiteCheckSvg { width: 19px; he=
ight: 19px; }

.peoplekitComponentsResultlistitemResultListItem.workspaceMaterialComfortab=
leDensity .peoplekitComponentsResultlistitemMetaIcon { width: 20px; height:=
 20px; }

.peoplekitComponentsResultlistitemResultListItem.workspaceMaterialComfortab=
leDensity .peoplekitComponentsResultlistitemResultListItemRow { padding-lef=
t: 12px; padding-right: 12px; }

.peoplekitComponentsResultlistitemResultListItem.workspaceMaterialCompactDe=
nsity { min-height: 44px; }

.peoplekitComponentsResultlistitemResultListItem.workspaceMaterialCompactDe=
nsity .peoplekitComponentsResultlistitemLabel { font-family: Roboto, Arial,=
 sans-serif; font-size: 0.875rem; letter-spacing: 0.0142857em; font-weight:=
 400; line-height: 1.125; }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemResultListItem.workspa=
ceMaterialCompactDensity .peoplekitComponentsResultlistitemLabel { font-fam=
ily: "Google Sans Text", "Google Sans", Roboto, Arial, sans-serif; font-siz=
e: 0.875rem; font-weight: 400; letter-spacing: 0px; line-height: 1.25rem; }

.peoplekitComponentsResultlistitemResultListItem.workspaceMaterialCompactDe=
nsity .peoplekitComponentsResultlistitemSublabel { font-family: Roboto, Ari=
al, sans-serif; font-size: 0.75rem; letter-spacing: 0.025em; font-weight: 4=
00; line-height: 0.875rem; }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemResultListItem.workspa=
ceMaterialCompactDensity .peoplekitComponentsResultlistitemSublabel { font-=
family: "Google Sans Text", "Google Sans", Roboto, Arial, sans-serif; font-=
size: 0.75rem; font-weight: 400; letter-spacing: 0.00625rem; line-height: 1=
rem; }

.peoplekitComponentsResultlistitemResultListItem.workspaceMaterialCompactDe=
nsity .peoplekitComponentsResultlistitemWhiteCheckSvg { width: 17px; height=
: 17px; }

.peoplekitComponentsResultlistitemResultListItem.workspaceMaterialCompactDe=
nsity .peoplekitComponentsResultlistitemMetaIcon { width: 20px; height: 20p=
x; }

.peoplekitComponentsResultlistitemResultListItem.workspaceMaterialCompactDe=
nsity .peoplekitComponentsResultlistitemResultListItemRow { padding-left: 1=
2px; padding-right: 12px; }

.peoplekitComponentsResultlistitemResultListItem.isDisabled { cursor: defau=
lt; }

.peoplekitComponentsResultlistitemResultListItem.isDisabled .peoplekitCompo=
nentsResultlistitemLabel, .peoplekitComponentsResultlistitemResultListItem.=
isDisabled .peoplekitComponentsResultlistitemSublabelText { color: var(--pk=
w-on-surface,#3c4043); opacity: 0.38; }

.peoplekitThemeDark .peoplekitComponentsResultlistitemResultListItem.isDisa=
bled .peoplekitComponentsResultlistitemLabel, .peoplekitThemeDark .peopleki=
tComponentsResultlistitemResultListItem.isDisabled .peoplekitComponentsResu=
ltlistitemSublabelText { color: var(--pkw-on-surface,#e8eaed); }

.peoplekitComponentsResultlistitemResultListItem.isDisabled .peoplekitCompo=
nentsResultlistitemAvatar { opacity: 0.5; }

.peoplekitComponentsResultlistitemResultListItem.isSelected .peoplekitCompo=
nentsResultlistitemAvatarSelectionOverlay { opacity: 1; transform: scale(1)=
; }

.peoplekitComponentsResultlistitemResultListItem.isOutOfOffice { background=
-color: var(--pkw-caution-container-low,#ffefd5); }

.peoplekitComponentsResultlistitemResultListItemRow { -webkit-box-align: ce=
nter; align-items: center; display: flex; -webkit-box-orient: horizontal; -=
webkit-box-direction: normal; flex-flow: row; }

.peoplekitComponentsResultlistitemLeft { -webkit-box-flex: initial; flex: i=
nitial; }

.peoplekitComponentsResultlistitemCenter { -webkit-box-flex: 1; flex: 1 1 a=
uto; overflow: hidden; }

.peoplekitComponentsResultlistitemRight { display: inline-flex; -webkit-box=
-flex: initial; flex: initial; }

.peoplekitComponentsResultlistitemLabelContainer { align-content: flex-star=
t; -webkit-box-align: start; align-items: flex-start; display: flex; -webki=
t-box-orient: vertical; -webkit-box-direction: normal; flex-flow: column; m=
argin-right: 0px; }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemLabelContainer { margi=
n-left: 16px; }

.peoplekitComponentsResultlistitemLabelContainer { margin-left: 12px; }

.peoplekitComponentsResultlistitemLabelRow { -webkit-box-flex: initial; fle=
x: initial; width: 100%; }

.peoplekitComponentsResultlistitemLabel { display: flex; -webkit-box-orient=
: horizontal; -webkit-box-direction: normal; flex-direction: row; overflow:=
 hidden; text-overflow: ellipsis; white-space: nowrap; }

.peoplekitComponentsResultlistitemLabelText { color: var(--pkw-on-surface,#=
3c4043); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.peoplekitThemeDark .peoplekitComponentsResultlistitemLabelText { color: va=
r(--pkw-on-surface,#e8eaed); }

.peoplekitComponentsResultlistitemTags { display: flex; -webkit-box-orient:=
 horizontal; -webkit-box-direction: normal; flex-direction: row; -webkit-bo=
x-align: center; align-items: center; }

.peoplekitComponentsResultlistitemSublabel { display: flex; -webkit-box-ori=
ent: horizontal; -webkit-box-direction: normal; flex-direction: row; overfl=
ow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.peoplekitComponentsResultlistitemSublabelText { color: var(--pkw-on-surfac=
e-variant,#5f6368); overflow: hidden; text-overflow: ellipsis; white-space:=
 nowrap; }

.peoplekitThemeDark .peoplekitComponentsResultlistitemSublabelText { color:=
 var(--pkw-on-surface-variant,#9aa0a6); }

.peoplekitComponentsResultlistitemAvatar { position: relative; }

.peoplekitComponentsResultlistitemAvatarContainer { height: inherit; width:=
 inherit; position: relative; }

.peoplekitComponentsResultlistitemAvatarSelectionOverlay { background-color=
: var(--pkw-primary,#1a73e8); border-radius: 50%; height: 100%; left: 0px; =
opacity: 0; outline: transparent solid 1px; position: absolute; top: 0px; t=
ransform: scale(0); transition: transform 0.15s ease-out, -webkit-transform=
 0.15s ease-out; width: 100%; display: flex; -webkit-box-align: center; ali=
gn-items: center; -webkit-box-pack: center; justify-content: center; }

.peoplekitThemeDark .peoplekitComponentsResultlistitemAvatarSelectionOverla=
y { background-color: var(--pkw-primary,#8ab4f8); }

.peoplekitComponentsResultlistitemWhiteCheck { fill: var(--pkw-background,#=
fff); display: inline-flex; }

.peoplekitThemeDark .peoplekitComponentsResultlistitemWhiteCheck { fill: va=
r(--pkw-background,#202124); }

@media (forced-colors: active) and (prefers-color-scheme: dark) {
  .peoplekitComponentsResultlistitemWhiteCheck { filter: brightness(0) inve=
rt(1); }
}

@media (forced-colors: active) and (prefers-color-scheme: light) {
  .peoplekitComponentsResultlistitemWhiteCheck { filter: brightness(0); }
}

.peoplekitComponentsResultlistitemOutOfOffice { font-family: Roboto, Arial,=
 sans-serif; line-height: 1.25rem; font-size: 0.875rem; letter-spacing: 0.0=
142857em; font-weight: 400; color: var(--pkw-on-surface-variant,#5f6368); o=
verflow: hidden; text-overflow: ellipsis; white-space: nowrap; display: non=
e; }

.peoplekitThemeDark .peoplekitComponentsResultlistitemOutOfOffice { color: =
var(--pkw-on-surface-variant,#9aa0a6); }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemOutOfOffice { font-fam=
ily: "Google Sans Text", "Google Sans", Roboto, Arial, sans-serif; font-siz=
e: 0.875rem; font-weight: 400; letter-spacing: 0px; line-height: 1.25rem; }

.peoplekitComponentsResultlistitemMetaIcon { margin-left: 16px; }

.peoplekitComponentsResultlistitemMetaIcon[src=3D""] { display: none; }

.peoplekitComponentsListImplList { list-style: none; margin: 0px; padding: =
0px; }

.peoplekitComponentsListImplList:focus { outline: none; }

.peoplekitComponentsResultListCoreGroupSectionListContainer { overflow: hid=
den; transform-origin: center top; transition: 0.5s cubic-bezier(0.05, 0.7,=
 0.1, 1); }

.peoplekitComponentsResultListCoreGroupSectionListContainer.collapsed { hei=
ght: 0px; transform: scaleY(0); transition: 0.2s cubic-bezier(0.3, 0, 0.8, =
0.15); }

.peoplekitComponentsGroupingHeaderCollapsibleChevronContainer { -webkit-box=
-align: center; align-items: center; border-radius: 50%; cursor: pointer; d=
isplay: flex; transition: transform 365ms cubic-bezier(0.4, 0, 0.2, 1), -we=
bkit-transform 365ms cubic-bezier(0.4, 0, 0.2, 1); }

.peoplekitComponentsGroupingHeaderCollapsibleChevronContainer:hover { backg=
round: var(--pkw-background,hsla(0,0%,4%,.04)); }

.peoplekitComponentsGroupingHeaderCollapsibleChevronContainer:active { back=
ground: var(--pkw-background,hsla(0,0%,4%,.12)); }

.peoplekitComponentsGroupingHeaderCollapsibleChevronContainer.isSpotlit { b=
ackground: var(--pkw-background,hsla(0,0%,4%,.12)); outline: transparent so=
lid 3px; outline-offset: -3px; }

.peoplekitComponentsGroupingHeaderCollapsibleChevronContainer.rotate { tran=
sform: rotate(-180deg); }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderCollapsibleChevronCon=
tainer { -webkit-box-align: center; align-items: center; border-radius: 50%=
; cursor: pointer; display: flex; transition: transform 365ms cubic-bezier(=
0.4, 0, 0.2, 1), -webkit-transform 365ms cubic-bezier(0.4, 0, 0.2, 1); }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderCollapsibleChevronCon=
tainer:hover { background: var(--pkw-background,linear-gradient(0deg,rgba(2=
32,234,237,.14),rgba(232,234,237,.14)),#202124); }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderCollapsibleChevronCon=
tainer:active { background: var(--pkw-background,linear-gradient(0deg,rgba(=
232,234,237,.19),rgba(232,234,237,.19)),#202124); }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderCollapsibleChevronCon=
tainer.isSpotlit { background: var(--pkw-background,linear-gradient(0deg,rg=
ba(232,234,237,.19),rgba(232,234,237,.19)),#202124); outline: transparent s=
olid 3px; outline-offset: -3px; }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderCollapsibleChevronCon=
tainer.rotate { transform: rotate(-180deg); }

.peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderCollapsibleChevronCont=
ainer { position: relative; }

.peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderCollapsibleChevronCont=
ainer::before { background: var(--pkw-on-surface-variant,var(--gm3-sys-colo=
r-on-surface-variant,#444746)); border-radius: 50%; content: ""; height: 10=
0%; left: 0px; opacity: 0; position: absolute; top: 0px; width: 100%; }

.peoplekitThemeDark .peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderCo=
llapsibleChevronContainer::before { background: var(--pkw-on-surface-varian=
t,var(--gm3-sys-color-on-surface-variant,#c4c7c5)); }

.peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderCollapsibleChevronCont=
ainer:hover::before { opacity: 0.08; }

.peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderCollapsibleChevronCont=
ainer:active::before { opacity: 0.1; }

.peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderCollapsibleChevronCont=
ainer.isSpotlit::before { opacity: 0.1; }

.peoplekitComponentsGroupingHeaderCollapsibleChevron { fill: var(--pkw-on-s=
urface-variant,#5f6368); }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderCollapsibleChevron { =
fill: var(--pkw-on-surface-variant,#f1f3f4); }

.peoplekitComponentsButtonLabelLabelButton { font-family: "Google Sans", Ro=
boto, Arial, sans-serif; font-size: 0.875rem; letter-spacing: 0.0178571em; =
font-weight: 500; -webkit-box-align: center; align-items: center; backgroun=
d: none; border: none; border-radius: 4px; color: var(--pkw-primary,#1a73e8=
); display: flex; height: 36px; line-height: unset; outline: transparent so=
lid 1px; padding: 0px 8px; user-select: none; }

.peoplekitComponentsButtonLabelLabelButton:hover { background-color: var(--=
pkw-surface-container-high,rgba(26,115,232,.04)); color: var(--pkw-primary,=
#174ea6); cursor: pointer; }

.peoplekitComponentsButtonLabelLabelButton:focus { background-color: var(--=
pkw-surface-container-high,rgba(26,115,232,.12)); color: var(--pkw-primary,=
#174ea6); cursor: pointer; outline-width: 3px; }

.peoplekitComponentsButtonLabelLabelButton.isDisabled { color: var(--pkw-on=
-surface,#3c4043); opacity: 0.38; }

.peoplekitThemeDark .peoplekitComponentsButtonLabelLabelButton { -webkit-bo=
x-align: center; align-items: center; background: none; border: none; borde=
r-radius: 4px; color: var(--pkw-primary,#8ab4f8); display: flex; height: 36=
px; line-height: unset; outline: transparent solid 1px; padding: 0px 8px; u=
ser-select: none; }

.peoplekitThemeDark .peoplekitComponentsButtonLabelLabelButton:hover { back=
ground-color: var(--pkw-surface-container-high,rgba(138,180,248,.04)); colo=
r: var(--pkw-primary,#d2e3fc); cursor: pointer; }

.peoplekitThemeDark .peoplekitComponentsButtonLabelLabelButton:focus { back=
ground-color: var(--pkw-surface-container-high,rgba(138,180,248,.12)); colo=
r: var(--pkw-primary,#d2e3fc); cursor: pointer; outline-width: 3px; }

.peoplekitThemeDark .peoplekitComponentsButtonLabelLabelButton.isDisabled {=
 color: var(--pkw-on-surface,#e8eaed); opacity: 0.38; }

.peopleKitStyleGm3 .peoplekitComponentsButtonLabelLabelButton { font-family=
: "Google Sans Text", "Google Sans", Roboto, Arial, sans-serif; font-size: =
0.875rem; font-weight: 500; letter-spacing: 0px; line-height: 1.25rem; bord=
er-radius: 20px; height: 40px; padding: 0px 24px; position: relative; }

.peopleKitStyleGm3 .peoplekitComponentsButtonLabelLabelButton::before { bac=
kground: var(--pkw-primary,var(--gm3-sys-color-primary,#0b57d0)); border-ra=
dius: 20px; content: ""; height: 100%; left: 0px; opacity: 0; position: abs=
olute; top: 0px; width: 100%; }

.peoplekitThemeDark .peopleKitStyleGm3 .peoplekitComponentsButtonLabelLabel=
Button::before { background: var(--pkw-primary,var(--gm3-sys-color-primary,=
#a8c7fa)); }

.peopleKitStyleGm3 .peoplekitComponentsButtonLabelLabelButton:hover::before=
 { opacity: 0.08; }

.peopleKitStyleGm3 .peoplekitComponentsButtonLabelLabelButton:focus::before=
 { opacity: 0.1; }

.peoplekitComponentsDialogImplScrim { background: var(--pkw-scrim,rgba(32,3=
3,36,.6)); -webkit-box-align: center; align-items: center; box-sizing: bord=
er-box; display: flex; height: 100%; -webkit-box-pack: center; justify-cont=
ent: center; left: 0px; position: fixed; top: 0px; width: 100%; z-index: 99=
9999; }

.peoplekitThemeDark .peoplekitComponentsDialogImplScrim { background: var(-=
-pkw-scrim,rgba(32,33,36,.6)); }

.peoplekitComponentsDialogImplDialog { border-width: 0px; box-shadow: rgba(=
60, 64, 67, 0.3) 0px 1px 3px 0px, rgba(60, 64, 67, 0.15) 0px 4px 8px 3px; b=
ackground: var(--pkw-surface-container-high,#fff); text-wrap-mode: wrap; bo=
rder-radius: 8px; max-width: 300px; outline: transparent solid 1px; overflo=
w: hidden; }

.peoplekitComponentsDialogImplDialog .mdc-elevation-overlay { opacity: 0; }

.peoplekitThemeDark .peoplekitComponentsDialogImplDialog { background: var(=
--pkw-surface-container-high,linear-gradient(0deg,rgba(232,234,237,.08),rgb=
a(232,234,237,.08)),#202124); }

.peoplekitComponentsDialogImplDialog.peopleKitStyleGm3 { box-shadow: rgba(0=
, 0, 0, 0.3) 0px 1px 3px 0px, rgba(0, 0, 0, 0.15) 0px 4px 8px 3px; border-r=
adius: 28px; padding: 24px; }

.peoplekitComponentsDialogImplAvatarHeader { background: var(--pkw-surface-=
container-high,#fff); border-bottom: 1px solid var(--pkw-outline-variant,#d=
adce0); display: flex; -webkit-box-orient: vertical; -webkit-box-direction:=
 normal; flex-direction: column; -webkit-box-pack: center; justify-content:=
 center; padding: 12px; }

.peoplekitThemeDark .peoplekitComponentsDialogImplAvatarHeader { background=
: var(--pkw-surface-container-high,linear-gradient(0deg,rgba(232,234,237,.0=
8),rgba(232,234,237,.08)),#202124); border-bottom: 1px solid var(--pkw-outl=
ine-variant,#80868b); }

.peopleKitStyleGm3 .peoplekitComponentsDialogImplAvatarHeader { padding: 0p=
x 0px 8px; }

.peoplekitComponentsDialogImplTextHeader { font-family: "Google Sans", Robo=
to, Arial, sans-serif; line-height: 1.5rem; font-size: 1rem; letter-spacing=
: 0.00625em; font-weight: 500; background: var(--pkw-surface-container-high=
,#fff); color: var(--pkw-on-surface,#202124); margin: 24px 24px 20px; }

.peoplekitThemeDark .peoplekitComponentsDialogImplTextHeader { background: =
var(--pkw-surface-container-high,linear-gradient(0deg,rgba(232,234,237,.08)=
,rgba(232,234,237,.08)),#202124); color: var(--pkw-on-surface,#e8eaed); }

.peopleKitStyleGm3 .peoplekitComponentsDialogImplTextHeader { font-family: =
"Google Sans", Roboto, Arial, sans-serif; font-size: 1.5rem; font-weight: 4=
00; letter-spacing: 0px; line-height: 2rem; margin: 0px; }

.peoplekitComponentsDialogImplHeaderRow { -webkit-box-align: center; align-=
items: center; display: flex; -webkit-box-orient: horizontal; -webkit-box-d=
irection: normal; flex-flow: row; }

.peoplekitComponentsDialogImplLeft { -webkit-box-flex: initial; flex: initi=
al; }

.peoplekitComponentsDialogImplCenter { -webkit-box-flex: 1; flex: 1 1 auto;=
 overflow: hidden; }

.peoplekitComponentsDialogImplAvatar { position: relative; }

.peoplekitComponentsDialogImplAvatarContainer { height: inherit; position: =
relative; width: inherit; }

.peoplekitComponentsDialogImplLabelContainer { align-content: flex-start; -=
webkit-box-align: start; align-items: flex-start; display: flex; -webkit-bo=
x-orient: vertical; -webkit-box-direction: normal; flex-flow: column; margi=
n-left: 12px; margin-right: 0px; }

.peoplekitComponentsDialogImplLabelRow { -webkit-box-flex: initial; flex: i=
nitial; width: 100%; }

.peoplekitComponentsDialogImplLabel { font-family: "Google Sans", Roboto, A=
rial, sans-serif; line-height: 1.25rem; font-size: 0.875rem; letter-spacing=
: 0.0178571em; font-weight: 500; color: var(--pkw-on-surface,#202124); over=
flow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.peoplekitThemeDark .peoplekitComponentsDialogImplLabel { color: var(--pkw-=
on-surface,#e8eaed); }

.peopleKitStyleGm3 .peoplekitComponentsDialogImplLabel { font-family: "Goog=
le Sans Text", "Google Sans", Roboto, Arial, sans-serif; font-size: 0.875re=
m; font-weight: 500; letter-spacing: 0px; line-height: 1.25rem; }

.peoplekitComponentsDialogImplSublabel { font-family: Roboto, Arial, sans-s=
erif; line-height: 1rem; font-size: 0.75rem; letter-spacing: 0.025em; font-=
weight: 400; color: var(--pkw-on-surface-variant,#3c4043); overflow: hidden=
; text-overflow: ellipsis; white-space: nowrap; }

.peoplekitThemeDark .peoplekitComponentsDialogImplSublabel { color: var(--p=
kw-on-surface-variant,#9aa0a6); }

.peopleKitStyleGm3 .peoplekitComponentsDialogImplSublabel { font-family: "G=
oogle Sans Text", "Google Sans", Roboto, Arial, sans-serif; font-size: 0.75=
rem; font-weight: 500; letter-spacing: 0.00625rem; line-height: 1rem; }

.peoplekitComponentsDialogImplContent { font-family: Roboto, Arial, sans-se=
rif; line-height: 1.5rem; font-size: 1rem; letter-spacing: 0.00625em; font-=
weight: 400; color: var(--pkw-on-surface-variant,#3c4043); margin: 24px 24p=
x 20px; }

.peoplekitThemeDark .peoplekitComponentsDialogImplContent { color: var(--pk=
w-on-surface-variant,#e8eaed); }

.peopleKitStyleGm3 .peoplekitComponentsDialogImplContent { font-family: "Go=
ogle Sans Text", "Google Sans", Roboto, Arial, sans-serif; font-size: 0.875=
rem; font-weight: 400; letter-spacing: 0px; line-height: 1.25rem; margin: 0=
px; padding-top: 16px; padding-bottom: 24px; }

.peoplekitComponentsDialogImplActions { display: flex; -webkit-box-pack: en=
d; justify-content: flex-end; padding: 8px; }

.peopleKitStyleGm3 .peoplekitComponentsDialogImplActions { padding: 0px; }

.peoplekitComponentsDialogImplActionDivider { width: 8px; }

.peoplekitComponentsGroupingHeaderInfoInfoIconContainer { -webkit-box-align=
: center; align-items: center; border-radius: 50%; cursor: pointer; display=
: flex; transition: transform 365ms cubic-bezier(0.4, 0, 0.2, 1), -webkit-t=
ransform 365ms cubic-bezier(0.4, 0, 0.2, 1); }

.peoplekitComponentsGroupingHeaderInfoInfoIconContainer:hover { background:=
 var(--pkw-background,hsla(0,0%,4%,.04)); }

.peoplekitComponentsGroupingHeaderInfoInfoIconContainer:active { background=
: var(--pkw-background,hsla(0,0%,4%,.12)); }

.peoplekitComponentsGroupingHeaderInfoInfoIconContainer.isSpotlit { backgro=
und: var(--pkw-background,hsla(0,0%,4%,.12)); outline: transparent solid 3p=
x; outline-offset: -3px; }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderInfoInfoIconContainer=
 { -webkit-box-align: center; align-items: center; border-radius: 50%; curs=
or: pointer; display: flex; transition: transform 365ms cubic-bezier(0.4, 0=
, 0.2, 1), -webkit-transform 365ms cubic-bezier(0.4, 0, 0.2, 1); }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderInfoInfoIconContainer=
:hover { background: var(--pkw-background,linear-gradient(0deg,rgba(232,234=
,237,.14),rgba(232,234,237,.14)),#202124); }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderInfoInfoIconContainer=
:active { background: var(--pkw-background,linear-gradient(0deg,rgba(232,23=
4,237,.19),rgba(232,234,237,.19)),#202124); }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderInfoInfoIconContainer=
.isSpotlit { background: var(--pkw-background,linear-gradient(0deg,rgba(232=
,234,237,.19),rgba(232,234,237,.19)),#202124); outline: transparent solid 3=
px; outline-offset: -3px; }

.peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderInfoInfoIconContainer =
{ position: relative; }

.peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderInfoInfoIconContainer:=
:before { background: var(--pkw-on-surface-variant,var(--gm3-sys-color-on-s=
urface-variant,#444746)); border-radius: 50%; content: ""; height: 100%; le=
ft: 0px; opacity: 0; position: absolute; top: 0px; width: 100%; }

.peoplekitThemeDark .peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderIn=
foInfoIconContainer::before { background: var(--pkw-on-surface-variant,var(=
--gm3-sys-color-on-surface-variant,#c4c7c5)); }

.peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderInfoInfoIconContainer:=
hover::before { opacity: 0.08; }

.peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderInfoInfoIconContainer:=
active::before { opacity: 0.1; }

.peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderInfoInfoIconContainer.=
isSpotlit::before { opacity: 0.1; }

.peoplekitComponentsGroupingHeaderInfoLearnMoreLink { color: var(--pkw-prim=
ary,#1a73e8); text-decoration: underline; }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderInfoLearnMoreLink { c=
olor: var(--pkw-primary,#8ab4f8); }

.peoplekitComponentsGroupingHeaderInfoLearnMoreLink:visited { color: var(--=
pkw-primary,#1a73e8); }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderInfoLearnMoreLink:vis=
ited { color: var(--pkw-primary,#8ab4f8); }

.peoplekitComponentsGroupingHeaderInfoInfoIcon { fill: var(--pkw-on-surface=
-variant,#5f6368); height: 16px; padding: 5px; width: 16px; }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderInfoInfoIcon { fill: =
var(--pkw-on-surface-variant,#f1f3f4); }

@media (forced-colors: active) and (prefers-color-scheme: dark) {
  .peoplekitComponentsGroupingHeaderInfoInfoIcon { filter: brightness(0) in=
vert(1); }
}

@media (forced-colors: active) and (prefers-color-scheme: light) {
  .peoplekitComponentsGroupingHeaderInfoInfoIcon { filter: brightness(0); }
}

.peoplekitComponentsGroupingHeaderGroupingHeader { background: var(--pkw-ba=
ckground,#fff); }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderGroupingHeader { back=
ground: var(--pkw-background,linear-gradient(0deg,rgba(232,234,237,.08),rgb=
a(232,234,237,.08)),#202124); }

.peoplekitComponentsGroupingHeaderGroupingHeaderRow { -webkit-box-align: ce=
nter; align-items: center; display: flex; -webkit-box-orient: horizontal; -=
webkit-box-direction: normal; flex-flow: row; padding-left: 16px; padding-r=
ight: 16px; }

.peoplekitComponentsGroupingHeaderHeader { font-family: Roboto, Arial, sans=
-serif; line-height: 1rem; font-size: 0.6875rem; letter-spacing: 0.0727273e=
m; font-weight: 500; text-transform: uppercase; color: var(--pkw-on-surface=
-variant,#5f6368); padding-bottom: 11px; padding-top: 13px; }

.peoplekitThemeDark .peoplekitComponentsGroupingHeaderHeader { color: var(-=
-pkw-on-surface-variant,#f1f3f4); }

.peopleKitStyleGm3 .peoplekitComponentsGroupingHeaderHeader { font-family: =
"Google Sans Text", "Google Sans", Roboto, Arial, sans-serif; font-size: 0.=
875rem; font-weight: 500; letter-spacing: 0px; line-height: 1.25rem; text-t=
ransform: none; padding: 6px 0px; }

.peoplekitComponentsGroupingHeaderAction { flex-shrink: initial; flex-basis=
: initial; -webkit-box-flex: 1; flex-grow: 1; }

.peoplekitComponentsGroupingHeaderActionRow { -webkit-box-align: center; al=
ign-items: center; display: flex; -webkit-box-orient: horizontal; -webkit-b=
ox-direction: normal; flex-direction: row; -webkit-box-pack: justify; justi=
fy-content: space-between; }

.peoplekitComponentsGroupingHeaderLeft { -webkit-box-flex: initial; flex: i=
nitial; }

.peoplekitComponentsGroupingHeaderRight { -webkit-box-flex: initial; flex: =
initial; margin-left: 16px; margin-right: 4px; }

.peoplekitComponentsTagTag { background: rgb(241, 243, 244); color: rgb(32,=
 33, 36); display: flex; -webkit-box-orient: horizontal; -webkit-box-direct=
ion: normal; flex-direction: row; -webkit-box-align: center; align-items: c=
enter; margin-left: 8px; border-radius: 4px; outline: transparent solid 1px=
; overflow: hidden; position: relative; }

.peoplekitComponentsTagTag.isWarning { background: rgb(251, 188, 4); color:=
 rgb(32, 33, 36); }

.peopleKitStyleGm3 .peoplekitComponentsTagTag { background: var(--gm3-sys-c=
olor-surface-container-high,#e9eef6); color: var(--gm3-sys-color-on-surface=
-variant,#444746); }

.peopleKitStyleGm3 .peoplekitComponentsTagTag.isWarning { background: rgb(2=
55, 187, 41); color: var(--gm3-sys-color-on-surface,#1f1f1f); }

@media (forced-colors: none) {
  .peopleKitStyleGm3 .peoplekitComponentsTagIcon.isWarning { filter: bright=
ness(0) saturate(100%) invert(0) sepia(7%) saturate(1357%) hue-rotate(335de=
g) brightness(112%) contrast(76%); }
}

.googleMaterialDefaultDensity .peoplekitComponentsTagTag { height: 20px; mi=
n-width: 20px; }

.workspaceMaterialComfortableDensity .peoplekitComponentsTagTag, .workspace=
MaterialCompactDensity .peoplekitComponentsTagTag { height: 16px; min-width=
: 16px; }

.googleMaterialDefaultDensity .peoplekitComponentsTagIcon { width: 16px; he=
ight: 16px; margin-left: 2px; font-size: 16px; }

.workspaceMaterialComfortableDensity .peoplekitComponentsTagIcon, .workspac=
eMaterialCompactDensity .peoplekitComponentsTagIcon { width: 14px; height: =
14px; margin-left: 1px; font-size: 14px; }

.peoplekitComponentsTagUnrollingAltText { max-width: 0px; overflow: hidden;=
 transition: max-width 0.3s; }

.peoplekitComponentsTagTag:hover .peoplekitComponentsTagUnrollingAltText { =
max-width: 1000px; }

@media (forced-colors: active) and (prefers-color-scheme: dark) {
  .peoplekitComponentsTagIcon { filter: brightness(0) invert(1); }
}

.peoplekitComponentsTagText { margin-left: 4px; margin-right: 4px; }

.googleMaterialDefaultDensity .peoplekitComponentsTagText { font-family: Ro=
boto, Arial, sans-serif; line-height: 1.25rem; font-size: 0.875rem; letter-=
spacing: 0.0178571em; font-weight: 500; }

.googleMaterialDefaultDensity .peoplekitComponentsTagText.peopleKitStyleGm3=
 { font-family: "Google Sans Text", "Google Sans", Roboto, Arial, sans-seri=
f; font-size: 0.875rem; font-weight: 400; letter-spacing: 0px; line-height:=
 1.25rem; }

.workspaceMaterialComfortableDensity .peoplekitComponentsTagText { font-fam=
ily: Roboto, Arial, sans-serif; line-height: 1rem; font-size: 0.75rem; lett=
er-spacing: 0.025em; font-weight: 400; }

.workspaceMaterialComfortableDensity .peoplekitComponentsTagText.peopleKitS=
tyleGm3 { font-family: "Google Sans Text", "Google Sans", Roboto, Arial, sa=
ns-serif; font-size: 0.75rem; font-weight: 400; letter-spacing: 0.00625rem;=
 line-height: 1rem; }

.workspaceMaterialCompactDensity .peoplekitComponentsTagText { font-family:=
 Roboto, Arial, sans-serif; line-height: 1rem; font-size: 0.75rem; letter-s=
pacing: 0.025em; font-weight: 400; }

.workspaceMaterialCompactDensity .peoplekitComponentsTagText.peopleKitStyle=
Gm3 { font-family: "Google Sans Text", "Google Sans", Roboto, Arial, sans-s=
erif; font-size: 0.75rem; font-weight: 400; letter-spacing: 0.00625rem; lin=
e-height: 1rem; }

.peoplekitComponentsResultlistitemDisabledDisableReasonContainer { -webkit-=
box-align: center; align-items: center; display: flex; }

.peoplekitComponentsResultlistitemDisabledTextIndicator { font-family: Robo=
to, Arial, sans-serif; line-height: 1.5rem; font-size: 1rem; letter-spacing=
: 0.00625em; font-weight: 400; color: var(--pkw-on-surface,#5f6368); }

.peoplekitThemeDark .peoplekitComponentsResultlistitemDisabledTextIndicator=
 { color: var(--pkw-on-surface,#fff); }

.peopleKitStyleGm3 .peoplekitComponentsResultlistitemDisabledTextIndicator =
{ font-family: "Google Sans Text", "Google Sans", Roboto, Arial, sans-serif=
; line-height: 1.5rem; font-size: 1rem; letter-spacing: 0px; font-weight: 4=
00; }

.peoplekitComponentsResultlistitemDisabledIconIndicator { display: flex; -w=
ebkit-box-align: center; align-items: center; -webkit-box-pack: center; jus=
tify-content: center; background: var(--pkw-background,#f1f3f4); border-rad=
ius: 50px; width: 32px; height: 32px; margin-left: 16px; margin-right: 4px;=
 }

.peoplekitThemeDark .peoplekitComponentsResultlistitemDisabledIconIndicator=
 { background: var(--pkw-background,rgba(241,243,244,.14)); }

.peoplekitComponentsResultlistitemDisabledSelectedIcon { fill: var(--pkw-on=
-surface-variant,#5f6368); }

.peoplekitThemeDark .peoplekitComponentsResultlistitemDisabledSelectedIcon =
{ fill: var(--pkw-on-surface-variant,#e8eaed); }

@media (forced-colors: active) and (prefers-color-scheme: dark) {
  .peoplekitComponentsResultlistitemDisabledSelectedIcon { filter: brightne=
ss(0) invert(1); }
}

@media (forced-colors: active) and (prefers-color-scheme: light) {
  .peoplekitComponentsResultlistitemDisabledSelectedIcon { filter: brightne=
ss(0); }
}

.peoplekitUiResultlistHeader { font-family: Roboto, Arial, sans-serif; line=
-height: 1rem; font-size: 0.6875rem; letter-spacing: 0.0727273em; font-weig=
ht: 500; text-transform: uppercase; background: var(--pkw-background,#fff);=
 color: var(--pkw-on-surface-variant,#5f6368); padding-bottom: 12px; paddin=
g-left: 16px; padding-top: 12px; }

.peoplekitThemeDark .peoplekitUiResultlistHeader { background: var(--pkw-ba=
ckground,linear-gradient(0deg,rgba(232,234,237,.08),rgba(232,234,237,.08)),=
#202124); color: var(--pkw-on-surface-variant,#f1f3f4); }

.peopleKitStyleGm3 .peoplekitUiResultlistHeader { font-family: "Google Sans=
 Text", "Google Sans", Roboto, Arial, sans-serif; font-size: 0.875rem; font=
-weight: 500; letter-spacing: 0px; line-height: 1.25rem; text-transform: no=
ne; }

.peoplekitComponentsAutocompleteInlineContainer { background: var(--pkw-bac=
kground,#fff); height: 100%; display: flex; -webkit-box-orient: vertical; -=
webkit-box-direction: normal; flex-direction: column; overflow: hidden; use=
r-select: none; }

.peoplekitThemeDark .peoplekitComponentsAutocompleteInlineContainer { backg=
round: var(--pkw-background,linear-gradient(0deg,rgba(232,234,237,.08),rgba=
(232,234,237,.08)),#202124); }

.peoplekitComponentsAutocompleteInlineContainer.isLoading .peoplekitCompone=
ntsAutocompleteInlineListContainer, .peoplekitComponentsAutocompleteInlineC=
ontainer.isLoading .peoplekitComponentsAutocompleteInlineNoResultsContainer=
 { display: none; }

.peoplekitComponentsAutocompleteInlineContainer.isLoading .peoplekitCompone=
ntsAutocompleteInlineCircularProgress { display: flex; -webkit-box-pack: ce=
nter; justify-content: center; -webkit-box-align: center; align-items: cent=
er; height: 100%; }

.peoplekitComponentsAutocompleteInlineContainer.isLoading .peoplekitCompone=
ntsAutocompleteInlineCircularProgress::before { -webkit-box-flex: 1; flex: =
1 1 auto; }

.peoplekitComponentsAutocompleteInlineContainer.isLoading .peoplekitCompone=
ntsAutocompleteInlineCircularProgress::after { -webkit-box-flex: 1; flex: 1=
 1 auto; }

.peoplekitComponentsAutocompleteInlineContainer.noResults .peoplekitCompone=
ntsAutocompleteInlineCircularProgress, .peoplekitComponentsAutocompleteInli=
neContainer.noResults .peoplekitComponentsAutocompleteInlineListContainer {=
 display: none; }

.peoplekitComponentsAutocompleteInlineContainer.noResults .peoplekitCompone=
ntsAutocompleteInlineNoResultsContainer { display: flex; -webkit-box-orient=
: vertical; -webkit-box-direction: normal; flex-direction: column; -webkit-=
box-pack: start; justify-content: flex-start; -webkit-box-align: center; al=
ign-items: center; height: 100%; overflow: auto; }

.peoplekitComponentsAutocompleteInlineListContainer { height: 100%; display=
: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-d=
irection: column; overflow: hidden; }

.peoplekitComponentsAutocompleteInlineCircularProgress, .peoplekitComponent=
sAutocompleteInlineNoResultsContainer { display: none; }

.peoplekitComponentsCircularprogressCircularProgress { display: inline-bloc=
k; height: 40px; position: relative; width: 40px; direction: ltr; }

.peoplekitComponentsCircularprogressMessageContainer { height: 0px; overflo=
w: hidden; position: absolute; width: 0px; }

.peoplekitComponentsCircularprogressCircularProgressContainer { width: 100%=
; height: 100%; }

.peoplekitComponentsCircularprogressCircularProgress.isActive .peoplekitCom=
ponentsCircularprogressCircularProgressContainer { animation: 1568ms linear=
 0s infinite normal none running circular-progress-container-rotate; }

.peoplekitComponentsCircularprogressCircularProgressLayer { height: 100%; o=
pacity: 0; position: absolute; width: 100%; }

.peoplekitComponentsCircularprogressColorOne { border-color: rgb(66, 133, 2=
44); }

.peoplekitComponentsCircularprogressColorTwo { border-color: rgb(234, 67, 5=
3); }

.peoplekitComponentsCircularprogressColorThree { border-color: rgb(251, 188=
, 4); }

.peoplekitComponentsCircularprogressColorFour { border-color: rgb(52, 168, =
83); }

.peoplekitComponentsCircularprogressCircularProgress.isActive .peoplekitCom=
ponentsCircularprogressCircularProgressLayer.peoplekitComponentsCircularpro=
gressColorOne { animation: 5332ms cubic-bezier(0.4, 0, 0.2, 1) 0s infinite =
normal both running circular-progress-fill-unfill-rotate, 5332ms cubic-bezi=
er(0.4, 0, 0.2, 1) 0s infinite normal both running circular-progress-blue-f=
ade-in-out; }

.peoplekitComponentsCircularprogressCircularProgress.isActive .peoplekitCom=
ponentsCircularprogressCircularProgressLayer.peoplekitComponentsCircularpro=
gressColorTwo { animation: 5332ms cubic-bezier(0.4, 0, 0.2, 1) 0s infinite =
normal both running circular-progress-fill-unfill-rotate, 5332ms cubic-bezi=
er(0.4, 0, 0.2, 1) 0s infinite normal both running circular-progress-red-fa=
de-in-out; }

.peoplekitComponentsCircularprogressCircularProgress.isActive .peoplekitCom=
ponentsCircularprogressCircularProgressLayer.peoplekitComponentsCircularpro=
gressColorThree { animation: 5332ms cubic-bezier(0.4, 0, 0.2, 1) 0s infinit=
e normal both running circular-progress-fill-unfill-rotate, 5332ms cubic-be=
zier(0.4, 0, 0.2, 1) 0s infinite normal both running circular-progress-yell=
ow-fade-in-out; }

.peoplekitComponentsCircularprogressCircularProgress.isActive .peoplekitCom=
ponentsCircularprogressCircularProgressLayer.peoplekitComponentsCircularpro=
gressColorFour { animation: 5332ms cubic-bezier(0.4, 0, 0.2, 1) 0s infinite=
 normal both running circular-progress-fill-unfill-rotate, 5332ms cubic-bez=
ier(0.4, 0, 0.2, 1) 0s infinite normal both running circular-progress-green=
-fade-in-out; }

.peoplekitComponentsCircularprogressGapPatch { position: absolute; box-sizi=
ng: border-box; top: 0px; left: 45%; width: 10%; height: 100%; overflow: hi=
dden; border-color: inherit; }

.peoplekitComponentsCircularprogressGapPatch .peoplekitComponentsCircularpr=
ogressCircle { width: 1000%; left: -450%; }

.peoplekitComponentsCircularprogressCircleClipper { display: inline-block; =
position: relative; width: 50%; height: 100%; overflow: hidden; border-colo=
r: inherit; }

.peoplekitComponentsCircularprogressCircleClipper .peoplekitComponentsCircu=
larprogressCircle { width: 200%; }

.peoplekitComponentsCircularprogressCircle { position: absolute; inset: 0px=
; box-sizing: border-box; height: 100%; border-width: 3px; border-style: so=
lid; border-top-color: inherit; border-right-color: inherit; border-left-co=
lor: inherit; border-bottom-color: transparent; border-radius: 50%; animati=
on: auto ease 0s 1 normal none running none; }

.peoplekitComponentsCircularprogressCircleClipper.peoplekitComponentsCircul=
arprogressLeft .peoplekitComponentsCircularprogressCircle { border-right-co=
lor: transparent; transform: rotate(129deg); }

.peoplekitComponentsCircularprogressCircleClipper.peoplekitComponentsCircul=
arprogressRight .peoplekitComponentsCircularprogressCircle { left: -100%; b=
order-left-color: transparent; transform: rotate(-129deg); }

.peoplekitComponentsCircularprogressCircularProgress.isActive .peoplekitCom=
ponentsCircularprogressCircleClipper.peoplekitComponentsCircularprogressLef=
t .peoplekitComponentsCircularprogressCircle { animation: 1333ms cubic-bezi=
er(0.4, 0, 0.2, 1) 0s infinite normal both running circular-progress-left-s=
pin; }

.peoplekitComponentsCircularprogressCircularProgress.isActive .peoplekitCom=
ponentsCircularprogressCircleClipper.peoplekitComponentsCircularprogressRig=
ht .peoplekitComponentsCircularprogressCircle { animation: 1333ms cubic-bez=
ier(0.4, 0, 0.2, 1) 0s infinite normal both running circular-progress-right=
-spin; }

.peoplekitComponentsCircularprogressCircularProgress.isWarmdown .peoplekitC=
omponentsCircularprogressCircularProgressContainer { animation: 1568ms line=
ar 0s infinite normal none running circular-progress-container-rotate, 0.4s=
 cubic-bezier(0.4, 0, 0.2, 1) 0s 1 normal none running circular-progress-fa=
de-out; }

@-webkit-keyframes circular-progress-container-rotate {=20
  100% { transform: rotate(1turn); }
}

@keyframes circular-progress-container-rotate {=20
  100% { transform: rotate(1turn); }
}

@-webkit-keyframes circular-progress-fill-unfill-rotate {=20
  12.5% { transform: rotate(135deg); }
  25% { transform: rotate(270deg); }
  37.5% { transform: rotate(405deg); }
  50% { transform: rotate(540deg); }
  62.5% { transform: rotate(675deg); }
  75% { transform: rotate(810deg); }
  87.5% { transform: rotate(945deg); }
  100% { transform: rotate(3turn); }
}

@keyframes circular-progress-fill-unfill-rotate {=20
  12.5% { transform: rotate(135deg); }
  25% { transform: rotate(270deg); }
  37.5% { transform: rotate(405deg); }
  50% { transform: rotate(540deg); }
  62.5% { transform: rotate(675deg); }
  75% { transform: rotate(810deg); }
  87.5% { transform: rotate(945deg); }
  100% { transform: rotate(3turn); }
}

@-webkit-keyframes circular-progress-blue-fade-in-out {=20
  0% { opacity: 0.99; }
  25% { opacity: 0.99; }
  26% { opacity: 0; }
  89% { opacity: 0; }
  90% { opacity: 0.99; }
  100% { opacity: 0.99; }
}

@keyframes circular-progress-blue-fade-in-out {=20
  0% { opacity: 0.99; }
  25% { opacity: 0.99; }
  26% { opacity: 0; }
  89% { opacity: 0; }
  90% { opacity: 0.99; }
  100% { opacity: 0.99; }
}

@-webkit-keyframes circular-progress-red-fade-in-out {=20
  0% { opacity: 0; }
  15% { opacity: 0; }
  25% { opacity: 0.99; }
  50% { opacity: 0.99; }
  51% { opacity: 0; }
}

@keyframes circular-progress-red-fade-in-out {=20
  0% { opacity: 0; }
  15% { opacity: 0; }
  25% { opacity: 0.99; }
  50% { opacity: 0.99; }
  51% { opacity: 0; }
}

@-webkit-keyframes circular-progress-yellow-fade-in-out {=20
  0% { opacity: 0; }
  40% { opacity: 0; }
  50% { opacity: 0.99; }
  75% { opacity: 0.99; }
  76% { opacity: 0; }
}

@keyframes circular-progress-yellow-fade-in-out {=20
  0% { opacity: 0; }
  40% { opacity: 0; }
  50% { opacity: 0.99; }
  75% { opacity: 0.99; }
  76% { opacity: 0; }
}

@-webkit-keyframes circular-progress-green-fade-in-out {=20
  0% { opacity: 0; }
  65% { opacity: 0; }
  75% { opacity: 0.99; }
  90% { opacity: 0.99; }
  100% { opacity: 0; }
}

@keyframes circular-progress-green-fade-in-out {=20
  0% { opacity: 0; }
  65% { opacity: 0; }
  75% { opacity: 0.99; }
  90% { opacity: 0.99; }
  100% { opacity: 0; }
}

@-webkit-keyframes circular-progress-left-spin {=20
  0% { transform: rotate(130deg); }
  50% { transform: rotate(-5deg); }
  100% { transform: rotate(130deg); }
}

@keyframes circular-progress-left-spin {=20
  0% { transform: rotate(130deg); }
  50% { transform: rotate(-5deg); }
  100% { transform: rotate(130deg); }
}

@-webkit-keyframes circular-progress-right-spin {=20
  0% { transform: rotate(-130deg); }
  50% { transform: rotate(5deg); }
  100% { transform: rotate(-130deg); }
}

@keyframes circular-progress-right-spin {=20
  0% { transform: rotate(-130deg); }
  50% { transform: rotate(5deg); }
  100% { transform: rotate(-130deg); }
}

@-webkit-keyframes circular-progress-fade-out {=20
  0% { opacity: 0.99; }
  100% { opacity: 0; }
}

@keyframes circular-progress-fade-out {=20
  0% { opacity: 0.99; }
  100% { opacity: 0; }
}

.peoplekitComponentsScrollboxScrollbar { border: none; outline: none; overf=
low: auto; }

.peoplekitComponentsNoResultsMessageNoResultsMessage { color: var(--pkw-on-=
surface,#5f6368); padding: 2em; text-align: center; -webkit-box-align: cent=
er; align-items: center; }

.peoplekitThemeDark .peoplekitComponentsNoResultsMessageNoResultsMessage { =
color: var(--pkw-on-surface,#9aa0a6); }

.peoplekitComponentsNoResultsMessageHeader { font-family: "Google Sans", Ro=
boto, Arial, sans-serif; line-height: 1.5rem; font-size: 1rem; letter-spaci=
ng: 0.00625em; font-weight: 500; }

.peopleKitStyleGm3 .peoplekitComponentsNoResultsMessageHeader { font-family=
: "Google Sans Text", "Google Sans", Roboto, Arial, sans-serif; font-size: =
1rem; font-weight: 500; letter-spacing: 0px; line-height: 1.5rem; }

.peoplekitComponentsNoResultsMessageExplanation { font-family: Roboto, Aria=
l, sans-serif; line-height: 1.25rem; font-size: 0.875rem; letter-spacing: 0=
.0142857em; font-weight: 400; }

.peopleKitStyleGm3 .peoplekitComponentsNoResultsMessageExplanation { font-f=
amily: "Google Sans Text", "Google Sans", Roboto, Arial, sans-serif; font-s=
ize: 0.875rem; font-weight: 400; letter-spacing: 0px; line-height: 1.25rem;=
 }

.peoplekitComponentsNoResultsMessageLearnMoreLink { color: inherit; text-de=
coration: underline; white-space: nowrap; }

.peoplekitComponentsAutocompletePopupContainer { border-width: 0px; box-sha=
dow: rgba(60, 64, 67, 0.3) 0px 1px 3px 0px, rgba(60, 64, 67, 0.15) 0px 4px =
8px 3px; background: var(--pkw-background,#fff); border-radius: 4px; displa=
y: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-=
direction: column; outline: transparent solid 2px; padding-bottom: 8px; pad=
ding-top: 8px; position: absolute; user-select: none; z-index: 999999; }

.peoplekitComponentsAutocompletePopupContainer .mdc-elevation-overlay { opa=
city: 0; }

.peoplekitThemeDark .peoplekitComponentsAutocompletePopupContainer { backgr=
ound: var(--pkw-background,linear-gradient(0deg,rgba(232,234,237,.08),rgba(=
232,234,237,.08)),#202124); }

.peopleKitStyleGm3 .peoplekitComponentsAutocompletePopupContainer { box-sha=
dow: rgba(0, 0, 0, 0.15) 0px 2px 6px 2px, rgba(0, 0, 0, 0.3) 0px 1px 2px 0p=
x; }

.goog-menu { background: rgb(255, 255, 255); border-color: rgb(204, 204, 20=
4) rgb(102, 102, 102) rgb(102, 102, 102) rgb(204, 204, 204); border-style: =
solid; border-width: 1px; font: 13px Arial, sans-serif; padding: 4px 0px; z=
-index: 20000; }

.goog-menuitem { color: rgb(0, 0, 0); font: 13px Arial, sans-serif; list-st=
yle: none; margin: 0px; padding: 4px 7em 4px 28px; white-space: nowrap; }

.goog-menuitem.goog-menuitem-rtl { padding-left: 7em; padding-right: 28px; =
}

.goog-menu-nocheckbox .goog-menuitem, .goog-menu-noicon .goog-menuitem { pa=
dding-left: 12px; }

.goog-menu-noaccel .goog-menuitem { padding-right: 20px; }

.goog-menuitem-content { color: rgb(0, 0, 0); font: 13px Arial, sans-serif;=
 }

.goog-menuitem-disabled .goog-menuitem-accel, .goog-menuitem-disabled .goog=
-menuitem-content { color: rgb(204, 204, 204) !important; }

.goog-menuitem-disabled .goog-menuitem-icon { opacity: 0.3; }

.goog-menuitem-highlight, .goog-menuitem-hover { background-color: rgb(214,=
 233, 248); border-color: rgb(214, 233, 248); border-style: dotted; border-=
width: 1px 0px; padding-bottom: 3px; padding-top: 3px; }

.goog-menuitem-checkbox, .goog-menuitem-icon { background-repeat: no-repeat=
; height: 16px; left: 6px; position: absolute; right: auto; vertical-align:=
 middle; width: 16px; }

.goog-menuitem-rtl .goog-menuitem-checkbox, .goog-menuitem-rtl .goog-menuit=
em-icon { left: auto; right: 6px; }

.goog-option-selected .goog-menuitem-checkbox, .goog-option-selected .goog-=
menuitem-icon { background: url("//ssl.gstatic.com/editor/editortoolbar.png=
") -512px 0px no-repeat; }

.goog-menuitem-accel { color: rgb(153, 153, 153); direction: ltr; left: aut=
o; padding: 0px 6px; position: absolute; right: 0px; text-align: right; }

.goog-menuitem-rtl .goog-menuitem-accel { left: 0px; right: auto; text-alig=
n: left; }

.goog-menuitem-mnemonic-hint { text-decoration: underline; }

.goog-menuitem-mnemonic-separator { color: rgb(153, 153, 153); font-size: 1=
2px; padding-left: 4px; }

.goog-menuseparator { border-top: 1px solid rgb(204, 204, 204); margin: 4px=
 0px; padding: 0px; }

.goog-combobox { background: url("//ssl.gstatic.com/closure/button-bg.gif")=
 0px 0px repeat-x scroll rgb(221, 221, 221); border: 1px solid rgb(181, 182=
, 181); font: small arial, sans-serif; }

.goog-combobox input { background-color: rgb(255, 255, 255); border-width: =
0px 1px 0px 0px; border-top-style: initial; border-bottom-style: initial; b=
order-left-style: initial; border-top-color: initial; border-bottom-color: =
initial; border-left-color: initial; border-image: initial; border-right-st=
yle: solid; border-right-color: rgb(181, 182, 181); color: rgb(0, 0, 0); fo=
nt: small arial, sans-serif; margin: 0px; padding: 0px 0px 0px 2px; vertica=
l-align: bottom; width: 200px; }

.goog-combobox input.label-input-label { background-color: rgb(255, 255, 25=
5); color: rgb(170, 170, 170); }

.goog-combobox .goog-menu { margin-top: -1px; width: 219px; z-index: 1000; =
}

.goog-combobox-button { cursor: pointer; display: inline-block; font-size: =
10px; text-align: center; width: 16px; }

* html .goog-combobox-button { padding: 0px 3px; }

.goog-inline-block { position: relative; display: inline-block; }

* html .goog-inline-block { display: inline; }

:first-child + html .goog-inline-block { display: inline; }

.goog-menubar { cursor: default; outline: none; position: relative; white-s=
pace: nowrap; background: rgb(255, 255, 255); }

.goog-menubar .goog-menu-button { padding: 1px; margin: 0px; outline: none;=
 background: rgb(255, 255, 255); border: 1px solid rgb(255, 255, 255); }

.goog-menubar .goog-menu-button-dropdown { display: none; }

.goog-menubar .goog-menu-button-inner-box, .goog-menubar .goog-menu-button-=
outer-box { border: none; }

.goog-menubar .goog-menu-button-hover { background: rgb(238, 238, 238); bor=
der: 1px solid rgb(238, 238, 238); }

.goog-menubar .goog-menu-button-open { background: rgb(255, 255, 255); bord=
er-left: 1px solid rgb(204, 204, 204); border-right: 1px solid rgb(204, 204=
, 204); }

.goog-menubar .goog-menu-button-disabled { color: rgb(204, 204, 204); }

.goog-menu-button { background: url("//ssl.gstatic.com/editor/button-bg.png=
") 0px 0px repeat-x rgb(221, 221, 221); border: 0px; color: rgb(0, 0, 0); c=
ursor: pointer; list-style: none; margin: 2px; outline: none; padding: 0px;=
 text-decoration: none; vertical-align: middle; }

.goog-menu-button-inner-box, .goog-menu-button-outer-box { border-style: so=
lid; border-color: rgb(170, 170, 170); vertical-align: top; }

.goog-menu-button-outer-box { margin: 0px; border-width: 1px 0px; padding: =
0px; }

.goog-menu-button-inner-box { margin: 0px -1px; border-width: 0px 1px; padd=
ing: 3px 4px; }

* html .goog-menu-button-inner-box { left: -1px; }

* html .goog-menu-button-rtl .goog-menu-button-outer-box { left: -1px; righ=
t: auto; }

* html .goog-menu-button-rtl .goog-menu-button-inner-box { right: auto; }

:first-child + html .goog-menu-button-inner-box { left: -1px; }

:first-child + html .goog-menu-button-rtl .goog-menu-button-inner-box { lef=
t: 1px; right: auto; }

.goog-menu-button-disabled { background-image: none !important; opacity: 0.=
3; }

.goog-menu-button-disabled .goog-menu-button-caption, .goog-menu-button-dis=
abled .goog-menu-button-dropdown, .goog-menu-button-disabled .goog-menu-but=
ton-inner-box, .goog-menu-button-disabled .goog-menu-button-outer-box { col=
or: rgb(51, 51, 51) !important; border-color: rgb(153, 153, 153) !important=
; }

* html .goog-menu-button-disabled { margin: 2px 1px !important; padding: 0p=
x 1px !important; }

:first-child + html .goog-menu-button-disabled { margin: 2px 1px !important=
; padding: 0px 1px !important; }

.goog-menu-button-hover .goog-menu-button-inner-box, .goog-menu-button-hove=
r .goog-menu-button-outer-box { border-color: rgb(153, 204, 255) rgb(102, 1=
53, 238) rgb(102, 153, 238) rgb(119, 170, 255) !important; }

.goog-menu-button-active, .goog-menu-button-open { background-color: rgb(18=
7, 187, 187); background-position: 0px 100%; }

.goog-menu-button-focused .goog-menu-button-inner-box, .goog-menu-button-fo=
cused .goog-menu-button-outer-box { border-color: orange; }

.goog-menu-button-caption { padding: 0px 4px 0px 0px; vertical-align: top; =
}

.goog-menu-button-dropdown { height: 15px; width: 7px; background: url("//s=
sl.gstatic.com/editor/editortoolbar.png") -388px 0px no-repeat; vertical-al=
ign: top; }

.goog-menu-button-collapse-right, .goog-menu-button-collapse-right .goog-me=
nu-button-inner-box, .goog-menu-button-collapse-right .goog-menu-button-out=
er-box { margin-right: 0px; }

.goog-menu-button-collapse-left, .goog-menu-button-collapse-left .goog-menu=
-button-inner-box, .goog-menu-button-collapse-left .goog-menu-button-outer-=
box { margin-left: 0px; }

.goog-menu-button-collapse-left .goog-menu-button-inner-box { border-left: =
1px solid rgb(255, 255, 255); }

.goog-menu-button-collapse-left.goog-menu-button-checked .goog-menu-button-=
inner-box { border-left: 1px solid rgb(221, 221, 221); }

.goog-submenu-arrow { color: rgb(0, 0, 0); padding-right: 6px; right: 0px; =
}

.goog-menuitem-rtl .goog-submenu-arrow { text-align: left; left: 0px; right=
: auto; padding-left: 6px; }

.goog-menuitem-disabled .goog-submenu-arrow { color: rgb(204, 204, 204); }

.goog-tab { position: relative; padding: 4px 8px; color: rgb(0, 0, 204); te=
xt-decoration: underline; cursor: default; }

.goog-tab-bar-top .goog-tab { margin: 1px 4px 0px 0px; border-bottom: 0px; =
float: left; }

.goog-tab-bar-bottom::after, .goog-tab-bar-top::after { content: " "; displ=
ay: block; height: 0px; clear: both; visibility: hidden; }

.goog-tab-bar-bottom .goog-tab { margin: 0px 4px 1px 0px; border-top: 0px; =
float: left; }

.goog-tab-bar-start .goog-tab { margin: 0px 0px 4px 1px; border-right: 0px;=
 }

.goog-tab-bar-end .goog-tab { margin: 0px 1px 4px 0px; border-left: 0px; }

.goog-tab-hover { background: rgb(238, 238, 238); }

.goog-tab-disabled { color: rgb(102, 102, 102); }

.goog-tab-selected { color: rgb(0, 0, 0); background: rgb(255, 255, 255); t=
ext-decoration: none; font-weight: 700; border: 1px solid rgb(107, 144, 218=
); }

.goog-tab-bar-top { padding-top: 5px !important; padding-left: 5px !importa=
nt; border-bottom: 1px solid rgb(107, 144, 218) !important; }

.goog-tab-bar-top .goog-tab-selected { top: 1px; margin-top: 0px; padding-b=
ottom: 5px; }

.goog-tab-bar-bottom .goog-tab-selected { top: -1px; margin-bottom: 0px; pa=
dding-top: 5px; }

.goog-tab-bar-start .goog-tab-selected { left: 1px; margin-left: 0px; paddi=
ng-right: 9px; }

.goog-tab-bar-end .goog-tab-selected { left: -1px; margin-right: 0px; paddi=
ng-left: 9px; }

.goog-tab-bar { margin: 0px; border: 0px; padding: 0px; list-style: none; c=
ursor: default; outline: none; background: rgb(235, 239, 249); }

.goog-tab-bar-clear { clear: both; height: 0px; overflow: hidden; }

.goog-tab-bar-start { float: left; }

.goog-tab-bar-end { float: right; }

* html .goog-tab-bar-start { margin-right: -3px; }

* html .goog-tab-bar-end { margin-left: -3px; }

.goog-toolbar { background: url("//ssl.gstatic.com/editor/toolbar-bg.png") =
0px 100% repeat-x rgb(250, 250, 250); border-bottom: 1px solid rgb(213, 213=
, 213); cursor: default; font: 12px Arial, sans-serif; margin: 0px; outline=
: none; padding: 2px; position: relative; zoom: 1; }

.goog-toolbar-button { margin: 0px 2px; border: 0px; padding: 0px; font-fam=
ily: Arial, sans-serif; color: rgb(51, 51, 51); text-decoration: none; list=
-style: none; vertical-align: middle; cursor: default; outline: none; }

.goog-toolbar-button-inner-box, .goog-toolbar-button-outer-box { border: 0p=
x; vertical-align: top; }

.goog-toolbar-button-outer-box { margin: 0px; padding: 1px 0px; }

.goog-toolbar-button-inner-box { margin: 0px -1px; padding: 3px 4px; }

* html .goog-toolbar-button-inner-box { left: -1px; }

* html .goog-toolbar-button-rtl .goog-toolbar-button-outer-box { left: -1px=
; }

* html .goog-toolbar-button-rtl .goog-toolbar-button-inner-box { right: aut=
o; }

:first-child + html .goog-toolbar-button-inner-box { left: -1px; }

:first-child + html .goog-toolbar-button-rtl .goog-toolbar-button-inner-box=
 { left: 1px; right: auto; }

.goog-toolbar-button-disabled { opacity: 0.3; }

.goog-toolbar-button-disabled .goog-toolbar-button-inner-box, .goog-toolbar=
-button-disabled .goog-toolbar-button-outer-box { color: rgb(51, 51, 51) !i=
mportant; border-color: rgb(153, 153, 153) !important; }

* html .goog-toolbar-button-disabled { background-color: rgb(240, 240, 240)=
; margin: 0px 1px; padding: 0px 1px; }

:first-child + html .goog-toolbar-button-disabled { background-color: rgb(2=
40, 240, 240); margin: 0px 1px; padding: 0px 1px; }

.goog-toolbar-button-active .goog-toolbar-button-outer-box, .goog-toolbar-b=
utton-checked .goog-toolbar-button-outer-box, .goog-toolbar-button-hover .g=
oog-toolbar-button-outer-box, .goog-toolbar-button-selected .goog-toolbar-b=
utton-outer-box { border-width: 1px 0px; border-style: solid; padding: 0px;=
 }

.goog-toolbar-button-active .goog-toolbar-button-inner-box, .goog-toolbar-b=
utton-checked .goog-toolbar-button-inner-box, .goog-toolbar-button-hover .g=
oog-toolbar-button-inner-box, .goog-toolbar-button-selected .goog-toolbar-b=
utton-inner-box { border-width: 0px 1px; border-style: solid; padding: 3px;=
 }

.goog-toolbar-button-hover .goog-toolbar-button-inner-box, .goog-toolbar-bu=
tton-hover .goog-toolbar-button-outer-box { border-color: rgb(161, 186, 223=
) !important; }

.goog-toolbar-button-active, .goog-toolbar-button-checked, .goog-toolbar-bu=
tton-selected { background-color: rgb(221, 225, 235) !important; }

.goog-toolbar-button-active .goog-toolbar-button-inner-box, .goog-toolbar-b=
utton-active .goog-toolbar-button-outer-box, .goog-toolbar-button-checked .=
goog-toolbar-button-inner-box, .goog-toolbar-button-checked .goog-toolbar-b=
utton-outer-box, .goog-toolbar-button-selected .goog-toolbar-button-inner-b=
ox, .goog-toolbar-button-selected .goog-toolbar-button-outer-box { border-c=
olor: rgb(114, 155, 209); }

.goog-toolbar-button-collapse-right, .goog-toolbar-button-collapse-right .g=
oog-toolbar-button-inner-box, .goog-toolbar-button-collapse-right .goog-too=
lbar-button-outer-box { margin-right: 0px; }

.goog-toolbar-button-collapse-left, .goog-toolbar-button-collapse-left .goo=
g-toolbar-button-inner-box, .goog-toolbar-button-collapse-left .goog-toolba=
r-button-outer-box { margin-left: 0px; }

* html .goog-toolbar-button-collapse-left .goog-toolbar-button-inner-box { =
left: 0px; }

:first-child + html .goog-toolbar-button-collapse-left .goog-toolbar-button=
-inner-box { left: 0px; }

.goog-toolbar-menu-button { margin: 0px 2px; border: 0px; padding: 0px; fon=
t-family: Arial, sans-serif; color: rgb(51, 51, 51); text-decoration: none;=
 list-style: none; vertical-align: middle; cursor: default; outline: none; =
}

.goog-toolbar-menu-button-inner-box, .goog-toolbar-menu-button-outer-box { =
border: 0px; vertical-align: top; }

.goog-toolbar-menu-button-outer-box { margin: 0px; padding: 1px 0px; }

.goog-toolbar-menu-button-inner-box { margin: 0px -1px; padding: 3px 4px; }

* html .goog-toolbar-menu-button-inner-box { left: -1px; }

* html .goog-toolbar-menu-button-rtl .goog-toolbar-menu-button-outer-box { =
left: -1px; }

* html .goog-toolbar-menu-button-rtl .goog-toolbar-menu-button-inner-box { =
right: auto; }

:first-child + html .goog-toolbar-menu-button-inner-box { left: -1px; }

:first-child + html .goog-toolbar-menu-button-rtl .goog-toolbar-menu-button=
-inner-box { left: 1px; right: auto; }

.goog-toolbar-menu-button-disabled { opacity: 0.3; }

.goog-toolbar-menu-button-disabled .goog-toolbar-menu-button-inner-box, .go=
og-toolbar-menu-button-disabled .goog-toolbar-menu-button-outer-box { color=
: rgb(51, 51, 51) !important; border-color: rgb(153, 153, 153) !important; =
}

* html .goog-toolbar-menu-button-disabled { background-color: rgb(240, 240,=
 240); margin: 0px 1px; padding: 0px 1px; }

:first-child + html .goog-toolbar-menu-button-disabled { background-color: =
rgb(240, 240, 240); margin: 0px 1px; padding: 0px 1px; }

.goog-toolbar-menu-button-active .goog-toolbar-menu-button-outer-box, .goog=
-toolbar-menu-button-hover .goog-toolbar-menu-button-outer-box, .goog-toolb=
ar-menu-button-open .goog-toolbar-menu-button-outer-box { border-width: 1px=
 0px; border-style: solid; padding: 0px; }

.goog-toolbar-menu-button-active .goog-toolbar-menu-button-inner-box, .goog=
-toolbar-menu-button-hover .goog-toolbar-menu-button-inner-box, .goog-toolb=
ar-menu-button-open .goog-toolbar-menu-button-inner-box { border-width: 0px=
 1px; border-style: solid; padding: 3px; }

.goog-toolbar-menu-button-hover .goog-toolbar-menu-button-inner-box, .goog-=
toolbar-menu-button-hover .goog-toolbar-menu-button-outer-box { border-colo=
r: rgb(161, 186, 223) !important; }

.goog-toolbar-menu-button-active, .goog-toolbar-menu-button-open { backgrou=
nd-color: rgb(221, 225, 235) !important; }

.goog-toolbar-menu-button-active .goog-toolbar-menu-button-inner-box, .goog=
-toolbar-menu-button-active .goog-toolbar-menu-button-outer-box, .goog-tool=
bar-menu-button-open .goog-toolbar-menu-button-inner-box, .goog-toolbar-men=
u-button-open .goog-toolbar-menu-button-outer-box { border-color: rgb(114, =
155, 209); }

.goog-toolbar-menu-button-caption { padding: 0px 4px 0px 0px; vertical-alig=
n: middle; }

.goog-toolbar-menu-button-dropdown { width: 7px; background: url("//ssl.gst=
atic.com/editor/editortoolbar.png") -388px 0px no-repeat; vertical-align: m=
iddle; }

.goog-toolbar-separator { margin: 0px 2px; border-left: 1px solid rgb(214, =
214, 214); border-right: 1px solid rgb(247, 247, 247); padding: 0px; width:=
 0px; text-decoration: none; list-style: none; outline: none; vertical-alig=
n: middle; line-height: normal; font-size: 120%; overflow: hidden; }

.goog-toolbar-select .goog-toolbar-menu-button-outer-box { border-width: 1p=
x 0px; border-style: solid; padding: 0px; }

.goog-toolbar-select .goog-toolbar-menu-button-inner-box { border-width: 0p=
x 1px; border-style: solid; padding: 3px; }

.goog-toolbar-select .goog-toolbar-menu-button-inner-box, .goog-toolbar-sel=
ect .goog-toolbar-menu-button-outer-box { border-color: rgb(191, 203, 223);=
 }

.goog-tree-root:focus { outline: none; }

.goog-tree-row { white-space: nowrap; font-style: ; font-variant: normal; f=
ont-weight: ; font-stretch: ; font-size: ; font-family: ; font-optical-sizi=
ng: ; font-size-adjust: ; font-kerning: ; font-feature-settings: ; font-var=
iation-settings: ; font-language-override: ; line-height: 16px; height: 16p=
x; }

.goog-tree-row span { overflow: hidden; text-overflow: ellipsis; }

.goog-tree-children { background-repeat: repeat-y; font: icon; background-i=
mage: url("//ssl.gstatic.com/closure/tree/I.png") !important; background-po=
sition-y: 1px !important; }

.goog-tree-children-nolines { font: icon; }

.goog-tree-icon { background-image: url("//ssl.gstatic.com/closure/tree/tre=
e.png"); }

.goog-tree-expand-icon { vertical-align: middle; height: 16px; width: 16px;=
 cursor: default; }

.goog-tree-expand-icon-plus { width: 19px; background-position: 0px 0px; }

.goog-tree-expand-icon-minus { width: 19px; background-position: -24px 0px;=
 }

.goog-tree-expand-icon-tplus { width: 19px; background-position: -48px 0px;=
 }

.goog-tree-expand-icon-tminus { width: 19px; background-position: -72px 0px=
; }

.goog-tree-expand-icon-lplus { width: 19px; background-position: -96px 0px;=
 }

.goog-tree-expand-icon-lminus { width: 19px; background-position: -120px 0p=
x; }

.goog-tree-expand-icon-t { width: 19px; background-position: -144px 0px; }

.goog-tree-expand-icon-l { width: 19px; background-position: -168px 0px; }

.goog-tree-expand-icon-blank { width: 19px; background-position: -168px -24=
px; }

.goog-tree-collapsed-folder-icon { vertical-align: middle; height: 16px; wi=
dth: 16px; background-position: 0px -24px; }

.goog-tree-expanded-folder-icon { vertical-align: middle; height: 16px; wid=
th: 16px; background-position: -24px -24px; }

.goog-tree-file-icon { vertical-align: middle; height: 16px; width: 16px; b=
ackground-position: -48px -24px; }

.goog-tree-item-label { margin-left: 3px; padding: 1px 2px; text-decoration=
: none; color: windowtext; cursor: default; }

.goog-tree-item-label:hover { text-decoration: underline; }

.selected .goog-tree-item-label { background-color: buttonface; color: butt=
ontext; }

.focused .selected .goog-tree-item-label { background-color: highlight; col=
or: highlighttext; }

.goog-tree-hide-root { display: none; }

html { --colab-dialog-bg-z-index: 1001; --colab-dialog-z-index: 1002; --col=
ab-above-dialog-z-index: 1003; --colab-below-dialog-bg-z-index: 1000; --col=
ab-survey-z-index: 1000; --colab-border-color: #c4c7c5; --colab-border-colo=
r-rgb: 196,199,197; --colab-bold-border-color: #747775; --colab-soft-border=
-color: rgba(var(--colab-border-color-rgb),0.4); --colab-divider-color: #e1=
e3e1; --colab-highlight-color: #ffe07c; --colab-highlight-color-rgb: 255,22=
4,124; --colab-comment-highlight-color: #ffe082; --colab-debugger-highlight=
-color: #ffdadc; --colab-smartpaste-highlight-color: rgba(255,224,130,.5); =
--colab-inverse-primary-color: #a8c7fa; --colab-inverse-surface-color: #303=
030; --colab-inverse-on-surface-color: #f2f2f2; --colab-primary-container-c=
olor: #d3e3fd; --colab-on-primary-container-color: #0842a0; --colab-primary=
-surface-color: #fff; --colab-surface-container-color: #f0f4f9; --colab-sur=
face-container-high-color: #e9eef6; --colab-surface-container-highest-color=
: #dde3ea; --colab-surface-container-low-color: #f8fafd; --colab-primary-te=
xt-color: #1f1f1f; --colab-primary-text-color-rgb: 31,31,31; --colab-second=
ary-text-color: #444746; --colab-secondary-container-color: #c2e7ff; --cola=
b-on-secondary-container-color: #004a77; --colab-secondary-surface-color: #=
f2f2f2; --colab-primary-color: #0b57d0; --colab-primary-color-rgb: 11,87,20=
8; --colab-on-primary-color: #fff; --colab-error-color: #b3261e; --colab-er=
ror-container-color: #f9dedc; --colab-on-error-container-color: #8c1d18; --=
colab-diff-editor-background: #fff; --colab-composer-diff-background: #acee=
bb; --colab-local-diff-background: #eef; --colab-remote-diff-background: #f=
effe0; --colab-merged-diff-background: #d7fed8; --colab-success-color: #128=
937; --colab-warning-color: #c05a01; --colab-warning-container-color: #fff2=
b4; --colab-on-warning-container-color: #6d3a01; --ansi-black: #000; --ansi=
-red: #8b0000; --ansi-green: #006400; --ansi-yellow: #cdcd00; --ansi-blue: =
#00e; --ansi-magenta: #cd00cd; --ansi-cyan: #4682b4; --ansi-gray: #e5e5e5; =
--ansi-bright-black: #7f7f7f; --ansi-bright-red: red; --ansi-bright-green: =
#00d000; --ansi-bright-yellow: #ff0; --ansi-bright-blue: #5c5cff; --ansi-br=
ight-magenta: #f0f; --ansi-bright-cyan: #0ff; --ansi-bright-gray: #fff; --c=
olab-logo-dark: #e8710a; --colab-logo-light: #f9ab00; --colab-chrome-font-f=
amily: "Google Sans Text","Google Sans","Noto",sans-serif; --colab-google-s=
ans-font-family: "Google Sans","Roboto","Noto",sans-serif; --colab-chrome-f=
ont-size: 14px; --colab-debugger-breakpoint-color: #db372d; --colab-code-fo=
nt-family: monospace; --colab-code-font-size: 14px; --colab-anchor-color: v=
ar(--colab-primary-color); --colab-disabled-border-color: rgba(var(--colab-=
primary-text-color-rgb),0.12); --colab-disabled-text-color: rgba(var(--cola=
b-primary-text-color-rgb),0.38); --colab-editor-background: var(--colab-pri=
mary-surface-color); --colab-focus-ring-color: var(--colab-primary-color); =
--colab-highlighted-surface-color: rgba(var(--colab-primary-text-color-rgb)=
,0.08); --colab-icon-color: var(--colab-secondary-text-color); --colab-scro=
llbar-color: rgba(var(--colab-primary-text-color-rgb),0.24); --colab-scroll=
bar-hover-color: rgba(var(--colab-primary-text-color-rgb),0.48); --colab-sc=
rollbar-active-color: rgba(var(--colab-primary-text-color-rgb),0.48); --col=
ab-soft-highlight-color: rgba(var(--colab-highlight-color-rgb),0.24); --mdc=
-button-disabled-ink-color: var(--colab-disabled-text-color); --mdc-button-=
outline-color: var(--colab-border-color); --mdc-checkbox-checked-color: var=
(--colab-primary-color); --mdc-checkbox-disabled-color: var(--colab-disable=
d-text-color); --mdc-checkbox-ink-color: var(--colab-primary-surface-color)=
; --mdc-checkbox-ripple-size: 36px; --mdc-checkbox-state-layer-size: 36px; =
--mdc-checkbox-unchecked-color: var(--colab-primary-text-color); --mdc-dial=
og-content-ink-color: var(--colab-primary-text-color); --mdc-dialog-heading=
-ink-color: var(--colab-primary-text-color); --mdc-dialog-z-index: var(--co=
lab-above-dialog-z-index); --mdc-icon-font: "Google Symbols"; --mdc-menu-z-=
index: 11; --mdc-radio-unchecked-color: var(--colab-primary-text-color); --=
mdc-radio-disabled-color: var(--colab-disabled-text-color); --mdc-ripple-pr=
ess-opacity: 0.03; --mdc-ripple-focus-opacity: 0.07; --mdc-select-label-ink=
-color: var(--colab-secondary-text-color); --mdc-select-fill-color: var(--c=
olab-primary-surface-color); --mdc-select-ink-color: var(--colab-primary-te=
xt-color); --mdc-select-dropdown-icon-color: var(--colab-icon-color); --mdc=
-select-hover-line-color: var(--colab-bold-border-color); --mdc-select-idle=
-line-color: var(--colab-border-color); --mdc-select-outlined-idle-border-c=
olor: var(--colab-border-color); --mdc-select-outlined-hover-border-color: =
var(--colab-bold-border-color); --mdc-select-outlined-disabled-border-color=
: var(
    --colab-disabled-text-color
  ); --mdc-text-field-disabled-fill-color: transparent; --mdc-text-field-di=
sabled-ink-color: var(--colab-primary-text-color); --mdc-text-field-fill-co=
lor: var(--colab-secondary-surface-color); --mdc-text-field-hover-line-colo=
r: var(--colab-primary-color); --mdc-text-field-idle-line-color: var(--cola=
b-primary-text-color); --mdc-text-field-ink-color: var(--colab-primary-text=
-color); --mdc-text-field-label-ink-color: var(--colab-secondary-text-color=
); --mdc-text-field-outlined-idle-border-color: var(--colab-border-color); =
--mdc-text-field-outlined-hover-border-color: var(
    --colab-bold-border-color
  ); --mdc-theme-error: var(--colab-error-color); --mdc-theme-primary: var(=
--colab-primary-color); --mdc-theme-on-primary: var(--colab-primary-surface=
-color); --mdc-theme-surface: var(--colab-primary-surface-color); --mdc-the=
me-on-surface: var(--colab-primary-text-color); --mdc-theme-text-disabled-o=
n-light: var(--colab-disabled-text-color); --mdc-theme-text-hint-on-backgro=
und: var(--colab-primary-text-color); --mdc-theme-text-primary-on-backgroun=
d: var(--colab-primary-text-color); --mdc-theme-text-secondary-on-backgroun=
d: var(--colab-primary-text-color); --mdc-typography-body1-font-size: var(-=
-colab-chrome-font-size); --mdc-typography-body1-letter-spacing: normal; --=
mdc-typography-button-letter-spacing: normal; --mdc-typography-button-text-=
transform: none; --mdc-typography-font-family: var(--colab-chrome-font-fami=
ly); --mdc-typography-subtitle1-font-size: var(--colab-chrome-font-size); -=
-mdc-typography-subtitle1-letter-spacing: normal; --md-checkbox-outline-col=
or: var(--colab-primary-text-color); --md-dialog-container-color: var(--col=
ab-primary-surface-color); --md-dialog-headline-font: var(--colab-google-sa=
ns-font-family); --md-dialog-supporting-text-color: var(--colab-primary-tex=
t-color); --md-dialog-supporting-text-font: var(--colab-chrome-font-family)=
; --md-dialog-supporting-text-size: var(--colab-chrome-font-size); --md-ele=
vated-button-leading-space: 16px; --md-elevated-button-trailing-space: 16px=
; --md-filled-button-label-text-size: var(--colab-chrome-font-size); --md-f=
illed-button-container-height: 36px; --md-filled-button-leading-space: 16px=
; --md-filled-button-trailing-space: 16px; --md-filled-button-disabled-cont=
ainer-opacity: 0.06; --md-filled-button-disabled-label-text-color: var(
    --colab-secondary-text-color
  ); --md-filled-button-disabled-label-text-opacity: 1; --md-filled-text-fi=
eld-label-text-size: var(--colab-chrome-font-size); --md-filled-tonal-butto=
n-with-leading-icon-trailing-space: 20px; --md-focus-ring-color: var(--cola=
b-focus-ring-color); --md-focus-ring-width: 2px; --md-icon-button-hover-sta=
te-layer-opacity: 0.08; --md-icon-button-pressed-state-layer-opacity: 0.12;=
 --md-icon-button-state-layer-shape: 9999px; --md-icon-font: "Google Symbol=
s"; --md-list-container-color: transparent; --md-menu-item-selected-contain=
er-color: var(
    --colab-highlighted-surface-color
  ); --md-menu-item-selected-label-text-color: var(--colab-primary-text-col=
or); --md-menu-item-label-text-size: 14px; --md-menu-item-one-line-containe=
r-height: 1.25rem; --md-menu-item-top-space: 0.25rem; --md-menu-item-bottom=
-space: 0.25rem; --md-outlined-button-container-height: 36px; --md-outlined=
-button-label-text-size: var(--colab-chrome-font-size); --md-outlined-butto=
n-pressed-state-layer-opacity: 0.03; --md-outlined-select-text-field-focus-=
outline-width: 2px; --md-outlined-text-field-focus-outline-width: 2px; --md=
-outlined-text-field-label-text-size: var(--colab-chrome-font-size); --md-r=
ef-typeface-plain: var(--colab-chrome-font-family); --md-slider-active-trac=
k-color: var(--colab-border-color); --md-slider-active-track-height: 2px; -=
-md-slider-disabled-active-track-opacity: 0.12; --md-slider-disabled-inacti=
ve-track-opacity: 0.12; --md-slider-inactive-track-color: var(--colab-borde=
r-color); --md-slider-inactive-track-height: 2px; --md-slider-handle-elevat=
ion: 0; --md-slider-handle-height: 16px; --md-slider-handle-width: 16px; --=
md-switch-with-icon-handle-height: 18px; --md-switch-with-icon-handle-width=
: 18px; --md-switch-selected-handle-height: 18px; --md-switch-selected-hand=
le-width: 18px; --md-switch-pressed-handle-height: 22px; --md-switch-presse=
d-handle-width: 22px; --md-switch-track-height: 26px; --md-switch-track-wid=
th: 40px; --md-sys-color-error: var(--colab-error-color); --md-sys-color-on=
-error-container: var(--colab-on-error-container-color); --md-sys-color-inv=
erse-surface: var(--colab-inverse-surface-color); --md-sys-color-inverse-on=
-surface: var(--colab-inverse-on-surface-color); --md-sys-color-on-surface:=
 var(--colab-primary-text-color); --md-sys-color-on-surface-variant: var(--=
colab-secondary-text-color); --md-sys-color-outline: var(--colab-bold-borde=
r-color); --md-sys-color-outline-variant: var(--colab-border-color); --md-s=
ys-color-primary: var(--colab-primary-color); --md-sys-color-on-primary: va=
r(--colab-on-primary-color); --md-sys-color-primary-container: var(--colab-=
primary-container-color); --md-sys-color-on-primary-container: var(
    --colab-on-primary-container-color
  ); --md-sys-color-secondary-container: var(--colab-secondary-container-co=
lor); --md-sys-color-on-secondary-container: var(
    --colab-on-secondary-container-color
  ); --md-sys-color-surface: var(--colab-primary-surface-color); --md-sys-c=
olor-surface-container: var(--colab-primary-surface-color); --md-sys-color-=
surface-container-highest: var(
    --colab-secondary-surface-color
  ); --md-sys-color-surface-container-high: var(
    --colab-surface-container-high-color
  ); --md-sys-color-surface-container-low: var(
    --colab-surface-container-low-color
  ); --md-text-button-container-height: 36px; --md-text-button-pressed-stat=
e-layer-opacity: 0.03; }

html.embedded { --colab-logo-dark: #3367d6; --colab-logo-light: #3b78e7; }

html[theme=3D"dark"] { --colab-border-color: #444746; --colab-border-color-=
rgb: 68,71,70; --colab-bold-border-color: #8e918f; --colab-soft-border-colo=
r: rgba(var(--colab-border-color-rgb),0.5); --colab-divider-color: #444746;=
 --colab-highlight-color: #8f4e06; --colab-highlight-color-rgb: 143,78,6; -=
-colab-comment-highlight-color: #1a237e; --colab-debugger-highlight-color: =
#b3251e; --colab-smartpaste-highlight-color: rgba(255,224,130,.3); --colab-=
inverse-primary-color: #0b57d0; --colab-inverse-surface-color: #e3e3e3; --c=
olab-inverse-on-surface-color: #303030; --colab-primary-container-color: #0=
842a0; --colab-on-primary-container-color: #d3e3fd; --colab-primary-surface=
-color: #282a2c; --colab-surface-container-color: #1e1f20; --colab-surface-=
container-high-color: #333537; --colab-surface-container-highest-color: #37=
393b; --colab-surface-container-low-color: #131314; --colab-primary-text-co=
lor: #e3e3e3; --colab-primary-text-color-rgb: 227,227,227; --colab-secondar=
y-text-color: #c4c7c5; --colab-secondary-container-color: #004a77; --colab-=
on-secondary-container-color: #c2e7ff; --colab-secondary-surface-color: #47=
4747; --colab-primary-color: #a8c7fa; --colab-primary-color-rgb: 168,199,25=
0; --colab-on-primary-color: #062e6f; --colab-error-color: #f2b8b5; --colab=
-error-container-color: #8c1d18; --colab-on-error-container-color: #f9dedc;=
 --colab-diff-editor-background: #000; --colab-composer-diff-background: #2=
34521; --colab-local-diff-background: #292935; --colab-remote-diff-backgrou=
nd: #2e2f08; --colab-merged-diff-background: #09380b; --colab-success-color=
: #44c265; --colab-warning-color: #fcbd00; --colab-warning-container-color:=
 #6d3a01; --colab-on-warning-container-color: #fff2b4; --ansi-black: #7f7f7=
f; --ansi-red: #ff7a88; --ansi-green: #57bb8a; --ansi-yellow: #ff6; --ansi-=
blue: #82b1ff; --ansi-magenta: #cd00cd; --ansi-cyan: #99bbd7; --ansi-gray: =
#e5e5e5; --ansi-bright-green: #0f0; }

html[theme=3D"dark"].embedded { --colab-editor-background: #000; --colab-se=
condary-surface-color: #202124; --colab-highlighted-surface-color: #202124;=
 --colab-border-color: #3c4043; --colab-border-color-rgb: 60,64,67; }

html[editor=3D"Classic Dark"] { --colab-editor-background: #1e1e1e; }

html[editor=3D"High Contrast Dark"] { --colab-editor-background: #000; }

html[editor=3D"Monokai"] { --colab-editor-background: #272822; }

html[editor=3D"All Hallows Eve"] { --colab-editor-background: #000; }

html[editor=3D"Amy"] { --colab-editor-background: #200020; }

html[editor=3D"Birds Of Paradise"] { --colab-editor-background: #372725; }

html[editor=3D"Blackboard"] { --colab-editor-background: #0c1021; }

html[editor=3D"Clouds Midnight"] { --colab-editor-background: #191919; }

html[editor=3D"Dominion Day"] { --colab-editor-background: #372725; }

html[editor=3D"Espresso Libre"] { --colab-editor-background: #2a211c; }

html[editor=3D"Merbivore"] { --colab-editor-background: #161616; }

html[editor=3D"Night Owl"] { --colab-editor-background: #011627; }

html[editor=3D"Oceanic Next"] { --colab-editor-background: #1b2b34; }

html[editor=3D"Pastels On Dark"] { --colab-editor-background: #211e1e; }

html[editor=3D"Space Cadet"] { --colab-editor-background: #0d0d0d; }

html[editor=3D"Sunburst"] { --colab-editor-background: #000; }

html[editor=3D"Twilight"] { --colab-editor-background: #141414; }

html[editor=3D"Vibrant Ink"] { --colab-editor-background: #000; }

html[editor=3D"Zenburnesque"] { --colab-editor-background: #404040; }

html[editor=3D"Idle Fingers"] { --colab-editor-background: #323232; }

html[editor=3D"Mono Industrial"] { --colab-editor-background: #222c28; }

html[editor=3D"Synthwave84"] { --colab-border-color: rgba(112,89,171,.4); -=
-colab-border-color-rgb: 112,89,171; --colab-primary-surface-color: #262335=
; --colab-secondary-surface-color: #49549539; --colab-surface-container-col=
or: #241b2f; --colab-surface-container-high-color: #2a2139; --colab-surface=
-container-highest-color: #34294f; --colab-surface-container-low-color: #17=
1520; --colab-editor-background: #262335; --colab-highlighted-surface-color=
: #37294d99; --colab-anchor-color: #f97e72; --ansi-red: #fe4450; --ansi-gre=
en: #72f1b8; --ansi-yellow: #f97e72; --ansi-blue: #03edf9; --ansi-magenta: =
#ff7edb; --ansi-cyan: #03edf9; --ansi-bright-red: #fe4450; --ansi-bright-gr=
een: #72f1b8; --ansi-bright-yellow: #fede5d; --ansi-bright-blue: #03edf9; -=
-ansi-bright-magenta: #ff7edb; --ansi-bright-cyan: #03edf9; }

html[editor=3D"Classic Light"] { --colab-editor-background: #f7f7f7; }

html[editor=3D"Chrome DevTools"], html[editor=3D"Textmate (Mac Classic)"], =
html[editor=3D"Xcode Default"], html[editor=3D"Active4D"], html[editor=3D"C=
louds"], html[editor=3D"Dreamweaver"], html[editor=3D"Eiffel"], html[editor=
=3D"IDLE"], html[editor=3D"LAZY"], html[editor=3D"Tomorrow"] { --colab-edit=
or-background: #fff; }

html[editor=3D"Dawn"] { --colab-editor-background: #f9f9f9; }

html[editor=3D"GitHub"] { --colab-editor-background: #f8f8ff; }

html[editor=3D"Kuroir Theme"] { --colab-editor-background: #e8e9e8; }

html[editor=3D"Slush and Poppies"] { --colab-editor-background: #f1f1f1; }

html[editor=3D"Solarized Light"] { --colab-editor-background: #fdf6e3; }

html[editor=3D"iPlastic"] { --colab-editor-background: #eeeeeeeb; }

.code pre.editor.monaco { overflow: auto; white-space: nowrap; }

.cell pre.editor.monaco { margin: 0px; padding: 10px 8px; outline: none; }

colab-aida-message .markdown { --md-outlined-button-container-height: 28px;=
 --md-outlined-button-leading-space: 12px; --md-outlined-button-trailing-sp=
ace: 12px; --md-outlined-button-with-leading-icon-trailing-space: 12px; --m=
d-outlined-button-with-trailing-icon-leading-space: 12px; --md-outlined-but=
ton-with-leading-icon-leading-space: 8px; --md-outlined-button-with-trailin=
g-icon-trailing-space: 8px; --md-outlined-button-icon-size: 20px; }

colab-aida-message .markdown ol, colab-aida-message .markdown p, colab-aida=
-message .markdown ul { font-size: var(--colab-chrome-font-size); }

colab-aida-message .markdown > * { margin: 6px 0px; }

colab-aida-message .markdown .generated-code-warning { display: flex; -webk=
it-box-orient: vertical; -webkit-box-direction: normal; flex-direction: col=
umn; }

colab-aida-message .markdown .generated-code-warning pre { margin: 0px; }

colab-aida-message .markdown .generated-code-warning a { align-self: end; f=
ont-size: 0.8em; }

.converse.error { color: var(--colab-error-color); }

.chat-cursor { animation: 1.5s ease 0s infinite normal none running chat-cu=
rsor-blink; background: var(--colab-icon-color); display: inline-block; hei=
ght: 18px; width: 10px; }

@-webkit-keyframes chat-cursor-blink {=20
  0% { opacity: 0.1; }
  20% { opacity: 1; }
  80% { opacity: 1; }
  100% { opacity: 0.1; }
}

@keyframes chat-cursor-blink {=20
  0% { opacity: 0.1; }
  20% { opacity: 1; }
  80% { opacity: 1; }
  100% { opacity: 0.1; }
}

colab-differ { display: flex; -webkit-box-orient: vertical; -webkit-box-dir=
ection: normal; flex-direction: column; -webkit-box-flex: 1; flex-grow: 1; =
}

colab-differ .monaco-editor { --vscode-editor-background: var(--colab-diff-=
editor-background); }

colab-differ .monaco-diff-editor { -webkit-box-flex: 1; flex-grow: 1; }

.differ { min-height: 300px; }

colab-differ .diff-annotation, colab-differ .diff-output, colab-differ .dif=
f-title { color: var(--colab-primary-text-color); white-space: nowrap; }

colab-differ .diff-annotation, colab-differ .diff-title { font-weight: 700;=
 }

.notebook-diff-titlebar { flex-shrink: 0; padding: 8px 8px 0px; }

.notebook-diff-options { padding-left: 8px; }

.notebook-diff-dialog .notebook-diff-options { padding: 8px 8px 0px; }

.notebook-diff-options label:has(md-checkbox) { margin-left: 16px; margin-t=
op: 2px; }

.notebook-diff-container { display: flex; -webkit-box-orient: vertical; -we=
bkit-box-direction: normal; flex-direction: column; -webkit-box-flex: 1; fl=
ex-grow: 1; justify-content: space-around; min-height: 300px; padding: 8px;=
 }

.notebook-diff-dialog mwc-circular-progress { display: none; }

.notebook-diff-dialog .diff-loading mwc-circular-progress { display: block;=
 margin: 0px auto; }

.notebook-diff-dialog { --mdc-dialog-max-width: 98vw; --mdc-dialog-min-widt=
h: 98vw; --mdc-dialog-max-height: 98vh; max-width: 98vw; min-width: 98vw; m=
ax-height: 98vh; }

.notebook-diff-dialog:not(.secure-save-diff-dialog) .content-area { display=
: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-d=
irection: column; height: calc(-150px + 98vh); }

.notebook-diff-dialog:not(.secure-save-diff-dialog) .content-area.dialog-ui=
-refresh { height: calc(-164px + 98vh); }

.secure-save-diff-dialog .content-area { min-height: 0px; max-width: 100%; =
}

.monaco-diff-editor .line-insert, .monaco-editor .line-insert { background-=
color: var(--vscode-diffEditor-insertedLineBackground,var(--vscode-diffEdit=
or-insertedTextBackground)) !important; }

.monaco-diff-editor .gutter-insert, .monaco-editor .gutter-insert, .monaco-=
editor .inline-added-margin-view-zone { background-color: var(--vscode-diff=
EditorGutter-insertedLineBackground,var(--vscode-diffEditor-insertedLineBac=
kground,var(--vscode-diffEditor-insertedTextBackground))) !important; }

.monaco-diff-editor .line-delete, .monaco-editor .line-delete { background-=
color: var(--vscode-diffEditor-removedLineBackground,var(--vscode-diffEdito=
r-removedTextBackground)) !important; }

.monaco-diff-editor .gutter-delete, .monaco-editor .gutter-delete, .monaco-=
editor .inline-deleted-margin-view-zone { background-color: var(--vscode-di=
ffEditorGutter-removedLineBackground,var(--vscode-diffEditor-removedLineBac=
kground,var(--vscode-diffEditor-removedTextBackground))) !important; }

colab-executions { display: flex; -webkit-box-orient: vertical; -webkit-box=
-direction: normal; flex-direction: column; height: 100%; }

colab-executions colab-scroller { -webkit-box-flex: 1; flex-grow: 1; overfl=
ow-y: scroll; }

colab-executions .cell-execution-indicator { display: block; }

colab-executions .input { background: var(--colab-editor-background); borde=
r: 1px solid var(--colab-border-color); border-radius: 8px; font-family: va=
r(--colab-code-font-family); overflow-x: auto; font-size: var(--colab-code-=
font-size); padding: 0px 8px; display: flex; flex-shrink: 0; margin: 4px; }

colab-executions .gutter { -webkit-box-align: center; align-items: center; =
position: relative; width: 36px; }

colab-executions .editor-host { background: var(--colab-editor-background);=
 -webkit-box-flex: 1; flex-grow: 1; padding-top: 10px; position: relative; =
}

colab-executions .editor-host .monaco-editor { position: absolute; }

colab-executions .execution-count { margin-top: 4px; text-align: center; }

colab-executions .code-placeholder { color: var(--colab-secondary-text-colo=
r); font-family: var(--colab-code-font-family); font-style: italic; left: 3=
0px; pointer-events: none; position: absolute; top: 12px; z-index: 1; }

colab-executions .code-placeholder.code-fold { left: 48px; }

colab-executions .hidden { display: none; }

colab-executions .executions-placeholder { color: var(--colab-secondary-tex=
t-color); margin: 8px 4px; }

colab-execution { display: block; }

colab-execution .code md-icon { cursor: pointer; height: 26px; transition: =
transform 0.2s, -webkit-transform 0.2s; }

colab-execution .code .gutter { display: flex; -webkit-box-orient: vertical=
; -webkit-box-direction: normal; flex-direction: column; flex-shrink: 0; }

colab-execution .execution-count { color: var(--colab-secondary-text-color)=
; cursor: default; font-family: var(--colab-code-font-family); }

colab-execution.collapsed .code md-icon { transform: rotate(-90deg); }

colab-execution .outputview, colab-execution colab-static-output-renderer {=
 margin-left: 36px; }

colab-execution iframe { border: 0px; width: 100%; }

colab-execution .code { display: flex; }

colab-execution .source { background: var(--colab-editor-background); borde=
r: 1px solid var(--colab-border-color); border-radius: 8px; font-family: va=
r(--colab-code-font-family); overflow-x: auto; font-size: var(--colab-code-=
font-size); padding: 8px; -webkit-box-flex: 1; flex-grow: 1; margin-right: =
4px; }

colab-execution.collapsed .source-lines > * { display: none; }

colab-execution.collapsed .source-lines > .preview { display: inline; }

colab-execution .start-time { color: var(--colab-secondary-text-color); fon=
t-size: 0.8em; margin: 8px 8px 0px 6px; }

colab-execution.selected { background: var(--colab-highlighted-surface-colo=
r); }

colab-execution .entry-action { --md-icon-button-state-layer-height: 28px; =
}

colab-interactive-table { display: block; position: relative; }

colab-interactive-table.collapsed-layout { display: inline-block; }

colab-interactive-table .google-visualization-table-table th { border-botto=
m: 1px solid var(--colab-bold-border-color); border-right: 1px solid var(--=
colab-border-color); }

colab-interactive-table .google-visualization-table-table { border-bottom: =
1px solid var(--colab-bold-border-color); border-left: 1px solid var(--cola=
b-border-color); }

colab-interactive-table .google-visualization-table-table tbody { border-bo=
ttom: 0px; }

colab-interactive-table .google-visualization-table .gradient, colab-intera=
ctive-table .google-visualization-table-table, colab-interactive-table .goo=
gle-visualization-table-table th, colab-interactive-table .google-visualiza=
tion-table-tr-head { background: none; }

colab-interactive-table .google-visualization-table-tr-odd { background-col=
or: var(--colab-secondary-surface-color); }

colab-interactive-table .google-visualization-table-tr-even { background-co=
lor: var(--colab-primary-surface-color); }

colab-interactive-table .google-visualization-table-tr-over, colab-interact=
ive-table .google-visualization-table-tr-sel { background-color: var(--cola=
b-highlighted-surface-color); }

colab-interactive-table .google-visualization-table-td:first-child::after {=
 content: ""; display: inline-block; }

colab-interactive-table .google-visualization-table-table td { border-color=
: var(--colab-border-color); vertical-align: top; }

colab-interactive-table .google-visualization-table-page-number { color: va=
r(--colab-primary-text-color); }

colab-interactive-table .google-visualization-table-div-page { background: =
none; text-align: right; }

colab-interactive-table .google-visualization-table-page-next, colab-intera=
ctive-table .google-visualization-table-page-prev { display: none; }

colab-interactive-table .google-visualization-table-page-number { border-ra=
dius: 3px; border: 1px solid transparent; box-sizing: border-box; display: =
inline-block; font-size: 11px; margin-left: 2px; min-width: 1.5em; padding:=
 0.5em 1em; text-align: center; }

colab-interactive-table .google-visualization-table-page-number.current { b=
ackground-color: var(--colab-primary-surface-color); border: 1px solid rgb(=
151, 151, 151); }

colab-interactive-table .google-visualization-table-page-number:hover { bac=
kground-color: rgb(88, 88, 88); color: rgb(255, 255, 255); }

colab-interactive-table .interactive-table-header { -webkit-box-align: cent=
er; align-items: center; display: flex; -webkit-box-pack: end; justify-cont=
ent: flex-end; padding-right: 2px; }

colab-interactive-table .display-count { margin-right: 8px; }

colab-interactive-table .collapsible-controls > div { border: 1px solid rgb=
(204, 204, 204); margin: 8px; padding: 8px; position: relative; }

colab-interactive-table .collapsible-controls .close { cursor: pointer; fon=
t-size: 16pt; position: absolute; right: 4px; top: 0px; }

colab-interactive-table button.close, colab-interactive-table button.copy-s=
how { background: none; border: none; color: var(--colab-icon-color); }

colab-interactive-table button.copy-show svg { fill: var(--colab-icon-color=
); height: 18px; width: 18px; }

colab-interactive-table .column-filters-container { display: grid; gap: 5px=
; grid-auto-rows: minmax(auto, 50px); grid-template-columns: repeat(auto-fi=
ll, minmax(300px, max-content)); }

colab-interactive-table .column-filter { display: inline-block; margin: 0px=
 32px 8px 0px; }

colab-interactive-table .column-filter label { display: block; }

colab-interactive-table .column-filter input[type=3D"text"][name=3D"from"],=
 colab-interactive-table .column-filter input[type=3D"text"][name=3D"to"] {=
 width: 70px; }

colab-interactive-table .num-per-page { float: left; margin-top: 2px; }

colab-interactive-table .goog-custom-button-outer-box { display: none; }

colab-interactive-table .help-anchor svg { fill: var(--colab-icon-color); h=
eight: 24px; margin-left: 8px; text-decoration: none; width: 24px; }

colab-interactive-table td.index_column { font-weight: 700; white-space: no=
wrap; }

colab-interactive-table .collapsible-controls textarea { min-height: 60px; =
width: 100%; }

colab-interactive-table select { background-color: var(--colab-primary-surf=
ace-color); color: var(--colab-primary-text-color); border-color: var(--col=
ab-bold-border-color); border-radius: 4px; }

.colab-left-pane-action { --md-focus-ring-outward-offset: -3px; }

colab-left-pane { display: flex; flex-shrink: 0; margin-top: 0px; min-width=
: 0px; will-change: opacity; }

.colab-left-pane-open { margin-right: 3px; }

colab-left-pane .resizer-contents { background-color: var(--colab-surface-c=
ontainer-color); border-radius: 24px; overflow: hidden; }

colab-left-pane .colab-left-pane-header { -webkit-box-align: center; align-=
items: center; gap: 2px; margin: 8px 8px 8px 20px; position: relative; }

colab-left-pane colab-resizer { flex-shrink: 1; min-width: 210px; max-width=
: 800px; width: 320px; }

colab-left-pane.has-user-secrets colab-resizer { width: 445px; }

colab-left-pane .left-pane-container, colab-left-pane .resizer-contents { d=
isplay: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; =
flex-flow: column; -webkit-box-flex: 1; flex-grow: 1; overflow: hidden; }

.left-pane-container { margin: 0px 20px 8px; }

body.mobile .notebook-vertical .colab-left-pane-nib { display: none; }

.colab-left-pane-nib .left-pane-top { background-color: var(--colab-surface=
-container-color); border-radius: 24px; display: flex; -webkit-box-orient: =
vertical; -webkit-box-direction: normal; flex-direction: column; -webkit-bo=
x-flex: 1; flex-grow: 1; gap: 4px; padding: 8px 4px; }

colab-left-pane .colab-left-pane-nib div { -webkit-box-flex: 1; flex-grow: =
1; }

.left-pane-content-title { -webkit-box-flex: 1; flex: 1 1 0%; font-family: =
var(--colab-google-sans-font-family); font-size: 16px; font-weight: 500; ma=
rgin: 0px; }

.colab-left-pane-nib { height: fit-content; margin-right: 8px; }

.colab-left-pane-nib md-icon-button { --md-focus-ring-outward-offset: -4px;=
 --md-sys-color-on-surface-variant: var(--colab-primary-text-color); }

.colab-left-pane-nib md-icon-button[selected] { background-color: var(--col=
ab-primary-container-color); border-radius: 9999px; --md-sys-color-primary:=
 var(--colab-on-secondary-container-color); }

@media (forced-colors: active) {
  .colab-left-pane-nib md-icon-button[selected] { --md-sys-color-primary: H=
ighlight; }
}

.left-pane-button { position: relative; }

colab-left-pane-notifier { bottom: 7px; cursor: pointer; position: absolute=
; right: 6px; }

.notebook-merge-dialog .content-area { min-height: 0px; max-width: 100%; pa=
dding: 0px; }

.notebook-merge-dialog colab-scroller { margin-top: 8px; overflow: auto; }

.merger-local-diff { background-color: var(--colab-local-diff-background); =
}

.merger-remote-diff { background-color: var(--colab-remote-diff-background)=
; }

.merger-merged-diff { background-color: var(--colab-merged-diff-background)=
; }

.local-merge-arrow, .remote-merge-arrow { cursor: pointer; }

.local-merge-arrow::after, .merger-gutter, .remote-merge-arrow::after { fon=
t-family: var(--colab-chrome-font-family); font-size: 16px; font-weight: 70=
0; }

.local-merge-arrow::after { content: "=E2=86=92"; }

.remote-merge-arrow::after { content: "=E2=86=90"; }

colab-merger-common { text-align: center; }

colab-cell-merger { display: block; margin: 20px; }

colab-cell-merger .cell { background: var(--colab-editor-background); borde=
r: 1px solid var(--colab-border-color); border-radius: 8px; font-family: va=
r(--colab-code-font-family); overflow-x: auto; font-size: var(--colab-code-=
font-size); padding: 8px; }

colab-merger .code .editor.monaco { margin: 0px; }

colab-merger .layout.vertical.edit { flex-shrink: 1; min-width: 0px; }

.colab-merger-output { flex-basis: 200px; -webkit-box-flex: 1; flex-grow: 1=
; }

.merger-gutter { padding-left: 1px; width: 36px; }

.merger-gutter div { cursor: pointer; }

.merger-status > div { -webkit-box-flex: 1; flex: 1 1 33%; font-weight: 700=
; min-width: 0px; overflow: hidden; text-align: center; }

.colab-open-dialog md-filled-button, .colab-open-dialog md-text-button { ma=
rgin: 10px; }

.colab-open-dialog md-filled-button.new-notebook { left: 0px; position: abs=
olute; top: 8px; -webkit-font-smoothing: antialiased; }

.colab-open-dialog colab-side-tab-dialog-page-viewer .open-github-notebook =
{ height: calc(100% - 10px); padding-top: 10px; }

.colab-open-dialog colab-github-repo-selector { margin-top: 8px; }

.colab-open-dialog .open-piper-notebook .buttons { margin: 10px 0px; paddin=
g-left: 8px; }

.colab-open-dialog .open-piper-notebook colab-workspace-list, .colab-open-d=
ialog .open-piper-notebook-path { display: block; width: 620px; }

.colab-open-dialog .upload-file-target { border: 1px solid transparent; bor=
der-radius: 10px; height: calc(100% - 20px); text-align: center; width: cal=
c(100% - 20px); }

.colab-open-dialog .upload-file-target label { background-color: var(--cola=
b-primary-color); border-radius: 5px; color: var(--colab-on-primary-color);=
 font-weight: 700; padding: 15px; cursor: pointer; }

.colab-open-dialog .upload-file-target label:focus { outline: 1px solid var=
(--colab-bold-border-color); }

.colab-open-dialog #upload-notebook { display: none; }

.colab-open-dialog .upload-file-target[active] { border-color: var(--colab-=
border-color); }

.colab-open-dialog .upload-file-target[disabled] { border: none; }

.colab-open-dialog .upload-file-target .uploading, .colab-open-dialog .uplo=
ad-file-target[disabled] label { display: none; }

.colab-open-dialog .upload-file-target[disabled] .uploading { display: inli=
ne-block; }

.colab-open-dialog .upload-file-target[disabled] .uploading mwc-circular-pr=
ogress { margin-bottom: 12px; }

.colab-open-dialog .upload-file-target::before { display: inline-block; hei=
ght: 100%; vertical-align: middle; }

.colab-open-dialog .sky { margin-bottom: 20px; }

.colab-open-dialog md-icon.cloud { --md-icon-size: 200px; color: rgb(211, 2=
11, 211); left: 50px; position: relative; font-variation-settings: "FILL" 1=
; user-select: none; }

.colab-open-dialog md-icon.cloud#light { --md-icon-size: 150px; color: rgb(=
238, 238, 238); left: -85px; top: 20px; }

.colab-open-dialog p { margin: 20px; }

@media only screen and (max-width: 430px) {
  .colab-open-dialog md-icon.cloud { left: 0px; }
  .colab-open-dialog md-icon.cloud#light { left: 30px; top: -120px; }
}

.colab-open-dialog .colab-icon.clear-history, .colab-open-dialog .colab-ico=
n.reload { padding-right: 10px; padding-top: 10px; }

#sharing-dialog mwc-textfield { cursor: pointer; display: block; margin-top=
: 8px; }

colab-table-of-contents { overflow: hidden; }

colab-table-of-contents colab-scroller { display: block; height: 100%; over=
flow: hidden auto; padding-bottom: 20px; }

colab-table-of-contents colab-scroller:not(:hover, :focus-within) { --colab=
-scrollbar-color: transparent; }

.colab-toc-sections:has(.toc-cell) { margin-bottom: 12px; }

.toc-add-section { --md-text-button-container-height: 28px; --md-text-butto=
n-leading-space: 12px; --md-text-button-trailing-space: 12px; --md-text-but=
ton-with-leading-icon-trailing-space: 12px; --md-text-button-with-trailing-=
icon-leading-space: 12px; --md-text-button-with-leading-icon-leading-space:=
 8px; --md-text-button-with-trailing-icon-trailing-space: 8px; --md-text-bu=
tton-icon-size: 20px; margin-left: 8px; }

.toc-cell { display: flex; -webkit-box-pack: justify; justify-content: spac=
e-between; gap: 4px; max-width: 100%; }

.toc-cell-focused > .toc-cell .toc-cell-link { border-left-color: var(--col=
ab-primary-color); color: var(--colab-primary-color); }

.toc-cell-focused > .toc-cell .toc-cell-link a { color: var(--colab-primary=
-color); }

.toc-cell-focused > .toc-cell .toc-cell-button-container md-icon-button { o=
pacity: 1; }

.toc-cell a { color: var(--colab-secondary-text-color); font-weight: 500; t=
ext-decoration: none; white-space: nowrap; }

.toc-cell .toc-cell-link { overflow: hidden; text-overflow: ellipsis; white=
-space: nowrap; border-left: 2px solid var(--colab-soft-border-color); flex=
-shrink: 1; padding-top: 6px; padding-right: 6px; padding-bottom: 6px; padd=
ing-left: calc(8px + var(--colab-toc-cell-depth, 0)*12px); }

.toc-cell-button-container { -webkit-box-align: center; align-items: center=
; display: flex; gap: 4px; }

.toc-cell md-icon-button { opacity: 0; --md-focus-ring-outward-offset: -2px=
; --md-icon-button-state-layer-height: 24px; --md-icon-button-state-layer-w=
idth: 24px; }

.toc-cell:focus-within md-icon-button, .toc-cell:hover md-icon-button, body=
.mobile .toc-cell md-icon-button { opacity: 1; }

@media (forced-colors: active) {
  .toc-cell:focus-within md-icon-button, .toc-cell:hover md-icon-button, bo=
dy.mobile .toc-cell md-icon-button { opacity: 1; }
}

body colab-tab-pane.layout.hidden, colab-tab-layout-container colab-resizer=
.hidden { display: none; }

colab-tab-layout-container .notebook-tab { position: relative; }

colab-tab-pane .tab-pane-header { gap: 2px; margin: 8px 8px 8px 20px; --md-=
focus-ring-outward-offset: -2px; --md-divider-thickness: 0; }

colab-tab-layout-container .tab-pane-parent > colab-resizer.sn-resize { min=
-height: 25px; max-height: 99%; }

colab-tab-layout-container .tab-pane-parent > colab-resizer.we-resize { min=
-width: 210px; max-width: 99%; }

colab-tab-pane { background-color: var(--colab-primary-surface-color); flex=
-shrink: 1; max-width: 100%; min-height: 0px; min-width: 0px; }

.notebook-vertical:not(.embedded) colab-tab-pane { border-radius: 28px; ove=
rflow: clip; }

colab-tab-pane .tab-pane-container, colab-tab-pane > div { min-height: 0px;=
 min-width: 0px; }

colab-tab-layout-container { min-height: 100px; }

colab-tab-layout-container md-primary-tab { padding: 0px; --md-primary-tab-=
active-indicator-color: var(--colab-primary-color); --md-primary-tab-active=
-indicator-shape: 0px; --md-primary-tab-active-indicator-height: 2px; --md-=
primary-tab-container-shape: 4px; --md-primary-tab-label-text-line-height: =
24px; --md-sys-color-primary: var(--colab-primary-text-color); --md-sys-col=
or-on-surface-variant: var(--colab-primary-text-color); }

colab-tab-layout-container md-primary-tab:not(:first-child) { margin-left: =
8px; }

colab-tab-layout-container md-primary-tab[active] { --md-primary-tab-contai=
ner-shape-end-end: 0px; --md-primary-tab-container-shape-end-start: 0px; }

colab-tab-layout-container .tab-pane-header md-primary-tab { --md-primary-t=
ab-label-text-size: 16px; }

colab-tab-layout-container .tab-pane-header md-primary-tab[active]:only-of-=
type { --md-primary-tab-active-indicator-color: transparent; --md-primary-t=
ab-container-shape-end-end: 4px; --md-primary-tab-container-shape-end-start=
: 4px; }

colab-tab-layout-container .tab-pane-header md-primary-tab[active]:only-of-=
type .tab-close { display: none; }

colab-tab-pane .tab-pane-header md-primary-tab { -webkit-box-flex: 0; flex-=
grow: 0; --md-primary-tab-container-height: 36px; }

colab-tab-layout-container.flexible-tabs .tab-close { --md-focus-ring-outwa=
rd-offset: -2px; --md-icon-button-icon-size: 20px; --md-icon-button-state-l=
ayer-height: 24px; --md-icon-button-state-layer-width: 24px; overflow: hidd=
en; vertical-align: middle; visibility: hidden; }

colab-tab-layout-container.flexible-tabs md-primary-tab:focus .tab-close, c=
olab-tab-layout-container.flexible-tabs md-primary-tab:hover .tab-close, co=
lab-tab-layout-container.flexible-tabs md-primary-tab[active] .tab-close { =
visibility: visible; }

.colab-tab-header { -webkit-box-align: center; align-items: center; display=
: flex; gap: 4px; padding-left: 4px; padding-right: 4px; }

.colab-tab-title { display: flex; gap: 8px; }

colab-tab-pane md-primary-tab.dragging { opacity: 0.6; }

colab-tab md-linear-progress { margin-bottom: 5px; }

colab-tab md-linear-progress.hidden { display: none; }

colab-tab-pane colab-tab > colab-scroller { min-height: 0px; overflow: auto=
; }

colab-tab-pane colab-tab > colab-scroller:not(:hover, :focus-within) { --co=
lab-scrollbar-color: transparent; }

colab-tab { flex-shrink: 1; min-height: 0px; overflow: hidden; transition: =
background-color 0.1s linear; }

.notebook-vertical:not(.embedded) colab-tab { margin: 0px 20px 8px; }

.notebook-vertical:not(.embedded) colab-tab.notebook-tab-content { margin: =
6px 10px 6px 6px; }

.notebook-vertical:not(.embedded) colab-tab.cell-tab { margin-left: 12px; m=
argin-right: 12px; }

.notebook-vertical:not(.embedded) colab-tab.scratchpad { margin-left: 4px; =
margin-right: 8px; }

colab-tab.highlight { background-color: var(--colab-highlighted-surface-col=
or); }

.tab-pane-container colab-tab:not(.selected-tab), colab-tab-layout-containe=
r:not(.drag-target) colab-resizer.no-tabs, colab-tab-layout-container:not(.=
drag-target) colab-tab-pane.no-header .tab-pane-header { display: none; }

colab-tab-layout-container .tab-pane-parent > colab-resizer { flex-shrink: =
0; }

colab-tab-layout-container .tab-pane-parent { -webkit-box-flex: 1; flex-gro=
w: 1; flex-shrink: 1; gap: 3px; min-width: 0px; min-height: 0px; }

colab-tab-layout-container.drag-target .tab-pane-parent > colab-resizer { m=
in-height: 25%; min-width: 25%; }

colab-tab-pane md-primary-tab[draggable=3D"true"] { cursor: move; }

colab-tab-pane md-tabs { min-width: 20px; padding-right: 16px; position: re=
lative; }

colab-tab-pane .tab-drop-indicator { color: var(--colab-primary-color); pos=
ition: absolute; top: 0px; z-index: 1; }

.right-pane-snap-hint { animation: 0.15s ease-out 0s 1 normal none running =
snapIn; background-color: var(--colab-scrollbar-color); bottom: 0px; displa=
y: none; pointer-events: none; position: absolute; right: 0px; top: 0px; wi=
dth: 30%; z-index: var(--colab-dialog-bg-z-index); }

@-webkit-keyframes snapIn {=20
  0% { opacity: 0; transform: scale(0.8); }
  100% { opacity: 1; transform: scale(1); }
}

@keyframes snapIn {=20
  0% { opacity: 0; transform: scale(0.8); }
  100% { opacity: 1; transform: scale(1); }
}

colab-tab-layout { background-color: var(--colab-primary-surface-color); di=
splay: block; }

colab-tab-layout .tab-layout-header { -webkit-box-align: center; align-item=
s: center; background-color: var(--colab-secondary-surface-color); padding:=
 0px 4px 0px 8px; --md-sys-color-surface: var(--colab-secondary-surface-col=
or); --md-divider-color: transparent; }

colab-tab-layout:not(.tabs-editing) .tabs-add-tab, colab-tab-layout:not(.ta=
bs-editing) .tabs-delete-tab, colab-tab-layout:not(.tabs-editing) .tabs-ren=
ame-tab { display: none; }

#header-background, #header-content { display: flex; height: 100%; position=
: absolute; width: 100%; }

body.mobile #header-content { position: relative; }

.goog-submenu-arrow { color: var(--colab-icon-color); font-size: 70%; left:=
 auto; padding-right: 0px; position: absolute; right: 15px; text-align: rig=
ht; transition: 0.218s; }

.goog-menuitem { padding: 6px 10em 6px 15px; }

.goog-menu:has(.goog-option-selected) .goog-menuitem { padding-left: 39px; =
}

.goog-menuitem-highlight, .goog-menuitem-hover { background-color: var(--co=
lab-highlighted-surface-color); border: none; }

.menubar-wrapper { display: inline-flex; }

#top-menubar .goog-menu-button-caption { font-weight: 500; padding: 0px; }

#top-menubar .goog-menu-button-caption, .goog-menu .goog-menuitem-content {=
 color: var(--colab-primary-text-color); font-family: var(--colab-chrome-fo=
nt-family); font-size: var(--colab-chrome-font-size); line-height: 20px; }

#top-menubar { background-color: transparent; border-radius: 4px; cursor: d=
efault; display: inline-flex; gap: 8px; outline: none; white-space: nowrap;=
 }

#top-menubar.jsfocus { outline: var(--colab-focus-ring-color) auto 1px; out=
line-offset: 1px; }

.goog-menu { background: var(--colab-primary-surface-color); border-radius:=
 4px; border-color: var(--colab-primary-surface-color); box-shadow: rgba(0,=
 0, 0, 0.15) 0px 2px 6px 2px, rgba(0, 0, 0, 0.3) 0px 1px 2px 0px; cursor: d=
efault; margin: 0px; outline: none; overflow-y: auto; padding: 7px 0px; pos=
ition: absolute; transition: opacity 0.218s; --md-icon-size: 20px; }

.goog-menuseparator { border-top: 1px solid var(--colab-border-color); marg=
in: 6px 0px; }

.header-warning { -webkit-box-align: center; align-items: center; align-sel=
f: stretch; background: var(--colab-primary-container-color); display: flex=
; gap: 12px; -webkit-box-pack: center; justify-content: center; letter-spac=
ing: 0px; padding: 8px 16px; line-height: 20px; }

.header-warning .message { color: var(--colab-primary-text-color); -webkit-=
box-flex: 1; flex: 1 0 0px; }

.header-warning .actions { display: flex; gap: 8px; -webkit-box-pack: end; =
justify-content: flex-end; }

.header-warning + .header-warning { margin-top: 1px; }

.header-warning .actions a { font-weight: 500; gap: 4px; padding: 4px 12px;=
 text-decoration: none; }

.ai-warning { background-color: unset; border-bottom: 1px solid var(--colab=
-border-color); }

.header-staging { color: var(--colab-secondary-text-color); font-size: 12px=
; left: 50%; margin-left: -100px; position: absolute; text-align: center; w=
idth: 200px; }

body:not(.mobile) .top-floater #header { font: normal 13px var(--colab-chro=
me-font-family); height: 64px; text-align: left; width: 100%; }

#header { position: relative; }

#header-logo { height: 64px; margin-left: 12px; text-align: center; width: =
50px; }

#header-logo > img { padding-top: 10px; position: relative; vertical-align:=
 middle; width: 40px; }

body:not(.mobile) #header-doc-toolbar { overflow: hidden; padding-left: 8px=
; padding-top: 8px; }

body.mobile #header-doc-toolbar { margin-left: 12px; }

#document-info { -webkit-box-align: center; align-items: center; display: f=
lex; height: 28px; margin-bottom: 2px; }

#document-info md-icon-button { --md-focus-ring-outward-offset: -2px; --md-=
icon-button-icon-size: 20px; --md-icon-button-state-layer-height: 28px; --m=
d-icon-button-state-layer-width: 28px; }

.header-warning .close { --md-focus-ring-outward-offset: -2px; --md-icon-bu=
tton-icon-size: 20px; --md-icon-button-state-layer-height: 28px; --md-icon-=
button-state-layer-width: 28px; margin: 0px -4px; --md-sys-color-on-surface=
-variant: var(--colab-primary-color); }

.doc-name { background: transparent; border: 1px solid transparent; color: =
var(--colab-primary-text-color); font: normal 18px var(--colab-google-sans-=
font-family); max-width: 100%; min-width: 65px; padding: 0px 4px 0px 3px; t=
ext-overflow: ellipsis; white-space: pre; }

md-text-button.show-chat-button { --md-text-button-container-height: 40px; =
--md-text-button-icon-size: 24px; --md-sys-color-primary: var(--colab-prima=
ry-text-color); }

.doc-name:hover { border: 1px solid var(--colab-bold-border-color); }

#header-right { -webkit-box-align: center; align-items: center; display: fl=
ex; gap: 12px; margin-right: 16px; }

#header md-filled-tonal-button, #header md-icon-button, #header md-text-but=
ton { --md-focus-ring-outward-offset: -2px; }

#header md-filled-tonal-button { --md-filled-tonal-button-icon-size: 24px; =
}

#header-doc-toolbar .file-location-icon { flex-shrink: 0; --md-icon-size: 1=
8px; margin: 0px 2px 0px 4px; }

#star-icon { flex-shrink: 0; }

#star-icon.starred md-icon { color: var(--colab-logo-dark); font-variation-=
settings: "FILL" 1; }

.goog-menuitem-checkbox { visibility: hidden; }

.goog-option-selected .goog-menuitem-checkbox { background: none; color: va=
r(--colab-icon-color); height: 20px; left: 15px; visibility: visible; width=
: 20px; }

.goog-menubar .goog-menu-button-dropdown { background: none; }

.goog-menubar .goog-menu-button { background: transparent; border: none; bo=
rder-radius: 4px; padding: 2px 4px; }

.goog-menubar .goog-menu-button-inner-box { margin: 0px; padding: 0px; }

.goog-menubar .goog-menu-button-hover { background: var(--colab-highlighted=
-surface-color); }

#top-menubar > div.goog-menu-button-open { background: var(--colab-highligh=
ted-surface-color); }

@media (forced-colors: active), (prefers-contrast: more) {
  #top-menubar > div.goog-menu-button-open, .goog-menubar .goog-menu-button=
.goog-menu-button-hover, .goog-menuitem-highlight, .goog-menuitem-hover { o=
utline: highlight solid 3px; outline-offset: -2px; }
}

.goog-menuitem-disabled, .goog-menuitem-disabled .goog-menuitem-accel, .goo=
g-menuitem-disabled .goog-menuitem-checkbox, .goog-menuitem-disabled .goog-=
menuitem-content { color: var(--colab-disabled-text-color) !important; }

.goog-menuitem-accel { color: var(--colab-secondary-text-color); padding-ri=
ght: 15px; }

body.mobile #document-info { -webkit-box-flex: 1; flex-grow: 1; margin-left=
: 4px; margin-top: 6px; overflow: hidden; }

colab-callout h2 { color: var(--colab-on-primary-color); font-size: 16px; f=
ont-weight: 500; margin: 0px; }

html.embedded #document-info { display: none; }

html.embedded #header-doc-toolbar { -webkit-box-align: center; align-items:=
 center; display: flex; margin-left: 12px; padding-top: 0px; }

html.embedded .menubar-wrapper { -webkit-box-align: center; align-items: ce=
nter; }

html.embedded .top-floater #header { height: 40px; }

html.embedded #show-chat-button { --md-text-button-container-height: 32px; =
}

.history-view-dialog { --mdc-dialog-max-width: 98vw; --mdc-dialog-min-width=
: 98vw; --mdc-dialog-max-height: 98vh; max-width: 98vw; min-width: 98vw; ma=
x-height: 98vh; }

.history-view-container { display: flex; -webkit-box-orient: vertical; -web=
kit-box-direction: normal; flex-direction: column; height: calc(-150px + 98=
vh); }

colab-history-view { display: block; height: 100%; min-width: 800px; overfl=
ow: hidden; }

colab-history-view.dialog-ui-refresh { margin-bottom: -16px; }

.history-view-container .history-view-columns { height: calc(-150px + 98vh)=
; min-height: 200px; overflow: hidden; }

.history-view-container .preview { overflow: hidden; }

.history-view-container .preview md-circular-progress { margin: auto; }

.history-view-left-column { border-right: 1px solid var(--colab-border-colo=
r); -webkit-box-flex: 0; flex-grow: 0; flex-shrink: 0; margin-top: 2px; wid=
th: 350px; }

.history-view-left-column md-checkbox { padding: 8px; }

md-circular-progress.hidden { display: none; }

colab-history-list.supports-named-versions { border-top: 1px solid var(--co=
lab-border-color); }

.ansibold { font-weight: 700; }

.ansiblack { color: rgb(0, 0, 0); }

.ansired { color: darkred; }

.ansigreen { color: rgb(0, 100, 0); }

.ansiyellow { color: brown; }

.ansiblue { color: rgb(0, 0, 139); }

.ansipurple { color: rgb(148, 0, 211); }

.ansicyan { color: rgb(70, 130, 180); }

.ansigray { color: gray; }

.ansibgblack { background-color: rgb(0, 0, 0); }

.ansibgred { background-color: red; }

.ansibggreen { background-color: green; }

.ansibgyellow { background-color: rgb(255, 255, 0); }

.ansibgblue { background-color: blue; }

.ansibgpurple { background-color: rgb(255, 0, 255); }

.ansibgcyan { background-color: cyan; }

.ansibggray { background-color: gray; }

.colab-assist-pane-input { margin: 8px 0px; }

colab-assist-pane { height: 100%; overflow: hidden; width: 100%; }

colab-assist-pane.horizontal { gap: 8px; }

colab-assist-pane > * { flex-basis: 50%; flex-shrink: 1; min-height: 50px; =
min-width: 100px; }

.colab-assist-progress { margin-right: 8px; visibility: hidden; }

.colab-assist-progress.searching { visibility: visible; }

.colab-assist-pane-results { flex-shrink: 1; max-height: unset; min-height:=
 0px; overflow: auto; }

.colab-assist-pane-results:not(:hover, :focus-within) { --colab-scrollbar-c=
olor: transparent; }

colab-assist-pane-result { -webkit-box-align: center; align-items: center; =
cursor: pointer; display: flex; padding: 3px 4px; }

.colab-assist-pane-result-text { overflow: hidden; text-overflow: ellipsis;=
 white-space: nowrap; -webkit-box-flex: 1; flex-grow: 1; }

colab-assist-pane-result.selected { background: var(--colab-highlighted-sur=
face-color); }

.colab-assist-pane-details { overflow: auto; padding: 0px 4px; }

.colab-assist-pane-details:not(:hover, :focus-within) { --colab-scrollbar-c=
olor: transparent; }

.colab-assist-pane-doc-header { -webkit-box-align: center; align-items: cen=
ter; display: flex; }

.colab-assist-pane-doc-title { overflow: hidden; text-overflow: ellipsis; w=
hite-space: nowrap; -webkit-box-flex: 1; flex-grow: 1; font-size: 16px; }

.colab-assist-pane-doc-title, .colab-assist-pane-documentation h2 { line-he=
ight: 24px; }

.colab-assist-pane-documentation h2 { font-size: 15px; }

.colab-assist-pane-documentation h3 { font-size: var(--colab-chrome-font-si=
ze); }

.colab-assist-pane-documentation h4 { font-size: 13px; }

.colab-assist-pane-documentation h5 { font-size: 11px; }

.colab-assist-pane-documentation h3, .colab-assist-pane-documentation h4, .=
colab-assist-pane-documentation h5 { line-height: 20px; }

.colab-assist-pane-no-selection .colab-assist-pane-code, .colab-assist-pane=
-no-selection .colab-assist-pane-doc-insert, .colab-assist-pane-no-selectio=
n .colab-assist-pane-view-source { display: none; }

.colab-assist-pane-code:has(.monaco) { background: var(--colab-editor-backg=
round); border: 1px solid var(--colab-border-color); border-radius: 8px; fo=
nt-family: var(--colab-code-font-family); overflow-x: auto; font-size: var(=
--colab-code-font-size); padding: 8px 8px 0px; }

.colab-assist-pane-code .monaco .context-view.monaco-menu-container { displ=
ay: none; }

.command-palette { color: var(--colab-secondary-text-color); margin-top: 2p=
x; max-height: 400px; min-width: 500px; }

.command-palette md-outlined-text-field { margin: 8px 8px 16px; }

.command-palette-results { overflow: auto; }

.command-palette-result-item { cursor: pointer; padding: 2px 80px 2px 16px;=
 position: relative; }

.command-palette .result-separator { border-top: 1px solid var(--colab-bord=
er-color); margin: 8px; }

.command-palette-match { font-weight: 700; }

.command-palette-result-item.selected, .command-palette-result-item:hover {=
 background: var(--colab-highlighted-surface-color); }

.command-palette-result-shortcut { color: var(--colab-secondary-text-color)=
; direction: ltr; left: auto; padding: 0px 16px 0px 6px; position: absolute=
; right: 0px; text-align: right; }

.command-palette-backdrop.opened { opacity: 0; }

.colab-assist-result-insert { flex-shrink: 0; }

.cell { --colab-cell-gutter-width: 40px; --colab-base-surface-color: var(--=
colab-primary-surface-color); align-content: flex-start; display: flex; -we=
bkit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: c=
olumn; position: relative; }

html { --colab-cell-gutter-button-transition-time: 250ms; }

.monaco-scrollable-element > .invisible { display: none; }

.cell:focus { outline-style: none; }

.imported .imported-from-banner { -webkit-box-align: center; align-items: c=
enter; display: flex; gap: 4px; }

.imported-from-banner { display: none; padding: 6px 12px; }

.sync-imported-cell { --md-focus-ring-outward-offset: -2px; --md-icon-butto=
n-icon-size: 20px; --md-icon-button-state-layer-height: 28px; --md-icon-but=
ton-state-layer-width: 28px; }

.inputarea, .text-top-div { display: flex; -webkit-box-orient: horizontal; =
-webkit-box-direction: normal; flex-flow: row; }

.views-hide-code .inputarea, .views-hide-code .inputarea-toolbar, .views-hi=
de-code .output-info { display: none !important; }

.views-hide-code .code .codecell-input-output { outline: none; }

.views-hide-code .code .output-content { border-top: none; }

.inputarea { background-color: var(--colab-editor-background); min-height: =
24px; position: relative; }

.code .inputarea.form { background-color: var(--colab-primary-surface-color=
); }

.text .markdown { box-sizing: border-box; color: var(--colab-primary-text-c=
olor); line-height: 1.6; max-width: 1016px; min-height: 28px; padding-left:=
 8px; padding-right: 8px; width: 100%; overflow-wrap: break-word; }

.toc .markdown { padding-right: 100px; }

.markdown img { max-width: 100%; max-height: 100%; }

.markdown blockquote { border-left: 5px solid var(--colab-highlighted-surfa=
ce-color); margin-left: 0px; padding: 0px 2em; }

pre { font-family: var(--colab-code-font-family); margin-bottom: 2px; margi=
n-top: 2px; white-space: pre-wrap; }

.notebook-vertical.large-notebook { --colab-run-button-position: static; }

.code .editor.monaco { margin: 10px 8px 0px 0px; }

.editor.flex { min-width: 0px; }

.text * .editor { display: none; }

.text.edit * .editor { display: block; }

.text.edit .editor-container { -webkit-box-orient: vertical; -webkit-box-di=
rection: normal; flex-direction: column; -webkit-box-flex: 1; flex-grow: 1;=
 overflow: hidden; }

.text.edit .editor-container.horizontal { display: flex; -webkit-box-orient=
: horizontal; -webkit-box-direction: normal; flex-direction: row; }

.text.edit .editor-root { background: var(--colab-editor-background); -webk=
it-box-flex: 1; flex-grow: 1; }

body:not(.mobile) .text.edit .editor-root { padding-top: 10px; }

.text.edit .editor-container.horizontal .editor-root { border-bottom-left-r=
adius: 8px; flex-basis: 0px; overflow-x: auto; }

.text.edit .editor-container .text-top-div { -webkit-box-flex: 1; flex: 1 1=
 0%; overflow-x: auto; }

.text:not(.edit) .editor-container .text-top-div { width: 100%; }

.text.edit .editor { border: none; }

.text.edit .editor-container.horizontal .markdown { border-left: 1px solid =
var(--colab-border-color); }

.text.edit .editor-container:not(.horizontal) .editor { border-bottom: 1px =
solid var(--colab-border-color); }

.cell-contents { display: flex; -webkit-box-orient: vertical; -webkit-box-d=
irection: normal; flex-direction: column; }

.main-content { border-radius: 8px; display: flex; -webkit-box-orient: vert=
ical; -webkit-box-direction: normal; flex-direction: column; min-height: 38=
px; position: relative; }

.notebook-cell.focused .main-content { outline: 1px solid var(--colab-bold-=
border-color); }

.notebook-cell.agent-focused .main-content, .notebook-cell.focused:focus .m=
ain-content, .notebook-cell.focused:has(.monaco-editor.focused) .main-conte=
nt { outline: 2px solid var(--colab-primary-color); }

.code .codecell-input-output { border-radius: 8px; display: flex; -webkit-b=
ox-orient: vertical; -webkit-box-direction: normal; flex-direction: column;=
 outline: 1px solid var(--colab-border-color); }

.code div.inputarea { border-radius: 8px; }

.code .formview, .code colab-viz-toolbar { border-bottom-right-radius: 8px;=
 border-top-right-radius: 8px; }

.code:has(.output-content:not([hidden])) div.inputarea.both:not(:has(.outpu=
t-content)), .code:has(.output-content:not([hidden])) div.inputarea.code { =
border-bottom-left-radius: 0px; border-bottom-right-radius: 0px; }

.code:has(.output-content:not([hidden])) .formview:not(:has(.output-content=
)), .code:has(.output-content:not([hidden])) colab-viz-toolbar { border-bot=
tom-right-radius: 0px; }

.code .output-content { border-top: 1px solid var(--colab-soft-border-color=
); }

.code .formview .output-content { border-top: none; }

.code .inputarea-toolbar { border-top: 0px; border-right: 0px; border-left:=
 0px; border-image: initial; border-bottom: 1px solid var(--colab-border-co=
lor); border-radius: 8px 8px 0px 0px; outline: 1px solid var(--colab-border=
-color); }

.code .inputarea-toolbar:not([invalid]) + div.inputarea { border-top-left-r=
adius: 0px; border-top-right-radius: 0px; }

.code.notebook-cell.agent-focused .codecell-input-output, .code.notebook-ce=
ll.focused .codecell-input-output { outline-color: transparent; }

.code.notebook-cell.agent-focused:has(colab-form-title, .imported-from-bann=
er, colab-cell-execution-schedule-editor:not([hidden])) .inputarea-toolbar,=
 .code.notebook-cell.focused:has(colab-form-title, .imported-from-banner, c=
olab-cell-execution-schedule-editor:not([hidden])) .inputarea-toolbar { bor=
der-radius: 0px; }

.code.notebook-cell.agent-focused:has(colab-form-title, .imported-from-bann=
er, colab-cell-execution-schedule-editor:not([hidden])) div.inputarea, .cod=
e.notebook-cell.focused:has(colab-form-title, .imported-from-banner, colab-=
cell-execution-schedule-editor:not([hidden])) div.inputarea { border-top-le=
ft-radius: 0px; border-top-right-radius: 0px; }

.code.notebook-cell.agent-focused:has(colab-form-title, .imported-from-bann=
er, colab-cell-execution-schedule-editor:not([hidden])) .formview, .code.no=
tebook-cell.agent-focused:has(colab-form-title, .imported-from-banner, cola=
b-cell-execution-schedule-editor:not([hidden])) colab-viz-toolbar, .code.no=
tebook-cell.focused:has(colab-form-title, .imported-from-banner, colab-cell=
-execution-schedule-editor:not([hidden])) .formview, .code.notebook-cell.fo=
cused:has(colab-form-title, .imported-from-banner, colab-cell-execution-sch=
edule-editor:not([hidden])) colab-viz-toolbar { border-top-right-radius: 0p=
x; }

.output-content { display: flex; font-family: var(--colab-code-font-family)=
; font-size: 10pt; }

.output-iframe-container { -webkit-box-flex: 1; flex: 1 1 0%; margin-right:=
 1px; min-width: 0px; }

.mirror-cell iframe, .output-iframe-sizer iframe { border: 0px; display: bl=
ock; width: 100%; }

.mirror-cell colab-static-output-renderer { max-height: unset; }

.mirror-cell div.inputarea { outline: 1px solid var(--colab-border-color); =
overflow: hidden; padding-left: 10px; }

.mirror-cell:has(.monaco-editor.focused) div.inputarea { outline: 2px solid=
 var(--colab-focus-ring-color); }

.editor { font-size: 13px; }

.add-cell { -webkit-box-align: center; align-items: center; align-self: cen=
ter; display: flex; -webkit-box-orient: vertical; -webkit-box-direction: no=
rmal; flex-flow: column; height: 16px; position: relative; width: 100%; }

.add-cell > hr { border-right-color: ; border-bottom-color: ; border-left-c=
olor: ; border-style: none solid solid; border-top-color: initial; border-w=
idth: 1px; left: 20px; opacity: 0; position: absolute; right: 20px; top: 0p=
x; transition: visibility 0.25s, opacity 0.2s; visibility: hidden; }

.add-cell:hover > hr { opacity: 1; transition: visibility 0.1s, opacity 0.2=
s; visibility: visible; }

.add-cell-buttons { display: flex; font-family: var(--colab-chrome-font-fam=
ily); margin-top: -4px; opacity: 0; transition: opacity 0.2s; visibility: h=
idden; z-index: 20; }

.add-cell-buttons md-outlined-button { --md-outlined-button-container-heigh=
t: 28px; --md-outlined-button-leading-space: 12px; --md-outlined-button-tra=
iling-space: 12px; --md-outlined-button-with-leading-icon-trailing-space: 1=
2px; --md-outlined-button-with-trailing-icon-leading-space: 12px; --md-outl=
ined-button-with-leading-icon-leading-space: 8px; --md-outlined-button-with=
-trailing-icon-trailing-space: 8px; --md-outlined-button-icon-size: 20px; b=
ackground: var(--colab-primary-surface-color); gap: 2px; margin: 0px 8px; }

.add-cell > .add-cell-buttons { transition: opacity 0.2s 0.25s, visibility =
0.25s; }

.add-cell:hover > .add-cell-buttons { opacity: 1; transition: opacity 0.2s =
0.1s; visibility: visible; }

.cell > .add-cell { height: 12px; }

.cell .add-cell-buttons { margin-top: -8px; }

.cell .add-cell > hr { margin-top: 5px; }

.notebook-content > .add-cell { margin-top: -1px; }

.toc-refresh-button { --md-outlined-button-container-height: 28px; --md-out=
lined-button-leading-space: 12px; --md-outlined-button-trailing-space: 12px=
; --md-outlined-button-with-leading-icon-trailing-space: 12px; --md-outline=
d-button-with-trailing-icon-leading-space: 12px; --md-outlined-button-with-=
leading-icon-leading-space: 8px; --md-outlined-button-with-trailing-icon-tr=
ailing-space: 8px; --md-outlined-button-icon-size: 20px; position: absolute=
; right: 4px; top: 12px; }

.toc .main-content { min-height: 48px; }

.toc:not(.edit) .main-content { padding: 4px 8px; }

.section-header { --colab-run-button-size: 24px; -webkit-box-align: center;=
 align-items: center; border-radius: 8px; cursor: pointer; display: flex; h=
eight: 32px; margin: 4px; padding: 0px 8px; }

.section-header:has(.section-header-container:hover) { background: var(--co=
lab-highlighted-surface-color); }

.section-header-container { --md-icon-size: 15px; -webkit-box-align: center=
; align-items: center; color: var(--colab-secondary-text-color); display: f=
lex; -webkit-box-flex: 1; flex-grow: 1; font-weight: 500; column-gap: 4px; =
height: 100%; }

.section-header-container span { margin-top: 2px; }

.notebook-busy .section-header { cursor: progress; }

.text colab-run-button { display: none; margin: -2px -4px 0px -10px; }

.text.executable colab-run-button { display: block; }

.toc * blockquote { margin: 0px 20px; }

.toc * p { margin: 0px; }

.cell.selected * .cell-mask { background: rgba(0, 156, 255, 0.35); border-r=
adius: 8px; height: 100%; position: absolute; width: 100%; z-index: 10; }

.panel-sizing .cell-mask { height: 100%; position: absolute; width: 100%; z=
-index: 10; }

.cell.toc * .cell-mask { left: 0px; top: 0px; }

.cell-gutter { border-radius: 8px 0px 0px 8px; -webkit-box-orient: vertical=
; -webkit-box-direction: normal; flex-flow: column; min-height: 39px; width=
: var(--colab-cell-gutter-width); }

.cell-execution-container { bottom: 0px; left: 0px; position: absolute; top=
: 0px; width: var(--colab-cell-gutter-width); }

html[theme=3D"dark"].embedded colab-cell-toolbar { background: var(--colab-=
secondary-surface-color); }

.cell-toolbar.sticky { position: sticky; top: 20px; z-index: 11; }

colab-tab-pane .scratchpad .cell { margin-left: 40px; }

colab-tab-pane .scratchpad .cell:has(.monaco-editor.focused) .codecell-inpu=
t-output { outline: 2px solid var(--colab-focus-ring-color); }

colab-cell-pair-slide .add-cell, colab-cell-slide .add-cell, colab-tab-pane=
 .cell-tab .add-cell, colab-tab-pane .scratchpad .add-cell, colab-tab-pane =
.scratchpad .cell-toolbar, mwc-dialog .cell-tab .add-cell { display: none; =
visibility: hidden; }

.cell-tab colab-scroller { padding: 8px; }

.scratchpad colab-scroller { padding: 4px 4px 4px 0px; }

.markdown-toolbar { display: none; }

.text.edit .markdown-toolbar { --md-focus-ring-outward-offset: -2px; --md-i=
con-button-icon-size: 20px; --md-icon-button-state-layer-height: 32px; --md=
-icon-button-state-layer-width: 32px; --md-icon-size: 20px; -webkit-box-ali=
gn: center; align-items: center; background-color: var(--colab-surface-cont=
ainer-low-color); border-top-left-radius: 8px; border-top-right-radius: 8px=
; display: flex; height: 40px; overflow: hidden; padding-left: 4px; white-s=
pace: nowrap; }

.text.edit:has(.imported-from-banner) .markdown-toolbar { border-top-left-r=
adius: 0px; border-top-right-radius: 0px; }

.markdown-toolbar .markdown-toolbar-close-editor { margin-left: 12px; }

.markdown-toolbar .markdown-toolbar-latex span { line-height: 0.8em; }

.markdown-toolbar .markdown-toolbar-insert-image { cursor: pointer; display=
: inline-block; position: relative; }

.markdown-toolbar .markdown-toolbar-insert-image > * { pointer-events: none=
; }

.markdown-toolbar .markdown-toolbar-insert-image md-ripple { border-radius:=
 var(--md-icon-button-state-layer-shape); --md-ripple-hover-color: var(--co=
lab-icon-color); --md-ripple-pressed-color: var(--colab-icon-color); --md-r=
ipple-hover-opacity: var(--md-icon-button-hover-state-layer-opacity); --md-=
ripple-pressed-opacity: var(
    --md-icon-button-pressed-state-layer-opacity
  ); }

.markdown-toolbar .markdown-toolbar-insert-image span { -webkit-box-align: =
center; align-items: center; display: inline-flex; height: var(--md-icon-bu=
tton-state-layer-height); -webkit-box-pack: center; justify-content: center=
; pointer-events: auto; position: relative; width: var(--md-icon-button-sta=
te-layer-width); }

.markdown-toolbar .markdown-toolbar-insert-image span:focus { outline: none=
; }

.markdown-toolbar .markdown-image-input { display: none; }

@media (forced-colors: active) {
  body:not(.mobile) .markdown-toolbar .markdown-toolbar-insert-image:focus-=
within, body:not(.mobile) .markdown-toolbar .markdown-toolbar-insert-image:=
hover { --colab-icon-color: Highlight; }
  .markdown-toolbar .markdown-toolbar-preview { --colab-icon-color: ButtonT=
ext; --colab-primary-text-color: ButtonText; }
  .markdown-toolbar .markdown-toolbar-preview:focus-within, .markdown-toolb=
ar .markdown-toolbar-preview:hover { --colab-icon-color: Highlight; --colab=
-primary-text-color: Highlight; }
}

.markdown-toolbar-blockquote md-icon { font-variation-settings: "FILL" 1; }

.text-cell-section-header { position: relative; }

md-icon-button.header-section-toggle { --md-focus-ring-outward-offset: -2px=
; --md-icon-button-icon-size: 20px; --md-icon-button-state-layer-height: 28=
px; --md-icon-button-state-layer-width: 28px; --md-sys-color-on-surface-var=
iant: var(--colab-primary-text-color); left: -44px; min-height: 28px; min-w=
idth: 28px; position: absolute; transition: transform 0.2s, -webkit-transfo=
rm 0.2s; }

.text.edit .header-section-toggle { display: none; }

.text.collapsed .header-section-toggle, colab-form-title.collapsed .header-=
section-toggle { transform: rotate(-90deg); }

.debugger-editor .monaco-editor .view-overlays .current-line, .editor .mona=
co-editor .view-overlays .current-line { background: none; border: 0px; }

.monaco-editor .overflowingContentWidgets .parameter-hints-widget > .wrappe=
r { max-height: 250px; }

.monaco-editor-hover .hover-row.status-bar { display: none; }

.monaco-editor .overflowingContentWidgets .monaco-editor-hover .monaco-edit=
or-hover-content, .monaco-editor .overflowingContentWidgets .parameter-hint=
s-widget > .wrapper { max-width: 800px !important; }

.monaco-editor .monaco-editor-hover-content p { margin: 8px 0px; }

.monaco-editor .overflowingContentWidgets .suggest-widget, .monaco-editor .=
overflowingContentWidgets .suggest-widget.docs-side { width: 800px; }

.notebook-vertical.large-notebook .decorationsOverviewRuler { display: none=
; }

.debugger-editor .monaco-editor .margin-view-overlays .line-numbers.lh-odd,=
 .editor .monaco-editor .margin-view-overlays .line-numbers.lh-odd { margin=
-top: 0px; }

.debugger-editor .monaco-editor .current-line ~ .line-numbers, .debugger-ed=
itor .monaco-editor .line-numbers, .editor .monaco-editor .current-line ~ .=
line-numbers, .editor .monaco-editor .line-numbers { color: var(--colab-sec=
ondary-text-color); }

.editor .monaco-editor .quick-input-widget .monaco-list { max-height: none;=
 min-height: 108px; }

.editor .monaco-editor .markdown-docs, .editor .monaco-editor .markdown-hov=
er { white-space: pre !important; }

.editor .monaco-editor .codelens-decoration > a, .editor .monaco-editor .co=
delens-decoration > span { color: var(--colab-secondary-text-color); }

.cell.focused .monaco-editor .current-line ~ .line-numbers { color: var(--c=
olab-primary-text-color); }

#context-menu .goog-menuitem { padding-left: 18px; padding-right: 9em; }

#context-menu .goog-menuitem-accel { padding-right: 18px; }

body.mobile .inputarea { flex-wrap: wrap; }

body.mobile .outputview { overflow: auto; }

body.mobile .add-cell { max-width: 100px; overflow-x: hidden; visibility: h=
idden; }

.monaco-emacs-statusbar, .monaco-vim-statusbar { border-bottom-left-radius:=
 8px; border-bottom-right-radius: 8px; bottom: 0px; box-sizing: border-box;=
 font-family: var(--colab-code-font-family); padding: 1px 4px 4px 8px; posi=
tion: sticky; width: 100%; }

.monaco-vim-statusbar { background-color: var(--colab-editor-background); }

.monaco-vim-statusbar span { color: var(--colab-primary-text-color) !import=
ant; }

.cell.text:not(.edit) .monaco-emacs-statusbar, .cell:not(.focused) .monaco-=
emacs-statusbar, .cell:not(.focused) .monaco-vim-statusbar, .monaco-emacs-s=
tatusbar:empty { display: none !important; }

.mirror-toolbar { background-color: var(--colab-surface-container-color); b=
order-radius: 100px; gap: 4px; height: 40px; margin: 0px 8px 4px; padding: =
0px 4px; --colab-cell-gutter-width: 32px; --colab-execution-icon-color: var=
(--colab-icon-color); }

.mirror-toolbar md-icon-button { margin: 4px 0px; --md-focus-ring-outward-o=
ffset: -2px; --md-icon-button-icon-size: 20px; --md-icon-button-state-layer=
-height: 32px; --md-icon-button-state-layer-width: 32px; }

colab-tab-pane .cell-tab { position: relative; }

colab-static-output-renderer { display: block; font-size: var(--colab-chrom=
e-font-size); max-height: 1000px; overflow: auto; padding: 7px 0px 7px 5px;=
 }

.cell.running colab-static-output-renderer, colab-static-output-renderer { =
contain: layout; }

colab-static-output-renderer .stdin-widget { -webkit-box-align: center; ali=
gn-items: center; display: inline; font-family: var(--colab-code-font-famil=
y); margin-right: 10px; margin-top: 10px; min-width: 250px; padding: 1px; }

colab-static-output-renderer .stdin-widget-hidden { visibility: hidden; }

colab-static-output-renderer pre { display: inline; white-space: pre; }

colab-static-output-renderer .output_text { display: inline; }

colab-static-output-renderer .execute_result.output_text pre { display: blo=
ck; white-space: pre-wrap; }

colab-static-output-renderer input { background: var(--colab-primary-surfac=
e-color); border: 1px solid var(--colab-bold-border-color); color: var(--co=
lab-primary-text-color); }

colab-static-output-renderer:focus { outline: none; }

.input-container { display: inline; position: relative; }

.input-container input.stdin-widget { margin-top: 0px; }

colab-static-output-renderer .stdin-widget:not(:focus) { border: none; outl=
ine: none; }

.input-container::after { animation: 1.2s step-end 0s infinite normal none =
running stdin-widget-blink; content: " "; height: 100%; left: 0px; pointer-=
events: none; position: absolute; top: 0px; width: 10px; }

.input-container.input-focused::after { display: none; }

@-webkit-keyframes stdin-widget-blink {=20
  0% { background: transparent; }
  50% { background: var(--colab-secondary-text-color); }
  100% { background: transparent; }
}

@keyframes stdin-widget-blink {=20
  0% { background: transparent; }
  50% { background: var(--colab-secondary-text-color); }
  100% { background: transparent; }
}

.monaco-currently-executing-line { border-color: transparent transparent tr=
ansparent var(--colab-success-color); border-style: solid; border-width: 6p=
x 0px 6px 4px; margin-left: 1px; top: 3px; height: 0px !important; width: 0=
px !important; }

.smartpaste-insert-text { font-style: italic; background-color: var(--colab=
-smartpaste-highlight-color); color: var(--colab-secondary-text-color) !imp=
ortant; }

.smartpaste-delete-text { font-style: italic; text-decoration: line-through=
; background-color: var(--colab-smartpaste-highlight-color); }

.code .lazy-editor { align-self: start; display: flex; -webkit-box-orient: =
vertical; -webkit-box-direction: normal; flex-flow: column; margin: 10px 8p=
x 0px 0px; }

.lazy-virtualized { display: flex; font-size: 14px; line-height: 19px; max-=
width: 100%; overflow-x: scroll; }

.lazy-virtualized-mobile { text-size-adjust: none; }

.lazy-virtualized-unstyled-scrollbars { overflow-x: hidden; padding-bottom:=
 10px; }

.lazy-virtualized .monaco-colorized { margin-left: 6px; white-space: pre; }

.lazy-virtualized::-webkit-scrollbar { height: 10px; width: 10px; }

.lazy-virtualized::-webkit-scrollbar-thumb { background-clip: border-box; b=
ackground-color: var(--colab-scrollbar-color); min-height: 28px; padding: 0=
px; }

.code .lazy-editor .monaco { margin: 0px; max-width: 100%; }

.monaco-editor .inline-variable-value { background: var(--colab-highlighted=
-surface-color); border-radius: 2px; color: var(--colab-secondary-text-colo=
r); font-style: italic; }

.monaco-editor .focused .wordHighlightText { opacity: 0.7; }

.monaco-editor .wordHighlightText { opacity: 0.3; }

.lazy-editor .lazy-gutter { color: var(--colab-secondary-text-color); white=
-space: pre; }

.collaborator-selection-start { position: absolute; border-left: var(--sele=
ction-color) solid 2px; border-top: var(--selection-color) solid 2px; borde=
r-bottom: var(--selection-color) solid 2px; height: 100%; box-sizing: borde=
r-box; }

.collaborator-selection-start::after { position: absolute; border: 3px soli=
d var(--selection-color); border-radius: 4px; left: -4px; top: -5px; }

.collaborator-selection { background-color: var(--selection-color); opacity=
: 0.5; }

.outputview { transition: height 0.2s; }

.viz-cell .outputview { transition: unset; }

.agent-focus-label { --md-icon-size: 16px; -webkit-box-align: center; align=
-items: center; background: var(--colab-primary-color); border-top-left-rad=
ius: 4px; border-top-right-radius: 4px; color: var(--colab-on-primary-color=
); gap: 4px; padding: 4px 8px 2px 6px; width: fit-content; display: none; }

.agent-focus-label { margin-left: -2px; }

.agent-focused .agent-focus-label { display: inline-flex; }

.agent-focused.cell .cell-gutter, .agent-focused.cell .main-content, .agent=
-focused.cell .markdown-toolbar { border-top-left-radius: 0px; }

.newly-added.code .main-content, .newly-added.text .editor-container { --co=
lab-primary-surface-color: var(--colab-composer-diff-background); --colab-s=
econdary-surface-color: var(--colab-composer-diff-background); }

.newly-added .main-content { --colab-editor-background: var(--colab-compose=
r-diff-background); }

.newly-added .main-content .monaco-editor { --vscode-editor-background: var=
(--colab-composer-diff-background); }

.newly-added .main-content .monaco-editor .margin { background-color: var(-=
-colab-composer-diff-background); }

.newly-added .main-content .cell-gutter, .newly-added .main-content .editor=
-container, .newly-added .main-content .formview { background-color: var(--=
colab-composer-diff-background); }

.inputarea-toolbar { border: 1px solid var(--colab-border-color); }

.output-show-output { --md-text-button-container-height: 28px; --md-text-bu=
tton-leading-space: 12px; --md-text-button-trailing-space: 12px; --md-text-=
button-with-leading-icon-trailing-space: 12px; --md-text-button-with-traili=
ng-icon-leading-space: 12px; --md-text-button-with-leading-icon-leading-spa=
ce: 8px; --md-text-button-with-trailing-icon-trailing-space: 8px; --md-text=
-button-icon-size: 20px; --md-focus-ring-outward-offset: -2px; }

body.prism-mode-loading::after { content: ""; position: fixed; top: 0px; le=
ft: 0px; width: 100vw; height: 100vh; background-color: var(--colab-primary=
-surface-color); z-index: 9998; }

body.prism-mode-active .prism-mode-output { background: var(--colab-primary=
-surface-color); height: 100vh; left: 0px; position: fixed; top: 0px; width=
: 100vw; z-index: 9999; }

body.prism-mode-active .prism-mode-output iframe { height: 100%; width: 100=
%; }

body.prism-mode-active .close-prism-btn { position: fixed; right: 16px; top=
: 16px; z-index: 10000; background-color: var(--colab-primary-surface-color=
); border-radius: 50%; box-shadow: rgba(0, 0, 0, 0.3) 0px 2px 5px; --md-sys=
-color-on-surface-variant: var(--colab-primary-text-color); }

label:has(md-checkbox) { display: inline-flex; place-items: center; }

label md-checkbox { flex-shrink: 0; }

md-checkbox::part(focus-ring) { height: 30px; width: 30px; }

.collaborator1 { --selection-color: #fd00ff; }

.collaborator2 { --selection-color: #4461f5; }

.collaborator3 { --selection-color: #66f96b; }

.collaborator4 { --selection-color: #ffe942; }

.collaborator5 { --selection-color: #ff6642; }

.collaborator6 { --selection-color: #42caff; }

.comment-input-text { box-sizing: border-box; font-family: sans-serif; font=
-size: var(--colab-chrome-font-size); line-height: 1.4; min-height: 36px; o=
utline: 0px; overflow: hidden; padding: 7px 8px; resize: none; width: 100%;=
 }

.bottom-buttons, .comment-input-text { border-radius: 4px; }

.comment .comment-action-button, .comment .comment-action-dropdown, .commen=
t .comment-date, .comment .comment-toggle-button { visibility: hidden; }

.comment.in-drive .comment-action-button, .comment.in-drive .comment-action=
-dropdown, .comment.in-drive .comment-date, .comment.in-drive .comment-togg=
le-button { visibility: visible; }

.comment-input { display: none; }

.editing > .comment-input { display: block; }

.comment-author { font-family: var(--colab-google-sans-font-family); margin=
-left: 45px; font-weight: 500; font-size: var(--colab-chrome-font-size); }

.comment .comment-author { margin-top: 11px; }

.comment.in-drive .comment-author { margin-top: 0px; }

.comment-image { border-radius: 50%; float: left; height: 32px; overflow: h=
idden; width: 32px; --md-icon-size: 32px; }

.comment-date { margin-left: 45px; font-size: 8pt; color: var(--colab-secon=
dary-text-color); }

.comment-text { overflow-wrap: break-word; }

.comment-text.comment-collapsed-text { height: 71px; overflow-y: hidden; }

.editing > .comment-content .comment-text { display: none; }

.comment-content { margin: 12px 5px 12px 12px; }

.comment .comment-header { display: flex; margin-bottom: 4px; padding: 0px;=
 position: relative; }

.comment.in-drive .comment-header { padding: 4px; }

.comment-input { padding: 0px 12px 1px; }

.comment .comment-text-container { padding: 0px; }

.comment.in-drive .comment-text-container { padding: 0px 4px 12px; }

.comment-collapse-control { color: var(--colab-anchor-color); cursor: point=
er; font-size: 8pt; padding: 4px 0px 2px; width: 100%; }

.comment-collapse-control:hover { text-decoration: underline; }

.reply-chain > .comment-input { padding-top: 4px; }

.show-more-replies { cursor: pointer; display: block; margin: 12px; padding=
: 4px 4px 12px; }

.submit-button { margin-right: 4px; --md-filled-button-container-height: 26=
px; }

.cancel-button { --md-text-button-container-height: 26px; }

.cancel-button, .submit-button { --md-focus-ring-outward-offset: -4px; }

.comment-action-button { font-size: 13px; height: 20px; margin: 0px; min-wi=
dth: 0px; opacity: 1; }

.comment-resolve-button { --md-icon-button-hover-state-layer-color: var(--c=
olab-icon-color); --md-icon-button-pressed-state-layer-color: var(--colab-i=
con-color); --md-sys-color-on-surface-variant: var(--colab-primary-color); =
}

.comment-action-dropdown { background: transparent; height: 20px; margin: 0=
px; min-width: 0px; opacity: 0.8; text-transform: none; }

.comment-action-dropdown { padding: 0px; width: 20px; }

.comment-header > .comment-buttons { display: flex; position: absolute; rig=
ht: 4px; top: 4px; }

.comment-buttons { -webkit-box-flex: 0; flex: 0 0 auto; }

.doc-comments-area > .comment > .reply-chain > .comment-input, .focused.in-=
drive > .reply-chain > .comment-input, .reply-chain > .comment-input.text-n=
ot-empty { display: block; }

.bottom-buttons { display: flex; padding-top: 8px; padding-bottom: 6px; hei=
ght: 32px; font-family: var(--colab-google-sans-font-family); font-size: 14=
px; font-weight: 500; }

.bottom-buttons, .comment-author { letter-spacing: 0.25px; line-height: 12p=
x; }

.sidebar { -webkit-box-flex: 0; flex: 0 0 260px; min-height: 100px; padding=
-left: 10px; padding-right: 20px; margin-right: 30px; }

.hide-comments .sidebar { display: none; }

.sidebar .comment { background: var(--colab-primary-surface-color); font-fa=
mily: sans-serif; font-size: var(--colab-chrome-font-size); font-weight: 40=
0; line-height: normal; margin-bottom: 5px; position: absolute; transition:=
 0.5s ease-in-out; width: 300px; }

.sidebar .comment.focused { box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 6px 2px=
, rgba(0, 0, 0, 0.3) 0px 1px 2px 0px; transform: translate(-10px); z-index:=
 50; }

.doc-comments-area { background: var(--colab-surface-container-color); bord=
er: 1px solid transparent; border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.=
15) 0px 2px 6px 2px, rgba(0, 0, 0, 0.3) 0px 1px 2px 0px; color: inherit; in=
set-inline-start: unset; max-height: 550px; outline: none; overflow-y: auto=
; padding: 0px; position: absolute; right: 20px; top: 57px; width: 434px; z=
-index: 987; }

.doc-comments-area.has-comments { padding-bottom: 18px; }

.doc-comments-area > .comment { background: var(--colab-primary-surface-col=
or); border: 1px solid transparent; border-radius: 8px; margin: 8px 18px 18=
px; padding: 4px; position: relative; transition: 0.5s ease-in-out; }

.doc-comments-area * .reply-chain { margin-left: 16px; }

.doc-comments-buttons { padding: 6px; text-align: right; }

.comment-fragment { display: block; position: relative; }

.sidebar > .comment-fragment { border: 1px solid var(--colab-border-color);=
 border-radius: 8px; }

.comment-author-info-container { -webkit-box-flex: 1; flex: 1 1 0%; }

.at-mention-message { color: var(--colab-secondary-text-color); margin: 4px=
; font-size: 12px; font-weight: 400; letter-spacing: 0.3px; line-height: 16=
px; }

.comment-content a { text-decoration: none; }

.comment-content a:hover { text-decoration: underline; }

.peoplekitThemeDark .peoplekitComponentsAutocompletePopupContainer { box-sh=
adow: rgba(0, 0, 0, 0.15) 0px 2px 6px 2px, rgba(0, 0, 0, 0.3) 0px 1px 2px 0=
px; --gm3-sys-color-background: var(--colab-primary-surface-color); }

.peoplekitComponentsAutocompletePopupContainer { max-width: 276px; }

.colab-comment-highlight-span { background-color: var(--colab-comment-highl=
ight-color); }

.doc-comments-area .comment-toggle-button { display: none; }

.comment-toggle-button { background: transparent; border: none; border-radi=
us: 8px; --md-focus-ring-shape: 8px; inset: 0px; position: absolute; pointe=
r-events: none; outline: none; }

@-webkit-keyframes corgis {=20
  0% { background-position: 120% center, -20% center, -20% center, 120% cen=
ter; }
  25% { background-position: -20% center, -20% center, -20% center, 120% ce=
nter; }
  30% { background-position: -20% center, -20% center, -20% center, 120% ce=
nter; }
  55% { background-position: -20% center, 120% center, -20% center, 120% ce=
nter; }
  65% { background-position: -20% center, 120% center, -20% center, 120% ce=
nter; }
  95% { background-position: -20% center, 120% center, 120% center, -20% ce=
nter; }
  100% { background-position: -20% center, 120% center, 120% center, -20% c=
enter; }
}

@keyframes corgis {=20
  0% { background-position: 120% center, -20% center, -20% center, 120% cen=
ter; }
  25% { background-position: -20% center, -20% center, -20% center, 120% ce=
nter; }
  30% { background-position: -20% center, -20% center, -20% center, 120% ce=
nter; }
  55% { background-position: -20% center, 120% center, -20% center, 120% ce=
nter; }
  65% { background-position: -20% center, 120% center, -20% center, 120% ce=
nter; }
  95% { background-position: -20% center, 120% center, 120% center, -20% ce=
nter; }
  100% { background-position: -20% center, 120% center, 120% center, -20% c=
enter; }
}

.basic-corgi-mode, .december-holiday-corgi-mode, .halloween-corgi-mode, .pr=
ide-corgi-mode { background-repeat: no-repeat; background-size: contain; an=
imation: 95s linear 0s infinite normal none running corgis; }

.basic-corgi-mode { background-image: url("../../v2/common/img/chocolatechi=
p.gif"), url("../../v2/common/img/oreo.gif"), url("../../v2/common/img/oreo=
.gif"), url("../../v2/common/img/redvelvet.gif"); }

.halloween-corgi-mode { background-image: url("../../v2/common/img/hallowee=
n_chocolatechip.gif"), url("../../v2/common/img/halloween_oreo.gif"), url("=
../../v2/common/img/halloween_oreo.gif"), url("../../v2/common/img/hallowee=
n_redvelvet.gif"); }

.december-holiday-corgi-mode { background-image: url("../../v2/common/img/h=
oliday_chocolatechip.gif"), url("../../v2/common/img/holiday_oreo.gif"), ur=
l("../../v2/common/img/holiday_oreo.gif"), url("../../v2/common/img/holiday=
_redvelvet.gif"); }

.pride-corgi-mode { background-image: url("../../v2/common/img/pride_chocol=
atechip.gif"), url("../../v2/common/img/oreo.gif"), url("../../v2/common/im=
g/oreo.gif"), url("../../v2/common/img/redvelvet.gif"); }

@-webkit-keyframes crabs {=20
  0% { background-position: -10% center; }
  5% { background-position: -10% center; }
  45% { background-position: 110% center; }
  50% { background-position: 110% center; }
  95% { background-position: -10% center; }
  100% { background-position: -10% center; }
}

@keyframes crabs {=20
  0% { background-position: -10% center; }
  5% { background-position: -10% center; }
  45% { background-position: 110% center; }
  50% { background-position: 110% center; }
  95% { background-position: -10% center; }
  100% { background-position: -10% center; }
}

.crab-mode { animation: 60s linear 0s infinite normal none running crabs; b=
ackground-repeat: no-repeat; background-size: contain; height: 100%; positi=
on: relative; width: 100%; }

.basic-crab { background-image: url("../../v2/common/img/crab.gif"); }

.christmas-crab { background-image: url("../../v2/common/img/christmas_crab=
.gif"); }

mwc-dialog.wide { --mdc-dialog-min-width: min(632px,99vw); }

mwc-dialog.very-wide { --mdc-dialog-min-width: min(750px,99vw); }

mwc-dialog.very-wide.colab-open-dialog { --mdc-dialog-min-width: min(900px,=
99vw); }

mwc-dialog md-text-button[dialogaction=3D"cancel"], mwc-dialog md-text-butt=
on[dialogaction=3D"close"] { --md-sys-color-primary: var(--colab-primary-te=
xt-color); }

mwc-dialog .buttons md-text-button, mwc-dialog md-text-button[slot=3D"prima=
ryAction"], mwc-dialog md-text-button[slot=3D"secondaryAction"] { --md-focu=
s-ring-outward-offset: -2px; }

md-dialog.wide { min-width: min(632px, 99vw); }

md-dialog.very-wide { min-width: min(750px, 99vw); }

md-dialog.very-wide.colab-open-dialog { min-width: min(900px, 99vw); }

md-dialog { max-height: min(700px, 98vh); }

.modal-dialog-bg { z-index: var(--colab-dialog-bg-z-index); }

.modal-dialog { background: rgb(255, 255, 255); border-color: rgb(218, 218,=
 218); box-shadow: rgba(0, 0, 0, 0.15) 0px 1px 3px 1px, rgba(0, 0, 0, 0.3) =
0px 1px 2px 0px; color: rgb(31, 31, 31); outline: none; padding: 4px 8px; z=
-index: var(--colab-dialog-z-index); }

.modal-dialog-title { background: rgb(255, 255, 255); }

.modal-dialog.share-client-error-dialog { background-color: rgb(255, 255, 2=
55); border-radius: 3px; font-family: arial, sans-serif; padding: 8px; posi=
tion: absolute; }

.modal-dialog-buttons { padding: 8px; text-align: center; }

mwc-dialog mwc-button[dialogaction=3D"cancel"], mwc-dialog mwc-button[dialo=
gaction=3D"close"] { --mdc-theme-primary: var(--colab-primary-text-color); =
}

.manage-views-dialog md-outlined-select { margin: 16px; }

.manage-views-dialog .buttons { margin-top: 30px; }

#error-dialog pre { background: var(--colab-editor-background); border: 1px=
 solid var(--colab-border-color); border-radius: 8px; font-family: var(--co=
lab-code-font-family); font-size: var(--colab-code-font-size); line-height:=
 21px; margin: 24px 0px 8px; max-height: 54px; overflow: auto; padding: 16p=
x; }

.copy-error-button { --md-text-button-container-height: 28px; --md-text-but=
ton-leading-space: 12px; --md-text-button-trailing-space: 12px; --md-text-b=
utton-with-leading-icon-trailing-space: 12px; --md-text-button-with-trailin=
g-icon-leading-space: 12px; --md-text-button-with-leading-icon-leading-spac=
e: 8px; --md-text-button-with-trailing-icon-trailing-space: 8px; --md-text-=
button-icon-size: 20px; }

#error-dialog .err-dialog-missing-field { background: var(--colab-editor-ba=
ckground); border: 1px solid var(--colab-border-color); border-radius: 8px;=
 font-family: var(--colab-code-font-family); overflow-x: auto; padding: 1px=
 4px; }

mwc-dialog a md-icon { --md-icon-size: 16px; vertical-align: text-bottom; }

.shortcut-dialog { --mdc-dialog-max-width: min(800px,99vw); --mdc-dialog-mi=
n-width: min(800px,99vw); }

.shortcut-dialog-content h3 { margin-bottom: 6px; margin-top: 6px; }

.shortcut-grid { display: flex; -webkit-box-orient: horizontal; -webkit-box=
-direction: normal; flex-flow: wrap; width: 100%; }

.shortcut-column { -webkit-box-flex: 1; flex: 1 0 0px; }

.shortcut-preference { display: flex; margin: 8px 0px; min-width: 350px; }

.shortcut-preference md-icon-button { margin-left: 10px; --md-icon-button-s=
tate-layer-height: 24px; --md-icon-button-state-layer-width: 24px; }

.shortcut-preference-keys { display: inline-block; margin-right: 8px; min-w=
idth: 120px; text-align: center; vertical-align: top; }

.shortcut-preference-keys input { text-align: center; width: 116px; }

.shortcut-preference-description { display: inline-block; max-width: 215px;=
 }

#shortcuts-reset { --md-focus-ring-outward-offset: -2px; }

.colab-request-dialog .preformatted { font-family: monospace; white-space: =
pre-wrap; }

.colab-request-dialog:has(.preformatted) { --mdc-dialog-min-width: 50vw; }

mwc-dialog .buttons { display: flex; -webkit-box-orient: horizontal; -webki=
t-box-direction: normal; flex-direction: row; -webkit-box-pack: end; justif=
y-content: flex-end; }

.code-cell-preview { white-space: pre; max-height: 500px; display: block; o=
verflow: auto; }

#preferences-dialog md-filled-select, #preferences-dialog md-filled-text-fi=
eld { margin-top: 10px; margin-bottom: 10px; }

#preferences-dialog .noFun { color: var(--colab-error-color); }

#preferences-dialog md-filled-select, #preferences-dialog md-filled-text-fi=
eld { min-width: 350px; }

colab-side-tab-dialog-page-viewer .right-content { box-sizing: border-box; =
width: 100%; }

colab-side-tab-dialog-page-viewer .upload-container { position: relative; }

.colab-side-tab-dialog { --mdc-dialog-min-width: 700px; min-width: 700px; }

.remove-dialog-content-padding [slot=3D"content"] { padding: 0px; }

.colab-side-tab-dialog > div[slot=3D"headline"] { padding-bottom: 8px; }

colab-side-tab-dialog-page-viewer .spinner { -webkit-box-align: center; ali=
gn-items: center; display: flex; -webkit-box-pack: center; justify-content:=
 center; min-height: 100px; }

@media only screen and (max-width: 800px) {
  .colab-side-tab-dialog { --mdc-dialog-min-width: 75vw; min-width: 75vw; }
}

mwc-dialog.colab-side-tab-dialog { --mdc-typography-headline6-font-family: =
var(
    --colab-google-sans-font-family
  ); }

colab-side-tab-dialog-page-viewer { display: block; height: 100%; }

colab-side-tab-dialog-page-viewer mwc-checkbox { display: flex; }

colab-side-tab-dialog-page-viewer md-list-item { --md-list-item-label-text-=
font: var(--colab-google-sans-font-family); --md-list-item-leading-space: 2=
4px; --md-list-item-trailing-space: 8px; --md-list-item-disabled-opacity: 0=
.6; }

colab-side-tab-dialog-page-viewer[smallviewport] md-list-item:hover { backg=
round-color: var(--colab-highlighted-surface-color); }

colab-side-tab-dialog-page-viewer md-list-item[tabindex=3D"0"] span { font-=
weight: 800; }

colab-side-tab-dialog-page-viewer md-list-item > md-icon { color: var(--col=
ab-icon-color); --md-icon-size: 30px; }

@media (forced-colors: active), (prefers-contrast: more) {
  colab-side-tab-dialog-page-viewer md-list-item:active, colab-side-tab-dia=
log-page-viewer md-list-item:focus, colab-side-tab-dialog-page-viewer md-li=
st-item:hover { outline: highlight solid 3px; outline-offset: -2px; }
}

mwc-dialog md-text-button.left-button { position: absolute; left: 0px; }

md-dialog md-text-button.left-button { position: absolute; left: 24px; }

colab-draggable { display: block; padding: 4px; position: relative; }

colab-drag-drop-target { display: block; margin: 0px 10px; min-height: 20px=
; min-width: 20px; }

colab-drag-drop-target.drop-target-selected { background-color: rgb(204, 20=
4, 204); min-height: 40px; min-width: 40px; }

.widget-area { display: flex; -webkit-box-orient: vertical; -webkit-box-dir=
ection: normal; flex-direction: column; gap: 12px; }

.widget-grid { display: grid; gap: 20px 16px; grid-template-columns: repeat=
(auto-fit,minmax(min(100%,max(25%,var(--colab-form-widget-min-width))),1fr)=
); }

.widget-grid:empty { display: none; }

colab-form-markdown + .widget-grid { margin-left: 16px; }

.single-column-form .widget-grid { grid-template-columns: 1fr; }

.both .widget-grid { --colab-form-widget-min-width: 200px; }

.form .widget-grid { --colab-form-widget-min-width: 400px; }

.formview-namelabel { overflow: hidden; text-overflow: ellipsis; white-spac=
e: nowrap; font-family: var(--colab-chrome-font-family); font-size: var(--c=
olab-chrome-font-size); font-weight: 500; line-height: 20px; }

.formview-edit-button { --md-focus-ring-outward-offset: -2px; --md-icon-but=
ton-icon-size: 20px; --md-icon-button-state-layer-height: 28px; --md-icon-b=
utton-state-layer-width: 28px; flex-shrink: 0; opacity: 0; transition: opac=
ity 0.3s linear; --md-sys-color-on-surface-variant: var(--colab-primary-col=
or); }

.editor-form-error, .form-widget-container, colab-form-markdown { -webkit-b=
ox-align: center; align-items: center; display: flex; gap: 4px; min-height:=
 28px; }

.editor-form-error:focus-within .formview-edit-button, .editor-form-error:h=
over .formview-edit-button, .form-widget-container:focus-within .formview-e=
dit-button, .form-widget-container:hover .formview-edit-button, colab-form-=
markdown:focus-within .formview-edit-button, colab-form-markdown:hover .for=
mview-edit-button { opacity: 1; }

.form-widget-container:has(> md-outlined-text-field) { -webkit-box-align: s=
tart; align-items: flex-start; }

.form-widget-container:has(> md-outlined-text-field) .formview-edit-button =
{ margin-top: 4px; }

.form .formview-edit-button, body.mobile .formview-edit-button { display: n=
one; }

.form .formview, body.mobile .formview { padding-left: 12px; padding-right:=
 12px; }

.toggle-code-button { --md-text-button-container-height: 28px; --md-text-bu=
tton-leading-space: 12px; --md-text-button-trailing-space: 12px; --md-text-=
button-with-leading-icon-trailing-space: 12px; --md-text-button-with-traili=
ng-icon-leading-space: 12px; --md-text-button-with-leading-icon-leading-spa=
ce: 8px; --md-text-button-with-trailing-icon-trailing-space: 8px; --md-text=
-button-icon-size: 20px; margin-left: -12px; --md-focus-ring-outward-offset=
: -2px; }

.editor-form-error { color: var(--colab-error-color); }

.formview-param-widget { display: flex; -webkit-box-orient: vertical; -webk=
it-box-direction: normal; flex-direction: column; gap: 4px; }

.formview-param-widget .editor-form-error { -webkit-box-align: start; align=
-items: flex-start; display: flex; font-size: 12px; min-height: 0px; paddin=
g: 0px 16px; }

.formview-param-widget:has(> .editor-form-error) md-outlined-select, .formv=
iew-param-widget:has(> .editor-form-error) md-outlined-text-field { --md-ou=
tlined-field-hover-outline-color: var(
    --colab-on-error-container-color
  ); --md-outlined-field-outline-color: var(--colab-error-color); }

.both .formview-param-widget .editor-form-error { padding-right: 48px; }

.formview-checkbox { -webkit-box-pack: center; justify-content: center; }

colab-form-title.formview-title { line-height: 1.4; margin: 0px 16px 0px 8p=
x; position: relative; }

colab-form-markdown hr, colab-form-title hr { margin: 8px 0px; }

colab-form-markdown > div > span > hr:first-child, colab-form-markdown > di=
v > span > p:first-child { margin-top: 0px; }

colab-form-markdown > div > span > hr:last-child, colab-form-markdown > div=
 > span > p:last-child { margin-bottom: 0px; }

.slider-container { -webkit-box-align: center; align-items: center; display=
: flex; -webkit-box-flex: 1; flex: 1 1 0%; }

.formview { background: var(--colab-primary-surface-color); overflow: auto =
hidden; padding: 8px 4px 8px 20px; }

.formview md-checkbox { flex-shrink: 0; margin-right: 8px; --md-checkbox-st=
ate-layer-size: 36px; }

.formview md-outlined-select, .formview md-outlined-text-field { -webkit-bo=
x-flex: 1; flex: 1 1 0%; min-width: 0px; --md-outlined-field-bottom-space: =
6px; --md-outlined-field-content-size: var(--colab-chrome-font-size); --md-=
outlined-field-content-space: 4px; --md-outlined-field-disabled-supporting-=
text-color: var(
    --colab-error-color
  ); --md-outlined-field-disabled-supporting-text-opacity: 1; --md-outlined=
-field-leading-space: 10px; --md-outlined-field-line-height: 24px; --md-out=
lined-field-top-space: 6px; --md-outlined-field-with-trailing-content-trail=
ing-space: 4px; }

.formview colab-input-dropdown { -webkit-box-flex: 1; flex: 1 1 0%; --colab=
-input-dropdown-button-horizontal-padding: 4px; --colab-input-dropdown-heig=
ht: 36px; }

.formview md-slider { -webkit-box-flex: 1; flex: 1 1 0%; min-inline-size: 0=
px; --md-slider-state-layer-size: 36px; }

.formview md-slider::part(focus-ring) { height: 30px; width: 30px; }

.formview input[type=3D"text"].range-output { background-color: var(--colab=
-primary-surface-color); border: none; font-family: var(--colab-chrome-font=
-family); font-size: var(--colab-chrome-font-size); outline: none; }

.formview input[type=3D"text"].range-output:disabled { opacity: 0.5; }

.formview input[type=3D"date"] { border-color: var(--colab-bold-border-colo=
r); border-radius: 4px; -webkit-box-flex: 1; flex: 1 1 0%; font-size: var(-=
-colab-chrome-font-size); line-height: 20px; padding: 6px; }

.formview input[type=3D"date"][disabled] { border-color: var(--colab-disabl=
ed-border-color); color: var(--colab-disabled-text-color); }

.formview input[type=3D"date"].error { border-color: var(--colab-error-colo=
r); }

html[theme=3D"dark"] .formview input[type=3D"date"] { color-scheme: dark; }

body:not(.mobile) .both .formview { border-left: 1px solid var(--colab-bord=
er-color); box-sizing: border-box; -webkit-box-flex: 0; flex-grow: 0; flex-=
shrink: 0; max-width: 50%; min-width: 50%; }

@media (orientation: portrait) {
  body.mobile .both .editor { min-width: 200px; -webkit-box-ordinal-group: =
2; order: 1; padding-left: 40px; }
  body.mobile .both .lazy-editor > .editor { padding-left: 0px; }
  body.mobile .both .formview { min-width: 200px; }
}

.inputarea.code > .formview { display: none; }

.colab-lasso-active { user-select: none; }

.colab-lasso { position: absolute; top: 0px; left: 0px; }

.lasso-handle { position: absolute; top: 0px; left: 0px; }

.lasso-selection { position: absolute; top: 0px; left: 0px; background: rgb=
a(0, 90, 255, 0.3); }

.edit-form-widget-dialog .dropdown-attributes colab-toolbar-button { displa=
y: flex; }

.edit-form-widget-dialog colab-scroller.dropdown-options-container { displa=
y: block; max-height: 220px; overflow: auto; padding: 0px 8px; }

.form-widget-attributes-container { min-height: 250px; min-width: 330px; pa=
dding: 0px 10px; }

.form-widget-attributes-container mwc-select, .form-widget-attributes-conta=
iner mwc-textarea, .form-widget-attributes-container mwc-textfield { margin=
-top: 16px; --mdc-typography-subtitle1-font-size: 16px; }

mwc-textfield.dropdown-option-input { margin-top: 2px; }

.edit-form-title-dialog .column { flex-basis: 50%; padding: 0px 20px 0px 0p=
x; }

.edit-form-title-dialog .column > * { width: 100%; }

.edit-form-title-dialog .form-width-container { -webkit-box-align: end; ali=
gn-items: flex-end; display: flex; }

.edit-form-title-dialog select { appearance: none; background-image: url("d=
ata:image/svg+xml;charset=3DUS-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w=
3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpat=
h%20fill%3D%22rgb%28155%2C155%2C155%29%22%20d%3D%22M287%2069.4a17.6%2017.6%=
200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200=
%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.=
4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200=
-5-1.9-9.2-5.5-12.8z%22/%3E%3C/svg%3E"); background-repeat: no-repeat, repe=
at; background-position: right 0.7em top 50%, 0px 0px; background-size: 0.5=
5em, 100%; background-color: var(--colab-primary-surface-color); border: 1p=
x solid transparent; color: var(--colab-primary-text-color); font-size: 16p=
x; margin: 8px 0px; padding: 0.6em 1.4em 0.5em 0.8em; }

@-webkit-keyframes kitty-mode-left-animation {=20
  0% { background-position: 110% center, 110% center; }
  15% { background-position: 110% center, 110% center; }
  35% { background-position: -10% center, 110% center; }
  50% { background-position: -10% center, 110% center; }
  65% { background-position: -10% center, 110% center; }
  85% { background-position: -10% center, 110% center; }
  100% { background-position: -10% center, -10% center; }
}

@keyframes kitty-mode-left-animation {=20
  0% { background-position: 110% center, 110% center; }
  15% { background-position: 110% center, 110% center; }
  35% { background-position: -10% center, 110% center; }
  50% { background-position: -10% center, 110% center; }
  65% { background-position: -10% center, 110% center; }
  85% { background-position: -10% center, 110% center; }
  100% { background-position: -10% center, -10% center; }
}

@-webkit-keyframes kitty-mode-right-animation {=20
  0% { background-position: 110% center, 110% center; }
  15% { background-position: 110% center, 110% center; }
  35% { background-position: 110% center, 110% center; }
  50% { background-position: 110% center, 110% center; }
  65% { background-position: -10% center, 110% center; }
  85% { background-position: -10% center, 110% center; }
  100% { background-position: -10% center, -10% center; }
}

@keyframes kitty-mode-right-animation {=20
  0% { background-position: 110% center, 110% center; }
  15% { background-position: 110% center, 110% center; }
  35% { background-position: 110% center, 110% center; }
  50% { background-position: 110% center, 110% center; }
  65% { background-position: -10% center, 110% center; }
  85% { background-position: -10% center, 110% center; }
  100% { background-position: -10% center, -10% center; }
}

@-webkit-keyframes kitty-mode-animation-slow {=20
  0% { background-position: 110% center; }
  100% { background-position: -10% center; }
}

@keyframes kitty-mode-animation-slow {=20
  0% { background-position: 110% center; }
  100% { background-position: -10% center; }
}

@-webkit-keyframes kitty-mode-animation-medium {=20
  0% { background-position: 110% center; }
  5% { background-position: 110% center; }
  95% { background-position: -10% center; }
  100% { background-position: -10% center; }
}

@keyframes kitty-mode-animation-medium {=20
  0% { background-position: 110% center; }
  5% { background-position: 110% center; }
  95% { background-position: -10% center; }
  100% { background-position: -10% center; }
}

@-webkit-keyframes kitty-mode-animation-fast {=20
  0% { background-position: 110% center; }
  10% { background-position: 110% center; }
  90% { background-position: -10% center; }
  100% { background-position: -10% center; }
}

@keyframes kitty-mode-animation-fast {=20
  0% { background-position: 110% center; }
  10% { background-position: 110% center; }
  90% { background-position: -10% center; }
  100% { background-position: -10% center; }
}

.stripes-kitty { background-image: url("../../v2/common/img/STRIPES.gif"); =
}

.kinako-kitty { background-image: url("../../v2/common/img/KINAKO.gif"); }

.midnight-kitty { background-image: url("../../v2/common/img/MIDNIGHT.gif")=
; }

.firefox-kitty { background-image: url("../../v2/common/img/FIREFOX.gif"); =
}

.maneki-kitty { background-image: url("../../v2/common/img/MANEKI.gif"); }

.valentin-kitty { background-image: url("../../v2/common/img/VALENTIN.gif")=
; }

.ghostpuffs-kitty { background-image: url("../../v2/common/img/GHOSTPUFFS.g=
if"); }

.psl-kitty { background-image: url("../../v2/common/img/PUMPKINSPICELATTE.g=
if"); }

.vampiregoth-kitty { background-image: url("../../v2/common/img/xX_vampireg=
oth91_Xx.gif"); }

.kace-kitty { background-image: url("../../v2/common/img/KACE.gif"); }

.ferris-kitty { background-image: url("../../v2/common/img/FERRIS.gif"); }

.sprinkles-kitty { background-image: url("../../v2/common/img/SPRINKLES.gif=
"); }

.kitty-mode-fast { animation: 40s linear 0s 1 normal none running kitty-mod=
e-animation-fast; }

.kitty-mode-medium { animation: 40s linear 0s 1 normal none running kitty-m=
ode-animation-medium; }

.kitty-mode-slow { animation: 40s linear 0s 1 normal none running kitty-mod=
e-animation-slow; }

.kitty-left { transform: scaleX(-1); }

.kitty-canvas { background-repeat: no-repeat; background-size: 73px 60px; h=
eight: 100%; left: 0px; pointer-events: none; position: absolute; top: 0px;=
 width: 100%; }

.power-overlay { height: 100%; left: 0px; pointer-events: none; position: a=
bsolute; top: 0px; width: 100%; z-index: 1; }

.power-label { background: linear-gradient(red, red) no-repeat text, darkre=
d; bottom: 30px; color: transparent; display: block; font-family: impact; f=
ont-size: 24pt; pointer-events: none; position: absolute; right: 30px; z-in=
dex: 3; -webkit-text-stroke: 2px rgb(0, 0, 0); }

.power-label-clone { background-image: none; background-position: initial; =
background-size: initial; background-repeat: initial; background-attachment=
: initial; background-origin: initial; background-color: initial; color: re=
d; z-index: 2; transition-property: margin-bottom, opacity; margin-bottom: =
0px; opacity: 1; background-clip: unset; }

body.power-mode-enabled .notebook-vertical { overflow: hidden; }

@media print {
  body { overflow-y: visible !important; }
  .notebook-vertical { position: static !important; height: auto !important=
; }
  .notebook-container { height: auto !important; position: static !importan=
t; overflow-y: initial !important; }
  .notebook-content { border: initial !important; margin: initial !importan=
t; min-width: 0px !important; }
  .notebook-content-background, .notebook-tab-content { min-width: 0px !imp=
ortant; }
  #top-toolbar, .add-cell > *, .cell-toolbar, .footer-links, .top-floater, =
colab-composer-floating-spark, colab-composer[view-mode=3D"floating"], cola=
b-left-pane, colab-resizer:has(colab-tab-pane), colab-snackbar, colab-statu=
s-bar { display: none !important; }
  .cell-gutter, colab-output-info { visibility: hidden !important; }
}

.colab-find-suffix { color: var(--colab-secondary-text-color); }

colab-left-pane .colab-find-suffix { margin: auto 0px; }

colab-find-replace.readonly .colab-find-replace, colab-find-replace.readonl=
y .colab-replace-input { display: none; }

colab-find-replace { gap: 12px; overflow: hidden; padding-bottom: 6px; --md=
-focus-ring-outward-offset: -3px; }

colab-find-replace .colab-find-button { margin-left: 0px; margin-right: 0px=
; padding-left: 4px; padding-right: 4px; }

@media (forced-colors: active) {
  colab-find-replace md-text-button { --md-text-button-focus-label-text-col=
or: Highlight; --md-text-button-hover-label-text-color: Highlight; --md-tex=
t-button-pressed-label-text-color: Highlight; }
}

colab-find-replace label:has(md-checkbox) { margin-right: 16px; }

colab-find-results { flex-shrink: 1; min-height: 40px; overflow: auto; }

colab-find-results:not(:hover, :focus-within) { --colab-scrollbar-color: tr=
ansparent; }

colab-find-results md-list { -webkit-box-flex: 1; flex-grow: 1; overflow: h=
idden; --md-list-item-one-line-container-height: 39px; --md-list-item-top-s=
pace: 2px; --md-list-item-bottom-space: 2px; --md-focus-ring-outward-offset=
: -2px; }

.find-replace-result { display: flex; -webkit-box-orient: horizontal; -webk=
it-box-direction: normal; flex-direction: row; min-height: 31px; }

.find-replace-result.active-selected { background-color: var(--colab-highli=
ghted-surface-color); }

.find-replace-result div { overflow: hidden; text-overflow: ellipsis; white=
-space: nowrap; font-family: var(--colab-code-font-family); font-size: 13px=
; min-width: 0px; }

.find-replace-result md-icon-button { margin: 0px; padding: 0px; display: n=
one; --md-icon-button-icon-size: 20px; --md-icon-button-state-layer-height:=
 30px; --md-icon-button-state-layer-width: 36px; }

.find-replace-result:focus-within md-icon-button, .find-replace-result:hove=
r md-icon-button { display: flex; }

colab-resizer { display: flex; }

colab-resizer.ew-resize, colab-resizer.we-resize { -webkit-box-orient: hori=
zontal; -webkit-box-direction: normal; flex-flow: row; }

colab-resizer.ns-resize, colab-resizer.sn-resize { -webkit-box-orient: vert=
ical; -webkit-box-direction: normal; flex-flow: column; }

colab-resizer > * { -webkit-box-flex: 1; flex-grow: 1; }

colab-resizer .ns-resize .resizer-contents, colab-resizer .sn-resize .resiz=
er-contents { height: calc(100% - 5px); }

colab-resizer.ew-resize > *, colab-resizer.we-resize > * { min-width: 0px; =
}

.resizer-thumb { -webkit-box-flex: 0; flex: 0 0 5px; transition: background=
 0.1s; }

.resizer-thumb:hover { background: var(--colab-bold-border-color); }

colab-resizer.ew-resize > .resizer-thumb, colab-resizer.we-resize > .resize=
r-thumb { cursor: ew-resize; }

colab-resizer.ns-resize > .resizer-thumb, colab-resizer.sn-resize > .resize=
r-thumb { cursor: ns-resize; height: 5px; }

colab-resizer.no-resize > .resizer-thumb { display: none; }

colab-resizing-grid { border-collapse: collapse; display: table; position: =
relative; width: 100%; }

.resizing-thumb { bottom: 0px; display: none; position: absolute; top: 0px;=
 width: 4px; }

.resizing-grid-column-group { display: table-column-group; }

.resizing-grid-column { display: table-column; }

.resizing-grid-row { display: table-row; }

.resizing-grid-cell { display: table-cell; height: 50px; padding: 2px; vert=
ical-align: top; }

colab-resizing-grid.resizing .resizing-thumb { cursor: ew-resize; }

colab-resizing-grid.resizing .resizing-thumb:active, colab-resizing-grid.re=
sizing .resizing-thumb:hover { border-left: 2px solid rgb(0, 0, 0); }

colab-resizing-grid.resizing .resizing-grid-cell { border: 1px dashed rgb(0=
, 0, 0); }

colab-resizing-grid.resizing .resizing-thumb { display: block; }

.screenreader-only { border: 0px; clip: rect(0px, 0px, 0px, 0px); clip-path=
: inset(50%); height: 1px; margin: -1px; overflow: hidden; padding: 0px; po=
sition: absolute; white-space: nowrap; width: 1px; }

::-webkit-scrollbar { height: 12px; width: 12px; }

::-webkit-scrollbar-button { height: 0px; width: 0px; }

::-webkit-scrollbar-corner { background: transparent; }

::-webkit-scrollbar-thumb { background-clip: content-box; background-color:=
 var(--colab-scrollbar-color); border: 2px solid transparent; border-radius=
: 8px; min-height: 28px; min-width: 28px; }

::-webkit-scrollbar-thumb:hover { background-color: var(--colab-scrollbar-h=
over-color); }

::-webkit-scrollbar-thumb:active { background-color: var(--colab-scrollbar-=
active-color); }

@supports not (selector(::-webkit-scrollbar)) {
  * { scrollbar-color: var(--colab-scrollbar-color) transparent; }
}

.text.has-statusbar:not(.edit) .monaco-emacs-statusbar, .text.has-statusbar=
:not(.edit) .monaco-vim-statusbar { display: none !important; }

.markdown a.error { color: var(--colab-error-color); text-decoration: under=
line dashed var(--colab-error-color); }

.text.edit .markdown a:not(.error) { color: var(--colab-anchor-color); }

.markdown-toolbar-preview[active] { font-weight: 700; }

.markdown span table { border-collapse: collapse; border-spacing: 0px; bord=
er: none; font-size: 12px; margin-left: 8px; table-layout: fixed; }

.markdown span thead { border-bottom: 1px solid rgb(0, 0, 0); vertical-alig=
n: bottom; }

.markdown span td, .markdown span th, .markdown span tr { overflow: hidden;=
 text-overflow: ellipsis; white-space: nowrap; border: none; line-height: 1=
; padding: 0.5em; vertical-align: middle; }

.markdown span th { font-weight: 700; }

.markdown span tbody tr:nth-child(2n+1) { background: var(--colab-secondary=
-surface-color); }

.markdown span tbody tr:hover { background: var(--colab-highlighted-surface=
-color); }

body.mobile .markdown > span > p, body.mobile .markdown > span > table { di=
splay: block; width: 100%; }

body.mobile .markdown > span > table { overflow-x: auto; }

.markdown { line-height: 1.6; }

.markdown ol, .markdown p, .markdown ul { font-size: 16px; margin-bottom: 0=
.5em; margin-top: 0.5em; }

.markdown h1, .markdown h2, .markdown h3, .markdown h4, .markdown h5, .mark=
down h6 { font-weight: 400; margin-bottom: 0.5em; margin-top: 0.5em; }

.formview .markdown h1, .formview .markdown h2, .formview .markdown h3, .fo=
rmview .markdown h4, .formview .markdown h5, .formview .markdown h6 { margi=
n-bottom: 0px; margin-top: 0px; }

.markdown h1 { font-size: 26px; }

.markdown h2 { font-size: 23px; }

.markdown h3 { font-size: 20px; }

.markdown h4 { font-size: 18px; }

.markdown h5, .markdown h6 { font-size: 16px; }

.markdown :not(pre) > code { background: var(--colab-editor-background); bo=
rder: 1px solid var(--colab-border-color); border-radius: 8px; font-family:=
 var(--colab-code-font-family); overflow-x: auto; padding: 1px 4px; }

.markdown pre { background: var(--colab-editor-background); border: 1px sol=
id var(--colab-border-color); border-radius: 8px; font-family: var(--colab-=
code-font-family); overflow-x: auto; font-size: var(--colab-code-font-size)=
; padding: 8px; margin: 1em 0px; white-space: pre; }

.cell-tab .header-section-toggle, .cell-tab .markdown-toolbar-preview, .cel=
l-tab .text.edit .text-top-div, colab-cell-pair-slide .header-section-toggl=
e, colab-cell-pair-slide .markdown-toolbar-preview, colab-cell-pair-slide .=
text.edit .text-top-div, colab-cell-slide .header-section-toggle, colab-cel=
l-slide .markdown-toolbar-preview, colab-cell-slide .text.edit .text-top-di=
v { display: none; }

.cell-tab .text.edit .editor-container:not(.horizontal) .editor, colab-cell=
-pair-slide .text.edit .editor-container:not(.horizontal) .editor, colab-ce=
ll-slide .text.edit .editor-container:not(.horizontal) .editor { border-bot=
tom: none; }

.cell-tab .text.edit .main-content, colab-cell-pair-slide .text.edit .main-=
content, colab-cell-slide .text.edit .main-content { border-radius: 8px; ou=
tline: 1px solid var(--colab-border-color); overflow: hidden; }

.cell-tab .text.edit:has(.monaco-editor.focused) .main-content, colab-cell-=
pair-slide .text.edit:has(.monaco-editor.focused) .main-content, colab-cell=
-slide .text.edit:has(.monaco-editor.focused) .main-content { outline: 2px =
solid var(--colab-focus-ring-color); }

.markdown .markdown-google-sans { font-family: var(--colab-google-sans-font=
-family); }

.md-recitation { margin-top: 4px; }

.md-recitation ol { font-size: var(--colab-chrome-font-size); }

#top-toolbar { background-color: var(--colab-surface-container-color); bord=
er-radius: 100px; gap: 4px; margin: 0px 12px; overflow: clip; padding: 4px =
8px; position: relative; --colab-split-button-container-shape: 9999px; --md=
-focus-ring-outward-offset: -2px; }

#top-toolbar.collapsed { margin-top: 8px; }

#top-toolbar md-icon-button { --md-focus-ring-outward-offset: -2px; --md-ic=
on-button-icon-size: 20px; --md-icon-button-state-layer-height: 28px; --md-=
icon-button-state-layer-width: 28px; --md-sys-color-on-surface-variant: var=
(--colab-primary-text-color); }

#top-toolbar md-icon-button[toggle] { --md-sys-color-primary: var(--colab-p=
rimary-text-color); }

#top-toolbar .toolbar-add-code-split md-icon-button { --md-icon-button-icon=
-size: 20px; --md-icon-button-state-layer-height: 32px; --md-icon-button-st=
ate-layer-width: 24px; --md-icon-button-state-layer-shape: 0 var(--colab-sp=
lit-button-container-shape,4px) var(--colab-split-button-container-shape,4p=
x) 0; --md-sys-color-on-surface-variant: var(--colab-primary-text-color); }

#top-toolbar .toolbar-add-code-split md-icon-button::part(focus-ring) { --m=
d-focus-ring-shape-start-start: 0; --md-focus-ring-shape-start-end: var(--c=
olab-split-button-container-shape,4px); --md-focus-ring-shape-end-end: var(=
--colab-split-button-container-shape,4px); --md-focus-ring-shape-end-start:=
 0; }

body.mobile #top-toolbar { padding: 0px 2px; }

body.mobile #top-toolbar colab-toolbar-button md-icon { --md-icon-size: 20p=
x; vertical-align: middle; }

#top-toolbar .collapsed-options { display: none; }

#top-toolbar.collapsed .expanded-options { display: none; }

#top-toolbar .expanded-options, #top-toolbar.collapsed .collapsed-options {=
 -webkit-box-align: center; align-items: center; display: inline-flex; gap:=
 4px; }

#top-toolbar.collapsed colab-permissions-button { display: none; }

#top-toolbar colab-last-saved-indicator { margin-left: 16px; }

.colab-separator { background: var(--colab-border-color); height: 20px; wid=
th: 1px; }

.toolbar-add-code-split { display: flex; -webkit-box-align: center; align-i=
tems: center; }

#top-toolbar .embedded-branch-indicator { -webkit-box-align: center; align-=
items: center; background-color: var(--colab-surface-container-highest-colo=
r); border-radius: 8px; display: flex; gap: 4px; padding: 4px; }

#top-toolbar .embedded-branch-indicator md-icon { color: var(--colab-icon-c=
olor); --md-icon-size: 18px; }

#view-editor colab-drag-drop-target.drop-target-selected { min-height: 100p=
x; }

.hidden-cell-pane colab-drag-drop-target { display: none; }

#view-editor #view-name { height: 34px; margin: 10px 12px 0px; --md-outline=
d-field-bottom-space: 6px; --md-outlined-field-leading-space: 10px; --md-ou=
tlined-field-top-space: 6px; }

#view-editor colab-drag-drop-zone { display: block; min-height: 100%; }

#view-editor colab-tab-layout colab-drag-drop-zone { border: 1px dashed rgb=
(0, 0, 0); }

#view-editor-hide-code-option { margin-left: 8px; }

#view-editor .edit-view-buttons { background: var(--colab-primary-surface-c=
olor); -webkit-box-flex: 0; flex: 0 0 0%; float: left; overflow: hidden; po=
sition: sticky; top: 0px; width: 30px; --md-icon-button-state-layer-height:=
 30px; --md-icon-button-state-layer-width: 30px; }

.draggable-cell > .view-draggable-paper > .edit-view-buttons .view-layout-c=
ontrol, .draggable-grid > .view-draggable-paper > .edit-view-buttons .view-=
cell-control, .draggable-tabs > .view-draggable-paper > .edit-view-buttons =
.view-cell-control, .hidden-cell-pane .view-move, .hidden-cell-pane .view-r=
emove, .notebook-content .view-add, .notebook-content .view-drag { display:=
 none; }

#view-editor .draggable-content { -webkit-box-flex: 1; flex: 1 1 0%; margin=
-left: 30px; min-height: 88px; overflow: hidden; padding: 4px; position: re=
lative; }

#view-editor .draggable-cell-mask { cursor: move; }

#view-editor .draggable-cell-mask { inset: 0px; position: absolute; }

#view-editor .cell { z-index: 0; }

#view-editor .notebook-content { margin: 8px; padding: 0px 2px; }

#view-editor .view-header { padding-left: 8px; }

#view-editor .view-header .buttons { display: none; }

.notebook-cell-list > colab-drag-drop-zone > colab-drag-drop-target:last-of=
-type { min-height: 200px; }

.view-editor-toolbar { background-color: var(--colab-secondary-surface-colo=
r); order: -1; position: relative; }

.cells-not-in-view { overflow-y: auto; }

.view-controls { -webkit-box-align: center; align-items: center; display: f=
lex; -webkit-box-flex: 1; flex-grow: 1; margin: 4px; }

.view-editor-cancel-button, .view-editor-save-button { margin: 4px; padding=
: 13px 0px; }

.view-draggable-paper { overflow: auto; }

.hidden-cell-pane colab-resizer { height: 150px; min-height: 150px; max-hei=
ght: 500px; overflow: auto; }

.hidden-cell-pane .resizer-contents { display: flex; -webkit-box-orient: ve=
rtical; -webkit-box-direction: normal; flex-flow: column; margin-left: 18px=
; }

.hidden-cell-pane-title { flex-shrink: 0; padding: 0px 4px 0px 0px; }

.hidden-cell-pane-title h2 { -webkit-box-flex: 1; flex-grow: 1; margin: 4px=
 12px 0px; }

.hidden-cell-pane .cells-not-in-view { overflow-y: auto; }

.hidden-cell-pane .view-draggable-paper { background: var(--colab-primary-s=
urface-color); display: block; margin-left: 8px; margin-right: 8px; }

#view-hidden-cells-button[active] { font-weight: 700; }

md-outlined-text-field.number-of-columns-input, md-outlined-text-field.numb=
er-of-rows-input { padding-top: 20px; }

.view-header { padding: 0px 26px 16px 30px; position: relative; }

.view-header h1 { -webkit-box-flex: 1; flex-grow: 1; }

.view-header md-icon { margin: 0px 8px; vertical-align: middle; }

.layouts-view .layout-grid table { width: 100%; }

.layouts-view .layout-grid td { vertical-align: top; }

.layout-grid img, .layout-tab img { max-width: 100%; }

.layouts-view colab-tab-layout { margin-top: 12px; }

.layouts-view .cell-toolbar, .views-hide-code .cell.code:not(.code-has-outp=
ut) { display: none; }

.notebook-vertical { height: 100%; display: flex; -webkit-box-orient: verti=
cal; -webkit-box-direction: normal; flex-flow: column; }

.notebook-vertical:not(.embedded) { background-color: var(--colab-surface-c=
ontainer-low-color); }

.notebook-horizontal { background-color: var(--colab-primary-surface-color)=
; display: flex; -webkit-box-orient: horizontal; -webkit-box-direction: nor=
mal; flex-flow: row; -webkit-box-flex: 1; flex-grow: 1; overflow: clip; pos=
ition: relative; min-height: 0px; }

.notebook-vertical:not(.embedded) .notebook-horizontal { background-color: =
transparent; margin: 8px 12px; }

.notebook-horizontal > div.layout.vertical { flex-shrink: 1; min-width: 200=
px; }

.exported-html .notebook-horizontal { overflow: visible; }

.overflow-flexbox-workaround { flex-basis: 50%; -webkit-box-orient: vertica=
l; -webkit-box-direction: normal; flex-flow: column; -webkit-box-flex: 1; f=
lex-grow: 1; position: relative; }

.notebook-container { height: 100%; overflow-y: scroll; position: absolute;=
 width: 100%; }

.notebook-container:not(:hover, :focus-within) { --colab-scrollbar-color: t=
ransparent; }

.notebook-container:focus { outline: none; }

.exported-html .notebook-container { overflow-y: initial; }

.exported-html .top-floater { display: none; }

.notebook-scrolling-horizontal { display: flex; -webkit-box-orient: horizon=
tal; -webkit-box-direction: normal; flex-flow: row; padding-bottom: 400px; =
-webkit-box-flex: 1; flex: 1 1 0%; }

.notebook-scrolling-horizontal-container { display: flex; -webkit-box-orien=
t: vertical; -webkit-box-direction: normal; flex-direction: column; height:=
 100%; }

.notebook-content-background { -webkit-box-flex: 1; flex: 1 1 auto; min-wid=
th: calc(var(--colab-notebook-content-min-width) + 100px); --colab-notebook=
-content-min-width: 300px; }

body.mobile .notebook-content-background { --colab-notebook-content-min-wid=
th: 150px; }

.notebook-content { background-color: var(--colab-primary-surface-color); d=
isplay: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; =
flex-direction: column; margin: 7px 0px 5px; min-height: 800px; min-width: =
var(--colab-notebook-content-min-width); padding: 2px 4px 8px 44px; }

.notebook-vertical:not(.embedded) .notebook-content { background-color: tra=
nsparent; padding-left: 38px; padding-top: 1px; }

.notebook-content.readonly { padding-top: 17px; }

.notebook-content.readonly .cell { margin-top: 8px; }

.notebook-cell-list { background: var(--colab-primary-surface-color); }

colab-snackbar md-icon-button { --md-sys-color-on-surface-variant: var(--co=
lab-inverse-on-surface-color); }

colab-snackbar md-text-button { --md-sys-color-primary: var(--colab-inverse=
-primary-color); }

.code-help { font-family: var(--colab-code-font-family); margin: 16px; whit=
e-space: pre-wrap; }

.code-help a:link { text-decoration: none; }

.code-help a:visited { text-decoration: none; }

.code-help a:hover { text-decoration: underline; }

.code-help a:active { text-decoration: underline; }

.notebook-busy { cursor: progress; }

[hidden] { display: none; }

.layout.horizontal { display: flex; -webkit-box-orient: horizontal; -webkit=
-box-direction: normal; flex-direction: row; }

.layout.noshrink { flex-shrink: 0; }

.layout.grow { -webkit-box-flex: 1; flex-grow: 1; }

.layout.vertical { display: flex; -webkit-box-orient: vertical; -webkit-box=
-direction: normal; flex-direction: column; }

.layout.center { -webkit-box-align: center; align-items: center; }

.layout.end { -webkit-box-align: end; align-items: flex-end; }

.flex { -webkit-box-flex: 1; flex: 1 1 0%; }

.nowrap { white-space: nowrap; }

.colab-large-icon { height: 60px; width: 40px; }

a { color: var(--colab-anchor-color); }

.proxies { height: 0px; overflow: hidden; }

.proxies iframe { border: 0px; display: none; height: 1px; position: absolu=
te; inset: -9999px; width: 1px; }

.footer-links { padding: 8px 0px; text-align: center; }

.footer-links a { margin: 0px 4px; text-decoration: none; }

md-icon[filled] { font-variation-settings: "FILL" 1; }

md-filled-text-field.space-for-label, md-outlined-text-field.space-for-labe=
l { margin-top: 12px; }

input[type=3D"date"], input[type=3D"text"], textarea { background-color: va=
r(--colab-primary-surface-color); border: 1px solid var(--colab-bold-border=
-color); color: var(--colab-primary-text-color); padding: 2px 1px; }

::-webkit-input-placeholder { color: var(--colab-secondary-text-color); }

::placeholder { color: var(--colab-secondary-text-color); }

html { height: 100%; }

body { background-color: var(--colab-primary-surface-color); color: var(--c=
olab-primary-text-color); font-family: var(--colab-chrome-font-family); fon=
t-size: var(--colab-chrome-font-size); font-weight: 400; height: 100%; line=
-height: 1.24; margin: 0px; overflow-y: hidden; }

body.exported-html { overflow-y: visible; }

h1, h2, h3, h4, h5, h6 { color: var(--colab-primary-text-color); font-weigh=
t: 700; margin-bottom: 4px; }

mark { background-color: var(--colab-highlight-color); color: var(--colab-p=
rimary-text-color); }

p, ul { color: var(--colab-primary-text-color); margin-bottom: 6px; margin-=
top: 6px; }

pre { color: var(--colab-primary-text-color); margin-bottom: 0px; margin-to=
p: 0px; }

body > .onegoogle { display: none; }

.colab-icon { color: var(--colab-icon-color); }

.grecaptcha-badge { display: none; }

mwc-textfield[outlined] { --mdc-typography-subtitle1-font-size: 16px; }

mwc-formfield { --mdc-theme-text-primary-on-background: var(--colab-primary=
-text-color); --mdc-theme-secondary: var(--colab-primary-color); --mdc-ripp=
le-focus-opacity: 0.15; }

mwc-formfield[disabled] { --mdc-theme-text-primary-on-background: var(--col=
ab-disabled-text-color); }

@media (forced-colors: active) {
  body { --md-filled-button-hover-label-text-color: Highlight; --md-filled-=
button-pressed-label-text-color: Highlight; --md-filled-button-focus-label-=
text-color: Highlight; --md-filled-button-hover-icon-color: Highlight; --md=
-filled-button-pressed-icon-color: Highlight; --md-filled-button-focus-icon=
-color: Highlight; --md-text-button-hover-label-text-color: Highlight; --md=
-text-button-pressed-label-text-color: Highlight; --md-text-button-focus-la=
bel-text-color: Highlight; --md-text-button-hover-icon-color: Highlight; --=
md-text-button-pressed-icon-color: Highlight; --md-text-button-focus-icon-c=
olor: Highlight; --md-outlined-button-hover-label-text-color: Highlight; --=
md-outlined-button-pressed-label-text-color: Highlight; --md-outlined-butto=
n-focus-label-text-color: Highlight; --md-outlined-button-hover-icon-color:=
 Highlight; --md-outlined-button-pressed-icon-color: Highlight; --md-outlin=
ed-button-focus-icon-color: Highlight; }
}

colab-github-repo-selector .github-repos { margin-right: 40px; }

colab-github-repo-selector md-filled-select { width: 100%; max-width: 300px=
; }

colab-github-repo-selector .open-in-github { vertical-align: middle; }

.github-scope-selector { margin: 0px 8px; display: flex; }

md-icon-button[href] md-icon { color: var(--colab-anchor-color); font-weigh=
t: 400; }

colab-file-browser { -webkit-box-flex: 1; flex-grow: 1; overflow-y: auto; }

.file-browser-message { padding-bottom: 8px; }

colab-file-tree { display: flex; -webkit-box-orient: vertical; -webkit-box-=
direction: normal; flex-flow: column; -webkit-box-flex: 1; flex-grow: 1; ov=
erflow-y: auto; position: relative; }

colab-file-tree:not(:hover, :focus-within) { --colab-scrollbar-color: trans=
parent; }

colab-file-tree .files-drag-to-upload.layout { background: var(--colab-prim=
ary-surface-color); border: 2px dashed var(--colab-border-color); bottom: 2=
8px; display: flex; font-size: small; left: 12px; opacity: 0; padding: 4px =
8px; pointer-events: none; position: absolute; right: 18px; transition: opa=
city 0.2s ease-in; }

colab-file-tree.file-hovered .files-drag-to-upload { opacity: 1; }

colab-file-tree .files-drag-to-upload * { margin: auto; }

.file-tree-composer-banner { -webkit-box-align: center; align-items: center=
; background: var(--colab-primary-container-color); border-radius: 8px; dis=
play: flex; gap: 8px; -webkit-box-pack: justify; justify-content: space-bet=
ween; margin: 8px 16px; padding: 12px 16px; }

.file-tree-composer-banner-text { -webkit-box-flex: 2; flex-grow: 2; }

.file-tree-composer-banner-close { flex-shrink: 0; --md-icon-button-icon-si=
ze: 20px; --md-sys-color-on-surface-variant: var(--colab-primary-color); }

.file-tree-buttons { --md-focus-ring-outward-offset: -2px; --md-icon-button=
-icon-size: 20px; --md-icon-button-state-layer-height: 24px; --md-icon-butt=
on-state-layer-width: 24px; -webkit-box-align: center; align-items: center;=
 background-color: var(--colab-surface-container-highest-color); border-rad=
ius: 20px; display: flex; gap: 4px; margin-bottom: 4px; padding: 4px; --col=
ab-icon-color: var(--colab-primary-text-color); --md-sys-color-on-surface-v=
ariant: var(--colab-primary-text-color); --md-sys-color-primary: var(--cola=
b-primary-text-color); }

label:has(.file-tree-upload-button) { height: 24px; }

colab-file-tree #file-tree-upload-input { display: none; }

colab-file-tree .files-root { -webkit-box-flex: 1; flex-grow: 1; overflow-y=
: auto; }

colab-file-tree .files-root:not(:hover, :focus-within) { --colab-scrollbar-=
color: transparent; }

.files-root > colab-file-view { height: 100%; }

colab-file-view { display: block; }

colab-file-view span { user-select: none; }

colab-file-tree .file-icon { flex-shrink: 0; --md-icon-size: 24px; width: 2=
4px; }

colab-file-tree .file-title-row { -webkit-box-align: center; align-items: c=
enter; cursor: pointer; display: flex; gap: 4px; height: 32px; overflow: hi=
dden; }

colab-file-tree .hidden-file { opacity: 0.7; }

colab-file-tree .file-title-row:hover, colab-file-view.focused, colab-file-=
view.hovered > .file-title-row, colab-file-view[active] > .file-title-row {=
 background: var(--colab-highlighted-surface-color); }

colab-file-view .file-title-row colab-file-progress { height: 20px; width: =
20px; }

colab-file-view .directory-icon { transition: transform 0.2s, -webkit-trans=
form 0.2s; }

colab-file-view.collapsed .directory-icon { transform: rotate(-90deg); }

colab-file-view .overflow-ellipsis, colab-file-view.collapsed.overflow .ove=
rflow-ellipsis { display: none; padding-left: 50px; }

colab-file-view.overflow > .overflow-ellipsis { display: block; }

colab-file-uploader { -webkit-box-align: center; align-items: center; displ=
ay: flex; padding: 8px; }

.file-upload-indicator { position: relative; height: 26px; width: 26px; }

colab-file-progress { position: relative; }

.file-upload-indicator:hover .file-upload-error, colab-file-progress .file-=
progress-cancel, colab-file-uploader .file-upload-error { display: none; }

colab-file-progress:hover .file-progress-cancel, colab-file-uploader.error =
.file-upload-error { display: block; }

.file-progress-icon, .file-upload-icon, colab-file-progress { height: 26px;=
 width: 26px; --md-icon-size: 26px; }

.file-progress-icon, .file-upload-icon { left: 0px; position: absolute; top=
: 0px; }

@-webkit-keyframes file-progress-rotate {=20
  100% { transform: rotate(1turn); }
}

@keyframes file-progress-rotate {=20
  100% { transform: rotate(1turn); }
}

colab-file-progress.indeterminate svg { animation: 2332ms steps(12) 0s infi=
nite normal none running file-progress-rotate; }

colab-file-progress .file-progress-fill { stroke: var(--colab-primary-color=
); }

colab-file-progress.error .file-progress-fill { stroke: var(--colab-error-c=
olor); }

colab-file-progress.paused .file-progress-fill { stroke: var(--colab-second=
ary-text-color); opacity: 0.5; }

.file-upload-error { color: var(--colab-error-color); }

.file-tree-name, .file-tree-name-input { overflow: hidden; text-overflow: e=
llipsis; white-space: nowrap; -webkit-box-flex: 1; flex-grow: 1; margin-top=
: 1px; }

.file-tree-name-input { min-width: 0px; }

colab-file-view.selected { background-color: var(--colab-highlighted-surfac=
e-color); }

.file-title-row:not(.renaming) .file-tree-name-input { display: none; }

.file-title-row.renaming .file-tree-name { display: none; }

.file-browser-disk-display { display: none; margin: 4px 8px; }

md-icon.nonwriteable { color: var(--colab-icon-color); height: 20px; width:=
 20px; }

.add-to-composer-button { display: none; }

.add-to-composer-button md-icon { background: linear-gradient(50deg, rgb(52=
, 107, 241) 33.06%, rgb(49, 134, 255) 48.67%, rgb(79, 160, 255) 65.69%) tex=
t; color: transparent; }

.file-item-action-button { display: none; flex-shrink: 0; padding: 0px; --m=
d-icon-button-icon-size: 24px; --md-icon-button-state-layer-height: 32px; -=
-md-icon-button-state-layer-width: 32px; }

:not(.parent-link) > .file-title-row:focus-within .file-item-action-button:=
not([hidden]), :not(.parent-link) > .file-title-row:hover .file-item-action=
-button:not([hidden]), body.mobile :not(.parent-link) > .file-title-row .fi=
le-item-action-button:not([hidden]) { display: flex; }

colab-file-tree .colab-usage-bar-container { display: flex; -webkit-box-ori=
ent: vertical; -webkit-box-direction: normal; flex-direction: column; gap: =
8px; }

colab-usage-bar { outline-offset: 3px; }

colab-files-ipynb-viewer, colab-files-text-viewer { display: flex; -webkit-=
box-orient: vertical; -webkit-box-direction: normal; flex-direction: column=
; -webkit-box-flex: 1; flex-grow: 1; overflow: hidden; }

colab-files-ipynb-viewer #ipynb-options { margin-bottom: 4px; white-space: =
nowrap; }

colab-files-ipynb-viewer .editor.flex { min-height: 0px; }

colab-file-viewer-manager { left: 0px; position: absolute; right: 0px; top:=
 0px; }

colab-files-image-viewer > img { max-width: 100%; }

colab-files-image-viewer > img.unconstrained { max-width: unset; }

.max-file-size > div { margin: 16px 0px; }

.max-file-size mwc-circular-progress { height: 20px; margin-right: 12px; wi=
dth: 20px; }

.github-saver { width: 800px; }

.github-saver .github-branches, .github-saver .github-repos { -webkit-box-f=
lex: 1; flex: 1 1 0%; margin-bottom: 16px; }

.local-kernel-dialog { max-width: 640px; }

#local-runtime-auth-url-input { height: 56px; width: 100%; }

.local-kernel-dialog-warning-icon { color: var(--colab-warning-color); font=
-variation-settings: "FILL" 1; padding-right: 5px; vertical-align: top; }

.local-kernel-dialog-space-bottom { padding-bottom: 12px; }

.local-kernel-dialog-extra-details { padding-left: 12px; }

.local-kernel-dialog-content { color: var(--colab-primary-text-color); marg=
in-bottom: 6px; margin-top: 6px; }

.local-kernel-troubleshooting-failure { color: var(--colab-error-color); fo=
nt-variation-settings: "FILL" 1; padding-right: 5px; vertical-align: top; }

.local-kernel-troubleshooting-list { padding-left: 24px; }

.local-kernel-troubleshooting-list pre { margin: 0px; border: 1px solid rgb=
(0, 0, 0); padding: 5px; background: var(--colab-highlighted-surface-color)=
; white-space: pre; overflow: auto; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: https://fonts.googleapis.com/css?family=Roboto:300,400,500,600,700|Google+Sans:300,400,500,600,700|Google+Sans+Text:400,500,700&display=block

@charset "utf-8";

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiIUvaYr.woff2")=
 format("woff2"); unicode-range: U+308, U+530-58F, U+2010, U+2024, U+25CC, =
U+FB13-FB17; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiAUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+980-9FE, U+1CD0, U=
+1CD2, U+1CD5-1CD6, U+1CD8, U+1CE1, U+1CEA, U+1CED, U+1CF2, U+1CF5-1CF7, U+=
200C-200D, U+20B9, U+25CC, U+A8F1; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPh0UvaYr.woff2")=
 format("woff2"); unicode-range: U+2C7, U+2D8-2D9, U+2DB, U+307, U+1400-167=
F, U+18B0-18F5, U+25CC, U+11AB0-11ABF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj8UvaYr.woff2")=
 format("woff2"); unicode-range: U+460-52F, U+1C80-1C8A, U+20B4, U+2DE0-2DF=
F, U+A640-A69F, U+FE2E-FE2F; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjYUvaYr.woff2")=
 format("woff2"); unicode-range: U+301, U+400-45F, U+490-491, U+4B0-4B1, U+=
2116; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjMUvaYr.woff2")=
 format("woff2"); unicode-range: U+900-97F, U+1CD0-1CF9, U+200C-200D, U+20A=
8, U+20B9, U+20F0, U+25CC, U+A830-A839, U+A8E0-A8FF, U+11B00-11B09; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiMUvaYr.woff2")=
 format("woff2"); unicode-range: U+30E, U+1200-1399, U+2D80-2DDE, U+AB01-AB=
2E, U+1E7E0-1E7E6, U+1E7E8-1E7EB, U+1E7ED-1E7EE, U+1E7F0-1E7FE; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPi0UvaYr.woff2")=
 format("woff2"); unicode-range: U+589, U+10A0-10FF, U+1C90-1CBA, U+1CBD-1C=
BF, U+205A, U+2D00-2D2F, U+2E31; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj4UvaYr.woff2")=
 format("woff2"); unicode-range: U+1F00-1FFF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjEUvaYr.woff2")=
 format("woff2"); unicode-range: U+370-377, U+37A-37F, U+384-38A, U+38C, U+=
38E-3A1, U+3A3-3FF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPikUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+A80-AFF, U+200C-20=
0D, U+20B9, U+25CC, U+A830-A839; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPhEUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+A01-A76, U+200C-20=
0D, U+20B9, U+25CC, U+262C, U+A830-A839; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjAUvaYr.woff2")=
 format("woff2"); unicode-range: U+307-308, U+590-5FF, U+200C-2010, U+20AA,=
 U+25CC, U+FB1D-FB4F; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjkUvaYr.woff2")=
 format("woff2"); unicode-range: U+1780-17FF, U+19E0-19FF, U+200C-200D, U+2=
5CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjsUvaYr.woff2")=
 format("woff2"); unicode-range: U+E81-EDF, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPioUvaYr.woff2")=
 format("woff2"); unicode-range: U+307, U+323, U+951-952, U+964-965, U+D00-=
D7F, U+1CDA, U+1CF2, U+200C-200D, U+20B9, U+25CC, U+A830-A832; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPisUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+B01-B77, U+1CDA, U=
+1CF2, U+200C-200D, U+20B9, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPi8UvaYr.woff2")=
 format("woff2"); unicode-range: U+964-965, U+D81-DF4, U+1CF2, U+200C-200D,=
 U+25CC, U+111E1-111F4; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPlwUvaYr.woff2")=
 format("woff2"); unicode-range: U+1-C, U+E-1F, U+7F-9F, U+20DD-20E0, U+20E=
2-20E4, U+2150-218F, U+2190, U+2192, U+2194-2199, U+21AF, U+21E6-21F0, U+21=
F3, U+2218-2219, U+2299, U+22C4-22C6, U+2300-243F, U+2440-244A, U+2460-24FF=
, U+25A0-27BF, U+2800-28FF, U+2921-2922, U+2981, U+29BF, U+29EB, U+2B00-2BF=
F, U+4DC0-4DFF, U+FFF9-FFFB, U+10140-1018E, U+10190-1019C, U+101A0, U+101D0=
-101FD, U+102E0-102FB, U+10E60-10E7E, U+1D2C0-1D2D3, U+1D2E0-1D37F, U+1F000=
-1F0FF, U+1F100-1F1AD, U+1F1E6-1F1FF, U+1F30D-1F30F, U+1F315, U+1F31C, U+1F=
31E, U+1F320-1F32C, U+1F336, U+1F378, U+1F37D, U+1F382, U+1F393-1F39F, U+1F=
3A7-1F3A8, U+1F3AC-1F3AF, U+1F3C2, U+1F3C4-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F=
3E0, U+1F3ED, U+1F3F1-1F3F3, U+1F3F5-1F3F7, U+1F408, U+1F415, U+1F41F, U+1F=
426, U+1F43F, U+1F441-1F442, U+1F444, U+1F446-1F449, U+1F44C-1F44E, U+1F453=
, U+1F46A, U+1F47D, U+1F4A3, U+1F4B0, U+1F4B3, U+1F4B9, U+1F4BB, U+1F4BF, U=
+1F4C8-1F4CB, U+1F4D6, U+1F4DA, U+1F4DF, U+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F=
4F7, U+1F4F9-1F4FB, U+1F4FD-1F4FE, U+1F503, U+1F507-1F50B, U+1F50D, U+1F512=
-1F513, U+1F53E-1F54A, U+1F54F-1F5FA, U+1F610, U+1F650-1F67F, U+1F687, U+1F=
68D, U+1F691, U+1F694, U+1F698, U+1F6AD, U+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U=
+1F6C6-1F6CF, U+1F6D3-1F6D7, U+1F6E0-1F6EA, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U=
+1F700-1F7FF, U+1F800-1F80B, U+1F810-1F847, U+1F850-1F859, U+1F860-1F887, U=
+1F890-1F8AD, U+1F8B0-1F8BB, U+1F8C0-1F8C1, U+1F900-1F90B, U+1F93B, U+1F946=
, U+1F984, U+1F996, U+1F9E9, U+1FA00-1FA6F, U+1FA70-1FA7C, U+1FA80-1FA89, U=
+1FA8F-1FAC6, U+1FACE-1FADC, U+1FADF-1FAE9, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiQUvaYr.woff2")=
 format("woff2"); unicode-range: U+964-965, U+B82-BFA, U+200C-200D, U+20B9,=
 U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPi4UvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+C00-C7F, U+1CDA, U=
+1CF2, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiYUvaYr.woff2")=
 format("woff2"); unicode-range: U+2D7, U+303, U+331, U+E01-E5B, U+200C-200=
D, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj0UvaYr.woff2")=
 format("woff2"); unicode-range: U+102-103, U+110-111, U+128-129, U+168-169=
, U+1A0-1A1, U+1AF-1B0, U+300-301, U+303-304, U+308-309, U+323, U+329, U+1E=
A0-1EF9, U+20AB; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjwUvaYr.woff2")=
 format("woff2"); unicode-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7=
, U+2DD-2FF, U+304, U+308, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+=
2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 4=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjIUvQ.woff2") f=
ormat("woff2"); unicode-range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, =
U+2DA, U+2DC, U+304, U+308, U+329, U+2000-206F, U+20AC, U+2122, U+2191, U+2=
193, U+2212, U+2215, U+FEFF, U+FFFD; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiIUvaYr.woff2")=
 format("woff2"); unicode-range: U+308, U+530-58F, U+2010, U+2024, U+25CC, =
U+FB13-FB17; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiAUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+980-9FE, U+1CD0, U=
+1CD2, U+1CD5-1CD6, U+1CD8, U+1CE1, U+1CEA, U+1CED, U+1CF2, U+1CF5-1CF7, U+=
200C-200D, U+20B9, U+25CC, U+A8F1; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPh0UvaYr.woff2")=
 format("woff2"); unicode-range: U+2C7, U+2D8-2D9, U+2DB, U+307, U+1400-167=
F, U+18B0-18F5, U+25CC, U+11AB0-11ABF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj8UvaYr.woff2")=
 format("woff2"); unicode-range: U+460-52F, U+1C80-1C8A, U+20B4, U+2DE0-2DF=
F, U+A640-A69F, U+FE2E-FE2F; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjYUvaYr.woff2")=
 format("woff2"); unicode-range: U+301, U+400-45F, U+490-491, U+4B0-4B1, U+=
2116; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjMUvaYr.woff2")=
 format("woff2"); unicode-range: U+900-97F, U+1CD0-1CF9, U+200C-200D, U+20A=
8, U+20B9, U+20F0, U+25CC, U+A830-A839, U+A8E0-A8FF, U+11B00-11B09; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiMUvaYr.woff2")=
 format("woff2"); unicode-range: U+30E, U+1200-1399, U+2D80-2DDE, U+AB01-AB=
2E, U+1E7E0-1E7E6, U+1E7E8-1E7EB, U+1E7ED-1E7EE, U+1E7F0-1E7FE; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPi0UvaYr.woff2")=
 format("woff2"); unicode-range: U+589, U+10A0-10FF, U+1C90-1CBA, U+1CBD-1C=
BF, U+205A, U+2D00-2D2F, U+2E31; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj4UvaYr.woff2")=
 format("woff2"); unicode-range: U+1F00-1FFF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjEUvaYr.woff2")=
 format("woff2"); unicode-range: U+370-377, U+37A-37F, U+384-38A, U+38C, U+=
38E-3A1, U+3A3-3FF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPikUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+A80-AFF, U+200C-20=
0D, U+20B9, U+25CC, U+A830-A839; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPhEUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+A01-A76, U+200C-20=
0D, U+20B9, U+25CC, U+262C, U+A830-A839; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjAUvaYr.woff2")=
 format("woff2"); unicode-range: U+307-308, U+590-5FF, U+200C-2010, U+20AA,=
 U+25CC, U+FB1D-FB4F; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjkUvaYr.woff2")=
 format("woff2"); unicode-range: U+1780-17FF, U+19E0-19FF, U+200C-200D, U+2=
5CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjsUvaYr.woff2")=
 format("woff2"); unicode-range: U+E81-EDF, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPioUvaYr.woff2")=
 format("woff2"); unicode-range: U+307, U+323, U+951-952, U+964-965, U+D00-=
D7F, U+1CDA, U+1CF2, U+200C-200D, U+20B9, U+25CC, U+A830-A832; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPisUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+B01-B77, U+1CDA, U=
+1CF2, U+200C-200D, U+20B9, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPi8UvaYr.woff2")=
 format("woff2"); unicode-range: U+964-965, U+D81-DF4, U+1CF2, U+200C-200D,=
 U+25CC, U+111E1-111F4; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPlwUvaYr.woff2")=
 format("woff2"); unicode-range: U+1-C, U+E-1F, U+7F-9F, U+20DD-20E0, U+20E=
2-20E4, U+2150-218F, U+2190, U+2192, U+2194-2199, U+21AF, U+21E6-21F0, U+21=
F3, U+2218-2219, U+2299, U+22C4-22C6, U+2300-243F, U+2440-244A, U+2460-24FF=
, U+25A0-27BF, U+2800-28FF, U+2921-2922, U+2981, U+29BF, U+29EB, U+2B00-2BF=
F, U+4DC0-4DFF, U+FFF9-FFFB, U+10140-1018E, U+10190-1019C, U+101A0, U+101D0=
-101FD, U+102E0-102FB, U+10E60-10E7E, U+1D2C0-1D2D3, U+1D2E0-1D37F, U+1F000=
-1F0FF, U+1F100-1F1AD, U+1F1E6-1F1FF, U+1F30D-1F30F, U+1F315, U+1F31C, U+1F=
31E, U+1F320-1F32C, U+1F336, U+1F378, U+1F37D, U+1F382, U+1F393-1F39F, U+1F=
3A7-1F3A8, U+1F3AC-1F3AF, U+1F3C2, U+1F3C4-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F=
3E0, U+1F3ED, U+1F3F1-1F3F3, U+1F3F5-1F3F7, U+1F408, U+1F415, U+1F41F, U+1F=
426, U+1F43F, U+1F441-1F442, U+1F444, U+1F446-1F449, U+1F44C-1F44E, U+1F453=
, U+1F46A, U+1F47D, U+1F4A3, U+1F4B0, U+1F4B3, U+1F4B9, U+1F4BB, U+1F4BF, U=
+1F4C8-1F4CB, U+1F4D6, U+1F4DA, U+1F4DF, U+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F=
4F7, U+1F4F9-1F4FB, U+1F4FD-1F4FE, U+1F503, U+1F507-1F50B, U+1F50D, U+1F512=
-1F513, U+1F53E-1F54A, U+1F54F-1F5FA, U+1F610, U+1F650-1F67F, U+1F687, U+1F=
68D, U+1F691, U+1F694, U+1F698, U+1F6AD, U+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U=
+1F6C6-1F6CF, U+1F6D3-1F6D7, U+1F6E0-1F6EA, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U=
+1F700-1F7FF, U+1F800-1F80B, U+1F810-1F847, U+1F850-1F859, U+1F860-1F887, U=
+1F890-1F8AD, U+1F8B0-1F8BB, U+1F8C0-1F8C1, U+1F900-1F90B, U+1F93B, U+1F946=
, U+1F984, U+1F996, U+1F9E9, U+1FA00-1FA6F, U+1FA70-1FA7C, U+1FA80-1FA89, U=
+1FA8F-1FAC6, U+1FACE-1FADC, U+1FADF-1FAE9, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiQUvaYr.woff2")=
 format("woff2"); unicode-range: U+964-965, U+B82-BFA, U+200C-200D, U+20B9,=
 U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPi4UvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+C00-C7F, U+1CDA, U=
+1CF2, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiYUvaYr.woff2")=
 format("woff2"); unicode-range: U+2D7, U+303, U+331, U+E01-E5B, U+200C-200=
D, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj0UvaYr.woff2")=
 format("woff2"); unicode-range: U+102-103, U+110-111, U+128-129, U+168-169=
, U+1A0-1A1, U+1AF-1B0, U+300-301, U+303-304, U+308-309, U+323, U+329, U+1E=
A0-1EF9, U+20AB; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjwUvaYr.woff2")=
 format("woff2"); unicode-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7=
, U+2DD-2FF, U+304, U+308, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+=
2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 5=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjIUvQ.woff2") f=
ormat("woff2"); unicode-range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, =
U+2DA, U+2DC, U+304, U+308, U+329, U+2000-206F, U+20AC, U+2122, U+2191, U+2=
193, U+2212, U+2215, U+FEFF, U+FFFD; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiIUvaYr.woff2")=
 format("woff2"); unicode-range: U+308, U+530-58F, U+2010, U+2024, U+25CC, =
U+FB13-FB17; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiAUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+980-9FE, U+1CD0, U=
+1CD2, U+1CD5-1CD6, U+1CD8, U+1CE1, U+1CEA, U+1CED, U+1CF2, U+1CF5-1CF7, U+=
200C-200D, U+20B9, U+25CC, U+A8F1; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPh0UvaYr.woff2")=
 format("woff2"); unicode-range: U+2C7, U+2D8-2D9, U+2DB, U+307, U+1400-167=
F, U+18B0-18F5, U+25CC, U+11AB0-11ABF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj8UvaYr.woff2")=
 format("woff2"); unicode-range: U+460-52F, U+1C80-1C8A, U+20B4, U+2DE0-2DF=
F, U+A640-A69F, U+FE2E-FE2F; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjYUvaYr.woff2")=
 format("woff2"); unicode-range: U+301, U+400-45F, U+490-491, U+4B0-4B1, U+=
2116; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjMUvaYr.woff2")=
 format("woff2"); unicode-range: U+900-97F, U+1CD0-1CF9, U+200C-200D, U+20A=
8, U+20B9, U+20F0, U+25CC, U+A830-A839, U+A8E0-A8FF, U+11B00-11B09; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiMUvaYr.woff2")=
 format("woff2"); unicode-range: U+30E, U+1200-1399, U+2D80-2DDE, U+AB01-AB=
2E, U+1E7E0-1E7E6, U+1E7E8-1E7EB, U+1E7ED-1E7EE, U+1E7F0-1E7FE; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPi0UvaYr.woff2")=
 format("woff2"); unicode-range: U+589, U+10A0-10FF, U+1C90-1CBA, U+1CBD-1C=
BF, U+205A, U+2D00-2D2F, U+2E31; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj4UvaYr.woff2")=
 format("woff2"); unicode-range: U+1F00-1FFF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjEUvaYr.woff2")=
 format("woff2"); unicode-range: U+370-377, U+37A-37F, U+384-38A, U+38C, U+=
38E-3A1, U+3A3-3FF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPikUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+A80-AFF, U+200C-20=
0D, U+20B9, U+25CC, U+A830-A839; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPhEUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+A01-A76, U+200C-20=
0D, U+20B9, U+25CC, U+262C, U+A830-A839; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjAUvaYr.woff2")=
 format("woff2"); unicode-range: U+307-308, U+590-5FF, U+200C-2010, U+20AA,=
 U+25CC, U+FB1D-FB4F; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjkUvaYr.woff2")=
 format("woff2"); unicode-range: U+1780-17FF, U+19E0-19FF, U+200C-200D, U+2=
5CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjsUvaYr.woff2")=
 format("woff2"); unicode-range: U+E81-EDF, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPioUvaYr.woff2")=
 format("woff2"); unicode-range: U+307, U+323, U+951-952, U+964-965, U+D00-=
D7F, U+1CDA, U+1CF2, U+200C-200D, U+20B9, U+25CC, U+A830-A832; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPisUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+B01-B77, U+1CDA, U=
+1CF2, U+200C-200D, U+20B9, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPi8UvaYr.woff2")=
 format("woff2"); unicode-range: U+964-965, U+D81-DF4, U+1CF2, U+200C-200D,=
 U+25CC, U+111E1-111F4; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPlwUvaYr.woff2")=
 format("woff2"); unicode-range: U+1-C, U+E-1F, U+7F-9F, U+20DD-20E0, U+20E=
2-20E4, U+2150-218F, U+2190, U+2192, U+2194-2199, U+21AF, U+21E6-21F0, U+21=
F3, U+2218-2219, U+2299, U+22C4-22C6, U+2300-243F, U+2440-244A, U+2460-24FF=
, U+25A0-27BF, U+2800-28FF, U+2921-2922, U+2981, U+29BF, U+29EB, U+2B00-2BF=
F, U+4DC0-4DFF, U+FFF9-FFFB, U+10140-1018E, U+10190-1019C, U+101A0, U+101D0=
-101FD, U+102E0-102FB, U+10E60-10E7E, U+1D2C0-1D2D3, U+1D2E0-1D37F, U+1F000=
-1F0FF, U+1F100-1F1AD, U+1F1E6-1F1FF, U+1F30D-1F30F, U+1F315, U+1F31C, U+1F=
31E, U+1F320-1F32C, U+1F336, U+1F378, U+1F37D, U+1F382, U+1F393-1F39F, U+1F=
3A7-1F3A8, U+1F3AC-1F3AF, U+1F3C2, U+1F3C4-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F=
3E0, U+1F3ED, U+1F3F1-1F3F3, U+1F3F5-1F3F7, U+1F408, U+1F415, U+1F41F, U+1F=
426, U+1F43F, U+1F441-1F442, U+1F444, U+1F446-1F449, U+1F44C-1F44E, U+1F453=
, U+1F46A, U+1F47D, U+1F4A3, U+1F4B0, U+1F4B3, U+1F4B9, U+1F4BB, U+1F4BF, U=
+1F4C8-1F4CB, U+1F4D6, U+1F4DA, U+1F4DF, U+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F=
4F7, U+1F4F9-1F4FB, U+1F4FD-1F4FE, U+1F503, U+1F507-1F50B, U+1F50D, U+1F512=
-1F513, U+1F53E-1F54A, U+1F54F-1F5FA, U+1F610, U+1F650-1F67F, U+1F687, U+1F=
68D, U+1F691, U+1F694, U+1F698, U+1F6AD, U+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U=
+1F6C6-1F6CF, U+1F6D3-1F6D7, U+1F6E0-1F6EA, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U=
+1F700-1F7FF, U+1F800-1F80B, U+1F810-1F847, U+1F850-1F859, U+1F860-1F887, U=
+1F890-1F8AD, U+1F8B0-1F8BB, U+1F8C0-1F8C1, U+1F900-1F90B, U+1F93B, U+1F946=
, U+1F984, U+1F996, U+1F9E9, U+1FA00-1FA6F, U+1FA70-1FA7C, U+1FA80-1FA89, U=
+1FA8F-1FAC6, U+1FACE-1FADC, U+1FADF-1FAE9, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiQUvaYr.woff2")=
 format("woff2"); unicode-range: U+964-965, U+B82-BFA, U+200C-200D, U+20B9,=
 U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPi4UvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+C00-C7F, U+1CDA, U=
+1CF2, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiYUvaYr.woff2")=
 format("woff2"); unicode-range: U+2D7, U+303, U+331, U+E01-E5B, U+200C-200=
D, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj0UvaYr.woff2")=
 format("woff2"); unicode-range: U+102-103, U+110-111, U+128-129, U+168-169=
, U+1A0-1A1, U+1AF-1B0, U+300-301, U+303-304, U+308-309, U+323, U+329, U+1E=
A0-1EF9, U+20AB; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjwUvaYr.woff2")=
 format("woff2"); unicode-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7=
, U+2DD-2FF, U+304, U+308, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+=
2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 6=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjIUvQ.woff2") f=
ormat("woff2"); unicode-range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, =
U+2DA, U+2DC, U+304, U+308, U+329, U+2000-206F, U+20AC, U+2122, U+2191, U+2=
193, U+2212, U+2215, U+FEFF, U+FFFD; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiIUvaYr.woff2")=
 format("woff2"); unicode-range: U+308, U+530-58F, U+2010, U+2024, U+25CC, =
U+FB13-FB17; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiAUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+980-9FE, U+1CD0, U=
+1CD2, U+1CD5-1CD6, U+1CD8, U+1CE1, U+1CEA, U+1CED, U+1CF2, U+1CF5-1CF7, U+=
200C-200D, U+20B9, U+25CC, U+A8F1; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPh0UvaYr.woff2")=
 format("woff2"); unicode-range: U+2C7, U+2D8-2D9, U+2DB, U+307, U+1400-167=
F, U+18B0-18F5, U+25CC, U+11AB0-11ABF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj8UvaYr.woff2")=
 format("woff2"); unicode-range: U+460-52F, U+1C80-1C8A, U+20B4, U+2DE0-2DF=
F, U+A640-A69F, U+FE2E-FE2F; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjYUvaYr.woff2")=
 format("woff2"); unicode-range: U+301, U+400-45F, U+490-491, U+4B0-4B1, U+=
2116; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjMUvaYr.woff2")=
 format("woff2"); unicode-range: U+900-97F, U+1CD0-1CF9, U+200C-200D, U+20A=
8, U+20B9, U+20F0, U+25CC, U+A830-A839, U+A8E0-A8FF, U+11B00-11B09; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiMUvaYr.woff2")=
 format("woff2"); unicode-range: U+30E, U+1200-1399, U+2D80-2DDE, U+AB01-AB=
2E, U+1E7E0-1E7E6, U+1E7E8-1E7EB, U+1E7ED-1E7EE, U+1E7F0-1E7FE; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPi0UvaYr.woff2")=
 format("woff2"); unicode-range: U+589, U+10A0-10FF, U+1C90-1CBA, U+1CBD-1C=
BF, U+205A, U+2D00-2D2F, U+2E31; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj4UvaYr.woff2")=
 format("woff2"); unicode-range: U+1F00-1FFF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjEUvaYr.woff2")=
 format("woff2"); unicode-range: U+370-377, U+37A-37F, U+384-38A, U+38C, U+=
38E-3A1, U+3A3-3FF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPikUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+A80-AFF, U+200C-20=
0D, U+20B9, U+25CC, U+A830-A839; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPhEUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+A01-A76, U+200C-20=
0D, U+20B9, U+25CC, U+262C, U+A830-A839; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjAUvaYr.woff2")=
 format("woff2"); unicode-range: U+307-308, U+590-5FF, U+200C-2010, U+20AA,=
 U+25CC, U+FB1D-FB4F; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjkUvaYr.woff2")=
 format("woff2"); unicode-range: U+1780-17FF, U+19E0-19FF, U+200C-200D, U+2=
5CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjsUvaYr.woff2")=
 format("woff2"); unicode-range: U+E81-EDF, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPioUvaYr.woff2")=
 format("woff2"); unicode-range: U+307, U+323, U+951-952, U+964-965, U+D00-=
D7F, U+1CDA, U+1CF2, U+200C-200D, U+20B9, U+25CC, U+A830-A832; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPisUvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+B01-B77, U+1CDA, U=
+1CF2, U+200C-200D, U+20B9, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPi8UvaYr.woff2")=
 format("woff2"); unicode-range: U+964-965, U+D81-DF4, U+1CF2, U+200C-200D,=
 U+25CC, U+111E1-111F4; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPlwUvaYr.woff2")=
 format("woff2"); unicode-range: U+1-C, U+E-1F, U+7F-9F, U+20DD-20E0, U+20E=
2-20E4, U+2150-218F, U+2190, U+2192, U+2194-2199, U+21AF, U+21E6-21F0, U+21=
F3, U+2218-2219, U+2299, U+22C4-22C6, U+2300-243F, U+2440-244A, U+2460-24FF=
, U+25A0-27BF, U+2800-28FF, U+2921-2922, U+2981, U+29BF, U+29EB, U+2B00-2BF=
F, U+4DC0-4DFF, U+FFF9-FFFB, U+10140-1018E, U+10190-1019C, U+101A0, U+101D0=
-101FD, U+102E0-102FB, U+10E60-10E7E, U+1D2C0-1D2D3, U+1D2E0-1D37F, U+1F000=
-1F0FF, U+1F100-1F1AD, U+1F1E6-1F1FF, U+1F30D-1F30F, U+1F315, U+1F31C, U+1F=
31E, U+1F320-1F32C, U+1F336, U+1F378, U+1F37D, U+1F382, U+1F393-1F39F, U+1F=
3A7-1F3A8, U+1F3AC-1F3AF, U+1F3C2, U+1F3C4-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F=
3E0, U+1F3ED, U+1F3F1-1F3F3, U+1F3F5-1F3F7, U+1F408, U+1F415, U+1F41F, U+1F=
426, U+1F43F, U+1F441-1F442, U+1F444, U+1F446-1F449, U+1F44C-1F44E, U+1F453=
, U+1F46A, U+1F47D, U+1F4A3, U+1F4B0, U+1F4B3, U+1F4B9, U+1F4BB, U+1F4BF, U=
+1F4C8-1F4CB, U+1F4D6, U+1F4DA, U+1F4DF, U+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F=
4F7, U+1F4F9-1F4FB, U+1F4FD-1F4FE, U+1F503, U+1F507-1F50B, U+1F50D, U+1F512=
-1F513, U+1F53E-1F54A, U+1F54F-1F5FA, U+1F610, U+1F650-1F67F, U+1F687, U+1F=
68D, U+1F691, U+1F694, U+1F698, U+1F6AD, U+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U=
+1F6C6-1F6CF, U+1F6D3-1F6D7, U+1F6E0-1F6EA, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U=
+1F700-1F7FF, U+1F800-1F80B, U+1F810-1F847, U+1F850-1F859, U+1F860-1F887, U=
+1F890-1F8AD, U+1F8B0-1F8BB, U+1F8C0-1F8C1, U+1F900-1F90B, U+1F93B, U+1F946=
, U+1F984, U+1F996, U+1F9E9, U+1FA00-1FA6F, U+1FA70-1FA7C, U+1FA80-1FA89, U=
+1FA8F-1FAC6, U+1FACE-1FADC, U+1FADF-1FAE9, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiQUvaYr.woff2")=
 format("woff2"); unicode-range: U+964-965, U+B82-BFA, U+200C-200D, U+20B9,=
 U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPi4UvaYr.woff2")=
 format("woff2"); unicode-range: U+951-952, U+964-965, U+C00-C7F, U+1CDA, U=
+1CF2, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPiYUvaYr.woff2")=
 format("woff2"); unicode-range: U+2D7, U+303, U+331, U+E01-E5B, U+200C-200=
D, U+25CC; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPj0UvaYr.woff2")=
 format("woff2"); unicode-range: U+102-103, U+110-111, U+128-129, U+168-169=
, U+1A0-1A1, U+1AF-1B0, U+300-301, U+303-304, U+308-309, U+323, U+329, U+1E=
A0-1EF9, U+20AB; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjwUvaYr.woff2")=
 format("woff2"); unicode-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7=
, U+2DD-2FF, U+304, U+308, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+=
2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: "Google Sans"; font-style: normal; font-weight: 7=
00; font-display: block; src: url("https://fonts.gstatic.com/s/googlesans/v=
67/4UasrENHsxJlGDuGo1OIlJfC6l_24rlCK1Yo_Iqcsih3SAyH6cAwhX9RPjIUvQ.woff2") f=
ormat("woff2"); unicode-range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, =
U+2DA, U+2DC, U+304, U+308, U+329, U+2000-206F, U+20AC, U+2122, U+2191, U+2=
193, U+2212, U+2215, U+FEFF, U+FFFD; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qFp2i1dC.woff2") format("woff2"); u=
nicode-range: U+308, U+530-58F, U+2010, U+2024, U+25CC, U+FB13-FB17; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qFh2i1dC.woff2") format("woff2"); u=
nicode-range: U+951-952, U+964-965, U+980-9FE, U+1CD0, U+1CD2, U+1CD5-1CD6,=
 U+1CD8, U+1CE1, U+1CEA, U+1CED, U+1CF2, U+1CF5-1CF7, U+200C-200D, U+20B9, =
U+25CC, U+A8F1; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qGV2i1dC.woff2") format("woff2"); u=
nicode-range: U+2C7, U+2D8-2D9, U+2DB, U+307, U+1400-167F, U+18B0-18F5, U+2=
5CC, U+11AB0-11ABF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qEd2i1dC.woff2") format("woff2"); u=
nicode-range: U+460-52F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+F=
E2E-FE2F; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qE52i1dC.woff2") format("woff2"); u=
nicode-range: U+301, U+400-45F, U+490-491, U+4B0-4B1, U+2116; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qEt2i1dC.woff2") format("woff2"); u=
nicode-range: U+900-97F, U+1CD0-1CF9, U+200C-200D, U+20A8, U+20B9, U+20F0, =
U+25CC, U+A830-A839, U+A8E0-A8FF, U+11B00-11B09; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qFt2i1dC.woff2") format("woff2"); u=
nicode-range: U+30E, U+1200-1399, U+2D80-2DDE, U+AB01-AB2E, U+1E7E0-1E7E6, =
U+1E7E8-1E7EB, U+1E7ED-1E7EE, U+1E7F0-1E7FE; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qFV2i1dC.woff2") format("woff2"); u=
nicode-range: U+589, U+10A0-10FF, U+1C90-1CBA, U+1CBD-1CBF, U+205A, U+2D00-=
2D2F, U+2E31; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qEZ2i1dC.woff2") format("woff2"); u=
nicode-range: U+1F00-1FFF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qEl2i1dC.woff2") format("woff2"); u=
nicode-range: U+370-377, U+37A-37F, U+384-38A, U+38C, U+38E-3A1, U+3A3-3FF;=
 }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qFF2i1dC.woff2") format("woff2"); u=
nicode-range: U+951-952, U+964-965, U+A80-AFF, U+200C-200D, U+20B9, U+25CC,=
 U+A830-A839; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qGl2i1dC.woff2") format("woff2"); u=
nicode-range: U+951-952, U+964-965, U+A01-A76, U+200C-200D, U+20B9, U+25CC,=
 U+262C, U+A830-A839; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qEh2i1dC.woff2") format("woff2"); u=
nicode-range: U+307-308, U+590-5FF, U+200C-2010, U+20AA, U+25CC, U+FB1D-FB4=
F; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qFB2i1dC.woff2") format("woff2"); u=
nicode-range: U+951-952, U+964-965, U+C80-CF3, U+1CD0, U+1CD2-1CD3, U+1CDA,=
 U+1CF2, U+1CF4, U+200C-200D, U+20B9, U+25CC, U+A830-A835; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qEF2i1dC.woff2") format("woff2"); u=
nicode-range: U+1780-17FF, U+19E0-19FF, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qEN2i1dC.woff2") format("woff2"); u=
nicode-range: U+E81-EDF, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qFJ2i1dC.woff2") format("woff2"); u=
nicode-range: U+307, U+323, U+951-952, U+964-965, U+D00-D7F, U+1CDA, U+1CF2=
, U+200C-200D, U+20B9, U+25CC, U+A830-A832; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qFN2i1dC.woff2") format("woff2"); u=
nicode-range: U+951-952, U+964-965, U+B01-B77, U+1CDA, U+1CF2, U+200C-200D,=
 U+20B9, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qFd2i1dC.woff2") format("woff2"); u=
nicode-range: U+964-965, U+D81-DF4, U+1CF2, U+200C-200D, U+25CC, U+111E1-11=
1F4; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qCR2i1dC.woff2") format("woff2"); u=
nicode-range: U+1-C, U+E-1F, U+7F-9F, U+20DD-20E0, U+20E2-20E4, U+2150-218F=
, U+2190, U+2192, U+2194-2199, U+21AF, U+21E6-21F0, U+21F3, U+2218-2219, U+=
2299, U+22C4-22C6, U+2300-243F, U+2440-244A, U+2460-24FF, U+25A0-27BF, U+28=
00-28FF, U+2921-2922, U+2981, U+29BF, U+29EB, U+2B00-2BFF, U+4DC0-4DFF, U+F=
FF9-FFFB, U+10140-1018E, U+10190-1019C, U+101A0, U+101D0-101FD, U+102E0-102=
FB, U+10E60-10E7E, U+1D2C0-1D2D3, U+1D2E0-1D37F, U+1F000-1F0FF, U+1F100-1F1=
AD, U+1F1E6-1F1FF, U+1F30D-1F30F, U+1F315, U+1F31C, U+1F31E, U+1F320-1F32C,=
 U+1F336, U+1F378, U+1F37D, U+1F382, U+1F393-1F39F, U+1F3A7-1F3A8, U+1F3AC-=
1F3AF, U+1F3C2, U+1F3C4-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F3E0, U+1F3ED, U+1F3=
F1-1F3F3, U+1F3F5-1F3F7, U+1F408, U+1F415, U+1F41F, U+1F426, U+1F43F, U+1F4=
41-1F442, U+1F444, U+1F446-1F449, U+1F44C-1F44E, U+1F453, U+1F46A, U+1F47D,=
 U+1F4A3, U+1F4B0, U+1F4B3, U+1F4B9, U+1F4BB, U+1F4BF, U+1F4C8-1F4CB, U+1F4=
D6, U+1F4DA, U+1F4DF, U+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F4F7, U+1F4F9-1F4FB,=
 U+1F4FD-1F4FE, U+1F503, U+1F507-1F50B, U+1F50D, U+1F512-1F513, U+1F53E-1F5=
4A, U+1F54F-1F5FA, U+1F610, U+1F650-1F67F, U+1F687, U+1F68D, U+1F691, U+1F6=
94, U+1F698, U+1F6AD, U+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U+1F6C6-1F6CF, U+1F6=
D3-1F6D7, U+1F6E0-1F6EA, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U+1F700-1F7FF, U+1F8=
00-1F80B, U+1F810-1F847, U+1F850-1F859, U+1F860-1F887, U+1F890-1F8AD, U+1F8=
B0-1F8BB, U+1F8C0-1F8C1, U+1F900-1F90B, U+1F93B, U+1F946, U+1F984, U+1F996,=
 U+1F9E9, U+1FA00-1FA6F, U+1FA70-1FA7C, U+1FA80-1FA89, U+1FA8F-1FAC6, U+1FA=
CE-1FADC, U+1FADF-1FAE9, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qFx2i1dC.woff2") format("woff2"); u=
nicode-range: U+964-965, U+B82-BFA, U+200C-200D, U+20B9, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qFZ2i1dC.woff2") format("woff2"); u=
nicode-range: U+951-952, U+964-965, U+C00-C7F, U+1CDA, U+1CF2, U+200C-200D,=
 U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qF52i1dC.woff2") format("woff2"); u=
nicode-range: U+2D7, U+303, U+331, U+E01-E5B, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qEV2i1dC.woff2") format("woff2"); u=
nicode-range: U+102-103, U+110-111, U+128-129, U+168-169, U+1A0-1A1, U+1AF-=
1B0, U+300-301, U+303-304, U+308-309, U+323, U+329, U+1EA0-1EF9, U+20AB; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qER2i1dC.woff2") format("woff2"); u=
nicode-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF, U+304,=
 U+308, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, =
U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUu9-KzpRiLCAt4Unrc-xIKmCU5qEp2iw.woff2") format("woff2"); uni=
code-range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA, U+2DC, U+304=
, U+308, U+329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215=
, U+FEFF, U+FFFD; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnnhjtiu7.woff2") format("woff2"=
); unicode-range: U+308, U+530-58F, U+2010, U+2024, U+25CC, U+FB13-FB17; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnnpjtiu7.woff2") format("woff2"=
); unicode-range: U+951-952, U+964-965, U+980-9FE, U+1CD0, U+1CD2, U+1CD5-1=
CD6, U+1CD8, U+1CE1, U+1CEA, U+1CED, U+1CF2, U+1CF5-1CF7, U+200C-200D, U+20=
B9, U+25CC, U+A8F1; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnkdjtiu7.woff2") format("woff2"=
); unicode-range: U+2C7, U+2D8-2D9, U+2DB, U+307, U+1400-167F, U+18B0-18F5,=
 U+25CC, U+11AB0-11ABF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmVjtiu7.woff2") format("woff2"=
); unicode-range: U+460-52F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F,=
 U+FE2E-FE2F; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmxjtiu7.woff2") format("woff2"=
); unicode-range: U+301, U+400-45F, U+490-491, U+4B0-4B1, U+2116; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmljtiu7.woff2") format("woff2"=
); unicode-range: U+900-97F, U+1CD0-1CF9, U+200C-200D, U+20A8, U+20B9, U+20=
F0, U+25CC, U+A830-A839, U+A8E0-A8FF, U+11B00-11B09; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnnljtiu7.woff2") format("woff2"=
); unicode-range: U+30E, U+1200-1399, U+2D80-2DDE, U+AB01-AB2E, U+1E7E0-1E7=
E6, U+1E7E8-1E7EB, U+1E7ED-1E7EE, U+1E7F0-1E7FE; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnndjtiu7.woff2") format("woff2"=
); unicode-range: U+589, U+10A0-10FF, U+1C90-1CBA, U+1CBD-1CBF, U+205A, U+2=
D00-2D2F, U+2E31; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmRjtiu7.woff2") format("woff2"=
); unicode-range: U+1F00-1FFF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmtjtiu7.woff2") format("woff2"=
); unicode-range: U+370-377, U+37A-37F, U+384-38A, U+38C, U+38E-3A1, U+3A3-=
3FF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnnNjtiu7.woff2") format("woff2"=
); unicode-range: U+951-952, U+964-965, U+A80-AFF, U+200C-200D, U+20B9, U+2=
5CC, U+A830-A839; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnktjtiu7.woff2") format("woff2"=
); unicode-range: U+951-952, U+964-965, U+A01-A76, U+200C-200D, U+20B9, U+2=
5CC, U+262C, U+A830-A839; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmpjtiu7.woff2") format("woff2"=
); unicode-range: U+307-308, U+590-5FF, U+200C-2010, U+20AA, U+25CC, U+FB1D=
-FB4F; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnnJjtiu7.woff2") format("woff2"=
); unicode-range: U+951-952, U+964-965, U+C80-CF3, U+1CD0, U+1CD2-1CD3, U+1=
CDA, U+1CF2, U+1CF4, U+200C-200D, U+20B9, U+25CC, U+A830-A835; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmNjtiu7.woff2") format("woff2"=
); unicode-range: U+1780-17FF, U+19E0-19FF, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmFjtiu7.woff2") format("woff2"=
); unicode-range: U+E81-EDF, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnnBjtiu7.woff2") format("woff2"=
); unicode-range: U+307, U+323, U+951-952, U+964-965, U+D00-D7F, U+1CDA, U+=
1CF2, U+200C-200D, U+20B9, U+25CC, U+A830-A832; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnnFjtiu7.woff2") format("woff2"=
); unicode-range: U+951-952, U+964-965, U+B01-B77, U+1CDA, U+1CF2, U+200C-2=
00D, U+20B9, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnnVjtiu7.woff2") format("woff2"=
); unicode-range: U+964-965, U+D81-DF4, U+1CF2, U+200C-200D, U+25CC, U+111E=
1-111F4; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVngZjtiu7.woff2") format("woff2"=
); unicode-range: U+1-C, U+E-1F, U+7F-9F, U+20DD-20E0, U+20E2-20E4, U+2150-=
218F, U+2190, U+2192, U+2194-2199, U+21AF, U+21E6-21F0, U+21F3, U+2218-2219=
, U+2299, U+22C4-22C6, U+2300-243F, U+2440-244A, U+2460-24FF, U+25A0-27BF, =
U+2800-28FF, U+2921-2922, U+2981, U+29BF, U+29EB, U+2B00-2BFF, U+4DC0-4DFF,=
 U+FFF9-FFFB, U+10140-1018E, U+10190-1019C, U+101A0, U+101D0-101FD, U+102E0=
-102FB, U+10E60-10E7E, U+1D2C0-1D2D3, U+1D2E0-1D37F, U+1F000-1F0FF, U+1F100=
-1F1AD, U+1F1E6-1F1FF, U+1F30D-1F30F, U+1F315, U+1F31C, U+1F31E, U+1F320-1F=
32C, U+1F336, U+1F378, U+1F37D, U+1F382, U+1F393-1F39F, U+1F3A7-1F3A8, U+1F=
3AC-1F3AF, U+1F3C2, U+1F3C4-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F3E0, U+1F3ED, U=
+1F3F1-1F3F3, U+1F3F5-1F3F7, U+1F408, U+1F415, U+1F41F, U+1F426, U+1F43F, U=
+1F441-1F442, U+1F444, U+1F446-1F449, U+1F44C-1F44E, U+1F453, U+1F46A, U+1F=
47D, U+1F4A3, U+1F4B0, U+1F4B3, U+1F4B9, U+1F4BB, U+1F4BF, U+1F4C8-1F4CB, U=
+1F4D6, U+1F4DA, U+1F4DF, U+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F4F7, U+1F4F9-1F=
4FB, U+1F4FD-1F4FE, U+1F503, U+1F507-1F50B, U+1F50D, U+1F512-1F513, U+1F53E=
-1F54A, U+1F54F-1F5FA, U+1F610, U+1F650-1F67F, U+1F687, U+1F68D, U+1F691, U=
+1F694, U+1F698, U+1F6AD, U+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U+1F6C6-1F6CF, U=
+1F6D3-1F6D7, U+1F6E0-1F6EA, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U+1F700-1F7FF, U=
+1F800-1F80B, U+1F810-1F847, U+1F850-1F859, U+1F860-1F887, U+1F890-1F8AD, U=
+1F8B0-1F8BB, U+1F8C0-1F8C1, U+1F900-1F90B, U+1F93B, U+1F946, U+1F984, U+1F=
996, U+1F9E9, U+1FA00-1FA6F, U+1FA70-1FA7C, U+1FA80-1FA89, U+1FA8F-1FAC6, U=
+1FACE-1FADC, U+1FADF-1FAE9, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnn5jtiu7.woff2") format("woff2"=
); unicode-range: U+964-965, U+B82-BFA, U+200C-200D, U+20B9, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnnRjtiu7.woff2") format("woff2"=
); unicode-range: U+951-952, U+964-965, U+C00-C7F, U+1CDA, U+1CF2, U+200C-2=
00D, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnnxjtiu7.woff2") format("woff2"=
); unicode-range: U+2D7, U+303, U+331, U+E01-E5B, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmdjtiu7.woff2") format("woff2"=
); unicode-range: U+102-103, U+110-111, U+128-129, U+168-169, U+1A0-1A1, U+=
1AF-1B0, U+300-301, U+303-304, U+308-309, U+323, U+329, U+1EA0-1EF9, U+20AB=
; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmZjtiu7.woff2") format("woff2"=
); unicode-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF, U+=
304, U+308, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20=
AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 500; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oLlVnmhjtg.woff2") format("woff2");=
 unicode-range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA, U+2DC, U=
+304, U+308, U+329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+=
2215, U+FEFF, U+FFFD; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnnhjtiu7.woff2") format("woff2"=
); unicode-range: U+308, U+530-58F, U+2010, U+2024, U+25CC, U+FB13-FB17; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnnpjtiu7.woff2") format("woff2"=
); unicode-range: U+951-952, U+964-965, U+980-9FE, U+1CD0, U+1CD2, U+1CD5-1=
CD6, U+1CD8, U+1CE1, U+1CEA, U+1CED, U+1CF2, U+1CF5-1CF7, U+200C-200D, U+20=
B9, U+25CC, U+A8F1; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnkdjtiu7.woff2") format("woff2"=
); unicode-range: U+2C7, U+2D8-2D9, U+2DB, U+307, U+1400-167F, U+18B0-18F5,=
 U+25CC, U+11AB0-11ABF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnmVjtiu7.woff2") format("woff2"=
); unicode-range: U+460-52F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F,=
 U+FE2E-FE2F; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnmxjtiu7.woff2") format("woff2"=
); unicode-range: U+301, U+400-45F, U+490-491, U+4B0-4B1, U+2116; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnmljtiu7.woff2") format("woff2"=
); unicode-range: U+900-97F, U+1CD0-1CF9, U+200C-200D, U+20A8, U+20B9, U+20=
F0, U+25CC, U+A830-A839, U+A8E0-A8FF, U+11B00-11B09; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnnljtiu7.woff2") format("woff2"=
); unicode-range: U+30E, U+1200-1399, U+2D80-2DDE, U+AB01-AB2E, U+1E7E0-1E7=
E6, U+1E7E8-1E7EB, U+1E7ED-1E7EE, U+1E7F0-1E7FE; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnndjtiu7.woff2") format("woff2"=
); unicode-range: U+589, U+10A0-10FF, U+1C90-1CBA, U+1CBD-1CBF, U+205A, U+2=
D00-2D2F, U+2E31; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnmRjtiu7.woff2") format("woff2"=
); unicode-range: U+1F00-1FFF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnmtjtiu7.woff2") format("woff2"=
); unicode-range: U+370-377, U+37A-37F, U+384-38A, U+38C, U+38E-3A1, U+3A3-=
3FF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnnNjtiu7.woff2") format("woff2"=
); unicode-range: U+951-952, U+964-965, U+A80-AFF, U+200C-200D, U+20B9, U+2=
5CC, U+A830-A839; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnktjtiu7.woff2") format("woff2"=
); unicode-range: U+951-952, U+964-965, U+A01-A76, U+200C-200D, U+20B9, U+2=
5CC, U+262C, U+A830-A839; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnmpjtiu7.woff2") format("woff2"=
); unicode-range: U+307-308, U+590-5FF, U+200C-2010, U+20AA, U+25CC, U+FB1D=
-FB4F; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnnJjtiu7.woff2") format("woff2"=
); unicode-range: U+951-952, U+964-965, U+C80-CF3, U+1CD0, U+1CD2-1CD3, U+1=
CDA, U+1CF2, U+1CF4, U+200C-200D, U+20B9, U+25CC, U+A830-A835; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnmNjtiu7.woff2") format("woff2"=
); unicode-range: U+1780-17FF, U+19E0-19FF, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnmFjtiu7.woff2") format("woff2"=
); unicode-range: U+E81-EDF, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnnBjtiu7.woff2") format("woff2"=
); unicode-range: U+307, U+323, U+951-952, U+964-965, U+D00-D7F, U+1CDA, U+=
1CF2, U+200C-200D, U+20B9, U+25CC, U+A830-A832; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnnFjtiu7.woff2") format("woff2"=
); unicode-range: U+951-952, U+964-965, U+B01-B77, U+1CDA, U+1CF2, U+200C-2=
00D, U+20B9, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnnVjtiu7.woff2") format("woff2"=
); unicode-range: U+964-965, U+D81-DF4, U+1CF2, U+200C-200D, U+25CC, U+111E=
1-111F4; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTngZjtiu7.woff2") format("woff2"=
); unicode-range: U+1-C, U+E-1F, U+7F-9F, U+20DD-20E0, U+20E2-20E4, U+2150-=
218F, U+2190, U+2192, U+2194-2199, U+21AF, U+21E6-21F0, U+21F3, U+2218-2219=
, U+2299, U+22C4-22C6, U+2300-243F, U+2440-244A, U+2460-24FF, U+25A0-27BF, =
U+2800-28FF, U+2921-2922, U+2981, U+29BF, U+29EB, U+2B00-2BFF, U+4DC0-4DFF,=
 U+FFF9-FFFB, U+10140-1018E, U+10190-1019C, U+101A0, U+101D0-101FD, U+102E0=
-102FB, U+10E60-10E7E, U+1D2C0-1D2D3, U+1D2E0-1D37F, U+1F000-1F0FF, U+1F100=
-1F1AD, U+1F1E6-1F1FF, U+1F30D-1F30F, U+1F315, U+1F31C, U+1F31E, U+1F320-1F=
32C, U+1F336, U+1F378, U+1F37D, U+1F382, U+1F393-1F39F, U+1F3A7-1F3A8, U+1F=
3AC-1F3AF, U+1F3C2, U+1F3C4-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F3E0, U+1F3ED, U=
+1F3F1-1F3F3, U+1F3F5-1F3F7, U+1F408, U+1F415, U+1F41F, U+1F426, U+1F43F, U=
+1F441-1F442, U+1F444, U+1F446-1F449, U+1F44C-1F44E, U+1F453, U+1F46A, U+1F=
47D, U+1F4A3, U+1F4B0, U+1F4B3, U+1F4B9, U+1F4BB, U+1F4BF, U+1F4C8-1F4CB, U=
+1F4D6, U+1F4DA, U+1F4DF, U+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F4F7, U+1F4F9-1F=
4FB, U+1F4FD-1F4FE, U+1F503, U+1F507-1F50B, U+1F50D, U+1F512-1F513, U+1F53E=
-1F54A, U+1F54F-1F5FA, U+1F610, U+1F650-1F67F, U+1F687, U+1F68D, U+1F691, U=
+1F694, U+1F698, U+1F6AD, U+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U+1F6C6-1F6CF, U=
+1F6D3-1F6D7, U+1F6E0-1F6EA, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U+1F700-1F7FF, U=
+1F800-1F80B, U+1F810-1F847, U+1F850-1F859, U+1F860-1F887, U+1F890-1F8AD, U=
+1F8B0-1F8BB, U+1F8C0-1F8C1, U+1F900-1F90B, U+1F93B, U+1F946, U+1F984, U+1F=
996, U+1F9E9, U+1FA00-1FA6F, U+1FA70-1FA7C, U+1FA80-1FA89, U+1FA8F-1FAC6, U=
+1FACE-1FADC, U+1FADF-1FAE9, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnn5jtiu7.woff2") format("woff2"=
); unicode-range: U+964-965, U+B82-BFA, U+200C-200D, U+20B9, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnnRjtiu7.woff2") format("woff2"=
); unicode-range: U+951-952, U+964-965, U+C00-C7F, U+1CDA, U+1CF2, U+200C-2=
00D, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnnxjtiu7.woff2") format("woff2"=
); unicode-range: U+2D7, U+303, U+331, U+E01-E5B, U+200C-200D, U+25CC; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnmdjtiu7.woff2") format("woff2"=
); unicode-range: U+102-103, U+110-111, U+128-129, U+168-169, U+1A0-1A1, U+=
1AF-1B0, U+300-301, U+303-304, U+308-309, U+323, U+329, U+1EA0-1EF9, U+20AB=
; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnmZjtiu7.woff2") format("woff2"=
); unicode-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF, U+=
304, U+308, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20=
AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: "Google Sans Text"; font-style: normal; font-weig=
ht: 700; font-display: block; src: url("https://fonts.gstatic.com/s/googles=
anstext/v25/5aUp9-KzpRiLCAt4Unrc-xIKmCU5oPFTnmhjtg.woff2") format("woff2");=
 unicode-range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA, U+2DC, U=
+304, U+308, U+329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+=
2215, U+FEFF, U+FFFD; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 300; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3GUBGEe.woff2") format("woff2"=
); unicode-range: U+460-52F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F,=
 U+FE2E-FE2F; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 300; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3iUBGEe.woff2") format("woff2"=
); unicode-range: U+301, U+400-45F, U+490-491, U+4B0-4B1, U+2116; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 300; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3CUBGEe.woff2") format("woff2"=
); unicode-range: U+1F00-1FFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 300; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3-UBGEe.woff2") format("woff2"=
); unicode-range: U+370-377, U+37A-37F, U+384-38A, U+38C, U+38E-3A1, U+3A3-=
3FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 300; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMawCUBGEe.woff2") format("woff2"=
); unicode-range: U+302-303, U+305, U+307-308, U+310, U+312, U+315, U+31A, =
U+326-327, U+32C, U+32F-330, U+332-333, U+338, U+33A, U+346, U+34D, U+391-3=
A1, U+3A3-3A9, U+3B1-3C9, U+3D1, U+3D5-3D6, U+3F0-3F1, U+3F4-3F5, U+2016-20=
17, U+2034-2038, U+203C, U+2040, U+2043, U+2047, U+2050, U+2057, U+205F, U+=
2070-2071, U+2074-208E, U+2090-209C, U+20D0-20DC, U+20E1, U+20E5-20EF, U+21=
00-2112, U+2114-2115, U+2117-2121, U+2123-214F, U+2190, U+2192, U+2194-21AE=
, U+21B0-21E5, U+21F1-21F2, U+21F4-2211, U+2213-2214, U+2216-22FF, U+2308-2=
30B, U+2310, U+2319, U+231C-2321, U+2336-237A, U+237C, U+2395, U+239B-23B7,=
 U+23D0, U+23DC-23E1, U+2474-2475, U+25AF, U+25B3, U+25B7, U+25BD, U+25C1, =
U+25CA, U+25CC, U+25FB, U+266D-266F, U+27C0-27FF, U+2900-2AFF, U+2B0E-2B11,=
 U+2B30-2B4C, U+2BFE, U+3030, U+FF5B, U+FF5D, U+1D400-1D7FF, U+1EE00-1EEFF;=
 }

@font-face { font-family: Roboto; font-style: normal; font-weight: 300; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMaxKUBGEe.woff2") format("woff2"=
); unicode-range: U+1-C, U+E-1F, U+7F-9F, U+20DD-20E0, U+20E2-20E4, U+2150-=
218F, U+2190, U+2192, U+2194-2199, U+21AF, U+21E6-21F0, U+21F3, U+2218-2219=
, U+2299, U+22C4-22C6, U+2300-243F, U+2440-244A, U+2460-24FF, U+25A0-27BF, =
U+2800-28FF, U+2921-2922, U+2981, U+29BF, U+29EB, U+2B00-2BFF, U+4DC0-4DFF,=
 U+FFF9-FFFB, U+10140-1018E, U+10190-1019C, U+101A0, U+101D0-101FD, U+102E0=
-102FB, U+10E60-10E7E, U+1D2C0-1D2D3, U+1D2E0-1D37F, U+1F000-1F0FF, U+1F100=
-1F1AD, U+1F1E6-1F1FF, U+1F30D-1F30F, U+1F315, U+1F31C, U+1F31E, U+1F320-1F=
32C, U+1F336, U+1F378, U+1F37D, U+1F382, U+1F393-1F39F, U+1F3A7-1F3A8, U+1F=
3AC-1F3AF, U+1F3C2, U+1F3C4-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F3E0, U+1F3ED, U=
+1F3F1-1F3F3, U+1F3F5-1F3F7, U+1F408, U+1F415, U+1F41F, U+1F426, U+1F43F, U=
+1F441-1F442, U+1F444, U+1F446-1F449, U+1F44C-1F44E, U+1F453, U+1F46A, U+1F=
47D, U+1F4A3, U+1F4B0, U+1F4B3, U+1F4B9, U+1F4BB, U+1F4BF, U+1F4C8-1F4CB, U=
+1F4D6, U+1F4DA, U+1F4DF, U+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F4F7, U+1F4F9-1F=
4FB, U+1F4FD-1F4FE, U+1F503, U+1F507-1F50B, U+1F50D, U+1F512-1F513, U+1F53E=
-1F54A, U+1F54F-1F5FA, U+1F610, U+1F650-1F67F, U+1F687, U+1F68D, U+1F691, U=
+1F694, U+1F698, U+1F6AD, U+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U+1F6C6-1F6CF, U=
+1F6D3-1F6D7, U+1F6E0-1F6EA, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U+1F700-1F7FF, U=
+1F800-1F80B, U+1F810-1F847, U+1F850-1F859, U+1F860-1F887, U+1F890-1F8AD, U=
+1F8B0-1F8BB, U+1F8C0-1F8C1, U+1F900-1F90B, U+1F93B, U+1F946, U+1F984, U+1F=
996, U+1F9E9, U+1FA00-1FA6F, U+1FA70-1FA7C, U+1FA80-1FA89, U+1FA8F-1FAC6, U=
+1FACE-1FADC, U+1FADF-1FAE9, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 300; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3OUBGEe.woff2") format("woff2"=
); unicode-range: U+102-103, U+110-111, U+128-129, U+168-169, U+1A0-1A1, U+=
1AF-1B0, U+300-301, U+303-304, U+308-309, U+323, U+329, U+1EA0-1EF9, U+20AB=
; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 300; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3KUBGEe.woff2") format("woff2"=
); unicode-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF, U+=
304, U+308, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20=
AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 300; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBA.woff2") format("woff2");=
 unicode-range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA, U+2DC, U=
+304, U+308, U+329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+=
2215, U+FEFF, U+FFFD; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3GUBGEe.woff2") format("woff2"=
); unicode-range: U+460-52F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F,=
 U+FE2E-FE2F; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3iUBGEe.woff2") format("woff2"=
); unicode-range: U+301, U+400-45F, U+490-491, U+4B0-4B1, U+2116; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3CUBGEe.woff2") format("woff2"=
); unicode-range: U+1F00-1FFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3-UBGEe.woff2") format("woff2"=
); unicode-range: U+370-377, U+37A-37F, U+384-38A, U+38C, U+38E-3A1, U+3A3-=
3FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMawCUBGEe.woff2") format("woff2"=
); unicode-range: U+302-303, U+305, U+307-308, U+310, U+312, U+315, U+31A, =
U+326-327, U+32C, U+32F-330, U+332-333, U+338, U+33A, U+346, U+34D, U+391-3=
A1, U+3A3-3A9, U+3B1-3C9, U+3D1, U+3D5-3D6, U+3F0-3F1, U+3F4-3F5, U+2016-20=
17, U+2034-2038, U+203C, U+2040, U+2043, U+2047, U+2050, U+2057, U+205F, U+=
2070-2071, U+2074-208E, U+2090-209C, U+20D0-20DC, U+20E1, U+20E5-20EF, U+21=
00-2112, U+2114-2115, U+2117-2121, U+2123-214F, U+2190, U+2192, U+2194-21AE=
, U+21B0-21E5, U+21F1-21F2, U+21F4-2211, U+2213-2214, U+2216-22FF, U+2308-2=
30B, U+2310, U+2319, U+231C-2321, U+2336-237A, U+237C, U+2395, U+239B-23B7,=
 U+23D0, U+23DC-23E1, U+2474-2475, U+25AF, U+25B3, U+25B7, U+25BD, U+25C1, =
U+25CA, U+25CC, U+25FB, U+266D-266F, U+27C0-27FF, U+2900-2AFF, U+2B0E-2B11,=
 U+2B30-2B4C, U+2BFE, U+3030, U+FF5B, U+FF5D, U+1D400-1D7FF, U+1EE00-1EEFF;=
 }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMaxKUBGEe.woff2") format("woff2"=
); unicode-range: U+1-C, U+E-1F, U+7F-9F, U+20DD-20E0, U+20E2-20E4, U+2150-=
218F, U+2190, U+2192, U+2194-2199, U+21AF, U+21E6-21F0, U+21F3, U+2218-2219=
, U+2299, U+22C4-22C6, U+2300-243F, U+2440-244A, U+2460-24FF, U+25A0-27BF, =
U+2800-28FF, U+2921-2922, U+2981, U+29BF, U+29EB, U+2B00-2BFF, U+4DC0-4DFF,=
 U+FFF9-FFFB, U+10140-1018E, U+10190-1019C, U+101A0, U+101D0-101FD, U+102E0=
-102FB, U+10E60-10E7E, U+1D2C0-1D2D3, U+1D2E0-1D37F, U+1F000-1F0FF, U+1F100=
-1F1AD, U+1F1E6-1F1FF, U+1F30D-1F30F, U+1F315, U+1F31C, U+1F31E, U+1F320-1F=
32C, U+1F336, U+1F378, U+1F37D, U+1F382, U+1F393-1F39F, U+1F3A7-1F3A8, U+1F=
3AC-1F3AF, U+1F3C2, U+1F3C4-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F3E0, U+1F3ED, U=
+1F3F1-1F3F3, U+1F3F5-1F3F7, U+1F408, U+1F415, U+1F41F, U+1F426, U+1F43F, U=
+1F441-1F442, U+1F444, U+1F446-1F449, U+1F44C-1F44E, U+1F453, U+1F46A, U+1F=
47D, U+1F4A3, U+1F4B0, U+1F4B3, U+1F4B9, U+1F4BB, U+1F4BF, U+1F4C8-1F4CB, U=
+1F4D6, U+1F4DA, U+1F4DF, U+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F4F7, U+1F4F9-1F=
4FB, U+1F4FD-1F4FE, U+1F503, U+1F507-1F50B, U+1F50D, U+1F512-1F513, U+1F53E=
-1F54A, U+1F54F-1F5FA, U+1F610, U+1F650-1F67F, U+1F687, U+1F68D, U+1F691, U=
+1F694, U+1F698, U+1F6AD, U+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U+1F6C6-1F6CF, U=
+1F6D3-1F6D7, U+1F6E0-1F6EA, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U+1F700-1F7FF, U=
+1F800-1F80B, U+1F810-1F847, U+1F850-1F859, U+1F860-1F887, U+1F890-1F8AD, U=
+1F8B0-1F8BB, U+1F8C0-1F8C1, U+1F900-1F90B, U+1F93B, U+1F946, U+1F984, U+1F=
996, U+1F9E9, U+1FA00-1FA6F, U+1FA70-1FA7C, U+1FA80-1FA89, U+1FA8F-1FAC6, U=
+1FACE-1FADC, U+1FADF-1FAE9, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3OUBGEe.woff2") format("woff2"=
); unicode-range: U+102-103, U+110-111, U+128-129, U+168-169, U+1A0-1A1, U+=
1AF-1B0, U+300-301, U+303-304, U+308-309, U+323, U+329, U+1EA0-1EF9, U+20AB=
; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3KUBGEe.woff2") format("woff2"=
); unicode-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF, U+=
304, U+308, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20=
AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBA.woff2") format("woff2");=
 unicode-range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA, U+2DC, U=
+304, U+308, U+329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+=
2215, U+FEFF, U+FFFD; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3GUBGEe.woff2") format("woff2"=
); unicode-range: U+460-52F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F,=
 U+FE2E-FE2F; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3iUBGEe.woff2") format("woff2"=
); unicode-range: U+301, U+400-45F, U+490-491, U+4B0-4B1, U+2116; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3CUBGEe.woff2") format("woff2"=
); unicode-range: U+1F00-1FFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3-UBGEe.woff2") format("woff2"=
); unicode-range: U+370-377, U+37A-37F, U+384-38A, U+38C, U+38E-3A1, U+3A3-=
3FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMawCUBGEe.woff2") format("woff2"=
); unicode-range: U+302-303, U+305, U+307-308, U+310, U+312, U+315, U+31A, =
U+326-327, U+32C, U+32F-330, U+332-333, U+338, U+33A, U+346, U+34D, U+391-3=
A1, U+3A3-3A9, U+3B1-3C9, U+3D1, U+3D5-3D6, U+3F0-3F1, U+3F4-3F5, U+2016-20=
17, U+2034-2038, U+203C, U+2040, U+2043, U+2047, U+2050, U+2057, U+205F, U+=
2070-2071, U+2074-208E, U+2090-209C, U+20D0-20DC, U+20E1, U+20E5-20EF, U+21=
00-2112, U+2114-2115, U+2117-2121, U+2123-214F, U+2190, U+2192, U+2194-21AE=
, U+21B0-21E5, U+21F1-21F2, U+21F4-2211, U+2213-2214, U+2216-22FF, U+2308-2=
30B, U+2310, U+2319, U+231C-2321, U+2336-237A, U+237C, U+2395, U+239B-23B7,=
 U+23D0, U+23DC-23E1, U+2474-2475, U+25AF, U+25B3, U+25B7, U+25BD, U+25C1, =
U+25CA, U+25CC, U+25FB, U+266D-266F, U+27C0-27FF, U+2900-2AFF, U+2B0E-2B11,=
 U+2B30-2B4C, U+2BFE, U+3030, U+FF5B, U+FF5D, U+1D400-1D7FF, U+1EE00-1EEFF;=
 }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMaxKUBGEe.woff2") format("woff2"=
); unicode-range: U+1-C, U+E-1F, U+7F-9F, U+20DD-20E0, U+20E2-20E4, U+2150-=
218F, U+2190, U+2192, U+2194-2199, U+21AF, U+21E6-21F0, U+21F3, U+2218-2219=
, U+2299, U+22C4-22C6, U+2300-243F, U+2440-244A, U+2460-24FF, U+25A0-27BF, =
U+2800-28FF, U+2921-2922, U+2981, U+29BF, U+29EB, U+2B00-2BFF, U+4DC0-4DFF,=
 U+FFF9-FFFB, U+10140-1018E, U+10190-1019C, U+101A0, U+101D0-101FD, U+102E0=
-102FB, U+10E60-10E7E, U+1D2C0-1D2D3, U+1D2E0-1D37F, U+1F000-1F0FF, U+1F100=
-1F1AD, U+1F1E6-1F1FF, U+1F30D-1F30F, U+1F315, U+1F31C, U+1F31E, U+1F320-1F=
32C, U+1F336, U+1F378, U+1F37D, U+1F382, U+1F393-1F39F, U+1F3A7-1F3A8, U+1F=
3AC-1F3AF, U+1F3C2, U+1F3C4-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F3E0, U+1F3ED, U=
+1F3F1-1F3F3, U+1F3F5-1F3F7, U+1F408, U+1F415, U+1F41F, U+1F426, U+1F43F, U=
+1F441-1F442, U+1F444, U+1F446-1F449, U+1F44C-1F44E, U+1F453, U+1F46A, U+1F=
47D, U+1F4A3, U+1F4B0, U+1F4B3, U+1F4B9, U+1F4BB, U+1F4BF, U+1F4C8-1F4CB, U=
+1F4D6, U+1F4DA, U+1F4DF, U+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F4F7, U+1F4F9-1F=
4FB, U+1F4FD-1F4FE, U+1F503, U+1F507-1F50B, U+1F50D, U+1F512-1F513, U+1F53E=
-1F54A, U+1F54F-1F5FA, U+1F610, U+1F650-1F67F, U+1F687, U+1F68D, U+1F691, U=
+1F694, U+1F698, U+1F6AD, U+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U+1F6C6-1F6CF, U=
+1F6D3-1F6D7, U+1F6E0-1F6EA, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U+1F700-1F7FF, U=
+1F800-1F80B, U+1F810-1F847, U+1F850-1F859, U+1F860-1F887, U+1F890-1F8AD, U=
+1F8B0-1F8BB, U+1F8C0-1F8C1, U+1F900-1F90B, U+1F93B, U+1F946, U+1F984, U+1F=
996, U+1F9E9, U+1FA00-1FA6F, U+1FA70-1FA7C, U+1FA80-1FA89, U+1FA8F-1FAC6, U=
+1FACE-1FADC, U+1FADF-1FAE9, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3OUBGEe.woff2") format("woff2"=
); unicode-range: U+102-103, U+110-111, U+128-129, U+168-169, U+1A0-1A1, U+=
1AF-1B0, U+300-301, U+303-304, U+308-309, U+323, U+329, U+1EA0-1EF9, U+20AB=
; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3KUBGEe.woff2") format("woff2"=
); unicode-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF, U+=
304, U+308, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20=
AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBA.woff2") format("woff2");=
 unicode-range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA, U+2DC, U=
+304, U+308, U+329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+=
2215, U+FEFF, U+FFFD; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 600; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3GUBGEe.woff2") format("woff2"=
); unicode-range: U+460-52F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F,=
 U+FE2E-FE2F; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 600; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3iUBGEe.woff2") format("woff2"=
); unicode-range: U+301, U+400-45F, U+490-491, U+4B0-4B1, U+2116; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 600; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3CUBGEe.woff2") format("woff2"=
); unicode-range: U+1F00-1FFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 600; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3-UBGEe.woff2") format("woff2"=
); unicode-range: U+370-377, U+37A-37F, U+384-38A, U+38C, U+38E-3A1, U+3A3-=
3FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 600; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMawCUBGEe.woff2") format("woff2"=
); unicode-range: U+302-303, U+305, U+307-308, U+310, U+312, U+315, U+31A, =
U+326-327, U+32C, U+32F-330, U+332-333, U+338, U+33A, U+346, U+34D, U+391-3=
A1, U+3A3-3A9, U+3B1-3C9, U+3D1, U+3D5-3D6, U+3F0-3F1, U+3F4-3F5, U+2016-20=
17, U+2034-2038, U+203C, U+2040, U+2043, U+2047, U+2050, U+2057, U+205F, U+=
2070-2071, U+2074-208E, U+2090-209C, U+20D0-20DC, U+20E1, U+20E5-20EF, U+21=
00-2112, U+2114-2115, U+2117-2121, U+2123-214F, U+2190, U+2192, U+2194-21AE=
, U+21B0-21E5, U+21F1-21F2, U+21F4-2211, U+2213-2214, U+2216-22FF, U+2308-2=
30B, U+2310, U+2319, U+231C-2321, U+2336-237A, U+237C, U+2395, U+239B-23B7,=
 U+23D0, U+23DC-23E1, U+2474-2475, U+25AF, U+25B3, U+25B7, U+25BD, U+25C1, =
U+25CA, U+25CC, U+25FB, U+266D-266F, U+27C0-27FF, U+2900-2AFF, U+2B0E-2B11,=
 U+2B30-2B4C, U+2BFE, U+3030, U+FF5B, U+FF5D, U+1D400-1D7FF, U+1EE00-1EEFF;=
 }

@font-face { font-family: Roboto; font-style: normal; font-weight: 600; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMaxKUBGEe.woff2") format("woff2"=
); unicode-range: U+1-C, U+E-1F, U+7F-9F, U+20DD-20E0, U+20E2-20E4, U+2150-=
218F, U+2190, U+2192, U+2194-2199, U+21AF, U+21E6-21F0, U+21F3, U+2218-2219=
, U+2299, U+22C4-22C6, U+2300-243F, U+2440-244A, U+2460-24FF, U+25A0-27BF, =
U+2800-28FF, U+2921-2922, U+2981, U+29BF, U+29EB, U+2B00-2BFF, U+4DC0-4DFF,=
 U+FFF9-FFFB, U+10140-1018E, U+10190-1019C, U+101A0, U+101D0-101FD, U+102E0=
-102FB, U+10E60-10E7E, U+1D2C0-1D2D3, U+1D2E0-1D37F, U+1F000-1F0FF, U+1F100=
-1F1AD, U+1F1E6-1F1FF, U+1F30D-1F30F, U+1F315, U+1F31C, U+1F31E, U+1F320-1F=
32C, U+1F336, U+1F378, U+1F37D, U+1F382, U+1F393-1F39F, U+1F3A7-1F3A8, U+1F=
3AC-1F3AF, U+1F3C2, U+1F3C4-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F3E0, U+1F3ED, U=
+1F3F1-1F3F3, U+1F3F5-1F3F7, U+1F408, U+1F415, U+1F41F, U+1F426, U+1F43F, U=
+1F441-1F442, U+1F444, U+1F446-1F449, U+1F44C-1F44E, U+1F453, U+1F46A, U+1F=
47D, U+1F4A3, U+1F4B0, U+1F4B3, U+1F4B9, U+1F4BB, U+1F4BF, U+1F4C8-1F4CB, U=
+1F4D6, U+1F4DA, U+1F4DF, U+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F4F7, U+1F4F9-1F=
4FB, U+1F4FD-1F4FE, U+1F503, U+1F507-1F50B, U+1F50D, U+1F512-1F513, U+1F53E=
-1F54A, U+1F54F-1F5FA, U+1F610, U+1F650-1F67F, U+1F687, U+1F68D, U+1F691, U=
+1F694, U+1F698, U+1F6AD, U+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U+1F6C6-1F6CF, U=
+1F6D3-1F6D7, U+1F6E0-1F6EA, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U+1F700-1F7FF, U=
+1F800-1F80B, U+1F810-1F847, U+1F850-1F859, U+1F860-1F887, U+1F890-1F8AD, U=
+1F8B0-1F8BB, U+1F8C0-1F8C1, U+1F900-1F90B, U+1F93B, U+1F946, U+1F984, U+1F=
996, U+1F9E9, U+1FA00-1FA6F, U+1FA70-1FA7C, U+1FA80-1FA89, U+1FA8F-1FAC6, U=
+1FACE-1FADC, U+1FADF-1FAE9, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 600; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3OUBGEe.woff2") format("woff2"=
); unicode-range: U+102-103, U+110-111, U+128-129, U+168-169, U+1A0-1A1, U+=
1AF-1B0, U+300-301, U+303-304, U+308-309, U+323, U+329, U+1EA0-1EF9, U+20AB=
; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 600; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3KUBGEe.woff2") format("woff2"=
); unicode-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF, U+=
304, U+308, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20=
AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 600; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBA.woff2") format("woff2");=
 unicode-range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA, U+2DC, U=
+304, U+308, U+329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+=
2215, U+FEFF, U+FFFD; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 700; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3GUBGEe.woff2") format("woff2"=
); unicode-range: U+460-52F, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F,=
 U+FE2E-FE2F; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 700; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3iUBGEe.woff2") format("woff2"=
); unicode-range: U+301, U+400-45F, U+490-491, U+4B0-4B1, U+2116; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 700; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3CUBGEe.woff2") format("woff2"=
); unicode-range: U+1F00-1FFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 700; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3-UBGEe.woff2") format("woff2"=
); unicode-range: U+370-377, U+37A-37F, U+384-38A, U+38C, U+38E-3A1, U+3A3-=
3FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 700; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMawCUBGEe.woff2") format("woff2"=
); unicode-range: U+302-303, U+305, U+307-308, U+310, U+312, U+315, U+31A, =
U+326-327, U+32C, U+32F-330, U+332-333, U+338, U+33A, U+346, U+34D, U+391-3=
A1, U+3A3-3A9, U+3B1-3C9, U+3D1, U+3D5-3D6, U+3F0-3F1, U+3F4-3F5, U+2016-20=
17, U+2034-2038, U+203C, U+2040, U+2043, U+2047, U+2050, U+2057, U+205F, U+=
2070-2071, U+2074-208E, U+2090-209C, U+20D0-20DC, U+20E1, U+20E5-20EF, U+21=
00-2112, U+2114-2115, U+2117-2121, U+2123-214F, U+2190, U+2192, U+2194-21AE=
, U+21B0-21E5, U+21F1-21F2, U+21F4-2211, U+2213-2214, U+2216-22FF, U+2308-2=
30B, U+2310, U+2319, U+231C-2321, U+2336-237A, U+237C, U+2395, U+239B-23B7,=
 U+23D0, U+23DC-23E1, U+2474-2475, U+25AF, U+25B3, U+25B7, U+25BD, U+25C1, =
U+25CA, U+25CC, U+25FB, U+266D-266F, U+27C0-27FF, U+2900-2AFF, U+2B0E-2B11,=
 U+2B30-2B4C, U+2BFE, U+3030, U+FF5B, U+FF5D, U+1D400-1D7FF, U+1EE00-1EEFF;=
 }

@font-face { font-family: Roboto; font-style: normal; font-weight: 700; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMaxKUBGEe.woff2") format("woff2"=
); unicode-range: U+1-C, U+E-1F, U+7F-9F, U+20DD-20E0, U+20E2-20E4, U+2150-=
218F, U+2190, U+2192, U+2194-2199, U+21AF, U+21E6-21F0, U+21F3, U+2218-2219=
, U+2299, U+22C4-22C6, U+2300-243F, U+2440-244A, U+2460-24FF, U+25A0-27BF, =
U+2800-28FF, U+2921-2922, U+2981, U+29BF, U+29EB, U+2B00-2BFF, U+4DC0-4DFF,=
 U+FFF9-FFFB, U+10140-1018E, U+10190-1019C, U+101A0, U+101D0-101FD, U+102E0=
-102FB, U+10E60-10E7E, U+1D2C0-1D2D3, U+1D2E0-1D37F, U+1F000-1F0FF, U+1F100=
-1F1AD, U+1F1E6-1F1FF, U+1F30D-1F30F, U+1F315, U+1F31C, U+1F31E, U+1F320-1F=
32C, U+1F336, U+1F378, U+1F37D, U+1F382, U+1F393-1F39F, U+1F3A7-1F3A8, U+1F=
3AC-1F3AF, U+1F3C2, U+1F3C4-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F3E0, U+1F3ED, U=
+1F3F1-1F3F3, U+1F3F5-1F3F7, U+1F408, U+1F415, U+1F41F, U+1F426, U+1F43F, U=
+1F441-1F442, U+1F444, U+1F446-1F449, U+1F44C-1F44E, U+1F453, U+1F46A, U+1F=
47D, U+1F4A3, U+1F4B0, U+1F4B3, U+1F4B9, U+1F4BB, U+1F4BF, U+1F4C8-1F4CB, U=
+1F4D6, U+1F4DA, U+1F4DF, U+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F4F7, U+1F4F9-1F=
4FB, U+1F4FD-1F4FE, U+1F503, U+1F507-1F50B, U+1F50D, U+1F512-1F513, U+1F53E=
-1F54A, U+1F54F-1F5FA, U+1F610, U+1F650-1F67F, U+1F687, U+1F68D, U+1F691, U=
+1F694, U+1F698, U+1F6AD, U+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U+1F6C6-1F6CF, U=
+1F6D3-1F6D7, U+1F6E0-1F6EA, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U+1F700-1F7FF, U=
+1F800-1F80B, U+1F810-1F847, U+1F850-1F859, U+1F860-1F887, U+1F890-1F8AD, U=
+1F8B0-1F8BB, U+1F8C0-1F8C1, U+1F900-1F90B, U+1F93B, U+1F946, U+1F984, U+1F=
996, U+1F9E9, U+1FA00-1FA6F, U+1FA70-1FA7C, U+1FA80-1FA89, U+1FA8F-1FAC6, U=
+1FACE-1FADC, U+1FADF-1FAE9, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 700; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3OUBGEe.woff2") format("woff2"=
); unicode-range: U+102-103, U+110-111, U+128-129, U+168-169, U+1A0-1A1, U+=
1AF-1B0, U+300-301, U+303-304, U+308-309, U+323, U+329, U+1EA0-1EF9, U+20AB=
; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 700; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3KUBGEe.woff2") format("woff2"=
); unicode-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF, U+=
304, U+308, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20=
AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 700; fon=
t-stretch: 100%; font-display: block; src: url("https://fonts.gstatic.com/s=
/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBA.woff2") format("woff2");=
 unicode-range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA, U+2DC, U=
+304, U+308, U+329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+=
2215, U+FEFF, U+FFFD; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: https://fonts.googleapis.com/css2?family=Google+Symbols:FILL@0..1&display=block

@charset "utf-8";

@font-face { font-family: "Google Symbols"; font-style: normal; font-weight=
: 400; font-display: block; src: url("https://fonts.gstatic.com/s/googlesym=
bols/v413/HhzZU5Ak9u-oMExPeInvcuEmPosC9zS3FYkFU68cPrjdKM1XMoDZlWmzc3IiWvF1S=
bxVhQidBnv_C_ar1J9g0sLBUv3G8taXmA.woff2") format("woff2"); }

.google-symbols { font-family: "Google Symbols"; font-weight: normal; font-=
style: normal; font-size: 24px; line-height: 1; letter-spacing: normal; tex=
t-transform: none; display: inline-block; white-space: nowrap; overflow-wra=
p: normal; direction: ltr; font-feature-settings: "liga"; -webkit-font-smoo=
thing: antialiased; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: cid:css-73d37a7a-4351-48e3-8997-662d892598fd@mhtml.blink

@charset "utf-8";

.codicon-add::before { content: "=EE=A9=A0"; }

.codicon-plus::before { content: "=EE=A9=A0"; }

.codicon-gist-new::before { content: "=EE=A9=A0"; }

.codicon-repo-create::before { content: "=EE=A9=A0"; }

.codicon-lightbulb::before { content: "=EE=A9=A1"; }

.codicon-light-bulb::before { content: "=EE=A9=A1"; }

.codicon-repo::before { content: "=EE=A9=A2"; }

.codicon-repo-delete::before { content: "=EE=A9=A2"; }

.codicon-gist-fork::before { content: "=EE=A9=A3"; }

.codicon-repo-forked::before { content: "=EE=A9=A3"; }

.codicon-git-pull-request::before { content: "=EE=A9=A4"; }

.codicon-git-pull-request-abandoned::before { content: "=EE=A9=A4"; }

.codicon-record-keys::before { content: "=EE=A9=A5"; }

.codicon-keyboard::before { content: "=EE=A9=A5"; }

.codicon-tag::before { content: "=EE=A9=A6"; }

.codicon-tag-add::before { content: "=EE=A9=A6"; }

.codicon-tag-remove::before { content: "=EE=A9=A6"; }

.codicon-person::before { content: "=EE=A9=A7"; }

.codicon-person-follow::before { content: "=EE=A9=A7"; }

.codicon-person-outline::before { content: "=EE=A9=A7"; }

.codicon-person-filled::before { content: "=EE=A9=A7"; }

.codicon-git-branch::before { content: "=EE=A9=A8"; }

.codicon-git-branch-create::before { content: "=EE=A9=A8"; }

.codicon-git-branch-delete::before { content: "=EE=A9=A8"; }

.codicon-source-control::before { content: "=EE=A9=A8"; }

.codicon-mirror::before { content: "=EE=A9=A9"; }

.codicon-mirror-public::before { content: "=EE=A9=A9"; }

.codicon-star::before { content: "=EE=A9=AA"; }

.codicon-star-add::before { content: "=EE=A9=AA"; }

.codicon-star-delete::before { content: "=EE=A9=AA"; }

.codicon-star-empty::before { content: "=EE=A9=AA"; }

.codicon-comment::before { content: "=EE=A9=AB"; }

.codicon-comment-add::before { content: "=EE=A9=AB"; }

.codicon-alert::before { content: "=EE=A9=AC"; }

.codicon-warning::before { content: "=EE=A9=AC"; }

.codicon-search::before { content: "=EE=A9=AD"; }

.codicon-search-save::before { content: "=EE=A9=AD"; }

.codicon-log-out::before { content: "=EE=A9=AE"; }

.codicon-sign-out::before { content: "=EE=A9=AE"; }

.codicon-log-in::before { content: "=EE=A9=AF"; }

.codicon-sign-in::before { content: "=EE=A9=AF"; }

.codicon-eye::before { content: "=EE=A9=B0"; }

.codicon-eye-unwatch::before { content: "=EE=A9=B0"; }

.codicon-eye-watch::before { content: "=EE=A9=B0"; }

.codicon-circle-filled::before { content: "=EE=A9=B1"; }

.codicon-primitive-dot::before { content: "=EE=A9=B1"; }

.codicon-close-dirty::before { content: "=EE=A9=B1"; }

.codicon-debug-breakpoint::before { content: "=EE=A9=B1"; }

.codicon-debug-breakpoint-disabled::before { content: "=EE=A9=B1"; }

.codicon-debug-hint::before { content: "=EE=A9=B1"; }

.codicon-primitive-square::before { content: "=EE=A9=B2"; }

.codicon-edit::before { content: "=EE=A9=B3"; }

.codicon-pencil::before { content: "=EE=A9=B3"; }

.codicon-info::before { content: "=EE=A9=B4"; }

.codicon-issue-opened::before { content: "=EE=A9=B4"; }

.codicon-gist-private::before { content: "=EE=A9=B5"; }

.codicon-git-fork-private::before { content: "=EE=A9=B5"; }

.codicon-lock::before { content: "=EE=A9=B5"; }

.codicon-mirror-private::before { content: "=EE=A9=B5"; }

.codicon-close::before { content: "=EE=A9=B6"; }

.codicon-remove-close::before { content: "=EE=A9=B6"; }

.codicon-x::before { content: "=EE=A9=B6"; }

.codicon-repo-sync::before { content: "=EE=A9=B7"; }

.codicon-sync::before { content: "=EE=A9=B7"; }

.codicon-clone::before { content: "=EE=A9=B8"; }

.codicon-desktop-download::before { content: "=EE=A9=B8"; }

.codicon-beaker::before { content: "=EE=A9=B9"; }

.codicon-microscope::before { content: "=EE=A9=B9"; }

.codicon-vm::before { content: "=EE=A9=BA"; }

.codicon-device-desktop::before { content: "=EE=A9=BA"; }

.codicon-file::before { content: "=EE=A9=BB"; }

.codicon-file-text::before { content: "=EE=A9=BB"; }

.codicon-more::before { content: "=EE=A9=BC"; }

.codicon-ellipsis::before { content: "=EE=A9=BC"; }

.codicon-kebab-horizontal::before { content: "=EE=A9=BC"; }

.codicon-mail-reply::before { content: "=EE=A9=BD"; }

.codicon-reply::before { content: "=EE=A9=BD"; }

.codicon-organization::before { content: "=EE=A9=BE"; }

.codicon-organization-filled::before { content: "=EE=A9=BE"; }

.codicon-organization-outline::before { content: "=EE=A9=BE"; }

.codicon-new-file::before { content: "=EE=A9=BF"; }

.codicon-file-add::before { content: "=EE=A9=BF"; }

.codicon-new-folder::before { content: "=EE=AA=80"; }

.codicon-file-directory-create::before { content: "=EE=AA=80"; }

.codicon-trash::before { content: "=EE=AA=81"; }

.codicon-trashcan::before { content: "=EE=AA=81"; }

.codicon-history::before { content: "=EE=AA=82"; }

.codicon-clock::before { content: "=EE=AA=82"; }

.codicon-folder::before { content: "=EE=AA=83"; }

.codicon-file-directory::before { content: "=EE=AA=83"; }

.codicon-symbol-folder::before { content: "=EE=AA=83"; }

.codicon-logo-github::before { content: "=EE=AA=84"; }

.codicon-mark-github::before { content: "=EE=AA=84"; }

.codicon-github::before { content: "=EE=AA=84"; }

.codicon-terminal::before { content: "=EE=AA=85"; }

.codicon-console::before { content: "=EE=AA=85"; }

.codicon-repl::before { content: "=EE=AA=85"; }

.codicon-zap::before { content: "=EE=AA=86"; }

.codicon-symbol-event::before { content: "=EE=AA=86"; }

.codicon-error::before { content: "=EE=AA=87"; }

.codicon-stop::before { content: "=EE=AA=87"; }

.codicon-variable::before { content: "=EE=AA=88"; }

.codicon-symbol-variable::before { content: "=EE=AA=88"; }

.codicon-array::before { content: "=EE=AA=8A"; }

.codicon-symbol-array::before { content: "=EE=AA=8A"; }

.codicon-symbol-module::before { content: "=EE=AA=8B"; }

.codicon-symbol-package::before { content: "=EE=AA=8B"; }

.codicon-symbol-namespace::before { content: "=EE=AA=8B"; }

.codicon-symbol-object::before { content: "=EE=AA=8B"; }

.codicon-symbol-method::before { content: "=EE=AA=8C"; }

.codicon-symbol-function::before { content: "=EE=AA=8C"; }

.codicon-symbol-constructor::before { content: "=EE=AA=8C"; }

.codicon-symbol-boolean::before { content: "=EE=AA=8F"; }

.codicon-symbol-null::before { content: "=EE=AA=8F"; }

.codicon-symbol-numeric::before { content: "=EE=AA=90"; }

.codicon-symbol-number::before { content: "=EE=AA=90"; }

.codicon-symbol-structure::before { content: "=EE=AA=91"; }

.codicon-symbol-struct::before { content: "=EE=AA=91"; }

.codicon-symbol-parameter::before { content: "=EE=AA=92"; }

.codicon-symbol-type-parameter::before { content: "=EE=AA=92"; }

.codicon-symbol-key::before { content: "=EE=AA=93"; }

.codicon-symbol-text::before { content: "=EE=AA=93"; }

.codicon-symbol-reference::before { content: "=EE=AA=94"; }

.codicon-go-to-file::before { content: "=EE=AA=94"; }

.codicon-symbol-enum::before { content: "=EE=AA=95"; }

.codicon-symbol-value::before { content: "=EE=AA=95"; }

.codicon-symbol-ruler::before { content: "=EE=AA=96"; }

.codicon-symbol-unit::before { content: "=EE=AA=96"; }

.codicon-activate-breakpoints::before { content: "=EE=AA=97"; }

.codicon-archive::before { content: "=EE=AA=98"; }

.codicon-arrow-both::before { content: "=EE=AA=99"; }

.codicon-arrow-down::before { content: "=EE=AA=9A"; }

.codicon-arrow-left::before { content: "=EE=AA=9B"; }

.codicon-arrow-right::before { content: "=EE=AA=9C"; }

.codicon-arrow-small-down::before { content: "=EE=AA=9D"; }

.codicon-arrow-small-left::before { content: "=EE=AA=9E"; }

.codicon-arrow-small-right::before { content: "=EE=AA=9F"; }

.codicon-arrow-small-up::before { content: "=EE=AA=A0"; }

.codicon-arrow-up::before { content: "=EE=AA=A1"; }

.codicon-bell::before { content: "=EE=AA=A2"; }

.codicon-bold::before { content: "=EE=AA=A3"; }

.codicon-book::before { content: "=EE=AA=A4"; }

.codicon-bookmark::before { content: "=EE=AA=A5"; }

.codicon-debug-breakpoint-conditional-unverified::before { content: "=EE=AA=
=A6"; }

.codicon-debug-breakpoint-conditional::before { content: "=EE=AA=A7"; }

.codicon-debug-breakpoint-conditional-disabled::before { content: "=EE=AA=
=A7"; }

.codicon-debug-breakpoint-data-unverified::before { content: "=EE=AA=A8"; }

.codicon-debug-breakpoint-data::before { content: "=EE=AA=A9"; }

.codicon-debug-breakpoint-data-disabled::before { content: "=EE=AA=A9"; }

.codicon-debug-breakpoint-log-unverified::before { content: "=EE=AA=AA"; }

.codicon-debug-breakpoint-log::before { content: "=EE=AA=AB"; }

.codicon-debug-breakpoint-log-disabled::before { content: "=EE=AA=AB"; }

.codicon-briefcase::before { content: "=EE=AA=AC"; }

.codicon-broadcast::before { content: "=EE=AA=AD"; }

.codicon-browser::before { content: "=EE=AA=AE"; }

.codicon-bug::before { content: "=EE=AA=AF"; }

.codicon-calendar::before { content: "=EE=AA=B0"; }

.codicon-case-sensitive::before { content: "=EE=AA=B1"; }

.codicon-check::before { content: "=EE=AA=B2"; }

.codicon-checklist::before { content: "=EE=AA=B3"; }

.codicon-chevron-down::before { content: "=EE=AA=B4"; }

.codicon-drop-down-button::before { content: "=EE=AA=B4"; }

.codicon-chevron-left::before { content: "=EE=AA=B5"; }

.codicon-chevron-right::before { content: "=EE=AA=B6"; }

.codicon-chevron-up::before { content: "=EE=AA=B7"; }

.codicon-chrome-close::before { content: "=EE=AA=B8"; }

.codicon-chrome-maximize::before { content: "=EE=AA=B9"; }

.codicon-chrome-minimize::before { content: "=EE=AA=BA"; }

.codicon-chrome-restore::before { content: "=EE=AA=BB"; }

.codicon-circle::before { content: "=EE=AA=BC"; }

.codicon-circle-outline::before { content: "=EE=AA=BC"; }

.codicon-debug-breakpoint-unverified::before { content: "=EE=AA=BC"; }

.codicon-circle-slash::before { content: "=EE=AA=BD"; }

.codicon-circuit-board::before { content: "=EE=AA=BE"; }

.codicon-clear-all::before { content: "=EE=AA=BF"; }

.codicon-clippy::before { content: "=EE=AB=80"; }

.codicon-close-all::before { content: "=EE=AB=81"; }

.codicon-cloud-download::before { content: "=EE=AB=82"; }

.codicon-cloud-upload::before { content: "=EE=AB=83"; }

.codicon-code::before { content: "=EE=AB=84"; }

.codicon-collapse-all::before { content: "=EE=AB=85"; }

.codicon-color-mode::before { content: "=EE=AB=86"; }

.codicon-comment-discussion::before { content: "=EE=AB=87"; }

.codicon-compare-changes::before { content: "=EE=AB=BD"; }

.codicon-credit-card::before { content: "=EE=AB=89"; }

.codicon-dash::before { content: "=EE=AB=8C"; }

.codicon-dashboard::before { content: "=EE=AB=8D"; }

.codicon-database::before { content: "=EE=AB=8E"; }

.codicon-debug-continue::before { content: "=EE=AB=8F"; }

.codicon-debug-disconnect::before { content: "=EE=AB=90"; }

.codicon-debug-pause::before { content: "=EE=AB=91"; }

.codicon-debug-restart::before { content: "=EE=AB=92"; }

.codicon-debug-start::before { content: "=EE=AB=93"; }

.codicon-debug-step-into::before { content: "=EE=AB=94"; }

.codicon-debug-step-out::before { content: "=EE=AB=95"; }

.codicon-debug-step-over::before { content: "=EE=AB=96"; }

.codicon-debug-stop::before { content: "=EE=AB=97"; }

.codicon-debug::before { content: "=EE=AB=98"; }

.codicon-device-camera-video::before { content: "=EE=AB=99"; }

.codicon-device-camera::before { content: "=EE=AB=9A"; }

.codicon-device-mobile::before { content: "=EE=AB=9B"; }

.codicon-diff-added::before { content: "=EE=AB=9C"; }

.codicon-diff-ignored::before { content: "=EE=AB=9D"; }

.codicon-diff-modified::before { content: "=EE=AB=9E"; }

.codicon-diff-removed::before { content: "=EE=AB=9F"; }

.codicon-diff-renamed::before { content: "=EE=AB=A0"; }

.codicon-diff::before { content: "=EE=AB=A1"; }

.codicon-discard::before { content: "=EE=AB=A2"; }

.codicon-editor-layout::before { content: "=EE=AB=A3"; }

.codicon-empty-window::before { content: "=EE=AB=A4"; }

.codicon-exclude::before { content: "=EE=AB=A5"; }

.codicon-extensions::before { content: "=EE=AB=A6"; }

.codicon-eye-closed::before { content: "=EE=AB=A7"; }

.codicon-file-binary::before { content: "=EE=AB=A8"; }

.codicon-file-code::before { content: "=EE=AB=A9"; }

.codicon-file-media::before { content: "=EE=AB=AA"; }

.codicon-file-pdf::before { content: "=EE=AB=AB"; }

.codicon-file-submodule::before { content: "=EE=AB=AC"; }

.codicon-file-symlink-directory::before { content: "=EE=AB=AD"; }

.codicon-file-symlink-file::before { content: "=EE=AB=AE"; }

.codicon-file-zip::before { content: "=EE=AB=AF"; }

.codicon-files::before { content: "=EE=AB=B0"; }

.codicon-filter::before { content: "=EE=AB=B1"; }

.codicon-flame::before { content: "=EE=AB=B2"; }

.codicon-fold-down::before { content: "=EE=AB=B3"; }

.codicon-fold-up::before { content: "=EE=AB=B4"; }

.codicon-fold::before { content: "=EE=AB=B5"; }

.codicon-folder-active::before { content: "=EE=AB=B6"; }

.codicon-folder-opened::before { content: "=EE=AB=B7"; }

.codicon-gear::before { content: "=EE=AB=B8"; }

.codicon-gift::before { content: "=EE=AB=B9"; }

.codicon-gist-secret::before { content: "=EE=AB=BA"; }

.codicon-gist::before { content: "=EE=AB=BB"; }

.codicon-git-commit::before { content: "=EE=AB=BC"; }

.codicon-git-compare::before { content: "=EE=AB=BD"; }

.codicon-git-merge::before { content: "=EE=AB=BE"; }

.codicon-github-action::before { content: "=EE=AB=BF"; }

.codicon-github-alt::before { content: "=EE=AC=80"; }

.codicon-globe::before { content: "=EE=AC=81"; }

.codicon-grabber::before { content: "=EE=AC=82"; }

.codicon-graph::before { content: "=EE=AC=83"; }

.codicon-gripper::before { content: "=EE=AC=84"; }

.codicon-heart::before { content: "=EE=AC=85"; }

.codicon-home::before { content: "=EE=AC=86"; }

.codicon-horizontal-rule::before { content: "=EE=AC=87"; }

.codicon-hubot::before { content: "=EE=AC=88"; }

.codicon-inbox::before { content: "=EE=AC=89"; }

.codicon-issue-closed::before { content: "=EE=AE=A4"; }

.codicon-issue-reopened::before { content: "=EE=AC=8B"; }

.codicon-issues::before { content: "=EE=AC=8C"; }

.codicon-italic::before { content: "=EE=AC=8D"; }

.codicon-jersey::before { content: "=EE=AC=8E"; }

.codicon-json::before { content: "=EE=AC=8F"; }

.codicon-bracket::before { content: "=EE=AC=8F"; }

.codicon-kebab-vertical::before { content: "=EE=AC=90"; }

.codicon-key::before { content: "=EE=AC=91"; }

.codicon-law::before { content: "=EE=AC=92"; }

.codicon-lightbulb-autofix::before { content: "=EE=AC=93"; }

.codicon-link-external::before { content: "=EE=AC=94"; }

.codicon-link::before { content: "=EE=AC=95"; }

.codicon-list-ordered::before { content: "=EE=AC=96"; }

.codicon-list-unordered::before { content: "=EE=AC=97"; }

.codicon-live-share::before { content: "=EE=AC=98"; }

.codicon-loading::before { content: "=EE=AC=99"; }

.codicon-location::before { content: "=EE=AC=9A"; }

.codicon-mail-read::before { content: "=EE=AC=9B"; }

.codicon-mail::before { content: "=EE=AC=9C"; }

.codicon-markdown::before { content: "=EE=AC=9D"; }

.codicon-megaphone::before { content: "=EE=AC=9E"; }

.codicon-mention::before { content: "=EE=AC=9F"; }

.codicon-milestone::before { content: "=EE=AC=A0"; }

.codicon-mortar-board::before { content: "=EE=AC=A1"; }

.codicon-move::before { content: "=EE=AC=A2"; }

.codicon-multiple-windows::before { content: "=EE=AC=A3"; }

.codicon-mute::before { content: "=EE=AC=A4"; }

.codicon-no-newline::before { content: "=EE=AC=A5"; }

.codicon-note::before { content: "=EE=AC=A6"; }

.codicon-octoface::before { content: "=EE=AC=A7"; }

.codicon-open-preview::before { content: "=EE=AC=A8"; }

.codicon-package::before { content: "=EE=AC=A9"; }

.codicon-paintcan::before { content: "=EE=AC=AA"; }

.codicon-pin::before { content: "=EE=AC=AB"; }

.codicon-play::before { content: "=EE=AC=AC"; }

.codicon-run::before { content: "=EE=AC=AC"; }

.codicon-plug::before { content: "=EE=AC=AD"; }

.codicon-preserve-case::before { content: "=EE=AC=AE"; }

.codicon-preview::before { content: "=EE=AC=AF"; }

.codicon-project::before { content: "=EE=AC=B0"; }

.codicon-pulse::before { content: "=EE=AC=B1"; }

.codicon-question::before { content: "=EE=AC=B2"; }

.codicon-quote::before { content: "=EE=AC=B3"; }

.codicon-radio-tower::before { content: "=EE=AC=B4"; }

.codicon-reactions::before { content: "=EE=AC=B5"; }

.codicon-references::before { content: "=EE=AC=B6"; }

.codicon-refresh::before { content: "=EE=AC=B7"; }

.codicon-regex::before { content: "=EE=AC=B8"; }

.codicon-remote-explorer::before { content: "=EE=AC=B9"; }

.codicon-remote::before { content: "=EE=AC=BA"; }

.codicon-remove::before { content: "=EE=AC=BB"; }

.codicon-replace-all::before { content: "=EE=AC=BC"; }

.codicon-replace::before { content: "=EE=AC=BD"; }

.codicon-repo-clone::before { content: "=EE=AC=BE"; }

.codicon-repo-force-push::before { content: "=EE=AC=BF"; }

.codicon-repo-pull::before { content: "=EE=AD=80"; }

.codicon-repo-push::before { content: "=EE=AD=81"; }

.codicon-report::before { content: "=EE=AD=82"; }

.codicon-request-changes::before { content: "=EE=AD=83"; }

.codicon-rocket::before { content: "=EE=AD=84"; }

.codicon-root-folder-opened::before { content: "=EE=AD=85"; }

.codicon-root-folder::before { content: "=EE=AD=86"; }

.codicon-rss::before { content: "=EE=AD=87"; }

.codicon-ruby::before { content: "=EE=AD=88"; }

.codicon-save-all::before { content: "=EE=AD=89"; }

.codicon-save-as::before { content: "=EE=AD=8A"; }

.codicon-save::before { content: "=EE=AD=8B"; }

.codicon-screen-full::before { content: "=EE=AD=8C"; }

.codicon-screen-normal::before { content: "=EE=AD=8D"; }

.codicon-search-stop::before { content: "=EE=AD=8E"; }

.codicon-server::before { content: "=EE=AD=90"; }

.codicon-settings-gear::before { content: "=EE=AD=91"; }

.codicon-settings::before { content: "=EE=AD=92"; }

.codicon-shield::before { content: "=EE=AD=93"; }

.codicon-smiley::before { content: "=EE=AD=94"; }

.codicon-sort-precedence::before { content: "=EE=AD=95"; }

.codicon-split-horizontal::before { content: "=EE=AD=96"; }

.codicon-split-vertical::before { content: "=EE=AD=97"; }

.codicon-squirrel::before { content: "=EE=AD=98"; }

.codicon-star-full::before { content: "=EE=AD=99"; }

.codicon-star-half::before { content: "=EE=AD=9A"; }

.codicon-symbol-class::before { content: "=EE=AD=9B"; }

.codicon-symbol-color::before { content: "=EE=AD=9C"; }

.codicon-symbol-customcolor::before { content: "=EE=AD=9C"; }

.codicon-symbol-constant::before { content: "=EE=AD=9D"; }

.codicon-symbol-enum-member::before { content: "=EE=AD=9E"; }

.codicon-symbol-field::before { content: "=EE=AD=9F"; }

.codicon-symbol-file::before { content: "=EE=AD=A0"; }

.codicon-symbol-interface::before { content: "=EE=AD=A1"; }

.codicon-symbol-keyword::before { content: "=EE=AD=A2"; }

.codicon-symbol-misc::before { content: "=EE=AD=A3"; }

.codicon-symbol-operator::before { content: "=EE=AD=A4"; }

.codicon-symbol-property::before { content: "=EE=AD=A5"; }

.codicon-wrench::before { content: "=EE=AD=A5"; }

.codicon-wrench-subaction::before { content: "=EE=AD=A5"; }

.codicon-symbol-snippet::before { content: "=EE=AD=A6"; }

.codicon-tasklist::before { content: "=EE=AD=A7"; }

.codicon-telescope::before { content: "=EE=AD=A8"; }

.codicon-text-size::before { content: "=EE=AD=A9"; }

.codicon-three-bars::before { content: "=EE=AD=AA"; }

.codicon-thumbsdown::before { content: "=EE=AD=AB"; }

.codicon-thumbsup::before { content: "=EE=AD=AC"; }

.codicon-tools::before { content: "=EE=AD=AD"; }

.codicon-triangle-down::before { content: "=EE=AD=AE"; }

.codicon-triangle-left::before { content: "=EE=AD=AF"; }

.codicon-triangle-right::before { content: "=EE=AD=B0"; }

.codicon-triangle-up::before { content: "=EE=AD=B1"; }

.codicon-twitter::before { content: "=EE=AD=B2"; }

.codicon-unfold::before { content: "=EE=AD=B3"; }

.codicon-unlock::before { content: "=EE=AD=B4"; }

.codicon-unmute::before { content: "=EE=AD=B5"; }

.codicon-unverified::before { content: "=EE=AD=B6"; }

.codicon-verified::before { content: "=EE=AD=B7"; }

.codicon-versions::before { content: "=EE=AD=B8"; }

.codicon-vm-active::before { content: "=EE=AD=B9"; }

.codicon-vm-outline::before { content: "=EE=AD=BA"; }

.codicon-vm-running::before { content: "=EE=AD=BB"; }

.codicon-watch::before { content: "=EE=AD=BC"; }

.codicon-whitespace::before { content: "=EE=AD=BD"; }

.codicon-whole-word::before { content: "=EE=AD=BE"; }

.codicon-window::before { content: "=EE=AD=BF"; }

.codicon-word-wrap::before { content: "=EE=AE=80"; }

.codicon-zoom-in::before { content: "=EE=AE=81"; }

.codicon-zoom-out::before { content: "=EE=AE=82"; }

.codicon-list-filter::before { content: "=EE=AE=83"; }

.codicon-list-flat::before { content: "=EE=AE=84"; }

.codicon-list-selection::before { content: "=EE=AE=85"; }

.codicon-selection::before { content: "=EE=AE=85"; }

.codicon-list-tree::before { content: "=EE=AE=86"; }

.codicon-debug-breakpoint-function-unverified::before { content: "=EE=AE=87=
"; }

.codicon-debug-breakpoint-function::before { content: "=EE=AE=88"; }

.codicon-debug-breakpoint-function-disabled::before { content: "=EE=AE=88";=
 }

.codicon-debug-stackframe-active::before { content: "=EE=AE=89"; }

.codicon-circle-small-filled::before { content: "=EE=AE=8A"; }

.codicon-debug-stackframe-dot::before { content: "=EE=AE=8A"; }

.codicon-debug-stackframe::before { content: "=EE=AE=8B"; }

.codicon-debug-stackframe-focused::before { content: "=EE=AE=8B"; }

.codicon-debug-breakpoint-unsupported::before { content: "=EE=AE=8C"; }

.codicon-symbol-string::before { content: "=EE=AE=8D"; }

.codicon-debug-reverse-continue::before { content: "=EE=AE=8E"; }

.codicon-debug-step-back::before { content: "=EE=AE=8F"; }

.codicon-debug-restart-frame::before { content: "=EE=AE=90"; }

.codicon-call-incoming::before { content: "=EE=AE=92"; }

.codicon-call-outgoing::before { content: "=EE=AE=93"; }

.codicon-menu::before { content: "=EE=AE=94"; }

.codicon-expand-all::before { content: "=EE=AE=95"; }

.codicon-feedback::before { content: "=EE=AE=96"; }

.codicon-group-by-ref-type::before { content: "=EE=AE=97"; }

.codicon-ungroup-by-ref-type::before { content: "=EE=AE=98"; }

.codicon-account::before { content: "=EE=AE=99"; }

.codicon-bell-dot::before { content: "=EE=AE=9A"; }

.codicon-debug-console::before { content: "=EE=AE=9B"; }

.codicon-library::before { content: "=EE=AE=9C"; }

.codicon-output::before { content: "=EE=AE=9D"; }

.codicon-run-all::before { content: "=EE=AE=9E"; }

.codicon-sync-ignored::before { content: "=EE=AE=9F"; }

.codicon-pinned::before { content: "=EE=AE=A0"; }

.codicon-github-inverted::before { content: "=EE=AE=A1"; }

.codicon-debug-alt::before { content: "=EE=AE=91"; }

.codicon-server-process::before { content: "=EE=AE=A2"; }

.codicon-server-environment::before { content: "=EE=AE=A3"; }

.codicon-pass::before { content: "=EE=AE=A4"; }

.codicon-stop-circle::before { content: "=EE=AE=A5"; }

.codicon-play-circle::before { content: "=EE=AE=A6"; }

.codicon-record::before { content: "=EE=AE=A7"; }

.codicon-debug-alt-small::before { content: "=EE=AE=A8"; }

.codicon-vm-connect::before { content: "=EE=AE=A9"; }

.codicon-cloud::before { content: "=EE=AE=AA"; }

.codicon-merge::before { content: "=EE=AE=AB"; }

.codicon-export::before { content: "=EE=AE=AC"; }

.codicon-graph-left::before { content: "=EE=AE=AD"; }

.codicon-magnet::before { content: "=EE=AE=AE"; }

.codicon-notebook::before { content: "=EE=AE=AF"; }

.codicon-redo::before { content: "=EE=AE=B0"; }

.codicon-check-all::before { content: "=EE=AE=B1"; }

.codicon-pinned-dirty::before { content: "=EE=AE=B2"; }

.codicon-pass-filled::before { content: "=EE=AE=B3"; }

.codicon-circle-large-filled::before { content: "=EE=AE=B4"; }

.codicon-circle-large::before { content: "=EE=AE=B5"; }

.codicon-circle-large-outline::before { content: "=EE=AE=B5"; }

.codicon-combine::before { content: "=EE=AE=B6"; }

.codicon-gather::before { content: "=EE=AE=B6"; }

.codicon-table::before { content: "=EE=AE=B7"; }

.codicon-variable-group::before { content: "=EE=AE=B8"; }

.codicon-type-hierarchy::before { content: "=EE=AE=B9"; }

.codicon-type-hierarchy-sub::before { content: "=EE=AE=BA"; }

.codicon-type-hierarchy-super::before { content: "=EE=AE=BB"; }

.codicon-git-pull-request-create::before { content: "=EE=AE=BC"; }

.codicon-run-above::before { content: "=EE=AE=BD"; }

.codicon-run-below::before { content: "=EE=AE=BE"; }

.codicon-notebook-template::before { content: "=EE=AE=BF"; }

.codicon-debug-rerun::before { content: "=EE=AF=80"; }

.codicon-workspace-trusted::before { content: "=EE=AF=81"; }

.codicon-workspace-untrusted::before { content: "=EE=AF=82"; }

.codicon-workspace-unspecified::before { content: "=EE=AF=83"; }

.codicon-terminal-cmd::before { content: "=EE=AF=84"; }

.codicon-terminal-debian::before { content: "=EE=AF=85"; }

.codicon-terminal-linux::before { content: "=EE=AF=86"; }

.codicon-terminal-powershell::before { content: "=EE=AF=87"; }

.codicon-terminal-tmux::before { content: "=EE=AF=88"; }

.codicon-terminal-ubuntu::before { content: "=EE=AF=89"; }

.codicon-terminal-bash::before { content: "=EE=AF=8A"; }

.codicon-arrow-swap::before { content: "=EE=AF=8B"; }

.codicon-copy::before { content: "=EE=AF=8C"; }

.codicon-person-add::before { content: "=EE=AF=8D"; }

.codicon-filter-filled::before { content: "=EE=AF=8E"; }

.codicon-wand::before { content: "=EE=AF=8F"; }

.codicon-debug-line-by-line::before { content: "=EE=AF=90"; }

.codicon-inspect::before { content: "=EE=AF=91"; }

.codicon-layers::before { content: "=EE=AF=92"; }

.codicon-layers-dot::before { content: "=EE=AF=93"; }

.codicon-layers-active::before { content: "=EE=AF=94"; }

.codicon-compass::before { content: "=EE=AF=95"; }

.codicon-compass-dot::before { content: "=EE=AF=96"; }

.codicon-compass-active::before { content: "=EE=AF=97"; }

.codicon-azure::before { content: "=EE=AF=98"; }

.codicon-issue-draft::before { content: "=EE=AF=99"; }

.codicon-git-pull-request-closed::before { content: "=EE=AF=9A"; }

.codicon-git-pull-request-draft::before { content: "=EE=AF=9B"; }

.codicon-debug-all::before { content: "=EE=AF=9C"; }

.codicon-debug-coverage::before { content: "=EE=AF=9D"; }

.codicon-run-errors::before { content: "=EE=AF=9E"; }

.codicon-folder-library::before { content: "=EE=AF=9F"; }

.codicon-debug-continue-small::before { content: "=EE=AF=A0"; }

.codicon-beaker-stop::before { content: "=EE=AF=A1"; }

.codicon-graph-line::before { content: "=EE=AF=A2"; }

.codicon-graph-scatter::before { content: "=EE=AF=A3"; }

.codicon-pie-chart::before { content: "=EE=AF=A4"; }

.codicon-bracket-dot::before { content: "=EE=AF=A5"; }

.codicon-bracket-error::before { content: "=EE=AF=A6"; }

.codicon-lock-small::before { content: "=EE=AF=A7"; }

.codicon-azure-devops::before { content: "=EE=AF=A8"; }

.codicon-verified-filled::before { content: "=EE=AF=A9"; }

.codicon-newline::before { content: "=EE=AF=AA"; }

.codicon-layout::before { content: "=EE=AF=AB"; }

.codicon-layout-activitybar-left::before { content: "=EE=AF=AC"; }

.codicon-layout-activitybar-right::before { content: "=EE=AF=AD"; }

.codicon-layout-panel-left::before { content: "=EE=AF=AE"; }

.codicon-layout-panel-center::before { content: "=EE=AF=AF"; }

.codicon-layout-panel-justify::before { content: "=EE=AF=B0"; }

.codicon-layout-panel-right::before { content: "=EE=AF=B1"; }

.codicon-layout-panel::before { content: "=EE=AF=B2"; }

.codicon-layout-sidebar-left::before { content: "=EE=AF=B3"; }

.codicon-layout-sidebar-right::before { content: "=EE=AF=B4"; }

.codicon-layout-statusbar::before { content: "=EE=AF=B5"; }

.codicon-layout-menubar::before { content: "=EE=AF=B6"; }

.codicon-layout-centered::before { content: "=EE=AF=B7"; }

.codicon-layout-sidebar-right-off::before { content: "=EE=B0=80"; }

.codicon-layout-panel-off::before { content: "=EE=B0=81"; }

.codicon-layout-sidebar-left-off::before { content: "=EE=B0=82"; }

.codicon-target::before { content: "=EE=AF=B8"; }

.codicon-indent::before { content: "=EE=AF=B9"; }

.codicon-record-small::before { content: "=EE=AF=BA"; }

.codicon-error-small::before { content: "=EE=AF=BB"; }

.codicon-arrow-circle-down::before { content: "=EE=AF=BC"; }

.codicon-arrow-circle-left::before { content: "=EE=AF=BD"; }

.codicon-arrow-circle-right::before { content: "=EE=AF=BE"; }

.codicon-arrow-circle-up::before { content: "=EE=AF=BF"; }

.codicon-heart-filled::before { content: "=EE=B0=84"; }

.codicon-map::before { content: "=EE=B0=85"; }

.codicon-map-filled::before { content: "=EE=B0=86"; }

.codicon-circle-small::before { content: "=EE=B0=87"; }

.codicon-bell-slash::before { content: "=EE=B0=88"; }

.codicon-bell-slash-dot::before { content: "=EE=B0=89"; }

.codicon-comment-unresolved::before { content: "=EE=B0=8A"; }

.codicon-git-pull-request-go-to-changes::before { content: "=EE=B0=8B"; }

.codicon-git-pull-request-new-changes::before { content: "=EE=B0=8C"; }

.codicon-search-fuzzy::before { content: "=EE=B0=8D"; }

.codicon-comment-draft::before { content: "=EE=B0=8E"; }

.codicon-send::before { content: "=EE=B0=8F"; }

.codicon-sparkle::before { content: "=EE=B0=90"; }

.codicon-insert::before { content: "=EE=B0=91"; }

.codicon-dialog-error::before { content: "=EE=AA=87"; }

.codicon-dialog-warning::before { content: "=EE=A9=AC"; }

.codicon-dialog-info::before { content: "=EE=A9=B4"; }

.codicon-dialog-close::before { content: "=EE=A9=B6"; }

.codicon-tree-item-expanded::before { content: "=EE=AA=B4"; }

.codicon-tree-filter-on-type-on::before { content: "=EE=AE=83"; }

.codicon-tree-filter-on-type-off::before { content: "=EE=AE=85"; }

.codicon-tree-filter-clear::before { content: "=EE=A9=B6"; }

.codicon-tree-item-loading::before { content: "=EE=AC=99"; }

.codicon-menu-selection::before { content: "=EE=AA=B2"; }

.codicon-menu-submenu::before { content: "=EE=AA=B6"; }

.codicon-menubar-more::before { content: "=EE=A9=BC"; }

.codicon-scrollbar-button-left::before { content: "=EE=AD=AF"; }

.codicon-scrollbar-button-right::before { content: "=EE=AD=B0"; }

.codicon-scrollbar-button-up::before { content: "=EE=AD=B1"; }

.codicon-scrollbar-button-down::before { content: "=EE=AD=AE"; }

.codicon-toolbar-more::before { content: "=EE=A9=BC"; }

.codicon-quick-input-back::before { content: "=EE=AA=9B"; }

.codicon-widget-close::before { content: "=EE=A9=B6"; }

.codicon-goto-previous-location::before { content: "=EE=AA=A1"; }

.codicon-goto-next-location::before { content: "=EE=AA=9A"; }

.codicon-diff-review-insert::before { content: "=EE=A9=A0"; }

.codicon-diff-review-remove::before { content: "=EE=AC=BB"; }

.codicon-diff-review-close::before { content: "=EE=A9=B6"; }

.codicon-parameter-hints-next::before { content: "=EE=AA=B4"; }

.codicon-parameter-hints-previous::before { content: "=EE=AA=B7"; }

.codicon-suggest-more-info::before { content: "=EE=AA=B6"; }

.codicon-inline-suggestion-hints-next::before { content: "=EE=AA=B6"; }

.codicon-inline-suggestion-hints-previous::before { content: "=EE=AA=B5"; }

.codicon-diff-insert::before { content: "=EE=A9=A0"; }

.codicon-diff-remove::before { content: "=EE=AC=BB"; }

.codicon-find-selection::before { content: "=EE=AE=85"; }

.codicon-find-collapsed::before { content: "=EE=AA=B6"; }

.codicon-find-expanded::before { content: "=EE=AA=B4"; }

.codicon-find-replace::before { content: "=EE=AC=BD"; }

.codicon-find-replace-all::before { content: "=EE=AC=BC"; }

.codicon-find-previous-match::before { content: "=EE=AA=A1"; }

.codicon-find-next-match::before { content: "=EE=AA=9A"; }

.codicon-folding-expanded::before { content: "=EE=AA=B4"; }

.codicon-folding-collapsed::before { content: "=EE=AA=B6"; }

.codicon-folding-manual-collapsed::before { content: "=EE=AA=B6"; }

.codicon-folding-manual-expanded::before { content: "=EE=AA=B4"; }

.codicon-marker-navigation-next::before { content: "=EE=AA=9A"; }

.codicon-marker-navigation-previous::before { content: "=EE=AA=A1"; }

.codicon-extensions-warning-message::before { content: "=EE=A9=AC"; }

.monaco-editor .inputarea.ime-input { background-color: rgb(255, 255, 255);=
 }

.monaco-editor .view-overlays .current-line { border: 2px solid rgb(238, 23=
8, 238); }

.monaco-editor .margin-view-overlays .current-line-margin { border: 2px sol=
id rgb(238, 238, 238); }

.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(4, 49, 250=
, 0.3); --guide-color-active: #0431fa; }

.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(49, 147, 4=
9, 0.3); --guide-color-active: #319331; }

.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(123, 56, 2=
0, 0.3); --guide-color-active: #7b3814; }

.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(4, 49, 250=
, 0.3); --guide-color-active: #0431fa; }

.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(49, 147, 4=
9, 0.3); --guide-color-active: #319331; }

.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(123, 56, 2=
0, 0.3); --guide-color-active: #7b3814; }

.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(4, 49, 250=
, 0.3); --guide-color-active: #0431fa; }

.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(49, 147, 4=
9, 0.3); --guide-color-active: #319331; }

.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(123, 56, 2=
0, 0.3); --guide-color-active: #7b3814; }

.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(4, 49, 250=
, 0.3); --guide-color-active: #0431fa; }

.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(49, 147, =
49, 0.3); --guide-color-active: #319331; }

.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(123, 56, =
20, 0.3); --guide-color-active: #7b3814; }

.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(4, 49, 25=
0, 0.3); --guide-color-active: #0431fa; }

.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(49, 147, =
49, 0.3); --guide-color-active: #319331; }

.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(123, 56, =
20, 0.3); --guide-color-active: #7b3814; }

.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(4, 49, 25=
0, 0.3); --guide-color-active: #0431fa; }

.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(49, 147, =
49, 0.3); --guide-color-active: #319331; }

.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(123, 56, =
20, 0.3); --guide-color-active: #7b3814; }

.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(4, 49, 25=
0, 0.3); --guide-color-active: #0431fa; }

.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(49, 147, =
49, 0.3); --guide-color-active: #319331; }

.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(123, 56, =
20, 0.3); --guide-color-active: #7b3814; }

.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(4, 49, 25=
0, 0.3); --guide-color-active: #0431fa; }

.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(49, 147, =
49, 0.3); --guide-color-active: #319331; }

.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(123, 56, =
20, 0.3); --guide-color-active: #7b3814; }

.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(4, 49, 25=
0, 0.3); --guide-color-active: #0431fa; }

.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(49, 147, =
49, 0.3); --guide-color-active: #319331; }

.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(123, 56, =
20, 0.3); --guide-color-active: #7b3814; }

.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(4, 49, 25=
0, 0.3); --guide-color-active: #0431fa; }

.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(49, 147, =
49, 0.3); --guide-color-active: #319331; }

.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(123, 56, =
20, 0.3); --guide-color-active: #7b3814; }

.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; =
}

.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); =
}

.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-co=
lor); }

.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-=
color-active) inset; }

.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--=
guide-color-active); }

.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid =
var(--guide-color-active); }

.monaco-editor .line-numbers.dimmed-line-number { color: rgba(153, 153, 153=
, 0.4); }

.monaco-editor .cursors-layer .cursor { background-color: rgb(0, 0, 0); bor=
der-color: rgb(0, 0, 0); color: rgb(255, 255, 255); }

.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8);=
 }

.monaco-editor .bracket-highlighting-0 { color: rgb(4, 49, 250); }

.monaco-editor .bracket-highlighting-1 { color: rgb(49, 147, 49); }

.monaco-editor .bracket-highlighting-2 { color: rgb(123, 56, 20); }

.monaco-editor .bracket-highlighting-3 { color: rgb(4, 49, 250); }

.monaco-editor .bracket-highlighting-4 { color: rgb(49, 147, 49); }

.monaco-editor .bracket-highlighting-5 { color: rgb(123, 56, 20); }

.monaco-editor .bracket-highlighting-6 { color: rgb(4, 49, 250); }

.monaco-editor .bracket-highlighting-7 { color: rgb(49, 147, 49); }

.monaco-editor .bracket-highlighting-8 { color: rgb(123, 56, 20); }

.monaco-editor .bracket-highlighting-9 { color: rgb(4, 49, 250); }

.monaco-editor .bracket-highlighting-10 { color: rgb(49, 147, 49); }

.monaco-editor .bracket-highlighting-11 { color: rgb(123, 56, 20); }

.monaco-editor .bracket-highlighting-12 { color: rgb(4, 49, 250); }

.monaco-editor .bracket-highlighting-13 { color: rgb(49, 147, 49); }

.monaco-editor .bracket-highlighting-14 { color: rgb(123, 56, 20); }

.monaco-editor .bracket-highlighting-15 { color: rgb(4, 49, 250); }

.monaco-editor .bracket-highlighting-16 { color: rgb(49, 147, 49); }

.monaco-editor .bracket-highlighting-17 { color: rgb(123, 56, 20); }

.monaco-editor .bracket-highlighting-18 { color: rgb(4, 49, 250); }

.monaco-editor .bracket-highlighting-19 { color: rgb(49, 147, 49); }

.monaco-editor .bracket-highlighting-20 { color: rgb(123, 56, 20); }

.monaco-editor .bracket-highlighting-21 { color: rgb(4, 49, 250); }

.monaco-editor .bracket-highlighting-22 { color: rgb(49, 147, 49); }

.monaco-editor .bracket-highlighting-23 { color: rgb(123, 56, 20); }

.monaco-editor .bracket-highlighting-24 { color: rgb(4, 49, 250); }

.monaco-editor .bracket-highlighting-25 { color: rgb(49, 147, 49); }

.monaco-editor .bracket-highlighting-26 { color: rgb(123, 56, 20); }

.monaco-editor .bracket-highlighting-27 { color: rgb(4, 49, 250); }

.monaco-editor .bracket-highlighting-28 { color: rgb(49, 147, 49); }

.monaco-editor .bracket-highlighting-29 { color: rgb(123, 56, 20); }

.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg=
%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%20=
3'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'=
%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201=
.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4=
%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%=
3C%2Fg%3E%3C%2Fsvg%3E") left bottom repeat-x; }

.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Cs=
vg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%=
203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'=
6'%3E%3Cg%20fill%3D'%23bf8803'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%2=
01.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205=
.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3=
E%3C%2Fg%3E%3C%2Fsvg%3E") left bottom repeat-x; }

.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%=
20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203=
'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%=
3E%3Cg%20fill%3D'%231a85ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.=
1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%=
2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3=
C%2Fg%3E%3C%2Fsvg%3E") left bottom repeat-x; }

.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%=
20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20w=
idth%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%=
20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%2=
0r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%=
3E%3C%2Fg%3E%3C%2Fsvg%3E") left bottom no-repeat; }

.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }

.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, =
0.15); }

.monaco-editor .diagonal-fill { background-image: linear-gradient(-45deg, r=
gba(34, 34, 34, 0.2) 12.5%, rgba(0, 0, 0, 0) 12.5%, rgba(0, 0, 0, 0) 50%, r=
gba(34, 34, 34, 0.2) 50%, rgba(34, 34, 34, 0.2) 62.5%, rgba(0, 0, 0, 0) 62.=
5%, rgba(0, 0, 0, 0) 100%); background-size: 8px 8px; }

.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }

.monaco-editor .currentFindMatch { background-color: rgb(168, 172, 148); }

.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }

.monaco-editor .find-widget { background-color: rgb(243, 243, 243); }

.monaco-editor .find-widget { box-shadow: rgba(0, 0, 0, 0.16) 0px 0px 8px 2=
px; }

.monaco-editor .find-widget { color: rgb(97, 97, 97); }

.monaco-editor .find-widget.no-results .matchesCount { color: rgb(161, 38, =
13); }

.monaco-editor .find-widget .monaco-sash { background-color: rgb(200, 200, =
200); }

.monaco-editor .find-widget .button:not(.disabled):hover, .monaco-editor .f=
ind-widget .codicon-find-selection:hover { background-color: rgba(184, 184,=
 184, 0.31) !important; }

.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-colo=
r: rgb(0, 144, 241); }

.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { bor=
der-top: 1px solid rgba(200, 200, 200, 0.5); }

.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(200, 200, 200,=
 0.5); }

.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(200, 200, 2=
00, 0.5); }

.monaco-editor { --vscode-foreground: #616161; --vscode-disabledForeground:=
 rgba(97, 97, 97, 0.5); --vscode-errorForeground: #a1260d; --vscode-descrip=
tionForeground: #717171; --vscode-icon-foreground: #424242; --vscode-focusB=
order: #0090f1; --vscode-textSeparator-foreground: rgba(0, 0, 0, 0.18); --v=
scode-textLink-foreground: #006ab1; --vscode-textLink-activeForeground: #00=
6ab1; --vscode-textPreformat-foreground: #a31515; --vscode-textBlockQuote-b=
ackground: rgba(127, 127, 127, 0.1); --vscode-textBlockQuote-border: rgba(0=
, 122, 204, 0.5); --vscode-textCodeBlock-background: rgba(220, 220, 220, 0.=
4); --vscode-widget-shadow: rgba(0, 0, 0, 0.16); --vscode-input-background:=
 #ffffff; --vscode-input-foreground: #616161; --vscode-inputOption-activeBo=
rder: #007acc; --vscode-inputOption-hoverBackground: rgba(184, 184, 184, 0.=
31); --vscode-inputOption-activeBackground: rgba(0, 144, 241, 0.2); --vscod=
e-inputOption-activeForeground: #000000; --vscode-input-placeholderForegrou=
nd: rgba(97, 97, 97, 0.5); --vscode-inputValidation-infoBackground: #d6ecf2=
; --vscode-inputValidation-infoBorder: #007acc; --vscode-inputValidation-wa=
rningBackground: #f6f5d2; --vscode-inputValidation-warningBorder: #b89500; =
--vscode-inputValidation-errorBackground: #f2dede; --vscode-inputValidation=
-errorBorder: #be1100; --vscode-dropdown-background: #ffffff; --vscode-drop=
down-foreground: #616161; --vscode-dropdown-border: #cecece; --vscode-butto=
n-foreground: #ffffff; --vscode-button-separator: rgba(255, 255, 255, 0.4);=
 --vscode-button-background: #007acc; --vscode-button-hoverBackground: #006=
2a3; --vscode-button-secondaryForeground: #ffffff; --vscode-button-secondar=
yBackground: #5f6a79; --vscode-button-secondaryHoverBackground: #4c5561; --=
vscode-badge-background: #c4c4c4; --vscode-badge-foreground: #333333; --vsc=
ode-scrollbar-shadow: #dddddd; --vscode-scrollbarSlider-background: rgba(10=
0, 100, 100, 0.4); --vscode-scrollbarSlider-hoverBackground: rgba(100, 100,=
 100, 0.7); --vscode-scrollbarSlider-activeBackground: rgba(0, 0, 0, 0.6); =
--vscode-progressBar-background: #0e70c0; --vscode-editorError-foreground: =
#e51400; --vscode-editorWarning-foreground: #bf8803; --vscode-editorInfo-fo=
reground: #1a85ff; --vscode-editorHint-foreground: #6c6c6c; --vscode-sash-h=
overBorder: #0090f1; --vscode-editor-background: #ffffff; --vscode-editor-f=
oreground: #000000; --vscode-editorStickyScroll-background: #ffffff; --vsco=
de-editorStickyScrollHover-background: #f0f0f0; --vscode-editorWidget-backg=
round: #f3f3f3; --vscode-editorWidget-foreground: #616161; --vscode-editorW=
idget-border: #c8c8c8; --vscode-quickInput-background: #f3f3f3; --vscode-qu=
ickInput-foreground: #616161; --vscode-quickInputTitle-background: rgba(0, =
0, 0, 0.06); --vscode-pickerGroup-foreground: #0066bf; --vscode-pickerGroup=
-border: #cccedb; --vscode-keybindingLabel-background: rgba(221, 221, 221, =
0.4); --vscode-keybindingLabel-foreground: #555555; --vscode-keybindingLabe=
l-border: rgba(204, 204, 204, 0.4); --vscode-keybindingLabel-bottomBorder: =
rgba(187, 187, 187, 0.4); --vscode-editor-selectionBackground: #add6ff; --v=
scode-editor-inactiveSelectionBackground: #e5ebf1; --vscode-editor-selectio=
nHighlightBackground: rgba(173, 214, 255, 0.3); --vscode-editor-findMatchBa=
ckground: #a8ac94; --vscode-editor-findMatchHighlightBackground: rgba(234, =
92, 0, 0.33); --vscode-editor-findRangeHighlightBackground: rgba(180, 180, =
180, 0.3); --vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22=
); --vscode-search-resultsInfoForeground: #616161; --vscode-editor-hoverHig=
hlightBackground: rgba(173, 214, 255, 0.15); --vscode-editorHoverWidget-bac=
kground: #f3f3f3; --vscode-editorHoverWidget-foreground: #616161; --vscode-=
editorHoverWidget-border: #c8c8c8; --vscode-editorHoverWidget-statusBarBack=
ground: #e7e7e7; --vscode-editorLink-activeForeground: #0000ff; --vscode-ed=
itorInlayHint-foreground: #616161; --vscode-editorInlayHint-background: rgb=
a(196, 196, 196, 0.3); --vscode-editorInlayHint-typeForeground: #616161; --=
vscode-editorInlayHint-typeBackground: rgba(196, 196, 196, 0.3); --vscode-e=
ditorInlayHint-parameterForeground: #616161; --vscode-editorInlayHint-param=
eterBackground: rgba(196, 196, 196, 0.3); --vscode-editorLightBulb-foregrou=
nd: #ddb100; --vscode-editorLightBulbAutoFix-foreground: #007acc; --vscode-=
diffEditor-insertedTextBackground: #aceebb; --vscode-diffEditor-removedText=
Background: #ffcecb; --vscode-diffEditor-insertedLineBackground: #dafbe1; -=
-vscode-diffEditor-removedLineBackground: #ffebe9; --vscode-diffEditor-diag=
onalFill: rgba(34, 34, 34, 0.2); --vscode-diffEditor-unchangedRegionBackgro=
und: #e4e4e4; --vscode-diffEditor-unchangedRegionForeground: #4d4c4c; --vsc=
ode-diffEditor-unchangedCodeBackground: rgba(184, 184, 184, 0.16); --vscode=
-list-focusOutline: #0090f1; --vscode-list-activeSelectionBackground: #d6eb=
ff; --vscode-list-activeSelectionForeground: #000000; --vscode-list-inactiv=
eSelectionBackground: #e4e6f1; --vscode-list-hoverBackground: #f0f0f0; --vs=
code-list-dropBackground: #d6ebff; --vscode-list-highlightForeground: #0066=
bf; --vscode-list-focusHighlightForeground: #0066bf; --vscode-list-invalidI=
temForeground: #b89500; --vscode-list-errorForeground: #b01011; --vscode-li=
st-warningForeground: #855f00; --vscode-listFilterWidget-background: #f3f3f=
3; --vscode-listFilterWidget-outline: rgba(0, 0, 0, 0); --vscode-listFilter=
Widget-noMatchesOutline: #be1100; --vscode-listFilterWidget-shadow: rgba(0,=
 0, 0, 0.16); --vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33); =
--vscode-tree-indentGuidesStroke: #a9a9a9; --vscode-tree-inactiveIndentGuid=
esStroke: rgba(169, 169, 169, 0.4); --vscode-tree-tableColumnsBorder: rgba(=
97, 97, 97, 0.13); --vscode-tree-tableOddRowsBackground: rgba(97, 97, 97, 0=
.04); --vscode-list-deemphasizedForeground: #8e8e90; --vscode-checkbox-back=
ground: #ffffff; --vscode-checkbox-selectBackground: #f3f3f3; --vscode-chec=
kbox-foreground: #616161; --vscode-checkbox-border: #cecece; --vscode-check=
box-selectBorder: #424242; --vscode-quickInputList-focusForeground: #000000=
; --vscode-quickInputList-focusBackground: #d6ebff; --vscode-menu-foregroun=
d: #616161; --vscode-menu-background: #ffffff; --vscode-menu-selectionForeg=
round: #000000; --vscode-menu-selectionBackground: #d6ebff; --vscode-menu-s=
eparatorBackground: #d4d4d4; --vscode-toolbar-hoverBackground: rgba(184, 18=
4, 184, 0.31); --vscode-toolbar-activeBackground: rgba(166, 166, 166, 0.31)=
; --vscode-editor-snippetTabstopHighlightBackground: rgba(10, 50, 100, 0.2)=
; --vscode-editor-snippetFinalTabstopHighlightBorder: rgba(10, 50, 100, 0.5=
); --vscode-breadcrumb-foreground: rgba(97, 97, 97, 0.8); --vscode-breadcru=
mb-background: #ffffff; --vscode-breadcrumb-focusForeground: #4e4e4e; --vsc=
ode-breadcrumb-activeSelectionForeground: #4e4e4e; --vscode-breadcrumbPicke=
r-background: #f3f3f3; --vscode-merge-currentHeaderBackground: rgba(64, 200=
, 174, 0.5); --vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.=
2); --vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5); --vsc=
ode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2); --vscode-merg=
e-commonHeaderBackground: rgba(96, 96, 96, 0.4); --vscode-merge-commonConte=
ntBackground: rgba(96, 96, 96, 0.16); --vscode-editorOverviewRuler-currentC=
ontentForeground: rgba(64, 200, 174, 0.5); --vscode-editorOverviewRuler-inc=
omingContentForeground: rgba(64, 166, 255, 0.5); --vscode-editorOverviewRul=
er-commonContentForeground: rgba(96, 96, 96, 0.4); --vscode-editorOverviewR=
uler-findMatchForeground: rgba(209, 134, 22, 0.49); --vscode-editorOverview=
Ruler-selectionHighlightForeground: rgba(0, 0, 0, 0); --vscode-minimap-find=
MatchHighlight: #d18616; --vscode-minimap-selectionOccurrenceHighlight: #c9=
c9c9; --vscode-minimap-selectionHighlight: #add6ff; --vscode-minimap-errorH=
ighlight: rgba(255, 18, 18, 0.7); --vscode-minimap-warningHighlight: #bf880=
3; --vscode-minimap-foregroundOpacity: #000000; --vscode-minimapSlider-back=
ground: rgba(100, 100, 100, 0.2); --vscode-minimapSlider-hoverBackground: r=
gba(100, 100, 100, 0.35); --vscode-minimapSlider-activeBackground: rgba(0, =
0, 0, 0.3); --vscode-problemsErrorIcon-foreground: #e51400; --vscode-proble=
msWarningIcon-foreground: #bf8803; --vscode-problemsInfoIcon-foreground: #1=
a85ff; --vscode-charts-foreground: #616161; --vscode-charts-lines: rgba(97,=
 97, 97, 0.5); --vscode-charts-red: #e51400; --vscode-charts-blue: #1a85ff;=
 --vscode-charts-yellow: #bf8803; --vscode-charts-orange: #d18616; --vscode=
-charts-green: #388a34; --vscode-charts-purple: #652d90; --vscode-symbolIco=
n-arrayForeground: #616161; --vscode-symbolIcon-booleanForeground: #616161;=
 --vscode-symbolIcon-classForeground: #d67e00; --vscode-symbolIcon-colorFor=
eground: #616161; --vscode-symbolIcon-constantForeground: #616161; --vscode=
-symbolIcon-constructorForeground: #652d90; --vscode-symbolIcon-enumeratorF=
oreground: #d67e00; --vscode-symbolIcon-enumeratorMemberForeground: #007acc=
; --vscode-symbolIcon-eventForeground: #d67e00; --vscode-symbolIcon-fieldFo=
reground: #007acc; --vscode-symbolIcon-fileForeground: #616161; --vscode-sy=
mbolIcon-folderForeground: #616161; --vscode-symbolIcon-functionForeground:=
 #652d90; --vscode-symbolIcon-interfaceForeground: #007acc; --vscode-symbol=
Icon-keyForeground: #616161; --vscode-symbolIcon-keywordForeground: #616161=
; --vscode-symbolIcon-methodForeground: #652d90; --vscode-symbolIcon-module=
Foreground: #616161; --vscode-symbolIcon-namespaceForeground: #616161; --vs=
code-symbolIcon-nullForeground: #616161; --vscode-symbolIcon-numberForegrou=
nd: #616161; --vscode-symbolIcon-objectForeground: #616161; --vscode-symbol=
Icon-operatorForeground: #616161; --vscode-symbolIcon-packageForeground: #6=
16161; --vscode-symbolIcon-propertyForeground: #616161; --vscode-symbolIcon=
-referenceForeground: #616161; --vscode-symbolIcon-snippetForeground: #6161=
61; --vscode-symbolIcon-stringForeground: #616161; --vscode-symbolIcon-stru=
ctForeground: #616161; --vscode-symbolIcon-textForeground: #616161; --vscod=
e-symbolIcon-typeParameterForeground: #616161; --vscode-symbolIcon-unitFore=
ground: #616161; --vscode-symbolIcon-variableForeground: #007acc; --vscode-=
editor-lineHighlightBorder: #eeeeee; --vscode-editor-rangeHighlightBackgrou=
nd: rgba(253, 255, 0, 0.2); --vscode-editor-symbolHighlightBackground: rgba=
(234, 92, 0, 0.33); --vscode-editorCursor-foreground: #000000; --vscode-edi=
torWhitespace-foreground: rgba(51, 51, 51, 0.2); --vscode-editorIndentGuide=
-background: #d3d3d3; --vscode-editorIndentGuide-activeBackground: #939393;=
 --vscode-editorLineNumber-foreground: #999999; --vscode-editorActiveLineNu=
mber-foreground: #0b216f; --vscode-editorLineNumber-activeForeground: #0b21=
6f; --vscode-editorRuler-foreground: #d3d3d3; --vscode-editorCodeLens-foreg=
round: #919191; --vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1=
); --vscode-editorBracketMatch-border: #b9b9b9; --vscode-editorOverviewRule=
r-border: rgba(127, 127, 127, 0.3); --vscode-editorGutter-background: #ffff=
ff; --vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.47); --vscode-e=
ditorGhostText-foreground: rgba(0, 0, 0, 0.47); --vscode-editorOverviewRule=
r-rangeHighlightForeground: rgba(0, 122, 204, 0.6); --vscode-editorOverview=
Ruler-errorForeground: rgba(255, 18, 18, 0.7); --vscode-editorOverviewRuler=
-warningForeground: #bf8803; --vscode-editorOverviewRuler-infoForeground: #=
1a85ff; --vscode-editorBracketHighlight-foreground1: #0431fa; --vscode-edit=
orBracketHighlight-foreground2: #319331; --vscode-editorBracketHighlight-fo=
reground3: #7b3814; --vscode-editorBracketHighlight-foreground4: rgba(0, 0,=
 0, 0); --vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0); --vs=
code-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0); --vscode-editorB=
racketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8); --vsc=
ode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0); --vscode-editorBr=
acketPairGuide-background2: rgba(0, 0, 0, 0); --vscode-editorBracketPairGui=
de-background3: rgba(0, 0, 0, 0); --vscode-editorBracketPairGuide-backgroun=
d4: rgba(0, 0, 0, 0); --vscode-editorBracketPairGuide-background5: rgba(0, =
0, 0, 0); --vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0); --=
vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0); --vscode=
-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0); --vscode-edito=
rBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0); --vscode-editorBrack=
etPairGuide-activeBackground4: rgba(0, 0, 0, 0); --vscode-editorBracketPair=
Guide-activeBackground5: rgba(0, 0, 0, 0); --vscode-editorBracketPairGuide-=
activeBackground6: rgba(0, 0, 0, 0); --vscode-editorUnicodeHighlight-border=
: #cea33d; --vscode-editorUnicodeHighlight-background: rgba(206, 163, 61, 0=
.08); --vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0; --vscod=
e-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3); --vscode-editor-wor=
dHighlightBackground: rgba(87, 87, 87, 0.25); --vscode-editor-wordHighlight=
StrongBackground: #d6ebff; --vscode-editor-wordHighlightTextBackground: rgb=
a(173, 214, 255, 0.45); --vscode-editorOverviewRuler-wordHighlightForegroun=
d: rgba(160, 160, 160, 0.8); --vscode-editorOverviewRuler-wordHighlightStro=
ngForeground: rgba(192, 160, 192, 0.8); --vscode-editorOverviewRuler-wordHi=
ghlightTextForeground: rgba(0, 0, 0, 0); --vscode-peekViewTitle-background:=
 #f3f3f3; --vscode-peekViewTitleLabel-foreground: #000000; --vscode-peekVie=
wTitleDescription-foreground: #616161; --vscode-peekView-border: #1a85ff; -=
-vscode-peekViewResult-background: #f3f3f3; --vscode-peekViewResult-lineFor=
eground: #646465; --vscode-peekViewResult-fileForeground: #1e1e1e; --vscode=
-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2); --vscode-peek=
ViewResult-selectionForeground: #6c6c6c; --vscode-peekViewEditor-background=
: #f2f8fc; --vscode-peekViewEditorGutter-background: #f2f8fc; --vscode-peek=
ViewEditorStickyScroll-background: #f2f8fc; --vscode-peekViewResult-matchHi=
ghlightBackground: rgba(234, 92, 0, 0.3); --vscode-peekViewEditor-matchHigh=
lightBackground: rgba(245, 216, 2, 0.87); --vscode-editorMarkerNavigationEr=
ror-background: #e51400; --vscode-editorMarkerNavigationError-headerBackgro=
und: rgba(229, 20, 0, 0.1); --vscode-editorMarkerNavigationWarning-backgrou=
nd: #bf8803; --vscode-editorMarkerNavigationWarning-headerBackground: rgba(=
191, 136, 3, 0.1); --vscode-editorMarkerNavigationInfo-background: #1a85ff;=
 --vscode-editorMarkerNavigationInfo-headerBackground: rgba(26, 133, 255, 0=
.1); --vscode-editorMarkerNavigation-background: #ffffff; --vscode-editorHo=
verWidget-highlightForeground: #0066bf; --vscode-editorSuggestWidget-backgr=
ound: #f3f3f3; --vscode-editorSuggestWidget-border: #c8c8c8; --vscode-edito=
rSuggestWidget-foreground: #000000; --vscode-editorSuggestWidget-selectedFo=
reground: #000000; --vscode-editorSuggestWidget-selectedBackground: #d6ebff=
; --vscode-editorSuggestWidget-highlightForeground: #0066bf; --vscode-edito=
rSuggestWidget-focusHighlightForeground: #0066bf; --vscode-editorSuggestWid=
getStatus-foreground: rgba(0, 0, 0, 0.5); --vscode-editor-foldBackground: r=
gba(173, 214, 255, 0.3); --vscode-editorGutter-foldingControlForeground: #4=
24242; }

.mtk1 { color: rgb(0, 0, 0); }

.mtk2 { color: rgb(255, 255, 255); }

.mtk3 { color: rgb(128, 128, 128); }

.mtk4 { color: rgb(255, 0, 0); }

.mtk5 { color: rgb(4, 81, 165); }

.mtk6 { color: rgb(0, 0, 255); }

.mtk7 { color: rgb(9, 134, 88); }

.mtk8 { color: rgb(0, 128, 0); }

.mtk9 { color: rgb(221, 0, 0); }

.mtk10 { color: rgb(129, 31, 63); }

.mtk11 { color: rgb(165, 52, 52); }

.mtk12 { color: rgb(17, 102, 68); }

.mtk13 { color: rgb(56, 56, 56); }

.mtk14 { color: rgb(37, 118, 147); }

.mtk15 { color: rgb(106, 82, 33); }

.mtk16 { color: rgb(0, 16, 128); }

.mtk17 { color: rgb(205, 49, 49); }

.mtk18 { color: rgb(134, 59, 0); }

.mtk19 { color: rgb(151, 35, 180); }

.mtk20 { color: rgb(175, 0, 219); }

.mtk21 { color: rgb(163, 21, 21); }

.mtk22 { color: rgb(128, 0, 0); }

.mtk23 { color: rgb(224, 0, 0); }

.mtk24 { color: rgb(48, 48, 192); }

.mtk25 { color: rgb(102, 102, 102); }

.mtk26 { color: rgb(119, 136, 153); }

.mtk27 { color: rgb(199, 0, 199); }

.mtk28 { color: rgb(79, 118, 172); }

.mtk29 { color: rgb(0, 128, 128); }

.mtk30 { color: rgb(0, 17, 136); }

.mtk31 { color: rgb(72, 100, 170); }

.mtki { font-style: italic; }

.mtkb { font-weight: bold; }

.mtku { text-decoration: underline; text-underline-position: under; }

.mtks { text-decoration: line-through; }

.mtks.mtku { text-decoration: underline line-through; text-underline-positi=
on: under; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: cid:css-26d7c64d-9945-4e0d-9372-dd06c853e612@mhtml.blink

@charset "utf-8";

.MathJax_Display { text-align: center; margin: 0px; position: relative; tex=
t-indent: 0px; max-width: none; max-height: none; min-width: 0px; min-heigh=
t: 0px; width: 100%; display: block !important; }

.MathJax .merror { background-color: rgb(255, 255, 136); color: rgb(204, 0,=
 0); border: 1px solid rgb(204, 0, 0); padding: 1px 3px; font-style: normal=
; font-size: 90%; }

.MathJax .MJX-monospace { font-family: monospace; }

.MathJax .MJX-sans-serif { font-family: sans-serif; }

#MathJax_Tooltip { background-color: infobackground; color: infotext; borde=
r: 1px solid black; box-shadow: rgb(170, 170, 170) 2px 2px 5px; padding: 3p=
x 4px; z-index: 401; position: absolute; left: 0px; top: 0px; width: auto; =
height: auto; display: none; }

.MathJax { display: inline; font-style: normal; font-weight: normal; line-h=
eight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0px; t=
ext-align: left; text-transform: none; letter-spacing: normal; word-spacing=
: normal; overflow-wrap: normal; white-space: nowrap; float: none; directio=
n: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px;=
 border: 0px; padding: 0px; margin: 0px; }

.MathJax:focus, body :focus .MathJax { display: inline-table; }

.MathJax.MathJax_FullWidth { text-align: center; display: table-cell !impor=
tant; width: 10000em !important; }

.MathJax img, .MathJax nobr, .MathJax a { border: 0px; padding: 0px; margin=
: 0px; max-width: none; max-height: none; min-width: 0px; min-height: 0px; =
vertical-align: 0px; line-height: normal; text-decoration: none; }

img.MathJax_strut { border: 0px !important; padding: 0px !important; margin=
: 0px !important; vertical-align: 0px !important; }

.MathJax span { display: inline; position: static; border: 0px; padding: 0p=
x; margin: 0px; vertical-align: 0px; line-height: normal; text-decoration: =
none; box-sizing: content-box; }

.MathJax nobr { white-space: nowrap !important; }

.MathJax img { display: inline !important; float: none !important; }

.MathJax * { transition: none; }

.MathJax_Processing { visibility: hidden; position: fixed; width: 0px; heig=
ht: 0px; overflow: hidden; }

.MathJax_Processed { display: none !important; }

.MathJax_test { font-style: normal; font-weight: normal; font-size: 100%; f=
ont-size-adjust: none; text-indent: 0px; text-transform: none; letter-spaci=
ng: normal; word-spacing: normal; overflow: hidden; height: 1px; }

.MathJax_test.mjx-test-display { display: table !important; }

.MathJax_test.mjx-test-inline { display: inline !important; margin-right: -=
1px; }

.MathJax_test.mjx-test-default { display: block !important; clear: both; }

.MathJax_ex_box { position: absolute; overflow: hidden; min-height: 0px; ma=
x-height: none; padding: 0px; border: 0px; margin: 0px; width: 1px; height:=
 60ex; display: inline-block !important; }

.MathJax_em_box { position: absolute; overflow: hidden; min-height: 0px; ma=
x-height: none; padding: 0px; border: 0px; margin: 0px; width: 1px; height:=
 60em; display: inline-block !important; }

.mjx-test-inline .MathJax_left_box { display: inline-block; width: 0px; flo=
at: left; }

.mjx-test-inline .MathJax_right_box { display: inline-block; width: 0px; fl=
oat: right; }

.mjx-test-display .MathJax_right_box { min-width: 0px; max-width: none; pad=
ding: 0px; border: 0px; margin: 0px; display: table-cell !important; width:=
 10000em !important; }

.MathJax .MathJax_HitBox { cursor: text; background: white; opacity: 0; }

.MathJax .MathJax_HitBox * { filter: none; opacity: 1; background: transpar=
ent; }

#MathJax_Tooltip * { filter: none; opacity: 1; background: transparent; }

@font-face { font-family: MathJax_Main; src: url("https://colab.research.go=
ogle.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=
=3D2.7.5") format("woff"), url("https://colab.research.google.com/static/ma=
thjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=3D2.7.5") format("o=
pentype"); }

@font-face { font-family: MathJax_Main-bold; src: url("https://colab.resear=
ch.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff=
?V=3D2.7.5") format("woff"), url("https://colab.research.google.com/static/=
mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=3D2.7.5") format("op=
entype"); }

@font-face { font-family: MathJax_Main-italic; src: url("https://colab.rese=
arch.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.=
woff?V=3D2.7.5") format("woff"), url("https://colab.research.google.com/sta=
tic/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=3D2.7.5") form=
at("opentype"); }

@font-face { font-family: MathJax_Math-italic; src: url("https://colab.rese=
arch.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.=
woff?V=3D2.7.5") format("woff"), url("https://colab.research.google.com/sta=
tic/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=3D2.7.5") form=
at("opentype"); }

@font-face { font-family: MathJax_Caligraphic; src: url("https://colab.rese=
arch.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-=
Regular.woff?V=3D2.7.5") format("woff"), url("https://colab.research.google=
.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?=
V=3D2.7.5") format("opentype"); }

@font-face { font-family: MathJax_Size1; src: url("https://colab.research.g=
oogle.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff=
?V=3D2.7.5") format("woff"), url("https://colab.research.google.com/static/=
mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=3D2.7.5") format=
("opentype"); }

@font-face { font-family: MathJax_Size2; src: url("https://colab.research.g=
oogle.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff=
?V=3D2.7.5") format("woff"), url("https://colab.research.google.com/static/=
mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=3D2.7.5") format=
("opentype"); }

@font-face { font-family: MathJax_Size3; src: url("https://colab.research.g=
oogle.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff=
?V=3D2.7.5") format("woff"), url("https://colab.research.google.com/static/=
mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=3D2.7.5") format=
("opentype"); }

@font-face { font-family: MathJax_Size4; src: url("https://colab.research.g=
oogle.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff=
?V=3D2.7.5") format("woff"), url("https://colab.research.google.com/static/=
mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=3D2.7.5") format=
("opentype"); }

.MathJax .noError { font-size: 90%; text-align: left; color: black; padding=
: 1px 3px; border: 1px solid; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: cid:css-823da69d-08ed-4725-ac61-1a0a93ff7b1e@mhtml.blink

@charset "utf-8";

.MJXp-script { font-size: 0.8em; }

.MJXp-right { transform-origin: right center; }

.MJXp-bold { font-weight: bold; }

.MJXp-italic { font-style: italic; }

.MJXp-scr { font-family: MathJax_Script, "Times New Roman", Times, STIXGene=
ral, serif; }

.MJXp-frak { font-family: MathJax_Fraktur, "Times New Roman", Times, STIXGe=
neral, serif; }

.MJXp-sf { font-family: MathJax_SansSerif, "Times New Roman", Times, STIXGe=
neral, serif; }

.MJXp-cal { font-family: MathJax_Caligraphic, "Times New Roman", Times, STI=
XGeneral, serif; }

.MJXp-mono { font-family: MathJax_Typewriter, "Times New Roman", Times, STI=
XGeneral, serif; }

.MJXp-largeop { font-size: 150%; }

.MJXp-largeop.MJXp-int { vertical-align: -0.2em; }

.MJXp-math { display: inline-block; line-height: 1.2; text-indent: 0px; fon=
t-family: "Times New Roman", Times, STIXGeneral, serif; white-space: nowrap=
; border-collapse: collapse; }

.MJXp-display { display: block; text-align: center; margin: 1em 0px; }

.MJXp-math span { display: inline-block; }

.MJXp-box { display: block !important; text-align: center; }

.MJXp-box::after { content: " "; }

.MJXp-rule { display: block !important; margin-top: 0.1em; }

.MJXp-char { display: block !important; }

.MJXp-mo { margin: 0px 0.15em; }

.MJXp-mfrac { margin: 0px 0.125em; vertical-align: 0.25em; }

.MJXp-denom { display: inline-table !important; width: 100%; }

.MJXp-denom > * { display: table-row !important; }

.MJXp-surd { vertical-align: top; }

.MJXp-surd > * { display: block !important; }

.MJXp-script-box > * { display: table !important; height: 50%; }

.MJXp-script-box > * > * { display: table-cell !important; vertical-align: =
top; }

.MJXp-script-box > :last-child > * { vertical-align: bottom; }

.MJXp-script-box > * > * > * { display: block !important; }

.MJXp-mphantom { visibility: hidden; }

.MJXp-munderover, .MJXp-munder { display: inline-table !important; }

.MJXp-over { display: inline-block !important; text-align: center; }

.MJXp-over > * { display: block !important; }

.MJXp-munderover > *, .MJXp-munder > * { display: table-row !important; }

.MJXp-mtable { vertical-align: 0.25em; margin: 0px 0.125em; }

.MJXp-mtable > * { display: inline-table !important; vertical-align: middle=
; }

.MJXp-mtr { display: table-row !important; }

.MJXp-mtd { text-align: center; padding: 0.5em 0px 0px 0.5em; display: tabl=
e-cell !important; }

.MJXp-mtr > .MJXp-mtd:first-child { padding-left: 0px; }

.MJXp-mtr:first-child > .MJXp-mtd { padding-top: 0px; }

.MJXp-mlabeledtr { display: table-row !important; }

.MJXp-mlabeledtr > .MJXp-mtd:first-child { padding-left: 0px; }

.MJXp-mlabeledtr:first-child > .MJXp-mtd { padding-top: 0px; }

.MJXp-merror { background-color: rgb(255, 255, 136); color: rgb(204, 0, 0);=
 border: 1px solid rgb(204, 0, 0); padding: 1px 3px; font-style: normal; fo=
nt-size: 90%; }

.MJXp-scale0 { transform: scaleX(0); }

.MJXp-scale1 { transform: scaleX(0.1); }

.MJXp-scale2 { transform: scaleX(0.2); }

.MJXp-scale3 { transform: scaleX(0.3); }

.MJXp-scale4 { transform: scaleX(0.4); }

.MJXp-scale5 { transform: scaleX(0.5); }

.MJXp-scale6 { transform: scaleX(0.6); }

.MJXp-scale7 { transform: scaleX(0.7); }

.MJXp-scale8 { transform: scaleX(0.8); }

.MJXp-scale9 { transform: scaleX(0.9); }

.MathJax_PHTML .noError { font-size: 90%; text-align: left; color: black; p=
adding: 1px 3px; border: 1px solid; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: cid:css-7f7fccf6-25fb-4460-bb6b-4a781765cc8b@mhtml.blink

@charset "utf-8";

.MathJax_Preview { color: rgb(136, 136, 136); }

#MathJax_Message { position: fixed; left: 1em; bottom: 1.5em; background-co=
lor: rgb(230, 230, 230); border: 1px solid rgb(149, 149, 149); margin: 0px;=
 padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto;=
 white-space: nowrap; }

#MathJax_MSIE_Frame { position: absolute; top: 0px; left: 0px; width: 0px; =
z-index: 101; border: 0px; margin: 0px; padding: 0px; }

.MathJax_Error { color: rgb(204, 0, 0); font-style: italic; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: cid:css-77556185-66c9-4dd3-b4b8-1957f3a4d71e@mhtml.blink

@charset "utf-8";

#MathJax_Zoom { position: absolute; background-color: rgb(240, 240, 240); o=
verflow: auto; display: block; z-index: 301; padding: 0.5em; border: 1px so=
lid black; margin: 0px; font-weight: normal; font-style: normal; text-align=
: left; text-indent: 0px; text-transform: none; line-height: normal; letter=
-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space:=
 nowrap; float: none; box-sizing: content-box; box-shadow: rgb(170, 170, 17=
0) 5px 5px 15px; }

#MathJax_ZoomOverlay { position: absolute; left: 0px; top: 0px; z-index: 30=
0; display: inline-block; width: 100%; height: 100%; border: 0px; padding: =
0px; margin: 0px; background-color: white; opacity: 0; }

#MathJax_ZoomFrame { position: relative; display: inline-block; height: 0px=
; width: 0px; }

#MathJax_ZoomEventTrap { position: absolute; left: 0px; top: 0px; z-index: =
302; display: inline-block; border: 0px; padding: 0px; margin: 0px; backgro=
und-color: white; opacity: 0; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: cid:css-9db2c5e4-cdee-48b4-8e79-cb55979ed7cd@mhtml.blink

@charset "utf-8";

.MJX_Assistive_MathML { top: 0px; left: 0px; clip: rect(1px, 1px, 1px, 1px)=
; user-select: none; position: absolute !important; padding: 1px 0px 0px !i=
mportant; border: 0px !important; height: 1px !important; width: 1px !impor=
tant; overflow: hidden !important; display: block !important; }

.MJX_Assistive_MathML.MJX_Assistive_MathML_Block { width: 100% !important; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: cid:css-5ef9603c-81a2-456a-a733-daec7b5f7a34@mhtml.blink

@charset "utf-8";

#MathJax_About { position: fixed; left: 50%; width: auto; text-align: cente=
r; border: 3px outset; padding: 1em 2em; background-color: rgb(221, 221, 22=
1); color: black; cursor: default; font-family: message-box; font-size: 120=
%; font-style: normal; text-indent: 0px; text-transform: none; line-height:=
 normal; letter-spacing: normal; word-spacing: normal; overflow-wrap: norma=
l; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; box=
-shadow: rgb(128, 128, 128) 0px 10px 20px; }

#MathJax_About.MathJax_MousePost { outline: none; }

.MathJax_Menu { position: absolute; background-color: white; color: black; =
width: auto; padding: 2px; border: 1px solid rgb(204, 204, 204); margin: 0p=
x; cursor: default; font-style: ; font-variant: normal; font-weight: ; font=
-stretch: ; font-size: ; font-family: ; font-optical-sizing: ; font-size-ad=
just: ; font-kerning: ; font-feature-settings: ; font-variation-settings: ;=
 font-language-override: ; text-align: left; text-indent: 0px; text-transfo=
rm: none; line-height: normal; letter-spacing: normal; word-spacing: normal=
; overflow-wrap: normal; white-space: nowrap; float: none; z-index: 201; bo=
x-shadow: rgb(128, 128, 128) 0px 10px 20px; }

.MathJax_MenuItem { padding: 2px 2em; background: transparent; }

.MathJax_MenuArrow { position: absolute; right: 0.5em; padding-top: 0.25em;=
 color: rgb(102, 102, 102); font-size: 0.75em; }

.MathJax_MenuActive .MathJax_MenuArrow { color: white; }

.MathJax_MenuArrow.RTL { left: 0.5em; right: auto; }

.MathJax_MenuCheck { position: absolute; left: 0.7em; }

.MathJax_MenuCheck.RTL { right: 0.7em; left: auto; }

.MathJax_MenuRadioCheck { position: absolute; left: 1em; }

.MathJax_MenuRadioCheck.RTL { right: 1em; left: auto; }

.MathJax_MenuLabel { padding: 2px 2em 4px 1.33em; font-style: italic; }

.MathJax_MenuRule { border-top: 1px solid rgb(204, 204, 204); margin: 4px 1=
px 0px; }

.MathJax_MenuDisabled { color: graytext; }

.MathJax_MenuActive { background-color: highlight; color: highlighttext; }

.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus { background-color: r=
gb(232, 232, 232); }

.MathJax_ContextMenu:focus { outline: none; }

.MathJax_ContextMenu .MathJax_MenuItem:focus { outline: none; }

#MathJax_AboutClose { top: 0.2em; right: 0.2em; }

.MathJax_Menu .MathJax_MenuClose { top: -10px; left: -10px; }

.MathJax_MenuClose { position: absolute; cursor: pointer; display: inline-b=
lock; border: 2px solid rgb(170, 170, 170); border-radius: 18px; font-famil=
y: "Courier New", Courier; font-size: 24px; color: rgb(240, 240, 240); }

.MathJax_MenuClose span { display: block; background-color: rgb(170, 170, 1=
70); border: 1.5px solid; border-radius: 18px; line-height: 0; padding: 8px=
 0px 6px; }

.MathJax_MenuClose:hover { color: white !important; border: 2px solid rgb(2=
04, 204, 204) !important; }

.MathJax_MenuClose:hover span { background-color: rgb(204, 204, 204) !impor=
tant; }

.MathJax_MenuClose:hover:focus { outline: none; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: cid:css-4450dfb2-a027-4f3b-b8e8-01a5af03fae0@mhtml.blink

@charset "utf-8";

.MathJax_Hover_Frame { border-radius: 0.25em; box-shadow: rgb(136, 51, 170)=
 0px 0px 15px; display: inline-block; position: absolute; border: 1px solid=
 rgb(170, 102, 221) !important; }

.MathJax_Menu_Button .MathJax_Hover_Arrow { position: absolute; cursor: poi=
nter; display: inline-block; border: 2px solid rgb(170, 170, 170); border-r=
adius: 4px; font-family: "Courier New", Courier; font-size: 9px; color: rgb=
(240, 240, 240); }

.MathJax_Menu_Button .MathJax_Hover_Arrow span { display: block; background=
-color: rgb(170, 170, 170); border: 1px solid; border-radius: 3px; line-hei=
ght: 0; padding: 4px; }

.MathJax_Hover_Arrow:hover { color: white !important; border: 2px solid rgb=
(204, 204, 204) !important; }

.MathJax_Hover_Arrow:hover span { background-color: rgb(204, 204, 204) !imp=
ortant; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: cid:css-fe8af014-6e3f-4905-acb4-c630493d54b0@mhtml.blink

@charset "utf-8";

[inert] { pointer-events: none; cursor: default; }

[inert], [inert] * { user-select: none; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: cid:css-dedaa6b4-544a-46cc-8eb3-4c7999afa88b@mhtml.blink

@charset "utf-8";

.gb_yb { font: 13px / 27px Roboto, Arial, sans-serif; z-index: 986; }

.gb_R { display: none; }

.gb_Q { background-size: 32px 32px; border: 0px; border-radius: 50%; displa=
y: block; margin: 0px; position: relative; height: 32px; width: 32px; z-ind=
ex: 0; }

.gb_kb { background-color: rgb(232, 240, 254); border: 1px solid rgba(32, 3=
3, 36, 0.08); position: relative; }

.gb_kb.gb_Q { height: 30px; width: 30px; }

.gb_kb.gb_Q:hover, .gb_kb.gb_Q:active { box-shadow: none; }

.gb_lb { background: rgb(255, 255, 255); border: none; border-radius: 50%; =
bottom: 2px; box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64=
, 67, 0.15) 0px 1px 3px 1px; height: 14px; margin: 2px; position: absolute;=
 right: 0px; width: 14px; line-height: normal; z-index: 1; }

.gb_mb { color: rgb(31, 113, 231); font: 400 22px / 32px "Google Sans", Rob=
oto, Helvetica, Arial, sans-serif; text-align: center; text-transform: uppe=
rcase; }

@media (-webkit-min-device-pixel-ratio: 1.25), (min-device-pixel-ratio:1.25=
), (min-resolution: 1.25dppx) {
  .gb_Q::before, .gb_nb::before { display: inline-block; transform: scale(0=
.5); transform-origin: left 0px; }
  .gb_4 .gb_nb::before { }
}

.gb_Q:hover, .gb_Q:focus { box-shadow: rgba(0, 0, 0, 0.15) 0px 1px 0px; }

.gb_Q:active { box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 0px inset; }

.gb_Q:active::after { background: rgba(0, 0, 0, 0.1); border-radius: 50%; c=
ontent: ""; display: block; height: 100%; }

.gb_ob { cursor: pointer; line-height: 40px; min-width: 30px; opacity: 0.75=
; overflow: hidden; vertical-align: middle; text-overflow: ellipsis; }

.gb_B.gb_ob { width: auto; }

.gb_ob:hover, .gb_ob:focus { opacity: 0.85; }

.gb_pb .gb_ob, .gb_pb .gb_qb { line-height: 26px; }

#gb#gb.gb_pb a.gb_ob, .gb_pb .gb_qb { font-size: 11px; height: auto; }

.gb_rb { border-top: 4px solid rgb(0, 0, 0); border-left: 4px dashed transp=
arent; border-right: 4px dashed transparent; display: inline-block; margin-=
left: 6px; opacity: 0.75; vertical-align: middle; }

.gb_0a:hover .gb_rb { opacity: 0.85; }

.gb_Xa > .gb_z { padding: 3px 3px 3px 4px; }

.gb_sb.gb_jb { color: rgb(255, 255, 255); }

.gb_2 .gb_ob, .gb_2 .gb_rb { opacity: 1; }

#gb#gb.gb_2.gb_2 a.gb_ob, #gb#gb .gb_2.gb_2 a.gb_ob { color: rgb(255, 255, =
255); }

.gb_2.gb_2 .gb_rb { border-top-color: rgb(255, 255, 255); opacity: 1; }

.gb_la .gb_Q:hover, .gb_2 .gb_Q:hover, .gb_la .gb_Q:focus, .gb_2 .gb_Q:focu=
s { box-shadow: rgba(0, 0, 0, 0.15) 0px 1px 0px, rgba(0, 0, 0, 0.2) 0px 1px=
 2px; }

.gb_tb .gb_z, .gb_ub .gb_z { position: absolute; right: 1px; }

.gb_z.gb_1, .gb_vb.gb_1, .gb_0a.gb_1 { -webkit-box-flex: 0; flex: 0 1 auto;=
 }

.gb_wb.gb_xb .gb_ob { width: 30px !important; }

.gb_P { height: 40px; position: absolute; right: -5px; top: -5px; width: 40=
px; }

.gb_yb .gb_P, .gb_zb .gb_P { right: 0px; top: 0px; }

.gb_Ha a.gb_Va { border-radius: 100px; background: var(--gm3-sys-color-prim=
ary,#0b57d0); box-sizing: border-box; color: var(--gm3-sys-color-on-primary=
,#fff); display: inline-block; font-size: 14px; font-weight: 500; min-heigh=
t: 40px; outline: none; padding: 10px 24px; text-align: center; text-decora=
tion: none; white-space: normal; line-height: 18px; position: relative; }

.gb_Ha a.gb_Wa { border-radius: 100px; border-width: 1px; border-style: sol=
id; border-image: initial; border-color: var(--gm3-sys-color-outline,#74777=
5); background: none; box-sizing: border-box; color: var(--gm3-sys-color-pr=
imary,#0b57d0); display: inline-block; font-size: 14px; font-weight: 500; m=
in-height: 40px; outline: none; padding: 10px 24px; text-align: center; tex=
t-decoration: none; white-space: normal; line-height: 18px; position: relat=
ive; }

.gb_1a.gb_H a.gb_Va, .gb_2a.gb_H a.gb_Va, .gb_3a.gb_H a.gb_Va { background:=
 var(--gm3-sys-color-secondary-fixed,#c2e7ff); color: var(--gm3-sys-color-o=
n-secondary-fixed,#001d35); }

.gb_Ha.gb_H a.gb_Wa { color: var(--gm3-sys-color-primary,#a8c7fa); }

.gb_Ha a.gb_Od { padding: 10px 12px; margin: 12px 16px 12px 10px; min-width=
: 85px; }

@media (max-width: 640px) {
  .gb_Ha a.gb_Od { min-width: 75px; }
}

.gb_Ha, .gb_Dd { font-family: "Google Sans Text", Roboto, Helvetica, Arial,=
 sans-serif; font-style: normal; }

.gb_Ha.gb_1a { color: var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f=
1f1f)); }

.gb_Ha.gb_1a.gb_Pd { background: var(--og-bar-background,var(--gm3-sys-colo=
r-background,#fff)); }

.gb_Ha.gb_1a .gb_pd.gb_qd, .gb_Ha.gb_1a a.gb_Z, .gb_Ha.gb_1a span.gb_Z { co=
lor: var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f)); }

.gb_Ha.gb_1a .gb_rd .gb_Qd, .gb_Ha.gb_1a .gb_id .gb_Qd { color: var(--og-lo=
go-color,var(--gm3-sys-color-on-surface,#1f1f1f)); }

.gb_Ha.gb_1a svg { color: var(--og-svg-color,var(--gm3-sys-color-on-surface=
-variant,#444746)); }

@media (forced-colors: active) and (prefers-color-scheme: dark) {
  .gb_Ha svg, .gb_Ha.gb_1a svg, .gb_Ha.gb_H svg { color: white; }
}

.gb_Ha.gb_H.gb_1a { color: var(--og-bar-color,var(--gm3-sys-color-on-surfac=
e,#e3e3e3)); }

.gb_Ha.gb_H.gb_1a.gb_Pd { background: transparent; }

.gb_Ha.gb_H.gb_1a .gb_pd.gb_qd, .gb_Ha.gb_H.gb_1a a.gb_Z, .gb_Ha.gb_H.gb_1a=
 span.gb_Z { color: var(--og-link-color,var(--gm3-sys-color-on-surface,#e3e=
3e3)); }

.gb_Ha.gb_H.gb_1a .gb_rd .gb_Qd, .gb_Ha.gb_H.gb_1a .gb_id .gb_Qd { color: v=
ar(--og-logo-color,var(--gm3-sys-color-on-surface,#e3e3e3)); }

.gb_Ha.gb_H.gb_1a svg { color: var(--og-svg-color,var(--gm3-sys-color-on-su=
rface-variant,#c4c7c5)); }

.gb_Ha.gb_H.gb_1a.gb_Pd { background: var(--og-bar-background,var(--gm3-sys=
-color-background,#131314)); }

.gb_Ha.gb_2a { color: var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f=
1f1f)); }

.gb_Ha.gb_2a.gb_Pd { background: var(--og-bar-background,var(--gm3-sys-colo=
r-surface-container-high,#e9eef6)); }

.gb_Ha.gb_2a .gb_pd.gb_qd, .gb_Ha.gb_2a a.gb_Z, .gb_Ha.gb_2a span.gb_Z { co=
lor: var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f)); }

.gb_Ha.gb_2a .gb_rd .gb_Qd, .gb_Ha.gb_2a .gb_id .gb_Qd { color: var(--og-lo=
go-color,var(--gm3-sys-color-on-surface,#1f1f1f)); }

.gb_Ha.gb_2a svg { color: var(--og-svg-color,var(--gm3-sys-color-on-surface=
-variant,#444746)); }

.gb_Ha.gb_H.gb_2a { color: var(--og-bar-color,var(--gm3-sys-color-on-surfac=
e,#e3e3e3)); }

.gb_Ha.gb_H.gb_2a.gb_Pd { background: var(--og-bar-background,var(--gm3-sys=
-color-surface-container-high,#282a2c)); }

.gb_Ha.gb_H.gb_2a .gb_pd.gb_qd, .gb_Ha.gb_H.gb_2a a.gb_Z, .gb_Ha.gb_H.gb_2a=
 span.gb_Z { color: var(--og-link-color,var(--gm3-sys-color-on-surface,#e3e=
3e3)); }

.gb_Ha.gb_H.gb_2a .gb_rd .gb_Qd, .gb_Ha.gb_H.gb_2a .gb_id .gb_Qd { color: v=
ar(--og-logo-color,var(--gm3-sys-color-on-surface,#e3e3e3)); }

.gb_Ha.gb_H.gb_2a svg { color: var(--og-svg-color,var(--gm3-sys-color-on-su=
rface-variant,#c4c7c5)); }

.gb_Ha.gb_3a { color: var(--og-bar-color,var(--gm3-sys-color-on-surface,#1f=
1f1f)); }

.gb_Ha.gb_3a.gb_Pd { background: transparent; }

.gb_Ha.gb_3a .gb_pd.gb_qd, .gb_Ha.gb_3a a.gb_Z, .gb_Ha.gb_3a span.gb_Z { co=
lor: var(--og-link-color,var(--gm3-sys-color-on-surface,#1f1f1f)); }

.gb_Ha.gb_3a .gb_rd .gb_Qd, .gb_Ha.gb_3a .gb_id .gb_Qd { color: var(--og-lo=
go-color,var(--gm3-sys-color-on-surface,#1f1f1f)); }

.gb_Ha.gb_3a svg { color: var(--og-svg-color,var(--gm3-sys-color-on-surface=
-variant,#444746)); }

.gb_Ha.gb_3a.gb_H.gb_Pd { background: transparent; }

.gb_Ha.gb_3a.gb_H .gb_pd.gb_qd, .gb_Ha.gb_3a.gb_H a.gb_Z, .gb_Ha.gb_3a.gb_H=
 span.gb_Z { color: var(--og-theme-color,white); }

.gb_Ha.gb_3a.gb_H .gb_rd .gb_Qd, .gb_Ha.gb_3a.gb_H .gb_id .gb_Qd { color: v=
ar(--og-theme-color,white); }

.gb_Ha.gb_3a.gb_H svg { color: var(--og-theme-color,white); }

.gb_Ha a.gb_Z, .gb_Ha span.gb_Z { text-decoration: none; }

.gb_pd { font-family: "Google Sans", Roboto, Helvetica, Arial, sans-serif; =
font-size: 20px; font-weight: 400; letter-spacing: 0.25px; line-height: 48p=
x; margin-bottom: 2px; opacity: 1; overflow: hidden; padding-left: 16px; po=
sition: relative; text-overflow: ellipsis; vertical-align: middle; top: 2px=
; white-space: nowrap; -webkit-box-flex: 1; flex: 1 1 auto; }

.gb_ud { display: none; }

.gb_Ha.gb_9a .gb_pd { margin-bottom: 0px; }

.gb_rd.gb_sd .gb_pd { padding-left: 4px; }

.gb_Ha.gb_9a .gb_td { position: relative; top: -2px; }

.gb_Ha { min-width: 160px; position: relative; }

.gb_Ha.gb_ad { min-width: 120px; }

.gb_Ha.gb_Rd .gb_Sd { display: none; }

.gb_Ha.gb_Rd .gb_Kd { height: 56px; }

header.gb_Ha { display: block; }

.gb_Ha svg { fill: currentcolor; }

.gb_Td { position: fixed; top: 0px; width: 100%; }

.gb_Ud { box-shadow: rgba(0, 0, 0, 0.14) 0px 4px 5px 0px, rgba(0, 0, 0, 0.1=
2) 0px 1px 10px 0px, rgba(0, 0, 0, 0.2) 0px 2px 4px -1px; }

.gb_Vd { height: 64px; }

.gb_Kd { box-sizing: border-box; position: relative; width: 100%; display: =
flex; -webkit-box-pack: justify; justify-content: space-between; min-width:=
 min-content; }

.gb_Ha:not(.gb_9a) .gb_Kd { padding: 8px; }

.gb_Ha:not(.gb_9a) .gb_Kd a.gb_Wd { margin: 12px 8px 12px 10px; }

.gb_Ha.gb_Xd .gb_Kd { -webkit-box-flex: 1; flex: 1 0 auto; }

.gb_Ha .gb_Kd.gb_Ld.gb_Zd { min-width: 0px; }

.gb_Ha.gb_9a .gb_Kd { padding: 4px 4px 4px 8px; min-width: 0px; }

.gb_Ha.gb_9a .gb_Kd a.gb_Wd { margin: 12px 8px 12px 10px; }

.gb_Sd { height: 48px; vertical-align: middle; white-space: nowrap; -webkit=
-box-align: center; align-items: center; display: flex; user-select: none; =
}

.gb_0d > .gb_Sd { display: table-cell; width: 100%; }

.gb_rd { padding-right: 25px; box-sizing: border-box; -webkit-box-flex: 1; =
flex: 1 0 auto; }

.gb_Ha.gb_9a .gb_rd { padding-right: 14px; }

.gb_1d { -webkit-box-flex: 1; flex: 1 1 100%; }

.gb_1d > :only-child { display: inline-block; }

.gb_2d.gb_jd { padding-left: 4px; }

.gb_2d.gb_3d, .gb_Ha.gb_Xd .gb_2d, .gb_Ha.gb_9a:not(.gb_Dd) .gb_2d { paddin=
g-left: 0px; }

.gb_Ha.gb_9a .gb_2d.gb_3d { padding-right: 0px; }

.gb_Ha.gb_9a .gb_2d.gb_3d .gb_Xa { margin-left: 10px; }

.gb_jd { display: inline; }

.gb_Ha.gb_dd .gb_2d.gb_4d, .gb_Ha.gb_Dd .gb_2d.gb_4d { padding-left: 2px; }

.gb_pd { display: inline-block; }

.gb_2d { box-sizing: border-box; height: 48px; padding: 0px 4px 0px 5px; -w=
ebkit-box-flex: 0; flex: 0 0 auto; -webkit-box-pack: end; justify-content: =
flex-end; }

.gb_Dd { height: 48px; }

.gb_Ha.gb_Dd { min-width: auto; }

.gb_Dd .gb_2d { float: right; padding-left: var(--og-bar-parts-side-padding=
,32px); }

.gb_Dd .gb_2d.gb_5d { padding-left: 0px; }

.gb_6d { font-size: 14px; max-width: 200px; overflow: hidden; padding: 0px =
12px; text-overflow: ellipsis; white-space: nowrap; user-select: text; }

.gb_a a, .gb_6c a { color: inherit; }

.gb_qd { text-rendering: optimizelegibility; -webkit-font-smoothing: antial=
iased; }

.gb_qd { opacity: 1; }

.gb_7d { position: relative; }

.gb_M { font-family: arial, sans-serif; line-height: normal; padding-right:=
 15px; }

.gb_0 { display: inline-block; padding-left: 15px; }

.gb_0 .gb_Z { display: inline-block; line-height: 24px; vertical-align: mid=
dle; }

.gb_8d { text-align: left; }

.gb_K { display: none; }

@media screen and (max-width: 319px) {
  .gb_Kd .gb_J { display: none; visibility: hidden; }
}

.gb_J .gb_B, .gb_J .gb_B:hover, .gb_J .gb_B:focus { opacity: 1; }

.gb_L { display: none; }

.gb_S { display: none !important; }

.gb_jb { visibility: hidden; }

@media screen and (max-width: 319px) {
  .gb_Kd:not(.gb_Ld) .gb_J { display: none; visibility: hidden; }
}

.gb_vd { display: inline-block; vertical-align: middle; }

.gb_wd .gb_R { bottom: -3px; right: -5px; }

.gb_vd:first-child { padding-left: 0px; }

.gb_D { position: relative; }

.gb_B { display: inline-block; outline: none; vertical-align: middle; borde=
r-radius: 50%; box-sizing: border-box; height: 40px; width: 40px; }

.gb_B, #gb#gb a.gb_B { cursor: pointer; text-decoration: none; }

.gb_B, a.gb_B { color: rgb(0, 0, 0); }

.gb_ma { background: rgb(255, 255, 255); border: 1px solid rgba(0, 0, 0, 0.=
2); color: rgb(0, 0, 0); box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 10px; displ=
ay: none; outline: none; overflow: hidden; position: absolute; right: 0px; =
top: 54px; animation: 0.2s ease 0s 1 normal none running gb__a; border-radi=
us: 2px; user-select: text; }

.gb_vd.gb_5a .gb_ma, .gb_5a.gb_ma { display: block; }

.gb_Ad { position: absolute; right: 0px; top: 54px; z-index: -1; }

.gb_pb .gb_ma { margin-top: -10px; }

.gb_vd:first-child { padding-left: 4px; }

.gb_Ha.gb_Bd .gb_vd:first-child { padding-left: 0px; }

.gb_Cd { position: relative; }

.gb_id .gb_Cd, .gb_Dd .gb_Cd { float: right; }

.gb_B { padding: 8px; cursor: pointer; }

.gb_Fd button svg, .gb_B { border-radius: 50%; }

.gb_vd { padding: 4px; }

.gb_Ha.gb_Bd .gb_vd { padding: 4px 2px; }

.gb_Ha.gb_Bd .gb_z.gb_vd { padding-left: 6px; }

.gb_ma { z-index: 991; line-height: normal; }

.gb_ma.gb_Id { left: 0px; right: auto; }

@media (max-width: 350px) {
  .gb_ma.gb_Id { left: 0px; }
}

.gb_Jd .gb_ma { top: 56px; }

.gb_z .gb_B { padding: 4px; }

.gb_T { display: none; }

.gb_0a:not(.gb_Wd) { position: relative; }

.gb_be::after { content: ""; border: 1px solid rgb(32, 33, 36); opacity: 0.=
13; position: absolute; top: 4px; left: 4px; border-radius: 50%; width: 30p=
x; height: 30px; box-sizing: content-box; }

.gb_Xa { box-sizing: border-box; cursor: pointer; display: inline-block; he=
ight: 48px; overflow: hidden; outline: none; padding: 7px 0px 0px 16px; ver=
tical-align: middle; width: 142px; border-radius: 28px; background-color: t=
ransparent; border: 1px solid; position: relative; }

.gb_Xa .gb_0a { width: 32px; height: 32px; padding: 0px; }

.gb_Xa .gb_R { bottom: -2px; right: -4px; }

.gb_1a .gb_Xa, .gb_2a .gb_Xa { border-color: var(--og-dasher-chip-outline,v=
ar(--gm3-sys-color-outline,#747775)); }

.gb_1a.gb_H .gb_Xa, .gb_2a.gb_H .gb_Xa { border-color: var(--og-dasher-chip=
-outline,var(--gm3-sys-color-outline,#8e918f)); }

.gb_3a .gb_Xa { border-color: var(--og-dasher-chip-outline,var(--gm3-sys-co=
lor-outline,#747775)); }

.gb_3a.gb_H .gb_Xa { border-color: var(--og-dasher-chip-outline,var(--gm3-s=
ys-color-on-surface,#e3e3e3)); }

.gb_4a { display: inherit; }

.gb_Xa .gb_4a { background: rgb(255, 255, 255); border-radius: 6px; display=
: inline-block; left: 15px; position: static; padding: 2px; top: -1px; heig=
ht: 32px; box-sizing: border-box; width: 78px; }

.gb_6a { text-align: center; }

.gb_6a.gb_7a { background-color: rgb(241, 243, 244); }

.gb_6a .gb_8a { vertical-align: middle; max-height: 28px; max-width: 74px; =
}

.gb_Ha .gb_Xa .gb_z.gb_vd { padding: 0px; margin-right: 9px; float: right; =
}

.gb_Ha:not(.gb_9a) .gb_Xa { margin-left: 10px; margin-right: 4px; }

.gb_Xa .gb_be::after { left: 0px; top: 0px; }

@media screen and (max-width: 480px) {
  .gb_Xa .gb_4a { display: none; }
  .gb_Xa { border: none; border-radius: 50%; height: 40px; margin: 4px; out=
line: transparent solid 1px; padding: 0px; width: 40px; }
  .gb_Ha .gb_Xa .gb_z.gb_vd { padding: 4px; margin-right: 0px; }
}

sentinel { }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/html
Content-ID: <frame-05FCC2522AA7309086A7993BE8A24149@mhtml.blink>
Content-Transfer-Encoding: quoted-printable
Content-Location: https://accounts.google.com/RotateCookiesPage?og_pid=425&rot=3&origin=https%3A%2F%2Fcolab.research.google.com&exp_id=0

<!DOCTYPE html><html><head><meta http-equiv=3D"Content-Type" content=3D"tex=
t/html; charset=3DUTF-8"></head><body data-new-gr-c-s-check-loaded=3D"14.12=
78.0" data-gr-ext-installed=3D""></body><grammarly-desktop-integration data=
-grammarly-shadow-root=3D"true"><template shadowmode=3D"open"><div aria-lab=
el=3D"grammarly-integration" role=3D"group" tabindex=3D"-1" class=3D"gramma=
rly-desktop-integration" data-content=3D"{&quot;mode&quot;:&quot;limited&qu=
ot;,&quot;isActive&quot;:false,&quot;isUserDisabled&quot;:false}"></div></t=
emplate></grammarly-desktop-integration></html>
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/html
Content-ID: <frame-E952051BCAE869AF75B67442D3AEFE77@mhtml.blink>
Content-Transfer-Encoding: quoted-printable
Content-Location: https://s0wirjwiw6-496ff2e9c6d22116-0-colab.googleusercontent.com/outputframe.html?vrz=colab-external_20260323-060112_RC00_888000233

<!DOCTYPE html><html><head><meta http-equiv=3D"Content-Type" content=3D"tex=
t/html; charset=3DUTF-8">

</head><body data-new-gr-c-s-check-loaded=3D"14.1278.0" data-gr-ext-install=
ed=3D""><div id=3D"output-area"><span id=3D"output-header"> </span><div id=
=3D"output-body"></div><span id=3D"output-footer"></span></div></body><gram=
marly-desktop-integration data-grammarly-shadow-root=3D"true"><template sha=
dowmode=3D"open"><div aria-label=3D"grammarly-integration" role=3D"group" t=
abindex=3D"-1" class=3D"grammarly-desktop-integration" data-content=3D"{&qu=
ot;mode&quot;:&quot;limited&quot;,&quot;isActive&quot;:false,&quot;isUserDi=
sabled&quot;:false}"></div></template></grammarly-desktop-integration></htm=
l>
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/html
Content-ID: <frame-2D36B4215F9045E8DA5158ACE6E29B15@mhtml.blink>
Content-Transfer-Encoding: quoted-printable
Content-Location: https://alut5uky0hd-496ff2e9c6d22116-0-colab.googleusercontent.com/outputframe.html?vrz=colab-external_20260323-060112_RC00_888000233

<!DOCTYPE html><html><head><meta http-equiv=3D"Content-Type" content=3D"tex=
t/html; charset=3DUTF-8">

</head><body data-new-gr-c-s-check-loaded=3D"14.1278.0" data-gr-ext-install=
ed=3D""><div id=3D"output-area"><span id=3D"output-header"> </span><div id=
=3D"output-body"></div><span id=3D"output-footer"></span></div></body><gram=
marly-desktop-integration data-grammarly-shadow-root=3D"true"><template sha=
dowmode=3D"open"><div aria-label=3D"grammarly-integration" role=3D"group" t=
abindex=3D"-1" class=3D"grammarly-desktop-integration" data-content=3D"{&qu=
ot;mode&quot;:&quot;limited&quot;,&quot;isActive&quot;:false,&quot;isUserDi=
sabled&quot;:false}"></div></template></grammarly-desktop-integration></htm=
l>
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/html
Content-ID: <frame-6681D917E1B9596489F12ED8670F4EC6@mhtml.blink>
Content-Transfer-Encoding: quoted-printable
Content-Location: https://feedback-pa.clients6.google.com/static/proxy.html?usegapi=1&jsh=m%3B%2F_%2Fscs%2Fabc-static%2F_%2Fjs%2Fk%3Dgapi.gapi.en.5G9F9JPGjf8.O%2Fd%3D1%2Frs%3DAHpOoo-OYuAVGK84U6cg5lkjGc85qYpeMw%2Fm%3D__features__#parent=https%3A%2F%2Fcolab.research.google.com&rpctoken=905828309

<!DOCTYPE html><html><head><meta http-equiv=3D"Content-Type" content=3D"tex=
t/html; charset=3DUTF-8">
<title></title>
<meta http-equiv=3D"X-UA-Compatible" content=3D"IE=3Dedge">


</head>
<body data-new-gr-c-s-check-loaded=3D"14.1278.0" data-gr-ext-installed=3D""=
>


</body><grammarly-desktop-integration data-grammarly-shadow-root=3D"true"><=
template shadowmode=3D"open"><div aria-label=3D"grammarly-integration" role=
=3D"group" tabindex=3D"-1" class=3D"grammarly-desktop-integration" data-con=
tent=3D"{&quot;mode&quot;:&quot;limited&quot;,&quot;isActive&quot;:false,&q=
uot;isUserDisabled&quot;:false}"></div></template></grammarly-desktop-integ=
ration></html>
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/html
Content-ID: <frame-CA6BC816279D3EABBACD8934FB5B9764@mhtml.blink>
Content-Transfer-Encoding: quoted-printable
Content-Location: https://colab.research.google.com/_/bscframe

<!DOCTYPE html><html><head><meta http-equiv=3D"Content-Type" content=3D"tex=
t/html; charset=3DUTF-8"></head><body data-new-gr-c-s-check-loaded=3D"14.12=
78.0" data-gr-ext-installed=3D""></body><grammarly-desktop-integration data=
-grammarly-shadow-root=3D"true"><template shadowmode=3D"open"><div aria-lab=
el=3D"grammarly-integration" role=3D"group" tabindex=3D"-1" class=3D"gramma=
rly-desktop-integration" data-content=3D"{&quot;mode&quot;:&quot;limited&qu=
ot;,&quot;isActive&quot;:false,&quot;isUserDisabled&quot;:false}"></div></t=
emplate></grammarly-desktop-integration></html>
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/html
Content-ID: <frame-6FEA70ED9138E49B32952BF767C4F156@mhtml.blink>
Content-Transfer-Encoding: quoted-printable
Content-Location: https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip&co=aHR0cHM6Ly9jb2xhYi5yZXNlYXJjaC5nb29nbGUuY29tOjQ0Mw..&hl=en&v=qm3PSRIx10pekcnS9DjGnjPW&size=invisible&anchor-ms=20000&execute-ms=30000&cb=uvru0tf8dl94

<!DOCTYPE html><html dir=3D"ltr" lang=3D"en"><head><meta http-equiv=3D"Cont=
ent-Type" content=3D"text/html; charset=3DUTF-8"><link rel=3D"stylesheet" t=
ype=3D"text/css" href=3D"cid:css-a1a0882a-d577-4833-a890-515d2153124f@mhtml=
.blink" />
<meta http-equiv=3D"X-UA-Compatible" content=3D"IE=3Dedge">
<title>reCAPTCHA</title>

<link rel=3D"stylesheet" type=3D"text/css" href=3D"https://www.gstatic.com/=
recaptcha/releases/qm3PSRIx10pekcnS9DjGnjPW/styles__ltr.css">

</head>
<body data-new-gr-c-s-check-loaded=3D"14.1278.0" data-gr-ext-installed=3D""=
><div id=3D"rc-anchor-alert" class=3D"rc-anchor-alert"></div>

<div class=3D"rc-anchor rc-anchor-invisible rc-anchor-light  rc-anchor-invi=
sible-hover"><div id=3D"recaptcha-accessible-status" class=3D"rc-anchor-ari=
a-status" aria-hidden=3D"true">Recaptcha requires verification. </div><div =
class=3D"rc-anchor-error-msg-container" style=3D"display:none"><span class=
=3D"rc-anchor-error-msg" aria-hidden=3D"true"></span></div><div class=3D"rc=
-anchor-normal-footer"><div class=3D"rc-anchor-logo-large" role=3D"presenta=
tion"><div class=3D"rc-anchor-logo-img rc-anchor-logo-img-large"></div></di=
v><div class=3D"rc-anchor-pt"><a href=3D"https://www.google.com/intl/en/pol=
icies/privacy/" target=3D"_blank">Privacy</a><span aria-hidden=3D"true" rol=
e=3D"presentation"> - </span><a href=3D"https://www.google.com/intl/en/poli=
cies/terms/" target=3D"_blank">Terms</a></div></div><div class=3D"rc-anchor=
-invisible-text"><span>protected by <strong>reCAPTCHA</strong></span><div c=
lass=3D"rc-anchor-pt"><a href=3D"https://www.google.com/intl/en/policies/pr=
ivacy/" target=3D"_blank" style=3D"">Privacy</a><span aria-hidden=3D"true" =
role=3D"presentation"> - </span><a href=3D"https://www.google.com/intl/en/p=
olicies/terms/" target=3D"_blank" style=3D"">Terms</a></div></div></div><if=
rame style=3D"display: none;"></iframe></body><grammarly-desktop-integratio=
n data-grammarly-shadow-root=3D"true"><template shadowmode=3D"open"><div ar=
ia-label=3D"grammarly-integration" role=3D"group" tabindex=3D"-1" class=3D"=
grammarly-desktop-integration" data-content=3D"{&quot;mode&quot;:&quot;limi=
ted&quot;,&quot;isActive&quot;:false,&quot;isUserDisabled&quot;:false}"></d=
iv></template></grammarly-desktop-integration></html>
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: image/png
Content-Transfer-Encoding: base64
Content-Location: https://www.gstatic.com/recaptcha/api2/logo_48.png

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
RK5CYII=

------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: https://www.gstatic.com/recaptcha/releases/qm3PSRIx10pekcnS9DjGnjPW/styles__ltr.css

@charset "utf-8";

.goog-inline-block { position: relative; display: inline-block; }

* html .goog-inline-block { display: inline; }

:first-child + html .goog-inline-block { display: inline; }

.recaptcha-checkbox { border: none; font-size: 1px; height: 28px; margin: 4=
px; width: 28px; overflow: visible; outline: 0px; vertical-align: text-bott=
om; }

.recaptcha-checkbox-border { border-radius: 2px; background-color: rgb(255,=
 255, 255); border: 2px solid rgb(68, 71, 70); font-size: 1px; height: 24px=
; position: absolute; width: 24px; z-index: 1; }

.recaptcha-checkbox-borderAnimation { background-image: url("data:image/png=
;base64,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3D"); background-r=
epeat: no-repeat; border: none; height: 28px; outline: 0px; position: absol=
ute; width: 28px; }

.recaptcha-checkbox-nodatauri.recaptcha-checkbox-borderAnimation { backgrou=
nd-image: url("https://www.gstatic.com/recaptcha/api2/checkbox_sprite.png")=
; }

.recaptcha-checkbox-spinner-gif { border-radius: 2px; background-color: rgb=
(255, 255, 255); background-size: 24px; border: 2px solid rgb(68, 71, 70); =
height: 24px; left: 0px; position: absolute; top: 0px; width: 24px; }

.recaptcha-checkbox-spinner { background-color: rgb(249, 249, 249); border-=
width: 6px; border-style: solid; border-color: rgb(77, 144, 254) rgb(77, 14=
4, 254) transparent transparent; border-image: initial; border-radius: 36px=
; height: 36px; left: -4px; outline: 0px; position: absolute; top: -4px; wi=
dth: 36px; box-sizing: border-box; opacity: 0; animation: 2.5s linear 0s in=
finite normal none paused spinner-spin; transition-duration: 1s; }

@-webkit-keyframes spinner-spin {=20
  0% { transform: rotateZ(0deg); }
  10% { transform: rotateZ(135deg); }
  25% { transform: rotateZ(245deg); }
  60% { transform: rotateZ(700deg); }
  75% { transform: rotateZ(810deg); }
  100% { transform: rotateZ(3turn); }
}

@keyframes spinner-spin {=20
  0% { transform: rotateZ(0deg); }
  10% { transform: rotateZ(135deg); }
  25% { transform: rotateZ(245deg); }
  60% { transform: rotateZ(700deg); }
  75% { transform: rotateZ(810deg); }
  100% { transform: rotateZ(3turn); }
}

.recaptcha-checkbox-spinner-overlay { content: ""; position: absolute; top:=
 -7px; left: -7px; width: 38px; height: 19px; background-color: rgb(249, 24=
9, 249); animation: 1s linear 0s 1 normal none paused overlay-spin; transfo=
rm-origin: center bottom; border-radius: 38px 38px 0px 0px; transform: rota=
teZ(45deg); opacity: 0; }

@-webkit-keyframes overlay-spin {=20
  0% { opacity: 1; transform: rotateZ(45deg); }
  100% { opacity: 1; transform: rotateZ(225deg); }
}

@keyframes overlay-spin {=20
  0% { opacity: 1; transform: rotateZ(45deg); }
  100% { opacity: 1; transform: rotateZ(225deg); }
}

.recaptcha-checkbox-checkmark { background-image: url("data:image/png;base6=
4,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
RU5ErkJggg=3D=3D"); background-repeat: no-repeat; border: none; height: 30p=
x; left: -5px; outline: 0px; position: absolute; width: 38px; }

.rc-anchor-dark .recaptcha-checkbox-spinner, .rc-anchor-dark .recaptcha-che=
ckbox-spinner-overlay { background-color: rgb(34, 34, 34); }

.recaptcha-checkbox-nodatauri.recaptcha-checkbox-checkmark { background-ima=
ge: url("https://www.gstatic.com/recaptcha/api2/checkmark_sprite.png"); }

.recaptcha-checkbox-hover .recaptcha-checkbox-border, .recaptcha-checkbox-h=
over .recaptcha-checkbox-spinner-gif { box-shadow: rgba(0, 0, 0, 0.1) 0px 1=
px 1px inset; border: 2px solid rgb(178, 178, 178); }

.recaptcha-checkbox-focused .recaptcha-checkbox-border, .recaptcha-checkbox=
-focused .recaptcha-checkbox-spinner-gif { border: 2px solid rgb(77, 144, 2=
54); }

.recaptcha-checkbox-active .recaptcha-checkbox-border, .recaptcha-checkbox-=
active .recaptcha-checkbox-spinner-gif { background-color: rgb(235, 235, 23=
5); }

.recaptcha-checkbox-disabled .recaptcha-checkbox-border, .recaptcha-checkbo=
x-disabled .recaptcha-checkbox-spinner-gif { background-color: rgb(241, 241=
, 241); }

.recaptcha-checkbox-loading .recaptcha-checkbox-spinner-gif { background-im=
age: url("https://www.gstatic.com/recaptcha/api2/loading.gif"); }

.recaptcha-checkbox-checked .recaptcha-checkbox-border, .recaptcha-checkbox=
-checked .recaptcha-checkbox-spinner-gif { visibility: hidden; }

.recaptcha-checkbox-checked .recaptcha-checkbox-checkmark { background-posi=
tion: 0px -600px; }

.recaptcha-checkbox-expired .recaptcha-checkbox-border, .recaptcha-checkbox=
-expired .recaptcha-checkbox-spinner-gif { border: 2px solid rgb(217, 48, 3=
7); }

.recaptcha-checkbox-clearOutline.recaptcha-checkbox-focused .recaptcha-chec=
kbox-border, .recaptcha-checkbox-clearOutline.recaptcha-checkbox-focused .r=
ecaptcha-checkbox-spinner-gif { border: 2px solid rgb(68, 71, 70); }

body { margin: 0px; }

.rc-anchor { border-radius: 3px; box-shadow: rgba(0, 0, 0, 0.08) 0px 0px 4p=
x 1px; }

.rc-anchor-normal { height: 74px; width: 300px; }

.rc-anchor-compact { height: 136px; width: 156px; }

.rc-anchor-compact #rc-anchor-classic-warning { width: 140px; text-align: c=
enter; }

.rc-anchor-dark { background: rgb(34, 34, 34); color: rgb(255, 255, 255); }

.rc-anchor-dark.rc-anchor-normal, .rc-anchor-dark.rc-anchor-compact { borde=
r: 1px solid rgb(82, 82, 82); }

.rc-anchor-dark #rc-anchor-over-quota, .rc-anchor-dark.rc-anchor-compact #r=
c-anchor-over-quota, .rc-anchor-dark.rc-anchor-normal #rc-anchor-classic-wa=
rning, .rc-anchor-dark.rc-anchor-compact #rc-anchor-classic-warning, .rc-an=
chor-dark.rc-anchor-normal #rc-anchor-v1beta1-shutdown-warning, .rc-anchor-=
dark.rc-anchor-compact #rc-anchor-v1beta1-shutdown-warning { color: rgb(255=
, 255, 255); }

.rc-anchor-light { background: rgb(249, 249, 249); color: rgb(0, 0, 0); }

.rc-anchor-light.rc-anchor-normal, .rc-anchor-light.rc-anchor-compact { bor=
der: 1px solid rgb(211, 211, 211); }

.rc-inline-block { display: inline-block; height: 100%; }

.rc-anchor-center-container { display: table; height: 100%; }

.rc-anchor-center-item { display: table-cell; vertical-align: middle; }

.rc-anchor-content { display: inline-block; position: relative; }

.rc-anchor-normal .rc-anchor-content { height: 74px; width: 206px; }

.rc-anchor-compact .rc-anchor-content { height: 85px; }

.rc-anchor-error-message { color: rgb(255, 0, 0); font-family: Roboto, helv=
etica, arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 1=
6px; padding: 0px 10px; }

.rc-anchor-checkbox { margin: 0px 12px 2px; }

.rc-anchor-checkbox-label { font-family: Roboto, helvetica, arial, sans-ser=
if; font-size: 14px; font-weight: 400; line-height: 17px; }

.rc-anchor-normal .rc-anchor-checkbox-label { width: 152px; }

.rc-anchor-compact .rc-anchor-checkbox-label { width: 95px; }

.rc-anchor-error-msg-container { color: rgb(217, 48, 37); font-family: Robo=
to, helvetica, arial, sans-serif; font-size: 12px; font-weight: 400; left: =
0px; line-height: 14px; margin: 2px; position: absolute; top: 0px; }

.rc-anchor-normal.rc-anchor-error .rc-anchor-error-msg-container { width: 2=
40px; }

.rc-anchor-normal.rc-anchor-error .rc-anchor-content { margin-top: 10px; }

.rc-anchor-compact.rc-anchor-error .rc-anchor-content { margin-top: 25px; }

.rc-anchor-normal-footer { display: inline-block; height: 74px; vertical-al=
ign: top; width: 70px; }

.rc-anchor-compact-footer { margin: 0px 12px; text-align: center; width: 13=
6px; }

.rc-anchor-logo-img { background: url("https://www.gstatic.com/recaptcha/ap=
i2/logo_48.png") no-repeat; }

.rc-anchor-logo-img-ie8 { }

.rc-anchor-logo-text { cursor: default; font-family: Roboto, helvetica, ari=
al, sans-serif; font-size: 10px; font-weight: 400; line-height: 10px; margi=
n-top: 5px; text-align: center; }

.rc-anchor-light .rc-anchor-logo-text, .rc-anchor-light div a:link, .rc-anc=
hor-light div a:visited { color: rgb(85, 85, 85); }

.rc-anchor-dark .rc-anchor-logo-text, .rc-anchor-dark div a:link, .rc-ancho=
r-dark div a:visited { color: rgb(245, 245, 245); }

.rc-anchor-logo-portrait { margin: 10px 0px 0px 26px; width: 58px; user-sel=
ect: none; }

.rc-anchor-logo-img-portrait { background-size: 32px; height: 32px; margin:=
 0px 13px; width: 32px; }

.rc-anchor-logo-landscape { user-select: none; }

.rc-anchor-logo-img-landscape { background-size: 24px; display: inline-bloc=
k; height: 24px; width: 24px; }

.rc-anchor-logo-landscape-text-holder { display: inline-block; height: 24px=
; margin: 0px 2px; width: 54px; }

.rc-anchor-normal .rc-anchor-pt, .rc-anchor-invisible .rc-anchor-pt, .rc-an=
chor-compact .rc-anchor-pt { font-family: Roboto, helvetica, arial, sans-se=
rif; font-size: 8px; font-weight: 400; }

.rc-anchor-pt { background-image: url("data:image/png;base64,iVBORw0KGgBX2E=
QZQBOnoDD2UcBhW1sSiNmRQ8RLXQFNGEeygBY2c9ObVv9U1t63RNBc6wgU2VvBPuEb0HRObDgBX=
lGjaztkBWm8aGJkATRZZa3RzU6xhDAwBuFJvGDokk0hlRv6FSghlBGdtzcqF6RQBVwudRzWvBcG=
FXHkxMO6F5Dx0B0GGK82EPKTobIlQ1OwBag4xQGEuQbhhZExTpOMDBdWcMLJAH6z05bpVM3n1yI=
HoBny71Em5nBb3FFaA1IB1nQYk269fH5kcxBuVnl2DwBHU8DmmdyZWV0Kp9/B/utvhXIgX65veQ=
BbxxyTBBhPIp43wBuV2HH3NWZDvKaRUBcaWcBYwCccgG1CS5ayvpLA+VaS2AoJEGZWOY/OJHry+=
PRBih8RohtGaoLIEyGBdlheMvRrX9ddH3tfKX9eyhoEy/2dl3sqLyixil0zXIrepVxUhxsq0CN8=
YypdBCrZLgz43ZCkKTB8Pqf4WkFkNSU3fTWFahPQLh42Bv853YXR2dHIBo7Vtbh5kR3Jm/t/o8W=
UBb4M/nElvLlCkb4TpsrVtByaN2YWM35OlwBOjsdc8PAB01o/BdE5l9unUdAooYXA74zIBawZfP=
8ccRU+Gb5hvUABVU0zkLigyABoG7f6XMOZHcTVVMBdAFk3zQB1G/Ea9NwaXQnBZnF2RxZlSI96R=
QBI89vGAM3C9I9p4U+RXPsBdJjXfmUB/Nt6pN2ZX3cUin0lWs98YnyzBaWA3ZOr3R7hqBfatk02=
0qBfBoRLHL6KHIBakhwo3XdbxkBUh6HRnEkfhv+fV1Zrn87g80uFFbUIA9Qtsxx+4pcPURUGvI/=
BHxZG75dkfdfKKVTm1OlkAQZD1Hb7EeEgylwBdHIenSyS95xEYe5pbgQBYZV2E255ZTuaZHo");=
 }

.rc-anchor-pt a { display: inline; padding: 2px 1px; text-decoration: none;=
 }

.rc-anchor-pt a:hover { text-decoration: underline; }

.rc-anchor-normal .rc-anchor-pt { margin: 2px 11px 0px 0px; padding-right: =
2px; position: absolute; right: 0px; text-align: right; width: 276px; }

.rc-anchor-compact .rc-anchor-pt { margin: 0px 0px 2px; width: 132px; }

.rc-anchor-aria-status { display: none; }

#rc-anchor-alert, .rc-anchor-alert { color: red; font-size: 9px; margin: 2p=
x; position: absolute; top: 0px; }

#rc-anchor-classic-warning, #rc-anchor-v1beta1-shutdown-warning { bottom: 0=
px; color: rgb(85, 85, 85); font-family: Roboto, helvetica, arial, sans-ser=
if; font-size: 9px; padding: 4px; position: absolute; width: 190px; display=
: flex; -webkit-box-align: center; align-items: center; height: 20px; }

#rc-anchor-classic-warning a { display: inline-block; position: relative; z=
-index: 1; padding: 4px; margin: -4px; }

#rc-anchor-v1beta1-shutdown-warning a { display: inline-block; position: re=
lative; z-index: 1; padding: 4px; margin: -4px; }

#rc-anchor-over-quota { bottom: 0px; color: rgb(85, 85, 85); font-family: R=
oboto, helvetica, arial, sans-serif; font-size: 9px; padding: 4px; position=
: absolute; width: 170px; display: flex; -webkit-box-align: center; align-i=
tems: center; height: 20px; }

.rc-anchor-compact .rc-anchor-content #rc-anchor-over-quota { width: 148px;=
 }

.rc-anchor-normal .rc-anchor-pt.rc-anchor-over-quota-pt { width: 130px; }

.rc-anchor-logo-portrait.rc-anchor-over-quota-logo { margin-top: 6px; }

#rc-anchor-invisible-over-quota, #rc-anchor-invisible-classic-warning { fon=
t-size: 9px; line-height: normal; }

#rc-anchor-invisible-over-quota a, #rc-anchor-invisible-classic-warning a, =
#rc-anchor-invisible-v1beta1-shutdown-warning a { color: white; }

#rc-anchor-invisible-v1beta1-shutdown-warning { font-size: 9px; line-height=
: normal; }

.rc-anchor-invisible { height: 60px; width: 256px; display: flex; }

.rc-anchor-invisible-text { background: rgb(26, 115, 232); color: white; di=
splay: flex; flex-basis: 166px; -webkit-box-orient: vertical; -webkit-box-d=
irection: normal; flex-direction: column; -webkit-box-flex: 1; flex-grow: 1=
; font-family: Roboto, helvetica, arial, sans-serif; font-size: 13px; font-=
weight: 400; height: 100%; -webkit-box-pack: center; justify-content: cente=
r; line-height: 20px; padding: 0px 16px; white-space: nowrap; }

.rc-anchor-invisible-text.smalltext { font-size: 12px; padding: 0px 10px; l=
ine-height: 16px; white-space: normal; }

.rc-anchor-invisible-text.smalltext .rc-anchor-pt { line-height: 12px; whit=
e-space: normal; }

.rc-anchor-invisible-text.smalltext .rc-anchor-pt a:link { font-size: 9px; =
}

.rc-anchor-normal-footer.smalltext .rc-anchor-pt { font-size: 5px; line-hei=
ght: 6px; }

.rc-anchor-invisible-text strong { font-weight: 500; }

.rc-anchor-invisible .rc-anchor-normal-footer .rc-anchor-pt { transition: o=
pacity 0.3s; text-align: center; width: 70px; margin-top: 2px; }

.rc-anchor-logo-img-large { transition: 0.3s; background-size: 40px; margin=
: 5px 15px 0px; height: 40px; width: 40px; }

.rc-anchor-invisible-nohover .rc-anchor-logo-img-large, .rc-anchor-invisibl=
e-hover-hovered .rc-anchor-logo-img-large { background-size: 44px; margin: =
8px 13px 0px; height: 44px; width: 44px; }

.rc-anchor-invisible-nohover .rc-anchor-normal-footer .rc-anchor-pt, .rc-an=
chor-invisible-hover-hovered .rc-anchor-normal-footer .rc-anchor-pt { opaci=
ty: 0; }

.rc-anchor-invisible-nohover .rc-anchor-invisible-text .rc-anchor-pt, .rc-a=
nchor-invisible-hover-hovered .rc-anchor-invisible-text .rc-anchor-pt { opa=
city: 1; }

.rc-anchor-invisible-text .rc-anchor-pt { transition: opacity 0.3s; }

.rc-anchor-invisible-text .rc-anchor-pt a:link, .rc-anchor-invisible-text .=
rc-anchor-pt a:visited { color: white; font-size: 10px; }

.rc-anchor-invisible-hover .rc-anchor-invisible-text .rc-anchor-pt a:link {=
 display: none; }

.rc-anchor-invisible-nohover .rc-anchor-invisible-text .rc-anchor-pt a:link=
, .rc-anchor-invisible-hover-hovered .rc-anchor-invisible-text .rc-anchor-p=
t a:link { display: inline; }

.rc-anchor-invisible-hover .rc-anchor-normal-footer .rc-anchor-pt a:link { =
display: inline; }

.rc-anchor-invisible-nohover .rc-anchor-normal-footer .rc-anchor-pt a:link,=
 .rc-anchor-invisible-hover-hovered .rc-anchor-normal-footer .rc-anchor-pt =
a:link { display: none; }

.rc-audiochallenge-response-field { margin: 7px; text-align: center; }

.rc-audiochallenge-response-field .rc-response-input-field { width: 220px; =
}

.rc-audiochallenge-error-message { color: rgb(217, 48, 37); font-family: Ro=
boto, helvetica, arial, sans-serif; font-size: 14px; font-weight: 400; marg=
in: 20px 20px 0px; }

.rc-audiochallenge-instructions { font-family: Roboto, helvetica, arial, sa=
ns-serif; font-size: 14px; font-weight: 400; margin: 10px 20px; }

.rc-audiochallenge-play-button { margin: 0px 20px; }

.rc-audiochallenge-play-button .rc-button-default { background: rgb(216, 21=
6, 216); color: rgb(0, 0, 0); font-weight: 500; width: 100%; }

.rc-audiochallenge-input-label { font-family: Roboto, helvetica, arial, san=
s-serif; font-size: 14px; font-weight: 400; margin: 10px 20px; }

.rc-audiochallenge-control audio { height: 30px; width: 240px; }

.rc-audiochallenge-tdownload { margin: 5px 20px; text-align: center; }

.rc-audiochallenge-tdownload-link { background-image: url("https://www.gsta=
tic.com/recaptcha/api2/download.png"); background-repeat: no-repeat; backgr=
ound-size: 36px; color: transparent; display: inline-block; height: 36px; o=
pacity: 0.55; overflow: hidden; width: 36px; }

.rc-audiochallenge-tdownload-link:focus-visible { background-color: rgb(216=
, 216, 216); }

@media screen and (forced-colors: active) and (prefers-color-scheme: dark) =
{
  .rc-audiochallenge-tdownload-link { background-image: url("https://www.gs=
tatic.com/recaptcha/api2/download_white.png"); background-repeat: no-repeat=
; background-size: 36px; color: transparent; display: inline-block; height:=
 36px; opacity: 0.55; overflow: hidden; width: 36px; }
}

.rc-audiochallenge-tdownload-link-on-dark { background-image: url("https://=
www.gstatic.com/recaptcha/api2/download_white.png"); background-repeat: no-=
repeat; background-size: 36px; color: transparent; display: inline-block; h=
eight: 36px; opacity: 0.55; overflow: hidden; width: 36px; }

.rc-audiochallenge-tdownload-link-on-dark:focus-visible { background-color:=
 rgb(216, 216, 216); }

.rc-audiochallenge-tdownload-link:focus, .rc-audiochallenge-tdownload-link:=
hover { opacity: 0.8; outline: none; }

.rc-audiochallenge-tdownload-link-on-dark:focus, .rc-audiochallenge-tdownlo=
ad-link-on-dark:hover { opacity: 0.8; outline: none; }

.fake-focus-audio { height: 0px; opacity: 0; width: 0px; }

.rc-button-default { background: rgb(26, 115, 232); border: 0px; border-rad=
ius: 2px; color: rgb(255, 255, 255); cursor: pointer; font-family: Roboto, =
helvetica, arial, sans-serif; font-size: 14px; font-weight: 500; height: 42=
px; line-height: 42px; min-width: 100px; padding: 0px 10px; text-align: cen=
ter; text-transform: uppercase; transition: 0.5s; }

.rc-button-default:focus { outline: 0px; box-shadow: rgb(24, 90, 188) 0px 0=
px 0px 2pt; }

.rc-button-default-disabled { background: rgba(73, 143, 225, 0.5); cursor: =
default; }

.rc-button-red { background: rgb(226, 74, 74); }

.rc-button-default-disabled.rc-button-red { background: rgba(226, 74, 74, 0=
.49); }

.rc-canvas-image { display: none; }

.rc-canvas-canvas { cursor: pointer; }

body { margin: 0px; }

.rc-imageselect-instructions strong { font-weight: 900; display: block; fon=
t-size: 28px; }

.rc-footer { font-family: Roboto, helvetica, arial, sans-serif; position: r=
elative; width: 100%; }

.rc-separator { border-top: 1px solid rgb(223, 223, 223); margin-bottom: 1p=
x; }

.rc-controls { width: 100%; }

.primary-controls { height: 60px; }

.rc-buttons { float: left; height: 48px; margin: 6px 0px 6px 6px; backgroun=
d-repeat: no-repeat; }

.fake-focus { height: 0px; opacity: 0; width: 0px; }

.button-holder, .qr-button-holder { float: left; height: 48px; }

.rc-button-reload { background: url("https://www.gstatic.com/recaptcha/api2=
/refresh_2x.png"); }

.rc-button-reload:focus-visible { background-color: rgb(216, 216, 216); }

@media screen and (forced-colors: active) and (prefers-color-scheme: dark) =
{
  .rc-button-reload { background: url("https://www.gstatic.com/recaptcha/ap=
i2/refresh_white_2x.png"); }
}

.rc-button-reload-on-dark { background: url("https://www.gstatic.com/recapt=
cha/api2/refresh_white_2x.png"); }

.rc-button-reload-on-dark:focus-visible { background-color: rgb(216, 216, 2=
16); }

.rc-button-audio { background: url("https://www.gstatic.com/recaptcha/api2/=
audio_2x.png"); }

.rc-button-audio:focus-visible { background-color: rgb(216, 216, 216); }

@media screen and (forced-colors: active) and (prefers-color-scheme: dark) =
{
  .rc-button-audio { background: url("https://www.gstatic.com/recaptcha/api=
2/audio_white_2x.png"); }
}

.rc-button-audio-on-dark { background: url("https://www.gstatic.com/recaptc=
ha/api2/audio_white_2x.png"); }

.rc-button-audio-on-dark:focus-visible { background-color: rgb(216, 216, 21=
6); }

.rc-button-image { background: url("https://www.gstatic.com/recaptcha/api2/=
image_2x.png"); }

.rc-button-image:focus-visible { background-color: rgb(216, 216, 216); }

@media screen and (forced-colors: active) and (prefers-color-scheme: dark) =
{
  .rc-button-image { background: url("https://www.gstatic.com/recaptcha/api=
2/image_white_2x.png"); }
}

.rc-button-image-on-dark { background: url("https://www.gstatic.com/recaptc=
ha/api2/image_white_2x.png"); }

.rc-button-image-on-dark:focus-visible { background-color: rgb(216, 216, 21=
6); }

.rc-button-liveness { background: url("https://www.gstatic.com/recaptcha/ap=
i2/liveness_dark.png"); }

.rc-button-qr { background: url("https://www.gstatic.com/recaptcha/api2/mod=
ac_mobile_dark.png"); }

.rc-button-liveness:focus-visible { background-color: rgb(216, 216, 216); }

.rc-button-qr:focus-visible { background-color: rgb(216, 216, 216); }

@media screen and (forced-colors: active) and (prefers-color-scheme: dark) =
{
  .rc-button-liveness { background: url("https://www.gstatic.com/recaptcha/=
api2/liveness_light.png"); }
}

@media screen and (forced-colors: active) and (prefers-color-scheme: dark) =
{
  .rc-button-qr { background: url("https://www.gstatic.com/recaptcha/api2/m=
odac_mobile_light.png"); }
}

.rc-button-liveness-on-dark { background: url("https://www.gstatic.com/reca=
ptcha/api2/liveness_light.png"); }

.rc-button-qr-on-dark { background: url("https://www.gstatic.com/recaptcha/=
api2/qr_light.png"); }

.rc-button-liveness-on-dark:focus-visible { background-color: rgb(216, 216,=
 216); }

.rc-button-qr-on-dark:focus-visible { background-color: rgb(216, 216, 216);=
 }

.rc-button-help { background: url("https://www.gstatic.com/recaptcha/api2/i=
nfo_2x.png"); }

.rc-button-help:focus-visible { background-color: rgb(216, 216, 216); }

@media screen and (forced-colors: active) and (prefers-color-scheme: dark) =
{
  .rc-button-help { background: url("https://www.gstatic.com/recaptcha/api2=
/info_white_2x.png"); }
}

.rc-button-help-on-dark { background: url("https://www.gstatic.com/recaptch=
a/api2/info_white_2x.png"); }

.rc-button-help-on-dark:focus-visible { background-color: rgb(216, 216, 216=
); }

.rc-button-undo { background: url("https://www.gstatic.com/recaptcha/api2/u=
ndo_2x.png"); }

.rc-button-undo:focus-visible { background-color: rgb(216, 216, 216); }

@media screen and (forced-colors: active) and (prefers-color-scheme: dark) =
{
  .rc-button-undo { background: url("https://www.gstatic.com/recaptcha/api2=
/undo_white_2x.png"); }
}

.rc-button-undo-on-dark { background: url("https://www.gstatic.com/recaptch=
a/api2/undo_white_2x.png"); }

.rc-button-undo-on-dark:focus-visible { background-color: rgb(216, 216, 216=
); }

.rc-button { background-size: 32px 32px; cursor: pointer; height: 48px; opa=
city: 0.55; width: 48px; padding: 0px; border: 0px; background-repeat: no-r=
epeat; background-position: center center; }

.rc-button:focus, .rc-button:hover { opacity: 0.8; outline: none; }

.verify-button-holder { float: right; margin: 8px 8px 9px 0px; }

.rc-challenge-help { font-family: Roboto, helvetica, arial, sans-serif; fon=
t-size: 12px; font-weight: 400; overflow-y: scroll; padding: 5px 20px; }

.reload-icon { height: 16px; width: 16px; }

.apps-toast { position: relative; text-align: center; width: 100%; z-index:=
 101; }

.apps-toast-content { background: rgb(50, 50, 50); border-radius: 2px; box-=
shadow: rgba(0, 0, 0, 0.14) 0px 6px 10px, rgba(0, 0, 0, 0.12) 0px 1px 18px,=
 rgba(0, 0, 0, 0.4) 0px 3px 5px -1px; color: rgb(238, 238, 238); display: i=
nline-block; font: 12px / 20px Roboto, helvetica, arial, sans-serif; paddin=
g: 14px; text-align: center; }

.goog-container:focus { outline: none; }

.rc-defaultchallenge-response-field { margin: 7px; text-align: center; }

.rc-defaultchallenge-response-field .rc-response-input-field { width: 230px=
; }

.rc-defaultchallenge-payload { border: none; font-family: Roboto, helvetica=
, arial, sans-serif; font-size: 14px; font-weight: 400; min-height: 61px; t=
ext-align: center; }

.rc-defaultchallenge-incorrect-response { color: rgb(255, 27, 27); font-fam=
ily: Roboto, helvetica, arial, sans-serif; font-size: 12px; font-weight: 40=
0; line-height: 14px; margin-left: 20px; }

.rc-doscaptcha-header { padding: 10px; margin: 10px; height: 20%; backgroun=
d-color: rgb(26, 115, 232); }

.rc-doscaptcha-header-text { font-family: Roboto, helvetica, arial, sans-se=
rif; font-size: 22px; font-weight: 400; text-align: center; color: white; }

.rc-doscaptcha-body { height: 80%; }

.rc-doscaptcha-body-text { font-family: Roboto, helvetica, arial, sans-seri=
f; font-size: 16px; font-weight: 400; padding: 10px 15px; }

.rc-doscaptcha-footer { pointer-events: none; }

.recaptchaJavascriptChallengeLivenessOuterContainer { position: absolute; i=
nset: 0px; display: flex; -webkit-box-orient: vertical; -webkit-box-directi=
on: normal; flex-direction: column; }

.recaptchaJavascriptChallengeLivenessContainer { -webkit-box-flex: 1; flex-=
grow: 1; }

.goog-container:focus { outline: none; }

#rc-imageselect { min-width: 240px; font-family: Roboto, helvetica, arial, =
sans-serif; background-color: rgb(255, 255, 255); }

#rc-imageselect .rc-button:focus { outline: none; }

.rc-imageselect-desc { margin-left: -10px; margin-top: -10px; padding-right=
: 100px; position: relative; }

.rc-imageselect-instructions .rc-imageselect-desc strong { font-size: 22px;=
 }

.rc-imageselect-desc span { display: block; }

.rc-imageselect-desc-no-canonical { position: relative; }

.rc-imageselect-desc-no-canonical span { display: block; }

.rc-imageselect-payload { min-width: 240px; margin: 0px 7px; padding: 7px 0=
px; }

.rc-imageselect-challenge { position: relative; width: 100%; height: 100%; =
}

.rc-footer { min-width: 240px; }

.rc-imageselect-incorrect-response, .rc-imageselect-error-dynamic-more, .rc=
-imageselect-error-select-more, .rc-imageselect-error-select-something { co=
lor: rgb(217, 48, 37); font-size: 14px; padding: 7px 0px; text-align: cente=
r; width: 100%; background-color: white; }

.rc-imageselect-desc-wrapper { margin-bottom: 6px; }

.rc-imageselect-checkbox { background: url("data:image/png;base64,iVBORw0KG=
goAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAAGnmlUWHRY=
TUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWh=
pSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeD=
p4bXB0az0iQWRvYmUgWE1QIENvcmUgNy4xLWMwMDAgNzkuZGFiYWNiYiwgMjAyMS8wNC8xNC0wM=
DozOTo0NCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8x=
OTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiI=
geG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczpkYz0iaHR0cD=
ovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zL=
mFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5j=
b20veGFwLzEuMC9tbS8iIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjA=
vc1R5cGUvUmVzb3VyY2VFdmVudCMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wID=
IzLjAgKE1hY2ludG9zaCkiIHhtcDpDcmVhdGVEYXRlPSIyMDIxLTExLTA0VDIzOjE2OjI2LTA3O=
jAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMS0xMS0wNFQyMzoxNzozNS0wNzowMCIgeG1wOk1ldGFk=
YXRhRGF0ZT0iMjAyMS0xMS0wNFQyMzoxNzozNS0wNzowMCIgZGM6Zm9ybWF0PSJpbWFnZS9wbmc=
iIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6NDM3Y2=
M2MTEtMjg5Mi00MmFkLWEyYmYtMjk1MzA4NGYxNjA1IiB4bXBNTTpEb2N1bWVudElEPSJhZG9iZ=
Tpkb2NpZDpwaG90b3Nob3A6YjEwZGYyNmItNGU5Mi0wNTQxLThjMDYtMTJjNWQ5ZDFmMjcxIiB4=
bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6ZjE0YzAyYmQtNDJhOC00ODkxLWIxMjM=
tMWZhYjg2NzZlNzJmIj4gPHhtcE1NOkhpc3Rvcnk+IDxyZGY6U2VxPiA8cmRmOmxpIHN0RXZ0Om=
FjdGlvbj0iY3JlYXRlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDpmMTRjMDJiZC00MmE4L=
TQ4OTEtYjEyMy0xZmFiODY3NmU3MmYiIHN0RXZ0OndoZW49IjIwMjEtMTEtMDRUMjM6MTY6MjYt=
MDc6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCAyMy4wIChNYWNpbnR=
vc2gpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG=
1wLmlpZDpjMDJkMDg2Zi1mNmZjLTRjMzItYWU2Zi0wOWMxZmU4MzFhNzciIHN0RXZ0OndoZW49I=
jIwMjEtMTEtMDRUMjM6MTc6MDktMDc6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBo=
b3Rvc2hvcCAyMy4wIChNYWNpbnRvc2gpIiBzdEV2dDpjaGFuZ2VkPSIvIi8+IDxyZGY6bGkgc3R=
FdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo0MzdjYzYxMS0yOD=
kyLTQyYWQtYTJiZi0yOTUzMDg0ZjE2MDUiIHN0RXZ0OndoZW49IjIwMjEtMTEtMDRUMjM6MTc6M=
zUtMDc6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCAyMy4wIChNYWNp=
bnRvc2gpIiBzdEV2dDpjaGFuZ2VkPSIvIi8+IDwvcmRmOlNlcT4gPC94bXBNTTpIaXN0b3J5PiA=
8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD=
0iciI/PlXsutAAAASdSURBVFiFtZdbbBRVGIC/mdnZdndr2+0l0BYsaEJ4ABGkUhHjlT6oT7QRb=
cHaqGkhvFBjBU3AKy9aTYwaQ9pI6wMxEClQiLcmKomtYikCkZsILbYGWuh2aXfLtrvHh53ZPTvd=
bbdtPMnJzOzMme87/392zjkKyRdFOipx7gupJlWEENiSBCuACij3bfgmx5G+dGUQez4h3S1CwQG=
h+PoGvcd+u7C3fAgITUcmXk/igbVVNdcrbJqr6nLqrTWJGiz03/FDaHxwd/vueYeAoEVmQhFCJB=
SIgIuqLxT3pqX/NFVPYkVc7UHl/JaOT1eesYgkJaAAGmArfvnqxp50ffd04HJZMDJS9svnd7cC4=
/EkhBCoieAP1HRXzgYOcMXl2l+8+exTgI4xhqzPKJZzFdDvf6lz9T8ZBW2zgcsl33N6xe+Na//E=
EglrBMK9z8qyzxZecY+bLytzIte6fdVHhKOgYYmCKWD23lZUdrxiNvANy9y8W67z2FKNPRvDEt1=
O38PF1Z0lhkBMKmQBDdB1LadqpvCNy9y885yO3aYwMio4+Ot45J6iFlYRZyyYFyqgLSjZlXfF6S=
+aCfz5e928bcCHRwV1zQEOXPBE7nc7x592Fj7kwpIGVTpqcwufKJ4p/K1no/DXmgK0SHCzLH70j=
WVY0mCehFNgc+TLDdbkZtCxLZeaVe6E8MrlUfgtv6CuKUDLxYlwAJuWMY9oBGIEVEBDOHPkBjvK=
7czPUXm9VGdTHIkXlrt5c30s/GACeNjAkS1FAOQTQEH1euXn61vGuDks0FSF7aU6m4qjElUr3Ow=
04F4DfuivSeCACHq9Uu8VIDIbKoAyFhi6hiMv0uDbbg+iMZP6F+1kpSlsX6ej4MYfgJ3rdXQtCj=
88BRzgtvff69bf5AiI/vNHTlkf+O6qh9rGADduhSOxbZ0ehfsEdXuSgwP83fHJ2UQCAhA9x97vi=
9fw+6setjYEGDAkTPirTQEOX0oOXjgifh7uOebDMj2rxkXIqMF5Q5d2xXtBW6+HWkNiyCd45YsA=
rUnCAfy+E18TOxcIiA4GHUgF0uxpc7Jyqv84nehFjxdkkmKHo5eThwP01c9dDHiBYWAUGBdCCDM=
FIcNuLDB8zZfV07Y50Yvaej3ThrvO7i0HAsAYlhlRTkHQeCBwZl/FjwVDlz6eFiVBmdN/YsfFo1=
u7gNvG+2MWJvIgNAVGAf/xhgcb5nsvfzYb+NyBk+91NT95APBLAkFZQJ6bVcLfhVTACbgA15Ky5=
rU3C0s+mC48/dz+6nNHtrQDI4TzbkqYKZiwJoysiIAUQ8IJOFPdCzOXlDaV92UsqpkKnHfj5Ien=
vnpm35jfOwz4jCpHIGZFZF2jRdYFhkQq4DCOqYB+5+raRdl3PbJET8nO1VRH+nhoZHBsdGCg/1x=
rV29nYzfhwXbbgPoJp9TseUz4E62KVaLpsBsiZrUTXVrJX9HIv0gSMKs58mPgpkC8nZF1ZxP5dx=
hSkwmYEnJNuC+AqXdGZjS0ONX8iMmiZjV7POOdUTwRWUieUuVomZ90wSS9nq6ALCLvkM2jCZGPS=
e2QhRAoQiS9m/5fyn/lu/UIgBExrQAAAABJRU5ErkJggg=3D=3D"); display: none; posit=
ion: absolute; }

.rc-imageselect-report-image { inset: 0px; display: none; position: absolut=
e; }

.rc-imageselect-table-42, .rc-imageselect-table-33, .rc-imageselect-table-4=
4 { border-collapse: separate; border-spacing: 0px; width: 100%; height: 10=
0%; transition: 1s; }

.rc-imageselect-table-42, .rc-imageselect-table-33 { margin: -2px; }

.rc-imageselect-table-44 { margin: -1px; }

.rc-imageselect-table-42 td { padding: 2px; }

.rc-imageselect-table-33 td { padding: 2px; }

.rc-imageselect-table-44 td { padding: 1px; }

.rc-image-tile-target tr, td { margin: 0px; }

.rc-imageselect-keyboard { position: relative; z-index: 100; outline: orang=
e solid !important; }

td:focus { outline: none; }

.rc-image-tile-overlay { display: none; opacity: 0; position: absolute; bac=
kground-color: rgb(26, 115, 232); width: 100%; height: 100%; z-index: 2; tr=
ansition: opacity 1s cubic-bezier(0.49, 0.78, 0.46, 1.34); }

.rc-image-followup-tile { display: block; }

.rc-imageselect-dynamic-selected { position: relative; transition: 2s; opac=
ity: 0.01; }

.rc-imageselect-dynamic-selected .rc-image-tile-target { opacity: 1; }

.rc-imageselect-dynamic-selected .rc-imageselect-checkbox { display: block;=
 opacity: 1; background-size: cover; width: 60px; height: 60px; left: 50%; =
top: 50%; margin-left: -30px; margin-top: -30px; }

.rc-image-tile-target { -webkit-tap-highlight-color: rgba(0, 0, 0, 0); posi=
tion: relative; }

.rc-imageselect-tileselected { position: relative; }

.rc-imageselect-tileselected .rc-image-tile-wrapper { transform: scale(0.8)=
; }

.rc-image-tile-wrapper { transform: scale(1); }

.rc-imageselect-tileselected .rc-imageselect-checkbox { display: block; bac=
kground-repeat: no-repeat; inset: 0px; }

.rc-imageselect-candidates { border: 2px solid white; box-sizing: border-bo=
x; height: 94px; overflow: hidden; position: absolute; right: 7px; top: 7px=
; width: 112px; }

.rc-imageselect-candidates > div { background-size: 112px 94px; display: in=
line-block; height: 94px; margin: 2px; position: relative; width: 112px; }

.rc-imageselect-challenge { box-sizing: border-box; text-align: center; use=
r-select: none; }

.rc-imageselect-response-field-error { border-bottom: 1px solid rgb(255, 0,=
 0); }

.rc-imageselect-desc { font-size: 16px; }

.rc-imageselect-desc-wrapper span { font-size: 14px; }

.rc-imageselect-clear { clear: both; }

.rc-image-tile-wrapper { overflow: hidden; position: relative; transition: =
0.1s; }

.rc-image-tile-wrapper img { position: relative; -webkit-user-drag: none; b=
ackface-visibility: hidden; }

.rc-image-tile-11 { width: 100%; height: 100%; }

.rc-image-tile-42 { width: 200%; height: 400%; }

.rc-image-tile-33 { width: 300%; height: 300%; }

.rc-image-tile-44 { width: 400%; height: 400%; }

.rc-imageselect-instructions { height: 113px; width: 100%; margin-bottom: 7=
px; position: relative; }

.rc-imageselect-desc-wrapper { background-color: rgb(26, 115, 232); positio=
n: relative; padding: 24px; color: white; height: 66px; font-size: 16px; }

.rc-imageselect-progress { background-color: rgb(65, 124, 193); position: a=
bsolute; bottom: 0px; right: 0px; width: 0px; height: 15px; transition: 1s;=
 }

.rc-imageselect-carousel-offscreen-right { left: 105%; position: absolute; =
transition: 0.5s; }

.rc-imageselect-carousel-entering-right { left: 0px; position: absolute; tr=
ansition: 0.5s; }

.rc-imageselect-carousel-mock-margin-1 { top: 1px; }

.rc-imageselect-carousel-mock-margin-2 { top: 2px; }

.rc-imageselect-carousel-leaving-left { left: 0px; opacity: 0.5; position: =
relative; transition: 0.5s; }

.rc-imageselect-carousel-offscreen-left { left: -105%; opacity: 0.5; positi=
on: relative; transition: 0.5s; }

.rc-imageselect-carousel-instructions { transition: 0.2s; opacity: 1; }

.rc-imageselect-carousel-instructions-hidden { opacity: 0.5; }

.rc-canonical-stop-sign { background: url("https://www.gstatic.com/recaptch=
a/api2/stop_sign.jpg") no-repeat; }

.rc-canonical-speed-limit { background: url("https://www.gstatic.com/recapt=
cha/api2/canonical_speed_limit.png") no-repeat; }

.rc-canonical-street-name { background: url("https://www.gstatic.com/recapt=
cha/api2/canonical_street_name.png") no-repeat; }

.rc-canonical-other { background: url("https://www.gstatic.com/recaptcha/ap=
i2/canonical_other.png") no-repeat; }

.rc-canonical-bounding-box { background: url("https://www.gstatic.com/recap=
tcha/api2/boundingbox2.gif") no-repeat; }

.rc-canonical-car { background: url("https://www.gstatic.com/recaptcha/api2=
/canonical_car.png") no-repeat; }

.rc-canonical-road { background: url("https://www.gstatic.com/recaptcha/api=
2/canonical_road.png") no-repeat; }

.rc-canonical-bridge { background: url("https://www.gstatic.com/recaptcha/a=
pi2/canonical_bridge.png") no-repeat; }

.recaptchaJavascriptChallengeQrOuterContainer { position: absolute; inset: =
0px; display: flex; -webkit-box-orient: vertical; -webkit-box-direction: no=
rmal; flex-direction: column; -webkit-box-pack: center; justify-content: ce=
nter; -webkit-box-align: center; align-items: center; }

.recaptchaJavascriptChallengeQrContainer { align-items: anchor-center; posi=
tion: relative; -webkit-box-flex: 1; flex-grow: 1; margin: 10px; display: f=
lex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-dire=
ction: column; }

.recaptchaJavascriptChallengeQrCanvas { min-width: 200px; min-height: 200px=
; max-height: 45%; max-width: 40%; outline-offset: 0px; outline: solid 2px;=
 border-radius: 2pt; padding: 20px; position: relative; border: 1px solid r=
gb(153, 153, 153); box-shadow: rgba(26, 115, 232, 0.3) 0px 0px 9px 2px; bac=
kground: white; }

.recaptchaJavascriptChallengeQrBackground { background: url("https://www.gs=
tatic.com/recaptcha/api2/modac_qr_background.svg") no-repeat; position: abs=
olute; top: 50%; margin-top: -20%; width: 100%; height: 100%; }

.recaptchaJavascriptChallengeQrButton { background: rgb(26, 115, 232); bord=
er: 0px; color: rgb(255, 255, 255); cursor: pointer; font-family: Roboto, h=
elvetica, arial, sans-serif; font-size: 14px; transition: 0.5s; border-radi=
us: 25px; padding: 15px; text-transform: uppercase; text-decoration: none; =
position: relative; margin: 25% auto; }

.recaptchaJavascriptChallengeQrInstructionsContainer { text-align: center; =
font-family: Roboto, helvetica, arial, sans-serif; display: flex; -webkit-b=
ox-orient: vertical; -webkit-box-direction: normal; flex-direction: column;=
 -webkit-box-pack: center; justify-content: center; -webkit-box-align: cent=
er; align-items: center; }

.recaptchaJavascriptChallengeQrShortInstructionsContainer { top: 0px; heigh=
t: 113px; position: relative; background: rgb(26, 115, 232); text-align: ce=
nter; margin: 0px auto; width: 100%; }

.recaptchaJavascriptChallengeQrShortInstructions { font-weight: 700; color:=
 rgb(255, 255, 255); font-size: 20px; margin-top: 45px; }

.recaptchaJavascriptChallengeQrAdditionalInstructionsContainer { position: =
relative; display: flex; -webkit-box-orient: horizontal; -webkit-box-direct=
ion: normal; flex-direction: row; -webkit-box-align: center; align-items: c=
enter; -webkit-box-pack: center; justify-content: center; padding: 10px; }

.recaptchaJavascriptChallengeQrCameraIcon { background: url("https://www.gs=
tatic.com/recaptcha/api2/modac_camera_dark.png") 0% 0% / contain no-repeat;=
 display: inline-block; width: 30px; height: 30px; }

.recaptchaJavascriptChallengeQrMobileIcon { background: url("https://www.gs=
tatic.com/recaptcha/api2/modac_mobile_dark.png") 0% 0% / contain no-repeat;=
 display: inline-block; width: 30px; height: 30px; }

.recaptchaJavascriptChallengeQrAdditionalInstructions { font-weight: 400; f=
ont-size: 14px; padding: 10px 20px 10px 10px; max-width: 80%; line-height: =
1.3; color: rgb(119, 119, 119); }

.recaptchaJavascriptChallengeQrCodeHidden { height: 0px; width: 0px; displa=
y: none; visibility: hidden; }

.recaptchaJavascriptChallengeQrCodeVisible { height: 200px; width: 200px; d=
isplay: inline-block; visibility: visible; }

.recaptchaJavascriptChallengeQrButtonHidden { display: none; visibility: hi=
dden; }

.recaptchaJavascriptChallengeQrButtonVisible { display: inline-block; visib=
ility: visible; }

.rc-prepositional-payload { padding: 20px; font-family: Roboto, helvetica, =
arial, sans-serif; font-size: 14px; font-weight: 400; }

.rc-prepositional-select-more, .rc-prepositional-verify-failed { color: rgb=
(255, 27, 27); font-family: Roboto, helvetica, arial, sans-serif; font-size=
: 14px; font-weight: 400; margin: 20px 20px 0px; }

.rc-prepositional-target label { margin: 5px; float: right; }

.rc-prepositional-instructions { margin-bottom: 20px; }

.rc-prepositional-table { width: 100%; }

.rc-prepositional-table td { background: rgb(249, 249, 249); border: 1px so=
lid rgb(255, 255, 255); color: rgb(0, 0, 0); cursor: pointer; font-family: =
Roboto, helvetica, arial, sans-serif; font-size: 14px; font-weight: 400; wi=
dth: 40%; padding: 15px; }

.rc-prepositional-table td.rc-prepositional-selected { background: rgb(239,=
 239, 239); border: 1px solid rgb(101, 101, 101); }

.rc-2fa-payload { font-family: Roboto, Helvetica, Arial, sans-serif; font-w=
eight: 400; font-size: 14px; color: rgb(32, 33, 36); text-align: center; }

.rc-2fa-background { background-color: rgb(236, 236, 236); width: 100%; hei=
ght: 100%; overflow: auto; }

.rc-2fa-container { background-color: rgb(255, 255, 255); width: 328px; ove=
rflow: auto; margin: 100px auto; }

.rc-2fa-header { margin: 36px 0px 24px; font-size: 16px; }

.rc-2fa-instructions { margin: 24px 40px; line-height: 17.5px; }

.rc-2fa-response-field { text-align: center; }

.rc-2fa-response-field input { width: 11.2ch; height: 40px; line-height: 40=
px; margin: auto; border: 1px solid rgb(151, 151, 151); font-size: 20px; le=
tter-spacing: 0.8ch; padding-left: 1.2ch; padding-right: 0px; }

.rc-2fa-response-field input:focus { border: 1px solid rgb(24, 90, 188); }

.rc-2fa-response-field-error input { border: 1px solid rgb(217, 48, 37); }

.rc-2fa-response-field-error input:focus { border: 1px solid rgb(217, 48, 3=
7); }

.rc-2fa-error-message { height: 36px; font-size: 12px; color: rgb(217, 48, =
37); margin: 2px 40px; }

.rc-2fa-submit-button-holder button { margin: 0px auto; min-width: 100px; h=
eight: 36px; line-height: 36px; text-transform: uppercase; text-align: cent=
er; font-weight: 500; letter-spacing: 1.25px; border-radius: 4px; backgroun=
d-color: rgb(24, 90, 188); border: 1px solid rgb(24, 90, 188); color: rgb(2=
55, 255, 255); }

.rc-2fa-submit-button-holder button:disabled { background-color: white; bor=
der: 1px solid rgb(151, 151, 151); color: rgba(0, 0, 0, 0.38); }

.rc-2fa-cancel-button-holder button { margin: 20px auto; min-width: 100px; =
height: 36px; line-height: 36px; text-transform: uppercase; text-align: cen=
ter; font-weight: 500; letter-spacing: 1.25px; border-radius: 4px; backgrou=
nd: none; border: none; color: rgb(24, 90, 188); }

.rc-2fa-cancel-button-holder button:active { border: none; }

.rc-response-input-field { border: 1px solid rgb(116, 119, 117); border-rad=
ius: 2px; height: 36px; margin: 5px 0px; padding: 1px 9px; font-family: Rob=
oto, helvetica, arial, sans-serif; font-size: 16px; font-weight: 400; outli=
ne: none; width: 270px; }

.rc-response-input-field:focus { border: 1px solid rgb(26, 115, 232); }

.rc-response-input-field-error, .rc-response-input-field-error:focus { bord=
er: 1px solid rgb(255, 0, 0); }

sentinel { }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: cid:css-a1a0882a-d577-4833-a890-515d2153124f@mhtml.blink

@charset "utf-8";

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3GUBGEe.woff2") format("woff2"); unicode-range: U+460-52F=
, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3iUBGEe.woff2") format("woff2"); unicode-range: U+301, U+=
400-45F, U+490-491, U+4B0-4B1, U+2116; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3CUBGEe.woff2") format("woff2"); unicode-range: U+1F00-1F=
FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3-UBGEe.woff2") format("woff2"); unicode-range: U+370-377=
, U+37A-37F, U+384-38A, U+38C, U+38E-3A1, U+3A3-3FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMawCUBGEe.woff2") format("woff2"); unicode-range: U+302-303=
, U+305, U+307-308, U+310, U+312, U+315, U+31A, U+326-327, U+32C, U+32F-330=
, U+332-333, U+338, U+33A, U+346, U+34D, U+391-3A1, U+3A3-3A9, U+3B1-3C9, U=
+3D1, U+3D5-3D6, U+3F0-3F1, U+3F4-3F5, U+2016-2017, U+2034-2038, U+203C, U+=
2040, U+2043, U+2047, U+2050, U+2057, U+205F, U+2070-2071, U+2074-208E, U+2=
090-209C, U+20D0-20DC, U+20E1, U+20E5-20EF, U+2100-2112, U+2114-2115, U+211=
7-2121, U+2123-214F, U+2190, U+2192, U+2194-21AE, U+21B0-21E5, U+21F1-21F2,=
 U+21F4-2211, U+2213-2214, U+2216-22FF, U+2308-230B, U+2310, U+2319, U+231C=
-2321, U+2336-237A, U+237C, U+2395, U+239B-23B7, U+23D0, U+23DC-23E1, U+247=
4-2475, U+25AF, U+25B3, U+25B7, U+25BD, U+25C1, U+25CA, U+25CC, U+25FB, U+2=
66D-266F, U+27C0-27FF, U+2900-2AFF, U+2B0E-2B11, U+2B30-2B4C, U+2BFE, U+303=
0, U+FF5B, U+FF5D, U+1D400-1D7FF, U+1EE00-1EEFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMaxKUBGEe.woff2") format("woff2"); unicode-range: U+1-C, U+=
E-1F, U+7F-9F, U+20DD-20E0, U+20E2-20E4, U+2150-218F, U+2190, U+2192, U+219=
4-2199, U+21AF, U+21E6-21F0, U+21F3, U+2218-2219, U+2299, U+22C4-22C6, U+23=
00-243F, U+2440-244A, U+2460-24FF, U+25A0-27BF, U+2800-28FF, U+2921-2922, U=
+2981, U+29BF, U+29EB, U+2B00-2BFF, U+4DC0-4DFF, U+FFF9-FFFB, U+10140-1018E=
, U+10190-1019C, U+101A0, U+101D0-101FD, U+102E0-102FB, U+10E60-10E7E, U+1D=
2C0-1D2D3, U+1D2E0-1D37F, U+1F000-1F0FF, U+1F100-1F1AD, U+1F1E6-1F1FF, U+1F=
30D-1F30F, U+1F315, U+1F31C, U+1F31E, U+1F320-1F32C, U+1F336, U+1F378, U+1F=
37D, U+1F382, U+1F393-1F39F, U+1F3A7-1F3A8, U+1F3AC-1F3AF, U+1F3C2, U+1F3C4=
-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F3E0, U+1F3ED, U+1F3F1-1F3F3, U+1F3F5-1F3F7=
, U+1F408, U+1F415, U+1F41F, U+1F426, U+1F43F, U+1F441-1F442, U+1F444, U+1F=
446-1F449, U+1F44C-1F44E, U+1F453, U+1F46A, U+1F47D, U+1F4A3, U+1F4B0, U+1F=
4B3, U+1F4B9, U+1F4BB, U+1F4BF, U+1F4C8-1F4CB, U+1F4D6, U+1F4DA, U+1F4DF, U=
+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F4F7, U+1F4F9-1F4FB, U+1F4FD-1F4FE, U+1F503=
, U+1F507-1F50B, U+1F50D, U+1F512-1F513, U+1F53E-1F54A, U+1F54F-1F5FA, U+1F=
610, U+1F650-1F67F, U+1F687, U+1F68D, U+1F691, U+1F694, U+1F698, U+1F6AD, U=
+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U+1F6C6-1F6CF, U+1F6D3-1F6D7, U+1F6E0-1F6EA=
, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U+1F700-1F7FF, U+1F800-1F80B, U+1F810-1F847=
, U+1F850-1F859, U+1F860-1F887, U+1F890-1F8AD, U+1F8B0-1F8BB, U+1F8C0-1F8C1=
, U+1F900-1F90B, U+1F93B, U+1F946, U+1F984, U+1F996, U+1F9E9, U+1FA00-1FA6F=
, U+1FA70-1FA7C, U+1FA80-1FA89, U+1FA8F-1FAC6, U+1FACE-1FADC, U+1FADF-1FAE9=
, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3OUBGEe.woff2") format("woff2"); unicode-range: U+102-103=
, U+110-111, U+128-129, U+168-169, U+1A0-1A1, U+1AF-1B0, U+300-301, U+303-3=
04, U+308-309, U+323, U+329, U+1EA0-1EF9, U+20AB; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3KUBGEe.woff2") format("woff2"); unicode-range: U+100-2BA=
, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF, U+304, U+308, U+329, U+1D00-1=
DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+=
2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 400; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3yUBA.woff2") format("woff2"); unicode-range: U+0-FF, U+1=
31, U+152-153, U+2BB-2BC, U+2C6, U+2DA, U+2DC, U+304, U+308, U+329, U+2000-=
206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3GUBGEe.woff2") format("woff2"); unicode-range: U+460-52F=
, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3iUBGEe.woff2") format("woff2"); unicode-range: U+301, U+=
400-45F, U+490-491, U+4B0-4B1, U+2116; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3CUBGEe.woff2") format("woff2"); unicode-range: U+1F00-1F=
FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3-UBGEe.woff2") format("woff2"); unicode-range: U+370-377=
, U+37A-37F, U+384-38A, U+38C, U+38E-3A1, U+3A3-3FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMawCUBGEe.woff2") format("woff2"); unicode-range: U+302-303=
, U+305, U+307-308, U+310, U+312, U+315, U+31A, U+326-327, U+32C, U+32F-330=
, U+332-333, U+338, U+33A, U+346, U+34D, U+391-3A1, U+3A3-3A9, U+3B1-3C9, U=
+3D1, U+3D5-3D6, U+3F0-3F1, U+3F4-3F5, U+2016-2017, U+2034-2038, U+203C, U+=
2040, U+2043, U+2047, U+2050, U+2057, U+205F, U+2070-2071, U+2074-208E, U+2=
090-209C, U+20D0-20DC, U+20E1, U+20E5-20EF, U+2100-2112, U+2114-2115, U+211=
7-2121, U+2123-214F, U+2190, U+2192, U+2194-21AE, U+21B0-21E5, U+21F1-21F2,=
 U+21F4-2211, U+2213-2214, U+2216-22FF, U+2308-230B, U+2310, U+2319, U+231C=
-2321, U+2336-237A, U+237C, U+2395, U+239B-23B7, U+23D0, U+23DC-23E1, U+247=
4-2475, U+25AF, U+25B3, U+25B7, U+25BD, U+25C1, U+25CA, U+25CC, U+25FB, U+2=
66D-266F, U+27C0-27FF, U+2900-2AFF, U+2B0E-2B11, U+2B30-2B4C, U+2BFE, U+303=
0, U+FF5B, U+FF5D, U+1D400-1D7FF, U+1EE00-1EEFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMaxKUBGEe.woff2") format("woff2"); unicode-range: U+1-C, U+=
E-1F, U+7F-9F, U+20DD-20E0, U+20E2-20E4, U+2150-218F, U+2190, U+2192, U+219=
4-2199, U+21AF, U+21E6-21F0, U+21F3, U+2218-2219, U+2299, U+22C4-22C6, U+23=
00-243F, U+2440-244A, U+2460-24FF, U+25A0-27BF, U+2800-28FF, U+2921-2922, U=
+2981, U+29BF, U+29EB, U+2B00-2BFF, U+4DC0-4DFF, U+FFF9-FFFB, U+10140-1018E=
, U+10190-1019C, U+101A0, U+101D0-101FD, U+102E0-102FB, U+10E60-10E7E, U+1D=
2C0-1D2D3, U+1D2E0-1D37F, U+1F000-1F0FF, U+1F100-1F1AD, U+1F1E6-1F1FF, U+1F=
30D-1F30F, U+1F315, U+1F31C, U+1F31E, U+1F320-1F32C, U+1F336, U+1F378, U+1F=
37D, U+1F382, U+1F393-1F39F, U+1F3A7-1F3A8, U+1F3AC-1F3AF, U+1F3C2, U+1F3C4=
-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F3E0, U+1F3ED, U+1F3F1-1F3F3, U+1F3F5-1F3F7=
, U+1F408, U+1F415, U+1F41F, U+1F426, U+1F43F, U+1F441-1F442, U+1F444, U+1F=
446-1F449, U+1F44C-1F44E, U+1F453, U+1F46A, U+1F47D, U+1F4A3, U+1F4B0, U+1F=
4B3, U+1F4B9, U+1F4BB, U+1F4BF, U+1F4C8-1F4CB, U+1F4D6, U+1F4DA, U+1F4DF, U=
+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F4F7, U+1F4F9-1F4FB, U+1F4FD-1F4FE, U+1F503=
, U+1F507-1F50B, U+1F50D, U+1F512-1F513, U+1F53E-1F54A, U+1F54F-1F5FA, U+1F=
610, U+1F650-1F67F, U+1F687, U+1F68D, U+1F691, U+1F694, U+1F698, U+1F6AD, U=
+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U+1F6C6-1F6CF, U+1F6D3-1F6D7, U+1F6E0-1F6EA=
, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U+1F700-1F7FF, U+1F800-1F80B, U+1F810-1F847=
, U+1F850-1F859, U+1F860-1F887, U+1F890-1F8AD, U+1F8B0-1F8BB, U+1F8C0-1F8C1=
, U+1F900-1F90B, U+1F93B, U+1F946, U+1F984, U+1F996, U+1F9E9, U+1FA00-1FA6F=
, U+1FA70-1FA7C, U+1FA80-1FA89, U+1FA8F-1FAC6, U+1FACE-1FADC, U+1FADF-1FAE9=
, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3OUBGEe.woff2") format("woff2"); unicode-range: U+102-103=
, U+110-111, U+128-129, U+168-169, U+1A0-1A1, U+1AF-1B0, U+300-301, U+303-3=
04, U+308-309, U+323, U+329, U+1EA0-1EF9, U+20AB; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3KUBGEe.woff2") format("woff2"); unicode-range: U+100-2BA=
, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF, U+304, U+308, U+329, U+1D00-1=
DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+=
2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 500; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3yUBA.woff2") format("woff2"); unicode-range: U+0-FF, U+1=
31, U+152-153, U+2BB-2BC, U+2C6, U+2DA, U+2DC, U+304, U+308, U+329, U+2000-=
206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 900; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3GUBGEe.woff2") format("woff2"); unicode-range: U+460-52F=
, U+1C80-1C8A, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 900; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3iUBGEe.woff2") format("woff2"); unicode-range: U+301, U+=
400-45F, U+490-491, U+4B0-4B1, U+2116; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 900; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3CUBGEe.woff2") format("woff2"); unicode-range: U+1F00-1F=
FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 900; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3-UBGEe.woff2") format("woff2"); unicode-range: U+370-377=
, U+37A-37F, U+384-38A, U+38C, U+38E-3A1, U+3A3-3FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 900; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMawCUBGEe.woff2") format("woff2"); unicode-range: U+302-303=
, U+305, U+307-308, U+310, U+312, U+315, U+31A, U+326-327, U+32C, U+32F-330=
, U+332-333, U+338, U+33A, U+346, U+34D, U+391-3A1, U+3A3-3A9, U+3B1-3C9, U=
+3D1, U+3D5-3D6, U+3F0-3F1, U+3F4-3F5, U+2016-2017, U+2034-2038, U+203C, U+=
2040, U+2043, U+2047, U+2050, U+2057, U+205F, U+2070-2071, U+2074-208E, U+2=
090-209C, U+20D0-20DC, U+20E1, U+20E5-20EF, U+2100-2112, U+2114-2115, U+211=
7-2121, U+2123-214F, U+2190, U+2192, U+2194-21AE, U+21B0-21E5, U+21F1-21F2,=
 U+21F4-2211, U+2213-2214, U+2216-22FF, U+2308-230B, U+2310, U+2319, U+231C=
-2321, U+2336-237A, U+237C, U+2395, U+239B-23B7, U+23D0, U+23DC-23E1, U+247=
4-2475, U+25AF, U+25B3, U+25B7, U+25BD, U+25C1, U+25CA, U+25CC, U+25FB, U+2=
66D-266F, U+27C0-27FF, U+2900-2AFF, U+2B0E-2B11, U+2B30-2B4C, U+2BFE, U+303=
0, U+FF5B, U+FF5D, U+1D400-1D7FF, U+1EE00-1EEFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 900; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMaxKUBGEe.woff2") format("woff2"); unicode-range: U+1-C, U+=
E-1F, U+7F-9F, U+20DD-20E0, U+20E2-20E4, U+2150-218F, U+2190, U+2192, U+219=
4-2199, U+21AF, U+21E6-21F0, U+21F3, U+2218-2219, U+2299, U+22C4-22C6, U+23=
00-243F, U+2440-244A, U+2460-24FF, U+25A0-27BF, U+2800-28FF, U+2921-2922, U=
+2981, U+29BF, U+29EB, U+2B00-2BFF, U+4DC0-4DFF, U+FFF9-FFFB, U+10140-1018E=
, U+10190-1019C, U+101A0, U+101D0-101FD, U+102E0-102FB, U+10E60-10E7E, U+1D=
2C0-1D2D3, U+1D2E0-1D37F, U+1F000-1F0FF, U+1F100-1F1AD, U+1F1E6-1F1FF, U+1F=
30D-1F30F, U+1F315, U+1F31C, U+1F31E, U+1F320-1F32C, U+1F336, U+1F378, U+1F=
37D, U+1F382, U+1F393-1F39F, U+1F3A7-1F3A8, U+1F3AC-1F3AF, U+1F3C2, U+1F3C4=
-1F3C6, U+1F3CA-1F3CE, U+1F3D4-1F3E0, U+1F3ED, U+1F3F1-1F3F3, U+1F3F5-1F3F7=
, U+1F408, U+1F415, U+1F41F, U+1F426, U+1F43F, U+1F441-1F442, U+1F444, U+1F=
446-1F449, U+1F44C-1F44E, U+1F453, U+1F46A, U+1F47D, U+1F4A3, U+1F4B0, U+1F=
4B3, U+1F4B9, U+1F4BB, U+1F4BF, U+1F4C8-1F4CB, U+1F4D6, U+1F4DA, U+1F4DF, U=
+1F4E3-1F4E6, U+1F4EA-1F4ED, U+1F4F7, U+1F4F9-1F4FB, U+1F4FD-1F4FE, U+1F503=
, U+1F507-1F50B, U+1F50D, U+1F512-1F513, U+1F53E-1F54A, U+1F54F-1F5FA, U+1F=
610, U+1F650-1F67F, U+1F687, U+1F68D, U+1F691, U+1F694, U+1F698, U+1F6AD, U=
+1F6B2, U+1F6B9-1F6BA, U+1F6BC, U+1F6C6-1F6CF, U+1F6D3-1F6D7, U+1F6E0-1F6EA=
, U+1F6F0-1F6F3, U+1F6F7-1F6FC, U+1F700-1F7FF, U+1F800-1F80B, U+1F810-1F847=
, U+1F850-1F859, U+1F860-1F887, U+1F890-1F8AD, U+1F8B0-1F8BB, U+1F8C0-1F8C1=
, U+1F900-1F90B, U+1F93B, U+1F946, U+1F984, U+1F996, U+1F9E9, U+1FA00-1FA6F=
, U+1FA70-1FA7C, U+1FA80-1FA89, U+1FA8F-1FAC6, U+1FACE-1FADC, U+1FADF-1FAE9=
, U+1FAF0-1FAF8, U+1FB00-1FBFF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 900; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3OUBGEe.woff2") format("woff2"); unicode-range: U+102-103=
, U+110-111, U+128-129, U+168-169, U+1A0-1A1, U+1AF-1B0, U+300-301, U+303-3=
04, U+308-309, U+323, U+329, U+1EA0-1EF9, U+20AB; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 900; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3KUBGEe.woff2") format("woff2"); unicode-range: U+100-2BA=
, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF, U+304, U+308, U+329, U+1D00-1=
DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+=
2C60-2C7F, U+A720-A7FF; }

@font-face { font-family: Roboto; font-style: normal; font-weight: 900; fon=
t-stretch: 100%; src: url("//fonts.gstatic.com/s/roboto/v48/KFO7CnqEu92Fr1M=
E7kSn66aGLdTylUAMa3yUBA.woff2") format("woff2"); unicode-range: U+0-FF, U+1=
31, U+152-153, U+2BB-2BC, U+2C6, U+2DA, U+2DC, U+304, U+308, U+329, U+2000-=
206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/html
Content-ID: <frame-19D67A386EFC80EC50805095F2459A81@mhtml.blink>
Content-Transfer-Encoding: quoted-printable

<html><head><meta http-equiv=3D"Content-Type" content=3D"text/html; charset=
=3DUTF-8"></head><body data-new-gr-c-s-check-loaded=3D"14.1278.0" data-gr-e=
xt-installed=3D""></body><grammarly-desktop-integration data-grammarly-shad=
ow-root=3D"true"><template shadowmode=3D"open"><div aria-label=3D"grammarly=
-integration" role=3D"group" tabindex=3D"-1" class=3D"grammarly-desktop-int=
egration" data-content=3D"{&quot;mode&quot;:&quot;limited&quot;,&quot;isAct=
ive&quot;:false,&quot;isUserDisabled&quot;:false}"></div></template></gramm=
arly-desktop-integration></html>
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN----
Content-Type: text/html
Content-ID: <frame-2E71A776E1BAEF95385BB2E47459EEC4@mhtml.blink>
Content-Transfer-Encoding: quoted-printable

<html><head><meta http-equiv=3D"Content-Type" content=3D"text/html; charset=
=3DUTF-8"></head><body data-new-gr-c-s-check-loaded=3D"14.1278.0" data-gr-e=
xt-installed=3D""></body><grammarly-desktop-integration data-grammarly-shad=
ow-root=3D"true"><template shadowmode=3D"open"><div aria-label=3D"grammarly=
-integration" role=3D"group" tabindex=3D"-1" class=3D"grammarly-desktop-int=
egration" data-content=3D"{&quot;mode&quot;:&quot;limited&quot;,&quot;isAct=
ive&quot;:false,&quot;isUserDisabled&quot;:false}"></div></template></gramm=
arly-desktop-integration></html>
------MultipartBoundary--wek7XXwBNB1NJmCX29prtA9l5zdSuNXg2CvaiVK6EN------
