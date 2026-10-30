# Stochastic Parrots and Beyond

Open educational resources for **Stochastic Parrots and Beyond: Normative Dimensions of Generative AI**. This one-day workshop is for doctoral candidates and postdocs at the University of Basel.

[![GitHub issues](https://img.shields.io/github/issues/maehr/stochastic-parrots-and-beyond.svg)](https://github.com/maehr/stochastic-parrots-and-beyond/issues)
[![Content license](https://img.shields.io/badge/content%20license-CC%20BY%204.0-blue.svg)](LICENSE-CCBY.md)
[![Liberating Structures adaptations](https://img.shields.io/badge/LS%20adaptations-CC%20BY--SA%204.0-blue.svg)](LICENSE-CCBYSA.md)
[![Code license](https://img.shields.io/badge/code%20license-AGPL--3.0-blue.svg)](LICENSE-AGPL.md)

**Course website: <https://maehr.github.io/stochastic-parrots-and-beyond/>**

## Overview

Researchers use generative AI more and more. Its environmental costs, training data, labor conditions, representations, commercial incentives, and governance often get separate treatment. This workshop puts them together.

Participants examine text and image generators through four analytical lenses:

1. Stochastic Parrots: scale and environment.
2. Representation and Displacement.
3. Lifecycle and labor: materiality and extraction.
4. Political economy: power and markets.

In Lens groups, participants apply the guiding questions of one lens to their own Research Uses. Then they use two blocks of the Liberating Structures [Panarchy](https://www.liberatingstructures.com/panarchy) to find feasible changes in their own research settings. Each participant leaves with an individual Action Plan. The aim is a transparent and defensible position on generative AI in research. The aim is not a list of permitted and forbidden tools.

## Who This Is For

| Reader                             | Start here                                                                                                                                                                                                               |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A participant in a Basel edition   | The [edition pages](https://maehr.github.io/stochastic-parrots-and-beyond/contents/editions/hs2026.html) give the date, the venue, and the preparation.                                                                  |
| A student who studies on their own | The [four lenses](https://maehr.github.io/stochastic-parrots-and-beyond/contents/syllabus.html) and the [literature](https://maehr.github.io/stochastic-parrots-and-beyond/contents/literature.html).                    |
| A teacher who reuses the course    | The [reuse guide](https://maehr.github.io/stochastic-parrots-and-beyond/documentation/reuse.html) and the [facilitator guide](https://maehr.github.io/stochastic-parrots-and-beyond/contents/panarchy-facilitator.html). |

## Editions

One set of teaching materials serves all editions. The practical facts differ for each edition.

| Edition              | Status                              |
| -------------------- | ----------------------------------- |
| Autumn semester 2026 | Confirmed                           |
| Spring semester 2027 | Planned. Details are not confirmed. |

The edition pages on the website show the date, the venue, and the rules for each edition. The file `data/editions.yml` is the single source for these facts. The [official University of Basel course listing](https://fortbildung.unibas.ch/courses/hauptfachbereich/dissertation--phd/stochastic-parrots-and-beyond-normative-dimensions-of-generative-ai-303499) overrides this repository.

This site is a course companion. It does not take registrations and does not award credits. The Graduate Center (GRACE) of the University of Basel does both.

## What the Repository Contains

| Material               | Purpose                                                                        |
| ---------------------- | ------------------------------------------------------------------------------ |
| Four lesson pages      | One page for each lens: concepts, evidence, a case, and four guiding questions |
| Seven Reveal.js decks  | Orientation, four lenses, Panarchy, and a running deck for the course day      |
| Two printable sheets   | Research Use Card, Panarchy Chart, Opportunities & Barriers, and Action Plan   |
| Facilitator guide      | The course day minute by minute, with the trainer timeline                     |
| Use statement template | A Markdown and Word template for the follow-up assignment                      |
| Reference list         | One verified BibTeX file for every cited work                                  |

## Repository Structure

| Path                 | Purpose                                                          |
| -------------------- | ---------------------------------------------------------------- |
| `index.qmd`          | Home page of the website                                         |
| `contents/`          | Course pages: description, syllabus, assignments, literature     |
| `contents/editions/` | One page for each edition                                        |
| `contents/lenses/`   | One lesson page for each lens                                    |
| `contents/slides/`   | Reveal.js slide decks                                            |
| `contents/handouts/` | Handout sources. Each source is also the accessible web version. |
| `assets/handouts/`   | Printable PDFs, editable files, and diagrams                     |
| `assets/cases/`      | Original figures for the cases                                   |
| `data/editions.yml`  | The single source for the facts of each edition                  |
| `data/schedule.yml`  | The single source for the timetable of the course day            |
| `references.bib`     | BibTeX entries for every cited work                              |
| `documentation/`     | Guidance for teachers who reuse the course                       |
| `test/`              | Tests for the edition data, the links, and the privacy rules     |

## Build the Site Locally

You need these tools:

- Node.js 24 or later.
- [uv](https://docs.astral.sh/uv/).
- [Quarto](https://quarto.org/).

Do these steps:

1. Clone the repository: `git clone https://github.com/maehr/stochastic-parrots-and-beyond.git`.
2. Go into the directory: `cd stochastic-parrots-and-beyond`.
3. Install the Node.js tools: `npm install`.
4. Install the Git hooks: `npm run prepare`.
5. Install the Python tools: `uv sync`.
6. Start the preview: `npm run preview`.

The preview server reloads the site after each change. The [reuse guide](documentation/reuse.qmd) explains the build, the checks, and the publication.

## Reuse

You can copy, change, and teach these materials. Give credit, and keep the license of each part.

| Content                                     | License                                                   |
| ------------------------------------------- | --------------------------------------------------------- |
| Original course text, figures, and handouts | [CC BY 4.0](LICENSE-CCBY.md)                              |
| Material adapted from Liberating Structures | [CC BY-SA 4.0](LICENSE-CCBYSA.md)                         |
| Code, configuration, and build scripts      | [AGPL 3.0](LICENSE-AGPL.md)                               |
| Third-party material                        | The terms of the owner, stated where the material appears |

Material adapted from Liberating Structures must keep CC BY-SA 4.0. Do not relicense it as CC BY. The repository contains no copyrighted readings. The literature page links to lawful copies.

## Citation

Cite these materials as described in [CITATION.cff](CITATION.cff). GitHub shows a citation in APA and BibTeX format in the sidebar of the repository.

## Support

Use a public channel when you can, so that other people find the answer.

| Type                                   | Channel                                                                        |
| -------------------------------------- | ------------------------------------------------------------------------------ |
| Content corrections and broken links   | [GitHub Issues](https://github.com/maehr/stochastic-parrots-and-beyond/issues) |
| Problems with the website or the build | [GitHub Issues](https://github.com/maehr/stochastic-parrots-and-beyond/issues) |
| Security problems and personal data    | See [SECURITY.md](SECURITY.md)                                                 |
| Registration, attendance, and credits  | The Graduate Center (GRACE), University of Basel. Not GitHub.                  |

## Contributing

Corrections, better sources, and reuse reports are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before you open a pull request.

## Authors and Acknowledgment

- **Laura Wagner**: course design and materials. [Website](https://laurajul.github.io/), [ORCID 0009-0003-4244-6342](https://orcid.org/0009-0003-4244-6342).
- **Moritz Mähr**: course design and materials. [Website](https://moritzmaehr.ch/), [ORCID 0000-0002-1367-1618](https://orcid.org/0000-0002-1367-1618).

The workshop is part of the Transferable Skills program of the Graduate Center (GRACE), University of Basel.

Henri Lipmanowicz and Keith McCandless created [Liberating Structures](https://www.liberatingstructures.com/). The Panarchy materials in this repository adapt their methods under [CC BY-SA 4.0](https://www.liberatingstructures.com/cc-license).

The repository started from the [open-research-data-template](https://github.com/maehr/open-research-data-template). The [All Data Are Local](https://github.com/maehr/all-data-are-local) course site is the model for its structure and design.

## License

Original course content is released under [CC BY 4.0](LICENSE-CCBY.md). Material adapted from Liberating Structures is released under [CC BY-SA 4.0](LICENSE-CCBYSA.md). Code is released under [AGPL 3.0](LICENSE-AGPL.md).
