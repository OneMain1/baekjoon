# Claude Skill: Python Concept Management

## Purpose
Efficiently manage Python concepts learned during problem-solving sessions by maintaining a well-structured, deduplicated concept.md file with improved readability.

## Workflow

### When learning new concepts:
1. **Check existing concepts**: Search concept.md for similar entries
2. **Evaluate duplication**: Determine if concept already exists or is similar
3. **Add/Update**: 
   - If new: Add to appropriate section in concept.md
   - If similar: Enhance existing entry
   - If duplicate: Skip addition

### Concept Entry Format (Markdown):
```markdown
### Function/Concept Name
Brief description
- Key point 1
- Key point 2
- Example: `code_example`
```

## Usage Instructions

### For User:
- Mention new concepts learned during problem solving
- Ask to "update concept.md with [concept]"

### For Claude:
1. Read current concept.md
2. Search for similar concepts using keywords
3. If not found: Add new entry to appropriate section
4. If found: Compare and potentially merge/update
5. Maintain organized sections and clear formatting
6. Use markdown features for better readability

## Example Commands:
- "Add enumerate() function to concepts"
- "Update concept.md with list comprehensions"
- "Check if binary search is already in concepts"

## File Structure:
- `concept.md` - Main concept database (Markdown format)
- `claude skill.md` - This instruction file

## Benefits of Markdown Format:
- Better readability with headers and sections
- Syntax highlighting for code examples
- Easy navigation with table of contents
- Better formatting for complex concepts