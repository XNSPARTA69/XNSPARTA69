name: Update README

on:
  schedule:
    # Ejecuta el workflow diariamente a las 00:00 UTC
    - cron: '0 0 * * *'
  workflow_dispatch: # Permite ejecución manual del workflow

jobs:
  update-readme:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set Up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests

      - name: Run update_readme.py
        run: python update_readme.py

      - name: Push Changes
        uses: ad-m/github-push-action@v0.6.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: main
          force: true
