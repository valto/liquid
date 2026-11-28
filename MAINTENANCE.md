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

## Reader guides and agent prompts

Reader guides use `kind: reader` and a `reader` record containing the stable slug, label, perspective, main question, focus and an ordered reading list. Reading items reference existing page IDs and explain why each source matters. Edit the guide's Markdown for its substantive explanation; use `@@READING@@` to include the registry's reading list. `@@READERS@@` produces guide cards on HTML pages and a linked list in their Markdown source copies.

The build generates `readers.json`, `readers/{slug}/agent-prompt.txt` and its Markdown equivalent from the same records. The dedicated `/agents/` page uses the general prompt. Keep profiles editorial and self-selected, and preserve shared definitions, attribution and evidence status. New guides retain null publication dates until their actual approved publication.

Copy and print controls use one local asset, `assets/reader-tools.js`. The validator permits only that deferred script alongside structured JSON metadata; it rejects inline handlers and other executable scripts. Reading and prompt downloads remain available without JavaScript. Copy failure opens and selects the full prompt for manual copying. Print output includes the complete prompt on the agent page and the substantive summary on reader pages.

For changes to these controls, run the focused browser checks as well as the build and content validator:

```sh
node scripts/check_reader_tools.mjs
```

After a change confined to print styling, use `node scripts/check_reader_tools.mjs --print-only` to check and render the affected print outputs without repeating unchanged interaction checks.

The check requires the existing Playwright Core and Chrome installation. Override `PLAYWRIGHT_CORE_PATH`, `CHROME_PATH` or `LIQUID_PREVIEW_PORT` when needed; it starts and stops its own loopback preview server.
