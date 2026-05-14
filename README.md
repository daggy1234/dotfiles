# Arnav's Dotfiles

macOS dotfiles managed with [GNU Stow](https://www.gnu.org/software/stow/).

## What's Included

```
dotfiles/
├── brew/
│   └── Brewfile              # Homebrew formulae, casks, taps, VS Code extensions
├── git/
│   └── .gitconfig            # Git user, GPG signing, credentials
├── vscode/
│   └── extensions.json       # VS Code extensions list
└── zsh/
    ├── .zshrc                # Shell config, aliases, PATH
    └── .p10k.zsh             # Powerlevel10k theme config
```

## Quick Start

```sh
# 1. Install Homebrew (skip if already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Clone
git clone https://github.com/arnavjindal/dotfiles.git ~/dotfiles
cd ~/dotfiles

# 3. Install stow and all packages from the Brewfile
brew install stow
brew bundle --file=brew/Brewfile

# 4. Back up existing configs (if any)
[ -f ~/.zshrc ] && mv ~/.zshrc ~/.zshrc.bak
[ -f ~/.p10k.zsh ] && mv ~/.p10k.zsh ~/.p10k.bak
[ -f ~/.gitconfig ] && mv ~/.gitconfig ~/.gitconfig.bak

# 5. Symlink everything
stow -t ~ zsh git
```

That's it. Open a new terminal and you're good to go.

## VS Code Extensions

Extensions are included in the Brewfile and installed by `brew bundle`. To install them separately:

```sh
cat vscode/extensions.json | jq -r '.extensions[]' | xargs -L 1 code --install-extension
```

## Post-Install

- **Powerlevel10k** is included — run `p10k configure` to recustomize the prompt.
- **GPG signing** — import your GPG key for signed commits.
- **Atuin** — run `atuin register` or `atuin login` for shell history sync.
- **rbenv** — run `rbenv install <version>` for Ruby.
- **Conda** — install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) if needed.

## Shell Aliases

Modern CLI replacements configured in `.zshrc` (all installed via Brewfile):

| Alias  | Replacement | Replaces |
|--------|-------------|----------|
| `ls`   | `eza`       | `ls`     |
| `find` | `fd`        | `find`   |
| `du`   | `dust`      | `du`     |
| `df`   | `duf`       | `df`     |
| `grep` | `rg`        | `grep`   |
| `ping` | `gping`     | `ping`   |
| `time` | `hyperfine` | `time`   |

## Updating

```sh
# Save current Homebrew state
brew bundle dump --file=~/dotfiles/brew/Brewfile --force

# Export VS Code extensions
code --list-extensions | jq -R -s 'split("\n") | map(select(. != "")) | {extensions: .}' > ~/dotfiles/vscode/extensions.json
```
