# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal blog/website built with [Zola](https://www.getzola.org/), a fast static site generator written in Rust. The site uses the `archie-zola` theme, which is a Zola port of the Archie theme that provides a clean, minimal design with dark/light mode toggle support.

## Architecture

- **Static Site Generator**: Zola
- **Theme**: `archie-zola` (located in `themes/archie-zola/`)
- **Content**: Blog posts in `content/posts/` directory
- **Templates**: Custom templates in `templates/` directory, with theme templates in `themes/archie-zola/templates/`
- **Static Assets**: Generated into `public/` directory
- **Configuration**: Main config in `config.toml`

## Essential Commands

### Development Server
```bash
make serve
# or directly:
zola serve
```
This starts a local development server with live reload.

### Build Site
```bash
zola build
```
Generates the static site into the `public/` directory.

### Check Site
```bash
zola check
```
Validates content and links.

### Deploy to GitHub Pages

**Option 1: Manual Deployment**
```bash
make deploy
```
Builds and deploys to gh-pages branch using git worktree.

**Option 2: Automatic Deployment (GitHub Actions)**
The site automatically deploys when you push to master branch using the workflow in `.github/workflows/deploy.yml`.

## Content Structure

- **Blog Posts**: Located in `content/posts/`
- **Front Matter**: Uses TOML format with `+++` delimiters
- **Templates**: Theme templates are used from `themes/archie-zola/templates/`

## Configuration Notes

The site is configured in `config.toml` with:
- Base URL: `https://mywebsite.com`
- Theme: `archie-zola`
- Author: "Simon"
- Dark mode: Toggle mode enabled
- Search: Disabled
- Syntax highlighting: Enabled with `base16-ocean-dark` theme

### Theme Customization
The theme supports extensive customization through the `[extra]` section:
- Dark/light mode toggle
- Social links in footer
- Custom menus and navigation
- Google Analytics integration

## File Organization

- `content/posts/` - Blog posts and blog index
- `themes/archie-zola/` - Theme files (git submodule)
- `static/` - Static assets (copied to public)
- `sass/` - Sass stylesheets (compiled to CSS)
- `public/` - Generated site output (gitignored)

## Development Workflow

### Manual Workflow
1. Start development server: `make serve`
2. Create new blog posts in `content/posts/`
3. Build for production: `make build`
4. Deploy to GitHub Pages: `make deploy`

### Automatic Workflow (Recommended)
1. Start development server: `make serve`
2. Create new blog posts in `content/posts/`
3. Commit and push to master: `git push origin master`
4. GitHub Actions automatically builds and deploys

## GitHub Pages Setup

The repository includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that:
- Triggers on pushes to master branch
- Installs Zola and builds the site
- Deploys to GitHub Pages using the modern Pages API
- Uses proper permissions and security settings

To enable automatic deployment:
1. Go to repository Settings → Pages
2. Set Source to "Deploy from a branch" 
3. Set Branch to "gh-pages" and folder to "/ (root)"
4. Push to master branch to trigger deployment

## Theme Management

The `archie-zola` theme is included as a git submodule. To update:
```bash
make update-theme
```