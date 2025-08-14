# Simon's Microblog

A minimal, fast personal blog built with modern static site generation.

🌐 **Live site:** [simeg.github.io](https://simeg.github.io)

## Tech Stack

- **[Zola](https://www.getzola.org/)** - Fast static site generator written in Rust
- **[archie-zola](https://github.com/XXXMrG/archie-zola)** - Clean, minimal theme with dark/light mode
- **GitHub Pages** - Hosting with automatic deployment
- **GitHub Actions** - CI/CD pipeline for seamless publishing

## Architecture

- **Content:** Blog posts in `content/posts/`, written in Markdown with TOML frontmatter
- **Theme:** Git submodule pointing to archie-zola theme for easy updates
- **Deployment:** Fully automated via GitHub Actions on every push to master
- **Config:** Single `config.toml` file for all site settings

## Development

```bash
# Start development server
make serve

# Build for production  
make build

# Initialize theme (first time setup)
make init-theme

# Update theme to latest version
make update-theme
```

## Deployment

Fully automated! Just push to master:

```bash
git push origin master
```

The GitHub Actions workflow automatically:
1. Builds the site with Zola
2. Deploys to GitHub Pages
3. Makes it live at simeg.github.io

## Why This Stack?

- **Zola** for speed and simplicity - no JavaScript build process needed
- **GitHub Pages** for free, reliable hosting with custom domain support
- **Minimal dependencies** - just Rust (Zola) and Git submodules
- **Git-based workflow** - write posts in your favorite editor, commit, and deploy

---

Built with ❤️ and deployed automatically via GitHub Actions.