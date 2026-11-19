import argparse, json
from collections import defaultdict, Counter

DEFAULT_MODULI = (840, 1680, 2520, 4200, 8400, 9240, 12600, 18480, 27720, 55440)


def analyze(path, moduli=DEFAULT_MODULI, min_samples=20):
    data = json.load(open(path))
    records = data['records']
    out = {}
    for modulus in moduli:
        bins = defaultdict(list)
        for n, u, kind, p, q, source in records:
            bins[n % modulus].append((u, kind, source))
        pure_route = pure_gate = large = covered = 0
        examples = []
        class_max = {}
        for residue, values in bins.items():
            if len(values) < min_samples:
                continue
            large += 1
            covered += len(values)
            routes = Counter(v[1] for v in values)
            gates = Counter(v[0] for v in values)
            if len(routes) == 1:
                pure_route += 1
            if len(gates) == 1:
                pure_gate += 1
            class_max[residue] = max(v[0] for v in values)
            top_kind, top_count = routes.most_common(1)[0]
            purity = top_count / len(values)
            if purity >= 0.95:
                examples.append((residue, len(values), top_kind, purity, class_max[residue]))
        out[modulus] = {
            'large_classes': large,
            'samples_in_large_classes': covered,
            'pure_route_classes': pure_route,
            'pure_gate_classes': pure_gate,
            '95pct_route_examples': sorted(examples, key=lambda z: (-z[3], -z[1]))[:20],
            'max_of_class_max_u': max(class_max.values()) if class_max else None,
        }
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('json')
    ap.add_argument('--min-samples', type=int, default=20)
    args = ap.parse_args()
    print(json.dumps(analyze(args.json, min_samples=args.min_samples), indent=2))
