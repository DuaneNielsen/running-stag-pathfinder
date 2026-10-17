// Fetches the Frontier binary with the beta token when it is not cached yet. The download is mise's tool stub
// (bin/frontier.stub names the per-platform URLs, checksums and the Authorization header); this only starts it.
export function register(on, options) {
  on('session.start', async ($, e, next) => {
    const root = $.plugin.root
    $.process.run([root + '/bin/mise', 'tool-stub', root + '/bin/frontier.stub', '--help'],
      { env: { FRONTIER_TOKEN: String(options.beta_token) }, timeoutMs: 600000 })
      .then(r => $.ui.toast(r.exitCode === 0 ? 'Frontier is ready' : 'Frontier download failed: ' + r.stderr.trim().split('\n').pop().slice(0, 120), { timeoutMs: 8000 }))
      .catch(err => $.ui.toast('Frontier download failed: ' + String(err.message ?? err).slice(0, 120), { timeoutMs: 8000 }))
    return next(e)
  })
}
