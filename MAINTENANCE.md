# GitHub Profile Maintenance & Customization Guide

This guide explains how to maintain, customize, preview, and update your GitHub profile (`amritkr1999/amritkr1999`).

---

## ⚡ Quick Workflow

Whenever you want to modify your profile:

1. **Edit** `README.md`
2. **Preview locally** in your browser:
   ```bash
   ./preview.sh
   ```
3. **Publish to GitHub**:
   ```bash
   ./sync.sh "Updated projects and tech stack"
   ```
   *(If you run `./sync.sh` without arguments, it generates an automatic timestamped commit message).*

---

## 🎨 1. Header Banner (`capsule-render`)

Your header banner uses the dynamic `capsule-render` SVG generator:

```markdown
https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=1,15,30&height=220&section=header&text=Hi%20there,%20I'm%20Amrit%20Kumar%20👋&fontSize=40&fontColor=ffffff&fontAlignY=40&animation=fadeIn
```

### Options You Can Tweak:
* **`type`**: `waving`, `wave`, `slice`, `shark`, `soft`, `cylinder`, `rect`
* **`color`**: `gradient`, `auto`, or custom hex codes `0000ff`
* **`customColorList`**: Color stop indices (e.g., `1,15,30` for deep navy/purple/cyan)
* **`height`**: Banner height in pixels (e.g. `200`, `220`, `250`)
* **`animation`**: `fadeIn`, `scaleIn`

Interactive builder: [https://kyechan99.github.io/capsule-render/](https://kyechan99.github.io/capsule-render/)

---

## ⌨️ 2. Dynamic Typing SVG

Located directly under the banner:

```markdown
https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=1000&color=38BDF8&center=true&vCenter=true&width=620&lines=Line+One;Line+Two;Line+Three
```

* **To add or edit lines**: Change `lines=Text+1;Text+2;Text+3` (use `+` for spaces and `%20` for special symbols).
* **To change font color**: Change `color=38BDF8` (hex code without `#`).
* **Fonts supported**: `Fira+Code`, `Courier+New`, `Roboto`, `Montserrat`, etc.

Interactive builder: [https://git.io/typing-svg](https://git.io/typing-svg)

---

## 🛠️ 3. Tech Stack & Icons (`skillicons.dev`)

Icons are grouped into categories and generated via URL slugs:

```markdown
<img src="https://skillicons.dev/icons?i=java,ts,js,python,html,css&perline=6" />
```

### Common Slugs:
* **Languages**: `java`, `ts`, `js`, `python`, `go`, `rust`, `cpp`, `c`, `cs`, `php`, `html`, `css`
* **Frontend**: `react`, `nextjs`, `vue`, `svelte`, `tailwind`, `bootstrap`, `redux`, `sass`
* **Backend**: `spring`, `fastapi`, `nodejs`, `express`, `django`, `flask`, `graphql`
* **Databases**: `postgres`, `mongodb`, `redis`, `mysql`, `sqlite`, `supabase`, `firebase`
* **DevOps & Cloud**: `docker`, `kubernetes`, `aws`, `gcp`, `azure`, `git`, `githubactions`, `linux`, `nginx`
* **Tools**: `vscode`, `postman`, `figma`, `pycharm`, `idea`

Catalog & builder: [https://skillicons.dev](https://skillicons.dev)

---

## 📊 4. GitHub Stats & Streaks

Your profile cards are rendered in the **tokyonight** dark theme:

### Supported Themes:
You can swap `theme=tokyonight` to any of these:
* `tokyonight` (Clean dark blue/purple)
* `catppuccin_mocha` (Pastel dark)
* `dracula` (High contrast violet)
* `radical` (Cyberpunk neon)
* `github_dark` (Native GitHub dark mode)
* `gruvbox` (Warm retro dark)

---

## 🚀 5. Adding New Projects to the Table

To add a new project under `### 🚀 Featured Highlights & Engineering Work`, insert a new row in the Markdown table:

```markdown
| **Your Project Name** | <ul><li>**1-line pitch** describing what the project solves.</li><li>**Key architecture highlight** (e.g. distributed queues, RAG pipeline, WebSockets).</li><li>**Tech Stack**: Tech1, Tech2, Tech3.</li></ul> | [Live Demo](https://...) • [Code](https://...) |
```

---

## 🐍 6. Contribution Snake Automation

The snake animation runs automatically every day at **midnight UTC** via GitHub Actions:
* **Workflow file**: `.github/workflows/snake.yml`
* **Output files**: Pushed to the hidden `output` branch:
  * `github-snake.svg`
  * `github-snake-dark.svg`

### To Trigger Manually:
1. Open [https://github.com/amritkr1999/amritkr1999/actions](https://github.com/amritkr1999/amritkr1999/actions)
2. Click **Generate Snake Animation** ➔ **Run workflow**.
