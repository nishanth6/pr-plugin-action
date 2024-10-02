# PR Plugin Action

This GitHub Action allows you to create a pull request automatically between branches.

## Inputs

- `github_token`: **Required**. GitHub token to authenticate the action.
- `base_branch`: **Required**. The base branch for the pull request (e.g., `main`).
- `head_branch`: **Required**. The branch with the changes (e.g., `feature-branch`).
- `pr_title`: **Required**. The title of the pull request.
- `pr_body`: Optional. The body text for the pull request.

## Example usage

```yaml
name: 'Create Pull Request'
on:
  push:
    branches:
      - 'feature-branch'

jobs:
  create_pr:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Create Pull Request
        uses: your-github-username/pr-plugin-action@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          base_branch: 'main'
          head_branch: 'feature-branch'
          pr_title: 'My New Feature'
          pr_body: 'This PR introduces a new feature.'
