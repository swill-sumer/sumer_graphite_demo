# Sumer Graphite demo

This repository is a **hands-on sandbox** for learning [**Graphite**](https://graphite.dev/) — the `gt` CLI that makes **stacked pull requests** (branches chained on top of each other) feel like a normal part of your workflow.

- **Stacking** means: PR B is based on PR A, not on `main`, so you can keep shipping incremental commits while earlier PRs are in review. See [stacking.dev](https://stacking.dev/) for the “why.”
- **Graphite** automates branch creation, rebasing/restacking, and opening/updating GitHub PRs so the stack stays coherent.

Official docs: [CLI quick start](https://graphite.dev/docs/cli-quick-start), [CLI tutorials](https://graphite.dev/docs/cli-tutorials), [command reference](https://graphite.dev/docs/command-reference).

---

## Prerequisites

- **Git** and **GitHub** access to this repository
- **Graphite CLI** (`gt`): [Install Graphite](https://graphite.dev/docs/install-the-cli)
- Authenticate once (follow the CLI prompts):

  ```bash
  gt auth
  ```

---

## One-time: initialize Graphite in this clone

After you clone this repo locally:

```bash
cd sumer_graphite_demo
gt init
```

Choose **`main`** as the trunk when prompted. Graphite stores repo config under `.git/` (see [Quick Start — Initializing Graphite](https://graphite.dev/docs/cli-quick-start)).

---

## Demo scenario: three stacked PRs

You will add small, reviewable slices to `src/sumer_demo.py` — **each slice is its own PR**, stacked so PR 2 depends on PR 1, and PR 3 on PR 2.

### 0. Start from trunk

```bash
gt checkout main
git pull
```

### 1. First PR — add `greet`

Edit `src/sumer_demo.py` and add a simple function, for example:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

Create a branch **and** a single commit in one step, then open a PR:

```bash
gt create --all --message "feat(demo): add greet()"

gt submit
```

You now have **one** open PR against `main`.

### 2. Second PR — stack on top of the first

Stay in the flow: build the **next** change on top of the branch you just created (Graphite tracks the stack).

```bash
# Optional: confirm you're on the first feature branch
gt log short
```

Add another function that uses `greet`, e.g. `wave(name)` that returns something like `"👋 " + greet(name)`.

```bash
gt create --all --message "feat(demo): add wave() using greet"

gt submit --stack
```

`--stack` pushes and creates/updates PRs for **the whole stack** so the second PR targets the first branch, not `main` directly.

### 3. Third PR — tests or a tiny CLI

Again from the **top** of your stack, add e.g. a `if __name__ == "__main__":` block that prints `wave("Graphite")`, or a `test_greet` in a new `tests/test_sumer_demo.py`.

```bash
gt create --all --message "test(demo): exercise greet and wave"

gt submit --stack
```

### Inspect the stack locally

```bash
gt log short    # or: gt ls
```

Open the top PR in Graphite’s UI:

```bash
gt top
gt pr
```

---

## Reviewer feedback (the interesting part)

If a reviewer asks for a change **in an earlier PR** in the stack, use **`gt modify`** so everything **above** that PR is restacked automatically.

Example: you’re on the bottom branch of the stack and you edited files:

```bash
gt modify --all
gt submit --stack
```

Or amend the last commit on the current branch:

```bash
gt modify -a
gt submit --stack
```

See [Quick Start — Addressing reviewer feedback](https://graphite.dev/docs/cli-quick-start).

---

## Staying in sync with `main`

When `main` moves forward (other people merge, or you merge the bottom PR):

```bash
gt sync
```

This pulls trunk, restacks open branches, and can prompt you to delete merged local branches. Resolve any conflicts where indicated, then continue with `gt restack` if needed.

---

## What’s in this repo

| Path | Purpose |
|------|---------|
| `src/sumer_demo.py` | Tiny module you extend across stacked PRs |
| `README.md` | This walkthrough |

---

## Next steps

- Run through the three PRs above in a **scratch clone** first if you want to avoid noise on the real repo.
- Read [Create PRs for a stack](https://graphite.dev/docs/create-submit-prs) for merge strategies and CI behavior across stacks.

When you’re done experimenting, merge from the Graphite UI (or your usual process), then `gt sync` locally to clean up.
