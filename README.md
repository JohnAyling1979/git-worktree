# Git Worktrees & Multi-Agent Workflows

## What is a Git Worktree?

A worktree creates an independent working directory from a single repo. Each worktree gets its own copy of the files on its own branch, but shares the same git database (history, objects, remotes). This makes them fast and lightweight compared to cloning.

```
project/                          <- main repo
├── .git/                          <- the REAL git database (shared)
├── app.py

.claude/worktrees/feature-xyz/    <- worktree
├── .git                           <- tiny FILE pointing back to project/.git/
├── app.py                         <- independent copy of files
```

## Commands

### Create a worktree

```bash
# Create a worktree with a new branch based on current HEAD
git worktree add <path> -b <branch-name>

# Example
git worktree add .claude/worktrees/my-feature -b feature-auth

# Claude Code shorthand (auto-creates path and branch)
claude --worktree my-feature
```

### List worktrees

```bash
git worktree list
```

### Remove a worktree

```bash
git worktree remove <path>
```

### Merge a worktree branch back into main

```bash
# 1. Review what the branch changed
git diff main..<branch-name>

# 2. Switch to main (if not already there)
git checkout main

# 3. Merge the branch
git merge <branch-name> --no-edit

# 4. Clean up the worktree directory
git worktree remove <path>

# 5. Delete the branch
git branch -D <branch-name>
```

### Push a worktree branch to remote (e.g. to continue work elsewhere)

```bash
git push origin <branch-name>
```

## General Flow

```
1. Create worktree(s)       Work happens on isolated branches
   ┌──────────────┐         in separate directories.
   │  main repo   │         The main branch stays untouched.
   │  (untouched) │
   └──────┬───────┘
          │
   ┌──────┴───────┐
   │              │
   ▼              ▼
┌──────┐     ┌──────┐
│ WT 1 │     │ WT 2 │     2. Agents/developers work in parallel
│ adds │     │ adds │        without file conflicts.
│ feat │     │tests │
└──┬───┘     └──┬───┘
   │             │
   ▼             ▼
  commit        commit       3. Commit work on each branch.

   │             │
   └──────┬──────┘
          │
          ▼
   ┌──────────────┐
   │  git merge   │          4. Merge branches into main.
   │  (per branch)│             Resolve conflicts if any.
   └──────┬───────┘
          │
          ▼
   ┌──────────────┐
   │   cleanup    │          5. Remove worktree dirs and branches.
   │  worktrees   │
   └──────────────┘
```

## Key Points

- Worktrees share the git database -- no duplicated history, instant creation
- The worktree directory does NOT need to be tracked (add to `.gitignore`)
- Merging worktree branches is standard `git merge` -- nothing special
- Conflicts are handled the same way as any merge conflict
- Always commit/push before leaving -- uncommitted changes live only in the worktree directory
- The branch is what matters, not the directory. You can delete the worktree and still merge the branch
