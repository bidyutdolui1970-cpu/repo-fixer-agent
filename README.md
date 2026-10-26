# repo-fixer-agent

Open-source coding agent, built with GitHub Copilot, that helps fix and improve code.

## What it does

`repo-fixer-agent` looks at a codebase, identifies common issues, and proposes actionable fixes.

- Scans a repository for obvious maintenance problems
- Detects TODO/FIXME markers and missing project documentation
- Explains findings in plain language
- Provides a lightweight command-line interface for quick repository checks

## Built with

- [GitHub Copilot](https://github.com/features/copilot) for scaffolding, code generation, and debugging support
- Python 3.11

## Features

- Repository scanning for common quality issues
- Fast CLI usage from any local checkout
- Extensible structure for future automation and fix suggestions

## Getting started

```bash
git clone https://github.com/bidyutdolui1970-cpu/repo-fixer-agent.git
cd repo-fixer-agent
python3 -m venv .venv
source .venv/bin/activate
python3 repo_fixer_agent.py --path .
```

## Usage

```bash
python3 repo_fixer_agent.py --path ./my-project
```

Example output:

```text
Repository scan for /path/to/project

Issues found:
- README.md is missing
- src/app.py contains TODO/FIXME markers
```

## How it was built

This project was created with the help of GitHub Copilot. Copilot assisted with the initial project layout, the CLI structure, and the repository health checks that make this tool useful as a starting point for more advanced automated repair workflows.

## Contributing

Issues and pull requests are welcome. Fork the repository, create a branch, and open a pull request with a clear description of the change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
