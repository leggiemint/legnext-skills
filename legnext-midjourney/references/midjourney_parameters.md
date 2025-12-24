# Midjourney V7 Parameters Reference

Complete reference for Midjourney parameters supported by the Legnext API.

## Core Parameters

### --ar (Aspect Ratio)

Controls image dimensions.

| Ratio | Use Case | Feel |
|-------|----------|------|
| `1:1` | Instagram, avatars, square | Balanced |
| `3:2` | Classic photography | Natural |
| `2:3` | Portrait orientation | Vertical |
| `4:5` | Instagram portrait | Tall portrait |
| `16:9` | Widescreen, presentations | Cinematic |
| `21:9` | Ultra-wide panoramic | Epic |
| `9:16` | Mobile wallpapers, stories | Vertical social |

**Note**: Cannot use decimals. Use `--ar 139:100` instead of `--ar 1.39:1`.

**Example**: `--ar 16:9`

---

### --stylize / --s (Stylization)

Controls how much Midjourney applies its artistic interpretation.

| Value | Effect | When to Use |
|-------|--------|-------------|
| `0-50` | Minimal styling, literal interpretation | Technical accuracy, products, photorealism |
| `100` | Default balance | General use (default) |
| `250-500` | Increased artistic interpretation | Creative/artistic work |
| `750-1000` | Maximum artistic expression | Abstract, highly stylized art |

**Example**: `--s 500`

---

### --chaos / --c (Variation)

Controls variation between the four images in a grid.

| Value | Effect |
|-------|--------|
| `0` | Very similar results (default) |
| `25-50` | Moderate variation |
| `75-100` | Maximum variation |

**Use cases**:
- Low chaos: When you know exactly what you want
- High chaos: Exploring different interpretations

**Example**: `--chaos 30`

---

### --weird / --w (Weirdness)

Adds unusual, quirky, or unexpected aesthetics (V7 feature).

| Value | Effect |
|-------|--------|
| `0` | Normal output (default) |
| `250-1000` | Subtle to noticeable oddness |
| `1500-3000` | Maximum weirdness |

**Note**: Can produce unexpected results. Start low and increase gradually.

**Example**: `--weird 500`

---

### --quality / --q (Quality)

Controls generation time and detail level.

| Value | Effect |
|-------|--------|
| `0.25` | Fastest, lowest detail (4x faster, 1/4 cost) |
| `0.5` | Quick, reduced detail (2x faster, 1/2 cost) |
| `1` | Default quality (recommended) |

**Note**: Higher values don't mean "better" — default is usually optimal.

**Example**: `--q 1`

---

### --seed (Reproducibility)

Sets random seed for reproducible results.

**Range**: 0-4294967295

**Use cases**:
- Reproduce specific results
- Create consistent variations
- A/B test prompt changes

**Example**: `--seed 12345`

---

### --no (Negative Prompt)

Excludes specific elements from the image.

```
--no text, watermark, frame
--no people
--no modern elements
```

**Important**:
- Words interpreted separately: `--no red car` = no red AND no car
- Don't use "without" or "don't" in prompt — they don't work
- Limit to essential exclusions (too many can cause conflicts)

---

### --tile (Seamless Pattern)

Creates seamless, tileable patterns.

**Best for**: Textures, patterns, wallpapers, backgrounds

**Example**: `geometric pattern --tile --ar 1:1`

---

## V7-Specific Parameters

### --draft (Draft Mode)

V7-exclusive: 10x faster generation at half cost for quick exploration.

**Use for**:
- Quick iterations and testing
- Exploring prompt concepts
- Finding direction before final quality

**Example**: `a landscape --draft`

**Note**: Remove `--draft` for final high-quality output.

---

### --style raw

Reduces Midjourney's auto-beautification for literal interpretation.

**When to use**:
- Photorealistic images
- Detailed, specific prompts
- Precise control needed
- Product photography

**When NOT to use**:
- Simple prompts (let MJ fill in gaps)
- Highly stylized artistic work

**Example**: `portrait, studio lighting --style raw --ar 2:3`

---

## Reference Parameters

### --sref (Style Reference)

Copies visual style from an image or code.

**Basic usage**:
```
a forest scene --sref https://example.com/image.jpg
```

**SREF codes** (numeric style shortcuts):
```
a portrait --sref 5000
```

**Random style discovery**:
```
a cityscape --sref random
```

**Multiple style references**:
```
a scene --sref URL1 URL2 URL3
```

**Weighted style references**:
```
a scene --sref URL1::2 URL2::1
```
(First style twice as influential)

---

### --sw (Style Weight)

Controls strength of style reference (use with --sref).

| Value | Effect |
|-------|--------|
| `0` | Minimal style influence |
| `100` | Default |
| `500` | Strong influence |
| `1000` | Maximum influence |

**Example**: `--sref [URL] --sw 500`

---

### --cref (Character Reference)

Maintains character appearance consistency across images.

**Basic usage**:
```
a knight in a forest --cref https://example.com/character.jpg
```

**Multiple characters** (blends features):
```
--cref URL1 URL2
```

**Best practice**: Works best with Midjourney-generated characters. Real photos may produce distortions.

---

### --cw (Character Weight)

Controls character reference consistency (use with --cref).

| Value | Effect |
|-------|--------|
| `0` | Face only, different hair/clothes allowed |
| `50` | Moderate consistency |
| `100` | Full consistency: face, hair, AND clothes (default) |

**Example**: `--cref [URL] --cw 100`

---

### --iw (Image Weight)

Controls influence of image prompts.

**Range**: 0-3 (V7), default: 1

**Usage**:
```
[image_URL] a forest scene --iw 2
```

Higher values = image has more influence over the generation.

---

## Multi-Prompts & Weights

### :: (Double Colon)

Separates concepts for independent interpretation.

```
space ship      → "spaceship" (one concept)
space:: ship    → "space" and "ship" (two concepts)
```

### Weighted Prompts

```
forest::3 cabin::1 river::1
```
Forest dominates (3x weight), cabin and river are secondary.

### Negative Weights

```
flowers::-0.5
```
Reduces flowers (similar to --no).

---

## V7 Best Practices

### DO

- Use specific visual details
- Include time of day, weather, specific elements
- Place important elements early in prompt
- Use `--style raw` for photorealism
- Use `--draft` for quick exploration
- Leverage V7's improved coherence for complex scenes

### DON'T (Junk Words to Avoid)

V7 produces high quality by default — these waste tokens:
- ❌ 4k, 6k, 8k, 16k, ultra 4k
- ❌ Octane, unreal, v-ray, lumion
- ❌ HDR, high-resolution
- ❌ Award-winning, photorealistic (unless specifically needed)
- ❌ Masterpiece, highly detailed (redundant in V7)

---

## Recommended Parameter Combinations

**Photorealism**:
```
--style raw --ar 2:3 --s 50
```

**Artistic freedom**:
```
--stylize 500 --chaos 25
```

**Consistent character series**:
```
--cref [URL] --cw 100 --seed [number]
```

**Style exploration**:
```
--sref random --sw 500 --c 50
```

**Quick iteration**:
```
--draft --chaos 50
```

**Seamless textures**:
```
--tile --style raw --ar 1:1
```

---

## V7 Advantages

V7 is Midjourney's most capable model:

- **Superior prompt understanding** — More accurate interpretation of complex prompts
- **Better coherence** — Improved hands, bodies, object relationships
- **Richer textures** — Higher quality details by default
- **Draft Mode** — 10x faster exploration at half cost
- **Enhanced references** — Better --sref and --cref capabilities
- **Personalization** — Applies learned preferences automatically

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Vague prompts | Unpredictable results | Be specific about subject, setting, style |
| Using "don't/without" | Words ignored or reversed | Use `--no` parameter |
| Too many --no items | Contradictory exclusions | Limit to essentials |
| Ignoring --style raw | Over-stylized photos | Use raw for photorealism |
| Not saving seeds | Can't reproduce results | Note seeds for favorites |
| Adding junk words | Wasted tokens | Trust V7's default quality |

---

## Notes

- V7 is the default version (no need to specify `--v 7`)
- Parameters can be combined in any order
- Not all parameters work together (experiment to learn)
- Some parameters may affect generation cost
