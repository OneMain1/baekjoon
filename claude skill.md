# Claude Skill: Python Concept Management

## Purpose
Efficiently manage Python concepts learned during problem-solving sessions by maintaining a concise, deduplicated concept.txt file.

## Workflow

### When learning new concepts:
1. **Check existing concepts**: Search concept.txt for similar entries
2. **Evaluate duplication**: Determine if concept already exists or is similar
3. **Add/Update**: 
   - If new: Add to concept.txt
   - If similar: Enhance existing entry
   - If duplicate: Skip addition

### Concept Entry Format:
```
**Function/Concept**: Brief description
- Key points (1-2 lines max)
- Example: `code_example`
```

## Usage Instructions

### For User:
- Mention new concepts learned during problem solving
- Ask to "update concept.txt with [concept]"

### For Claude:
1. Read current concept.txt
2. Search for similar concepts using keywords
3. If not found: Add new entry
4. If found: Compare and potentially merge/update
5. Keep entries concise (max 3 lines each)

## Example Commands:
- "Add map() function to concepts"
- "Update concepts with list unpacking"
- "Check if sorting is already in concepts"

## File Structure:
- `concept.txt` - Main concept database
- `claude skill.md` - This instruction file