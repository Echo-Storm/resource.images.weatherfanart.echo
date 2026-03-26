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

This addon supplies a curated set of photographic fanart images organized by weather condition code. When paired with a compatible weather addon, Kodi can display a contextual full-screen or background image that matches the current weather condition rather than a static skin default.

Images are sourced from free-use photography sites and converted to Kodi-compatible formats. The maintainer is currently using [Pexels](https://www.pexels.com/), but any rights-cleared source is acceptable.

> **Status: Work in Progress**  
> Image conversion is ongoing. Coverage varies by condition—see the [Image Coverage](#image-coverage) table below for current status.  
> Contributions welcome. If you'd like to add images for underrepresented conditions, see [Contributing](#contributing).

---

## Compatibility

| Component    | Requirement                                              |
|--------------|----------------------------------------------------------|
| Kodi         | 19 (Matrix) or later                                     |
| Python       | Not required (resource addon)                            |
| Platform     | Any platform Kodi supports                               |
| Paired addon | Any weather addon that resolves fanart via resource packs |

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

Images are organized by Yahoo weather condition code. Each condition maps to a numbered folder under `resources/`.

> **Note on ambiguous codes:** The Yahoo/Kodi spec lists codes 11 & 12 both as "showers", codes 38 & 39 both as "scattered thunderstorms", and codes 41 & 43 both as "heavy snow". Based on how Yahoo's own implementation mapped icons, this pack intentionally treats these as distinct day/night or light/heavy pairs. The skin and weather addon will be updated to route these codes accordingly.

|  Code | Condition                       | Files | Target | Status | Clone? | Pass 1 | Pass 2 |
| ----: | ------------------------------- | ----: | -----: | ------ | :----: | :----: | :----: |
|     0 | Tornado                         |    12 |     10 | ✔ good |   —    |   ✔    |   ✗    |
|     1 | Tropical Storm                  |    10 |     10 | ✔ good |   —    |   ✔    |   ✗    |
|     2 | Hurricane                       |    10 |     10 | ✔ good |   —    |   ✔    |   ✗    |
|     3 | Severe Thunderstorms            |    54 |     15 | ✔ good |   +    |   ✔    |   ✗    |
|     4 | Thunderstorms                   |    54 |     15 | ✔ good |   3    |   ✔    |   ✗    |
|     5 | Mixed Rain and Snow             |    20 |     15 | ✔ good |   +    |   ✔    |   ✗    |
|     6 | Mixed Rain and Sleet            |    20 |     15 | ✔ good |   5    |   ✔    |   ✗    |
|     7 | Mixed Snow and Sleet            |    20 |     15 | ✔ good |   5    |   ✔    |   ✗    |
|     8 | Freezing Drizzle                |    20 |     15 | ✔ good |   5    |   ✔    |   ✗    |
|     9 | Drizzle                         |    18 |     15 | ✔ good |   —    |   ✔    |   ✗    |
|    10 | Freezing Rain                   |    20 |     15 | ✔ good |   5    |   ✔    |   ✗    |
|    11 | Light Showers (Night)           |    23 |     20 | ✔ good |   —    |   ✔    |   ✗    |
|    12 | Heavy Showers (Day)             |    33 |     30 | ✔ good |   +    |   ✔    |   ✗    |
|    13 | Snow Flurries                   |    43 |     25 | ✔ good |   +    |   ✔    |   ✗    |
|    14 | Light Snow Showers              |    43 |     25 | ✔ good |   13   |   ✔    |   ✗    |
|    15 | Blowing Snow                    |    43 |     25 | ✔ good |   13   |   ✔    |   ✗    |
|    16 | Snow                            |    43 |     25 | ✔ good |   13   |   ✔    |   ✗    |
|    17 | Hail                            |    16 |     10 | ✔ good |   +    |   ✔    |   ✗    |
|    18 | Sleet                           |    20 |     15 | ✔ good |   5    |   ✔    |   ✗    |
|    19 | Dust                            |    13 |     10 | ✔ good |   —    |   ✔    |   ✗    |
|    20 | Foggy                           |    25 |     20 | ✔ good |   +    |   ✔    |   ✗    |
|    21 | Haze                            |    25 |     15 | ✔ good |   20   |   ✔    |   ✗    |
|    22 | Smoky                           |    10 |     10 | ✔ good |   —    |   ✔    |   ✗    |
|    23 | Blustery                        |    35 |     20 | ✔ good |   +    |   ✔    |   ✗    |
|    24 | Windy                           |    35 |     20 | ✔ good |   23   |   ✔    |   ✗    |
|    25 | Cold                            |    32 |     25 | ✔ good |   —    |   ✔    |   ✗    |
|    26 | Cloudy                          |    53 |     50 | ✔ good |   +    |   ✔    |   ✗    |
|    27 | Mostly Cloudy (Night)           |    54 |     50 | ✔ good |   +    |   ✔    |   ✗    |
|    28 | Mostly Cloudy (Day)             |    53 |     30 | ✔ good |   26   |   ✔    |   ✗    |
|    29 | Partly Cloudy (Night)           |    54 |     50 | ✔ good |   27   |   ✔    |   ✗    |
|    30 | Partly Cloudy (Day)             |    53 |     50 | ✔ good |   26   |   ✔    |   ✗    |
|    31 | Clear (Night)                   |    33 |     30 | ✔ good |   +    |   ✔    |   ✗    |
|    32 | Sunny                           |    54 |     30 | ✔ good |   +    |   ✔    |   ✗    |
|    33 | Fair (Night)                    |    33 |     30 | ✔ good |   33   |   ✔    |   ✗    |
|    34 | Fair (Day)                      |    54 |     30 | ✔ good |   32   |   ✔    |   ✗    |
|    35 | Mixed Rain and Hail             |    16 |     10 | ✔ good |   17   |   ✔    |   ✗    |
|    36 | Hot                             |    54 |     30 | ✔ good |   32   |   ✔    |   ✗    |
|    37 | Isolated Thunderstorms          |    54 |     15 | ✔ good |   3    |   ✔    |   ✗    |
|    38 | Scattered Thunderstorms (Night) |    54 |     15 | ✔ good |   3    |   ✔    |   ✗    |
|    39 | Scattered Thunderstorms (Day)   |    54 |     15 | ✔ good |   3    |   ✔    |   ✗    |
|    40 | Scattered Showers               |    33 |     25 | ✔ good |   12   |   ✔    |   ✗    |
|    41 | Heavy Snow (Night)              |    43 |     25 | ✔ good |   13   |   ✔    |   ✗    |
|    42 | Scattered Snow Showers          |    43 |     25 | ✔ good |   13   |   ✔    |   ✗    |
|    43 | Heavy Snow (Day)                |    43 |     25 | ✔ good |   13   |   ✔    |   ✗    |
|    44 | Partly Cloudy                   |    53 |     50 | ✔ good |   26   |   ✔    |   ✗    |
|    45 | Thundershowers                  |    54 |     15 | ✔ good |   3    |   ✔    |   ✗    |
|    46 | Snow Showers                    |    43 |     25 | ✔ good |   13   |   ✔    |   ✗    |
|    47 | Isolated Thundershowers         |    54 |     15 | ✔ good |   3    |   ✔    |   ✗    |
|    na | Not Available                   |    12 |      5 | ✔ good |   —    |   ✔    |   ✗    |
| alert | Weather Alert                   |    10 |      5 | ✔good  |   —    |   ✔    |   ✗    |

**Legend**

| Symbol | Meaning                              |
|:------:|--------------------------------------|
|   ✔    | At or near target / complete         |
|   ▲    | Needs more images                    |
|   ▼    | Overpopulated / needs cull           |
|   ✗    | Not yet started                      |
|   —    | No cloning needed                    |
|   +    | Master clone source                  |
|  *n*   | Cloned from directory *n*            |

---

## Contributing

Contributions are welcome, particularly for conditions that are underpopulated.

### Image Requirements

| Attribute  | Requirement                                                        |
|------------|--------------------------------------------------------------------|
| Resolution | 1920×1080 exactly — no borders, letterboxing, or pillarboxing      |
| Format     | JPG only, quality 10 — no PNG or other formats                     |
| Content    | Photographic only — no illustrations, heavy filters, or watermarks |
| Subject    | Image should clearly convey the weather condition it represents    |
| Source     | Any free-use or rights-cleared source (Pexels, Unsplash, etc.)     |

### How to Contribute

1. Fork the repository on GitHub
2. Add images to the appropriate numbered folder under `resources/`
3. Name files sequentially continuing from the last existing file (e.g., `012.jpg`)
4. Open a pull request with a brief note on what condition(s) you're filling and the source URLs

**Priority conditions (most needed):** `alert`, 26, 27, 29, 37, 38, 39, 40, 41, 42, 46, 47

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

> **Note on folder names:** Kodi's resource addon system uses unpadded integers for condition code folders—`0`, `1`, `2`—not zero-padded values like `00`, `01`, `02`. This is a Kodi convention and must be followed exactly or the images will not be found at runtime.

---

## License

**Images:** Sourced from weatherfanartcode (Kodi, 2014), weather.multi (Kodi, 2026), an old MediaPortal archive (2020), and [Pexels](https://www.pexels.com/) under the [Pexels License](https://www.pexels.com/license/), which permits free use without attribution.

**Addon code and structure:** MIT License — see `LICENSE` file.

---

## Author

**Echostorm**  
GitHub: [Echo-Storm](https://github.com/Echo-Storm)
