import csv
import math

INPUT_FILE = "cones.csv"
BLUE_FILE = "blue_cones.csv"
YELLOW_FILE = "yellow_cones.csv"
CENTRELINE_FILE = "centreline.csv"


def load_cones(path):
    """Read cones.csv into a list of dicts with numeric x, y."""
    cones = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cones.append({
                "id": row["id"],
                "x": float(row["x"]),
                "y": float(row["y"]),
                "colour": row["colour"].strip().lower(),
            })
    return cones


def distance_from_origin(cone):
    return math.hypot(cone["x"], cone["y"])


def distance_between(a, b):
    return math.hypot(a["x"] - b["x"], a["y"] - b["y"])


def write_cones(path, cones):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "x", "y", "colour"])
        writer.writeheader()
        for c in cones:
            writer.writerow(c)


def nearest_yellow(blue_cone, yellow_cones):
    """Brute-force nearest neighbour. Fine for a few hundred/thousand cones."""
    best = min(yellow_cones, key=lambda y: distance_between(blue_cone, y))
    return best


def main():
    cones = load_cones(INPUT_FILE)

    # 1. Sort all cones by distance from origin
    cones.sort(key=distance_from_origin)

    # 2. Split by colour, keeping sorted order
    blue_cones = [c for c in cones if c["colour"] == "blue"]
    yellow_cones = [c for c in cones if c["colour"] == "yellow"]

    write_cones(BLUE_FILE, blue_cones)
    write_cones(YELLOW_FILE, yellow_cones)

    # 3. For each blue cone, find nearest yellow cone and compute midpoint
    midpoints = []
    for b in blue_cones:
        if not yellow_cones:
            break
        y = nearest_yellow(b, yellow_cones)
        mx = (b["x"] + y["x"]) / 2
        my = (b["y"] + y["y"]) / 2
        midpoints.append({
            "blue_id": b["id"],
            "yellow_id": y["id"],
            "mid_x": mx,
            "mid_y": my,
        })

    with open(CENTRELINE_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["blue_id", "yellow_id", "mid_x", "mid_y"])
        writer.writeheader()
        for m in midpoints:
            writer.writerow(m)

    print(f"Done. Wrote {len(blue_cones)} blue cones, {len(yellow_cones)} yellow cones, "
          f"and {len(midpoints)} centreline points.")


if __name__ == "__main__":
    main()