# Permanent Unit-Partner Classification Through 10^9

**Status:** exact finite classification on the audited corrected residual population; not a global theorem

The audited unit-partner computation through

\[
n\le10^9
\]

contains **195,271** residual primes after the corrected classical, hard-gate, and `n+1` / `n+4` shift reductions.

Of these:

- **195,270** have a unit-partner certificate with some `u <= 299`;
- exactly one fails all such bounded shifts:
  \[
  \boxed{n=2521}.
  \]

Any permanent unit-partner exception must in particular fail the search through `u <= 299`. Therefore, inside the audited population `n <= 10^9`, the only possible permanent exception is `2521`.

`PERMANENT_UNIT_PARTNER_EXCEPTION_2521.md` and `verify_2521_permanent_unit_partner_exception.py` settle that candidate completely: both the untwisted and twisted unit-partner branches fail for **every** admissible shift.

Hence:

\[
\boxed{
2521\text{ is the unique permanent unit-partner exception among the audited corrected residual primes }n\le10^9.
}
\]

This conclusion is finite but exact. It does not assert that no additional permanent exception exists above `10^9`.

## Why the classification is logically valid

The argument is one-way and requires no assumption about larger shifts for the other 195,270 primes:

- a prime already possessing a certificate at `u <= 299` cannot be a permanent failure;
- `2521` is the only bounded failure;
- an independent finite argument proves that `2521` fails at all shifts.

Thus the permanent-exception classification through `10^9` follows directly from the audited certificate database plus the exact `2521` proof.
