# AlexOS Boot Protocol

---

# AlexOS! Hola Amigo!

This is the official boot command of the AlexOS project.

Whenever a developer or an AI assistant receives the command:

    AlexOS! Hola Amigo!

it means that the AlexOS engineering session officially begins.

---

# Mission

Synchronize with the current state of AlexOS before writing a single line of code.

Never guess.

Never skip steps.

Continue only from the latest stable architecture.

---

# Boot Sequence

Always execute the following order.

## 1. Read documentation

Read in this exact order:

1. BOOT_PROTOCOL.md
2. ROADMAP.md
3. MASTER_PLAN.md
4. ARCHITECTURE.md
5. COGNITIVE_ARCHITECTURE.md
6. DEVELOPER_GUIDE.md
7. CHANGELOG.md
8. IDENTITY_MODEL.md (if available)

---

## 2. Detect current project state

Determine:

- Current version
- Current Roadmap stage
- Last stable release
- Current development milestone

---

## 3. Verify engineering state

Review:

- Git history
- Current branch
- Working tree
- Test status
- Latest release tag

---

## 4. Engineering Rules

AlexOS always follows:

Architecture

↓

Implementation

↓

Tests

↓

Commit

↓

Push

Never change this order.

---

## 5. Project Principles

1. Documentation First

2. Roadmap is the Source of Truth

3. Architecture Before Code

4. Small Commits

5. GitHub is the Canonical History

6. Tests Before Every Commit

7. Working Tree Should Stay Clean

8. Every Major Version Ends With an Audit

9. Never Skip Roadmap Stages

10. Continue From the Latest Stable State

---

## 6. Communication Rules

When AlexOS Boot starts:

- understand the project first;
- never rewrite existing architecture without reason;
- preserve previous decisions;
- continue the project instead of restarting it.

---

## 7. Terminal Workflow

Typical development session:

```bash
cd ~/AlexAI
source .venv/bin/activate

git status
pytest
```

After implementation:

```bash
git add ...

git commit -m "..."

git push
```

---

## 8. Ollama Workflow

Start Ollama:

```bash
ollama serve
```

Verify:

```bash
ollama list
ollama ps
```

Run AlexOS:

```bash
python -m app.main
```

---

## 9. Release Workflow

Every stable release must finish with:

- Audit
- CHANGELOG update
- ROADMAP update
- Documentation update
- Git Tag
- GitHub Push

---

## Boot Complete

When everything above has been verified, AlexOS may answer:

> Hola, Amigo!

> AlexOS Boot Protocol loaded.

> Documentation synchronized.

> Roadmap synchronized.

> Engineering state verified.

> Ready to continue development.
