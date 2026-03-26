# resource.images.weatherfanart.echo

**Weather Fanart Image Pack for Kodi**

A resource addon providing high-quality background and fanart images for all standard Yahoo weather condition codes (0–47), plus `na` and `alert` states.

---

<p align="center">
  <img src="pic01.jpg" width="48%" alt="Sample fanart 1" />
  <img src="pic02.jpg" width="48%" alt="Sample fanart 2" />
</p>
<p align="center">
  <img src="pic03.jpg" width="48%" alt="Sample fanart 3" />
  <img src="pic04.jpg" width="48%" alt="Sample fanart 4" />
</p>

---

## Overview

This addon supplies a curated set of photographic fanart images organized by weather condition code. When paired with weather.kodiweather 2.4.2+, Kodi displays contextual full-screen background images matching current weather conditions.

Images are sourced from free-use photography sites and converted to Kodi-compatible formats. The maintainer is currently using [Pexels](https://www.pexels.com/), but any rights-cleared source is acceptable.

---

## Compatibility

| Component    | Requirement                                              |
|--------------|----------------------------------------------------------|
| Kodi         | 19 (Matrix) or later                                     |
| Python       | Not required (resource addon)                            |
| Platform     | Any platform Kodi supports                               |
| Paired addon | weather.kodiweather 2.4.2+ (handles condition mapping)   |

---

## Installation

This addon is not yet available through a public repository. Manual installation only.

### Step 1 — Download

Clone or download the repository from GitHub:

```
https://github.com/Echo-Storm/resource.images.weatherfanart.echo
```

Or download the ZIP directly from the Releases page (when available).

### Step 2 — Install in Kodi

- Copy the `resource.images.weatherfanart.echo` folder into your Kodi `addons` directory, **or**
- In Kodi: *Settings → Add-ons → Install from ZIP file* and select the downloaded archive.

### Step 3 — Enable

Kodi should enable the addon automatically on install. Verify under *Settings → Add-ons → My Add-ons → Image Resources*.

---

## Image Coverage

This addon uses 21 master image folders to cover all 50 weather condition codes. The weather.kodiweather addon (2.4.2+) handles the mapping from condition codes to master folders, eliminating duplicate storage.

### Master Folders

| Folder | Condition | Files | Covers Codes |
|-------:|-----------|------:|--------------|
| 0 | Tornado | 10 | 0 |
| 1 | Tropical Storm | 10 | 1 |
| 2 | Hurricane | 10 | 2 |
| 3 | Thunderstorms | 54 | 3, 4, 37, 38, 39, 45, 47 |
| 5 | Mixed Precip / Freezing | 20 | 5, 6, 7, 8, 10, 18 |
| 9 | Drizzle | 18 | 9 |
| 11 | Light Showers (Night) | 23 | 11 |
| 12 | Heavy Showers (Day) | 33 | 12, 40 |
| 13 | Snow | 43 | 13, 14, 15, 16, 41, 42, 43, 46 |
| 17 | Hail | 16 | 17, 35 |
| 19 | Dust | 13 | 19 |
| 20 | Foggy | 25 | 20, 21 |
| 22 | Smoky | 10 | 22 |
| 23 | Windy | 35 | 23, 24 |
| 25 | Cold | 32 | 25 |
| 26 | Cloudy (Day) | 53 | 26, 28, 30, 44 |
| 27 | Cloudy (Night) | 54 | 27, 29 |
| 31 | Clear (Night) | 34 | 31, 33 |
| 32 | Sunny / Fair / Hot | 54 | 32, 34, 36 |
| na | Not Available | 12 | na |
| alert | Weather Alert | 10 | alert |

**Total: 569 files across 21 folders (931 MB)**

### Condition Code Mapping

The weather addon redirects these codes to master folders:

| Code | Condition | → Master |
|-----:|-----------|:--------:|
| 4 | Thunderstorms | 3 |
| 6 | Mixed Rain and Sleet | 5 |
| 7 | Mixed Snow and Sleet | 5 |
| 8 | Freezing Drizzle | 5 |
| 10 | Freezing Rain | 5 |
| 14 | Light Snow Showers | 13 |
| 15 | Blowing Snow | 13 |
| 16 | Snow | 13 |
| 18 | Sleet | 5 |
| 21 | Haze | 20 |
| 24 | Windy | 23 |
| 28 | Mostly Cloudy (Day) | 26 |
| 29 | Partly Cloudy (Night) | 27 |
| 30 | Partly Cloudy (Day) | 26 |
| 33 | Fair (Night) | 31 |
| 34 | Fair (Day) | 32 |
| 35 | Mixed Rain and Hail | 17 |
| 36 | Hot | 32 |
| 37 | Isolated Thunderstorms | 3 |
| 38 | Scattered Thunderstorms (Night) | 3 |
| 39 | Scattered Thunderstorms (Day) | 3 |
| 40 | Scattered Showers | 12 |
| 41 | Heavy Snow (Night) | 13 |
| 42 | Scattered Snow Showers | 13 |
| 43 | Heavy Snow (Day) | 13 |
| 44 | Partly Cloudy | 26 |
| 45 | Thundershowers | 3 |
| 46 | Snow Showers | 13 |
| 47 | Isolated Thundershowers | 3 |

---

## File Naming Convention

Files within each folder follow a prefixed zero-padded sequential naming scheme:

```
resources/
  0/
    0-000.jpg
    0-001.jpg
    ...
  3/
    3-000.jpg
    3-001.jpg
    ...
  na/
    na-000.jpg
    ...
  alert/
    alert-000.jpg
    ...
```

> **Note on folder names:** Kodi's resource addon system uses unpadded integers for condition code folders—`0`, `1`, `2`—not zero-padded values like `00`, `01`, `02`. This is a Kodi convention and must be followed exactly or the images will not be found at runtime.

---

## Image Requirements

| Attribute  | Requirement                                                        |
|------------|--------------------------------------------------------------------|
| Resolution | 1920×1080 exactly — no borders, letterboxing, or pillarboxing      |
| Format     | JPG only, quality 10 — no PNG or other formats                     |
| Content    | Photographic only — no illustrations, heavy filters, or watermarks |
| Subject    | Image should clearly convey the weather condition it represents    |
| Source     | Any free-use or rights-cleared source (Pexels, Unsplash, etc.)     |

---

## Contributing

Contributions are welcome. To add images:

1. Fork the repository on GitHub
2. Add images to the appropriate master folder under `resources/`
3. Name files sequentially continuing from the last existing file (e.g., `3-054.jpg`)
4. Open a pull request with a brief note on what condition(s) you're filling and the source URLs

---

## License

**Images:** Sourced from weatherfanartcode (Kodi, 2014), weather.multi (Kodi, 2026), an old MediaPortal archive (2020), and [Pexels](https://www.pexels.com/) under the [Pexels License](https://www.pexels.com/license/), which permits free use without attribution.

**Addon code and structure:** MIT License — see `LICENSE` file.

---

## Author

**Echostorm**  
GitHub: [Echo-Storm](https://github.com/Echo-Storm)
