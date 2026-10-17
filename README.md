# running-stag pathfinder

Scratch repo for one question: on a clean Windows runner (and a "detuned" one with no Node or Bun), can a Claude Code
mod launch mise (`mise.cmd`) and fetch a Bearer-gated binary when a plugin loads? The workflow in `.github/workflows`
packs a real small executable into a local gated release and runs the install end to end. The plugin under `plugin/`
is a copy of `running-stag` from a private monorepo; this repo exists only to run Windows CI.
