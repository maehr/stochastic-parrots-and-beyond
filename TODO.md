# Open Tasks

The course site is built. The tasks below need a decision by the instructors, an external service, or a check by a person.

## Owner Labels

| Label      | Meaning                                                                       |
| ---------- | ----------------------------------------------------------------------------- |
| `[Agent]`  | A coding agent can do this directly in the repository.                        |
| `[Shared]` | An agent can prepare the work, but a maintainer approves the external action. |
| `[Manual]` | Complete this in GitHub, Zenodo, or another external service.                 |

## Approve the Content

- [x] `[Manual]` Approve the timetable in `contents/_timetable.qmd`. Then set `detailed_program_status: approved` in `data/editions.yml`.
- [ ] `[Manual]` Approve the four documented cases: BLOOM, LAION-5B, Sama and OpenAI, and the Llama 2 license.
- [x] `[Manual]` Approve the eight-hour preparation plan in `contents/assignments.qmd`.
- [ ] `[Manual]` Confirm the deadline of the follow-up task with GRACE. Then set `assessment_deadline` in `data/editions.yml`.
- [ ] `[Manual]` Read the lens pages and the decks for accuracy and tone. Laura Wagner and Moritz Mähr both sign off.
- [x] `[Manual]` Approve the formal check and the discussion with a domain-expert peer. The instructors check the form only. Laura Wagner and GRACE both agree.
- [ ] `[Manual]` Create the `use-statement` label on GitHub. The Use Statement issue form uses it.
- [x] `[Manual]` Approve the two submission channels: email to GRACE, or the public GitHub issue form. Publication on the site stays opt-in.
- [ ] `[Manual]` Ask GRACE for the language of instruction. Then state it on the course description.
- [ ] `[Manual]` Verify whether GRACE or other stakeholders need to approve the revised format of issue 12: Lens groups, two Panarchy blocks without Ecocycle, and the individual Action Plan. Check whether the official course listing needs the same change.
- [ ] `[Manual]` Review the sixteen guiding questions in `contents/lenses/_guiding-questions-0N.qmd`. Laura Wagner and Moritz Mähr both sign off.

## HS 2026 Operations

These tasks hold no participant data. Keep all participant data outside this repository.

- [ ] `[Manual]` By 21 October 2026: send the registered participants the course message with a link to the HS 2026 page. Copy grace@unibas.ch.
- [ ] `[Manual]` Before 4 November 2026: arrange the welcome with GRACE. Print Sheet 1 and Sheet 2 double-sided for each participant. Prepare flipchart paper or a shared document for each group.
- [ ] `[Manual]` On 4 November 2026: record attendance privately, and keep the last ten minutes for the evaluation.
- [ ] `[Manual]` After the course day: return the attendance table to GRACE. After the deadline, return the completion table. Arrange the certificates.
- [ ] `[Agent]` After 4 November 2026: set `hs2026.status: delivered` and decide on `featured_edition`.
- [ ] `[Manual]` After 4 November 2026: check whether the reasoning of the participants changed, not only their satisfaction. Compare a sample of statements with the rubric. Use no personal data in this repository.

## FS 2027

- [ ] `[Manual]` Request the confirmed schedule, venue, course link, rules, evaluation link, and deadline from GRACE.
- [ ] `[Agent]` Enter only confirmed facts in `data/editions.yml`. Keep `null` for the rest.

## Materials

- [ ] `[Shared]` Run `npm run handouts:build` for Sheet 1, Sheet 2, and the risk worksheet. Open each PDF and check that each page fits. Commit the generated files.
- [ ] `[Shared]` Rehearse the course day deck (`contents/slides/06-day.qmd`) on the room screen. Check the countdown and the follow mode.
- [ ] `[Shared]` Check the seven decks for legibility and accessibility. Then offer PDF versions.
- [ ] `[Agent]` Run veraPDF on the handouts (`quarto install verapdf`) to validate PDF/UA-1.
- [ ] `[Shared]` Decide whether to self-host the IBM Plex fonts instead of loading them from Google Fonts.
- [ ] `[Agent]` Check the IEA 2026 update of the data center figures against the IEA report itself. Only then add a dated note to Lens 1. Keep the 2025 figures.

## GitHub and Zenodo

- [x] `[Manual]` Enable GitHub Pages with the source **GitHub Actions**.
- [x] `[Shared]` Enable Dependabot alerts and security updates, secret scanning, and push protection.
- [x] `[Manual]` Merge PR #1. The published site must come from `main`, so that the reuse guide matches a fresh clone.
- [x] `[Shared]` Restrict the `github-pages` environment to the `main` branch.
- [ ] `[Shared]` Protect the `main` branch. For one maintainer: require a pull request and passing checks, 0 approvals.
- [ ] `[Shared]` Enable CodeQL default setup for GitHub Actions.
- [ ] `[Manual]` Enable the Zenodo-GitHub integration. Add the DOI badge and a `doi` key to `CITATION.cff` after the first release. Do not invent a DOI.
- [ ] `[Agent]` Remove the exclusion for `https://maehr.github.io/stochastic-parrots-and-beyond` from `.lycheerc.toml` after the first deployment.

## Validation

Run these commands before you push:

| Command                  | Purpose                                    |
| ------------------------ | ------------------------------------------ |
| `npm run check`          | Formatting, lint, types, and tests         |
| `npm run lychee-check`   | Links                                      |
| `npm run handouts:build` | Rebuild the handouts after a source change |
| `npm run schedule:build` | Rebuild the timetable files                |
| `npm run site:build`     | Full build with the Reveal.js decks        |
