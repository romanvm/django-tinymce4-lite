# Contributing django-tinymce4-lite

## Submitting Issues

When creating issue tickets please provide as much information as possible,
including:

- Detailed description of your issue (not just "does not work").
- Python and Django version.
- Your project setup.
- Steps to reproduse the issue.
- Exception traceback if this is a back-end issue.
- Browser console output if this is a front-end issue.

## Creating Pull Requests

Any help with developing `django-tinymce4-lite` is always appreciated. When
submitting pull requests please follow these rules:

- PRs should be submited into `develop` branch.
- Python code must follow `PEP-8` style conventions.
- Docstrings must have Sphinx-compatible ReStructuredText formatting.
- Please provide a short rationale on why do you think this change is needed.
- If a PR introduces a new feature, please add a corresponding test case
  to the test suite, unless the change is trivial.
- All tests in the Travis CI build matrix must pass.
- Any changes to the API should be reflected in the project documentation.
