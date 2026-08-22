# Writing

How this project writes prose, for humans and agents alike. It governs
`README.md`, commit messages, docstrings, and source comments — every
surface a reader reaches.

For environment setup, the gates, and pull request workflow, see
[CONTRIBUTING.md](CONTRIBUTING.md).

## Voice

One voice, wherever it appears. A docstring says what a caller may rely
on; prose says what happens. Both are present tense, lead with the thing
being described, and stop. Why it was built that way belongs in the
commit message, which is timestamped and attached to the diff.

The most useful editing operation is deleting the introductory sentence.

Lead with verbs and name concrete things. Put identifiers in backticks.
Prefer short declarative sentences, one operational fact each. Do not
explain Python to Python developers; do explain this project's
semantics.

Type annotations describe shape. Documentation describes meaning. A
sentence that restates a signature has said nothing.

Use MUST, SHOULD, and MAY only where the normative sense is meant. Say
what actually happens rather than that something is "supported".

| Instead of                       | Prefer                            |
| --------------------------------- | ---------------------------------- |
| "We added…"                      | "`Query.hello` now returns…"      |
| "New and improved"               | "`Settings.port` now…"            |
| "powerful", "seamless"           | state the capability              |
| "easily", "simply", "just"       | omit                              |
| "simple", "obvious", "intuitive" | omit                              |
| "robust"                         | name the failure that is handled  |
| "comprehensive"                  | name what is covered              |
| "production-ready"               | state the guarantee               |
| "optimized", "blazingly fast"    | give the magnitude                |
| "various fixes"                  | name the components               |
| "under the hood"                 | omit unless observable            |
| "please note that", "note that"  | state the fact                    |
| "leverage", "utilize"            | "use"                             |
| "delve into"                     | "read", or omit                   |
| "best practices"                 | name the practice                 |
| "in order to"                    | "to"                              |

## Who you are writing for

The default reader is fluent in Python and new to this project. They can
read a signature; they cannot guess this project's semantics. Serve them
first — this repo does not have a distinct "advanced" audience to layer
material on top of.

Rules that follow:

- **Second person, present tense, active.** "You send a query", not "A
  query is sent". Address the reader who is doing the thing.
- **Concept before API surface.** Open by saying what the route or
  resolver *does* for the reader. The signature is the last detail they
  need, not the first.
- **Say when they can stop.** Lead with the default and the reassurance.
  Let a skimmer leave after one paragraph.
- **Progressive disclosure.** Order by how many readers need it: the
  common call, then the one argument a few will tune.
- **Name the trade-off.** If a call costs something, say so, and say
  what it buys. State it; do not sell it.

## README

A README is the shortest path from "what is this?" to competent use, not
the project's autobiography.

The first sentence is a contract. It says what abstraction the reader
has been handed, concretely enough to tell this package apart from a
neighbouring one.

Get to a runnable command before anything the reader can skip.

State the minimum Python version in prose, not only as a fact buried in
`pyproject.toml`. `requires-python` there is the authority; the README
must agree with it.

Name the distribution and the import separately where they differ: `pip
install learning-fastapi`, `import app`. There is no console script.

Examples are executable, not illustrative fiction. See
[Documented examples that run](#documented-examples-that-run) for which
blocks are executed and how to write one that qualifies.

State defaults explicitly — defaults are API.

Headings stay conventional and stable, because people deep-link them.

## Documented examples that run

Examples in this repo are tests, wherever the mechanism below reaches
them. This section is the contract for writing one the test suite can
actually see.

**A fence tag is cosmetic. Only a `>>> ` prompt executes.** A block
written as

    ```python
    app.state
    ```

is prose that looks like a test. Nothing collects it, nothing runs it,
and it can be wrong for years. The same block written with a prompt is a
test:

    ```python
    >>> app.state
    ```

This is the single most expensive mistake available when editing
documentation, because removing the prompts leaves a green test suite
and a silently deleted test. When editing a file that contains examples,
count the prompts before and after.

**The fence tag is `python`.** Not `pycon`, not bare — kept uniform even
though no markdown page in this repo is doctested; see below.

**Where examples run, here.** `addopts` in `pyproject.toml` sets
`--doctest-modules`, and `testpaths` is `src` and `tests` — pytest
collects doctests only from `.py` files under those two paths. There is
no `--doctest-glob` addopt, so `README.md` and any other markdown file
are never scanned for `>>> ` blocks regardless of `testpaths`; adding
`>>> ` to `README.md` would not execute it. `doctest_optionflags`
sets `ELLIPSIS` and `NORMALIZE_WHITESPACE` globally, so `...` elides
variable output and whitespace differences do not fail a comparison.

**No `doctest_namespace` fixture is configured.** There is no
`conftest.py` in this repo, so a doctest block may use only names it
imports or defines itself — nothing is injected automatically. Add a
`conftest.py` with a `doctest_namespace` fixture if a doctest needs one.

**`# doctest: +SKIP` is not permitted.** It is a workaround that tests
nothing.

**Do not downgrade a doctest to a non-executed block to make it pass.**
An unprompted fence or a `.. code-block::` does not run. If an example
cannot pass, fix the example or fix the code.

**A public function or method must carry a working doctest.** Use the
NumPy `Examples` section:

    Examples
    --------
    >>> from app.app import app
    >>> from starlette.testclient import TestClient
    >>> client = TestClient(app)
    >>> client.get("/").status_code
    200

**Room to grow.** Extending doctest collection to `README.md` or other
markdown needs a configuration change here — add `README.md` to
`testpaths` and set `--doctest-glob` (or an equivalent addopt) in
`pyproject.toml`. Neither is set, so a prompted block added to markdown
does not run until that change lands.

## Docstrings

The prime directive: never restate the type. The annotation is the
source of truth; the docstring carries what the annotation cannot.

Document instead the dimensions the type system cannot encode:

- **Mutation.** What it changes in place.
- **Ownership.** What the caller must close, release, or keep alive.
- **Ordering.** Whether results come back in a guaranteed order.
- **Timing.** What has finished by the time the call returns, or the
  awaitable resolves.
- **Failure.** Which exceptions are raised and what triggers each.
- **Idempotence.** Whether calling twice does anything the second time.
- **Concurrency.** Whether calls are coalesced, queued, or independent,
  and whether the object is thread-safe, process-safe, or fork-safe.
- **Units and ranges.** What a number means and what values are
  accepted.
- **Boundary behaviour.** What zero, empty, and the maximum do.
- **Platform.** Behaviour that differs by operating system or dependency
  version.
- **Security boundary.** What is executed, and what is only read.

The first sentence stands alone; tooling truncates there. PEP 257
applies: triple double quotes, an imperative one-line summary ending in
a period, a blank line before any extended description. Do not repeat an
introspectable signature.

`pydocstyle` is configured for the `numpy` convention in `pyproject.toml`
and enforced by `ruff check` — one docstring dialect, enforced by the
linter rather than relitigated in review.

### Classes with fields

`NamedTuple` and dataclasses document every field in an `Attributes`
section:

    class RouteCase(NamedTuple):
        """One request/response pair a lesson exercises.

        Attributes
        ----------
        path : str
            Route path the request targets.
        expected_status : int
            Status the handler is expected to return.
        """

A type says how a field is shaped, not what it holds. Describing each
one keeps that meaning next to the code, and anything that renders the
class — autodoc, a REPL, an editor tooltip — has a description to show
instead of a bare name.

## Sync and async execution

A `def` path operation runs through Starlette's `run_in_threadpool` —
off the event loop, in a worker thread. An `async def` path operation
runs directly on the loop. `hello_world` is the `def` case.

Strawberry resolvers get no such dispatch: a `def` resolver — like
`Query.hello` — runs inline on the event loop, exactly where an `async
def` resolver would. A slow synchronous resolver blocks every other
request the loop is holding.

State which of the two applies when a docstring or comment documents a
handler's blocking behaviour — the Concurrency and Timing dimensions
under [Docstrings](#docstrings) are exactly where that fact belongs.

## Source comments

A comment ships only if it passes all three gates. Fail any: delete or
rewrite. Borderline: delete — borderline means the information is
reconstructible, which is what makes deletion cheap.

**Loss.** Three years from now, would losing this cost a maintainer real
time rediscovering intent, an invariant, a constraint, or a failure mode
the code and tests do not already make obvious?

**Elite.** Would SQLite, Redis, the Go standard library, or CPython write
this comment, at this length? Those projects state the constraint and
stop. They do not argue with an imagined objector.

**Upkeep.** Will it stay true without maintenance? A comment that
hand-syncs a value the code owns — a count, an offset, a line reference,
a duplicated constant — is false the first time that value moves.

### Ceiling

One or two lines. A comment reaching four is either carrying several
facts, in which case split it, or arguing, in which case cut it to the
fact.

Rationale, alternatives weighed, and the story of how the code got here
belong in the commit message: timestamped, attached to the exact diff,
and free to maintain.

A comment often holds both a constraint and the deliberation that found
it. Keep the constraint, cut the deliberation. "Runs at most once per
second" survives; "this is the right trade for now" does not.

### Keep

- Why over how: upstream quirks, protocol and compatibility constraints,
  performance tradeoffs still part of the contract.
- Invariants, preconditions, ordering, lifetime, and concurrency
  requirements that types and tests cannot express.
- Code that looks wrong but is not, so a later cleanup does not
  reintroduce the bug.
- A high-level sketch of an algorithm whose local operations do not
  reveal the whole.

### Delete

- Narration of the next lines; code translated into English.
- Restated names, types, defaults, or control flow.
- Values duplicated from the code and hand-synced.
- Justification, hedging, or apology for a choice.
- Speculation about future requirements.
- History version control already holds, including commented-out code.
- Ticket and issue numbers. They say nothing to a reader without tracker
  access, and they rot when the tracker moves. Unfinished work goes in
  the tracker, not the source.
- Transient observations — "currently", "for now", "the latest release"
  — that go stale with no nearby edit.

### The upkeep gate in practice

It reaches values that track our own code. It does not reach frozen
external facts.

Bad (Delete):

    # There are 2 routes registered on this app.

Good (Keep):

    # CPython < 3.11 has no ExceptionGroup, so this branch stays.

### Documentation exception

Minimal usage examples, and parameter, return, and raises entries on
public API are exempt from the loss gate — they serve the caller, not
the maintainer. They are exempt from nothing else. Ceiling: a good man
page entry.

NumPy-style `Parameters`, `Returns`, and `Attributes` sections and
executable doctests fall under this exception — autodoc ships every
field whether or not it is described, and a doctest that runs is also a
test.

## Terminology and capitalization

Pick the domain noun and keep it: this project says **route** for the
HTTP handler, **resolver** for a GraphQL field method, and **endpoint**
for the URL path either is mounted at — not three words for one thing in
the same paragraph.

Do not write counts into prose — how many routes exist, how many tests
there are. They go stale silently; a count that guards an invariant
belongs in code, not prose.

## Markdown

Prose wraps at 80 columns. Table rows, badge lines, and long links are
exempt, because breaking them harms rendering. A pull request or issue
body does not wrap at all: GitHub renders a single newline as a space in
a file and as a line break in a comment, so a wrapped comment body
arrives as ragged stubs.

GitHub alert blocks — `> [!NOTE]`, `> [!WARNING]` — render as literal
text outside GitHub, so reserve them for at most one load-bearing
warning per document.

Do not use a local absolute path or an email address in anything
published.

## Code blocks

Code blocks are paste-and-run units: pasting one block runs exactly one
intended action. Executed examples are exempt — the test suite runs
them, nobody pastes them.

- **One command per block.** Multiple steps may share a block only when
  explicitly chained with `&&`, `;`, or `\` continuations — the chain is
  then one logical command.
- **Explanations go in prose above the block**, never as `#` comments
  inside it.
- **Command menus are per-command blocks with prose lead-ins**, not
  tables.
- **Shell commands use the `console` tag with a `$ ` prefix.** This
  separates interactive commands from scripts and enables prompt-aware
  copy.
- **Split long commands with `\`** — one flag or flag+value pair per
  indented continuation line, positional arguments last.

Good — show the last ten commits as a graph:

```console
$ git log \
    --max-count=10 \
    --graph \
    --oneline
```

Bad:

```console
# Show the last ten commits as a graph
$ git log --max-count=10 --graph --oneline
```

## Commits

    Scope(type[detail]): concise description

    why: Explanation of necessity or impact.

    what:
    - Specific technical changes made
    - Focused on a single topic

Keep the subject to 50 characters or fewer, excluding any trailing
`(#NN)` pull request reference, and wrap body lines at 72. Separate the
`why:` and `what:` blocks with a blank line. Use the imperative mood
("Add", "Fix" — not "Added", "Fixed"). Mark a breaking change with a
`BREAKING:` line in the body. Subjects are plain English — no
repo-internal shorthand a reader of `git log --oneline` would need to
decode.

Routine maintenance commits drop the colon and take a capitalised
description, which is what distinguishes them at a glance in `git log
--oneline`:

    py(deps[dev]) Bump dev packages
    .tool-versions(uv) uv 0.12.3 -> 0.12.5

Everything that changes behaviour keeps the colon.

Common types:

- **feat**: New features or enhancements
- **fix**: Bug fixes
- **refactor**: Code restructuring without functional change
- **docs**: Documentation updates
- **chore**: Maintenance (dependencies, tooling, config)
- **test**: Test-related updates
- **style**: Code style and formatting
- **ci**: Workflow and pipeline changes
- **py(deps)**: Dependencies
- **py(deps[dev])**: Dev dependencies
- **.tool-versions(tool)**: Pinned tool version bumps (`uv`, `just`)
- **ai(rules[AGENTS])**: AI rule updates

Example:

    app(feat[graphql]): Add a mutation to the schema

    why: Exercise a write path alongside the existing query.

    what:
    - Add a `setGreeting` mutation to `Query`
    - Add a test exercising it through `TestClient`

For a multi-line message, use a heredoc so the formatting survives:

```console
$ git commit -m "$(cat <<'EOF'
Scope(feat[detail]): Concise description

why: Explanation of the change.

what:
- First change
- Second change
EOF
)"
```

## Slop prevention

Treat AI slop as review-hostile noise, not as proof that text or code is
wrong. The goal is to maximise information density.

- **AI signatures.** No "Generated by", no conversational filler, no
  unexplained emoji, no tool metadata.
- **Brittle references.** No hard-coded line numbers, fragile file
  counts, dated "as of" claims, bare SHAs, or local absolute paths —
  unless they are strict evidentiary artefacts such as a benchmark log.
- **Diff narration.** Do not restate what moved, was renamed, or was
  removed in anything the reader holds alongside the diff: code,
  docstrings, README, or a pull request description. The diff and the
  commit message already carry it.
- **Branch-internal narrative — the published-release test.** Before
  mentioning an old name, an old behaviour, or a bug in anything shipped
  (docstring, README, comment), ask: did a user of the most recently
  published release ever experience it? This project has not published
  a release, so the answer is always no — describe only the current
  state, and put the history in the commit message instead.
- **Low-value scaffolding.** No ownerless TODOs, unused
  future-proofing, debug artefacts, or defensive wrappers around failure
  modes nothing can reach.
- **Prose inflation.** The diction table under [Voice](#voice) governs;
  replace an inflated word with a concrete description of behaviour,
  constraints, or trade-offs.
- **Coded labels.** Write rules and findings as plain imperatives. No
  `[R1]`, `Option B`, or any index a reader has to decode.
- **Durable source links.** Link to a pinned revision, never to `main`
  — a `blob/main/…` link rots silently as the file moves and the anchor
  lands on unrelated code while still resolving. Prefer a release tag
  once one exists; until then, a 7-character commit SHA reachable from
  `main` is durable enough. Never link a pull-request-head SHA — it can
  be rebased away. Line anchors (`#L120-L145`) are safe only on a
  pinned ref.

Preserve the "why". Never delete a comment documenting an invariant, a
protocol constraint, a platform quirk, or an upstream workaround — those
are the facts [Source comments](#source-comments) keeps, and every other
comment is judged by it.
