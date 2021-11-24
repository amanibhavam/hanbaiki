package boot

import "github.com/defn/boot"

cfg: "boot": boot.#Boot & {
	module: "github.com/amanibhavam/hanbaiki"
	version: _boot.version
}