# Security Policy

## Supported Versions

This project is under active development. Security fixes are applied to the
latest version on the `main` branch.

## Reporting a Vulnerability

If you discover a security vulnerability, please **do not** open a public issue.

Instead, report it privately by opening a
[GitHub security advisory](https://github.com/Prithvi8706/quantum-water-optimizer/security/advisories/new)
or contacting the maintainer directly.

Please include:

- A description of the vulnerability and its potential impact.
- Steps to reproduce.
- Any suggested mitigation, if known.

We will acknowledge your report as soon as possible and keep you informed of the
progress toward a fix.

## Sensitive Data

Never commit API tokens, D-Wave Leap credentials, or `.env` files. These are
excluded via `.gitignore`. If a secret is accidentally committed, rotate it
immediately.
