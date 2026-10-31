#!/usr/bin/env bash
# ==============================================================================
# Profile Sync Helper for amritkr1999/amritkr1999
# Usage: ./sync.sh ["optional custom commit message"]
# ==============================================================================

set -e

# Terminal colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}==> Syncing GitHub Profile (amritkr1999)...${NC}"

# Check for uncommitted changes
if [ -z "$(git status --porcelain)" ]; then
  echo -e "${YELLOW}No changes detected in repository.${NC}"
  exit 0
fi

# Determine commit message
MESSAGE="$1"
if [ -z "$MESSAGE" ]; then
  TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
  MESSAGE="chore(profile): update profile README & assets ($TIMESTAMP)"
fi

# Stage, commit, and push
git add .
git commit -m "$MESSAGE"

echo -e "${BLUE}==> Pulling latest remote changes...${NC}"
git pull --rebase origin main

echo -e "${BLUE}==> Pushing updates to GitHub...${NC}"
git push origin main

echo -e "${GREEN}✔ Profile successfully synced and live on GitHub!${NC}"
echo -e "Check your profile at: ${BLUE}https://github.com/amritkr1999${NC}"
