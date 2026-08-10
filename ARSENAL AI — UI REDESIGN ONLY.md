# ARSENAL AI — UI REDESIGN ONLY

Redesign the **UI/UX of the existing application** into a premium **Arsenal AI** interface.

This task is **UI ONLY**.

Do not change, remove, or rewrite the application's functionality, backend logic, AI logic, API integrations, system monitoring logic, file handling logic, signals, timers, keyboard shortcuts, or application behavior.

Your job is to make the existing application look significantly more polished, modern, cohesive, and professional.

---

## 1. BRAND

Replace the visible **XENO** branding with:

**ARSENAL AI**

Use:

**ARSENAL AI — Personal AI Command System**

for the application identity where appropriate.

Do not change internal class/function names unless absolutely necessary.

---

## 2. VISUAL STYLE

Completely move away from the current cyan/blue cyberpunk appearance.

Create a sophisticated:

**Obsidian + Dark Brown + Bronze + Warm Gold**

theme.

The interface should feel like:

- Premium AI command center
- Tactical intelligence console
- Sophisticated desktop application
- Dark, precise, controlled
- Modern rather than gaming-oriented

Avoid excessive neon, excessive glow, bright cyan, or generic futuristic styling.

The UI should look **expensive and intentional**.

---

## 3. COLOR PALETTE

Use a centralized palette similar to:

```python
BG        = "#0B0908"
DARK      = "#100C0A"
PANEL     = "#15100D"
PANEL2    = "#1C1511"
BAR_BG    = "#241A14"

BORDER    = "#35271E"
BORDER_A  = "#493427"
BORDER_B  = "#654936"

PRI       = "#C49A5A"
PRI_DIM   = "#80643D"
PRI_GHO   = "#2A2119"

ACC       = "#A86F3D"
ACC2      = "#D2B06A"

GREEN     = "#8FAF72"
RED       = "#B85C50"

TEXT      = "#D8CBB8"
TEXT_DIM  = "#786B5C"
TEXT_MED  = "#A99A86"
WHITE     = "#E8DED0"
```

Use these as a design direction, not necessarily as immutable values.

Important:

**Do not turn the entire UI brown.**

Use:

- Obsidian for backgrounds
- Dark brown for panels
- Bronze for primary accents
- Gold for important highlights
- Warm ivory for primary text
- Taupe for secondary text
- Green/red only for system status

---

## 4. HEADER

Redesign the top header.

Create a clean hierarchy such as:

```text
ARSENAL AI                         17:42:08
TACTICAL INTELLIGENCE SYSTEM       MON 10 AUG 2026
```

Use subtle borders and spacing.

The brand should be the strongest visual element.

Avoid excessive glow.

---

## 5. LEFT SYSTEM PANEL

Redesign the system monitoring panel into a premium tactical monitoring panel.

Keep the existing information and functionality.

Visually improve:

- CPU
- Memory
- Network
- GPU
- Temperature
- Uptime
- Processes
- OS
- AI status
- Security status
- Protocol status

Use compact cards and clean metric bars.

Example visual direction:

```text
SYSTEM STATUS
──────────────

CPU       42%
████████░░

MEM       61%
██████████

GPU       37%
██████░░░░

TEMP      54°C
█████░░░░░
```

Use muted bronze/gold rather than neon colors.

---

## 6. CENTRAL AI HUD

Keep the existing HUD functionality and animations.

Do NOT remove:

- avatar
- circular rings
- scanner
- crosshair
- pulse effects
- particles
- waveform
- status indicator

But completely restyle them.

Replace the current cyan aesthetic with:

- bronze rings
- dark amber scanning
- muted gold highlights
- subtle brown grid
- warm particles
- restrained glow

The HUD should look like a **premium tactical AI interface**.

Avoid making every element glow.

The avatar must remain the central focal point.

---

## 7. AI STATUS COLORS

Keep the existing states.

Visually style them as:

```text
INITIALISING → Bronze
LISTENING    → Muted Green
THINKING     → Warm Gold
PROCESSING   → Bronze
SPEAKING     → Burnt Bronze
MUTED        → Muted Red
```

Maintain the existing animations.

---

## 8. RIGHT PANEL

Redesign the entire right-side interface.

Keep all existing information and controls.

Improve:

- section hierarchy
- spacing
- alignment
- typography
- borders
- cards
- button styling
- visual grouping

Use small uppercase section headers with subtle bronze separators.

Do not put every individual element inside a large card.

The panel should feel organized and premium.

---

## 9. FILE DROP AREA

Redesign the file upload/drop area.

Keep its current functionality.

Visual direction:

```text
┌──────────────────────────────────┐
│                                  │
│              ↓                   │
│       DROP FILE HERE             │
│       OR CLICK TO BROWSE         │
│                                  │
│ Images · Video · Audio · PDF     │
│ Docs · Code · Data               │
│                                  │
└──────────────────────────────────┘
```

Use a subtle dashed bronze border.

Hover:

- slightly brighter border
- subtle background change

Drag-over:

- warm gold highlight
- subtle glow
- clear feedback

Loaded file:

- clean file icon
- filename
- extension
- size
- path
- remove control

---

## 10. LOG / TERMINAL UI

Keep the existing log functionality and typewriter effect.

Redesign its appearance.

Use:

- Obsidian background
- warm ivory text
- bronze AI messages
- gold system messages
- green file/status messages
- muted red errors

Make it look like a sophisticated AI command terminal rather than an old-school neon terminal.

---

## 11. TYPOGRAPHY

Use a modern typography hierarchy.

Prefer:

- Segoe UI
- Inter
- IBM Plex Sans
- JetBrains Mono

Use sans-serif fonts for the majority of the interface.

Use monospace selectively for:

- logs
- system values
- timestamps
- technical information

Do not make the entire application look like a terminal.

---

## 12. BUTTONS

Redesign every visible button.

Normal:

- dark brown/obsidian background
- subtle bronze border
- warm ivory text

Hover:

- bronze border
- subtle background highlight

Active:

- warm gold accent

Use small/moderate corner radii.

Avoid:

- neon buttons
- huge rounded buttons
- excessive gradients
- excessive glow

---

## 13. PANELS & CARDS

Create a consistent visual system.

Panels should use:

- dark obsidian/brown backgrounds
- subtle borders
- consistent padding
- consistent spacing
- restrained corner radius
- subtle hover states

Do not make every component look like a separate floating box.

Use whitespace and borders to create hierarchy.

---

## 14. SETUP / INITIALIZATION SCREEN

Redesign the existing initialization/setup UI visually.

Keep all existing fields and functionality.

Make it look like an Arsenal AI secure initialization screen.

Example:

```text
ARSENAL AI
INITIALIZATION REQUIRED

Configure Arsenal AI before first boot.

GEMINI API KEY
[••••••••••••••••••]

OPENROUTER API KEY
[••••••••••••••••••]

OPERATING SYSTEM
[ WINDOWS ] [ macOS ] [ LINUX ]

[ INITIALIZE ARSENAL AI ]
```

Use the same Obsidian/Brown/Bronze visual system.

---

## 15. FOOTER

Redesign the footer to match the new identity.

Keep useful information and shortcuts.

Example:

```text
ARSENAL AI     SYSTEM ONLINE     F4 MUTE     F11 FULLSCREEN
```

Keep it minimal and unobtrusive.

---

## 16. SCROLL THROUGH THE ENTIRE UI

This is very important.

Do **not** redesign only the first visible screen.

Inspect the **entire application and all UI sections**.

Scroll through every available page, panel, overlay, dialog, and lower section.

Check:

- Main screen
- Left panel
- Central HUD
- Right panel
- File section
- Logs
- Setup overlay
- Footer
- Any hidden/secondary sections
- Any scrollable areas
- Any content below the initial viewport

Every page/section must use the same Arsenal AI design language.

There must be **no old cyan/blue UI remaining anywhere**.

---

## 17. RESPONSIVE UI

Check the redesigned interface at different window sizes.

Make sure:

- nothing overlaps
- text is not clipped
- buttons remain usable
- panels remain readable
- HUD scales correctly
- content does not disappear
- long sections can scroll
- setup overlay remains properly positioned

If any existing section is taller than the available window, improve its scrolling/layout behavior **without changing its functionality**.

---

## 18. OLD THEME CLEANUP

Search the complete code for old visual styling.

Find old cyan/blue colors and replace them with the new design system.

Pay particular attention to:

- hardcoded colors
- stylesheets
- `paintEvent()` drawing colors
- borders
- hover states
- progress bars
- overlays
- labels
- buttons
- scrollbars
- file icons
- HUD effects

Do not simply perform a mechanical color replacement.

Every component should be visually coherent.

---

## 19. ANIMATION STYLE

Keep existing animations.

Make them feel more refined.

Use:

- subtle movement
- smooth transitions
- restrained glow
- slow idle animations
- stronger animation during active AI states

Avoid excessive flashing or distracting effects.

Do not introduce animations that unnecessarily increase CPU usage.

---

## 20. FINAL REQUIREMENT

This is a **UI/UX redesign only**.

Do not modify application functionality.

Do not remove features.

Do not rewrite backend logic.

Do not change API behavior.

Do not change system-monitoring behavior.

Do not change file-processing behavior.

Do not change AI behavior.

Only improve:

**branding + colors + layout + spacing + typography + components + styling + visual hierarchy + UI responsiveness + visual consistency.**

Final visual identity:

# ARSENAL AI

**Obsidian / Dark Brown / Bronze / Warm Gold**

Premium. Tactical. Minimal. Sophisticated. Professional.