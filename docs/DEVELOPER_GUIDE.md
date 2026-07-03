# AlexOS Developer Guide

Version: 1.0

---

# Purpose

This document defines the engineering workflow for AlexOS.

Its purpose is to keep the project consistent, maintainable and scalable.

Every developer working on AlexOS should follow this guide.

---

# Standard Development Workflow

Every development session starts with:

```bash
cd ~/AlexAI
source .venv/bin/activate
```

---

Before writing code:

```bash
git status
pytest
```

The project must always start from a healthy state.

---

After writing code:

```bash
pytest
```

All tests must pass before committing.

---

Commit changes:

```bash
git add .
git commit -m "Meaningful commit message"
git push
```

---

# Running AlexOS

```bash
python -m app.main
```

---

# Running Tests

Run all tests:

```bash
pytest
```

Run one test:

```bash
pytest tests/test_cognitive_loop.py
```

Quiet mode:

```bash
pytest -q
```

---

# Git Commands

Current status:

```bash
git status
```

Recent commits:

```bash
git log --oneline --decorate -10
```

Push changes:

```bash
git push
```

Pull latest changes:

```bash
git pull
```

---

# Creating New Modules

Create source file:

```bash
touch app/core/example.py
open -e app/core/example.py
```

Create test:

```bash
touch tests/test_example.py
open -e tests/test_example.py
```

---

# Project Structure

Show directory tree:

```bash
tree -L 4
```

List all project files:

```bash
find app tests docs -type f | sort
```

---

# Project Snapshot

Before every major milestone create a project snapshot.

```bash
{
echo "===== GIT ====="
git log --oneline --decorate -10

echo
echo "===== STATUS ====="
git status

echo
echo "===== TREE ====="
tree -L 4

echo
echo "===== FILES ====="
find app tests docs -type f | sort

echo
echo "===== TESTS ====="
pytest -q
} > project_snapshot.txt

cat project_snapshot.txt
```

---

# Main Documentation

Core project documents:

- README.md
- ARCHITECTURE.md
- MASTER_PLAN.md
- ROADMAP.md
- DOMAIN_MODEL.md
- COGNITIVE_ARCHITECTURE.md
- COGNITIVE_CORE.md
- DEVELOPER_GUIDE.md

---

# Development Principles

## Rule 1

ROADMAP.md is the primary source of truth.

Never skip roadmap stages.

---

## Rule 2

Architecture comes before implementation.

Understand the component first.

Code second.

---

## Rule 3

Every new feature must include tests.

No exceptions.

---

## Rule 4

Every commit must leave the project in a working state.

---

## Rule 5

Small commits are preferred.

One logical change per commit.

---

## Rule 6

StorageManager is the only entry point to Long-Term Memory.

CognitiveLoop must never communicate directly with:

- ChromaDB
- Graph Memory
- Embedding Engine

---

## Rule 7

Context is more important than agents.

AlexOS is built around cognitive context.

---

## Rule 8

AlexOS stores knowledge, not conversations.

Conversation

↓

CognitiveEvent

↓

Knowledge

↓

Memory

---

## Rule 9

Every development session starts with:

1. Activate venv

2. git status

3. pytest

Only then begin development.

---

## Rule 10

Before every major version:

- create Project Snapshot;
- review ROADMAP;
- review ARCHITECTURE;
- ensure all tests pass.

---

# Commit Naming Convention

New feature:

```
v1.8.2 Add ChromaDB interface
```

Documentation:

```
docs Update developer guide
```

Maintenance:

```
chore Ignore project archives
```

Bug fix:

```
fix Resolve context builder bug
```

Refactoring:

```
refactor Simplify CognitiveLoop
```

---

# AlexOS Philosophy

AlexOS is not a chatbot.

AlexOS is a Cognitive Operating System.

The objective is not to answer questions.

The objective is to build a continuously improving cognitive model of its owner.

Every component should support this vision.

---

# Audit Before Every Major Release

Before releasing any major version of AlexOS:

1. Activate virtual environment

```bash
source .venv/bin/activate
```

2. Verify repository

```bash
git status
```

3. Run all tests

```bash
pytest
```

4. Generate Project Snapshot

5. Review ROADMAP

6. Review ARCHITECTURE

7. Review CHANGELOG

8. Review commit history

```bash
git log --oneline --decorate -15
```

9. Push latest changes

10. Create Git Tag


---

# Running AlexOS with Ollama

AlexOS currently uses local LLM infrastructure through Ollama.

## Check Ollama

```bash
ollama list
ollama ps
curl http://127.0.0.1:11434/api/tags
```

If `curl` returns a list of models, Ollama is running.

---

## Start Ollama Server

If Ollama is not running, start it in a separate terminal:

```bash
ollama serve
```

Keep this terminal open.

---

## Check Local Model

Example:

```bash
ollama run qwen3:4b
```

Exit model chat:

```text
/bye
```

or:

```text
Ctrl + D
```

---

## Run AlexOS Terminal

Open a new terminal:

```bash
cd ~/AlexAI
source .venv/bin/activate
python -m app.main
```

Exit AlexOS:

```text
/exit
```

---

## Recommended Startup Sequence

Terminal 1:

```bash
ollama serve
```

Terminal 2:

```bash
cd ~/AlexAI
source .venv/bin/activate
pytest
python -m app.main
```
