# Contributing

Edit canonical Markdown and site/pages.json, then build and validate. Keep concept IDs and published PDF versions stable. Explain substantive definition or meaning changes, cite primary sources and flag unresolved contradictions. Do not submit private conversations or credentials.

```sh
python3 -m pip install -r requirements.txt
python3 scripts/build_site.py
python3 scripts/validate_site.py
python3 scripts/build_site.py --check
```

Generated docs/ is committed for review and raw-file access. CI checks that it matches canonical inputs. Public release and license changes require the owner decision described in GOVERNANCE.md.
