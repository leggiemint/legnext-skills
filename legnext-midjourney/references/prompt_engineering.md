# Midjourney V7 Prompt Engineering Guide

Professional guide for crafting effective Midjourney prompts through the Legnext API.

## Core Principle

**Be specific about what you want to SEE, not abstract concepts.**

Short, specific prompts work best. V7 produces high quality by default — focus on visual details, not quality keywords.

---

## The 7-Element Framework

Build complete, systematic prompts using these elements:

| Element | Question | Examples |
|---------|----------|----------|
| **Subject** | Who/what is in the image? | A weathered fisherman, a cyberpunk samurai, vintage bicycle |
| **Medium** | What art form? | Oil painting, photograph, 3D render, digital illustration |
| **Environment** | Where is this? | Stormy harbor, neon-lit alley, misty forest, cobblestone street |
| **Lighting** | How is it lit? | Golden hour, dramatic backlighting, soft diffused, studio lighting |
| **Color** | What palette? | Muted blues, warm earth tones, high contrast, pastel colors |
| **Mood** | What feeling? | Melancholic, triumphant, eerie, peaceful, energetic |
| **Composition** | How is it framed? | Rule of thirds, centered, wide shot, close-up |

**Example**:
```
A weathered fisherman, oil painting, stormy harbor at dawn,
dramatic backlighting, muted blues and grays, melancholic,
rule of thirds composition --ar 3:2
```

**Not all elements are required** — use what's relevant for your image.

---

## Quick Prompt Structure

```
[Subject] [Description] [Environment] [Lighting] [Style] [Parameters]
```

**Example**:
```
30-year-old woman with freckles, wearing cream linen shirt,
sun-drenched cafe, soft window light, Canon EOS R5, 85mm f/1.8,
Kodak Portra 400 --ar 2:3 --style raw
```

---

## Prompt Types & Templates

### Photorealistic Portrait

```
[Age] [ethnicity if relevant] [gender] [action/pose], [clothing],
[environment], [lighting type], [camera] [lens] [aperture],
[film stock if desired] --ar [ratio] --style raw
```

**Example**:
```
45-year-old man with gray beard, wearing wool sweater, seated in rustic cabin,
soft window light mixed with warm firelight, Hasselblad 80mm f/2.8,
Kodak Portra 400 --ar 4:5 --style raw
```

### Illustration/Art

```
[Subject] in the style of [artist/medium], [environment],
[lighting], [mood] --ar [ratio] --stylize [value]
```

**Example**:
```
A mystical forest spirit, digital illustration in the style of Loish,
enchanted woodland, dappled sunlight, ethereal and mysterious
--ar 2:3 --stylize 250
```

### Product Photography

```
[Product] on [surface], [background], [lighting setup],
professional product photography --ar [ratio] --style raw
```

**Example**:
```
Luxury watch on black marble surface, dark gradient background,
dramatic side lighting with subtle rim light, professional product photography
--ar 1:1 --style raw
```

### Landscape

```
[Scene], [time of day], [weather/atmosphere], [mood],
[focal length] lens --ar [ratio]
```

**Example**:
```
Misty mountain valley with winding river, blue hour, low clouds clinging to peaks,
ethereal and mysterious, 24mm wide angle, Fujifilm Velvia 100 --ar 16:9
```

### Character Design

```
[Character description], [pose], [outfit], [art style],
full body shot --ar [ratio]
```

**Example**:
```
Fierce warrior princess in dynamic action pose, detailed ornate armor,
cherry blossom battlefield, dramatic lighting --ar 2:3
```

---

## V7 Best Practices

### DO

✓ Be specific with visual details
✓ Use natural language clearly
✓ Include time of day, weather, specific elements
✓ Place important elements early in prompt
✓ Use `--style raw` for photorealism and precise control
✓ Use `--draft` for quick exploration iterations
✓ Leverage V7's improved coherence for complex scenes

### DON'T (Junk Words to Avoid)

V7 produces high quality by default — **avoid these wasteful tokens**:

❌ 4k, 6k, 8k, 16k, ultra 4k, high resolution, HDR
❌ Octane, unreal engine, v-ray, lumion
❌ Award-winning, photorealistic (unless specifically needed)
❌ Masterpiece, highly detailed, intricate details (redundant in V7)
❌ Ultra realistic, trending on artstation (unnecessary)

**Trust V7's default quality** — add meaningful visual details instead.

---

## Advanced Techniques

### Style Reference (--sref)

Copy visual style from images or codes:

```
a mountain landscape --sref https://example.com/image.jpg
```

**SREF codes**:
```
a portrait --sref 5000
```

**Random styles**:
```
a cityscape --sref random
```

**Multiple weighted references**:
```
a scene --sref URL1::2 URL2::1 --sw 500
```

See `midjourney_parameters.md` for full --sref details.

### Character Reference (--cref)

Maintain character consistency:

```
a knight in a forest --cref https://example.com/character.jpg --cw 100
```

**Best with** Midjourney-generated characters. Real photos may distort.

### Multi-Prompts & Weights

Separate concepts with `::`

```
space ship      → "spaceship" (one concept)
space:: ship    → "space" and "ship" (two concepts)
```

**Weighted prompts**:
```
forest::3 cabin::1 river::1
```

**Negative weights** (like --no):
```
flowers::-0.5
```

---

## Effective Descriptors

### Lighting
- Golden hour, blue hour, sunset, sunrise
- Studio lighting, Rembrandt lighting, clamshell lighting
- Backlit, rim lighting, volumetric lighting
- Soft diffused, harsh sunlight, dappled light
- Cinematic lighting, chiaroscuro, neon lighting

### Mood/Atmosphere
- Cozy, dramatic, peaceful, chaotic
- Mysterious, ethereal, gritty, serene
- Melancholic, triumphant, eerie, energetic

### Camera & Lens
- 14mm (extreme wide), 24mm (wide), 35mm (versatile)
- 50mm (natural), 85mm (portrait), 135mm (telephoto), 200mm+ (compressed)
- Wide aperture (f/1.4, f/1.8), shallow depth of field, bokeh
- Sharp focus, rule of thirds, centered composition

### Film Stocks
- Kodak Portra 400/800 (natural skin tones, soft contrast)
- Kodak Ektar 100 (vivid colors, punchy)
- Fujifilm Velvia 100 (extremely vivid, saturated greens)
- Cinestill 800T (tungsten-balanced, halation, cinematic)
- Kodak Tri-X 400 (black & white, classic grain, high contrast)

See `photography.md` for comprehensive camera/lighting terminology.

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Vague prompts | Unpredictable results | Be specific: subject, setting, style, lighting |
| Using "don't/without" | Words ignored/reversed | Use `--no` parameter |
| Overly long prompts | Confused output | Keep under ~40 words, use `/shorten` command |
| Adding junk words | Wasted tokens | Trust V7's quality, add visual details instead |
| Contradictory terms | Conflicting output | Check for logical conflicts (e.g., "dark bright scene") |
| Ignoring --style raw | Over-stylized photos | Use `--style raw` for photorealism |
| Not saving seeds | Can't reproduce | Note `--seed` values from favorites |

---

## Negative Prompts (--no)

**Correct usage**:
```
still life painting --no fruit, shadows, bright colors
```

**Critical warnings**:
- "don't" and "without" DO NOT work — use `--no` instead
- `--no modern clothing` = "no modern" AND "no clothing" (words interpreted separately)
- Limit to essential exclusions (too many can conflict)

---

## Text in Images

```
A storefront sign that says "BAKERY"
```

**Tips** (V7 handles text better than previous versions):
- Use **double quotes** only (single quotes don't work)
- Keep text SHORT (5 words or fewer)
- Include context: "sign that says", "text reading"
- Use `--style raw` for better accuracy
- Lower `--stylize` helps text clarity

---

## Key Principles

### The Specificity Principle
More specific = more control. Vague prompts let Midjourney decide; specific prompts give you your vision.

### The Subtraction Principle
Adding more words doesn't always help. Use `/shorten` command to identify essential terms.

### The Reference Power Law
`--sref` and `--cref` provide more consistent control than text descriptions alone.

### The Iteration Mindset
First generation = starting point. Use variations, remix, and parameter adjustments to refine.

---

## Examples by Use Case

### Logo Design
```
minimalist logo design for tech startup, modern, clean lines,
geometric, professional, simple icon --v 7 --ar 1:1
```

### Book Cover
```
fantasy book cover, mysterious forest with glowing portal,
magical atmosphere, professional book cover design --ar 3:4 --v 7
```

### Social Media Post
```
motivational quote background, gradient colors blue to purple,
abstract shapes, modern design --ar 4:5
```

### Website Hero Image
```
tech startup hero image, modern office space, diverse team collaborating,
bright and professional, wide angle --ar 21:9 --style raw
```

### Seamless Pattern
```
geometric pattern, blue and gold Art Deco style --tile --ar 1:1 --style raw
```

---

## Testing and Iteration

1. **Start Simple** — Begin with basic prompt
2. **Add Details Gradually** — Refine one aspect at a time
3. **Use `--draft`** — 10x faster exploration
4. **Experiment with Parameters** — Test `--s`, `--chaos`, `--ar` values
5. **Save Good Seeds** — Note seeds from successful generations
6. **Use `/shorten`** — Identify essential vs unnecessary words

---

## Quick Reference

**Basic prompt**:
```
[subject], [description], [environment], [lighting] --ar [ratio]
```

**Photorealistic**:
```
[subject], [details], [lighting], [camera] [lens] [aperture], [film stock] --ar [ratio] --style raw
```

**Artistic**:
```
[subject], [style], [mood], [composition] --ar [ratio] --stylize [value]
```

**With style reference**:
```
[subject], [details] --sref [URL or code] --sw [0-1000] --ar [ratio]
```

**With character reference**:
```
[subject], [scene] --cref [URL] --cw [0-100] --ar [ratio]
```

---

## Additional Resources

- **Parameters**: See `midjourney_parameters.md` for complete parameter reference
- **Photography**: See `photography.md` for detailed camera/lighting terminology
- **API**: See `api_reference.md` for Legnext API details
