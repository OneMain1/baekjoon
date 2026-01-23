# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Baekjoon Online Judge (BOJ) competitive programming repository. Solutions are written in Python 3 for problems from the BaaaaaaaaaaarkingDog workbook series.

## Running Solutions

Solutions are standalone Python scripts that read from stdin and write to stdout:

```bash
python 0x01/1267.py < input.txt   # Run with file input
python 0x01/1267.py               # Run with manual input
```

## Repository Structure

- `0x01/`, `0x02/`, etc. - Problem solutions organized by workbook chapter
- `concept.md` - Python concepts reference (managed via `/concept` skill)

## Development Workflow

- Each problem solution gets its own commit with the problem number as the message
- Multiple solution approaches per problem are encouraged (show both basic and optimized versions)
- Update `concept.md` when learning new Python patterns

## Using the /concept Skill

When learning a new Python concept, use `/concept` to add it to `concept.md`. The skill checks for duplicates and maintains consistent formatting.

## Solution Style

- Use standard library only (no external packages)
- Include multiple solution approaches when applicable
- Follow stdin/stdout I/O patterns for BOJ compatibility
