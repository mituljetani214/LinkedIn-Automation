# Career Intake System

Phase 1.5 turns raw career information into structured source-of-truth files.

Use this folder before generating LinkedIn profile copy, posts, recruiter outreach, portfolio case studies, or resume variants.

## Workflow

1. Fill `intake/master-career-intake.md`.
2. Add one file per strong project using `intake/project-intake-template.md`.
3. Fill `intake/linkedin-profile-intake.md` with current LinkedIn profile text.
4. Fill `intake/writing-voice-intake.md` so content sounds like Mitul.
5. Run the completeness checker:

```powershell
python scripts/check_career_intake.py
```

6. Move verified facts into:

- `career/profile.md`
- `career/resume.md`
- `career/projects.md`
- `career/skills.md`
- `career/metrics.md`
- `knowledge/writing-style.md`

## Quality Rule

Anything not supported by intake answers, resume details, project evidence, or metrics should be treated as a draft assumption.

## Done Criteria

Phase 1.5 is usable when:

- Master career intake is complete
- At least 2 projects are documented
- LinkedIn profile text is captured
- Writing voice examples are captured
- Missing metrics are listed clearly

