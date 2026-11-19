import Lake
open Lake DSL

package «ErdosStrausLean» where

@[default_target]
lean_lib ErdosStrausLean where

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.33.1"
