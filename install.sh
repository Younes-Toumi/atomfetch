#!/bin/bash

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_DIR="$HOME/.local/bin"

echo "Installing Atomfetch..."

mkdir -p "$BIN_DIR"

ln -sf "$PROJECT_DIR/atomfetch" "$BIN_DIR/atomfetch"

echo "Atomfetch installed."
echo "Run it with: atomfetch"