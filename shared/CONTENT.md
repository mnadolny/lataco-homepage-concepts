# LA Taco homepage concepts — shared content + brand facts

All three concepts use the SAME stories so the client compares design, not content.
Images live in `../img/` (relative to a concept file in `homepage-concepts/`, use `img/...`).

## Brand facts
- L.A. TACO: independent, reader-funded L.A. news + culture publication. Tagline: "Celebrating the taco lifestyle in Los Angeles." Started as a taco + street-art blog (2006), James Beard award 2024. Voice: blunt, irreverent, fiercely local.
- Membership: **Local** $59/yr ($4.92/mo) — "the membership that keeps the lights on". **Loyal** $99/yr ($8.25/mo) — adds a merch pick (shirt, hat, zine). All members: every story, two members-only newsletters, free entry to Taco Madness, a member card good for free tacos at partner spots (Mariscos Jalisco, Guerrilla Tacos, Carnitas El Momo), 20% off merch.
- Franchises: **Taco Madness** (reader-voted bracket of taquerías since 2009 + April festival), **L.A. TACO Guides** (ranked lists — the count is the hook), **Sunday Taquitos** (weekly comic by Pulitzer finalist Ivan Ehlers), **ICE Watch** newsletter, **Weekend Eats**, Photo Essay, L.A. TACO Magazine (print, Summer 2026, Vol. 2 Issue 1, 48 pages, 11×11 in, $35, includes a sticker and the L.A. TACO POST tabloid).
- Nav (client): News, Food & Tacos, Explore L.A., Shop. Utility: About, Member log in. CTA: Join L.A. TACO.
- Today's date for the edition line: Saturday, October 10, 2026.

## Brand assets (img/)
- `logo-fill.png` + `logo-line.png` — the horizontal Tuscan wood-type logo split into two masks (1200×447). Use `shared/fonts.css` `.logo` class with `--logo-fill` / `--logo-line` to color it any two colors. `logo-solid.png` = one-piece silhouette mask. `logo-cream.png` = the original cream+black raster.
- `logo-stacked.png` — stacked "L.A. / TACO" hand-drawn logo, white on transparent (1200×799). Use as a CSS mask to color it.
- `palm.png` — the palm tree + "L.A. TACO" sign illustration (cream/black, transparent, 1044×1507).

## Type (see shared/fonts.css)
- `var(--sutro)` — Sutro by Jim Parkinson: 300 Light, 500 Medium, 700 Bold, 800 ExtraBold, 900 Heavy, all with italics. Headlines.
- Chromatic layers (stack in same position, one color each) via `.chroma.chroma--shaded` (Fill + Primary-with-shade) and `.chroma.chroma--deluxe` (Fill + Primary + Inline). Works best ALL CAPS at 60px+. Font families also directly usable: 'Shaded Primary', 'Shaded Fill', 'Deluxe Primary', 'Deluxe Fill', 'Deluxe Inline', 'Open Fill', and the family "Sutro Open".
- `var(--serif)` Source Serif 4 — deks, body. `var(--sans)` IBM Plex Sans — UI, bylines, meta. `var(--sans-cond)` IBM Plex Sans Condensed — labels where tight.

## Stories

### Lead
- **Brick-and-Mortar Restaurants Need to Stop Blaming Street Vendors** — Food / Opinion — by Jake Hook. Dek: "The city has room for both. What's missing is real support for the people who feed it." Image `lead.jpg` (1600×1067, taquero shaving a trompo at night — dark, dramatic).

### Latest (news)
1. **I Was an Airborne Cameraman for Decades. This Is Why We Need to Retire News Choppers** — Opinion — Scott Shulman — 2h ago — `183785.jpg` (helicopter, yellow)
2. **Data Shows City of L.A. as Extreme Hotspot for ICE Arrests** — ICE Watch — Memo Torres — 4h — `183737.jpg` (agents making arrest). Dek: "L.A. TACO broke down the nearly 4,000 logged apprehensions in L.A. County by neighborhood and city."
3. **The U.S. Government Quietly Just Made It Legal to Go Through Your Phone at the Border** — News — Izzy Ramirez — `183746.jpg` (border landscape)
4. **The No-BS Guide to What Karen Bass and Nithya Raman Plan to Do If They're Elected** — Politics — Sam Ribakoff — `183598.jpg` (illustration, blue/yellow portraits)
5. **Long Beach's 'Vibe City' Rebrand Is a Slap in the Face to Locals Living in Poverty** — Opinion — Myriam Gurba — `183710.jpg`

### Food & Tacos
- **I Found the New Best Carne Asada Taco in L.A., and It's in a Parking Lot in Silver Lake** — Tacos — Javier Cabral — `180786.jpg` (taco in red paper boat, dark). Dek: "Even the beef tallow-enriched, organic wheat flour tortilla alone is worth a visit."
- **They Had Degrees, Careers and Dreams. Then They Came Home to Grow the Family Taquería** — Tacos — Karina Soriano — `183203.jpg` (three people in white shirts in front of painted taquería sign). Dek: "A generation raised in mesquite smoke is choosing legacy over escape."
- **Palestinian-and-Syrian Street Food With Handmade Pita and Mana'eesh in Silver Lake** — Weekend Eats — Hadley Tomicki — `183752.jpg`
- **L.A.'s Most Exclusive Poke Comes From a Car Trunk and Sells Out in Minutes** — Food — Marina Watanabe — `182892.jpg` (overhead poke bowls)
- **Beijing's Crispy Bing Burgers Are Coming to the SGV This Week** — Food — Hadley Tomicki — `183160.jpg` (overhead pastries, dark)
- **After 34 Years, Hollywood's Iconic Cactus Taquería #1 Is Being Forced to Close This Sunday** — Tacos — Jake Hook — `181136.jpg` (neon taquería sign at night)
- **Tijuana's Prized 'Tacos Varios' Enter East L.A.** — Food — Hadley Tomicki — `182907.jpg`
- **He Makes Some of the 'Best Pizza in America.' His New Side-Hustle? 900 Sourdough Bagels Each Weekend** — Food — Javier Cabral — `183557.jpg`
- Extra taco photography (high-res, from the carne asada guide): `asada-01.jpg`, `asada-03.jpg`, `asada-08.jpg`, `asada-13.jpg`, `asada-18.jpg`, `tacos.jpg` (1600, carne asada tacos on green tablecloth with blue-white paper)

### Guides (ranked lists — the count is real information)
- **The 19 Best Carne Asada Tacos in L.A.** — Javier Cabral & L.A. TACO Staff — `131745.jpg` / `tacos.jpg`. Dek: "You could argue that asada is the official taco of Los Angeles. Exhibit A: these 19 tacos, ranked."
- **The 21 Best Street Kebabs in L.A.** — `182778.jpg` (skewers over smoke)
- **L.A.'s 27 Best Record Shops** — Hadley Tomicki — `173124.jpg` (mural)
- **L.A.'s 29 Best Independent Bookshops** — `170528.jpg` (1984 book in sand)
- **The 17 Best Steakhouses in Los Angeles, Ranked** — `183034.jpg`
- **The Seven Best Tacos in Lynwood, Ranked** — Karina Soriano — `180868.jpg`
- **We Mapped All 64 TACO MADNESS Competitors, From Palms to Pomona** — Javier Cabral — `178114.jpg` (map)

### Culture / Explore L.A.
- **Photo Essay: East Hollywood Gay Club Famous for Its "Vaquero Nights" Turns 35** — Sean Maung, Julianne Le — `182414.jpg` (three men in cowboy hats)
- **The Unlikely Sisterhood of Women Skaters in Santa Monica** — Julianne Le — `182003.jpg` (skaters under palms, blue sky, wide)
- **You See His Murals Across L.A. and at Your Favorite Restaurants. Now Meet the Painter** — Karina Soriano — `182537.jpg`
- **This 21-Year-Old Bagpiper Plays Through Tear Gas to 'Fire Up' Anti-ICE Protesters** — Julianne Le — `176038.jpg`
- **These Hacienda Heights Latino Punk Phenoms Are Under 20** — Javier Cabral — `172738.jpg` (punk show, flash)
- **The East L.A. Artist Behind 'Homeboy Beautiful' Magazine** — Izzy Ramirez — `182568.jpg`
- **The First Native Powwow Comes to Cal State LA After 79 Years** — Shylah Featherstone — `181851.jpg` (colorful regalia)
- **Seven Dancers Proving L.A.'s Burlesque Scene Is the Best in the World** — `182300.jpg` (performer in red gown in front of the Hollywood sign)
- **'60 Miles East': A New Exhibit Celebrates Inland Empire Punk** — `172756.jpg` (flyer wall)
- **Are the Lakers Still L.A.'s Team?** — `182533.jpg` (fans in the street at night)
- Neighborhood feature: **This is how L.A. celebrates.** — "Mexican Independence Day, through the lens of L.A.'s lowrider community." — Erwin Recinos — `lowrider.jpg` (1600, lowrider hopping on palm-lined street, blue sky)
- Neighborhood photos (2560 wide, food shot in each hood): `hood-boyle-heights.jpg`, `hood-hollywood.jpg`, `hood-long-beach.jpg`, `hood-highland-park.jpg`, `hood-east-la.jpg` (street scene)

### House / extras
- **Sunday Taquitos #33: One of the Good Ones** — Ivan Ehlers — `183639.jpg` (b/w single-panel comic, portrait)
- **L.A. TACO Goes Print!** — "Did we just start a tabloid war? Let's hope so." — `183183.jpg` (L.A. TACO POST tabloid cover, red/black)
- **Try L.A. TACO's New Beer at Our Long Beach Release Party** — `183610.jpg` (beer cans)
- `magazine.jpg` — L.A. TACO Magazine cover (1200 square)
- `182539.jpg` — L.A. TACO zine release party flyer (red, punk)

Do not use any other posts (several in the archive are explicit and deliberately excluded).
