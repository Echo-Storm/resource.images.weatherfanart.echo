# resource.images.weatherfanart.echo

**Weather Fanart Image Pack for Kodi**  
A resource addon providing high-quality background/fanart images for all standard Yahoo weather condition codes (0–47), plus `na` and `alert` states.

---

## Overview

This addon supplies a curated set of photographic fanart images organized by weather condition code. When paired with a compatible weather addon, Kodi can display a contextual full-screen or background image that matches the current weather condition rather than a static skin default.

Images are sourced from free-use photography sites and converted to Kodi-compatible formats. The maintainer is currently using [Pexels](https://www.pexels.com/), but any rights-cleared source is acceptable.

> **⚠ Status: Work in Progress**  
> Image conversion is ongoing. Coverage varies by condition — see the [Image Coverage](#image-coverage) table below for current status.  
> **Volunteers welcome.** If you'd like to contribute images for underrepresented conditions, see [Contributing](#contributing).

---

## Compatibility

| Component | Requirement |
|-----------|-------------|
| Kodi | 19 (Matrix) or later |
| Python | Not required (resource addon) |
| Platform | Any platform Kodi supports |
| Paired addon | Any weather addon that resolves fanart via resource image packs |

---

## Installation

This addon is not yet available through a public repository. Manual installation only.

**Step 1 — Download**

Clone or download the repository from GitHub:

```
https://github.com/Echo-Storm/resource.images.weatherfanart.echo
```

Or download the ZIP directly from the Releases page (when available).

**Step 2 — Install in Kodi**

1. Copy the `resource.images.weatherfanart.echo` folder into your Kodi `addons` directory, **or**
2. In Kodi: *Settings → Add-ons → Install from ZIP file* and select the downloaded archive.

**Step 3 — Enable**

Kodi should enable the addon automatically on install. Verify under *Settings → Add-ons → My Add-ons → Image Resources*.

---

## Image Coverage

Images are organized by Yahoo weather condition code. Each condition maps to a numbered folder under `resources/`.

> **Note on ambiguous codes:** The Yahoo/Kodi spec lists codes 11 & 12 both as "showers", codes 38 & 39 both as "scattered thunderstorms", and codes 41 & 43 both as "heavy snow". Based on how Yahoo's own implementation mapped icons, this pack intentionally treats these as distinct day/night or light/heavy pairs. The skin and weather addon will be updated to route these codes accordingly.

| Code | Condition | Files | Target | Status |
|------|-----------|-------|--------|--------|
| 0 | Tornado | 11 | 10 | ✔ good |
| 1 | Tropical Storm | 10 | 10 | ✔ good |
| 2 | Hurricane | 10 | 10 | ✔ good |
| 3 | Severe Thunderstorms | 15 |15 | ✔ good |
| 4 | Thunderstorms | 17 | 15 | ✔ good |
| 5 | Mixed Rain and Snow | 20 | 15 | ✔ good |
| 6 | Mixed Rain and Sleet | 20 | 15 | ✔ good |
| 7 | Mixed Snow and Sleet | 20 | 15 | ✔ good |
| 8 | Freezing Drizzle | 20 | 15 | ✔ good |
| 9 | Drizzle | 18 | 15 | ✔ good |
| 10 | Freezing Rain | 20 | 15 | ✔ good |
| 11 | Light Showers (Night) | 23 | 20 | ✔ good |
| 12 | Heavy Showers (Day) | 14 | 20–30 | ▲ needs +6 to +16 |
| 13 | Snow Flurries | 12 | 15–25 | ▲ needs +3 to +13 |
| 14 | Light Snow Showers | 11 | 15–25 | ▲ needs +4 to +14 |
| 15 | Blowing Snow | 10 | 10–15 | ✔ good |
| 16 | Snow | 12 | 15–25 | ▲ needs +3 to +13 |
| 17 | Hail | 13 | 5–10 | ▼ slightly high |
| 18 | Sleet | 17 | 10–15 | ▼ slightly high |
| 19 | Dust | 10 | 3–8 | ▼ high |
| 20 | Foggy | 48 | 10–20 | ▼ extremely high — needs culling |
| 21 | Haze | 14 | 10–15 | ✔ good |
| 22 | Smoky | 5 | 3–8 | ✔ perfect |
| 23 | Blustery | 13 | 10–15 | ✔ good |
| 24 | Windy | 14 | 10–15 | ✔ good |
| 25 | Cold | 21 | 15–25 | ✔ good |
| 26 | Cloudy | 24 | 30–50 | ▲ needs +6 to +26 |
| 27 | Mostly Cloudy (Night) | 11 | 20–30 | ▲ needs +9 to +19 |
| 28 | Mostly Cloudy (Day) | 23 | 20–30 | ✔ good |
| 29 | Partly Cloudy (Night) | 9 | 20–30 | ▲ needs +11 to +21 |
| 30 | Partly Cloudy (Day) | 42 | 30–50 | ✔ strong |
| 31 | Clear (Night) | 23 | 20–30 | ✔ good |
| 32 | Sunny | 34 | 20–30 | ▼ slightly high |
| 33 | Fair (Night) | 10 | 10–15 | ✔ good |
| 34 | Fair (Day) | 12 | 10–15 | ✔ good |
| 35 | Mixed Rain and Hail | 7 | 5–10 | ✔ good |
| 36 | Hot | 11 | 10–15 | ✔ good |
| 37 | Isolated Thunderstorms | 8 | 10–15 | ▲ needs +2 to +7 |
| 38 | Scattered Thunderstorms (Night) | 7 | 10–15 | ▲ needs +3 to +8 |
| 39 | Scattered Thunderstorms (Day) | 9 | 10–15 | ▲ needs +1 to +6 |
| 40 | Scattered Showers | 9 | 15–25 | ▲ needs +6 to +16 |
| 41 | Heavy Snow (Night) | 13 | 15–25 | ▲ needs +2 to +12 |
| 42 | Scattered Snow Showers | 11 | 15–25 | ▲ needs +4 to +14 |
| 43 | Heavy Snow (Day) | 18 | 15–25 | ✔ good |
| 44 | Partly Cloudy | 33 | 30–50 | ✔ strong |
| 45 | Thundershowers | 10 | 10–15 | ✔ good |
| 46 | Snow Showers | 11 | 15–25 | ▲ needs +4 to +14 |
| 47 | Isolated Thundershowers | 6 | 10–15 | ▲ needs +4 to +9 |
| na | Not Available | 3 | 3–5 | ✔ fine |
| alert | Weather Alert | 0 | 3–5 | ▲ needs +3 to +5 |

**Legend:** ✔ at or near target · ▲ needs more images · ▼ overpopulated or needs culling

---

## Contributing

Contributions are welcome, particularly for conditions that are underpopulated.

**Image requirements (initial release):**

- Resolution: 1920×1080 exactly — no borders, no letterboxing, no pillarboxing
- Format: JPG only, quality 10 — no PNG, no other formats accepted at this time
- Content: Photographic only — no illustrations, no heavy filters, no watermarks
- Subject: The image should clearly convey the weather condition it represents
- Source: Any free-use or rights-cleared source is acceptable. The maintainer is currently sourcing from [Pexels](https://www.pexels.com/). Please retain the source URL in your PR notes regardless of origin.

**To contribute:**

1. Fork the repository on GitHub
2. Add images to the appropriate numbered folder under `resources/`
3. Name files sequentially continuing from the last existing file (e.g. `012.jpg`)
4. Open a pull request with a brief note on what condition(s) you're filling and the Pexels source URLs

Priority conditions (most needed): `alert`, codes 11, 12, 26, 27, 29, 40

---

## Image Naming Convention

Files within each condition folder follow a zero-padded sequential naming scheme:

```
resources/
  0/
    000.jpg
    001.jpg
    ...
  1/
    000.jpg
    ...
  na/
    000.jpg
    ...
  alert/
    000.jpg
    ...
```

> **Note on folder names:** Kodi's resource addon system uses unpadded integers for condition code folders — `0`, `1`, `2` — not zero-padded values like `00`, `01`, `02`. This is a Kodi convention and must be followed exactly or the images will not be found at runtime.

---

## License

Images are currently sourced from 

weatherfanartcode (kodi) (2014)
weather.multi (kodi) (2026)
old archive (mediaportal) (2020)

[Pexels](https://www.pexels.com/) under the [Pexels License](https://www.pexels.com/license/), which permits free use without attribution.

Addon code and structure: MIT License — see `LICENSE` file.

---

## Author

**Echostorm**  
GitHub: [Echo-Storm](https://github.com/Echo-Storm)
