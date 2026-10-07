# Automation Deal Profit Gate — Lite

Turn an automation brief into a structured intake, missing requirements, a basic risk checklist and PASS / REVIEW / SKIP triage. **Free • v1.0.0 • MIT**

Lite helps you identify what needs clarification before deeper assessment. Its PASS never approves a price or deployment. The complete deterministic economics and delivery workflow is in Pro; see [edition boundaries](EDITIONS.md).

## Install

```sh
npx skills add youyipeng/ai17-profit-gate-lite --skill ai17-profit-gate-lite
```

Or download the [v1.0.0 release](https://github.com/youyipeng/ai17-profit-gate-lite/releases/tag/v1.0.0) and place `skills/ai17-profit-gate-lite` in your agent's skill directory. Consult your agent's own installation instructions. The skill format is agent-neutral; local script examples require Python 3.9+.

## Use

Ask your agent: "Use ai17-profit-gate-lite to review this automation brief and list the three most useful clarifications." Include your brief as data. Your agent performs free-text normalization. The optional local script consumes that structured JSON.

```sh
python skills/ai17-profit-gate-lite/scripts/triage.py skills/ai17-profit-gate-lite/examples/review-input.json
```

Expected: REVIEW with missing volume, access, data boundary, acceptance, owners, deadline and budget. [PASS](skills/ai17-profit-gate-lite/examples/pass-output.json), [REVIEW](skills/ai17-profit-gate-lite/examples/review-output.json) and [SKIP](skills/ai17-profit-gate-lite/examples/skip-output.json) examples are invented demonstrations, not customer stories.

## Evidence and limitations

See the [internal benchmark summary](BENCHMARK.md) for Pro-related candidate results and small-sample limitations. Lite has not been evaluated with those metrics. Agent output needs evidence review; no guarantee of project feasibility or profit is offered.

## Pro availability

Pro launch price: US$29 once. Gumroad Bundle: US$49 once. Paid storefront publication is pending account access. No purchase URL is claimed until verified. The [release status](RELEASE-STATUS.json) records actual channel state.

## Privacy and support

The local Lite script sends no data over a network, reads only your supplied JSON, and prints its result. Your AI agent/provider has its own privacy and cost policies. Redact credentials and unnecessary client data. Report ordinary bugs in [GitHub Issues](https://github.com/youyipeng/ai17-profit-gate-lite/issues); do not post confidential briefs. See [Security](SECURITY.md), [Privacy](PRIVACY.md), [Limitations](LIMITATIONS.md) and [Changelog](CHANGELOG.md).

MIT permits commercial use and redistribution of Lite. It does not grant rights to separate Pro files, private implementation, trademarks, or unpublished data.
