#!/usr/bin/env python3
"""Builds the three article-hero options (article-1/2/3.html) from one shared page shell.
Run from homepage-concepts/:  python3 tools/build-article.py
Each output file is self-contained (links only shared/fonts.css), like a.html and b.html."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

KICKER = "Opinion"
HED = "I Was an Airborne Cameraman for Decades. This Is Why We Need to Retire News Choppers"
DEK = ("We are mourning the losses from NBC4 and Telemundo 52’s recent helicopter crash, "
       "yet not asking the question: Is the benefit of in-air reporting worth the risk?")
AUTHOR = "Scott Shulman"
DATE = "September 28, 2026"
READ = "6"
IMG = "img/183785.jpg"
ALT = "A young cameraman grins as he leans out of a yellow Hughes 500C news helicopter with a film camera on his lap."
CAPTION = "Scott Shulman holding a news camera inside a chopper. Photo courtesy of Shulman."

BASE_CSS = r"""
:root {
  --red: #D7261E; --mus: #FFC20E; --nop: #1E7B4A; --dod: #005A9C; --cream: #FFF4DC; --comal: #1B1714;
  --cream-muted: rgba(255, 244, 220, .78); --cream-line: rgba(255, 244, 220, .55); --cream-rule: rgba(255, 244, 220, .18);
  --ink-muted: rgba(27, 23, 20, .68); --ink-rule: rgba(27, 23, 20, .18);
  --col: calc((min(1320px, 100vw - 120px) - 264px) / 12);
  --indent: calc(var(--col) + 24px);
}
*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; background: var(--cream); color: var(--comal); font: 400 16px/1.5 var(--sans); -webkit-font-smoothing: antialiased; }
img { display: block; max-width: 100%; }
a { color: inherit; text-decoration: none; }
h1, h2, h3, p, figure, blockquote { margin: 0; }
:focus-visible { outline: 3px dashed currentColor; outline-offset: 4px; }
.wrap { width: min(1320px, 100% - 120px); margin-inline: auto; }
.grid { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); column-gap: 24px; }

/* ---------- Compact article masthead (the homepage fascia at about half height) ---------- */
.masthead { background: var(--red); color: var(--cream); }
.masthead__in { height: 112px; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; }
.masthead__tag { font: italic 700 15px/1.3 var(--sutro); }
.masthead__tag span { display: block; }
.masthead .logo { width: 320px; margin: -23px 0 -47px; left: 10px; --logo-fill: var(--cream); --logo-line: var(--comal); }
.join-card { justify-self: end; display: block; background: var(--mus); color: var(--comal); padding: 11px 18px 12px; font: 800 20px/1 var(--sutro); transition: background .15s ease; }
.join-card:hover { background: var(--cream); }
.navstrip { background: var(--comal); color: var(--cream); }
.navstrip .wrap { display: flex; justify-content: space-between; align-items: center; height: 56px; }
.navstrip ul { display: flex; gap: 36px; list-style: none; margin: 0; padding: 0; }
.navstrip a { font: 600 15px/1 var(--sans); }
.navstrip a:hover { color: var(--mus); }
.navstrip__util { display: flex; align-items: center; gap: 28px; font: 700 14px/1 var(--sans); }

/* ---------- Shared hero type ---------- */
.kicker { display: block; font: italic 700 20px/1.2 var(--sutro); color: var(--red); }
.hed { font-family: var(--sutro); font-weight: 800; letter-spacing: -0.012em; line-height: 1; text-wrap: balance; }
.dek { font: 700 20px/1.45 var(--serif); }
.cap { font: 500 13px/1.45 var(--sans); color: var(--ink-muted); }
.tools { display: flex; gap: 8px; }
.tools a { font: 600 13px/1 var(--sans); padding: 9px 12px; border: 2px solid currentColor; }
.tools a:hover { background: var(--mus); border-color: var(--mus); color: var(--comal); }
/* 32-point starburst from the homepage guide cards */
.star { position: absolute; width: 150px; height: 150px; transform: rotate(8deg); filter: drop-shadow(5px 5px 0 var(--comal)); z-index: 2; }
.star::before, .star__in { position: absolute; clip-path: var(--burst); }
.star::before { content: ""; inset: 0; background: var(--comal); }
.star__in { inset: 4px; background: var(--mus); display: grid; place-content: center; text-align: center; color: var(--comal); }
.star__in b { font: 900 66px/.86 var(--sutro); letter-spacing: -0.02em; display: block; }
.star__in small { font: italic 700 17px/1 var(--sutro); display: block; margin-top: 4px; }
:root { --burst: polygon(50.0% 0.0%, 58.0% 9.8%, 69.1% 3.8%, 72.8% 15.9%, 85.4% 14.6%, 84.1% 27.2%, 96.2% 30.9%, 90.2% 42.0%, 100.0% 50.0%, 90.2% 58.0%, 96.2% 69.1%, 84.1% 72.8%, 85.4% 85.4%, 72.8% 84.1%, 69.1% 96.2%, 58.0% 90.2%, 50.0% 100.0%, 42.0% 90.2%, 30.9% 96.2%, 27.2% 84.1%, 14.6% 85.4%, 15.9% 72.8%, 3.8% 69.1%, 9.8% 58.0%, 0.0% 50.0%, 9.8% 42.0%, 3.8% 30.9%, 15.9% 27.2%, 14.6% 14.6%, 27.2% 15.9%, 30.9% 3.8%, 42.0% 9.8%); }

/* ---------- Article body + rail ---------- */
.article { padding: 56px 0 104px; }
.body { grid-column: 1 / 9; padding-left: var(--indent); }
.body > * { max-width: 680px; }
.body p { font: 400 20px/1.6 var(--serif); margin-bottom: 1.2em; }
.body p:first-of-type::first-letter { float: left; font: 900 98px/.78 var(--sutro); color: var(--red); padding: 9px 12px 0 0; }
.body blockquote { margin: 44px 0 48px; padding: 4px 0 6px 28px; border-left: 12px solid var(--mus); font: italic 700 31px/1.22 var(--sutro); text-wrap: pretty; }
.rail { grid-column: 10 / 13; display: grid; gap: 44px; align-content: start; }
.ad { height: 250px; display: grid; place-items: center; border: 2px dashed var(--ink-rule); font: 600 12px/1 var(--sans); color: var(--ink-muted); }
.most h2 { font: italic 700 24px/1.1 var(--sutro); color: var(--red); padding-bottom: 12px; border-bottom: 4px solid var(--comal); }
.most ol { list-style: none; margin: 0; padding: 0; counter-reset: n; }
.most li { counter-increment: n; display: grid; grid-template-columns: 34px 1fr; gap: 6px; padding: 16px 0; border-bottom: 1px solid var(--ink-rule); }
.most li::before { content: counter(n); font: 900 30px/.95 var(--sutro); color: var(--red); }
.most a { font: 700 18px/1.18 var(--sutro); }
.most a:hover { text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 3px; }
.most span { display: block; font: 600 13px/1.3 var(--sans); color: var(--ink-muted); margin-top: 6px; }

.foot { background: var(--comal); color: var(--cream-muted); font: 700 13px/1.4 var(--sans); }
.foot .wrap { display: flex; justify-content: space-between; padding: 28px 0; }

@media (max-width: 900px) {
  .wrap { width: calc(100% - 40px); }
  .grid { grid-template-columns: 1fr; row-gap: 40px; }
  .grid > * { grid-column: 1 / -1 !important; }
  .masthead__in { height: auto; grid-template-columns: 1fr auto; padding: 14px 0; }
  .masthead__tag { display: none; }
  .masthead .logo { width: 200px; margin: -14px 0 -29px; left: 0; }
  .join-card { font-size: 16px; padding: 9px 12px; }
  .navstrip ul { gap: 20px; } .navstrip__util { display: none; }
  .article { padding: 36px 0 64px; }
  .body { padding-left: 0; }
  .body p { font-size: 18px; }
  .body blockquote { font-size: 25px; padding-left: 18px; border-left-width: 8px; }
  .hed { font-size: 36px !important; }
  .dek { font-size: 18px; }
}
"""

# ---------------------------------------------------------------- Option 1
HERO_1_CSS = r"""
/* OPTION 1 — HANGING SIGN. The homepage hero, carried over: a full-bleed photo with the mustard sign
   hanging off its bottom edge. A comal strip bolted under the sign carries byline, date and tools,
   and the story starts directly beneath it on the same left edge.
   The sign, story and side column share one grid: the side column (photo caption, then the rail)
   starts beside the sign, so the rail rides up next to the hero instead of waiting for the story. */
:root { --indent: 40px; }
.hero__img { width: 100%; height: 640px; object-fit: cover; object-position: 50% 42%; }
.article { position: relative; z-index: 1; margin-top: -196px; padding-top: 0; }
.hang { align-items: start; row-gap: 48px; }
.sign { grid-column: 1 / 9; grid-row: 1; }
.hang > .body { grid-row: 2; }
.side { grid-column: 10 / 13; grid-row: 1 / 3; align-self: stretch; display: flex; flex-direction: column; gap: 60px; padding-top: 210px; }
.side .rail { flex: 1; }
.sign__face { background: var(--mus); padding: 30px 40px 34px; }
.sign .hed { font-size: 54px; margin-top: 12px; }
.sign .dek { margin-top: 16px; }
.sign__strip { background: var(--comal); color: var(--cream); padding: 14px 40px; display: flex; align-items: center; justify-content: space-between; gap: 24px; }
.sign__by { display: flex; align-items: baseline; gap: 22px; font: 600 14px/1.3 var(--sans); color: var(--cream-muted); }
.sign__by b { font: 700 16px/1.3 var(--sans); color: var(--cream); }
@media (max-width: 900px) {
  .hero__img { height: 320px; }
  .article { margin-top: -56px; }
  .hang { row-gap: 14px; }
  /* one column: sign, caption, story, then the rail */
  .side { display: contents; }
  .side > * { grid-column: 1 / -1; }
  .sign, .hang > .body { grid-row: auto; }
  .hang > .body { margin-top: 34px; }
  .side .rail { order: 1; margin-top: 26px; }
  .sign__face { padding: 22px 20px 24px; }
  .sign__strip { padding: 14px 20px; flex-direction: column; align-items: flex-start; gap: 12px; }
  .sign__by { flex-wrap: wrap; gap: 4px 16px; }
}
"""
HERO_1 = f"""
<div class="hero"><img class="hero__img" src="{IMG}" alt="{ALT}"></div>
"""
SIGN_1 = f"""<header class="sign">
      <div class="sign__face">
        <a class="kicker" href="#">{KICKER}</a>
        <h1 class="hed">{HED}</h1>
        <p class="dek">{DEK}</p>
      </div>
      <div class="sign__strip">
        <p class="sign__by"><b>By {AUTHOR}</b><time datetime="2026-09-28">{DATE}</time><span>{READ} minute read</span></p>
        <p class="tools"><a href="#">Share</a><a href="#">Copy link</a></p>
      </div>
    </header>"""

# ---------------------------------------------------------------- Option 2
HERO_2_CSS = r"""
/* OPTION 2 — PAINTED WALL. The section owns a wall colour (Opinion = Dodger blue; News red, Food mustard,
   Culture nopal). The section name is a small chromatic sign, the headline is lettered straight on the wall,
   and the photo is pinned on like a lobby-card still, hanging off the wall into the page. */
:root { --mount: #FFE8A4; }
.wall { background: var(--dod); color: var(--cream); padding: 60px 0 68px; min-height: 672px; }
.wall .grid { align-items: start; }
.wall__txt { grid-column: 1 / 7; }
.wall__sec { display: inline-block; font-size: 30px; line-height: 1; }
.wall__sec .chroma { --c-fill: var(--red); --c-primary: var(--cream); --c-inline: var(--mus); }
.wall__sec .chroma > span { display: block; }
.wall .hed { font-size: 52px; margin-top: 14px; }
.wall .dek { margin-top: 18px; color: var(--cream); }
.wall__meta { margin-top: 26px; padding-top: 18px; border-top: 2px solid var(--cream-line); display: flex; align-items: center; justify-content: space-between; gap: 20px; }
.wall__by { font: 600 14px/1.4 var(--sans); color: var(--cream-muted); }
.wall__by b { display: block; font: 700 16px/1.3 var(--sans); color: var(--cream); }
/* the card sits up near the top of the wall and 14px past the grid's right edge (Figma: right 46, top 55) */
.still { grid-column: 7 / 13; margin: -5px -14px -260px 14px; position: relative; z-index: 1; }
.still__snap { background: var(--mount); padding: 12px; box-shadow: 12px 12px 0 var(--comal); }
.still__snap img { width: 100%; aspect-ratio: 1 / 1; object-fit: cover; object-position: 78% 50%; }
.still .cap { margin: 34px 12px 0 12px; }
/* the story uses article 1's measure (40px indent, 680 wide), so it starts low enough to clear the
   card's caption; the rail keeps Figma's position, 154px below the wall */
:root { --indent: 40px; }
.article { padding-top: 120px; }
.rail { padding-top: 34px; }
@media (max-width: 900px) {
  .wall { padding: 32px 0 40px; min-height: 0; }
  .wall__sec { font-size: 24px; }
  .wall__meta { flex-direction: column; align-items: flex-start; }
  .still { margin: 0 0 -120px; }
  .still__snap { padding: 8px; box-shadow: 8px 8px 0 var(--comal); }
  .article { padding-top: 130px; }
  .rail { padding-top: 0; }
}
"""
HERO_2 = f"""
<header class="wall">
  <div class="wrap grid">
    <div class="wall__txt">
      <a class="wall__sec" href="#" aria-label="{KICKER}"><span class="chroma chroma--deluxe" data-text="{KICKER.upper()}"><span>{KICKER.upper()}</span></span></a>
      <h1 class="hed">{HED}</h1>
      <p class="dek">{DEK}</p>
      <div class="wall__meta">
        <p class="wall__by"><b>By {AUTHOR}</b><time datetime="2026-09-28">{DATE}</time>, {READ} minute read</p>
        <p class="tools"><a href="#">Share</a><a href="#">Copy link</a></p>
      </div>
    </div>
    <figure class="still">
      <div class="still__snap"><img src="{IMG}" alt="{ALT}"></div>
      <figcaption class="cap">{CAPTION}</figcaption>
    </figure>
  </div>
</header>
"""

# ---------------------------------------------------------------- Option 3
HERO_3_CSS = r"""
/* OPTION 3 — MENU BOARD. The homepage's Latest board becomes the headline: comal board, cream pinstripe,
   chromatic section sign, centred headline, and the byline details set as menu lines with dot leaders.
   The photo is propped against the bottom of the board, with a starburst for the read time. */
.mb { padding-top: 40px; }
.board { background: var(--comal); color: var(--cream); padding: 12px; }
.board__in { border: 1px solid var(--cream-line); padding: 48px 60px 176px; text-align: center; }
.board__sec { display: inline-block; font-size: 60px; line-height: 1; }
.board__sec .chroma { --c-fill: var(--mus); --c-primary: var(--cream); --c-inline: var(--red); }
.board__sec .chroma > span { display: block; }
.board .hed { font-size: 62px; max-width: 17.5em; margin: 20px auto 0; }
.board .dek { max-width: 40em; margin: 20px auto 0; color: var(--cream-muted); }
.lines { list-style: none; margin: 36px auto 0; padding: 0; max-width: 1000px; display: grid; grid-template-columns: repeat(3, 1fr); column-gap: 48px; }
.lines li { display: flex; align-items: baseline; gap: 10px; }
.lines i { font: italic 700 18px/1.2 var(--sutro); color: var(--mus); }
.lines li::after { content: ""; order: 1; flex: 1; border-bottom: 3px dotted var(--cream-line); transform: translateY(-4px); }
.lines b { order: 2; font: 700 16px/1.2 var(--sans); }
.prop { position: relative; z-index: 1; width: calc(var(--col) * 10 + 216px); margin: -128px auto 0; }
.prop img { width: 100%; height: 620px; object-fit: cover; object-position: 50% 45%; }
.prop .star { top: -58px; right: -52px; }
.prop__foot { display: flex; justify-content: space-between; align-items: flex-start; gap: 32px; margin-top: 14px; }
.prop .tools { flex: none; }
@media (max-width: 900px) {
  .mb { padding-top: 20px; }
  .board { padding: 8px; }
  .board__in { padding: 28px 18px 92px; }
  .board__sec { font-size: 40px; }
  .lines { grid-template-columns: 1fr; row-gap: 12px; margin-top: 24px; }
  .prop { width: auto; margin: -64px 12px 0; }
  .prop img { height: 280px; }
  .prop .star { width: 104px; height: 104px; top: -40px; right: -10px; }
  .star__in b { font-size: 44px; } .star__in small { font-size: 13px; }
  .prop__foot { flex-direction: column; gap: 14px; }
}
"""
HERO_3 = f"""
<header class="mb">
  <div class="wrap">
    <div class="board"><div class="board__in">
      <a class="board__sec" href="#" aria-label="{KICKER}"><span class="chroma chroma--deluxe" data-text="{KICKER.upper()}"><span>{KICKER.upper()}</span></span></a>
      <h1 class="hed">{HED}</h1>
      <p class="dek">{DEK}</p>
      <ul class="lines">
        <li><i>Words</i><b>{AUTHOR}</b></li>
        <li><i>Posted</i><b><time datetime="2026-09-28">{DATE}</time></b></li>
        <li><i>Section</i><b>{KICKER}, Media</b></li>
      </ul>
    </div></div>
    <figure class="prop">
      <div class="star" aria-label="{READ} minute read"><div class="star__in"><b>{READ}</b><small>min read</small></div></div>
      <img src="{IMG}" alt="{ALT}">
      <div class="prop__foot">
        <figcaption class="cap">{CAPTION}</figcaption>
        <p class="tools"><a href="#">Share</a><a href="#">Copy link</a></p>
      </div>
    </figure>
  </div>
</header>
"""

BODY = """
<main class="article">
  <div class="wrap grid">
    <div class="body">
      <p>What began as a fatal carjacking on January 3, 1992, at 10:30 a.m., in Central California became the catalyst for change in local television that redefined live coverage of breaking news.</p>
      <p>Although newsrooms have had access to helicopters for years, it wasn’t until Darren Michael Stroh led police on a 300-mile pursuit that the public developed a hunger for live pictures of a dramatic, high-speed chase.</p>
      <p>When they crossed the L.A. County line, local news helicopters picked up the chase, broadcasting pictures live. Stroh eventually slowed to a crawl as he ran out of gas on a Westminster freeway offramp.</p>
      <blockquote>I remember it as though it was yesterday, because I was the cameraman who shot it from the KABC helicopter.</blockquote>
      <p>It didn’t take long before high-speed police pursuits became a staple of local news. Stations regularly interrupt programming to bring viewers these Roman Colosseum-style spectacles delivered right to their home screen.</p>
      <p>As a witness to this man’s death, I became an active participant. It troubles me that my role in bringing the horrific scene to viewers helped fuel a thirst for more.</p>
      <p>When UPS delivered my Golden Mike, I pitched it—three-pointer style—into the trash bin.</p>
    </div>
    <aside class="rail" aria-label="More from L.A. TACO">
      <div class="ad">Advertisement, 300 × 250</div>
      <section class="most">
        <h2>Most read</h2>
        <ol>
          <li><div><a href="article-1.html">I Found the New Best Carne Asada Taco in L.A., and It’s in a Parking Lot in Silver Lake</a><span>By Javier Cabral</span></div></li>
          <li><div><a href="article-1.html">After 34 Years, Hollywood’s Iconic Cactus Taquería #1 Is Being Forced to Close This Sunday</a><span>By Jake Hook</span></div></li>
          <li><div><a href="article-1.html">Brick-and-Mortar Restaurants Need to Stop Blaming Street Vendors</a><span>By Jake Hook</span></div></li>
          <li><div><a href="article-1.html">L.A.’s Most Exclusive Poke Comes From a Car Trunk and Sells Out in Minutes</a><span>By Marina Watanabe</span></div></li>
        </ol>
      </section>
    </aside>
  </div>
</main>
<footer class="foot"><div class="wrap"><span>© 2026 L.A. TACO. Independent and member supported.</span><span>James Beard Award, 2024.</span></div></footer>
"""

SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>L.A. TACO — Article hero, option {n}: {name}</title>
<link rel="stylesheet" href="shared/fonts.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,700&display=swap">
<!-- Generated by tools/build-article.py. Edit the generator, not this file. -->
<style>{base}{hero_css}</style>
</head>
<body>
<header class="masthead">
  <div class="wrap masthead__in">
    <p class="masthead__tag"><span>Independent.</span> <span>Member supported.</span></p>
    <a class="logo" href="b.html" aria-label="L.A. TACO home"></a>
    <a class="join-card" href="#">Join L.A. TACO</a>
  </div>
</header>
<nav class="navstrip" aria-label="Main">
  <div class="wrap">
    <ul><li><a href="#">News</a></li><li><a href="#">Food &amp; Tacos</a></li><li><a href="#">Explore L.A.</a></li><li><a href="#">Shop</a></li></ul>
    <div class="navstrip__util"><a href="#">Search</a><a href="#">Member log in</a><time datetime="2026-10-10">Saturday, October 10</time></div>
  </div>
</nav>
{hero}{body}
<script src="shared/switcher.js" defer></script>
<script src="shared/comments.js" defer></script>
</body>
</html>
"""

# ---------------------------------------------------------------- Option 1, full page
# The whole story from content/articles/183785.json, plus everything below the body.
import html, json, re
ART = json.loads((ROOT.parent / "content/articles/183785.json").read_text())
INLINE = {4: ("img/article/chopper-bw.jpg", "A young cameraman sits in the open door of a news helicopter.", "Photo courtesy of Scott Shulman."),
          19: ("img/article/chopper-2.jpg", "Shulman rides with a film camera in the open bubble of a small helicopter, mountains behind.", "Photo courtesy of Scott Shulman.")}
# WordPress repeats a nearby paragraph as each pull quote. Drop the first quote (it would sit right under its own paragraph)
# and the one-line paragraph that the red sign quote restates word for word.
SKIP = {7, 15}
MEMBER_AFTER = 12   # the member prompt goes in after this block

def block(i, b):
    t = html.escape(b.get("text", ""), quote=False)
    if b["type"] == "p":
        return f"<p>{t}</p>"
    if b["type"] == "blockquote":
        # Option A from pullquotes.html: a chromatic Sutro Deluxe quote mark hangs into the margin, no box
        by = html.escape(ART["byline"], quote=False)
        return ('<figure class="pq"><span class="pq__mark" aria-hidden="true"><span class="chroma chroma--deluxe" data-text="“"><span>“</span></span></span>'
                f'<blockquote><p>{t}</p></blockquote><figcaption>{by}</figcaption></figure>')
    if b["type"] == "image":
        src, alt, cap = INLINE[i]
        return f'<figure class="inline"><img src="{src}" alt="{alt}" loading="lazy"><figcaption class="cap">{cap}</figcaption></figure>'
    return ""

MEMBER = """
<aside class="member" aria-label="Membership">
  <div class="member__in">
    <p class="kicker">Members only, free today</p>
    <h2 class="member__hed">Stories like this one cost money to report. Our members cover it.</h2>
    <p class="member__dek">L.A. TACO is independent and runs on readers. Join for $59 a year and you get every story, the members-only newsletters, and a discount at our partner taquerías.</p>
    <p class="member__row"><a class="btn" href="#">Join for $59 a year</a><a class="member__link" href="#">See the Loyal tier, $99</a></p>
  </div>
</aside>
"""

body_parts = []
for i, b in enumerate(ART["body"]):
    if i in SKIP:
        continue
    body_parts.append(block(i, b))
    if i == MEMBER_AFTER:
        body_parts.append(MEMBER)
STORY = "\n      ".join(body_parts)

FULL_CSS = r"""
/* ---------- Full article page (option 1) ---------- */
.body p:first-of-type::first-letter { float: none; font: inherit; color: inherit; padding: 0; }
.body > p:first-child::first-letter { float: left; font: 900 98px/.78 var(--sutro); color: var(--red); padding: 9px 12px 0 0; }
/* inline photos break out of the 40px indent to the full story column */
.body .inline { max-width: none; margin: 48px 0 48px calc(-1 * var(--indent)); }
.inline img { width: 100%; aspect-ratio: 3 / 2; object-fit: cover; }
.inline .cap { margin-top: 10px; }
/* pull quotes: a chromatic quote mark (68 x 51 ink) sits on the measure's left edge above the quote.
   left/top offset the glyph's side bearing and ascent so the ink lands at 0, 7px, as in Figma. */
.body .pq { position: relative; margin: 24px 0 52px; padding-top: 84px; }
.pq__mark { position: absolute; left: -5px; top: -12px; font-size: 118px; line-height: 1; --c-fill: var(--mus); --c-primary: var(--red); --c-inline: var(--cream); }
.pq__mark .chroma > span { display: block; }
.body .pq blockquote { margin: 0; padding: 0; border: 0; }
.body .pq blockquote p { font: italic 700 40px/1.16 var(--sutro); letter-spacing: -0.008em; margin: 0; text-wrap: balance; }
.body .pq figcaption { margin-top: 18px; font: 600 14px/1.3 var(--sans); color: var(--ink-muted); display: flex; align-items: center; gap: 12px; }
.body .pq figcaption::before { content: ""; width: 44px; height: 4px; background: var(--comal); }
/* member prompt: the homepage's comal board, in the body column */
.body .member { max-width: none; margin: 48px 0 48px calc(-1 * var(--indent)); background: var(--comal); color: var(--cream); padding: 12px; }
.member__in { border: 1px solid var(--cream-line); padding: 32px 40px 36px; }
.member .kicker { color: var(--mus); font-size: 18px; }
.body .member__hed { font: 800 34px/1.05 var(--sutro); letter-spacing: -0.005em; margin-top: 10px; text-wrap: balance; }
.body .member__dek { font: 700 18px/1.5 var(--serif); color: var(--cream-muted); margin: 12px 0 0; max-width: 560px; }
.body .member__row { display: flex; align-items: center; gap: 24px; margin: 22px 0 0; font: inherit; }
.btn { display: inline-block; font: 600 15px/1 var(--sans); padding: 14px 20px; background: var(--mus); color: var(--comal); transition: background .15s ease; }
.btn:hover { background: var(--cream); }
.member__link { font: 600 15px/1.2 var(--sans); text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 5px; }
/* end of story: filed under + share, then the author */
.body .endmatter { margin-top: 48px; padding-top: 22px; border-top: 4px solid var(--comal); display: flex; justify-content: space-between; align-items: center; gap: 24px; }
.filed { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; font: italic 700 18px/1 var(--sutro); color: var(--red); }
.filed a { font: 600 13px/1 var(--sans); color: var(--comal); background: var(--mus); padding: 8px 11px; }
.filed a:hover { background: var(--comal); color: var(--cream); }
.endmatter .tools a { border-color: var(--comal); }
.body .author { margin-top: 36px; display: grid; grid-template-columns: 96px 1fr; gap: 24px; align-items: start; }
.author img { width: 96px; height: 96px; object-fit: cover; border: 3px solid var(--comal); }
.body .author p { font: 400 17px/1.5 var(--serif); margin: 6px 0 0; }
.author__name { font: 800 26px/1.1 var(--sutro); }
.author__more { display: inline-block; margin-top: 10px; font: 600 14px/1.2 var(--sans); text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 4px; }
/* the rail's ad follows the reader down the long story */
.rail .ad--sticky { position: sticky; top: 24px; height: 600px; }
.rail { align-self: stretch; grid-template-rows: auto auto 1fr; }

/* ---------- Keep reading: a red fascia + three shop-window stories, as on the homepage ---------- */
.more { background: var(--red); }
.more__sign { display: flex; flex-direction: column; align-items: center; min-height: 220px; padding: 44px 0 38px; font-size: 96px; line-height: 1; }
.more__sign .chroma { --c-fill: var(--mus); --c-primary: var(--comal); --c-inline: var(--cream); }
.more__sign .chroma > span { display: block; }
.more__body { background: var(--cream); padding: 56px 0 96px; }
.story .window { margin: 0 0 24px; background: var(--comal); }
.story .window img { width: 100%; height: 250px; object-fit: cover; }
.story .kicker { font-size: 18px; margin-bottom: 8px; }
.story .hed { font-size: 26px; line-height: 1.04; }
.story .by { font: 700 14px/1.4 var(--sans); margin-top: 8px; }
.story a:hover .hed { text-decoration: underline; text-decoration-thickness: 3px; text-underline-offset: .12em; }
.more__body .story { grid-column: span 4; }

/* ---------- Full footer from homepage B ---------- */
.foot { color: var(--cream); font: inherit; }
.foot .wrap { display: block; padding: 0; }  /* undo the short placeholder footer used by options 2 and 3 */
.foot .foot__in { padding: 88px 0 56px; }  /* .foot .wrap above zeroes padding, so this needs the same specificity */
.foot__top { align-items: start; }
.foot__mark { grid-column: 1 / 4; }
.stacked { display: block; width: 260px; aspect-ratio: 1200 / 799; background: var(--cream); -webkit-mask: url(img/logo-stacked.png) center / contain no-repeat; mask: url(img/logo-stacked.png) center / contain no-repeat; }
.foot__mark p { font: italic 700 18px/1.3 var(--sutro); margin-top: 22px; max-width: 240px; }
.foot__cols { grid-column: 4 / 8; display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.foot__cols h3, .foot__news h3 { font: 700 20px/1.2 var(--sutro); color: var(--mus); margin-bottom: 9px; }
.foot__news h3 { margin-bottom: 12px; }
.foot__cols ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 9px; font: 700 15px/1.3 var(--sans); }
.foot__cols a:hover, .foot__mag a:hover { color: var(--mus); text-decoration: underline; text-underline-offset: 4px; }
.foot__news { grid-column: 8 / 13; }
.foot__mag { display: flex; gap: 20px; align-items: center; margin-bottom: 36px; }
.foot__mag img { width: 104px; height: 104px; object-fit: cover; }
.foot__mag b { display: block; font: 800 24px/1.1 var(--sutro); }
.foot__mag span { display: block; font: 700 15px/1.45 var(--serif); color: var(--cream-muted); margin-top: 4px; }
.foot__mag a { display: inline-block; margin-top: 8px; font: 600 14px/1 var(--sans); text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 4px; }
.nl label { display: block; font: 700 15px/1.45 var(--serif); color: var(--cream-muted); margin-bottom: 12px; }
.nl__row { display: flex; }
.nl input { flex: 1; min-width: 0; font: 700 16px/1 var(--sans); padding: 14px 16px; border: 2px solid var(--cream); background: var(--comal); color: var(--cream); border-radius: 0; }
.nl input::placeholder { color: var(--cream-muted); }
.nl button { font: 600 15px/1 var(--sans); padding: 0 22px; background: var(--mus); color: var(--comal); border: 2px solid var(--cream); border-left: 0; cursor: pointer; border-radius: 0; }
.nl button:hover { background: var(--cream); }
.foot__base { margin-top: 72px; padding-top: 22px; border-top: 1px solid var(--cream-rule); display: flex; justify-content: space-between; font: 700 13px/1.4 var(--sans); color: var(--cream-muted); }

@media (max-width: 900px) {
  .body .inline, .body .member { margin-left: 0; }
  .body .pq blockquote p { font-size: 28px; }
  .member__in { padding: 24px 20px 26px; }
  .body .member__hed { font-size: 27px; }
  .body .member__row { flex-direction: column; align-items: flex-start; gap: 16px; }
  .body .endmatter { flex-direction: column; align-items: flex-start; }
  .body .author { grid-template-columns: 72px 1fr; gap: 16px; }
  .author img { width: 72px; height: 72px; }
  .rail .ad--sticky { position: static; }
  .more__sign { font-size: 13vw; min-height: 0; padding: 28px 0 24px; }
  .more__sign .chroma { white-space: normal; text-align: center; }
  .more__body { padding: 40px 0 64px; }
  .foot__cols { grid-template-columns: 1fr 1fr; }
  .foot__base { flex-direction: column; gap: 6px; }
}
"""

FULL_BODY = f"""
<main class="article">
  <div class="hang wrap grid">
    {SIGN_1}
    <div class="side">
      <p class="cap">{CAPTION}</p>
      <aside class="rail" aria-label="More from L.A. TACO">
        <div class="ad">Advertisement, 300 × 250</div>
        <section class="most">
          <h2>Most read</h2>
          <ol>
            <li><div><a href="article-1.html">I Found the New Best Carne Asada Taco in L.A., and It’s in a Parking Lot in Silver Lake</a><span>By Javier Cabral</span></div></li>
            <li><div><a href="article-1.html">After 34 Years, Hollywood’s Iconic Cactus Taquería #1 Is Being Forced to Close This Sunday</a><span>By Jake Hook</span></div></li>
            <li><div><a href="article-1.html">Data Shows City of L.A. as Extreme Hotspot for ICE Arrests</a><span>By Memo Torres</span></div></li>
            <li><div><a href="article-1.html">L.A.’s Most Exclusive Poke Comes From a Car Trunk and Sells Out in Minutes</a><span>By Marina Watanabe</span></div></li>
          </ol>
        </section>
        <div><div class="ad ad--sticky">Advertisement, 300 × 600</div></div>
      </aside>
    </div>
    <article class="body">
      {STORY}
      <div class="endmatter">
        <p class="filed">Filed under <a href="#">Opinion</a><a href="#">Media</a><a href="#">Los Angeles</a></p>
        <p class="tools"><a href="#">Share</a><a href="#">Copy link</a></p>
      </div>
      <div class="author">
        <img src="img/article/scott-shulman.jpg" alt="Scott Shulman">
        <div>
          <a class="author__name" href="#">Scott Shulman</a>
          <p>Shulman spent decades as a news cameraman in Los Angeles, including years in KABC’s helicopter.</p>
          <a class="author__more" href="#">More from Scott Shulman</a>
        </div>
      </div>
    </article>
  </div>
</main>

<section class="more" aria-labelledby="more-h">
  <div class="wrap"><h2 class="more__sign" id="more-h"><span class="chroma chroma--deluxe" data-text="MORE OPINION"><span>MORE OPINION</span></span></h2></div>
  <div class="more__body">
    <div class="wrap grid">
      <article class="story"><a href="article-1.html">
        <figure class="window"><img src="img/lead.jpg" alt="A taquero shaves meat from a glowing trompo at a street stand at night." style="object-position: 50% 70%"></figure>
        <span class="kicker">Food, opinion</span>
        <h3 class="hed">Brick-and-Mortar Restaurants Need to Stop Blaming Street Vendors</h3>
        <p class="by">By Jake Hook</p>
      </a></article>
      <article class="story"><a href="article-1.html">
        <figure class="window"><img src="img/183710.jpg" alt="A street in Long Beach."></figure>
        <span class="kicker">Opinion</span>
        <h3 class="hed">Long Beach’s ‘Vibe City’ Rebrand Is a Slap in the Face to Locals Living in Poverty</h3>
        <p class="by">By Myriam Gurba</p>
      </a></article>
      <article class="story"><a href="article-1.html">
        <figure class="window"><img src="img/183598.jpg" alt="Illustrated portraits of Karen Bass and Nithya Raman in blue and yellow."></figure>
        <span class="kicker">Politics</span>
        <h3 class="hed">The No-BS Guide to What Karen Bass and Nithya Raman Plan to Do If They’re Elected</h3>
        <p class="by">By Sam Ribakoff</p>
      </a></article>
    </div>
  </div>
</section>
"""

# footer markup is lifted from b.html so the two stay in step
B = (ROOT / "b.html").read_text()
FOOTER = re.search(r'<footer class="foot pin">.*?</footer>', B, re.S).group(0).replace('class="foot pin"', 'class="foot"')

for n, name, css, hero in [(1, "Hanging sign", HERO_1_CSS, HERO_1), (2, "Painted wall", HERO_2_CSS, HERO_2), (3, "Menu board", HERO_3_CSS, HERO_3)]:
    out = ROOT / f"article-{n}.html"
    if n == 1:
        page = SHELL.format(n=n, name=name, base=BASE_CSS, hero_css=css + FULL_CSS, hero=hero, body=FULL_BODY + FOOTER)
    else:
        page = SHELL.format(n=n, name=name, base=BASE_CSS, hero_css=css, hero=hero, body=BODY)
    out.write_text(page)
    print("wrote", out.name)
