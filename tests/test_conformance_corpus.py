"""Corpus-level tests for the output-conformance hook.

The unit tests in `test_check_conformance.py` use a four-section fixture. That
is not enough to catch the failure this file exists to pin: a recognition rule
that looks fine on one hand-built template can still misfire on 110 real ones.
Both tests below run the hook over every shipped template.

They are cheap — a few hundred `evaluate` calls, each an O(n·m) table over
8–30 records — and finish in a couple of seconds.
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "skel"))   # so the hook finds md_shape
_spec = importlib.util.spec_from_file_location(
    "check_output_conformance", ROOT / "scripts" / "skel" / "check_output_conformance.py")
checker = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(checker)
import md_shape  # noqa: E402

TEMPLATES = sorted(ROOT.glob("pm-*/skills/*/template.md"))

# Real markdown in this repo that is emphatically NOT any skill's deliverable.
# Several are long and heavily sectioned, which is exactly the shape that fooled
# the "any pair counts" recognition rule.
UNRELATED = ["README.md", "CLAUDE.md", "TASKS.md", "docs/SKILL-STANDARD.md",
             "docs/output-language.md"]

_BLOCK = {"para": "Du texte ordinaire.", "list": "- un élément",
          "quote": "> une citation", "code": "```\nx\n```"}


def _render(sections, skip=None, translate=True):
    """Turn shape records back into a markdown document.

    With `translate=True` the headings are replaced by French placeholders, so
    the document shares the template's shape and none of its words — the case
    the whole design exists for.
    """
    out = ["# Document"]
    for i, s in enumerate(sections):
        if i == skip:
            continue
        out.append("%s %s" % ("#" * s.depth,
                              "Section numéro %d" % i if translate else s.text))
        for b in s.blocks:
            if b.startswith("table:"):
                n = int(b.split(":")[1])
                out.append("| " + " | ".join(["cellule"] * n) + " |")
                out.append("|" + "|".join(["---"] * n) + "|")
            else:
                out.append(_BLOCK[b])
        out.append("")
    return "\n".join(out)


def _shape(path):
    return md_shape.collapse_repeats(
        md_shape.parse_sections(path.read_text(encoding="utf-8")))


def _check(tmp_path, template, text):
    doc = tmp_path / "doc.md"
    doc.write_text(text, encoding="utf-8")
    return checker.evaluate(
        {"tool_name": "Write", "tool_input": {"file_path": str(doc)}}, str(template))


def test_the_corpus_is_all_here():
    # A glob that silently matched nothing would make both tests below vacuous.
    assert len(TEMPLATES) == 110


def test_no_unrelated_repo_document_is_ever_flagged(tmp_path):
    """The hook fires on every `.md` write while a PM skill is loaded, with no
    path filter. Blocking an unrelated file means telling the model to add
    "TAM — Total Addressable Market" to the user's meeting notes, so the only
    acceptable count here is zero."""
    docs = {name: (ROOT / name).read_text(encoding="utf-8") for name in UNRELATED}
    flagged = []
    for template in TEMPLATES:
        for name, text in docs.items():
            code, _ = _check(tmp_path, template, text)
            if code != 0:
                flagged.append("%s vs %s" % (template.parent.name, name))
    assert flagged == [], "%d/%d unrelated documents flagged: %s" % (
        len(flagged), len(TEMPLATES) * len(docs), flagged[:10])


def test_deleting_one_section_reports_exactly_one_missing(tmp_path):
    """No cascade: one omitted section must not drag the rest of the sequence
    out of register and report six. The *name* the message offers is only a
    candidate (see `_describe`), so only the count is asserted here."""
    wrong = []
    for template in TEMPLATES:
        want = _shape(template)
        if len(want) < 2:
            continue
        for k in range(len(want)):
            code, msg = _check(tmp_path, template, _render(want, skip=k))
            # one "level-N" per reported section
            if code != 2 or msg.count("level-") != 1:
                wrong.append("%s #%d -> code=%d, %d reported"
                             % (template.parent.name, k, code, msg.count("level-")))
    assert wrong == [], "%d trials reported the wrong number: %s" % (
        len(wrong), wrong[:10])


def test_a_french_market_sizing_memo_is_recognised_and_silent(tmp_path):
    """The shipped `market-sizing` template, every heading translated and no
    markers of any kind left in the document, must still be recognised as the
    deliverable and pass."""
    template = ROOT / "pm-strategy" / "skills" / "market-sizing" / "template.md"
    memo = """# Dimensionnement du marché : signature électronique pour PME

## Définition du marché
- **Problème et besoin client :** signer des contrats à distance.
- **Périmètre géographique :** Union européenne.
- **Exclusions :** grands comptes.

## TAM — Marché total adressable
- **Descendante :** 24 M de PME × 15 €/mois × 12 = **4,3 Md€**
- **Ascendante :** 2,1 M d'entreprises équipées × 180 € = **378 M€**
- **Réconciliation :** écart d'équipement → **TAM actuel : 1,2 Md€**

## SAM — Marché adressable desservi
- **Part desservie :** PME de 10 à 250 salariés.
- **Contraintes :** langue, canal indirect, offre milieu de gamme.
- **SAM = 420 M€** (35 % du TAM)

## SOM — Marché obtenable
- **Atteignable sous 1 à 3 ans :** 18 M€
- **Base :** capacité commerciale actuelle.
- **SOM = 18 M€** (4 % du SAM)

## Synthèse
| Indicateur | Aujourd'hui | Projection 2–3 ans |
|------------|-------------|--------------------|
| TAM        | 1,2 Md€     | 1,6 Md€            |
| SAM        | 420 M€      | 600 M€             |
| SOM        | 18 M€       | 55 M€              |

## Moteurs de croissance et tendances
- Obligation de facturation électronique à partir de 2027.

## Hypothèses clés et risques
1. Taux d'équipement de 9 % — confiance : moyenne — à valider par : panel.
2. Prix moyen de 15 €/mois — confiance : haute — à valider par : grille tarifaire.

## Sources
| # | Source | Type | Année | URL / Référence | Utilisée pour |
|---|--------|------|-------|-----------------|---------------|
| 1 | Eurostat | base de données | 2025 | eurostat.ec.europa.eu | TAM descendant |
"""
    assert _check(tmp_path, template, memo) == (0, "")
