# Build and maintain Liquid Software

The canonical inputs are Markdown documents, `site/pages.json` and explicitly selected assets. `docs/` contains generated output. The static build needs Python 3.12 and the pinned dependency in `requirements.txt`.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/build_site.py
.venv/bin/python scripts/build_site.py --check
.venv/bin/python scripts/validate_site.py
.venv/bin/python scripts/serve_preview.py --port 18790
```

Open the printed localhost address under `/liquid/`. Stop the preview with Ctrl-C. Choose another port with `--port` if necessary.

Edit source Markdown rather than generated HTML. Add a concept by creating its Markdown file and one registry record with a stable ID, unique path, definition, thesis, principles, scope, relationships, conceptual source and version information. Unknown origin dates remain null. Record actual website publication dates separately from concept origins and paper edition dates. The build generates its page, source copy, index cards, JSON and discovery files together.

For a new paper, retain the prior edition, add the new canonical source and PDF, and register the landing page and version-specific asset hash. A corrected version receives a new version path. Never overwrite the supplied umbrella PDF or describe a research draft as an approved final paper.

Run both checks after a build and commit canonical inputs together with generated output. Validation runs on pushes and pull requests. The Pages workflow validates the exact generated files on main and deploys only when the owner-approved `LIQUID_PUBLICATION_APPROVED` repository variable is true. Use reviewed pull requests for substantive changes; permission to edit does not itself approve publication.

The initial release was authorized by Valto on 26 November 2026 with CC BY 4.0 content and MIT code terms. For subsequent releases, obtain the applicable approval for substantive public changes, retain actual publication dates, update release status and rebuild. Verify the workflow and live HTTPS pages before issuing the selected release tag. The Pages approval variable is scoped to reviewed release content; it is not blanket approval to change canonical definitions.

Rollback uses the preceding accepted commit and deployment; preserve versioned paper assets and source history. GitHub Pages deployment does not transfer authority over PIOS, EIOS, CRD or PAIX definitions.
