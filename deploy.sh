#!/usr/bin/env bash
# ============================================================
#  Publish this portfolio to https://nizambhl2001.github.io
#  Usage:  ./deploy.sh            (uses GitHub username + PAT)
#          ./deploy.sh <TOKEN>    (non-interactive)
# ============================================================
set -euo pipefail

REPO="nizambhl2001/nizambhl2001.github.io"
USER_NAME="nizambhl2001"
SITE="https://nizambhl2001.github.io"
BRANCH="main"

cd "$(dirname "$0")"

TOKEN="${1:-}"
if [ -z "$TOKEN" ]; then
  echo "Paste a GitHub Personal Access Token with 'repo' scope"
  echo "(create one at https://github.com/settings/tokens — push access to $REPO)"
  read -rsp "Token: " TOKEN
  echo
fi
if [ -z "$TOKEN" ]; then
  echo "No token supplied — aborting." >&2
  exit 1
fi

if [ ! -d .git ]; then
  git init -q
  git remote add origin "https://github.com/${REPO}.git"
fi
git remote set-url origin "https://github.com/${REPO}.git"
git config user.name >/dev/null 2>&1 || true

git add -A
git commit -q -m "Professional portfolio website" || echo "(nothing new to commit)"
git branch -M "$BRANCH"

echo "→ Pushing to ${REPO} (${BRANCH})…"
git -c credential.helper= \
    push "https://${USER_NAME}:${TOKEN}@github.com/${REPO}.git" "${BRANCH}:${BRANCH}" --force

echo
echo "✅ Pushed. Next steps (one time only):"
echo "   1. Open https://github.com/${REPO}/settings/pages"
echo "   2. Source: 'Deploy from a branch' → Branch: ${BRANCH} → Folder: / (root) → Save"
echo "   3. Wait ~1 minute, then visit ${SITE}"
echo
echo "Later updates: run this script again."
